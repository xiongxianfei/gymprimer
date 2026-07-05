# Plan: Brisk Walking and Everyday Walking Guidance

## Status

- Status: reviewed
- Plan lifecycle state: active
- Terminal disposition: pending

## Purpose / big picture

Implement the approved walking guidance contract without turning GymPrimer into a walking tracker, weight-loss plan, medical walking program, or adaptive coach.

The work adds `basic_cardio_activity` as the non-equipment cardio method type, creates `exercises/brisk-walking.md` and `principles/everyday-walking.md`, keeps walking guidance citation-backed and page-local, and records manual proof for source support and beginner comprehension before promotion.

## Source artifacts

- Proposal: `../proposals/2026-07-05-brisk-walking-and-everyday-walking.md`
- Proposal review R2: `../changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/proposal-review-r2.md`
- Spec: `../../specs/brisk-walking-and-everyday-walking.md`
- Spec review R1: `../changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r1.md`
- Amended proposal review R3: `../changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/proposal-review-r3.md`
- Amended spec review R3: `../changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r3.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review R1: `../changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/architecture-review-r1.md`
- Architecture review R2: `../changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/architecture-review-r2.md`
- Governing specs:
  - `../../specs/markdown-first-primer.md`
  - `../../specs/exercise-method-guidance.md`
  - `../../specs/exercise-muscle-guidance.md`
  - `../../specs/exercise-image-standard.md`
- Test spec: `../../specs/brisk-walking-and-everyday-walking.test.md`

## Context and orientation

Exercise pages live under `exercises/`; principle pages live under `principles/`.

The exercise template is `docs/templates/exercise-card.md`.

Markdown validation is centered in `tools/checks/check_markdown_first.py` with unit coverage under `tests/`, including focused exercise-method, exercise-image, exercise-muscle, real-page, and template tests.

`SOURCES.md` already contains reusable walking and activity-guideline source IDs from the accepted proposal work. Page-local `## Sources` sections remain required for claims on the walking pages.

Generated exercise images are governed by `specs/exercise-image-standard.md`, `media/PROVENANCE.md`, and prompt records. The amended walking spec now requires one brisk-walking movement image and one brisk-walking muscle-attention image before final closeout. Those images are handled as a new M4 milestone because M1-M3 closed under the prior text-only media contract.

## Non-goals

- Do not create a personalized walking plan.
- Do not create a weight-loss prescription, calorie target, step-count mandate, or heart-rate-zone prescription.
- Do not create a tracker app, wearable integration, calculator, dashboard, user input flow, or adaptive recommendation flow.
- Do not create a medical walking program, return-to-walking protocol, pain treatment, gait diagnosis, posture correction, or rehabilitation pathway.
- Do not add race-walking, running progression, hiking, rucking, loaded walking, treadmill protocol, or incline walking in this slice.
- Do not generate extra walking images beyond the required brisk-walking movement and muscle-attention images in this slice.
- Do not broadly migrate unrelated exercise pages.

## Requirements covered

- BWG-R1-R4: M2 creates the two pages and preserves the brisk/everyday distinction.
- BWG-R5-R6: M2 covers brisk pace, talk test, effort, pace reference, and page-local citations.
- BWG-R7-R13: M1 and M2 cover `basic_cardio_activity`, method-contract activation, starter duration, progression, and static non-adaptive wording.
- BWG-R14-R17: M2 covers role-based muscles, feel cues, and walking technique.
- BWG-R18-R23: M2 and M3 cover safety routing, stop rules, sources, source IDs, and manual source audit.
- BWG-R24-R26: M4 covers the required brisk-walking movement image, required brisk-walking muscle-attention image, and no everyday-walking image.
- BWG-R27-R28: M1-M3 cover excluded scope and deterministic forbidden wording where practical.
- BWG-R29-R30: M1 and M3 cover automated validation and manual beginner proof.
- AC1-AC10: Plan review, test-spec review, implementation milestones, code review, explain-change, and verify provide acceptance evidence.

## Current Handoff Summary

- Current milestone: M4
- Current milestone state: closed
- Last reviewed milestone: M4
- Review status: proposal-review R2 approved; spec-review R1 approved; architecture-review R1 approved; plan-review R1 approved; test-spec-review R1 approved; code-review M1 R2 clean-with-notes; code-review M2 R1 clean-with-notes; code-review M3 R1 clean-with-notes; spec-review R2 changes-requested; proposal-review R3 approved amended proposal; spec-review R3 approved and closed SR-WALK-IMG-1; architecture-review R2 approved; plan-review R2 approved; test-spec-review R2 approved; code-review M4 R1 clean-with-notes
- Remaining in-scope implementation milestones: none
- Next stage: pr
- Final closeout readiness: branch-ready
- Reason final closeout is or is not ready: final local verify passed; PR handoff remains.

