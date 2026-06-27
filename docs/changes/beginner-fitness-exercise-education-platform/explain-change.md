# Explain Change: Content Schema Foundation M1-M4

## Scope

M1 established the repository scaffold, schema shells, validator harness, privacy scan helper, and first local tests. M2 adds executable validation for the v1 card content contract. M3 adds lifecycle, review-routing, publication eligibility, approval-event, and audit-event validation. M3 review-resolution makes review routing policy-driven and gates `review_expired -> approved` on recorded review-completion evidence. M4 adds deterministic public content package emission for eligible reviewed cards.

This change does not implement CI, UI, CMS, AI behavior, legal policy, public launch operations, or a broad exercise library.

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
- Added M3 tests and fixtures for lifecycle transitions, review-sensitive edits, publication eligibility, review-routing obligations, elevated-risk default-deny, blocked rehab publication blocking, approval events, and audit events.
- Added review-event and audit-event schema summaries plus `content/policies/review-routing-v1.json`.
- Updated the validator to load `content/policies/review-routing-v1.json` as the executable review-routing source of truth and report policy metadata.
- Added a special lifecycle gate so `review_expired -> approved` requires `review_completion` plus current digest-scoped approvals.
- Added `--emit-public` to produce `generated/public-content.json` from valid, published, approved repository-native cards only.
- Added M4 generated-output tests for deterministic reruns, non-public content exclusion, discovery fields, source-boundary behavior, and 60-card local performance smoke.
- Added generated validation evidence and MP3 fixture privacy proof for M2.
- Added generated lifecycle/review-routing validation evidence and MP1 lifecycle state-sync proof for M3.
- Added generated public-content evidence plus MP2 source-boundary and MP4 scope/non-goal proofs for M4.

## Requirement Coverage

- R1-R8 and AC1-AC3, AC22-AC25c: card identity, required `en-US`, optional `zh-Hans`, controlled enums, unknown taxonomy rejection, and bare `en` rejection.
- R9-R13 and AC4-AC5: canonical SVG step count, media path existence, and accessible text for each published locale.
- R14-R18 and AC6: required disclaimer, narrow diagnosis/treatment blockers, readiness-tied progressions, and required regressions.
- R30-R33 and AC7, AC26-AC27, AC32-AC33: actionable validation findings, privacy-safe reports, license metadata, contribution provenance, and review metadata blockers.
- R37-R40 and AC34: no user-specific program fields, no PII dependency, schema versioning, and architecture-aligned source/schema/media/generated boundaries.

- R19-R29 and AC8-AC21, AC28-AC31: separate lifecycle state fields, allowed transition validation, review-sensitive edit rules, hiding/superseding/reverting support, digest-scoped approval events, review-routing tier checks, elevated-risk default-deny, blocked-rehab publication blocking, and audit-event schema checks.
- R34-R36 and AC34: generated public output exposes discovery fields, relationships/prompts placeholders, and deterministic repository-reviewed source boundaries.

Future UX/search behavior remains out of scope.

## Validation

- `python3 -m unittest discover -s tests`
- `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json`
- `python3 tools/validation/validate_content.py --source tests/fixtures/invalid --schemas schemas --media media --out generated/invalid-fixture-report.json --expect-invalid`
- `python3 tools/validation/validate_content.py --source tests/fixtures/lifecycle --schemas schemas --media media --out generated/lifecycle-validation-report.json --expect-mixed`
- `python3 tools/validation/validate_content.py --source tests/fixtures/review-routing --schemas schemas --media media --out generated/review-routing-validation-report.json --expect-mixed`
- `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json --emit-public generated/public-content.json`
- `diff -u generated/public-content.json /tmp/gymprimer-public-content.json`
- `python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI|personal health" -- generated/`

All commands passed locally. CI is not configured.
