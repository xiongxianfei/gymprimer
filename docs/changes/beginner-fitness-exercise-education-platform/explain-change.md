# Explain Change: Content Schema Foundation M1-M2

## Scope

M1 established the repository scaffold, schema shells, validator harness, privacy scan helper, and first local tests. M2 adds executable validation for the v1 card content contract.

This change does not implement lifecycle transitions, review routing, generated public content, CI, UI, CMS, AI behavior, legal policy, public launch content, or a broad exercise library.

## Changes

- Added repository-native source directories under `content/`, `media/`, `schemas/`, `tools/validation/`, `tests/`, and `generated/`.
- Added `tools/validation/validate_content.py` as the local validation entry point, now covering M2 card contract checks.
- Added `tools/validation/privacy_scan.py` with negative-match exit semantics:
  - `0`: scan completed and no forbidden pattern was found.
  - `1`: forbidden pattern found.
  - `2`: setup, regex, path, or scan error.
- Added `content/taxonomy/v1.json` with the v1 controlled enums and seed muscle/equipment/movement IDs.
- Added one valid repository example card for the lat pulldown plus three canonical SVG step examples.
- Updated schema summary files for card, taxonomy, and media contracts.
- Added M2 tests for accepted `en-US` and `zh-Hans` card shape plus invalid locale, enum, taxonomy, SVG, safety, licensing, provenance, and review-metadata cases.
- Added generated validation evidence and MP3 fixture privacy proof for M2.

## Requirement Coverage

- R1-R8 and AC1-AC3, AC22-AC25c: card identity, required `en-US`, optional `zh-Hans`, controlled enums, unknown taxonomy rejection, and bare `en` rejection.
- R9-R13 and AC4-AC5: canonical SVG step count, media path existence, and accessible text for each published locale.
- R14-R18 and AC6: required disclaimer, narrow diagnosis/treatment blockers, readiness-tied progressions, and required regressions.
- R30-R33 and AC7, AC26-AC27, AC32-AC33: actionable validation findings, privacy-safe reports, license metadata, contribution provenance, and review metadata blockers.
- R37-R40 and AC34: no user-specific program fields, no PII dependency, schema versioning, and architecture-aligned source/schema/media/generated boundaries.

R19-R29, AC8-AC21, and AC28-AC31 remain M3 lifecycle, review-routing, publication eligibility, and audit work.

## Validation

- `python3 -m unittest discover -s tests`
- `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json`
- `python3 tools/validation/validate_content.py --source tests/fixtures/invalid --schemas schemas --media media --out generated/invalid-fixture-report.json --expect-invalid`
- `python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI" --report generated/privacy-scan-report.json -- generated/validation-report.json`

All commands passed locally. CI is not configured.
