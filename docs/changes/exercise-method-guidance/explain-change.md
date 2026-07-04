# Change Rationale: Exercise Method Guidance

## Summary

This change adds a Markdown-first exercise method guidance contract so selected exercise pages can answer "How much should I do?" with training-type-appropriate static guidance. It adds a focused spec, test spec, architecture amendment, execution plan, validation rules, template guidance, a shared principle page, six proof-slice exercise-page method sections, pattern-preview alignment, and manual proof records.

The implementation keeps GymPrimer inside its governed boundary: citation-backed beginner education in Markdown, not a workout planner, diagnosis tool, rehab protocol, AI coach, hosted app, user-intake flow, or adaptive program.

## Problem

Exercise pages already explained what an exercise is, how to set up, what to feel, common mistakes, easier and harder versions, safety notes, and sources. They did not consistently answer the next beginner question: how many reps, sets, holds, rounds, or rest periods to try.

A universal "2-3 sets of 8-12 reps" answer was rejected because stretches, isometric holds, low-load control drills, mobility drills, dynamic resistance exercises, and bodyweight progressions need different method shapes.

## Decision Trail

| Stage | Decision | Durable artifact |
| --- | --- | --- |
| Proposal | Use visible page-local method guidance by training type, headed `How much to do`, with static educational starter ranges. | `docs/proposals/2026-07-04-exercise-method-guidance.md` |
| Proposal review | Approved after resolving the normative home and material open questions. | `docs/changes/exercise-method-guidance/reviews/proposal-review-r2.md` |
| Spec | Created `specs/exercise-method-guidance.md` as the normative home for method section structure, method types, source rules, non-prescriptive boundaries, proof slice, and manual evidence. | `specs/exercise-method-guidance.md` |
| Architecture | Kept visible Markdown as the source of truth; rejected hidden metadata, generated taxonomy files, generated indexes, user profiles, runtime services, and adaptive logic. | `docs/architecture/system/architecture.md` |
| Plan | Split the work into M1 validation/template, M2 principle page, M3 six-page proof slice, M4 manual evidence, and Lifecycle Closeout. | `docs/plans/2026-07-04-exercise-method-guidance.md` |
| Test spec | Mapped requirements to EMG-T1 through EMG-T13, manual proofs EMG-M1 through EMG-M3, and validation commands EMG-CMD1 through EMG-CMD14. | `specs/exercise-method-guidance.test.md` |
| Reviews | M1 R1 found two validator gaps; M1 R2 and M2-M4 reviews closed all implementation milestones. | `docs/changes/exercise-method-guidance/review-log.md` |

Key requirement links:

- R1-R6 define the visible `## How much to do`, `Method type:`, and required labels contract.
- R7-R13 preserve static education, non-prescription wording, safety boundaries, and page-local source support.
- R14-R25 define method-shape expectations for the six active training types.
- R26-R29 define deferred method types and the six-page proof slice.
- R30-R32 require the shared method principle page and exercise-page links.
- R33-R35 govern pattern-preview alignment.
- R36-R38 require template and validation support.
- R39-R40 require manual source and beginner-comprehension evidence.
- R41-R42 preserve additive migration and focused-spec compatibility.

## Diff Rationale By Area