## Milestones

### M1. Method Contract, Template, and Checker Support

- Milestone state: closed
- Goal: make `basic_cardio_activity` authorable and checkable before adding the walking pages.
- Requirements: BWG-R7-R13, BWG-R27-R29, AC4, AC8-AC10.
- Files/components likely touched:
  - `specs/exercise-method-guidance.md`
  - `docs/templates/exercise-card.md`
  - `tools/checks/check_markdown_first.py`
  - `tests/test_exercise_method_guidance.py`
  - `tests/test_markdown_first_templates.py`
  - `tests/test_markdown_first_real_pages.py`
- Dependencies:
  - Plan-review and test-spec-review must approve the proof map before implementation.
- Tests to add/update:
  - `basic_cardio_activity` passes for `exercises/brisk-walking.md`.
  - `basic_cardio_activity` fails for out-of-scope exercise pages.
  - `basic_cardio_equipment` remains scoped to rowing-machine and approved cardio-equipment pages.
  - `loaded_carry` remains inactive.
  - Cardio activity method guidance requires visible time, effort, progression, and stop language without sets/reps as the primary shape.
  - Template guidance names `basic_cardio_activity` without making it a user-facing personalization system.
- Implementation steps:
  - Amend the method contract surfaces to recognize `basic_cardio_activity` for walking and later approved non-equipment aerobic activity pages.
  - Update template prompts so authors can write time/effort/progression guidance for non-equipment cardio activity.
  - Extend deterministic checker behavior and tests for active method type scope and required visible method labels.
  - Keep visible Markdown as the source of truth; do not add hidden metadata or generated data.
- Validation commands:
  - `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_templates tests.test_markdown_first_real_pages`
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises`
  - `python3 tools/checks/check_privacy.py specs/brisk-walking-and-everyday-walking.md specs/exercise-method-guidance.md docs/templates tools tests docs/changes/2026-07-05-brisk-walking-and-everyday-walking`
- Expected observable result: `basic_cardio_activity` has a visible, scoped, test-backed method path without reactivating unrelated deferred method types.
- Commit message: `M1: add basic cardio activity method support`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Method validation could become too broad and allow unrelated pages to use `basic_cardio_activity`.
- Rollback/recovery:
  - Scope checker acceptance to `exercises/brisk-walking.md` until later approved non-equipment cardio activity specs exist.

### M2. Walking Markdown Pages and Sources

- Milestone state: closed
- Goal: add the brisk walking exercise page and everyday walking principle page with page-local citations and safety routing.
- Requirements: BWG-R1-R28, AC1-AC7, AC9-AC10.
- Files/components likely touched:
  - `exercises/brisk-walking.md`
  - `principles/everyday-walking.md`
  - `SOURCES.md`
  - `RED-FLAGS.md` only if a link target or wording issue is discovered
  - `tests/test_markdown_first_real_pages.py`
  - `tests/test_exercise_muscle_guidance.py`
- Dependencies:
  - M1 should be closed.
- Tests to add/update:
  - Real-page tests assert both walking pages exist.
  - Brisk walking has `## How much to do`, `Method type: basic_cardio_activity`, `## Muscles involved`, `## What you should feel`, safety notes, and `## Sources`.
  - Everyday walking has the approved principle sections, practical walking examples, safety notes, and `## Sources`.
  - Tests assert the pages link to `../RED-FLAGS.md` when safety context is present.
  - Tests or checker assertions cover forbidden personalized, medical, calorie, step-mandate, heart-rate-zone, tracker, and adaptive-plan wording where deterministic.
- Implementation steps:
  - Draft `exercises/brisk-walking.md` from the approved spec and template.
  - Draft `principles/everyday-walking.md` from the approved spec and principle-page conventions.
  - Add page-local citations for intensity, talk test, activity guidance, less sitting, walking technique, starter/progression wording, and safety stop rules.
  - Reuse or adjust `SOURCES.md` source IDs only when sources are reused across pages.
  - Historical M2 note: the first pass stayed text-only under the prior contract. The amended media contract now requires downstream image implementation before final closeout.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md`
  - `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_markdown_first_real_pages`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking`
