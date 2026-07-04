# Plan: Exercise Method Guidance

## Status

- Status: draft
- Plan lifecycle state: active
- Terminal disposition: not-terminal

## Purpose / big picture

Implement the approved exercise-method guidance contract without turning
GymPrimer into a workout planner. The work adds a visible `## How much to do`
section, method-type-specific starter-range guidance, supporting validation, a
short principle page, six proof-slice exercise pages, and manual evidence for
source support and beginner comprehension.

This plan sequences implementation only. It does not reopen the accepted
training-type menu, add hidden metadata, expand into carries or cardio
equipment, or rewrite every exercise page.

## Source artifacts

- Proposal: `../proposals/2026-07-04-exercise-method-guidance.md`
- Proposal review: `../changes/exercise-method-guidance/reviews/proposal-review-r2.md`
- Spec: `../../specs/exercise-method-guidance.md`
- Spec review: `../changes/exercise-method-guidance/reviews/spec-review-r1.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review: `../changes/exercise-method-guidance/reviews/architecture-review-r1.md`
- Governing specs:
  - `../../specs/markdown-first-primer.md`
  - `../../specs/responsible-breadth.md`
- Test spec: `../../specs/exercise-method-guidance.test.md`

## Context and orientation

GymPrimer is a Markdown-first beginner primer. Exercise pages live under
`exercises/`, pattern pages can include compact exercise previews under
`patterns/`, shared concepts live under `principles/`, templates live under
`docs/templates/`, and validation currently runs through
`tools/checks/check_markdown_first.py`, Python `unittest` tests, and manual
evidence under `docs/changes/exercise-method-guidance/`.

The approved method contract is visible Markdown only. Updated exercise pages
must add `## How much to do`, declare one visible `Method type:` value, include
beginner starting point, effort, rest, progression, and stop guidance, preserve
page-local source support, and avoid adaptive programming. Hidden metadata,
YAML front matter, shared taxonomy files, generated indexes, generated public
data packages, user input, diagnosis, treatment, rehab, return-to-training
prescriptions, and personalized programming remain out of scope.

The first proof slice is exactly:

- `exercises/chest-press.md` as `dynamic_resistance`
- `exercises/incline-push-up.md` as `bodyweight_progression`
- `exercises/chin-nod.md` as `low_load_control_drill`
- `exercises/plank.md` as `isometric_hold`
- `exercises/thoracic-extension.md` as `mobility_drill`
- `exercises/kneeling-hip-flexor-stretch.md` as `stretch_hold`

## Non-goals

- Do not add personalized plans, adaptive programming, calculators, user intake,
  symptom checkers, training logs, or hosted app behavior.
- Do not diagnose, treat, prescribe rehab, promise posture correction, provide
  return-to-training guidance, or recommend injury-specific substitutions.
- Do not activate `loaded_carry` or `basic_cardio_equipment`.
- Do not make hidden metadata, YAML front matter, taxonomy files, generated
  indexes, or generated data the source of truth.
- Do not rewrite every exercise page in the first implementation slice.
- Do not add advanced athlete, sport-specific, powerlifting, advanced lifting,
  kettlebell ballistic, plyometric, sprint, or competition programming content.

## Requirements covered

- R1-R6: M1 validates and templates the visible method section, method type,
  active enum, required labels, and hidden-only metadata rejection.
- R7-R13: M1, M3, and M4 preserve static education, non-prescriptive wording,
  safety routing, and page-local source-support expectations.
- R14-R25: M3 applies method-type starter-range shapes to the six proof-slice
  exercise pages.
- R26-R27: M1 validation rejects deferred method types.
- R28-R29: M3 implements exactly the six proof-slice pages and method mappings.
- R30-R32: M2 creates the supporting principle page and links it from updated
  exercise pages where useful.
- R33-R35: M1 and M3 check or manually audit pattern-preview alignment.
- R36: M1 updates `docs/templates/exercise-card.md`.
- R37-R38: M1 adds or updates automated validation and stable failure behavior.
- R39-R40: M4 records source-audit and beginner-comprehension evidence.
- R41: M3 keeps unselected exercise pages valid under their prior contract.
- R42: M1 adds compatibility notes only where needed.
- AC1-AC10: M1-M4 plus downstream reviews, explain-change, and verify provide
  acceptance evidence.

