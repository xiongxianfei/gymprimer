# Plan: Necessary Images and Baduanjin Exercise

## Status

- Status: completed
- Plan lifecycle state: completed
- Terminal disposition: completed by PR #14

## Purpose / big picture

This plan sequences the approved Baduanjin Basics direction into reviewable implementation milestones.
The change adds one beginner exercise page, records a ten-candidate image pool for that page, generates exactly five first-batch support images under the approved sequence-based exception, and proves the media remains subordinate to Markdown.

## Source artifacts

- Proposal: `docs/proposals/2026-07-06-necessary-images-and-baduanjin-exercise.md`
- Spec: `specs/necessary-images-and-baduanjin-exercise.md`
- Architecture: `docs/architecture/system/architecture.md`
- Test spec: `specs/necessary-images-and-baduanjin-exercise.test.md`
- Proposal review: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/proposal-review-r1.md`
- Spec review: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/spec-review-r1.md`
- Architecture review: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/architecture-review-r1.md`
- Test-spec review: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/test-spec-review-r1.md`

## Context and orientation

The product surface is Markdown-first.
The future implementation adds `exercises/baduanjin-basics.md` without turning Baduanjin into a full traditional course, medical qigong treatment page, martial curriculum, fall-prevention protocol, adaptive coaching flow, or video-first feature.

The first image batch is exactly five generated raster images:

- `media/exercises/baduanjin-basics/setup.png`
- `media/exercises/baduanjin-basics/two-hands-lift.png`
- `media/exercises/baduanjin-basics/drawing-bow.png`
- `media/exercises/baduanjin-basics/alternating-reach.png`
- `media/exercises/baduanjin-basics/muscle-attention.png`

Each generated raster image needs a matching prompt record under `media/prompts/exercises/baduanjin-basics/`, an approved `media/PROVENANCE.md` row, meaningful alt text, visual-safety review evidence, and beginner-comprehension proof.
Candidates 6-10 are deferred alternatives or future replacements, not permission to publish a sixth image without downstream approved exception justification.

## Non-goals

- No implementation before plan-review and test-spec-review.
- No full eight-brocade course, martial application, lineage debate, clinical protocol, fall-prevention program, or adaptive balance coaching.
- No borrowed web images, stock photos, screenshots, branded media, identifiable people, remote image references, video, animation, app, database, user account, or generated public JSON.
- No generated image as source-of-truth instruction, safety evidence, anatomy evidence, martial-form evidence, or programming guidance.

## Requirements covered

| Requirement range | Milestone or evidence surface |
|---|---|
| R1-R9 | M2 page path, title, aliases, sections, beginner scope, and non-clinical framing |
| R10-R20 | M2 setup, safety, source support, method guidance, and muscle guidance |
| R21-R29 | M1 proof map and M3 image-count / candidate-pool implementation |
| R30-R35 | M3 provenance and prompt records |
| R36-R40 | M1 validation expectations and M4 visual-safety evidence |
| R41-R42 | M4 beginner comprehension proof and rollback check |
| R43 | M1-M4 scope checks and validation |

## Current Handoff Summary

- Current milestone: Lifecycle Closeout
- Current milestone state: completed
- Last reviewed milestone: final holistic code-review
- Review status: final holistic code-review R1 passed with no material findings; explain-change complete; verify passed; PR #14 merged
- Remaining in-scope implementation milestones: none
- Next stage: none
- Final closeout readiness: complete
- Reason final closeout is or is not ready: PR #14 merged on 2026-07-06 with GitHub Actions `Validation checks` successful, and lifecycle cleanup is recorded on `main`.

## Milestones

### M1. Validation and Proof Map

- Milestone state: closed
- Goal: Add or update deterministic tests and proof obligations before content and media are introduced.
- Requirements: R21-R29, R36-R43
- Files/components likely touched:
  - `specs/necessary-images-and-baduanjin-exercise.test.md`
  - `tools/checks/check_markdown_first.py`
  - `tests/test_exercise_image_standard.py`
  - `tests/test_exercise_method_guidance.py`
  - `tests/test_markdown_first_real_pages.py`
  - `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/`
