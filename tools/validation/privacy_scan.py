#!/usr/bin/env python3
"""Negative-match privacy scanner with stable exit semantics."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


DEFAULT_REPORT = Path("generated/privacy-scan-report.json")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scan files for forbidden privacy patterns.")
    parser.add_argument("--pattern", required=True, help="Regular expression for forbidden text.")
    parser.add_argument("--report", default=str(DEFAULT_REPORT), help="JSON report path.")
    parser.add_argument("targets", nargs="+", help="Files or directories to scan.")
    return parser


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def report_base(status: str) -> dict[str, Any]:
    return {
        "status": status,
        "target_count": 0,
        "findings": [],
    }


def iter_files(targets: Iterable[Path]) -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    missing: list[str] = []
    for target in targets:
        if not target.exists():
            missing.append("target")
            continue
        if target.is_dir():
            files.extend(sorted(path for path in target.rglob("*") if path.is_file()))
        elif target.is_file():
            files.append(target)
    return files, missing


def display_name(path: Path) -> str:
    return path.name


def scan(pattern: re.Pattern[str], files: list[Path]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for path in files:
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            findings.append(
                {
                    "code": "read_error",
                    "file": display_name(path),
                    "line": None,
                    "match": "[REDACTED]",
                }
            )
            continue

        for line_number, line in enumerate(lines, start=1):
            if pattern.search(line):
                findings.append(
                    {
                        "code": "forbidden_pattern_found",
                        "file": display_name(path),
                        "line": line_number,
                        "match": "[REDACTED]",
                    }
                )
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    report_path = Path(args.report)

    try:
        pattern = re.compile(args.pattern)
    except re.error:
        report = report_base("error")
        report["findings"] = [
            {
                "code": "invalid_regex",
                "message": "Pattern could not be compiled.",
            }
        ]
        write_report(report_path, report)
        return 2

    files, missing = iter_files(Path(target) for target in args.targets)
    if missing:
        report = report_base("error")
        report["findings"] = [
            {
                "code": "missing_target",
                "message": "One or more scan targets do not exist.",
            }
        ]
        write_report(report_path, report)
        return 2

    findings = scan(pattern, files)
    report = report_base("fail" if findings else "pass")
    report["target_count"] = len(files)
    report["findings"] = findings
    write_report(report_path, report)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