- Expected observable result: readers can open two Markdown pages and understand the difference between everyday walking and brisk walking, how to identify brisk effort, how to start generally, what to feel, when to stop, and where the sources are.
- Commit message: `M2: add walking guidance pages`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Starter guidance may read like a personal prescription instead of static education.
  - Everyday walking may become too motivational and not practical enough.
- Rollback/recovery:
  - Narrow starter wording, add cross-links between the two pages, or remove under-supported claims before code review.

### M3. Manual Proof, Optional Media Decision, and Promotion Gate

- Milestone state: closed
- Goal: record semantic evidence that checks cannot fully automate and decide whether the brisk walking page remains text-only under the prior contract.
- Requirements: BWG-R23, BWG-R27-BWG-R30 under the prior text-only media contract.
- Files/components likely touched:
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/source-audit.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/beginner-comprehension.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/optional-image-decision.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/validation-ledger.md`
- Dependencies:
  - M2 should be closed.
- Tests to add/update:
  - Tests assert manual proof files exist and cover source-audit categories.
  - Tests assert beginner-comprehension evidence records the walking-specific prompts without private health information.
  - Historical M3 note: tests or proof recorded the text-only decision under the prior contract.
- Implementation steps:
  - Record source-audit support for intensity, talk test, weekly activity when used, less-sitting framing, technique, starter/progression, and stop rules.
  - Record beginner-comprehension outcomes for the approved walking questions.
  - Historical M3 note: record an optional image decision under the prior contract.
  - Record validation command results in a validation ledger.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md`
  - `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media docs/changes/2026-07-05-brisk-walking-and-everyday-walking`
- Expected observable result: semantic source support, beginner comprehension, and image/no-image decision evidence are recorded before final promotion readiness.
- Commit message: `M3: record walking guidance proof`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Manual proof could be too vague to support promotion.
  - Optional image work could expand scope late in the slice.
- Rollback/recovery:
  - Historical M3 recovery under the prior contract was to require per-claim source-audit rows and keep the image decision text-only unless a specific read-test gap justified the asset.

### M4. Required Brisk Walking Images

- Milestone state: closed
- Goal: add the two required support images for `exercises/brisk-walking.md` without making images the source of truth.
- Requirements: BWG-R24, BWG-R25, BWG-R25A, BWG-R25B, BWG-R26, BWG-R29.
- Files/components likely touched:
  - `exercises/brisk-walking.md`
  - `principles/everyday-walking.md` only if a no-image assertion or link check needs a small adjustment
  - `media/exercises/brisk-walking/movement.png`
  - `media/exercises/brisk-walking/muscle-attention.png`
  - `media/prompts/exercises/brisk-walking/movement.md`
  - `media/prompts/exercises/brisk-walking/muscle-attention.md`
  - `media/PROVENANCE.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/required-image-decision.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/visual-safety.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/validation-ledger.md`
  - `tests/test_exercise_image_standard.py`
  - `tests/test_markdown_first_real_pages.py`
- Dependencies:
  - Plan-review must approve this M4 plan update before test-spec update.
  - Test-spec and test-spec-review must approve the M4 proof map before implementation.
  - Architecture-review R2 is approved and the canonical architecture package is normalized to approved.
- Tests to add/update:
  - Assert `exercises/brisk-walking.md` references exactly one movement image and exactly one muscle-attention image.
  - Assert the movement image uses `exercise_movement_illustration`, a local asset path, meaningful alt text, a prompt record, approved provenance, and `page_refs` containing `exercises/brisk-walking.md`.
  - Assert the muscle-attention image uses `exercise_muscle_attention_illustration`, a local asset path, meaningful alt text, a prompt record, approved provenance, and `page_refs` containing `exercises/brisk-walking.md`.
  - Assert `principles/everyday-walking.md` remains text-only.
  - Assert prompt records point back to the normalized asset paths.
  - Assert required visual-safety evidence exists for both image paths.
