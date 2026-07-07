# Plan: Top-Five Generated Images for Fewer-Than-Five Exercise Documents

## Status

- Status: reviewed
- Plan lifecycle state: active
- Terminal disposition: not terminal

## Purpose / big picture

This plan sequences the approved named-population top-five image initiative into three implementation milestones.
The change evaluates the eighteen included exercise documents, counts accepted existing images toward five total images, generates only the missing images needed to reach each page's approved target, and updates validation so the repository-local reviewer exception applies only to this initiative.

## Source artifacts

- Proposal: `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- Spec: `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- Architecture: `docs/architecture/system/architecture.md`
- Spec review: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/spec-review-r1.md`
- Architecture review: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/architecture-review-r1.md`

## Context and orientation

The initiative is a named exception to the normal exercise-image policy.
It applies only to the eighteen included exercise documents and excludes `exercises/baduanjin-basics.md`.
Existing accepted images and accepted older sequence images count toward the five total image target.
New generated raster images still need prompt records, provenance rows, local page references, meaningful alt text, source support, privacy checks, beginner-comprehension proof, and rollback proof.
Repository-local `human_reviewer`, review-owner, visual-safety-review evidence, and replacement accountability artifacts are not required for this initiative after the approved spec is implemented.

## Non-goals

- No implementation before test-spec-review.
- No images for `exercises/baduanjin-basics.md`.
- No sixth image without later approved page-specific exception.
- No second muscle-attention image on any exercise page.
- No borrowed web images, stock photos, remote image references, hosted service, video, animation, app, database, account, generated public API, or personalized coaching.

## Requirements covered

| Requirement range | Milestone or evidence surface |
|---|---|
| R1-R6 | M1 population and accepted-existing-image audit |
| R7-R14 | M1 candidate and count audit, M2-M3 generated image targeting |
| R15-R24 | M1 validation update and M2-M3 media implementation |
| R25-R28 | M1 audit policy and M2-M3 page-batch implementation |
| R29-R30 | M1-M3 scope checks |

## Current Handoff Summary

- Current milestone: M3
- Current milestone state: closed
- Last reviewed milestone: M3
- Review status: code-review R5 clean-with-notes; M3 closed
- Remaining in-scope implementation milestones: none
- Next stage: pr
- Final closeout readiness: ready for PR handoff
- Reason final closeout is or is not ready: all implementation milestones are closed, explain-change is recorded, and final local verify passed; PR handoff remains.

## Milestones

### M1. Validation and Audit Framework

- Milestone state: closed
- Goal: Update deterministic validation and evidence structure for the named population, five-total-image counting, accepted existing image counting, older sequence image counting, no-sixth-image behavior, duplicate muscle-attention rejection, and repository reviewer exception.
- Requirements: R1-R15, R20-R22A, R25-R30
- Files/components likely touched:
  - `tools/checks/check_markdown_first.py`
  - `tools/checks/exercise_document_image_prioritization.py`
  - `tests/test_exercise_image_standard.py`
  - `tests/test_exercise_document_image_prioritization.py`
  - `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/`
- Tests to add/update:
  - Named included and excluded population fixtures.
  - Five-total-image counting fixtures with existing accepted images.
  - Older sequence image counting fixture.
  - Blank `human_reviewer` and missing repository-local review evidence allowed only for the named initiative.
  - Sixth-image and duplicate muscle-attention failures.
- Validation commands:
  - `python3 -m unittest tests.test_exercise_image_standard tests.test_exercise_document_image_prioritization`
  - `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents`
  - `python3 tools/checks/check_privacy.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents`
  - `git diff --check`
- Expected observable result: tests fail before implementation for the new exception and pass after validation updates.
- Risks: The exception could leak to other exercise pages.
- Rollback/recovery: Remove the named exception and keep the prior exercise-image standard behavior.

### M2. First Milestone Batch Images

- Milestone state: closed
- Goal: Audit and implement generated-image gaps for the first batch of included exercise documents.
- Requirements: R1-R30
- Files/components likely touched:
  - Selected `exercises/*.md` pages from the included population.
  - `media/exercises/<exercise-slug>/`
  - `media/prompts/exercises/<exercise-slug>/`
  - `media/PROVENANCE.md`
  - Batch evidence under the change directory.
- Tests to add/update:
  - Real-page image-count, prompt-record, provenance, page-ref, alt-text, and source-support checks for the batch.
- Validation commands:
  - `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`
  - `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents`
  - `python3 tools/checks/check_privacy.py exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents`
  - `git diff --check`
- Expected observable result: first batch pages reach the approved total image target or record a coverage-limit outcome.
- Risks: Generated assets may be visually low quality or duplicate existing coverage.
- Rollback/recovery: Remove the failed Markdown image reference, unused asset, prompt record, and provenance row.

