# Validation Ledger: Brisk Walking and Everyday Walking Guidance

## M1 Validation

| Date | Command | Result | Notes |
| --- | --- | --- | --- |
| 2026-07-05 | `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_templates tests.test_markdown_first_real_pages` | pass | Ran 29 tests covering method scope, template cues, and real-page regressions. |
| 2026-07-05 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises` | pass | Checked 24 Markdown files. |
| 2026-07-05 | `python3 tools/checks/check_privacy.py specs/brisk-walking-and-everyday-walking.md specs/exercise-method-guidance.md docs/templates tools tests docs/changes/2026-07-05-brisk-walking-and-everyday-walking` | pass | Checked 78 files. |

## M1 Notes

- Added focused failing tests before implementation for `basic_cardio_activity` scope and template guidance.
- Implemented `basic_cardio_activity` as a visible method type scoped to `exercises/brisk-walking.md`.
- Kept `basic_cardio_equipment` scoped to rowing-machine pages and kept `loaded_carry` inactive.
- Added cardio-activity authoring cues to the exercise template without introducing hidden metadata or generated source-of-truth data.