## Current Handoff Summary

- Current milestone: Lifecycle Closeout
- Current milestone state: planned
- Last reviewed milestone: M4
- Review status: proposal-review R2 approved; spec-review R1 approved;
  architecture-review R1 approved; plan-review R1 approved; test-spec-review R2
  approved after TSR-EMG-1 and TSR-EMG-2 resolution
- Remaining in-scope implementation milestones: none
- Remaining lifecycle milestones: Lifecycle Closeout
- Next stage: verify
- Final closeout readiness: not-ready
- Reason final closeout is or is not ready: M1, M2, M3, and M4 are closed;
  verify and PR handoff remain.

## Milestones

### M1. Method Contract Validation and Template

- Milestone state: closed
- Goal: make the exercise-method contract authorable and checkable before
  proof-slice content changes.
- Requirements: R1-R6, R7-R13, R26-R27, R33-R38, R42, AC1, AC3, AC6, AC8-AC10.
- Files/components likely touched:
  - `docs/templates/exercise-card.md`
  - `tools/checks/check_markdown_first.py`
  - `tests/test_markdown_first_templates.py`
  - `tests/test_markdown_first_real_pages.py`
  - focused test fixtures under `tests/fixtures/markdown-first/`
  - `specs/markdown-first-primer.md`
  - `specs/responsible-breadth.md`
- Dependencies:
  - plan-review and test-spec-review must approve the proof map before
    implementation.
- Tests to add/update:
  - method section required for pages selected under the method-guidance slice;
  - active method type enum passes and inactive values fail;
  - hidden-only method metadata fails when no visible `Method type:` exists;
  - required visible labels are present;
  - forbidden personalized-programming and treatment language is rejected;
  - deferred method types fail;
  - exercise template includes `## How much to do`.
- Implementation steps:
  - Add template guidance for the method section and labels.
  - Add visible-text method parsing to the checker.
  - Add fixture and real-page tests for valid and invalid method sections.
  - Add compatibility notes to related specs only where needed.
  - Keep validation opt-in or slice-aware so existing unselected exercise pages
    do not fail solely for missing method guidance.
- Validation commands:
  - `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises patterns principles`
  - `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-method-guidance`
- Expected observable result: contributors have a template and deterministic
  validation path for method guidance without requiring hidden metadata.
- Commit message: `M1: add exercise method validation and template`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - A broad checker rule could accidentally make every existing exercise page
    fail before the rollout reaches it.
- Rollback/recovery:
  - Keep the rule gated to selected proof-slice paths or an explicit adopted
    section; if it still overreaches, revert the checker change and keep the
    template-only edit until test-spec is revised.

### M2. Sets, Reps, Holds, Rest, and Progression Principle Page

- Milestone state: closed
- Goal: add the same-slice principle page that explains shared method concepts
  once so exercise pages can stay concise.
- Requirements: R30-R32, R7-R13, AC5, AC7, AC9-AC10.
- Files/components likely touched:
  - `principles/sets-reps-holds-rest-and-progression.md`
  - `SOURCES.md`
  - `tools/checks/check_markdown_first.py`
  - `tests/test_responsible_breadth_m1.py`
  - `docs/changes/exercise-method-guidance/manual-proof/`
- Dependencies:
  - M1 validation contract should be in place before this page is promoted.
- Tests to add/update:
  - principle page has the required Responsible Breadth principle sections;
  - principle page includes page-local sources;
  - privacy check covers the new page and proof records.