- Tests to add/update:
  - Page section and title checks for `exercises/baduanjin-basics.md`.
  - Method label checks for `Method type: low_load_control_drill` and required visible labels.
  - Image-count checks for exactly five first-batch images, no sixth image, and no second muscle-attention image.
  - Prompt-record and provenance checks for generated raster Baduanjin assets.
  - Forbidden-scope and privacy checks.
- Validation commands:
  - `python3 -m unittest tests.test_exercise_method_guidance`
  - `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
- Expected observable result: tests or proof obligations fail before the page, media, prompt records, provenance, and review evidence exist, then pass after later milestones.
- Implemented result:
  - Added a path-scoped five-image checker exception for `exercises/baduanjin-basics.md` while preserving the three-image default for other exercise pages.
  - Added Baduanjin image-standard fixtures for the first five images, sixth-image failure, second muscle-attention failure, prompt-record failure, out-of-scope visual wording failure, and unchanged default image limit.
  - Added Baduanjin `low_load_control_drill` fixtures for valid static guidance and invalid adaptive recovery-care wording.
  - Added change-local ranked candidate-pool evidence at `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/image-candidate-pool.md`.
  - Recorded rationale and validation in `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/explain-change.md` and `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md`.
- Validation results:
  - `python3 -m unittest tests.test_exercise_method_guidance` passed: 19 tests.
  - `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed: 55 tests.
  - `python3 -m unittest discover -s tests` passed: 174 tests.
  - `git diff --check` passed.
  - `python3 tools/checks/check_markdown_first.py docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/image-candidate-pool.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/explain-change.md` passed.
  - `python3 tools/checks/check_privacy.py docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` passed.
- Aligned-surface audit:
  - `exercises/baduanjin-basics.md` is intentionally unchanged for M1; it belongs to M2.
  - Baduanjin generated assets, prompt records, and `media/PROVENANCE.md` rows are intentionally unchanged for M1; they belong to M3.
  - Visual-safety review, beginner-comprehension proof, and rollback proof are intentionally unchanged for M1; they belong to M4.
- Code-review R1:
  - Finding CR-M1-001 requires direct BJ-T8 forbidden-scope fixture coverage for treatment, full-form, fall-prevention, and adaptive-coaching wording, or an upstream re-reviewed deferral.
