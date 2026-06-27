#!/usr/bin/env python3
"""M1 content validation harness for repository-native GymPrimer content."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_SCHEMA_VERSION = "content-schema-v1"
CARD_SUFFIXES = {".json"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate GymPrimer source content.")
    parser.add_argument("--source", required=True, help="Content source directory.")
    parser.add_argument("--schemas", required=True, help="Schema directory.")
    parser.add_argument("--media", required=True, help="Media directory.")
    parser.add_argument("--out", required=True, help="Validation report output path.")
    return parser


def schema_version(schemas: Path) -> str:
    version_file = schemas / "content-schema-version.txt"
    if version_file.exists():
        version = version_file.read_text(encoding="utf-8").strip()
        return version or DEFAULT_SCHEMA_VERSION

    report_schema = schemas / "validation-report.schema.json"
    if report_schema.exists():
        try:
            data = json.loads(report_schema.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return DEFAULT_SCHEMA_VERSION
        value = data.get("schema_version")
        if isinstance(value, str) and value:
            return value

    return DEFAULT_SCHEMA_VERSION


def base_report(version: str, status: str) -> dict[str, Any]:
    return {
        "schema_version": version,
        "status": status,
        "counts": {
            "valid_cards": 0,
            "invalid_cards": 0,
            "warnings": 0,
            "review_sensitive_changes": 0,
        },
        "findings": [],
        "warnings": [],
        "privacy": {
            "pii_required": False,
            "sensitive_data_allowed": False,
            "absolute_paths_redacted": True,
        },
    }


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def missing_path_finding(role: str) -> dict[str, str]:
    return {
        "code": "missing_path",
        "path_role": role,
        "message": f"Required {role} path does not exist.",
    }


def validate(args: argparse.Namespace) -> int:
    source = Path(args.source)
    schemas = Path(args.schemas)
    media = Path(args.media)
    out = Path(args.out)

    version = schema_version(schemas) if schemas.exists() else DEFAULT_SCHEMA_VERSION
    report = base_report(version, "pass")

    missing_roles = [
        role
        for role, path in (("source", source), ("schemas", schemas), ("media", media))
        if not path.exists()
    ]
    if missing_roles:
        report["status"] = "error"
        report["findings"] = [missing_path_finding(role) for role in missing_roles]
        write_report(out, report)
        return 2

    card_files = sorted(
        path
        for path in source.rglob("*")
        if path.is_file() and path.suffix.lower() in CARD_SUFFIXES
    )
    if not card_files:
        report["warnings"].append(
            {
                "code": "no_cards_found",
                "message": "No content card files were found under the source path.",
            }
        )
        report["counts"]["warnings"] = 1

    write_report(out, report)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return validate(args)
    except OSError as exc:
        out = Path(args.out)
        report = base_report(DEFAULT_SCHEMA_VERSION, "error")
        report["findings"] = [
            {
                "code": "io_error",
                "message": exc.__class__.__name__,
            }
        ]
        write_report(out, report)
        return 2


if __name__ == "__main__":
    sys.exit(main())