- Implementation steps:
  - Draft the principle page with definitions for sets, reps, timed holds,
    easy/moderate/hard effort, rest, one-variable progression, and
    starter-range boundaries.
  - Add or reuse source-index entries for the supporting public sources.
  - Keep wording general and educational, not a personal program.
  - Add a source-support manual proof record if automation cannot prove the
    semantic claims.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md principles`
  - `python3 -m unittest tests.test_responsible_breadth_m1`
  - `python3 tools/checks/check_privacy.py principles SOURCES.md docs/changes/exercise-method-guidance`
- Expected observable result: readers can follow updated exercise-page links to
  a concise explanation of method terms and non-prescriptive starter ranges.
- Commit message: `M2: add exercise method principle page`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - The principle page could become a programming plan instead of literacy
    guidance.
- Rollback/recovery:
  - Narrow the page to definitions and examples, remove weekly routine language,
    and route any broader programming topic to a later approved spec amendment.

### M3. Six Proof-Slice Exercise Pages

- Milestone state: closed
- Goal: add source-supported method guidance to the six approved proof-slice
  exercise pages and keep pattern previews aligned.
- Requirements: R1-R29, R32-R35, R41, AC2, AC4, AC8-AC10.
- Files/components likely touched:
  - `exercises/chest-press.md`
  - `exercises/incline-push-up.md`
  - `exercises/chin-nod.md`
  - `exercises/plank.md`
  - `exercises/thoracic-extension.md`
  - `exercises/kneeling-hip-flexor-stretch.md`
  - pattern pages that preview these exercises, if contradictory
  - `SOURCES.md`
  - `docs/changes/exercise-method-guidance/manual-proof/`
- Dependencies:
  - M1 and M2 should be closed.
- Tests to add/update:
  - real-page validation for all six method sections and method mappings;
  - pattern-preview alignment checks where deterministic;
  - privacy checks for edited content and proof records.
- Implementation steps:
  - Add `## How much to do` to each proof-slice exercise page.
  - Use the exact active method type assigned in the spec.
  - Include beginner starting point, effort, rest, progression, and stop
    guidance in non-prescriptive language.
  - Add page-local citations for concrete amount, effort, progression, rest, or
    safety claims.
  - Link the principle page where beginner terms need explanation.
  - Inspect pattern pages for previews that mention these exercises and remove
    or align contradictions.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md principles exercises patterns`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 -m unittest tests.test_responsible_breadth_m1`
  - `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md principles exercises patterns docs/changes/exercise-method-guidance`
- Expected observable result: the six exercise pages answer "how much should I
  do?" with method-type-appropriate static guidance and no conflicting pattern
  previews.
- Commit message: `M3: add exercise method proof slice`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Concrete ranges may be under-sourced or read like prescriptions.
- Rollback/recovery:
  - Narrow the wording to source-supported ranges, remove unsupported claims, or
    revert a problematic page from the proof slice and return to spec if the
    six-method coverage can no longer be satisfied.

### M4. Manual Evidence and Broad-Rollout Gate

- Milestone state: closed
- Goal: record the semantic proof that automation cannot provide before any
  broad rollout is considered.
- Requirements: R11-R13, R33-R40, AC6-AC10.
- Files/components likely touched:
  - `docs/changes/exercise-method-guidance/manual-proof/method-source-audit.md`
  - `docs/changes/exercise-method-guidance/manual-proof/beginner-comprehension.md`
  - `docs/changes/exercise-method-guidance/manual-proof/validation-ledger.md`
  - `docs/changes/exercise-method-guidance/review-log.md`
- Dependencies:
  - M3 proof-slice pages must be complete enough to inspect.
- Tests to add/update:
  - no new production tests expected unless manual review exposes a repeatable
    validation gap.
- Implementation steps:
  - Audit at least one page from each active method type for source support of
    method guidance.
  - Record beginner-comprehension evidence showing whether a reader can state
    the starting point, effort, stop condition, and non-prescription boundary.
  - Record a validation ledger with exact commands and residual risks.
  - State that broad rollout is not authorized until this slice passes reviews
    and a later plan selects the next batch.