- Review-resolution:
  - Added direct Baduanjin forbidden-scope fixtures for treatment protocol, full traditional form / all eight brocades, fall-prevention program, and adaptive coaching wording.
  - `python3 -m unittest tests.test_exercise_image_standard` passed: 26 tests.
  - `python3 -m unittest tests.test_exercise_method_guidance` passed: 19 tests.
  - `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed: 56 tests.
  - `python3 -m unittest discover -s tests` passed: 175 tests.
  - `git diff --check` passed.
- Code-review R2:
  - CR-M1-001 resolved.
  - M1 closed with no material findings.
- Risks:
  - Overfitting checks to one page could hide broader media regressions.
- Rollback/recovery:
  - Keep Baduanjin-specific checks gated to the approved page path and remove fixtures if the page scope changes upstream.

### M2. Baduanjin Markdown Page

- Milestone state: closed
- Goal: Draft the static beginner-facing Baduanjin Basics page without generated images.
- Requirements: R1-R20, R42-R43
- Files/components likely touched:
  - `exercises/baduanjin-basics.md`
  - `SOURCES.md`
  - `RED-FLAGS.md` only if existing routing is insufficient
- Tests to add/update:
  - Page structure, source support, source-index, method guidance, forbidden wording, and privacy checks.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md SOURCES.md RED-FLAGS.md`
  - `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md SOURCES.md`
  - `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
- Expected observable result: the page passes text-only checks and remains valid without image references.
- Implemented result:
  - Added `exercises/baduanjin-basics.md` as a text-only beginner page with required title, alias line, sections, movement steps, setup and safety guidance, method labels, and broad muscle guidance.
  - Added `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/source-audit.md`.
  - Added real-page Baduanjin tests in `tests/test_markdown_first_real_pages.py`.
  - Updated `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` to include the new text-only page.
- Validation results:
  - `python3 -m unittest tests.test_markdown_first_real_pages` passed: 36 tests.
  - `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/source-audit.md docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` passed.
  - `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md SOURCES.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/source-audit.md docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` passed.
  - `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages` passed: 55 tests.
  - `python3 -m unittest discover -s tests` passed: 181 tests.
  - `git diff --check` passed.
- Aligned-surface audit:
  - Baduanjin generated assets, prompt records, and `media/PROVENANCE.md` rows are intentionally unchanged for M2; they belong to M3.
  - Visual-safety review, beginner-comprehension proof, and rollback proof are intentionally unchanged for M2; they belong to M4.
- Code-review:
  - Code-review M2 R1 closed M2 with no material findings.
- Risks:
  - Content could drift into clinical, martial, lineage, or full-form instruction.
- Rollback/recovery:
  - Remove or narrow the page back to ready stance, two-hands-lift, and return-to-standing while preserving tests for forbidden scope.

### M3. Governed First Image Batch

- Milestone state: closed
- Goal: Generate and promote exactly five Baduanjin support images through the governed media workflow.
- Requirements: R21-R40, R43
- Files/components likely touched:
  - `media/exercises/baduanjin-basics/setup.png`
  - `media/exercises/baduanjin-basics/two-hands-lift.png`
  - `media/exercises/baduanjin-basics/drawing-bow.png`
  - `media/exercises/baduanjin-basics/alternating-reach.png`
  - `media/exercises/baduanjin-basics/muscle-attention.png`
  - `media/prompts/exercises/baduanjin-basics/setup.md`
  - `media/prompts/exercises/baduanjin-basics/two-hands-lift.md`
  - `media/prompts/exercises/baduanjin-basics/drawing-bow.md`
  - `media/prompts/exercises/baduanjin-basics/alternating-reach.md`
  - `media/prompts/exercises/baduanjin-basics/muscle-attention.md`
  - `media/PROVENANCE.md`
  - `exercises/baduanjin-basics.md`
- Tests to add/update:
  - Media path, image-count, purpose, prompt-record, provenance, page-reference, review-status, and alt-text checks.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md`
  - `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/`
  - `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
- Expected observable result: the page references exactly five generated raster images with matching prompt records, approved provenance, valid purposes, and meaningful alt text.
- Implemented result:
  - Added exactly five generated raster assets under `media/exercises/baduanjin-basics/`.
  - Added exact prompt records under `media/prompts/exercises/baduanjin-basics/`.
  - Added approved `media/PROVENANCE.md` rows with expected media purposes and `exercises/baduanjin-basics.md` page refs.
  - Added five Markdown image references with meaningful alt text to `exercises/baduanjin-basics.md`.
  - Added `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/visual-safety-review.md`.
  - Updated `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` from text-only to the governed five-image batch.
- Validation results:
  - `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m3_images_are_local_prompt_backed_and_reviewed` failed before implementation because the page had zero image references.
  - `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m3_images_are_local_prompt_backed_and_reviewed` passed after implementation.
  - `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed: 63 tests.
  - `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/ docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` passed: checked 24 files.
  - `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/ docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` passed: checked 20 Markdown files.
  - `python3 -m unittest discover -s tests` passed: 182 tests.
  - `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/ docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` passed: checked 22 Markdown files.
  - `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/ docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` passed: checked 26 files.
  - `git diff --check` passed.
- Aligned-surface audit:
  - Beginner-comprehension proof and rollback proof are intentionally unchanged for M3; they belong to M4.
- Code-review:
  - Code-review M3 R1 closed M3 with no material findings.
- Risks:
  - A generated image may imply therapy, combat, exact correctness, overprecise anatomy, or identifying-person content.
