# Validation Tools

Local validation entry points:

```sh
python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json
python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI" -- generated/validation-report.json
```

`privacy_scan.py` is a negative-match check: exit `0` means clean, exit `1`
means a forbidden pattern was found, and exit `2` means setup or scan error.