- Validation commands:
  - `python3 tools/checks/check_privacy.py docs/changes/exercise-method-guidance`
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md principles exercises patterns`
  - `python3 -m unittest discover -s tests`
- Expected observable result: manual evidence closes the source-support and
  comprehension gaps for the proof slice without claiming broad rollout is done.
- Commit message: `M4: record exercise method proof evidence`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Reader-test or source-audit findings may require content changes from M3.
- Rollback/recovery:
  - Move the affected milestone back to `resolution-needed`, fix the page or
    checker, and rerun the relevant code-review loop.

### Lifecycle Closeout

- Milestone state: planned
- Goal: complete non-implementation lifecycle gates after all implementation
  milestones close.
- Requirements: AC1-AC10 and repository workflow requirements.
- Files/components likely touched:
  - `docs/changes/exercise-method-guidance/explain-change.md`
  - `docs/changes/exercise-method-guidance/verify-report.md`
  - `docs/plan.md`
  - this plan
- Dependencies:
  - M1-M4 closed and required code-review or review-resolution loops complete.
- Tests to add/update:
  - no new tests expected; this milestone reruns full validation.
- Implementation steps:
  - Record durable explain-change after reviewed implementation.
  - Run final verification against artifacts, tests, content, proof records,
    and workflow state.
  - Prepare PR handoff only after verification passes.
  - Close or update the plan lifecycle state only when the owning downstream
    gate provides evidence.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md principles exercises patterns`
  - `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md docs specs tools tests principles exercises patterns`
  - `git diff --check`
- Expected observable result: final local evidence is recorded for PR handoff
  without claiming unobserved CI.
- Commit message: `Close exercise method guidance implementation`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Plan or lifecycle state can drift after review-resolution loops.
- Rollback/recovery:
  - Restore the active milestone state, update the current handoff summary, and
    rerun the relevant review before final verification.

## Validation plan

- `python3 -m unittest discover -s tests`: full local regression suite.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`:
  focused Markdown-first contract and real-page coverage.
- `python3 -m unittest tests.test_responsible_breadth_m1`: expanded-content and
  principle-page contract coverage.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md principles exercises patterns`:
  real Markdown contract validation for the affected surfaces.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md docs specs tools tests principles exercises patterns`:
  privacy scan for content, tools, tests, and proof records.
- `git diff --check`: whitespace and patch hygiene for tracked edits.
- Manual source audit: sample at least one page from each active method type.
- Manual beginner comprehension proof: confirm the reader can identify starting
  point, effort, stop condition, and the non-prescription boundary.

## Risks and recovery

- Risk: Method guidance drifts into personal programming.
  - Recovery: remove adaptive wording, keep starter ranges static, and rerun
    forbidden-language checks plus code review.
- Risk: Page-level method claims are under-sourced.
  - Recovery: narrow claims to what page-local sources support or remove the
    concrete claim.
- Risk: Validation becomes too broad and fails unrelated exercise pages.
  - Recovery: make first-slice adoption explicit and keep unselected pages under
    their prior contract until selected by a later slice.
- Risk: Pattern previews contradict full exercise pages.
  - Recovery: align or remove the preview starter range and record the manual
    review outcome.
- Risk: Beginner-comprehension evidence exposes unclear method wording.
  - Recovery: revise the affected page and repeat the comprehension prompt for
    that page before M4 closes.

## Dependencies

- Plan-review must approve this execution plan before test-spec authoring.
- Test-spec and test-spec-review must map requirements to concrete automated
  tests and manual evidence before implementation.
- M1 must establish validation/template behavior before broad proof-slice page
  edits.
- M2 must create the principle page before M3 links to it from exercise pages.
- M3 must finish before M4 source-audit and beginner-comprehension proof can be
  meaningful.
- Code-review and any required review-resolution loop must complete per
  milestone before lifecycle closeout.

## Progress

- 2026-07-04: Proposal, spec, architecture review, and plan review are
  approved. Architecture status wording was normalized for downstream planning.
  Initial test spec drafted and routed to test-spec-review.
- 2026-07-04: Test-spec-review R1 requested changes for validation-command
  ownership and manual-proof metadata. Revised `specs/exercise-method-guidance.test.md`
  with EMG-CMD1 through EMG-CMD14, a milestone proof map, and expanded EMG-M1
  through EMG-M3 metadata; routed to test-spec-review R2.
- 2026-07-04: Test-spec-review R2 approved the revised proof map and allowed
  implementation handoff for M1.
- 2026-07-04: M1 implementation started. Same-slice completeness set is the
  exercise template method section, slice-aware visible-Markdown method
  validation, fixture tests for valid and invalid method sections,
  compatibility notes in related specs where needed, and validation evidence
  for EMG-CMD1 through EMG-CMD4.
- 2026-07-04: M1 added the exercise template method section, visible-Markdown
  method validation, focused method-guidance tests, compatibility-note coverage,
  and required M1 validation evidence. M1 is review-requested.
- 2026-07-04: Code-review M1 R1 requested changes for CR-EMG-M1-1 and
  CR-EMG-M1-2. M1 remains active and moves to review-resolution.
- 2026-07-04: Review-resolution addressed CR-EMG-M1-1 and CR-EMG-M1-2 with
  exact method-heading validation, non-empty required-label validation, focused
  regression tests, and rerun M1 validation. M1 is review-requested for
  code-review re-review.
- 2026-07-04: Code-review M1 R2 confirmed CR-EMG-M1-1 and CR-EMG-M1-2 are
  resolved. M1 is closed and M2 implementation is next.
- 2026-07-04: M2 added the shared method principle page, focused page-content
  assertions, reusable source-index support, and a bounded principle-page
  source audit. M2 is review-requested.
- 2026-07-04: Code-review M2 R1 confirmed the principle page slice, found no
  material issues, and closed M2. M3 implementation is next.
- 2026-07-04: M3 added method sections to the six proof-slice exercise pages,
  linked the method principle page, aligned the hip-flexor pattern preview, and
  added real-page method mapping tests. M3 is review-requested.
- 2026-07-04: Code-review M3 R1 confirmed the six proof-slice exercise pages,
  found no material issues, and closed M3. M4 implementation is next.
- 2026-07-04: M4 implementation started. Same-slice completeness set is
  `method-source-audit.md`, `beginner-comprehension.md`, `validation-ledger.md`,
  broad-rollout gate wording, M4 validation evidence, and workflow handoff
  state.
- 2026-07-04: M4 recorded the source audit, beginner-comprehension proof,
  validation ledger, deferred-method guardrail, and broad-rollout gate evidence.
  M4 is review-requested.
- 2026-07-04: Code-review M4 R1 confirmed the manual proof records, found no
  material issues, and closed M4. Lifecycle Closeout is next.
- 2026-07-04: Explain-change recorded the durable rationale from problem,
  proposal, requirements, architecture, milestones, tests, reviews, and
  validation evidence to the actual diff. Final verification is next.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-04 | Sequence validation/template before content rollout. | The spec changes the exercise-page contract and needs deterministic checks before proof-slice pages rely on it. | Edit six pages first and retrofit checks later; broad exercise-page rewrite. |
| 2026-07-04 | Keep manual evidence as its own closeout milestone. | Source support and beginner comprehension are required but only partly automatable. | Hide manual proof inside code review; defer proof until broad rollout. |

## Surprises and discoveries

- M2 checker validation treated stop-condition wording on the principle page as
  a safety claim. The page now cites those stop and safety-routing lines
  directly.
- M3 checker validation treated an uncited `Stop each set...` effort line on
  chest press as a safety claim. The method guidance now cites stop, rest,
  progression, and other concrete method-label claims directly.

## Validation notes

- M1 fail-before-implementation:
  - `python3 -m unittest tests.test_exercise_method_guidance` failed before
    checker implementation because `validate_exercise_method_guidance` did not
    exist.
  - `python3 -m unittest tests.test_markdown_first_templates` failed before the
    exercise template included `## How much to do`.
