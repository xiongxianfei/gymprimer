# Validation Notes: Necessary Images and Baduanjin Exercise

## Status

M4 implementation validation complete; code-review pending.

## 2026-07-06 M1

Scope validated:

- path-scoped five-image exception for `exercises/baduanjin-basics.md`;
- unchanged three-image default for other exercise pages;
- one muscle-attention image limit;
- prompt-record and visual-semantic negative fixtures for Baduanjin images;
- `low_load_control_drill` positive and negative method fixtures;
- ranked top-10 candidate-pool evidence before image generation.

Commands run:

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_exercise_method_guidance` | pass: 19 tests |
| `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass: 55 tests |
| `python3 -m unittest discover -s tests` | pass: 174 tests |
| `git diff --check` | pass |
| `python3 tools/checks/check_markdown_first.py docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/image-candidate-pool.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/explain-change.md` | pass: checked 5 Markdown files |
| `python3 tools/checks/check_privacy.py docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | pass: checked 12 files |

Residual risk:

- M1 does not implement `exercises/baduanjin-basics.md`, generated assets, prompt records, provenance rows, visual-safety review, beginner-comprehension proof, or rollback proof.
- Real-page integration tests for Baduanjin remain assigned to later milestones once those files exist.

## 2026-07-06 M1 Review Resolution

Scope validated:

- CR-M1-001 forbidden-scope fixture coverage for treatment protocol, full traditional form / all eight brocades, fall-prevention program, and adaptive coaching wording.

Commands run:

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_exercise_image_standard` | pass: 26 tests |
| `python3 -m unittest tests.test_exercise_method_guidance` | pass: 19 tests |
| `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass: 56 tests |
| `python3 -m unittest discover -s tests` | pass: 175 tests |
| `git diff --check` | pass |

## 2026-07-06 M2

Scope validated:

- text-only `exercises/baduanjin-basics.md`;
- required Baduanjin title, alias line, sections, and beginner movement breakdown;
- non-clinical, non-martial, static-page wording;
- setup and safety source support;
- `low_load_control_drill` method labels;
- broad role-based muscle and feel guidance;
- source-audit proof;
- current exercise-image audit inventory updated for the new text-only page.

Commands run:

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_markdown_first_real_pages` | pass: 36 tests |
| `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/source-audit.md` | pass after fixing source-audit references |
| `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md SOURCES.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/source-audit.md` | pass: checked 3 files |
| `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages` | pass: 55 tests |
| `python3 -m unittest discover -s tests` | pass: 181 tests |
| `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/source-audit.md docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | pass: checked 5 Markdown files |
| `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md SOURCES.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/source-audit.md docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | pass: checked 4 files |
| `git diff --check` | pass |

Residual risk:

- M2 does not generate or reference Baduanjin images.
- Prompt records, provenance rows, visual-safety review, beginner-comprehension proof, and rollback proof remain assigned to M3-M4.

## 2026-07-06 M3

Scope validated:

- exactly five Baduanjin first-batch image references on `exercises/baduanjin-basics.md`;
- local generated raster assets under `media/exercises/baduanjin-basics/`;
- exact prompt records under `media/prompts/exercises/baduanjin-basics/`;
- approved `media/PROVENANCE.md` rows with expected purposes and page refs;
- meaningful alt text for each Baduanjin image;
- manual visual-safety review evidence for the selected image batch;
- exercise-image audit inventory updated from text-only to the governed first image batch.

Commands run:

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m3_images_are_local_prompt_backed_and_reviewed` | fail before implementation: expected five image references, found zero |
| `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m3_images_are_local_prompt_backed_and_reviewed` | pass after adding images, prompt records, provenance rows, and page references |
| `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass: 63 tests |
| `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/ docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | pass: checked 24 files |
| `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/ docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | pass after adding `visual-safety-review.md` sources: checked 20 Markdown files |
| `python3 -m unittest discover -s tests` | pass: 182 tests |
| `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/ docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | pass: checked 22 Markdown files |
| `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/ docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | pass: checked 26 files |
| `git diff --check` | pass |

Residual risk:

- M3 does not record beginner comprehension proof or text-only rollback proof.
- M4 must still run final local validation and prove that removing image references, unused assets, prompt records, and provenance rows preserves the text-only page.

## 2026-07-06 M4

Scope validated:

- beginner-comprehension proof for Baduanjin purpose, ready stance, upward reach, drawing bow, alternating reach, body regions to notice, pause conditions, and image usefulness;
- rollback proof that the text-only page remains valid after Baduanjin image references, unused assets, prompt records, and provenance rows are removed in a temporary review state;
- final local validation across exercise method, image standard, real page, Markdown-first, privacy, and whitespace checks.

Temporary rollback rehearsal:

- Temporary root: `/tmp/gymprimer-baduanjin-rollback.*`
- `GYMPRIMER_ROOT=/tmp/gymprimer-baduanjin-rollback.* python3 tools/checks/check_markdown_first.py /tmp/gymprimer-baduanjin-rollback.*/exercises/baduanjin-basics.md /tmp/gymprimer-baduanjin-rollback.*/media/PROVENANCE.md /tmp/gymprimer-baduanjin-rollback.*/SOURCES.md /tmp/gymprimer-baduanjin-rollback.*/RED-FLAGS.md`: pass, checked 4 Markdown files.
- `GYMPRIMER_ROOT=/tmp/gymprimer-baduanjin-rollback.* python3 tools/checks/check_privacy.py /tmp/gymprimer-baduanjin-rollback.*/exercises/baduanjin-basics.md /tmp/gymprimer-baduanjin-rollback.*/media/PROVENANCE.md /tmp/gymprimer-baduanjin-rollback.*/SOURCES.md /tmp/gymprimer-baduanjin-rollback.*/RED-FLAGS.md`: pass, checked 4 files.

Commands run:

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_rollback_proof_records_text_only_cleanup` | fail before implementation: proof files missing |
| `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_rollback_proof_records_text_only_cleanup` | pass after adding proof files |
| `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/beginner-comprehension-proof.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/rollback-proof.md` | pass after adding claim-level safety source reference: checked 2 Markdown files |
| `python3 tools/checks/check_privacy.py docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/beginner-comprehension-proof.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/rollback-proof.md` | pass: checked 2 files |
| `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass: 84 tests |
| `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | pass: checked 22 Markdown files |
| `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | pass: checked 26 files |
| `python3 -m unittest discover -s tests` | pass: 184 tests |
| `git diff --check` | pass |
| `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | pass: checked 24 Markdown files |
| `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | pass: checked 28 files |

Residual risk:

- M4 records a non-identifying reviewer simulation for beginner comprehension.
- This does not replace future public-reader feedback after publication.

## Sources

- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