- Implementation steps:
  - Generate or select exactly two high-quality raster assets for brisk walking: one movement/form image and one broad muscle-attention image.
  - Inspect the generated assets before use; reject assets with in-image labels, red pain marks, race-walking, running, treadmill, hiking, wearable-tracker, wrong/correct, clinical, precise-anatomy, exposed-musculature, diagnosis, treatment, rehab, or exact-activation framing.
  - Copy only accepted assets into `media/exercises/brisk-walking/` with stable purpose filenames.
  - Add prompt records under `media/prompts/exercises/brisk-walking/` preserving exact full prompts for the accepted assets.
  - Add approved provenance rows with `asset_type = ai_generated_raster`, the correct `media_purpose`, prompt-record paths, source inputs, license assertion, human reviewer, review status, page refs, and concise creation notes.
  - Add the image references and meaningful alt text to `exercises/brisk-walking.md`; keep nearby Markdown as the source of truth for technique, muscles, feel, safety, and citations.
  - Confirm `principles/everyday-walking.md` remains text-only.
  - Record required-image decision, visual-safety evidence, and validation command results.
- Validation commands:
  - `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`
  - `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md`
  - `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media docs/changes/2026-07-05-brisk-walking-and-everyday-walking`
  - `git diff --check`
- Expected observable result: `exercises/brisk-walking.md` has exactly the two required support images with valid prompt records, provenance, alt text, page refs, and visual-safety evidence; `principles/everyday-walking.md` remains text-only.
- Commit message: `M4: add required brisk walking images`
- Milestone closeout:
  - validation passed
  - M4 proof records updated
  - validation ledger updated
  - plan progress updated
  - code-review M4 passed
- Risks:
  - Generated images could imply exact anatomy, clinical correction, wrong/correct comparison, race-walking, running, or other out-of-scope guidance.
  - Prompt records or provenance rows could drift from the accepted asset path.
  - The brisk walking page could start relying on the image instead of Markdown for technique or muscle guidance.
- Rollback/recovery:
  - Replace invalid assets before promotion when the issue is visual quality, purpose mismatch, prompt/provenance mismatch, or visual-safety failure.
  - Remove unused rejected assets and prompt records from the implementation diff.
  - If no valid image can be produced without violating the image standard, route back to spec/proposal amendment instead of promoting a text-only page under the required-media contract.

## Validation plan

- `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_templates tests.test_markdown_first_real_pages`: method, template, and real-page contract checks.
- `python3 -m unittest tests.test_exercise_muscle_guidance`: role-based muscle and feel-cue surfaces.
- `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`: generated raster image constraints and real-page references for the required brisk-walking images.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`: broader Markdown-first regression coverage.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md`: focused content validation.
- `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media docs/changes/2026-07-05-brisk-walking-and-everyday-walking`: privacy scan over content, media prompt records, provenance, and lifecycle evidence.
- Manual source audit: records source support for the claim categories in BWG-R23.
- Beginner comprehension proof: records the prompts in BWG-R30.
- Artifact lifecycle state-sync check: confirms `docs/plan.md`, this plan, `change.yaml`, review records, and validation ledger agree before downstream handoffs.
- Architecture amendment validation: `python3 tools/checks/check_privacy.py docs/architecture/system/architecture.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking/change.yaml docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md docs/plan.md`, `git diff --check`, and focused routing grep.
- M4 plan-update validation: privacy scan over plan surfaces, `git diff --check`, and lifecycle routing grep before plan-review handoff.

## Risks and recovery

- Risk: `basic_cardio_activity` opens a broad method type too early.
  - Recovery: Keep validation scoped to `exercises/brisk-walking.md` until a later approved non-equipment cardio activity spec extends it.
- Risk: walking guidance becomes a personal plan or medical program.
  - Recovery: Remove adaptive wording, disease-specific advice, weight-loss framing, step mandates, and heart-rate zones; route safety concerns to `RED-FLAGS.md`.
- Risk: source support is too broad for concrete technique or starter-duration claims.
  - Recovery: Narrow the claim, add direct page-local support, or remove the claim before promotion.
- Risk: a required walking image adds little value or fails provenance.
  - Recovery: replace the image or revise the amended spec; do not promote invalid or unproven media.
- Risk: everyday walking becomes motivational filler.
  - Recovery: Require practical examples, brisk/everyday distinction, safety notes, and sources.

## Dependencies

- Spec review and architecture review are approved.
- Plan-review R2 approved this M4 plan update before test-spec authoring.
- Test-spec and test-spec-review must approve proof mapping before implementation.
- `SOURCES.md` source IDs must remain stable or be updated consistently in page-local sources and tests.
- Required media depends on the exercise-image standard, generated raster prompt records, approved provenance, and visual-safety evidence.
- M4 image implementation must not start until this amended plan passes plan-review and the test spec is updated and approved for the M4 proof map.

## Progress