- M1 targeted validation:
  - `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` passed, 7 tests.
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed, 52 tests.
  - `python3 -m unittest tests.test_exercise_method_guidance` passed, 7 tests.
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises patterns principles` passed, checked 21 Markdown files.
  - `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-method-guidance` passed, checked 89 files.
  - `git diff --check` passed.
- M1 additional smoke:
  - `python3 -m unittest discover -s tests` passed, 109 tests.
- M1 review-resolution:
  - `python3 -m unittest tests.test_exercise_method_guidance` failed before the
    checker fix for CR-EMG-M1-1 and CR-EMG-M1-2 as expected.
  - `python3 -m unittest tests.test_exercise_method_guidance` passed, 9 tests.
  - `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` passed, 7 tests.
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed, 52 tests.
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises patterns principles` passed, checked 21 Markdown files.
  - `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-method-guidance` passed, checked 90 files.
  - `python3 -m unittest discover -s tests` passed, 111 tests.
  - `git diff --check` passed.
- M1 aligned-surface audit:
  - `docs/templates/exercise-card.md` updated with the method section and required labels.
  - `tools/checks/check_markdown_first.py` updated with slice-aware method validation for visible Markdown sections and hidden-only metadata rejection.
  - `tests/test_exercise_method_guidance.py` added focused tests for valid sections, missing fields, deferred types, hidden-only metadata, forbidden wording, and compatibility notes.
  - `tests/test_markdown_first_templates.py` updated to assert template method guidance.
  - `specs/markdown-first-primer.md` and `specs/responsible-breadth.md` updated with pointer-only compatibility notes to `specs/exercise-method-guidance.md`.
