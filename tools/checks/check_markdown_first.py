#!/usr/bin/env python3
"""Lightweight Markdown-first content contract checks."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from collections import defaultdict
import os
from pathlib import Path
import re
import sys


DISCLAIMER_LIMIT = 8
SAFETY_TERMS = (
    "stop",
    "sharp",
    "worsening",
    "unsafe",
    "seek qualified",
)
EXCLUDED_SCOPE_TERMS = (
    "barbell",
    "deadlift",
    "olympic",
    "kettlebell",
    "plyometric",
    "sprint",
    "diagnose",
    "diagnosis",
    "rehab",
    "rehabilitation",
    "treat pain",
    "treating pain",
    "posture correction",
)
SUPPORT_FILENAMES = {
    "README.md",
    "SOURCES.md",
    "CONTRIBUTING.md",
    "CONTENT_LICENSE.md",
    "PROVENANCE.md",
}
RASTER_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SVG_EXTENSIONS = {".svg"}
ALLOWED_MEDIA_PURPOSES = {"equipment_identification", "key_movement_illustration"}
REQUIRED_PROVENANCE_FIELDS = (
    "asset_path",
    "asset_type",
    "media_purpose",
    "generator",
    "prompt_or_creation_notes",
    "created_date",
    "human_reviewer",
    "license_assertion",
    "source_inputs",
    "review_status",
    "page_refs",
    "notes",
)

REFERENCE_LINK_RE = re.compile(r"\[[^\]]+\]\[([A-Za-z0-9_.:-]+)\]")
REFERENCE_DEF_RE = re.compile(r"^\[([A-Za-z0-9_.:-]+)\]:\s+(\S+)\s*$", re.MULTILINE)
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
ROOT = Path(os.environ.get("GYMPRIMER_ROOT", Path(__file__).resolve().parents[2]))
SOURCES_INDEX = ROOT / "SOURCES.md"
PROVENANCE_INDEX = ROOT / "media/PROVENANCE.md"


@dataclass(frozen=True)
class Finding:
    path: Path
    code: str
    message: str

    def format(self) -> str:
        return f"{self.path}: {self.code}: {self.message}"


def iter_markdown_paths(paths: list[Path]) -> tuple[list[Path], list[str]]:
    markdown_paths: list[Path] = []
    errors: list[str] = []

    for path in paths:
        if not path.exists():
            errors.append(f"setup: missing path: {path}")
            continue
        if path.is_dir():
            markdown_paths.extend(sorted(p for p in path.rglob("*.md") if p.is_file()))
        elif path.suffix.lower() == ".md":
            markdown_paths.append(path)

    return markdown_paths, errors


def is_support_file(path: Path) -> bool:
    return path.name in SUPPORT_FILENAMES


def has_prominent_disclaimer(lines: list[str]) -> bool:
    top = "\n".join(lines[:DISCLAIMER_LIMIT]).lower()
    return (
        "disclaimer" in top
        and "not medical advice" in top
        and "not personalized coaching" in top
    )


def source_ids(text: str) -> set[str]:
    return {match.group(1) for match in REFERENCE_DEF_RE.finditer(text)}


def source_urls(text: str) -> dict[str, str]:
    return {match.group(1): match.group(2) for match in REFERENCE_DEF_RE.finditer(text)}


def duplicate_source_ids(text: str) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for match in REFERENCE_DEF_RE.finditer(text):
        source_id = match.group(1)
        if source_id in seen:
            duplicates.add(source_id)
        seen.add(source_id)
    return duplicates


def safety_lines(lines: list[str]) -> list[tuple[int, str]]:
    flagged: list[tuple[int, str]] = []
    for index, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        lower = stripped.lower()
        if any(term in lower for term in SAFETY_TERMS):
            flagged.append((index, stripped))
    return flagged


def reference_ids_on_line(line: str) -> set[str]:
    return {match.group(1) for match in REFERENCE_LINK_RE.finditer(line)}


def cited_reference_ids(text: str) -> set[str]:
    return {match.group(1) for match in REFERENCE_LINK_RE.finditer(text)}


def cjk_character_count(text: str) -> int:
    return sum(1 for char in text if "\u4e00" <= char <= "\u9fff")


def normalize_url(url: str) -> str:
    return url.rstrip("/")


def repo_relative_path(path: Path, root: Path = ROOT) -> str | None:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return None


def is_remote_media_reference(target: str) -> bool:
    return target.lower().startswith(("http://", "https://", "file://"))


def is_page_local_source_id(source_id: str, path: Path) -> bool:
    return source_id.startswith(f"local-{path.stem}-")


def load_sources_index(path: Path = SOURCES_INDEX) -> tuple[dict[str, str], list[Finding], list[str]]:
    if not path.exists():
        return {}, [], [f"setup: sources_index_missing: {path}"]

    text = path.read_text(encoding="utf-8")
    findings = [
        Finding(path, "sources_index_duplicate_id", f"duplicate source ID in SOURCES.md: {source_id}")
        for source_id in sorted(duplicate_source_ids(text))
    ]
    return source_urls(text), findings, []


def markdown_table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def load_media_provenance(path: Path = PROVENANCE_INDEX) -> dict[str, list[dict[str, str]]]:
    if not path.exists():
        return {}

    rows_by_asset: dict[str, list[dict[str, str]]] = defaultdict(list)
    headers: list[str] | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = markdown_table_cells(line)
        if headers is None:
            headers = cells
            continue
        if all(set(cell) <= {"-", ":"} for cell in cells):
            continue
        row = {header: cells[index] if index < len(cells) else "" for index, header in enumerate(headers)}
        asset_path = row.get("asset_path", "").strip()
        if asset_path:
            rows_by_asset[asset_path].append(row)
    return dict(rows_by_asset)


def split_page_refs(value: str) -> set[str]:
    return {item.strip() for item in re.split(r"[,;]", value) if item.strip()}


def validate_raster_provenance(
    page_path: Path,
    asset_path: str,
    provenance_rows: dict[str, list[dict[str, str]]],
    root: Path = ROOT,
) -> list[Finding]:
    rows = provenance_rows.get(asset_path, [])
    if not rows:
        return [
            Finding(
                page_path,
                "media_provenance_missing",
                f"AI-generated raster asset lacks an approved provenance row: {asset_path}",
            )
        ]

    if len(rows) != 1:
        return [
            Finding(
                page_path,
                "media_provenance_incomplete",
                f"AI-generated raster asset must have exactly one provenance row: {asset_path}",
            )
        ]

    row = rows[0]
    missing_fields = [field for field in REQUIRED_PROVENANCE_FIELDS if not row.get(field, "").strip()]
    if missing_fields or row.get("asset_type", "").strip() != "ai_generated_raster":
        return [
            Finding(
                page_path,
                "media_provenance_incomplete",
                f"AI-generated raster provenance is incomplete for {asset_path}: {', '.join(missing_fields)}",
            )
        ]

    if row["media_purpose"].strip() not in ALLOWED_MEDIA_PURPOSES:
        return [
            Finding(
                page_path,
                "media_usage_out_of_scope",
                f"media_purpose is outside v0.1 scope for {asset_path}: {row['media_purpose']}",
            )
        ]

    if row["review_status"].strip() != "approved":
        return [
            Finding(
                page_path,
                "media_provenance_not_approved",
                f"AI-generated raster provenance is not approved for {asset_path}: {row['review_status']}",
            )
        ]

    page_ref = repo_relative_path(page_path, root)
    if page_ref is None or page_ref not in split_page_refs(row["page_refs"]):
        return [
            Finding(
                page_path,
                "media_page_refs_mismatch",
                f"provenance page_refs must include referencing page for {asset_path}: {page_ref}",
            )
        ]

    return []


def validate_media_reference(
    page_path: Path,
    target: str,
    provenance_rows: dict[str, list[dict[str, str]]],
    root: Path = ROOT,
) -> list[Finding]:
    if is_remote_media_reference(target):
        return [
            Finding(page_path, "external_media_reference", f"remote media references are not allowed: {target}")
        ]

    if Path(target).is_absolute() or target.startswith("/"):
        return [
            Finding(
                page_path,
                "media_outside_allowed_directory",
                f"media references must be relative paths under media/: {target}",
            )
        ]

    resolved = (page_path.parent / target).resolve()
    asset_path = repo_relative_path(resolved, root)
    if asset_path is None or not asset_path.startswith("media/"):
        return [
            Finding(
                page_path,
                "media_outside_allowed_directory",
                f"media references must resolve under media/: {target}",
            )
        ]

    extension = resolved.suffix.lower()
    if extension in SVG_EXTENSIONS:
        if not resolved.exists():
            return [Finding(page_path, "media_asset_missing", f"local media file is missing: {asset_path}")]
        return []

    if extension not in RASTER_EXTENSIONS:
        return [Finding(page_path, "unsupported_media_type", f"unsupported media extension for {asset_path}")]

    if not resolved.exists():
        return [Finding(page_path, "media_asset_missing", f"local media file is missing: {asset_path}")]

    return validate_raster_provenance(page_path, asset_path, provenance_rows, root)


def check_page(
    path: Path,
    global_sources: dict[str, str],
    provenance_rows: dict[str, list[dict[str, str]]],
    root: Path = ROOT,
) -> tuple[list[Finding], dict[str, str], set[str]]:
    if is_support_file(path):
        return [], {}, set()

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    findings: list[Finding] = []
    ids = source_ids(text)
    urls = source_urls(text)
    cited_ids = cited_reference_ids(text)

    if not has_prominent_disclaimer(lines):
        findings.append(
            Finding(
                path,
                "MF001",
                "prominent disclaimer with not medical advice and not personalized coaching is missing or too low",
            )
        )

    if "## Sources" not in text:
        findings.append(Finding(path, "MF002", "page-local ## Sources section is missing"))

    for source_id in sorted(cited_ids):
        if source_id not in ids:
            findings.append(
                Finding(
                    path,
                    "citation_missing_page_reference_definition",
                    f"cited source ID lacks a page-local reference definition: {source_id}",
                )
            )
            continue
        if is_page_local_source_id(source_id, path):
            continue
        if source_id not in global_sources:
            findings.append(
                Finding(
                    path,
                    "source_id_missing_from_sources_md",
                    f"non-local source ID must appear in SOURCES.md: {source_id}",
                )
            )
            continue
        if normalize_url(urls[source_id]) != normalize_url(global_sources[source_id]):
            findings.append(
                Finding(
                    path,
                    "source_url_mismatch_sources_md",
                    f"page-local URL does not match SOURCES.md for source ID: {source_id}",
                )
            )

    for line_number, line in safety_lines(lines):
        linked_ids = reference_ids_on_line(line)
        if not linked_ids:
            findings.append(
                Finding(path, "MF003", f"safety line {line_number} lacks a claim-level reference link")
            )
            continue
        missing_ids = sorted(linked_ids - ids)
        if missing_ids:
            findings.append(
                Finding(
                    path,
                    "MF004",
                    f"safety line {line_number} cites IDs not defined in the page-local sources: {', '.join(missing_ids)}",
                )
            )

    for ref_id, url in sorted(urls.items()):
        if "example.com" in url or url in {"TODO", "TBD"}:
            findings.append(Finding(path, "MF005", f"placeholder source URL for {ref_id} is not allowed"))

    if cjk_character_count(text) > 20:
        findings.append(Finding(path, "MF006", "full-card Chinese translation is outside v0.1 scope"))

    lower_text = text.lower()
    for term in EXCLUDED_SCOPE_TERMS:
        if term in lower_text:
            findings.append(Finding(path, "MF007", f"excluded v0.1 scope term found: {term}"))
            break

    for match in IMAGE_RE.finditer(text):
        alt_text = match.group(1).strip()
        target = match.group(2).strip()
        if not alt_text:
            findings.append(Finding(path, "MF009", "media reference is missing alt text"))
        findings.extend(validate_media_reference(path, target, provenance_rows, root))

    return findings, urls, cited_ids


def check_cross_page_source_usage(page_sources: dict[str, dict[str, str]], page_citations: dict[str, set[str]], global_sources: dict[str, str]) -> list[Finding]:
    pages_by_source: dict[str, set[str]] = defaultdict(set)
    path_by_name = {str(path): path for path in page_sources}

    for path_name, cited_ids in page_citations.items():
        for source_id in cited_ids:
            pages_by_source[source_id].add(path_name)

    findings: list[Finding] = []
    for source_id, path_names in sorted(pages_by_source.items()):
        if len(path_names) < 2:
            continue
        first_path = path_by_name[sorted(path_names)[0]]
        if source_id.startswith("local-"):
            findings.append(
                Finding(
                    first_path,
                    "local_source_id_reused_across_pages",
                    f"page-local source ID is used in multiple pages: {source_id}",
                )
            )
        elif source_id not in global_sources:
            findings.append(
                Finding(
                    first_path,
                    "reused_source_id_missing_from_sources_md",
                    f"reused source ID must appear in SOURCES.md: {source_id}",
                )
            )
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check Markdown-first GymPrimer pages for v0.1 structural, citation, scope, language, and media rules."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Markdown files or directories to check")
    args = parser.parse_args(argv)

    markdown_paths, errors = iter_markdown_paths(args.paths)
    if errors:
        for error in errors:
            print(error)
        return 2
    if not markdown_paths:
        print("setup: no Markdown files found")
        return 2

    global_sources, index_findings, source_errors = load_sources_index()
    if source_errors:
        for error in source_errors:
            print(error)
        return 2
    media_provenance = load_media_provenance()

    findings: list[Finding] = list(index_findings)
    page_sources: dict[str, dict[str, str]] = {}
    page_citations: dict[str, set[str]] = {}
    for path in markdown_paths:
        page_findings, urls, cited_ids = check_page(path, global_sources, media_provenance)
        findings.extend(page_findings)
        if not is_support_file(path):
            page_sources[str(path)] = urls
            page_citations[str(path)] = cited_ids

    findings.extend(check_cross_page_source_usage(page_sources, page_citations, global_sources))

    if findings:
        for finding in findings:
            print(finding.format())
        return 1

    print(f"checked {len(markdown_paths)} Markdown file(s): pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
