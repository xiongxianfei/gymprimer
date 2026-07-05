# Review Resolution: Exercise Muscle Guidance Standard

## Status

closed

## Findings

| Finding ID | Review | Severity | Required outcome | Status |
| --- | --- | --- | --- | --- |
| CR-XMG-M1-1 | `docs/changes/exercise-muscle-guidance-standard/reviews/code-review-m1-r1.md` | major | Add deterministic XMG-T8 source-surface coverage for adopted muscle guidance without broad migration. | resolved |

## Resolution Notes

- 2026-07-04: Opened CR-XMG-M1-1 from code-review M1 R1. M1 implemented heading, role, legacy, and wording checks, but omitted the required source-support surface fixture/check from XMG-T8.
- 2026-07-04: Addressed CR-XMG-M1-1 by adding focused source-surface tests and minimal structural checker behavior. Re-review is required before M1 can close.
- 2026-07-04: Code-review M1 R2 accepted the resolution and closed M1.

## CR-XMG-M1-1 - Missing XMG-T8 Source-Surface Proof

Required outcome:

- M1 must include deterministic source-surface coverage for adopted muscle guidance.
- Tests must prove missing or global-only support for source-sensitive muscle guidance fails where deterministic.
- Semantic source adequacy must remain a manual-review responsibility.
- Untouched legacy `## Used muscles` pages must remain compatible.

Safe resolution path:

- Add a focused failing test in `tests/test_exercise_muscle_guidance.py` for an adopted `## Muscles involved` role claim without page-local citation/source structure.
- Add a focused failing test for a source-sensitive technical muscle or safety-style muscle/feel claim that relies only on global source indexing if feasible within the existing source parser.
- Implement minimal checker behavior in `tools/checks/check_markdown_first.py` that checks source-surface presence in adopted muscle and feel sections without trying to prove semantic source truth.
- Rerun M1 validation commands and return M1 to code-review.

Resolution evidence:

- Added `test_source_sensitive_role_guidance_requires_page_local_source_surface` to `tests/test_exercise_muscle_guidance.py`.
- Added structural source-surface checks to `validate_exercise_muscle_guidance()`:
  - explicit role or phase guidance requires at least one source citation in `## Muscles involved`;
  - citations in muscle or feel sections must have page-local reference definitions.
- Semantic source truth remains outside automation and is still routed to manual audit.
- Untouched legacy `## Used muscles` pages remain compatible.

Validation:

- `python3 -m unittest tests.test_exercise_muscle_guidance` passed.
- `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` passed.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises` passed.
- `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-muscle-guidance-standard` passed.
- `git diff --check` passed.