- 2026-07-05: Proposal accepted after proposal-review R2 closed PR-WALK-1.
- 2026-07-05: Spec approved by spec-review R1.
- 2026-07-05: Canonical architecture amendment approved by architecture-review R1.
- 2026-07-05: Drafted this execution plan for plan-review.
- 2026-07-05: Plan-review R1 approved this plan for test-spec authoring.
- 2026-07-05: Drafted `specs/brisk-walking-and-everyday-walking.test.md` for test-spec-review.
- 2026-07-05: Test-spec-review R1 approved the active proof map and allowed implementation handoff.
- 2026-07-05: Started M1 implementation for `basic_cardio_activity` method, template, and checker support.
- 2026-07-05: Completed M1 implementation and validation; M1 is ready for code-review.
- 2026-07-05: Code-review M1 R1 found no material implementation findings in the inspected diff but recorded an inconclusive result because governing artifacts for this change are untracked; M1 remains review-requested.
- 2026-07-05: Code-review M1 R2 passed after governing artifacts were committed and tracked; M1 is closed and M2 implementation is next.
- 2026-07-05: Started M2 implementation for brisk walking and everyday walking Markdown pages, page-local sources, safety routing, and real-page tests.
- 2026-07-05: Added failing real-page tests for walking page existence, structure, method, source IDs, safety routing, forbidden scope, text-only media, and brisk walking muscle/feel guidance.
- 2026-07-05: Added `exercises/brisk-walking.md` and `principles/everyday-walking.md`; kept both text-only; left `SOURCES.md` and `RED-FLAGS.md` unchanged because required source IDs and central safety routing already existed.
- 2026-07-05: M2 validation passed; M2 is ready for code-review.
- 2026-07-05: Code-review M2 R1 passed; M2 is closed and M3 implementation is next.
- 2026-07-05: Started M3 implementation for manual source audit, beginner comprehension proof, optional image decision, and promotion-gate validation evidence.
- 2026-07-05: Added failing tests for walking manual proof records and M3 validation ledger coverage.
- 2026-07-05: Added source audit, beginner-comprehension proof, and optional-image text-only decision records.
- 2026-07-05: Updated the exercise-image audit inventory to include text-only `exercises/brisk-walking.md`.
- 2026-07-05: M3 validation passed; M3 is ready for code-review.
- 2026-07-05: Code-review M3 R1 passed; M3 and the then-current implementation milestones were closed, and explain-change was next before the later image amendment.
- 2026-07-05: Amended the walking spec and test spec to require brisk-walking movement and muscle-attention images; final closeout is paused pending amended spec review and downstream artifact updates.
- 2026-07-05: Spec-review R2 requested changes with SR-WALK-IMG-1 because the amended two-image requirement conflicts with the accepted proposal's first-slice image decision.
- 2026-07-05: Owner selected the proposal-amendment path for SR-WALK-IMG-1 and revised the proposal to require brisk-walking movement and muscle-attention images.
- 2026-07-05: Proposal-review R3 approved the amended proposal; SR-WALK-IMG-1 remains open pending spec-review recheck.
- 2026-07-05: Spec-review R3 approved the amended spec and closed SR-WALK-IMG-1; architecture update is next.
- 2026-07-05: Updated the canonical architecture package for the required brisk-walking movement and muscle-attention image contract; architecture-review R2 followed.
- 2026-07-05: Architecture-review R2 approved the required brisk-walking media architecture amendment; architecture status normalization followed before downstream artifacts rely on it.
- 2026-07-05: Normalized the canonical architecture package to approved for the required brisk-walking media amendment; plan update followed.
- 2026-07-05: Revised the execution plan with M4 for the required brisk-walking movement and muscle-attention images; plan-review followed.
- 2026-07-05: Plan-review R2 approved the M4 required-image plan update; test-spec update followed before implementation.
- 2026-07-05: Updated the test spec with the M4 required-image proof map; test-spec-review R2 followed before implementation.
- 2026-07-05: Test-spec-review R2 approved the M4 required-image proof map; M4 implementation handoff is allowed.
- 2026-07-05: Started M4 implementation with failing required-image real-page tests before adding assets or page references.
- 2026-07-05: Completed M4 implementation with exactly two brisk-walking support images, prompt records, provenance rows, page references, required-image proof, visual-safety proof, and validation evidence; M4 moved to code-review.
- 2026-07-05: Code-review M4 R1 passed with no material findings; all implementation milestones are closed and final closeout began.
- 2026-07-05: Added `explain-change.md` for the final reviewed diff and routed the change to verify.
- 2026-07-05: Final local verify passed, branch-ready evidence is recorded in `verify-report.md`, and PR handoff is next.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-05 | Use three implementation milestones: method/checker support, page content, manual proof. | The method type must be accepted by validation before pages can promote, and manual source/comprehension proof should remain separate from content drafting. | One large milestone; page content before method support; optional image as required work. |
| 2026-07-05 | Default the walking slice to text-only media. | The approved spec says no image is required and text-only pages remain valid. | Generate a walking image by default. |
| 2026-07-05 | Amend the walking media contract to require movement and muscle-attention images for brisk walking. | Maintainer requested all necessary images for the document according to best practices. | Keep the already-closed text-only media decision as final. |
| 2026-07-05 | Add required walking images as M4 instead of reopening closed M3. | M1-M3 closed under the prior text-only media contract; the amended image work needs its own implementation, proof, and code-review boundary. | Reopen M3; mix image implementation into final closeout; implement images before plan/test-spec review. |

