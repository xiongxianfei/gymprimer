# Explain Change: Content Schema Foundation M1

## Scope

M1 implements the repository scaffold, schema shells, validator harness, privacy scan helper, and first local tests for the approved content-schema foundation.

This change does not implement card-shape validation, taxonomy validation, lifecycle review routing, generated public content, CI, UI, CMS, AI behavior, legal policy, or public exercise content.

## Changes

- Added repository-native source directories under `content/`, `media/`, `schemas/`, `tools/validation/`, `tests/`, and `generated/`.
- Added M1 schema shell files for card, taxonomy, media metadata, review event, audit event, and validation report records.
- Added `tools/validation/validate_content.py` as the local validation entry point.
- Added `tools/validation/privacy_scan.py` with negative-match exit semantics:
  - `0`: scan completed and no forbidden pattern was found.
  - `1`: forbidden pattern found.
  - `2`: setup, regex, path, or scan error.
- Added `unittest` coverage for validator report shape, deterministic output, privacy-safe error output, and privacy-scan exit behavior.
- Added generated validation evidence and MP5 developer-command documentation proof for M1.

## Requirement Coverage

- R30 and AC33: validation reports identify actionable failure records without stack traces.
- R31 and R40: validation and privacy-scan reports avoid private contact data, PHI, secrets, credentials, local paths, and PII-dependent behavior.
- R38: reports include `content-schema-v1`.
- AC34: source, schema, media, validation, generated-output, and review evidence boundaries now exist for downstream architecture-aligned implementation.

R1 is scaffolded but full card-ID validation remains in M2, where card content fixtures are introduced.

## Validation

- `python3 -m unittest discover -s tests`
- `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json`
- `python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI" -- generated/validation-report.json`

All commands passed locally. CI is not configured.