### M3. Remaining Milestone Batch Images and Closeout Evidence

- Milestone state: closed
- Goal: Complete the remaining included exercise documents and record final batch-level comprehension and rollback evidence.
- Requirements: R1-R30
- Files/components likely touched:
  - Remaining included `exercises/*.md` pages.
  - Remaining `media/exercises/<exercise-slug>/` assets.
  - Remaining prompt records and provenance rows.
  - Final batch evidence under the change directory.
- Tests to add/update:
  - Full named-population real-page coverage.
  - Rollback proof fixtures or evidence scan.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents`
  - `python3 tools/checks/check_privacy.py exercises media media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents`
  - `git diff --check`
- Expected observable result: all included documents are complete or have documented coverage-limit outcomes.
- Risks: Large generated-media diff becomes hard to review.
- Rollback/recovery: Revert any failed page batch independently while preserving completed pages.

## Validation plan

Validation starts with focused unit tests in M1, expands to real-page media checks in M2, and finishes with broad repository test discovery plus Markdown/privacy checks in M3.
Each milestone must report exact commands and outcomes before code-review.

## Risks and recovery

| Risk | Recovery |
|---|---|
| Reviewer exception leaks beyond the named population. | Add negative fixtures and keep path-scoped validation. |
| Image count becomes filler-driven. | Require page-local audit and coverage-limit outcome below five when needed. |
| Generated assets create large rollback cost. | Keep each page's references, assets, prompt records, and provenance rows independently removable. |
| Existing useful images are overwritten. | Count accepted existing and older sequence images toward five total images. |

## Dependencies

- Proposal accepted.
- Spec approved.
- Architecture review approved.
- Plan-review approved.
- Test-spec-review approved before implementation.

## Progress

- Proposal accepted after proposal-review R2.
- Spec-review R1 approved.
- Architecture-review R1 approved.
- Plan created for plan-review.
- M1 implementation added named-population audit validation, five-total image counting, top-five rank 1-5 generation dispositions for this initiative, sixth-image rejection, duplicate muscle-attention rejection, and path-scoped reviewer exceptions.
- M1 added change-local audit framework evidence at `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/m1-audit-framework.md`.
- M2 selected `exercises/band-pull-apart.md` and `exercises/bird-dog.md` as the first generated-image batch.
- M2 promoted two new band pull-apart images and four new bird dog images with prompt records, provenance rows, page references, and batch audit evidence.
- M3 promoted the remaining top-five batch images for `brisk-walking`, `chest-press`, `chin-nod`, `dead-bug`, `glute-bridge`, `hip-hinge`, `incline-push-up`, `kneeling-hip-flexor-stretch`, `lat-pulldown`, `plank`, `prone-y-t`, `rowing-machine`, `seated-row`, `tai-chi-basics`, `thoracic-extension`, and `wall-slide`.
- M3 added prompt records, provenance rows, page references, and final remaining-batch audit evidence at `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m3-remaining-batch-audit.md`.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-06 | Use three implementation milestones. | Separates validation framework, first batch, and remaining batch closeout. | One page per slice; one giant all-media milestone. |
| 2026-07-06 | Keep reviewer exception path-scoped. | Prevents accidental global weakening of the exercise-image standard. | Global removal of reviewer fields. |
| 2026-07-06 | Use band pull-apart and bird dog for M2. | Exercises cover an existing modern-media page and an older sequence-image page while keeping the generated batch reviewable. | Starting with a large all-page generated-media batch. |
| 2026-07-06 | Leave band pull-apart at four total images for M2. | The fifth generated candidate duplicated existing movement coverage, so it would add count without distinct page value. | Promoting the duplicate chest-height movement candidate solely to reach five images. |
| 2026-07-06 | Use deterministic crops from accepted generated sequence and movement images where they improve single-position readability. | Crops preserve accepted older images while adding clearer page-local references without replacing the sequence source. | Replacing accepted sequence images for style alone. |

## Surprises and discoveries

- `tests/test_exercise_image_standard.py` contained temporary-directory checks that ran after fixture cleanup in two older branches; M1 moved those checks inside the fixture lifetime while preserving their original validation purpose.
- `exercises/tai-chi-basics.md` is part of the named top-five population, so its older fourth-image failure fixture was updated to allow four images while still rejecting a second muscle-attention image.
- `exercises/band-pull-apart.md` did not need five promoted images in M2 because the generated fifth candidate overlapped the existing movement image.
- M3 had no local image-library dependency available for scripted cropping, so deterministic `ffmpeg` crops were used for derived support images.

## Validation notes

- M1 red test command before implementation: `python3 -m unittest tests.test_exercise_image_standard tests.test_exercise_document_image_prioritization` failed because named-population helpers were missing and blank named-initiative reviewers were rejected.
- M1 focused unit validation after implementation: `python3 -m unittest tests.test_exercise_image_standard tests.test_exercise_document_image_prioritization` passed with 46 tests.
- M1 markdown validation: `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed.
- M1 privacy validation: `python3 tools/checks/check_privacy.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed.
- M1 whitespace validation: `git diff --check` passed.
- M1 code-review R1 recorded changes requested for score field alignment and named `automatic_generation` rejection.
- M1 review-resolution for CR-T5IMG-M1-1: `python3 -m unittest tests.test_exercise_document_image_prioritization tests.test_exercise_image_standard` passed with 47 tests.
- M1 review-resolution for CR-T5IMG-M1-1: `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed.
- M1 review-resolution for CR-T5IMG-M1-1: `python3 tools/checks/check_privacy.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed.
- M1 review-resolution for CR-T5IMG-M1-1: `git diff --check` passed.
- M1 review-resolution for CR-T5IMG-M1-2: `python3 -m unittest tests.test_exercise_document_image_prioritization tests.test_exercise_image_standard` passed with 47 tests.
- M1 review-resolution for CR-T5IMG-M1-2: `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed.
- M1 review-resolution for CR-T5IMG-M1-2: `python3 tools/checks/check_privacy.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed.
- M1 review-resolution for CR-T5IMG-M1-2: `git diff --check` passed.
- M1 code-review R2: `python3 -m unittest tests.test_exercise_document_image_prioritization tests.test_exercise_image_standard` passed with 47 tests.
- M1 code-review R2: `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed.
- M1 code-review R2: `python3 tools/checks/check_privacy.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed.
- M1 code-review R2: `git diff --check` passed.
- M2 unit validation: `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed with 68 tests.
- M2 markdown validation: `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed.
- M2 privacy validation: `python3 tools/checks/check_privacy.py exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed.
- M2 whitespace validation: `git diff --check` passed.
- M2 code-review R3 requested changes: CR-T5IMG-M2-1 for the M2 audit's 0-3 score scale, and CR-T5IMG-M2-2 for `bird-dog/short-reach.png` not visibly supporting the shorter-reach teaching purpose.
- M2 code-review R3 reviewer validation: `python3 tools/checks/check_privacy.py exercises media media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed with 107 files.
- M2 code-review R3 reviewer validation: `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed with 32 Markdown files.
- M2 code-review R3 reviewer validation: `git diff --check` passed.
- M2 review-resolution for CR-T5IMG-M2-1: `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed with 68 tests.
- M2 review-resolution for CR-T5IMG-M2-1: `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed.
- M2 review-resolution for CR-T5IMG-M2-1: `python3 tools/checks/check_privacy.py exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed.
- M2 review-resolution for CR-T5IMG-M2-1: `git diff --check` passed.
- M2 review-resolution for CR-T5IMG-M2-2: `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed with 68 tests.
- M2 review-resolution for CR-T5IMG-M2-2: `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed.
- M2 review-resolution for CR-T5IMG-M2-2: `python3 tools/checks/check_privacy.py exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed.
- M2 review-resolution for CR-T5IMG-M2-2: `git diff --check` passed.
- M2 code-review R4: `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed with 68 tests.
- M2 code-review R4: `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed with 35 Markdown files.
- M2 code-review R4: `python3 tools/checks/check_privacy.py exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed with 63 files.
- M2 code-review R4: `git diff --check` passed.
- M3 red test before implementation: `python3 -m unittest tests.test_exercise_image_standard.ExerciseImageStandardTest.test_top_five_m3_remaining_batch_has_page_images_prompt_records_and_audit_evidence` failed because `m3-remaining-batch-audit.md` did not exist.
- M3 targeted regression after implementation: `python3 -m unittest tests.test_exercise_image_standard.ExerciseImageStandardTest.test_top_five_m3_remaining_batch_has_page_images_prompt_records_and_audit_evidence` passed.
- M3 broad unit validation: `python3 -m unittest discover -s tests` passed with 207 tests.
- M3 markdown validation: `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed with 37 Markdown files.
- M3 privacy validation: `python3 tools/checks/check_privacy.py exercises media media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed with 214 files.
- M3 whitespace validation: `git diff --check` passed.

## Outcome and retrospective

M3 code-review R5 closed the remaining generated-image batch with no material findings.
Explain-change recorded the reviewed-diff rationale in `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/explain-change.md`.
Final closeout is not complete until PR handoff finishes.

## Readiness

M1, M2, and M3 are closed. Explain-change is recorded. Final local verify passed. The next stage is pr.

## Sources

- `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/spec-review-r1.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/architecture-review-r1.md`
