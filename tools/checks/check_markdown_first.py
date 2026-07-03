#!/usr/bin/env python3
"""Lightweight Markdown-first content contract checks."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from collections import defaultdict
from datetime import date
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
RESPONSIBLE_BREADTH_PAGE_CLASSES = {
    "patterns": "pattern_page",
    "conditions": "condition_page",
    "principles": "programming_principle_page",
    "programs": "program_example_page",
    "exercises": "expanded_exercise_page",
}
RESPONSIBLE_BREADTH_METADATA_FIELDS = (
    "Author",
    "Created",
    "Last reviewed",
    "Next review due",
    "Review scope",
)
PATTERN_SECTIONS = (
    "## What this page is",
    "## What this page is not",
    "## Red flags",
    "## Why beginners come to this page",
    "## Working definition",
    "## How to notice this in yourself",
    "## The core reason",
    "## What is uncertain or mixed",
    "## What commonly helps",
    "## What to avoid",
    "## When to see a professional",
    "## Where to next in this primer",
    "## Sources",
    "## Author and review date",
)
CONDITION_SECTIONS = (
    "## What this page is",
    "## What this page is not",
    "## Red flags",
    "## Plain-language overview",
    "## What mainstream sources generally agree on",
    "## What is uncertain or mixed",
    "## Commonly recommended self-management themes",
    "## What to avoid",
    "## When to see a professional",
    "## Sources",
    "## Author and review date",
)
PROGRAM_PRINCIPLE_SECTIONS = (
    "## What this page is",
    "## What this page is not",
    "## Plain-language overview",
    "## Sources",
)
PROGRAM_EXAMPLE_SECTIONS = (
    "## What this page is",
    "## What this page is not",
    "## Example week",
    "## Sources",
)
FORWARD_HEAD_PATTERN_PATH = "patterns/forward-head-posture.md"
FORWARD_HEAD_EXERCISE_LINKS = (
    "../exercises/chin-nod.md",
    "../exercises/thoracic-extension.md",
    "../exercises/wall-slide.md",
    "../exercises/prone-y-t.md",
    "../exercises/band-pull-apart.md",
)
FORWARD_HEAD_EXERCISE_PATHS = {
    "exercises/chin-nod.md",
    "exercises/thoracic-extension.md",
    "exercises/wall-slide.md",
    "exercises/prone-y-t.md",
    "exercises/band-pull-apart.md",
}
FORWARD_HEAD_EXERCISE_SECTIONS = (
    "## What this exercise is for",
    "## Equipment setup",
    "## Muscles involved",
    "## Movement breakdown",
    "## What you should feel",
    "## Common mistakes",
    "## Easier version",
    "## Harder version",
    "## Safety notes",
    "## Sources",
)
RESPONSIBLE_BREADTH_FORBIDDEN_PATTERNS = (
    re.compile(r"\byou have\b", re.IGNORECASE),
    re.compile(r"\btreatment plan\b", re.IGNORECASE),
    re.compile(r"\brehab(?:ilitation)? progression\b", re.IGNORECASE),
    re.compile(r"\bcorrect(?:ive|ion) routine\b", re.IGNORECASE),
    re.compile(r"\bfix (?:this|your|it)\b", re.IGNORECASE),
    re.compile(r"\bfollow this program\b", re.IGNORECASE),
    re.compile(r"\bfor your [a-z -]*pain\b", re.IGNORECASE),
    re.compile(r"\bsymptom checker\b", re.IGNORECASE),
    re.compile(r"\bdiagnostic decision tree\b", re.IGNORECASE),
    re.compile(r"\bpost-surgical\b", re.IGNORECASE),
    re.compile(r"\bpregnan(?:cy|t)\b", re.IGNORECASE),
    re.compile(r"\bpediatric\b", re.IGNORECASE),
    re.compile(r"\boncology\b", re.IGNORECASE),
)
SUPPORT_FILENAMES = {
    "README.md",
    "SOURCES.md",
    "CONTRIBUTING.md",
    "CONTENT_LICENSE.md",
    "PROVENANCE.md",
    "RED-FLAGS.md",
}
OLD_CONTENT_DIRS = {
    "01" + "-getting-started",
    "02" + "-machines",
    "03" + "-bodyweight",
}
OLD_MEDIA_BUCKETS = {
    "media/" + "equipment/",
    "media/" + "movements/",
    "media/" + "supplemental/",
}
OLD_REFERENCE_PATTERNS = tuple(f"{directory}/" for directory in sorted(OLD_CONTENT_DIRS)) + ("about/" + "red-flags.md",)
OLD_MEDIA_REFERENCE_PATTERNS = (
    "media/" + "equipment/",
    "media/" + "movements/",
    "media/" + "supplemental/",
)
HISTORICAL_ARTIFACT_DIRS = {
    "content",
    "schemas",
    "generated",
}
ROOT_GOVERNANCE_DIRS = {
    "proposals",
    "adr",
}
RASTER_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SVG_EXTENSIONS = {".svg"}
ALLOWED_MEDIA_PURPOSES = {"equipment_identification", "key_movement_illustration"}
EXERCISE_IMAGE_MEDIA_PURPOSES = {
    "exercise_setup_illustration",
    "exercise_movement_illustration",
    "exercise_muscle_attention_illustration",
}
LEGACY_EXERCISE_IMAGE_MEDIA_PURPOSES = {"equipment_identification", "key_movement_illustration"}
RESPONSIBLE_BREADTH_MEDIA_PURPOSES_BY_CLASS = {
    "pattern_page": {"pattern_alignment_illustration", "exercise_preview_illustration"},
    "condition_page": {"anatomical_region_illustration", "exercise_preview_illustration"},
    "expanded_exercise_page": EXERCISE_IMAGE_MEDIA_PURPOSES | LEGACY_EXERCISE_IMAGE_MEDIA_PURPOSES,
    "programming_principle_page": {"equipment_identification", "key_movement_illustration"},
    "program_example_page": {"equipment_identification", "key_movement_illustration"},
}
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
PROMPT_RECORD_COMPATIBILITY_NOTE = "M3 pre-amendment prompt unavailable; compatibility limitation recorded"
PROMPT_RECORD_COMPATIBILITY_ASSETS = {
    "media/exercises/chin-nod/muscle-attention.png",
    "media/exercises/thoracic-extension/muscle-attention.png",
    "media/exercises/wall-slide/movement.png",
    "media/exercises/wall-slide/muscle-attention.png",
    "media/exercises/prone-y-t/muscle-attention.png",
}
PROMPT_RECORD_REQUIRED_FIELDS = (
    "asset_path",
    "generator",
    "created_date",
    "review_status",
)

REFERENCE_LINK_RE = re.compile(r"\[[^\]]+\]\[([A-Za-z0-9_.:-]+)\]")
REFERENCE_DEF_RE = re.compile(r"^\[([A-Za-z0-9_.:-]+)\]:\s+(\S+)\s*$", re.MULTILINE)
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
PATTERN_ALIGNMENT_FORBIDDEN_MEDIA_TEXT_RE = re.compile(
    r"\b(label(?:s|ed)?|caption|wording|with text|contains text|bad posture|red (?:pain|injury)|pain mark|cure|before/after|thumbnail)\b",
    re.IGNORECASE,
)
EXERCISE_IMAGE_FORBIDDEN_MEDIA_TEXT_RE = re.compile(
    r"\b(diagnos(?:e|is|ed)?|treat(?:ment|ing)?|cure|correct(?:ness)?|wrong|warning badge|red (?:pain|injury)|pain mark|injury symbol|before/after|personalized coaching)\b",
    re.IGNORECASE,
)
GENERIC_IMAGE_ALT_TEXT = {
    "image",
    "exercise image",
    "diagram",
    "picture",
    "photo",
    "illustration",
}
AI_REVIEWER_RE = re.compile(r"\b(openai|chatgpt|image generation tool|ai tool|artificial intelligence)\b", re.IGNORECASE)
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


def is_red_flags_file(path: Path, root: Path = ROOT) -> bool:
    return repo_relative_path(path, root) == "RED-FLAGS.md"


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


def responsible_breadth_page_class(path: Path, root: Path = ROOT) -> str | None:
    relative = repo_relative_path(path, root)
    if relative is None:
        return None
    first_part = relative.split("/", 1)[0]
    return RESPONSIBLE_BREADTH_PAGE_CLASSES.get(first_part)


def is_template_file(path: Path, root: Path = ROOT) -> bool:
    relative = repo_relative_path(path, root)
    return bool(relative and relative.startswith("docs/templates/"))


def is_forward_head_pattern(path: Path, root: Path = ROOT) -> bool:
    return repo_relative_path(path, root) == FORWARD_HEAD_PATTERN_PATH


def is_forward_head_exercise(path: Path, root: Path = ROOT) -> bool:
    relative = repo_relative_path(path, root)
    return relative in FORWARD_HEAD_EXERCISE_PATHS


def normalized_layout_active(root: Path = ROOT) -> bool:
    return (root / "RED-FLAGS.md").exists()


def media_layout_active(root: Path = ROOT) -> bool:
    return normalized_layout_active(root) and not any((root / old_bucket).exists() for old_bucket in OLD_MEDIA_BUCKETS)


def relative_parts(path: Path, root: Path = ROOT) -> list[str]:
    relative = repo_relative_path(path, root)
    return [] if relative is None else relative.split("/")


def is_old_content_path(path: Path, root: Path = ROOT) -> bool:
    parts = relative_parts(path, root)
    return bool(parts and parts[0] in OLD_CONTENT_DIRS)


def is_historical_artifact_path(path: Path, root: Path = ROOT) -> bool:
    parts = relative_parts(path, root)
    return bool(parts and parts[0] in HISTORICAL_ARTIFACT_DIRS)


def has_historical_classification(text: str) -> bool:
    lower = text.lower()
    return "historical" in lower or "archive" in lower or "archived" in lower


def looks_like_compatibility_stub(text: str) -> bool:
    return bool(re.search(r"\b(moved|renamed|redirect|see instead)\b", text, re.IGNORECASE))


def stale_references(text: str) -> list[str]:
    references = [pattern for pattern in OLD_REFERENCE_PATTERNS if pattern in text]
    if media_layout_active(ROOT):
        references.extend(pattern for pattern in OLD_MEDIA_REFERENCE_PATTERNS if pattern in text)
    return references


def expected_subject_media_prefix(page_path: Path, page_class: str | None, root: Path = ROOT) -> str | None:
    if page_class is None:
        return None
    relative = repo_relative_path(page_path, root)
    if relative is None:
        return None
    parts = relative.split("/")
    if len(parts) < 2:
        return None
    slug = Path(parts[-1]).stem
    if page_class == "pattern_page":
        return f"media/patterns/{slug}/"
    if page_class == "condition_page":
        return f"media/conditions/{slug}/"
    if page_class == "expanded_exercise_page":
        return f"media/exercises/{slug}/"
    return None


def parse_metadata(lines: list[str]) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in lines[:20]:
        for field in RESPONSIBLE_BREADTH_METADATA_FIELDS:
            prefix = f"{field}:"
            if line.startswith(prefix):
                metadata[field] = line.removeprefix(prefix).strip()
    return metadata


def parse_iso_date(value: str) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def heading_position(text: str, heading_prefix: str) -> int:
    pattern = re.compile(rf"^{re.escape(heading_prefix)}(?:$|[:\n ])", re.MULTILINE)
    match = pattern.search(text)
    return -1 if match is None else match.start()


def section_text(text: str, heading_prefix: str) -> str:
    start = heading_position(text, heading_prefix)
    if start == -1:
        return ""
    next_heading = re.search(r"^##\s+", text[start + 1 :], re.MULTILINE)
    if next_heading is None:
        return text[start:]
    return text[start : start + 1 + next_heading.start()]


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


def media_purpose_allowed_for_page(page_class: str | None, media_purpose: str) -> bool:
    if page_class is None:
        return media_purpose in ALLOWED_MEDIA_PURPOSES
    return media_purpose in RESPONSIBLE_BREADTH_MEDIA_PURPOSES_BY_CLASS.get(page_class, ALLOWED_MEDIA_PURPOSES)


def expected_media_purpose_message(page_class: str | None) -> str:
    if page_class is None:
        expected = sorted(ALLOWED_MEDIA_PURPOSES)
    else:
        expected = sorted(RESPONSIBLE_BREADTH_MEDIA_PURPOSES_BY_CLASS.get(page_class, ALLOWED_MEDIA_PURPOSES))
    return ", ".join(expected)


def image_text_implies_condition_diagnosis(alt_text: str) -> bool:
    return bool(re.search(r"\b(diagnos(?:is|ed)|patholog(?:y|ic)|treat(?:ment)?|damaged|disease)\b", alt_text, re.IGNORECASE))


def expected_prompt_record_path(asset_path: str) -> str | None:
    parts = asset_path.split("/")
    if len(parts) != 4 or parts[0] != "media" or parts[1] != "exercises":
        return None
    return f"media/prompts/exercises/{parts[2]}/{Path(parts[3]).stem}.md"


def parse_prompt_record_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^\s*([A-Za-z_][A-Za-z0-9_ -]*):\s*(.*)\s*$", line)
        if match:
            key = match.group(1).strip().lower().replace(" ", "_").replace("-", "_")
            fields[key] = match.group(2).strip()
    return fields


def prompt_record_section(text: str, heading: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(text)
    if match is None:
        return ""
    next_heading = re.search(r"^##\s+", text[match.end() :], re.MULTILINE)
    end = len(text) if next_heading is None else match.end() + next_heading.start()
    return text[match.end() : end].strip()


def has_prompt_record_text_or_redaction(text: str) -> bool:
    exact_prompt = prompt_record_section(text, "Exact prompt")
    if exact_prompt:
        return True
    return bool(prompt_record_section(text, "Redaction note"))


def validate_prompt_record(
    page_path: Path,
    asset_path: str,
    provenance_row: dict[str, str],
    root: Path = ROOT,
) -> list[Finding]:
    prompt_record = provenance_row.get("prompt_record", "").strip()
    if not prompt_record:
        if (
            provenance_row.get("notes", "").strip() == PROMPT_RECORD_COMPATIBILITY_NOTE
            and asset_path in PROMPT_RECORD_COMPATIBILITY_ASSETS
        ):
            return []
        return [
            Finding(
                page_path,
                "media_prompt_record_missing",
                f"generated raster exercise image provenance lacks prompt_record for {asset_path}",
            )
        ]

    expected = expected_prompt_record_path(asset_path)
    if (
        is_remote_media_reference(prompt_record)
        or Path(prompt_record).is_absolute()
        or "\\" in prompt_record
        or expected is None
        or prompt_record != expected
    ):
        return [
            Finding(
                page_path,
                "media_prompt_record_invalid",
                f"prompt_record for {asset_path} must be repository-local and match {expected}: {prompt_record}",
            )
        ]

    prompt_record_path = (root / prompt_record).resolve()
    if repo_relative_path(prompt_record_path, root) != prompt_record:
        return [
            Finding(
                page_path,
                "media_prompt_record_invalid",
                f"prompt_record for {asset_path} must resolve inside the repository: {prompt_record}",
            )
        ]
    if prompt_record_path.suffix.lower() != ".md":
        return [
            Finding(
                page_path,
                "media_prompt_record_invalid",
                f"prompt_record for {asset_path} must be a Markdown file: {prompt_record}",
            )
        ]
    if not prompt_record_path.exists():
        return [
            Finding(
                page_path,
                "media_prompt_record_missing",
                f"prompt_record file is missing for {asset_path}: {prompt_record}",
            )
        ]

    text = prompt_record_path.read_text(encoding="utf-8")
    fields = parse_prompt_record_fields(text)
    missing_fields = [field for field in PROMPT_RECORD_REQUIRED_FIELDS if not fields.get(field, "").strip()]
    if not fields.get("human_reviewer", "").strip() and not fields.get("review_owner", "").strip():
        missing_fields.append("human_reviewer_or_review_owner")
    if missing_fields or not has_prompt_record_text_or_redaction(text):
        if not has_prompt_record_text_or_redaction(text):
            missing_fields.append("exact_prompt_or_redaction_note")
        return [
            Finding(
                page_path,
                "media_prompt_record_incomplete",
                f"prompt_record is incomplete for {asset_path} at {prompt_record}: {', '.join(missing_fields)}",
            )
        ]

    if fields["asset_path"].strip() != asset_path:
        return [
            Finding(
                page_path,
                "media_prompt_record_mismatch",
                f"prompt_record asset_path must match provenance asset_path for {asset_path}: {fields['asset_path']}",
            )
        ]

    return []


def pattern_alignment_text_contract_violation(alt_text: str, provenance_row: dict[str, str]) -> str | None:
    fields = (
        alt_text,
        provenance_row.get("prompt_or_creation_notes", ""),
        provenance_row.get("notes", ""),
    )
    match = PATTERN_ALIGNMENT_FORBIDDEN_MEDIA_TEXT_RE.search(" ".join(fields))
    return None if match is None else match.group(0)


def exercise_image_text_contract_violation(alt_text: str, provenance_row: dict[str, str]) -> str | None:
    fields = (
        alt_text,
        provenance_row.get("prompt_or_creation_notes", ""),
        provenance_row.get("notes", ""),
    )
    match = EXERCISE_IMAGE_FORBIDDEN_MEDIA_TEXT_RE.search(" ".join(fields))
    return None if match is None else match.group(0)


def generic_image_alt_text(alt_text: str) -> bool:
    normalized = re.sub(r"\s+", " ", alt_text.strip().lower()).strip(" .:-_")
    return normalized in GENERIC_IMAGE_ALT_TEXT


def ai_tool_reviewer(value: str) -> bool:
    return bool(AI_REVIEWER_RE.search(value.strip()))


def validate_raster_provenance(
    page_path: Path,
    asset_path: str,
    alt_text: str,
    page_class: str | None,
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

    media_purpose = row["media_purpose"].strip()
    if not media_purpose_allowed_for_page(page_class, media_purpose):
        return [
            Finding(
                page_path,
                "media_usage_out_of_scope",
                f"media_purpose is outside allowed scope for {asset_path}: {media_purpose}; expected one of {expected_media_purpose_message(page_class)}",
            )
        ]

    if page_class == "expanded_exercise_page" and ai_tool_reviewer(row["human_reviewer"]):
        return [
            Finding(
                page_path,
                "media_human_reviewer_invalid",
                f"AI-generated raster provenance human_reviewer must identify an accountable human for {asset_path}: {row['human_reviewer']}",
            )
        ]

    if media_purpose == "anatomical_region_illustration" and image_text_implies_condition_diagnosis(alt_text):
        return [
            Finding(
                page_path,
                "media_usage_out_of_scope",
                f"anatomical_region_illustration must not imply diagnosis, pathology, or treatment: {alt_text}",
            )
        ]

    if page_class == "pattern_page" and media_purpose == "pattern_alignment_illustration":
        violation = pattern_alignment_text_contract_violation(alt_text, row)
        if violation:
            return [
                Finding(
                    page_path,
                    "media_usage_out_of_scope",
                    f"pattern alignment image must not include in-image text, labels, thumbnails, injury marks, or cure implications: {violation}",
                )
            ]

    if page_class == "expanded_exercise_page" and media_purpose in EXERCISE_IMAGE_MEDIA_PURPOSES:
        violation = exercise_image_text_contract_violation(alt_text, row)
        if violation:
            return [
                Finding(
                    page_path,
                    "exercise_image_visual_safety_text",
                    f"exercise image text, alt text, or provenance notes must not imply diagnosis, treatment, correction, injury, warning badge, cure, or coaching claims: {violation}",
                )
            ]
        prompt_record_findings = validate_prompt_record(page_path, asset_path, row, root)
        if prompt_record_findings:
            return prompt_record_findings

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


def validate_exercise_image_summary(
    page_path: Path,
    image_matches: list[re.Match[str]],
    provenance_rows: dict[str, list[dict[str, str]]],
    root: Path = ROOT,
) -> list[Finding]:
    findings: list[Finding] = []
    if len(image_matches) > 3:
        findings.append(
            Finding(
                page_path,
                "exercise_image_count_exceeded",
                f"exercise pages may reference no more than three exercise images without an approved exception; found {len(image_matches)}",
            )
        )

    muscle_attention_count = 0
    for match in image_matches:
        target = match.group(2).strip()
        if is_remote_media_reference(target) or Path(target).is_absolute() or target.startswith("/"):
            continue
        asset_path = repo_relative_path((page_path.parent / target).resolve(), root)
        if asset_path is None:
            continue
        rows = provenance_rows.get(asset_path, [])
        if len(rows) == 1 and rows[0].get("media_purpose", "").strip() == "exercise_muscle_attention_illustration":
            muscle_attention_count += 1

    if muscle_attention_count > 1:
        findings.append(
            Finding(
                page_path,
                "exercise_muscle_attention_limit",
                f"exercise pages may reference no more than one exercise_muscle_attention_illustration; found {muscle_attention_count}",
            )
        )

    return findings


def validate_media_reference(
    page_path: Path,
    alt_text: str,
    target: str,
    page_class: str | None,
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
    if media_layout_active(root):
        for old_bucket in OLD_MEDIA_BUCKETS:
            if asset_path.startswith(old_bucket):
                return [
                    Finding(
                        page_path,
                        "old_media_bucket_reference",
                        f"media reference uses removed media bucket: {asset_path}",
                    )
                ]
        expected_prefix = expected_subject_media_prefix(page_path, page_class, root)
        if extension in RASTER_EXTENSIONS and expected_prefix is not None and not asset_path.startswith(expected_prefix):
            return [
                Finding(
                    page_path,
                    "subject_media_path_mismatch",
                    f"raster media for this page must live under {expected_prefix}: {asset_path}",
                )
            ]

    if extension in SVG_EXTENSIONS:
        if not resolved.exists():
            return [Finding(page_path, "media_asset_missing", f"local media file is missing: {asset_path}")]
        return []

    if extension not in RASTER_EXTENSIONS:
        return [Finding(page_path, "unsupported_media_type", f"unsupported media extension for {asset_path}")]

    if not resolved.exists():
        return [Finding(page_path, "media_asset_missing", f"local media file is missing: {asset_path}")]

    return validate_raster_provenance(page_path, asset_path, alt_text, page_class, provenance_rows, root)


def validate_responsible_breadth_page(
    path: Path,
    page_class: str,
    text: str,
    lines: list[str],
    cited_ids: set[str],
) -> list[Finding]:
    findings: list[Finding] = []

    required_sections: tuple[str, ...] = ()
    if page_class == "pattern_page":
        required_sections = PATTERN_SECTIONS
    elif page_class == "condition_page":
        required_sections = CONDITION_SECTIONS
    elif page_class == "programming_principle_page":
        required_sections = PROGRAM_PRINCIPLE_SECTIONS
    elif page_class == "program_example_page":
        required_sections = PROGRAM_EXAMPLE_SECTIONS

    for section in required_sections:
        if heading_position(text, section) == -1:
            findings.append(Finding(path, "RB002", f"Responsible Breadth section is missing: {section.removeprefix('## ')}"))

    metadata = parse_metadata(lines)
    for field in RESPONSIBLE_BREADTH_METADATA_FIELDS:
        if field not in metadata:
            findings.append(Finding(path, "RB003", f"Responsible Breadth metadata field is missing: {field}"))

    created = parse_iso_date(metadata.get("Created", ""))
    next_review = parse_iso_date(metadata.get("Next review due", ""))
    if created is None and "Created" in metadata:
        findings.append(Finding(path, "RB003", "Responsible Breadth metadata field has invalid date: Created"))
    if next_review is None and "Next review due" in metadata:
        findings.append(Finding(path, "RB003", "Responsible Breadth metadata field has invalid date: Next review due"))
    if created is not None and next_review is not None:
        days_until_review = (next_review - created).days
        if days_until_review < 0:
            findings.append(Finding(path, "RB003", "Next review due must not precede Created"))
        if page_class in {"pattern_page", "condition_page", "program_example_page"} and days_until_review > 90:
            findings.append(
                Finding(path, "RB003", "safety-relevant Responsible Breadth pages need first review due within 90 days")
            )
        if page_class in {"expanded_exercise_page", "programming_principle_page"} and days_until_review > 366:
            findings.append(Finding(path, "RB003", "Responsible Breadth review due date is too far in the future"))

    if page_class in {"pattern_page", "condition_page"}:
        red_flags_position = heading_position(text, "## Red flags")
        self_management_heading = "## What commonly helps" if page_class == "pattern_page" else "## Commonly recommended self-management themes"
        self_management_position = heading_position(text, self_management_heading)
        if red_flags_position == -1:
            findings.append(Finding(path, "RB004", "red-flags section is missing"))
        elif normalized_layout_active(ROOT) and "RED-FLAGS.md" not in text:
            findings.append(Finding(path, "RB004", "red-flags section must link to RED-FLAGS.md"))
        elif not normalized_layout_active(ROOT) and "../about/" + "red-flags.md" not in text and "about/" + "red-flags.md" not in text:
            findings.append(Finding(path, "RB004", "red-flags section must link to the nested red-flags reference"))
        elif self_management_position != -1 and red_flags_position > self_management_position:
            findings.append(Finding(path, "RB004", "red-flags routing must appear before self-management discussion"))

    if page_class == "pattern_page":
        findings.extend(validate_pattern_architecture(path, text))

    if page_class == "expanded_exercise_page" and is_forward_head_exercise(path):
        findings.extend(validate_forward_head_exercise_contract(path, text))

    if page_class == "expanded_exercise_page" and re.search(r"(^##\s+Exact prompt\b|^prompt_record:)", text, re.MULTILINE | re.IGNORECASE):
        findings.append(Finding(path, "media_prompt_record_embedded", "prompt records must not be embedded in reader-facing exercise Markdown"))

    if len(cited_ids) < 3:
        findings.append(
            Finding(path, "RB005", f"Responsible Breadth pages must cite at least three named sources; found {len(cited_ids)}")
        )

    for pattern in RESPONSIBLE_BREADTH_FORBIDDEN_PATTERNS:
        match = pattern.search(text)
        if match:
            findings.append(Finding(path, "RB006", f"Responsible Breadth forbidden scope language found: {match.group(0)}"))
            break

    return findings


def validate_pattern_architecture(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []

    beginner_section = section_text(text, "## Why beginners come to this page")
    beginner_bullets = re.findall(r"^\s*-\s+", beginner_section, re.MULTILINE)
    if beginner_section and not 3 <= len(beginner_bullets) <= 5:
        findings.append(
            Finding(
                path,
                "RB007",
                f"Why beginners come to this page must contain three to five entry-point bullets; found {len(beginner_bullets)}",
            )
        )

    reason_section = section_text(text, "## The core reason")
    contributors = list(re.finditer(r"^\*\*([^*]+)\.\*\*", reason_section, re.MULTILINE))
    if reason_section and not 3 <= len(contributors) <= 5:
        findings.append(
            Finding(
                path,
                "RB007",
                f"The core reason must name three to five contributors; found {len(contributors)}",
            )
        )
    for index, contributor in enumerate(contributors):
        next_start = contributors[index + 1].start() if index + 1 < len(contributors) else len(reason_section)
        contributor_block = reason_section[contributor.start() : next_start]
        if not reference_ids_on_line(contributor_block):
            findings.append(
                Finding(
                    path,
                    "RB007",
                    f"The core reason contributor lacks a citation: {contributor.group(1)}",
                )
            )

    helps_section = section_text(text, "## What commonly helps")
    preview_pattern = re.compile(r"^-\s+\*\*\[([^\]]+)\]\((../exercises/[^)]+\.md)\)\*\*", re.MULTILINE)
    previews = list(preview_pattern.finditer(helps_section))
    for index, preview in enumerate(previews):
        next_start = previews[index + 1].start() if index + 1 < len(previews) else len(helps_section)
        block = helps_section[preview.start() : next_start]
        link_target = preview.group(2)
        exercise_path = (path.parent / link_target).resolve()
        if not exercise_path.exists() and "not yet available" not in block.lower():
            findings.append(Finding(path, "RB007", f"pattern exercise preview links missing exercise page: {link_target}"))
        for required in ("Fix reason", "Used muscles", "Important note"):
            if f"*{required}:*" not in block:
                findings.append(Finding(path, "RB007", f"pattern exercise preview is missing {required}: {link_target}"))

    if is_forward_head_pattern(path):
        findings.extend(validate_forward_head_pattern_contract(path, text, helps_section))

    return findings


def validate_forward_head_pattern_contract(path: Path, text: str, helps_section: str) -> list[Finding]:
    findings: list[Finding] = []

    first_heading = next((line.strip() for line in text.splitlines() if line.startswith("# ")), "")
    if first_heading != "# Forward Head Posture":
        findings.append(Finding(path, "RB008", 'forward-head pattern title must be exactly "Forward Head Posture"'))

    for link_target in FORWARD_HEAD_EXERCISE_LINKS:
        if f"]({link_target})" not in helps_section:
            findings.append(Finding(path, "RB008", f"forward-head pattern is missing detailed exercise link: {link_target}"))

    image_matches = list(IMAGE_RE.finditer(text))
    if len(image_matches) > 1:
        findings.append(
            Finding(
                path,
                "RB009",
                f"forward-head pattern page may reference no more than one pattern comparison image; found {len(image_matches)}",
            )
        )

    for match in image_matches:
        alt_text = match.group(1)
        target = match.group(2)
        combined = f"{alt_text} {target}"
        if "../media/exercises/" in target or "thumbnail" in combined.lower():
            findings.append(Finding(path, "RB009", "forward-head pattern page must not include exercise thumbnails"))
        if PATTERN_ALIGNMENT_FORBIDDEN_MEDIA_TEXT_RE.search(alt_text):
            findings.append(
                Finding(
                    path,
                    "RB009",
                    "forward-head pattern image alt text must not imply in-image text, labels, injury marks, or cure framing",
                )
            )

    return findings


def validate_forward_head_exercise_contract(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []

    for section in FORWARD_HEAD_EXERCISE_SECTIONS:
        if heading_position(text, section) == -1:
            findings.append(Finding(path, "RB010", f"forward-head exercise page section is missing: {section.removeprefix('## ')}"))

    return findings


def check_page(
    path: Path,
    global_sources: dict[str, str],
    provenance_rows: dict[str, list[dict[str, str]]],
    root: Path = ROOT,
) -> tuple[list[Finding], dict[str, str], set[str]]:
    if is_support_file(path):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        findings: list[Finding] = []
        if is_red_flags_file(path, root) and not has_prominent_disclaimer(lines):
            findings.append(
                Finding(
                    path,
                    "MF001",
                    "central RED-FLAGS.md disclaimer with not medical advice and not personalized coaching is missing or too low",
                )
            )
        if normalized_layout_active(root):
            findings.extend(
                Finding(path, "stale_old_path_reference", f"active Markdown references removed path: {reference}")
                for reference in stale_references(text)
            )
            return findings, {}, set()
        return findings, {}, set()

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    findings: list[Finding] = []
    if is_template_file(path, root):
        for match in IMAGE_RE.finditer(text):
            alt_text = match.group(1).strip()
            target = match.group(2).strip()
            if not alt_text:
                findings.append(Finding(path, "MF009", "media reference is missing alt text"))
            findings.extend(validate_media_reference(path, alt_text, target, None, provenance_rows, root))
        return findings, {}, set()

    ids = source_ids(text)
    urls = source_urls(text)
    cited_ids = cited_reference_ids(text)
    rb_page_class = responsible_breadth_page_class(path, root)
    strict_layout = normalized_layout_active(root)

    if strict_layout and is_historical_artifact_path(path, root):
        if not has_historical_classification(text):
            findings.append(
                Finding(
                    path,
                    "historical_artifact_unclassified",
                    "historical structured-platform artifacts must be labeled historical or archived when retained",
                )
            )
        return findings, {}, set()

    if strict_layout and is_old_content_path(path, root):
        code = "compatibility_stub_forbidden" if looks_like_compatibility_stub(text) else "old_content_path_active"
        findings.append(Finding(path, code, "old numbered content paths must be removed directly after migration"))

    if strict_layout:
        for reference in stale_references(text):
            findings.append(Finding(path, "stale_old_path_reference", f"active Markdown references removed path: {reference}"))

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

    if rb_page_class is None:
        lower_text = text.lower()
        for term in EXCLUDED_SCOPE_TERMS:
            if term in lower_text:
                findings.append(Finding(path, "MF007", f"excluded v0.1 scope term found: {term}"))
                break
    else:
        findings.extend(validate_responsible_breadth_page(path, rb_page_class, text, lines, cited_ids))

    image_matches = list(IMAGE_RE.finditer(text))
    if rb_page_class == "expanded_exercise_page":
        findings.extend(validate_exercise_image_summary(path, image_matches, provenance_rows, root))

    for match in image_matches:
        alt_text = match.group(1).strip()
        target = match.group(2).strip()
        if not alt_text:
            findings.append(Finding(path, "MF009", "media reference is missing alt text"))
        elif rb_page_class == "expanded_exercise_page" and generic_image_alt_text(alt_text):
            findings.append(
                Finding(
                    path,
                    "exercise_image_alt_text_generic",
                    f"exercise image alt text must describe the exercise context and teaching purpose: {alt_text}",
                )
            )
        findings.extend(validate_media_reference(path, alt_text, target, rb_page_class, provenance_rows, root))

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


def validate_repository_layout(root: Path, provenance_rows: dict[str, list[dict[str, str]]]) -> list[Finding]:
    if not normalized_layout_active(root):
        return []

    findings: list[Finding] = []
    for directory in sorted(ROOT_GOVERNANCE_DIRS):
        path = root / directory
        if path.exists():
            findings.append(
                Finding(
                    path,
                    "governance_path_not_under_docs",
                    f"governance artifacts must remain under docs/: {directory}/",
                )
            )

    if media_layout_active(root):
        for asset_path in sorted(provenance_rows):
            if any(asset_path.startswith(old_bucket) for old_bucket in OLD_MEDIA_BUCKETS):
                findings.append(
                    Finding(
                        root / "media/PROVENANCE.md",
                        "stale_media_provenance_path",
                        f"media provenance row uses removed media bucket: {asset_path}",
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
    findings.extend(validate_repository_layout(ROOT, media_provenance))
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