- Rollback/recovery:
  - Remove the failed Markdown reference, unused asset, prompt record, and provenance row; keep the text-only page.

### M4. Review Evidence and Final Local Readiness

- Milestone state: closed
- Goal: Record manual visual-safety review, beginner comprehension proof, rollback proof, and final local validation evidence.
- Requirements: R40-R43
- Files/components likely touched:
  - `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/visual-safety-review.md`
  - `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/beginner-comprehension-proof.md`
  - `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/rollback-proof.md`
  - `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md`
- Tests to add/update:
  - Review-evidence presence checks if existing validation supports them.
  - Manual proof records when semantic criteria cannot be automated.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/`
  - `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/`
  - `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
- Expected observable result: manual evidence and automated checks support promotion of the Baduanjin page and first image batch.
- Implemented result:
  - Added `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/beginner-comprehension-proof.md`.
  - Added `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/rollback-proof.md`.
  - Added Baduanjin M4 proof-record checks to `tests/test_markdown_first_real_pages.py`.
  - Rehearsed a temporary text-only rollback state with Baduanjin image references, assets, prompt records, and provenance rows removed.
- Validation results:
  - `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_rollback_proof_records_text_only_cleanup` failed before implementation because proof files were missing.
  - `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_rollback_proof_records_text_only_cleanup` passed after implementation.
  - `tmp=/tmp/gymprimer-baduanjin-rollback.cr-m4-001; GYMPRIMER_ROOT="$tmp" python3 tools/checks/check_markdown_first.py "$tmp/exercises/baduanjin-basics.md" "$tmp/media/PROVENANCE.md" "$tmp/SOURCES.md" "$tmp/RED-FLAGS.md"` passed after CR-M4-001 correction: checked 4 Markdown files.
  - `tmp=/tmp/gymprimer-baduanjin-rollback.cr-m4-001; GYMPRIMER_ROOT="$tmp" python3 tools/checks/check_privacy.py "$tmp/exercises/baduanjin-basics.md" "$tmp/media/PROVENANCE.md" "$tmp/SOURCES.md" "$tmp/RED-FLAGS.md"` passed after CR-M4-001 correction: checked 4 files.
  - `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed: 84 tests.
  - `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` passed: checked 22 Markdown files.
  - `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` passed: checked 26 files.
  - `python3 -m unittest discover -s tests` passed: 184 tests.
  - `git diff --check` passed.
  - `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` passed: checked 24 Markdown files.
  - `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` passed: checked 28 files.
- Aligned-surface audit:
  - No generated asset, prompt-record, provenance, or page-reference changes were needed for M4.
- Code-review:
  - Finding CR-M4-001 requires the rollback proof to record a reproducible temporary-root command sequence and rerun the focused rollback Markdown-first and privacy checks.
- Review-resolution:
  - Updated rollback proof, validation notes, plan evidence, and change metadata to record concrete temporary-root commands for `/tmp/gymprimer-baduanjin-rollback.cr-m4-001`.
  - Reran the focused rollback Markdown-first and privacy checks from that concrete temporary root.
  - Reran M4 proof tests, full local unittest discovery, Markdown-first checks, privacy checks, and `git diff --check`.
- Code-review R2:
  - Closed CR-M4-001 and M4 with no material findings.
- Risks:
  - Beginner comprehension proof could be too vague or store private health information.
- Rollback/recovery:
  - Keep the text-only page and remove unapproved images, prompt records, provenance rows, and references.

## Validation plan

| Command | First required milestone | Purpose |
|---|---|---|
| `python3 -m unittest tests.test_exercise_method_guidance` | M1 | Method label and low-load control guidance fixtures. |
| `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | M1 | Image-count, prompt-record, provenance, and real-page behavior. |
| `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | M2 with existing paths; full by M4 | Markdown, source, media, review-evidence, and scope checks. |
| `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | M2 with existing paths; full by M4 | Privacy scan. |
| `python3 -m unittest discover -s tests` | M1 | Broad local unittest regression. |
| `git diff --check` | M1 | Whitespace sanity. |

