# Validation Tools

Superseded structured-platform artifact.

The tools in this directory belonged to the prior structured content-schema platform. That direction has been superseded by the Markdown-first primer direction.

Do not use `tools/validation/` as active Markdown-first v0.1 implementation guidance. New lightweight checks for the Markdown-first contract belong under `tools/checks/` in the reviewed M2 milestone.

Historical local validation entry points:

```sh
python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json
python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json --emit-public generated/public-content.json
python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI" -- generated/validation-report.json
```

`privacy_scan.py` is a negative-match check: exit `0` means clean, exit `1`
means a forbidden pattern was found, and exit `2` means setup or scan error.

`--emit-public` writes a deterministic public content package containing only
valid, published, approved, repository-native cards. It is generated evidence,
not Markdown-first source of truth.

CI is not configured yet.
