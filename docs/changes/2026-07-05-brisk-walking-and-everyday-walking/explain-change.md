# Explain Change: Brisk Walking and Everyday Walking Guidance

## Summary

This change adds walking guidance to GymPrimer as two Markdown-first pages: `exercises/brisk-walking.md` and `principles/everyday-walking.md`.
It also adds the scoped `basic_cardio_activity` method type, source-backed walking content, manual proof records, validation coverage, and the two required generated raster support images for the brisk-walking exercise document.

The implementation keeps brisk walking and everyday walking related but distinct.
Brisk walking is taught as beginner cardio using time, effort, progression, and stop rules.
Everyday walking is taught as habit-building and sitting interruption, not automatically as a workout.

The final reviewed branch includes four implementation milestones.
M1 added method/checker/template support, M2 added the two pages, M3 added manual proof, and M4 added the required brisk-walking movement and muscle-attention images.

## Problem

GymPrimer did not clearly represent walking, even though walking is one of the lowest-barrier activities for beginners.
The project needed beginner-readable guidance that explains the difference between casual everyday walking and brisk moderate-intensity walking without turning the site into a tracker, walking program, weight-loss plan, medical product, or adaptive coach.

The later image amendment added a second problem.
The brisk-walking exercise document needed all necessary support images according to the approved exercise-image standard, while preserving Markdown as the source of truth.

## Decision Trail

| Decision point | Result | Durable source |
| --- | --- | --- |
| Proposal direction | Chose Option C: two complementary pages, `exercises/brisk-walking.md` and `principles/everyday-walking.md`. | `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md`; proposal-review R2 |
| Method decision | Added `basic_cardio_activity` for non-equipment aerobic activity instead of forcing walking into sets/reps or equipment cardio. | Proposal decision log; BWG-R7-BWG-R13 |
| Image amendment | Required one brisk-walking movement image and one brisk-walking muscle-attention image. | Proposal-review R3; spec-review R3; BWG-R24-BWG-R26 |
| Requirements | Defined page contracts, source support, method behavior, safety boundaries, image constraints, and validation surfaces. | `specs/brisk-walking-and-everyday-walking.md` |
| Architecture | Kept walking as static Markdown content with visible method text, local citations, manual proof, and support-only generated raster media. | `docs/architecture/system/architecture.md`; architecture-review R1/R2 |
| Test strategy | Split deterministic checks from manual source/comprehension/visual proof. | `specs/brisk-walking-and-everyday-walking.test.md`; test-spec-review R1/R2 |
| Execution plan | Implemented M1 method support, M2 content pages, M3 manual proof, and M4 required images. | `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md` |
| Code review | M1 R2, M2 R1, M3 R1, and M4 R1 closed implementation milestones with no open blockers. | `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md` |

## Diff Rationale By Area

