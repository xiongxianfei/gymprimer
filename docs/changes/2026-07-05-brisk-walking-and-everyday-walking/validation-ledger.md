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

## M3 Validation

| Date | Command | Result | Notes |
| --- | --- | --- | --- |
| 2026-07-05 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md` | pass | Checked 5 Markdown files; walking pages remain text-only and media provenance remains unchanged. |
| 2026-07-05 | `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass | Ran after adding manual proof and updating the exercise-image audit for `exercises/brisk-walking.md`. |
| 2026-07-05 | `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | pass | Ran Markdown-first discovery after M3 proof records and ledger update. |
| 2026-07-05 | `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media docs/changes/2026-07-05-brisk-walking-and-everyday-walking` | pass | Checked 62 files; manual proof contains no private reader details or private health information. |

## M3 Notes

- Added focused failing tests first for walking manual proof files and required M3 validation ledger commands.
- Added `manual-proof/source-audit.md` with sampled claim categories for intensity, talk test, weekly activity guidance, less-sitting framing, walking technique, starter/progression, and stop rules.
- Added `manual-proof/beginner-comprehension.md` with non-identifying prompt outcomes for the approved walking questions.
- Added `manual-proof/optional-image-decision.md` and kept the first walking slice text-only because no comprehension gap required an image.
- Updated `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` to include the new text-only `exercises/brisk-walking.md` exercise page in the current exercise inventory.

## M4 Validation

| Date | Command | Result | Notes |
| --- | --- | --- | --- |
| 2026-07-05 | `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_brisk_walking_required_images_are_local_prompt_backed_and_reviewed tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_walking_m4_required_image_proof_records_visual_safety` | fail-then-pass | Failed before implementation because the required images and proof files were missing; passed after adding assets, prompt records, provenance, page references, and proof records. |
| 2026-07-05 | `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass | Ran 36 tests covering generated raster image constraints and real-page references. |
| 2026-07-05 | `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass | Ran 64 tests covering method, muscle, image, and real-page contracts. |
| 2026-07-05 | `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | pass | Ran 71 Markdown-first tests. |
| 2026-07-05 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md` | pass | Checked 5 Markdown files. |
| 2026-07-05 | `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media docs/changes/2026-07-05-brisk-walking-and-everyday-walking` | pass | Checked 75 files. |
| 2026-07-05 | `git diff --check` | pass | No whitespace errors. |

## M4 Notes

- Added focused failing tests first for required brisk-walking images, prompt/provenance wiring, visual-safety proof, and no everyday-walking image.
- Generated exactly two brisk-walking raster support images with the built-in image generation tool: `movement.png` and `muscle-attention.png`.
- Copied accepted assets to `media/exercises/brisk-walking/` and preserved the generated originals under `$CODEX_HOME/generated_images/`.
- Added exact prompt records under `media/prompts/exercises/brisk-walking/`.
- Added approved `media/PROVENANCE.md` rows with local paths, prompt records, image purposes, source inputs, review status, and page references.
- Added `manual-proof/required-image-decision.md` and `manual-proof/visual-safety.md`.
- Updated `exercises/brisk-walking.md` with two support-only image references and kept `principles/everyday-walking.md` text-only.