## Surprises and discoveries

- Existing checker and tests already cover method guidance, exercise images, muscle guidance, real pages, and templates; this plan can extend those surfaces instead of creating a separate validation system.
- M2 did not need a `SOURCES.md` edit because the accepted proposal/spec work had already added the reusable walking source IDs.
- M2 did not need a `RED-FLAGS.md` edit because the walking pages could route to the existing central safety page.
- M3 needed an aligned exercise-image audit update because the existing image-standard tests require every current `exercises/*.md` page to appear in the audit inventory.

## Validation notes

- M1 validation passed and is ready for code-review.

- 2026-07-05: `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_templates tests.test_markdown_first_real_pages` passed, running 29 tests.
- 2026-07-05: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises` passed, checking 24 Markdown files.
- 2026-07-05: `python3 tools/checks/check_privacy.py specs/brisk-walking-and-everyday-walking.md specs/exercise-method-guidance.md docs/templates tools tests docs/changes/2026-07-05-brisk-walking-and-everyday-walking` passed, checking 78 files.
- M2 validation passed and is ready for code-review.
- 2026-07-05: `python3 -m unittest tests.test_markdown_first_real_pages` passed, running 16 tests.
- 2026-07-05: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md` passed, checking 4 Markdown files.
- 2026-07-05: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md` passed, checking 5 Markdown files.
- 2026-07-05: `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_markdown_first_real_pages` passed, running 44 tests.
- 2026-07-05: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed, running 65 tests.
- 2026-07-05: `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking` passed, checking 16 files.
- M3 validation passed and is ready for code-review.
- 2026-07-05: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md` passed, checking 5 Markdown files.
- 2026-07-05: `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed after ledger update.
- 2026-07-05: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed after ledger update.
- 2026-07-05: `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media docs/changes/2026-07-05-brisk-walking-and-everyday-walking` passed, checking 62 files.
  - 2026-07-05: M4 plan update validation passed with `python3 tools/checks/check_privacy.py docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md docs/plan.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking/change.yaml` and `git diff --check`.
  - 2026-07-05: M4 implementation validation passed with `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_brisk_walking_required_images_are_local_prompt_backed_and_reviewed tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_walking_m4_required_image_proof_records_visual_safety`, `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`, `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages`, `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`, `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md`, `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media docs/changes/2026-07-05-brisk-walking-and-everyday-walking`, and `git diff --check`.
  - 2026-07-05: Explain-change validation passed with `python3 tools/checks/check_privacy.py docs/changes/2026-07-05-brisk-walking-and-everyday-walking/explain-change.md docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md docs/plan.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking/change.yaml`, lifecycle routing grep, and `git diff --check`.
  - 2026-07-05: Final verify validation passed with `python3 -m unittest discover -s tests`, `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md principles exercises patterns`, `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md docs specs tools tests principles exercises patterns media`, walking-specific image/proof tests, walking-specific Markdown-first check, lifecycle routing grep, and `git diff --check`.

## Outcome and retrospective

- M1-M3 implementation milestones were closed under the prior text-only media contract. The accepted amended proposal and approved amended spec required brisk-walking images, M4 is now closed with no material code-review findings, explain-change is complete, and final local verify passed. PR handoff is next.

## Readiness

- See `Current Handoff Summary`.
- M1, M2, M3, and M4 are closed with validation evidence recorded. Explain-change and final local verify are complete; PR handoff is next.
