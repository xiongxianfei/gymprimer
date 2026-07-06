# Explain Change: Necessary Images and Tai Chi Exercise

## M1 validation proof-map implementation

M1 adds Tai Chi-specific validation coverage before page content or image assets are introduced.
The implementation updates `tests/test_exercise_image_standard.py` with fixtures for the Tai Chi candidate-pool contract, the exact first-batch image paths and purposes, fourth-image rejection, second muscle-attention rejection, prompt-record failure, generic alt-text failure, and deterministic visual-safety text failure.

The implementation also updates `tests/test_exercise_method_guidance.py` with Tai Chi-specific `low_load_control_drill` method fixtures.
Those fixtures confirm that static low-load control wording passes and adaptive or rehab/treatment wording fails.

No checker code changed in M1.
The new tests passed against the existing method, media-purpose, image-count, prompt-record, provenance, alt-text, and visual-safety validation paths.
That keeps M1 scoped to proof coverage and avoids adding page-specific checker branches before a failing test demonstrates a gap.

## M2 Tai Chi Markdown page implementation

M2 adds `exercises/tai-chi-basics.md` as a text-only beginner page.
The page uses the approved title, required sections, ready-stance / weight-shift / opening-movement / return-to-standing breakdown, `Method type: low_load_control_drill`, visible beginner starting point, effort, rest, progression, and stop guidance.
It keeps generated images out of the page so M2 proves the Markdown-first fallback before the M3 image batch.

The page adds broad role-based muscle guidance for legs/glutes, trunk, shoulders/upper back, and feet/ankles.
It uses page-local Tai Chi source definitions, and `SOURCES.md` now indexes the reused NCCIH, Harvard Health, VA, and NHS source IDs.
`docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/source-audit.md` records MP1 claim samples for setup, safety, method, movement, muscle, feel, and stop-condition claims.

`tests/test_markdown_first_real_pages.py` now checks the real Tai Chi page shape, text-only rollback surface, beginner scope, source-index discipline, low-load method labels, broad muscle guidance, and M2 source-audit evidence.
`docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` also gets a Tai Chi text-only row because the existing image-standard test treats that audit as the current inventory of exercise pages.

## Validation evidence

- `python3 -m unittest tests.test_exercise_image_standard tests.test_exercise_method_guidance` passed after correcting an overly literal contract assertion.
- `python3 -m unittest tests.test_exercise_method_guidance` passed.
- `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed.
- `python3 -m unittest discover -s tests` passed.
- `git diff --check` passed.
- `python3 tools/checks/check_privacy.py tests/test_exercise_image_standard.py tests/test_exercise_method_guidance.py specs/necessary-images-and-tai-chi-exercise.test.md docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/` passed.
- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_page_exists_and_has_required_text_only_shape tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_setup_safety_sources_and_source_index tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_m2_source_audit_records_required_claim_samples` failed before M2 implementation because the page and source-audit file did not exist.
- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_page_exists_and_has_required_text_only_shape tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_beginner_scope_and_forbidden_product_language tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_setup_safety_sources_and_source_index tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_low_load_method_guidance tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_broad_muscle_and_feel_guidance tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_m2_source_audit_records_required_claim_samples` passed.
- `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md` passed.
- `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md media/PROVENANCE.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/ SOURCES.md` passed.
- `python3 -m unittest discover -s tests` initially failed because the current exercise-image audit did not list `exercises/tai-chi-basics.md`; after adding the text-only audit row it passed.
- `git diff --check` passed.

`python3 -m pytest` was attempted because the draft plan had named it, but it could not run in this environment because `pytest` is not installed.
The reviewed test spec command ledger uses unittest commands for M1/M2.
