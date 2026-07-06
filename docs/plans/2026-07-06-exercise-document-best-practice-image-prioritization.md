# Plan: Exercise Document Best-Practice Image Prioritization

## Status

- Status: active
- Plan lifecycle state: active
- Terminal disposition: not-applicable

## Purpose / big picture

Sequence the approved per-exercise-document image-prioritization contract into small, reviewable implementation work.
The plan starts with audit proof and validation infrastructure, then handles one selected exercise document or a deliberately small page batch.
It treats documents with fewer than five images as an evaluation population, not a generation target.

## Source artifacts

- Proposal: `../proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- Proposal review:
  - `../changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/proposal-review-r1.md`
  - `../changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/proposal-review-r2.md`
- Review resolution: `../changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`
- Spec: `../../specs/exercise-document-best-practice-image-prioritization.md`
- Spec review: `../changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/spec-review-r1.md`
- Architecture assessment: `../changes/2026-07-06-exercise-document-best-practice-image-prioritization/architecture-assessment.md`
- Governing exercise-image spec: `../../specs/exercise-image-standard.md`
- Governing media ADRs:
  - `../adr/2026-07-03-exercise-document-image-purposes.md`
  - `../adr/2026-07-03-generated-raster-prompt-records.md`

## Context and orientation

Exercise pages live under `exercises/`.
Generated exercise media lives under `media/exercises/<exercise-slug>/`, prompt records live under `media/prompts/exercises/<exercise-slug>/`, and generated raster provenance is centralized in `media/PROVENANCE.md`.
The current Markdown-first checker and exercise-image tests already govern media paths, prompt records, provenance, image purposes, one muscle-attention image, and image-count exceptions.

This plan adds a workflow layer around page-local audit and candidate prioritization.
It does not broaden the exercise-image standard's count policy.

## Non-goals

- Do not generate images before test-spec review and implementation milestones authorize them.
- Do not require exercise documents to reach five images.
- Do not evaluate a repository-wide top-10 list.
- Do not replace existing acceptable images for style alone.
- Do not update `docs/templates/exercise-card.md` before first-slice audit criteria are proven.
- Do not add new exercise pages, hosted app behavior, video-first media, clinical behavior, or personalized coaching.

## Requirements covered

- R1-R8: M1 records the evaluation population, audit schema, top-10 table fields, and candidate scoring rules.
- R9-R18: M1 and M2 separate top-five backlog from generated subset and preserve image-count, purpose, prompt/provenance, Markdown-source, and safety boundaries.
- R19-R22: M1 records older-image preservation and change-local proof before template updates.
- R23-R26: M2 and M3 keep implementation slices small, prove rollback, and preserve non-goals.
- AC1-AC8: M1-M3 plus review evidence provide acceptance proof before PR handoff.

## Current Handoff Summary

- Current milestone: Lifecycle Closeout
- Current milestone state: planned
- Last reviewed milestone: M3
- Review status: proposal-review R2 approved; spec-review R1 approved; architecture assessment recorded architecture-not-required; plan-review R1 approved; test-spec-review R1 approved; code-review M1 R2 closed M1 after CR-EDIP-M1-1 resolution; code-review M2 R2 closed M2 after CR-EDIP-M2-1 resolution; code-review M3 R1 closed M3.
- Remaining in-scope implementation milestones: none
- Next stage: pr
- Final closeout readiness: not ready
- Reason final closeout is or is not ready: implementation milestones, explain-change, final local verify, and PR opening are complete; hosted CI, author review, and lifecycle cleanup remain.

## Milestones

### M1. Audit Inventory and Proof Contract

- Milestone state: closed
- Goal: add or update tests and evidence surfaces for the evaluation population, page-local audit fields, top-10 candidate table, top-five backlog semantics, and older-image replacement reasons.
- Requirements: R1-R9, R19-R22, AC1-AC3, AC5.
- Likely files:
  - `tests/test_exercise_document_image_prioritization.py`
  - `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/`
  - possible focused helper in `tools/checks/` only if current checks cannot validate audit artifacts.
- Tests:
  - exercise document image counts identify fewer-than-five pages as evaluation population;
  - fewer-than-five status does not require generated images;
  - page-local audit fixtures require candidate fields and scoring dimensions;
  - top-five rows are backlog, not generation target;
  - style-only replacement rationale fails.
- Steps:
  - Add failing fixtures or tests for audit inventory and candidate-table behavior.
  - Implement the smallest local validation or proof helper needed for page-local audit artifacts.
  - Create first-slice audit criteria evidence under the change root.
  - Do not edit exercise pages or media assets in this milestone.
- Validation:
  - `python3 -m unittest tests.test_exercise_document_image_prioritization`
  - `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`
  - `python3 tools/checks/check_privacy.py -- docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization tests`
  - `git diff --check`
- Result: Closed by code-review M1 R2 after CR-EDIP-M1-1 resolution.
- Risks: audit helper over-specifies the first slice or accidentally treats five images as required.
- Rollback: remove the focused helper/tests/evidence and leave exercise content and media unchanged.

### M2. First Page-Specific Evaluation Slice

- Milestone state: closed
- Goal: apply the audit to one selected exercise document or deliberately small page batch, record top-10 candidates, and choose the minimum-needed generated subset.
- Requirements: R3-R18, R23, AC2-AC6.
- Likely files:
  - selected `exercises/*.md` pages only when page-local edits are approved by the audit;
  - `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/`;
  - optional `media/exercises/<exercise-slug>/`, `media/prompts/exercises/<exercise-slug>/`, and `media/PROVENANCE.md` only if the approved minimum-needed subset includes generated images.
- Tests:
  - selected page has page-local audit and top-10 table;
  - any generated subset stays within zero-to-three images unless approved page-specific exception exists;
  - no second muscle-attention image is introduced;
  - prompt/provenance/alt/page-reference checks cover generated assets when present.
- Steps:
  - Identify selected page or small batch from the fewer-than-five evaluation population.
  - Record image count, current image purposes, source support, existing-image preservation or replacement reasons, top-10 candidate table, and generation decision.
  - Add only the minimum-needed generated subset, if any, after prompt records and provenance rows are ready.
  - Keep setup, movement, muscles, safety, and citations in Markdown.
- Validation:
  - `python3 -m unittest tests.test_exercise_document_image_prioritization tests.test_exercise_image_standard tests.test_markdown_first_real_pages`
  - `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`
  - `python3 tools/checks/check_privacy.py -- exercises media docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`
  - `git diff --check`
- Result: Closed by code-review M2 R2 after CR-EDIP-M2-1 resolution.
- Risks: generated images create visual overload or unsupported claims.
- Rollback: remove page references, unused generated assets, prompt records, provenance rows, and keep the selected page readable as text.

### M3. Review Evidence and Closeout

- Milestone state: closed
- Goal: record visual-safety review, source-support audit, beginner-comprehension proof, rollback proof, and final local validation for the first slice.
- Requirements: R16-R18, R24-R26, AC6-AC8.
- Likely files:
  - `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/`
  - `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml`
  - `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`
  - `docs/plan.md`
- Tests:
  - proof artifacts contain required visual-safety, source-support, beginner-comprehension, privacy, and rollback fields;
  - final Markdown-first and privacy checks cover changed pages, media, prompts, provenance, and evidence.
- Steps:
  - Record manual proof for any generated image batch.
  - Record rollback proof using concrete local paths and commands.
  - Update lifecycle state and validation notes.
  - Route to final code review, explain-change, verify, and PR after implementation reviews are clean.
- Validation:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`
  - `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans media exercises tools tests`
  - `git diff --check`
- Result: Closed by code-review M3 R1.
- Risks: manual proof may be too global to prove page-level comprehension.
- Rollback: remove incomplete proof artifacts or return to M2 for corrected page-specific evidence.

## Validation plan

The proof strategy starts with focused tests for audit artifacts, then broadens to existing exercise-image and real-page checks only when page/media changes exist.
Manual proof is required for visual semantics, beginner comprehension, and rollback because static checks cannot prove those fully.

## Risks and recovery

| Risk | Recovery |
|---|---|
| Five-image trigger is misread as a five-image target. | M1 tests and evidence must fail wording or audit records that make generation mandatory. |
| Existing images are replaced for style alone. | Require concrete replacement reasons and preserve acceptable images. |
| Page-specific slice becomes too broad. | Keep M2 to one exercise document or a deliberately small batch. |
| Current validation cannot express an audit rule. | Add the narrowest helper/test, or return to architecture if shared validation architecture changes. |
| Generated assets fail safety or privacy review. | Roll back image references, assets, prompt records, and provenance rows. |

## Dependencies

- Approved spec and clean spec review.
- Architecture-not-required assessment.
- Clean plan review.
- Active test spec and clean test-spec review before implementation.
- Existing exercise-image standard, prompt-record ADR, provenance contract, and Markdown-first validation.

## Progress

- 2026-07-06: Proposal accepted after proposal-review R2.
- 2026-07-06: Spec approved by spec-review R1.
- 2026-07-06: Architecture assessment recorded `architecture-not-required`.
- 2026-07-06: Plan drafted and approved by plan-review R1.
- 2026-07-06: Test spec drafted and approved by test-spec-review R1.
- 2026-07-06: M1 implemented audit inventory and proof-contract helper/tests, recorded change-local audit criteria and current evaluation population, and routed to code-review M1.
- 2026-07-06: Code-review M1 R1 requested changes for CR-EDIP-M1-1; M1 routes to review-resolution.
- 2026-07-06: Review-resolution addressed CR-EDIP-M1-1 by rejecting top-five direct generation dispositions and adding focused tests; M1 routed back to code-review.
- 2026-07-06: Code-review M1 R2 confirmed CR-EDIP-M1-1 resolved, closed M1, and routed to implement M2.
- 2026-07-06: M2 implemented the first page-specific audit slice for `exercises/bird-dog.md`, selected zero generated images, and routed to code-review M2.
- 2026-07-06: Code-review M2 R1 requested changes for CR-EDIP-M2-1; M2 routes to review-resolution.
- 2026-07-06: Review-resolution addressed CR-EDIP-M2-1 by adding the required per-rank scoring matrix; M2 routes back to code-review.
- 2026-07-06: Code-review M2 R2 confirmed CR-EDIP-M2-1 resolved, closed M2, and routed to implement M3.
- 2026-07-06: M3 implemented review closeout proof for the zero-generated-image Bird Dog slice and routed to code-review M3.
- 2026-07-06: Code-review M3 R1 closed M3; final closeout begins with explain-change.
- 2026-07-06: Explain-change refreshed the durable rationale for the final reviewed M1-M3 diff; verify is next.
- 2026-07-06: Final local verify passed with branch-ready evidence; PR handoff is next.
- 2026-07-06: PR #15 opened from `proposal/exercise-document-image-prioritization` to `main`; GitHub Actions `Validation checks` is in progress.

## Decision log

| Date | Decision | Reason | Rejected alternatives |
|---|---|---|---|
| 2026-07-06 | Use a three-milestone implementation plan. | Separates audit proof, first page-specific slice, and manual closeout evidence. | Generate images in the planning stage. |
| 2026-07-06 | Keep template update out of M1. | The accepted proposal requires first-slice criteria to be proven change-locally first. | Update `docs/templates/exercise-card.md` immediately. |
| 2026-07-06 | Add a focused helper instead of extending the Markdown-first checker. | M1 needs deterministic audit-record validation, not product-page validation. | Overload `check_markdown_first.py` with change-local audit schema rules. |
| 2026-07-06 | Use Bird Dog as the first M2 page-specific audit. | It is in the fewer-than-five evaluation population and has an older sequence image that exercises the preserve-existing-image path without requiring generated media. | Start with a page that needs image generation. |

## Surprises and discoveries

- The existing exercise-image audit from 2026-07-03 is now stale for several pages because later page-specific image work added images. M1 records the current image counts directly in this change-local evidence.
- The first page-specific M2 audit can select zero generated images while still recording a top-10 backlog; this preserves the evaluation-trigger distinction.

## Validation notes

- `python3 -m unittest tests.test_exercise_document_image_prioritization` passed: 7 focused M1 tests.
- `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization` passed.
- `python3 tools/checks/check_privacy.py -- docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization tests` passed.
- `git diff --check` passed.
- State-sync inspection passed with `rg -n "Current stage: code-review M1|Current milestone state: review-requested|Next stage: code-review M1|current_stage: code-review|current_milestone_state: review-requested|next_stage: code-review|M1 implementation complete" docs/plan.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml`.
- Broader changed-artifact Markdown-first check passed with `python3 tools/checks/check_markdown_first.py docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md specs/exercise-document-best-practice-image-prioritization.md specs/exercise-document-best-practice-image-prioritization.test.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`.
- Broader changed-artifact privacy check passed with `python3 tools/checks/check_privacy.py -- docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md specs/exercise-document-best-practice-image-prioritization.md specs/exercise-document-best-practice-image-prioritization.test.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization tests tools`.
- CR-EDIP-M1-1 resolution validation passed with `python3 -m unittest tests.test_exercise_document_image_prioritization`.
- CR-EDIP-M1-1 resolution validation passed with `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`.
- CR-EDIP-M1-1 resolution validation passed with `python3 tools/checks/check_privacy.py -- docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization tests`.
- CR-EDIP-M1-1 resolution validation passed with `git diff --check`.
- CR-EDIP-M1-1 state-sync inspection passed with `rg -n "Current stage: code-review M1 re-review|Current milestone state: review-requested|Next stage: code-review M1 re-review|current_stage: code-review|current_milestone_state: review-requested|next_stage: code-review|open_findings: \\[\\]|CR-EDIP-M1-1" docs/plan.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`.
- M2 validation passed with `python3 -m unittest tests.test_exercise_document_image_prioritization tests.test_exercise_image_standard tests.test_markdown_first_real_pages`.
- M2 validation passed with `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`.
- M2 validation passed with `python3 tools/checks/check_privacy.py -- exercises media docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`.
- M2 validation passed with `git diff --check`.
- M2 state-sync inspection passed with `rg -n "Current stage: code-review M2|Current milestone: M2|Current milestone state: review-requested|Next stage: code-review M2|current_stage: code-review|current_milestone: M2|current_milestone_state: review-requested|next_stage: code-review|M2 implemented" docs/plan.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml`.
- M2 broader changed-artifact Markdown-first check passed with `python3 tools/checks/check_markdown_first.py docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md specs/exercise-document-best-practice-image-prioritization.md specs/exercise-document-best-practice-image-prioritization.test.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization tests/test_exercise_document_image_prioritization.py tools/checks/exercise_document_image_prioritization.py`.
- M2 broader changed-artifact privacy check passed with `python3 tools/checks/check_privacy.py -- docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md specs/exercise-document-best-practice-image-prioritization.md specs/exercise-document-best-practice-image-prioritization.test.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization tests tools`.
- Code-review M2 R1 recorded CR-EDIP-M2-1 and routed M2 to review-resolution.
- Code-review M2 R1 review-record Markdown-first check passed with `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md`.
- Code-review M2 R1 review-record privacy check passed with `python3 tools/checks/check_privacy.py -- docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md`.
- Code-review M2 R1 state-sync inspection passed with `rg -n "Current stage: review-resolution M2|Current milestone: M2|Current milestone state: resolution-needed|Next stage: review-resolution for M2|current_stage: review-resolution|current_milestone: M2|current_milestone_state: resolution-needed|next_stage: review-resolution|CR-EDIP-M2-1" docs/plan.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-log.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/code-review-m2-r1.md`.
- Code-review M2 R1 whitespace check passed with `git diff --check`.
- CR-EDIP-M2-1 resolution validation passed with `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md`.
- CR-EDIP-M2-1 resolution validation passed with `python3 tools/checks/check_privacy.py -- docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md`.
- CR-EDIP-M2-1 focused audit regression validation passed with `python3 -m unittest tests.test_exercise_document_image_prioritization`.
- CR-EDIP-M2-1 state-sync inspection passed with `rg -n "Current stage: code-review M2 re-review|Current milestone: M2|Current milestone state: review-requested|Next stage: code-review M2 re-review|current_stage: code-review|current_milestone: M2|current_milestone_state: review-requested|next_stage: code-review|open_findings: \\[\\]|CR-EDIP-M2-1" docs/plan.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`.
- CR-EDIP-M2-1 resolution validation passed with `git diff --check`.
- Code-review M2 R2 reviewer validation passed with `python3 -m unittest tests.test_exercise_document_image_prioritization`.
- Code-review M2 R2 reviewer validation passed with `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md`.
- Code-review M2 R2 reviewer validation passed with `python3 tools/checks/check_privacy.py -- docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md`.
- Code-review M2 R2 state-sync inspection passed with `rg -n "Current stage: implement M3|Current milestone: M3|Current milestone state: planned|Last reviewed milestone: M2|Next stage: implement M3|current_stage: implement|current_milestone: M3|current_milestone_state: planned|last_reviewed_milestone: M2|next_stage: implement|open_findings: \\[\\]|CR-EDIP-M2-1|code-review M2 R2" docs/plan.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-log.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/code-review-m2-r2.md`.
- Code-review M2 R2 reviewer validation passed with `git diff --check`.
- M3 focused closeout-proof validation passed with `python3 -m unittest tests.test_exercise_document_image_prioritization`.
- M3 rollback worktree validation passed with `git worktree add --detach .tmp/gymprimer-edip-m3-rollback HEAD`, `python3 tools/checks/check_markdown_first.py exercises/bird-dog.md`, `python3 tools/checks/check_privacy.py -- exercises/bird-dog.md`, and `git worktree remove .tmp/gymprimer-edip-m3-rollback`.
- M3 validation passed with `python3 -m unittest discover -s tests`.
- M3 validation passed with `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`.
- M3 validation passed with `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans media exercises tools tests`.
- M3 validation passed with `git diff --check`.
- M3 state-sync inspection passed with `rg -n "Current stage: code-review M3|Current milestone: M3|Current milestone state: review-requested|Last reviewed milestone: M2|Next stage: code-review M3|current_stage: code-review|current_milestone: M3|current_milestone_state: review-requested|last_reviewed_milestone: M2|next_stage: code-review|open_findings: \\[\\]|M3 implemented" docs/plan.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml`.
- Code-review M3 R1 reviewer validation passed with `python3 -m unittest discover -s tests`.
- Code-review M3 R1 reviewer validation passed with `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`.
- Code-review M3 R1 reviewer validation passed with `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans media exercises tools tests`.
- Code-review M3 R1 rollback worktree proof passed with Markdown-first and privacy checks against `exercises/bird-dog.md`.
- Code-review M3 R1 reviewer validation passed with `git diff --check`.
- Code-review M3 R1 state-sync inspection passed with `rg -n "Current stage: explain-change|Current milestone: Lifecycle Closeout|Current milestone state: planned|Last reviewed milestone: M3|last_reviewed_milestone: M3|Next stage: explain-change|current_stage: explain-change|current_milestone: Lifecycle Closeout|current_milestone_state: planned|next_stage: explain-change|open_findings: \\[\\]|Code-review M3 R1|M3 is closed|Ready for explain-change" docs/plan.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-log.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/code-review-m3-r1.md`.
- Explain-change validation passed with `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/explain-change.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md`.
- Explain-change validation passed with `python3 tools/checks/check_privacy.py -- docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/explain-change.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/plan.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml`.
- Explain-change state-sync inspection passed with `rg -n 'Current stage: verify|Next stage: verify|current_stage: verify|next_stage: verify|Explain-change refreshed|Ready for verify|open_findings: \\[\\]|review-resolution|Final verification has not run yet' docs/plan.md docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/explain-change.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`.
- Explain-change validation passed with `git diff --check`.
- Final verify passed with `python3 -m unittest discover -s tests`.
- Final verify passed with `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`.
- Final verify passed with `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans media exercises tools tests`.
- Final verify passed with local CI-equivalent Markdown-first and privacy checks from `.github/workflows/ci.yml`.
- Final verify passed with `git diff --check`.

## Outcome and retrospective

M1 is closed.
M2 is closed.
M3 is closed.
Explain-change is complete.
Final local verify is complete.

## Readiness

PR handoff is open.
Not ready for final closeout completion.

## Sources

- `specs/exercise-document-best-practice-image-prioritization.md`
- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/spec-review-r1.md`
- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/architecture-assessment.md`
