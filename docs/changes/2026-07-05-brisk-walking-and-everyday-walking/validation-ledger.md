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

## M2 Validation

| Date | Command | Result | Notes |
| --- | --- | --- | --- |
| 2026-07-05 | `python3 -m unittest tests.test_markdown_first_real_pages` | pass | Ran 16 tests after adding walking page contract tests and both walking pages. |
| 2026-07-05 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md` | pass | Checked 4 Markdown files for focused M2 page validation. |
| 2026-07-05 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md` | pass | Checked 5 Markdown files using the test-spec CMD6 form; no image references were added. |
| 2026-07-05 | `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_markdown_first_real_pages` | pass | Ran 44 tests covering method, muscle/feel, and real-page contracts. |
| 2026-07-05 | `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | pass | Ran 65 Markdown-first tests. |
| 2026-07-05 | `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking` | pass | Checked 16 files. |

## M2 Notes

- Added focused failing tests first for `exercises/brisk-walking.md` and `principles/everyday-walking.md` existence, structure, method guidance, safety routing, source IDs, forbidden scope, and text-only media.
- Added `exercises/brisk-walking.md` as a text-only `basic_cardio_activity` page with talk-test, pace-reference, time/effort/progression, role-based muscle, technique, safety, and page-local source guidance.
- Added `principles/everyday-walking.md` as a text-only daily-movement principle page that distinguishes everyday walking from brisk walking and links to the brisk walking page.
- `SOURCES.md` was unaffected because the required reusable walking source IDs were already indexed before M2.
- `RED-FLAGS.md` was unaffected because the existing central safety route resolved and the walking pages only needed page-local links to it.
