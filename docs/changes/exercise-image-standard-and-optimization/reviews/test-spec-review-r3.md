# Test Spec Review R3: Exercise Image Standard

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR-EIS-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/test-spec-review-r3.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Open blockers: none
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
- Stop condition: none

## Findings

### Finding TSR-EIS-2

- Finding ID: TSR-EIS-2
- Severity: major
- Location: `specs/exercise-image-standard.test.md:141`, `docs/plans/2026-07-03-exercise-image-standard.md:328`
- Evidence: The amended test spec now classifies EIS-CMD4 as `lifecycle closeout / verify`, with `Required starting = verify`, and says the broad privacy sweep is not an implementation-milestone closeout gate. The plan's general `Validation plan` section still lists the same broad `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/exercise-image-standard-and-optimization docs/plans media exercises tools tests` command under "Expected local command set after implementation begins." That contradicts the amended command ownership and can cause M1 code-review re-review to keep treating EIS-CMD4 as an active milestone gate.
- Required outcome: The test spec and plan must consistently state when EIS-CMD4 is required, with broad privacy validation deferred to lifecycle closeout / verify and milestone-level privacy checks scoped to current-change hygiene where applicable.
- Safe resolution path: Update the plan's general validation plan to mirror the amended EIS-CMD4 ownership, and update any stale test-spec readiness or next-artifact wording that still describes the pre-implementation R2 handoff. Then request test-spec-review re-review before M1 code-review re-review.
- needs-decision rationale: none

## Review Dimensions

| Dimension | Verdict | Notes |
| --- | --- | --- |
| Governing-contract alignment | concern | Moving broad privacy validation to verify is consistent with the owner's direction and still preserves R37 before PR handoff, but the plan has one stale validation-plan command that contradicts the amended proof map. |
| Requirement coverage | pass | R1-R38 still map to automated tests, smoke checks, migration checks, or manual proof IDs. R37 remains covered by EIS-T16 and EIS-CMD4 at verify. |
| Example coverage | pass | E1-E7 coverage is unchanged by the privacy timing amendment. |
| Negative and boundary coverage | pass | Invalid media purposes, provenance failures, path failures, generic alt text, unsafe wording, legacy compatibility, template behavior, privacy, and no-runtime boundaries remain represented. |
| Proof-level adequacy | pass | Deterministic media behavior remains milestone-tested; broader privacy is a verify-stage gate, and manual visual/privacy checks remain tied to image batches. |
| Milestone mapping | concern | EIS-CMD4's table row is corrected, but the plan's general validation plan still implies the broad command starts during implementation. |
| Command validity | concern | EIS-CMD4 has owner, command, starting point, failure behavior, and closeout evidence, but the stale plan section makes ownership ambiguous. |
| Fixture and data design | pass | Temporary-root fixtures, placeholder image bytes, template-context examples, and manual final-asset evidence remain deterministic and safe. |
| Manual-proof boundary | pass | EIS-RO1 through EIS-RO4 remain bounded to semantics automation cannot prove. |
| Observability | pass | EIS-T15 and command IDs preserve failure-category and command traceability. |
| Determinism and isolation | pass | Automated proof remains local and fixture-driven; no network or generated-image service is required. |
| Scope and non-goals | pass | The amendment does not add runtime, CMS, API, user input, video, medical-effectiveness testing, or existing-image migration. |
| Execution economics | concern | Deferring the broad privacy sweep to verify is reasonable, but the plan must stop advertising it as an implementation-start command. |
| Traceability | concern | EIS-CMD4 traces to verify in the test spec but to implementation-start in the plan, so traceability is currently inconsistent. |
| Implementation handoff | block | M1 code-review re-review should not proceed until the validation-path amendment is internally consistent across the test spec and plan. |

## Readiness

The validation-path amendment is not yet approved. Revise the stale validation-plan wording, then rerun test-spec-review. Implementation handoff is not allowed from this review.