## Risks and recovery

- Five images may create visual overload; recovery is to keep setup, one key movement, and muscle-attention images while deferring two images with updated evidence.
- Drawing-bow may look combat-focused; recovery is replacement before promotion.
- Muscle-attention may become too anatomical; recovery is replacement with broad-region highlighting.
- Prompt/provenance records may be incomplete; recovery is to block promotion until exact prompt records and approved rows exist.
- Static checks cannot prove reader comprehension; recovery is manual proof with non-identifying evidence.

## Dependencies

- Approved Baduanjin spec.
- Approved architecture update.
- Approved plan-review.
- Active test spec and approved test-spec-review before implementation.
- Existing exercise-image, prompt-record, method, and muscle-guidance contracts.

## Progress

- 2026-07-06: Plan drafted during `$workflow auto: test-spec-review`.
- 2026-07-06: Plan-review R1 approved this plan.
- 2026-07-06: M1 implementation added validation fixtures, path-scoped checker support, candidate-pool evidence, and validation notes; milestone moved to code-review.
- 2026-07-06: Code-review R1 requested changes for CR-M1-001; M1 moved to review-resolution.
- 2026-07-06: CR-M1-001 resolution added focused forbidden-scope fixtures and returned M1 to code-review rereview.
- 2026-07-06: Code-review R2 closed M1; next stage is M2 implementation.
- 2026-07-06: M2 implementation added the text-only Baduanjin page, source audit, real-page tests, and exercise-image audit inventory row; milestone moved to code-review.
- 2026-07-06: Code-review M2 R1 closed M2; next stage is M3 implementation.
- 2026-07-06: M3 implementation added the governed first image batch, prompt records, provenance rows, page references, visual-safety review, and real-page media tests; milestone moved to code-review.
- 2026-07-06: Code-review M3 R1 closed M3; next stage is M4 implementation.
- 2026-07-06: M4 implementation added beginner-comprehension proof, rollback proof, proof-record tests, temporary rollback validation, and final local validation evidence; milestone moved to code-review.
- 2026-07-06: Code-review M4 R1 requested changes for CR-M4-001; M4 moved to review-resolution.
- 2026-07-06: CR-M4-001 resolution recorded concrete rollback commands and returned M4 to code-review rereview.
- 2026-07-06: Code-review M4 R2 closed CR-M4-001 and M4; final closeout is next.
- 2026-07-06: Final holistic code-review R1 passed with no material findings; explain-change is next.
- 2026-07-06: Explain-change refreshed the final reviewed-diff rationale; verify is next.
- 2026-07-06: Final local verify passed; PR handoff is next.
- 2026-07-06: PR #14 opened from `proposal/baduanjin-exercise-images` to `main`; hosted CI is pending.
- 2026-07-06: PR #14 merged with GitHub Actions `Validation checks` successful; lifecycle cleanup marked the change complete on `main`.

## Decision log

| Date | Decision | Reason | Rejected alternatives |
|---|---|---|---|
| 2026-07-06 | Use four implementation milestones. | Separates proof map, text page, governed images, and manual evidence. | One large implementation milestone. |
| 2026-07-06 | Generate images only after text page and proof map. | Keeps media subordinate to Markdown and validates rollback. | Generate images first. |
| 2026-07-06 | Keep five-image exception page-specific. | Baduanjin is sequence-based, but the global exercise-image default should not drift. | Change the global limit. |

## Surprises and discoveries

- None yet.

## Validation notes

- Authoring-stage validation is recorded in the workflow final response.
- Implementation validation will be recorded per milestone.

## Outcome and retrospective

Not applicable yet.

## Readiness

This plan is approved after plan-review R1 and is ready for test-spec authoring.

Implementation is not allowed until test-spec-review approves the proof map.

## Sources

- `specs/necessary-images-and-baduanjin-exercise.md`
- `docs/architecture/system/architecture.md`
- `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/architecture-review-r1.md`
- `docs/proposals/2026-07-06-necessary-images-and-baduanjin-exercise.md`