| Area / files | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md` | Recorded the walking product direction, later amended to require two brisk-walking images. | The change affected product scope, media policy, safety boundaries, and page shape, so it needed durable direction before implementation. | Proposal-review R2 and R3 | Review log; review-resolution PR-WALK-1 and SR-WALK-IMG-1 closed. |
| `specs/brisk-walking-and-everyday-walking.md` | Added BWG-R1-BWG-R30 and AC1-AC10. | Implementation needed testable contracts for page paths, distinction, method type, sources, safety, forbidden scope, images, and proof. | Accepted proposal | Spec-review R1 and R3. |
| `specs/brisk-walking-and-everyday-walking.test.md` | Added BWG-T1-BWG-T9 and BWG-MP1-BWG-MP3. | The checker can prove structure and wiring, while source adequacy, beginner comprehension, and visual safety need manual evidence. | BWG-R1-BWG-R30 | Test-spec-review R1 and R2. |
| `docs/architecture/system/architecture.md` | Added walking content flow, `basic_cardio_activity`, required brisk-walking media handling, validation observability, and risks. | The change touches long-lived content contracts, media provenance, checker behavior, and manual proof. | Architecture review R1/R2 | Architecture approvals. |
| `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`, `docs/plan.md`, `change.yaml` | Added and maintained the active workflow state, milestones, validations, reviews, and final-closeout routing. | The work needed staged implementation and traceable handoff before verify and PR. | Workflow guide and plan reviews | Plan-review R1/R2; lifecycle state scans. |
| `docs/workflows.md` | Added explicit new change ID rules using `YYYY-MM-DD-slug` and legacy-root handling. | The user requested a workflow update for change ID requirements, and this change root follows that dated format. | User request; workflow guide | `git diff --check`; privacy scans over workflow surfaces. |
| `SOURCES.md` | Added reusable CDC intensity, AHA activity, Mayo walking, and NHS walking source IDs. | Walking pages reuse these sources and must keep stable source IDs in the central index. | BWG-R21-BWG-R23 | BWG-T7; Markdown-first checker. |
| `specs/exercise-method-guidance.md` | Amended the existing method contract to allow scoped downstream method types and define `basic_cardio_activity` behavior. | Walking is cardio but not equipment-based and does not use strength sets/reps as the primary method shape. | BWG-R7-BWG-R13 | `tests/test_exercise_method_guidance.py`. |
| `docs/templates/exercise-card.md` | Added author guidance for non-equipment cardio activity pages. | Future authors need visible prompts for time, talk-test effort, repeatability, progression, and stop rules. | BWG-R10; M1 plan | `tests/test_markdown_first_templates.py`. |
| `tools/checks/check_markdown_first.py` | Scoped `basic_cardio_activity` to `exercises/brisk-walking.md` and added method-label expectations for cardio activity. | Prevents unapproved pages from using the new method type while allowing walking to omit a rest label when repeatability is the method shape. | BWG-R8-BWG-R10, BWG-R13, BWG-R29 | `tests/test_exercise_method_guidance.py`; code-review M1 R2. |
| `exercises/brisk-walking.md` | Added the beginner cardio page with talk test, pace reference, technique, muscles, feel, method guidance, safety notes, sources, and two support images. | Satisfies the exercise-page contract for brisk walking and the amended image requirement. | BWG-R1-R2, BWG-R5-R21, BWG-R24-R28 | BWG-T3, BWG-T5, BWG-T6, BWG-T8, BWG-T9; M4 visual proof. |
| `principles/everyday-walking.md` | Added the daily-movement principle page and kept it text-only. | Everyday walking needed habit and sitting-interruption guidance without pretending every walk is deliberate cardio. | BWG-R1, BWG-R3-R4, BWG-R18-R22, BWG-R26-R28 | BWG-T4, BWG-T5, BWG-T8; beginner proof. |
| `media/exercises/brisk-walking/movement.png` | Added the required movement/form support image. | The amended proposal and spec require a visual reference for posture, arm swing, and heel-to-toe stride. | BWG-R24-BWG-R25 | BWG-T8, BWG-MP3, code-review M4 R1. |
| `media/exercises/brisk-walking/muscle-attention.png` | Added the required broad muscle-attention support image. | The exercise document needs a visual aid for broad walking regions without exact anatomy. | BWG-R24, BWG-R25A | BWG-T8, BWG-MP3, code-review M4 R1. |
| `media/prompts/exercises/brisk-walking/*.md` and `media/PROVENANCE.md` | Added exact prompt records and approved provenance rows for both generated raster assets. | The exercise-image standard requires traceability from page reference to local asset, prompt record, provenance row, review status, and page refs. | BWG-R25B; `specs/exercise-image-standard.md` | BWG-T8, BWG-T9. |
| `docs/changes/.../manual-proof/*.md` | Added source audit, beginner comprehension, optional-image history, required-image decision, and visual-safety proof. | Semantic source support, reader comprehension, and visual safety cannot be fully proven by static parsing. | BWG-R23, BWG-R30, BWG-MP1-BWG-MP3 | Real-page tests assert required proof surfaces. |
| `docs/changes/.../reviews/`, `review-log.md`, `review-resolution.md`, `validation-ledger.md` | Recorded proposal/spec/architecture/plan/test-spec/code reviews, material finding closure, and command evidence. | Workflow-managed changes need durable review and validation evidence before verify. | AGENTS.md; workflow guide | M1-M4 code reviews; validation ledger. |
| `tests/test_exercise_method_guidance.py` | Added method-scope and label tests for `basic_cardio_activity`. | Proves the new method is active only where approved and requires visible cardio guidance. | BWG-T1, BWG-T2 | M1 validation. |
| `tests/test_markdown_first_templates.py` | Added assertions that the exercise template names cardio-activity cues. | Prevents the template from drifting behind the new method contract. | BWG-T2 | M1 validation. |
| `tests/test_markdown_first_real_pages.py` | Added walking page, source, safety, forbidden-scope, manual-proof, and image/provenance/prompt tests. | Real content needed integration checks against the approved walking contract. | BWG-T3-BWG-T9; BWG-MP1-BWG-MP3 | M2-M4 validation. |
| `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | Added `exercises/brisk-walking.md` to the existing exercise-image audit inventory. | New exercise pages need to stay visible to the existing image-standard audit surface. | Exercise-image standard | M3 validation and code-review M3 R1. |

The untracked `docs/learn/sessions/2026-07-05-walking-image-timing.md` file currently in the worktree is not part of this implementation explanation.

## Tests Added Or Changed

| Test ID | Location | What it proves | Why this level is appropriate |
| --- | --- | --- | --- |
| BWG-T1 | `tests/test_exercise_method_guidance.py` | `basic_cardio_activity` passes for `exercises/brisk-walking.md` and fails on unrelated exercise paths. | Method-scope behavior is deterministic checker logic. |
| BWG-T2 | `tests/test_exercise_method_guidance.py`, `tests/test_markdown_first_templates.py` | Cardio activity guidance uses visible beginner starting point, effort, progression, stop language, time, talk test, and repeatability. | Unit/template tests catch authoring and checker drift cheaply. |
| BWG-T3 | `tests/test_markdown_first_real_pages.py` | Brisk walking page has required sections, method line, intensity guidance, citations, safety routing, and static method wording. | Real-page integration tests verify the reader-facing artifact. |
| BWG-T4 | `tests/test_markdown_first_real_pages.py` | Everyday walking page exists, stays habit-oriented, distinguishes brisk walking, and includes safety/source structure. | The distinction is content-level behavior. |
| BWG-T5 | `tests/test_markdown_first_real_pages.py` and checker coverage | Walking pages avoid calorie targets, weight-loss prescriptions, step mandates, trackers, adaptive plans, medical plans, race-walking, running, hiking, treadmill, and incline protocols. | Deterministic forbidden wording guards the safety boundary. |
| BWG-T6 | `tests/test_markdown_first_real_pages.py` | Brisk walking includes role-based muscles and aligned feel guidance without exact activation or clinical claims. | Real-page coverage verifies the actual wording. |
| BWG-T7 | `tests/test_markdown_first_real_pages.py` and checker validation | Reused source IDs exist in `SOURCES.md`, and walking pages use page-local sources. | Source-surface validation is structural and automatable. |
| BWG-T8 | `tests/test_markdown_first_real_pages.py` | Brisk walking references exactly one movement image and one muscle-attention image; everyday walking has no image. | Image presence, paths, alt text, provenance, and page refs are deterministic. |
| BWG-T9 | `tests/test_markdown_first_real_pages.py` | Prompt records and provenance rows point back to the accepted image paths with approved generated-raster metadata. | Traceability is mechanical and should fail loudly. |
| BWG-MP1 | `manual-proof/source-audit.md` plus tests for proof presence | Source review sampled intensity, talk test, weekly activity guidance, less-sitting, technique, starter/progression, and stop rules. | Semantic source adequacy needs manual review. |
| BWG-MP2 | `manual-proof/beginner-comprehension.md` plus tests for proof presence | Non-identifying beginner proof records the approved walking comprehension prompts. | Reader comprehension cannot be proven by static parsing. |
| BWG-MP3 | `manual-proof/required-image-decision.md`, `manual-proof/visual-safety.md` | Required images are justified, visually reviewed, provenance-backed, and subordinate to Markdown. | Visual safety requires human inspection plus deterministic metadata checks. |

## Validation Evidence Available Before Final Verify

Local validation is recorded in `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/validation-ledger.md` and the code-review records.

| Stage | Commands / evidence | Result |
| --- | --- | --- |
| M1 | `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_templates tests.test_markdown_first_real_pages`; `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises`; privacy scan over specs/templates/tools/tests/change record | pass |
| M2 | `python3 -m unittest tests.test_markdown_first_real_pages`; focused Markdown-first checks over walking pages; method/muscle/real-page suites; Markdown-first discovery; privacy scan over pages and change record | pass |
| M3 | Markdown-first check over walking pages and media provenance; method/muscle/image/real-page suites; Markdown-first discovery; privacy scan over pages, media, and change record | pass |
| M4 | Required-image focused tests failed before implementation and passed after; `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`; broader method/muscle/image/real-page suites; Markdown-first discovery; Markdown-first checker; privacy scan; `git diff --check` | pass after implementation |
| Code-review M4 R1 | `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`; `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md`; `git diff --check` | pass |

Hosted CI has not been observed.
Final `verify` has not run yet.

## Review Resolution Summary

Two material review findings were opened and closed:

| Finding ID | Disposition | Summary |
| --- | --- | --- |
| PR-WALK-1 | accepted / closed | Proposal-review R1 found the proposal reopened already-selected decisions. Proposal-review R2 confirmed the revision keeps Option C, both page paths, and `basic_cardio_activity` as decisions. |
| SR-WALK-IMG-1 | accepted / closed | Spec-review R2 found the amended two-image spec conflicted with the then-accepted proposal. Proposal-review R3 accepted the two-image decision, and spec-review R3 confirmed the spec matched it. |

Durable resolution record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-resolution.md`.

M1 R2, M2 R1, M3 R1, and M4 R1 recorded no open implementation blockers.
`review-log.md` has no open findings.

## Alternatives Rejected

- Do nothing: rejected because walking is a major beginner-content gap.
- One broad walking page only: rejected because it would blur brisk cardio guidance with everyday movement habits.
- A walking program first: rejected because it is more prescriptive than the first slice and risks drifting toward personalized planning.
- Force walking into strength sets/reps: rejected because brisk walking is better represented by time, effort, repeatability, progression, and stop rules.
- Force walking into `basic_cardio_equipment`: rejected because walking is a non-equipment cardio activity.
- Keep brisk walking text-only or add only one optional movement image: rejected after the approved image amendment required both movement and muscle-attention support images.
- Add an everyday-walking image: rejected by BWG-R26 because the principle page remains text-only in this slice.
- Build a tracker, calculator, step-count target, heart-rate-zone prescription, or adaptive walking plan: rejected by proposal non-goals and BWG-R27.

## Scope Control

This change preserves the approved boundaries:

- No personalized walking plan.
- No weight-loss prescription, calorie target, fixed step-count mandate, or heart-rate-zone prescription.
- No tracker app, wearable integration, calculator, dashboard, database, user-input flow, or adaptive recommendation flow.
- No medical walking program, diagnosis, treatment, rehabilitation pathway, gait correction, posture correction, or return-to-walking protocol.
- No race-walking, running progression, hiking, rucking, loaded walking, treadmill protocol, incline-walking protocol, or full walking program.
- No generated content as source of truth; Markdown remains authoritative for effort, technique, muscles, safety, and citations.
- No extra walking images beyond the two required brisk-walking support images.

## Risks And Follow-Ups

- Generated images are approximate educational support assets and should be replaced if later reader review finds they confuse technique or muscle attention.
- Manual source audit is sampled evidence, not a guarantee that future edits remain source-supported.
- Beginner comprehension proof is non-identifying proxy evidence, not a formal usability study.
- Public source wording can change; source support should be rechecked when the walking pages are edited.
- Final verify still needs to run and record the branch-ready validation set.
- Hosted CI has not been observed.

## Readiness Statement

All implementation milestones are closed by code review, and material review findings are closed in `review-resolution.md`.
This explanation is the pre-verify rationale artifact.
The next lifecycle stage is `verify`.

This artifact does not claim final verification, branch readiness, PR readiness, PR-open readiness, or hosted CI success.