| Area | Files | Change | Reason | Evidence |
| --- | --- | --- | --- | --- |
| Direction and contract | `docs/proposals/2026-07-04-exercise-method-guidance.md`, `specs/exercise-method-guidance.md`, `specs/exercise-method-guidance.test.md` | Added accepted direction, normative requirements, examples, edge cases, validation commands, and manual proof obligations. | The method section changes the exercise-page contract and needed durable requirements before content rollout. | Proposal/spec/test-spec reviews R2/R1/R2. |
| Architecture | `docs/architecture/system/architecture.md` | Added exercise-method guidance constraints: visible Markdown source of truth, active method enum, deferred method types, no hidden metadata or generated source of truth. | The change affects source-of-truth and validation boundaries. | Architecture-review R1. |
| Execution state | `docs/plans/2026-07-04-exercise-method-guidance.md`, `docs/plan.md`, `docs/changes/exercise-method-guidance/change.yaml`, `review-log.md`, `review-resolution.md`, review records | Recorded milestone state, validation evidence, findings, resolutions, and clean reviews. | The standard workflow requires traceability from proposal through implementation, review, and closeout. | Code-review M1 R1/R2, M2 R1, M3 R1, M4 R1. |
| Template | `docs/templates/exercise-card.md` | Added the `## How much to do` section shape with visible labels. | Contributors need the contract before broad exercise-page rollout. | EMG-T1; template tests. |
| Validator | `tools/checks/check_markdown_first.py` | Added visible method-section parsing, active/deferred method type checks, hidden-only metadata rejection, required-label checks, exact-heading validation, empty-label validation, and forbidden adaptive/treatment wording checks. | Validation must catch malformed method guidance with stable categories while keeping unselected pages valid. | EMG-T2, EMG-T3, EMG-T4, EMG-T10, EMG-T13. |
| Focused tests | `tests/test_exercise_method_guidance.py`, `tests/test_markdown_first_templates.py` | Added fixture-style method tests, deferred-type tests, hidden metadata tests, forbidden-language tests, real proof-slice mapping tests, and preview-alignment assertions. | The behavior is a Markdown content contract, so unit and integration tests are appropriate. | `python3 -m unittest tests.test_exercise_method_guidance`; Markdown-first test suite. |
| Related specs | `specs/markdown-first-primer.md`, `specs/responsible-breadth.md` | Added pointer-only compatibility notes to the focused spec. | Avoids splitting the normative method contract across multiple specs. | EMG-T11. |
| Sources | `SOURCES.md` | Added the reusable Mayo Clinic stretching source. | The principle page and stretch guidance needed reusable public source support. | M2 validation and source audit. |
| Principle page | `principles/sets-reps-holds-rest-and-progression.md` | Added concise definitions of sets, reps, holds, effort, rest, one-variable progression, and non-prescription boundaries. | Exercise pages can link to one shared explanation instead of repeating long definitions. | R30-R32; EMG-T7; M2 review. |
| Proof-slice exercise pages | `exercises/chest-press.md`, `exercises/incline-push-up.md`, `exercises/chin-nod.md`, `exercises/plank.md`, `exercises/thoracic-extension.md`, `exercises/kneeling-hip-flexor-stretch.md` | Added source-cited `How much to do` sections with exact method types and required labels. | The first proof slice covers all six active method types before broad rollout. | R28-R29; EMG-T6; M3 review. |
| Pattern preview alignment | `patterns/anterior-pelvic-tilt.md` | Aligned the kneeling hip-flexor stretch preview range with the exercise page. | Pattern previews must not contradict promoted same-slice exercise guidance. | R33-R35; EMG-T8. |
| Manual proof | `docs/changes/exercise-method-guidance/manual-proof/*.md` | Added principle source audit, method source audit, beginner comprehension proof, validation ledger, deferred-method guardrail, and broad-rollout gate. | Semantic source support and reader comprehension cannot be fully proven by static parsing. | EMG-M1, EMG-M2, EMG-M3; M4 review. |

Separate from this feature rationale, `docs/learn/sessions/2026-07-04-test-spec-skill-proof-contracts.md` and `docs/follow-ups.md` were created by the earlier learning workflow. They are not required by the exercise-method spec and are not justified as part of the method-guidance implementation.

## Tests Added Or Changed

| Test or proof | What it proves | Why this level is appropriate |
| --- | --- | --- |
| EMG-T1 | The exercise template includes the method section and labels. | Template contract should be deterministic. |
| EMG-T2 | Valid method sections pass; missing heading/type/labels fail. | Parser behavior belongs in focused unit tests. |
| EMG-T3 / EMG-T13 | Hidden metadata cannot replace visible Markdown; deferred method types fail. | Source-of-truth rules need direct negative coverage. |
| EMG-T4 | Adaptive programming, rehab/treatment, and correction-promise wording fail. | Safety boundary drift is detectable with focused fixtures. |
| EMG-T5 | Structural page-local source support is checkable; semantic support routes to manual proof. | Static parsing can find citations but cannot prove source meaning. |
| EMG-T6 | The six real proof-slice pages exist, declare the exact method type, link the principle page, and pass method validation. | Real-page integration proves the promoted slice. |
| EMG-T7 | The principle page exists and explains shared method concepts. | The supporting page is user-facing content and needs content assertions. |
| EMG-T8 | Promoted pattern previews do not contradict linked exercise method guidance where deterministic. | Cross-page alignment needs integration coverage. |
| EMG-T9 | Unselected exercise pages remain valid under the prior contract. | Additive migration must not break existing pages. |
| EMG-T10 | Checker failures use stable method-specific categories. | Authors and reviewers need actionable validation output. |
| EMG-T11 | Related specs point to the focused spec without duplicating the enum. | Prevents normative drift. |
| EMG-M1 | Manual source and non-prescription audit samples one page per active method type. | Source meaning and tone need bounded human review. |
| EMG-M2 | Beginner-comprehension proof covers starting point, effort, stop condition, and non-prescription understanding. | Reader comprehension cannot be inferred from parser output. |
| EMG-M3 | Deferred method types remain inactive outside rejected/deferred references. | Final guardrail protects future-scope categories. |

