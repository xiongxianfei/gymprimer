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
- Architecture: `../architecture/system/architecture.md`
- Architecture review R1: `../changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/architecture-review-r1.md`
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

Optional generated exercise images are governed by `specs/exercise-image-standard.md`, `media/PROVENANCE.md`, and prompt records. The approved first slice does not require a walking image; text-only brisk walking remains valid.

## Non-goals

- Do not create a personalized walking plan.
- Do not create a weight-loss prescription, calorie target, step-count mandate, or heart-rate-zone prescription.
- Do not create a tracker app, wearable integration, calculator, dashboard, user input flow, or adaptive recommendation flow.
- Do not create a medical walking program, return-to-walking protocol, pain treatment, gait diagnosis, posture correction, or rehabilitation pathway.
- Do not add race-walking, running progression, hiking, rucking, loaded walking, treadmill protocol, or incline walking in this slice.
- Do not generate an image unless implementation evidence shows text alone is not enough and the image can satisfy the exercise-image standard.
- Do not broadly migrate unrelated exercise pages.

## Requirements covered

- BWG-R1-R4: M2 creates the two pages and preserves the brisk/everyday distinction.
- BWG-R5-R6: M2 covers brisk pace, talk test, effort, pace reference, and page-local citations.
- BWG-R7-R13: M1 and M2 cover `basic_cardio_activity`, method-contract activation, starter duration, progression, and static non-adaptive wording.
- BWG-R14-R17: M2 covers role-based muscles, feel cues, and walking technique.
- BWG-R18-R23: M2 and M3 cover safety routing, stop rules, sources, source IDs, and manual source audit.
- BWG-R24-R26: M2 and M3 cover text-only validity and optional image handling.
- BWG-R27-R28: M1-M3 cover excluded scope and deterministic forbidden wording where practical.
- BWG-R29-R30: M1 and M3 cover automated validation and manual beginner proof.
- AC1-AC10: Plan review, test-spec review, implementation milestones, code review, explain-change, and verify provide acceptance evidence.

## Current Handoff Summary

- Current milestone: M1
- Current milestone state: review-requested
- Last reviewed milestone: none
- Review status: proposal-review R2 approved; spec-review R1 approved; architecture-review R1 approved; plan-review R1 approved; test-spec-review R1 approved; code-review M1 R1 inconclusive
- Remaining in-scope implementation milestones: M1, M2, M3
- Next stage: code-review
- Final closeout readiness: not-ready
- Reason final closeout is or is not ready: M1 code-review clean closeout is blocked by untracked governing artifacts; remaining implementation milestones, review-resolution if triggered, explain-change, verify, and PR handoff remain.

## Milestones

### M1. Method Contract, Template, and Checker Support

- Milestone state: review-requested
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

- Milestone state: planned
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
  - Keep the first pass text-only unless a concrete comprehension issue supports adding one optional brisk-walking movement image.
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

- Milestone state: planned
- Goal: record semantic evidence that checks cannot fully automate and decide whether the brisk walking page remains text-only.
- Requirements: BWG-R23-R30, AC5-AC10.
- Files/components likely touched:
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/source-audit.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/beginner-comprehension.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/optional-image-decision.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/validation-ledger.md`
  - optional `media/exercises/brisk-walking/`, `media/prompts/exercises/brisk-walking/`, and `media/PROVENANCE.md` only if the image decision approves one generated raster image
- Dependencies:
  - M2 should be closed.
- Tests to add/update:
  - Tests assert manual proof files exist and cover source-audit categories.
  - Tests assert beginner-comprehension evidence records the walking-specific prompts without private health information.
  - If an image is added, existing exercise-image tests cover path, purpose, alt text, prompt record, provenance, visual-safety evidence, and page refs.
  - If no image is added, tests or proof record the text-only decision.
- Implementation steps:
  - Record source-audit support for intensity, talk test, weekly activity when used, less-sitting framing, technique, starter/progression, and stop rules.
  - Record beginner-comprehension outcomes for the approved walking questions.
  - Record an optional image decision: no image first, unless text-only proof shows a concrete comprehension gap.
  - If an image is approved, add exactly one `exercise_movement_illustration` for brisk walking with prompt record, provenance row, meaningful alt text, and visual-safety evidence.
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
  - Require per-claim source-audit rows and keep the image decision text-only unless a specific read-test gap justifies the asset.

## Validation plan

- `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_templates tests.test_markdown_first_real_pages`: method, template, and real-page contract checks.
- `python3 -m unittest tests.test_exercise_muscle_guidance`: role-based muscle and feel-cue surfaces.
- `python3 -m unittest tests.test_exercise_image_standard`: optional generated raster image constraints when media is present.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`: broader Markdown-first regression coverage.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md`: focused content validation.
- `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking`: privacy scan over content and lifecycle evidence.
- Manual source audit: records source support for the claim categories in BWG-R23.
- Beginner comprehension proof: records the prompts in BWG-R30.
- Artifact lifecycle state-sync check: confirms `docs/plan.md`, this plan, `change.yaml`, review records, and validation ledger agree before downstream handoffs.

## Risks and recovery

- Risk: `basic_cardio_activity` opens a broad method type too early.
  - Recovery: Keep validation scoped to `exercises/brisk-walking.md` until a later approved non-equipment cardio activity spec extends it.
- Risk: walking guidance becomes a personal plan or medical program.
  - Recovery: Remove adaptive wording, disease-specific advice, weight-loss framing, step mandates, and heart-rate zones; route safety concerns to `RED-FLAGS.md`.
- Risk: source support is too broad for concrete technique or starter-duration claims.
  - Recovery: Narrow the claim, add direct page-local support, or remove the claim before promotion.
- Risk: an optional image adds little value or fails provenance.
  - Recovery: Keep the brisk walking page text-only and remove unused media artifacts.
- Risk: everyday walking becomes motivational filler.
  - Recovery: Require practical examples, brisk/everyday distinction, safety notes, and sources.

## Dependencies

- Spec review and architecture review are approved.
- Plan-review must approve this plan before test-spec authoring.
- Test-spec and test-spec-review must approve proof mapping before implementation.
- `SOURCES.md` source IDs must remain stable or be updated consistently in page-local sources and tests.
- Optional media depends on the exercise-image standard, generated raster prompt records, approved provenance, and visual-safety evidence.

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

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-05 | Use three implementation milestones: method/checker support, page content, manual proof. | The method type must be accepted by validation before pages can promote, and manual source/comprehension proof should remain separate from content drafting. | One large milestone; page content before method support; optional image as required work. |
| 2026-07-05 | Default the walking slice to text-only media. | The approved spec says no image is required and text-only pages remain valid. | Generate a walking image by default. |

## Surprises and discoveries

- Existing checker and tests already cover method guidance, exercise images, muscle guidance, real pages, and templates; this plan can extend those surfaces instead of creating a separate validation system.

## Validation notes

- M1 validation passed and is ready for code-review.

- 2026-07-05: `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_templates tests.test_markdown_first_real_pages` passed, running 29 tests.
- 2026-07-05: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises` passed, checking 24 Markdown files.
- 2026-07-05: `python3 tools/checks/check_privacy.py specs/brisk-walking-and-everyday-walking.md specs/exercise-method-guidance.md docs/templates tools tests docs/changes/2026-07-05-brisk-walking-and-everyday-walking` passed, checking 78 files.

## Outcome and retrospective

- Pending implementation and lifecycle closeout.

## Readiness

- See `Current Handoff Summary`.
- M1 is ready for code-review. M2 and M3 have not started.
