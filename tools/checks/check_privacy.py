#!/usr/bin/env python3
"""Negative-match privacy scan for Markdown-first proof artifacts."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys


HOME_PATH_PATTERN = "/" + "home/"
SECRET_WORD = "sec" + "ret"
PHI_WORD = "P" + "HI"
PERSONAL_HEALTH_PATTERN = "personal " + "health profile"

FORBIDDEN_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "PF001",
        re.compile(
            rf"({re.escape(HOME_PATH_PATTERN)}|{SECRET_WORD}\s*[:=]|{SECRET_WORD}[-_ ]?(key|token)|{PHI_WORD}\s*[:=]|{PERSONAL_HEALTH_PATTERN})",
            re.IGNORECASE,
        ),
    ),
)


@dataclass(frozen=True)
class Finding:
    path: Path
    code: str
    line_number: int

    def format(self) -> str:
        return f"{self.path}: {self.code}: forbidden privacy pattern found on line {self.line_number}"


def iter_files(paths: list[Path]) -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    errors: list[str] = []

    for path in paths:
        if not path.exists():
            errors.append(f"setup: missing path: {path}")
            continue
        if path.is_dir():
            files.extend(sorted(p for p in path.rglob("*") if p.is_file()))
        else:
            files.append(path)

    return files, errors


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return findings

    for line_number, line in enumerate(lines, start=1):
        for code, pattern in FORBIDDEN_PATTERNS:
            if pattern.search(line):
                findings.append(Finding(path, code, line_number))
                break
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a negative-match privacy scan over files or directories.")
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to scan")
    args = parser.parse_args(argv)

    files, errors = iter_files(args.paths)
    if errors:
        for error in errors:
            print(error)
        return 2
    if not files:
        print("setup: no files found")
        return 2

    findings: list[Finding] = []
    for path in files:
        findings.extend(scan_file(path))

    if findings:
        for finding in findings:
            print(finding.format())
        return 1

    print(f"checked {len(files)} file(s): privacy pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