- M2 fail-before-implementation:
  - `python3 -m unittest tests.test_responsible_breadth_m1` failed before the
    principle page existed, as expected.
- M2 targeted validation:
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md principles` passed, checked 5 Markdown files.
  - `python3 -m unittest tests.test_responsible_breadth_m1` passed, 28 tests.
  - `python3 tools/checks/check_privacy.py principles SOURCES.md docs/changes/exercise-method-guidance` passed, checked 17 files.
  - `git diff --check` passed.
- M2 aligned-surface audit:
  - `principles/sets-reps-holds-rest-and-progression.md` created with required Responsible Breadth principle sections, page-local sources, shared method concepts, one-variable progression, and non-prescriptive starter-range framing.
  - `SOURCES.md` added the reusable Mayo Clinic stretching source used by the principle page.
  - `tests/test_responsible_breadth_m1.py` now asserts the M2 principle page exists and explains sets, repetitions, timed holds, easy/moderate/hard effort, rest, one-variable progression, and non-prescription framing.
  - `docs/changes/exercise-method-guidance/manual-proof/principle-page-source-audit.md` records bounded source-support review for the M2 principle page.
- M3 fail-before-implementation:
  - `python3 -m unittest tests.test_exercise_method_guidance` failed before
    page edits because the six proof-slice pages lacked method sections and the
    hip-flexor pattern preview still used the older range.
- M3 targeted validation:
  - `python3 -m unittest tests.test_exercise_method_guidance` passed, 11 tests.
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md principles exercises patterns` passed, checked 22 Markdown files.
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed, 52 tests.
  - `python3 -m unittest tests.test_responsible_breadth_m1` passed, 28 tests.
  - `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md principles exercises patterns docs/changes/exercise-method-guidance` passed, checked 36 files.
  - `git diff --check` passed.
- M3 aligned-surface audit:
  - `exercises/chest-press.md`, `exercises/incline-push-up.md`, `exercises/chin-nod.md`, `exercises/plank.md`, `exercises/thoracic-extension.md`, and `exercises/kneeling-hip-flexor-stretch.md` now include `## How much to do`, exact method type, required method labels, page-local citations, and a link to the shared method principle page.
  - `patterns/anterior-pelvic-tilt.md` now aligns the kneeling hip-flexor stretch preview range with the exercise page.
  - `patterns/forward-head-posture.md` required no edit because chin nod and thoracic extension method guidance matches the existing preview range shapes.
  - `tests/test_exercise_method_guidance.py` now asserts proof-slice method mappings, method-section validity, principle links, and deterministic preview-range alignment.
- M4 targeted validation:
  - `python3 tools/checks/check_privacy.py docs/changes/exercise-method-guidance` passed, checked 18 files.
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md principles exercises patterns` passed, checked 22 Markdown files.
  - `python3 -m unittest discover -s tests` passed, 114 tests.
  - `git diff --check` passed.
- M4 aligned-surface audit:
  - `docs/changes/exercise-method-guidance/manual-proof/method-source-audit.md` records EMG-M1 source and non-prescription evidence for one proof page from each active method type.
  - `docs/changes/exercise-method-guidance/manual-proof/beginner-comprehension.md` records EMG-M2 comprehension evidence for the proof-slice pages and promoted pattern previews.
  - `docs/changes/exercise-method-guidance/manual-proof/validation-ledger.md` records EMG-M3 deferred-method guardrail evidence, M4 command results, residual risks, and the broad-rollout gate.

## Outcome and retrospective

- Pending until implementation, review, verification, and PR handoff complete.

## Readiness

- See `Current Handoff Summary`.
- Ready for verify. Final closeout is not ready until verify and PR handoff
  complete.