## Validation Evidence Available Before Final Verify

Local validation has been run during implementation and code review. Important command evidence includes:

- `python3 -m unittest tests.test_exercise_method_guidance` passed with 11 tests after M3 implementation and review.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed with 52 tests during M1/M3 validation.
- `python3 -m unittest tests.test_responsible_breadth_m1` passed with 28 tests during M2/M3 validation.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md principles exercises patterns` passed, checking 22 Markdown files during M3/M4 validation.
- `python3 tools/checks/check_privacy.py docs/changes/exercise-method-guidance` passed, checking 18 files during M4 validation and review.
- `python3 -m unittest discover -s tests` passed with 114 tests during M4 validation and review.
- `git diff --check` passed during review and handoff checks.

Manual evidence:

- `docs/changes/exercise-method-guidance/manual-proof/principle-page-source-audit.md`
- `docs/changes/exercise-method-guidance/manual-proof/method-source-audit.md`
- `docs/changes/exercise-method-guidance/manual-proof/beginner-comprehension.md`
- `docs/changes/exercise-method-guidance/manual-proof/validation-ledger.md`

Hosted CI has not been observed. Final verification has not run yet.

## Review Resolution Summary

Material or required-change findings were resolved before this explanation:

- Test-spec review R1 findings: 2 resolved by test-spec review R2.
- Code-review M1 R1 findings: 2 resolved by M1 review-resolution and code-review M1 R2.
- Code-review M2, M3, and M4: no material findings.

The durable disposition record is `docs/changes/exercise-method-guidance/review-resolution.md`.

## Alternatives Rejected

- Doing nothing was rejected because exercise pages would still fail to answer a practical beginner question.
- A universal sets-and-reps line was rejected because it would be wrong for holds, stretches, mobility drills, and low-load control drills.
- Principle-page-only guidance was rejected as the primary solution because it would force readers to combine a technique page with a separate principle page before acting.
- Hidden metadata, YAML front matter, generated taxonomy files, generated indexes, and generated data packages were rejected for the first version because visible Markdown must remain the source of truth.
- Broad exercise-page rollout was rejected for this slice. The proof slice covers six pages only; later rollout needs a later reviewed plan.

## Scope Control

The implementation preserved these non-goals:

- no individualized workout plan;
- no adaptive programming based on symptoms, goals, equipment, measurements, or training response;
- no diagnosis, treatment, rehab protocol, posture-correction promise, or return-to-training prescription;
- no user profile, intake form, database, API, hosted app, generated public data package, or AI coach;
- no activation of `loaded_carry` or `basic_cardio_equipment`;
- no requirement that unselected exercise pages adopt method guidance in this slice.

## Risks And Follow-Ups

- Final verify still needs to run the lifecycle closeout command set and confirm artifact-code-test coherence.
- PR handoff still needs to record the final diff, validation evidence, and residual risks.
- Hosted CI has not been observed.
- The manual source and comprehension audits are bounded to the proof slice; any later edits to proof-slice method wording, source citations, starter ranges, stop guidance, method type assignments, or pattern previews must rerun the relevant manual proof.
- Broad rollout remains blocked until a later proposal/plan selects the next exercise-page batch.

## Current Handoff State

All implementation milestones M1 through M4 are closed by code review. Lifecycle Closeout is active. The next stage is `verify`; this explanation does not claim final verification, branch readiness, PR readiness, or hosted CI success.
