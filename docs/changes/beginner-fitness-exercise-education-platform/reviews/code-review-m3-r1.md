# Code Review: Content Schema Foundation M3 R1

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/beginner-fitness-exercise-education-platform/reviews/code-review-m3-r1.md`, `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`, `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`, `docs/changes/beginner-fitness-exercise-education-platform/change.yaml`, `docs/plans/2026-06-26-content-schema-foundation.md`, `docs/plan.md`, `docs/workflows.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-M3-1, CR-M3-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/beginner-fitness-exercise-education-platform/reviews/code-review-m3-r1.md`
- Review log: `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`
- Review resolution: `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`
- Reviewed milestone: M3
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M3, M4
- Required review-resolution: yes
- Finding IDs: CR-M3-1, CR-M3-2
- Verify readiness: not-claimed

## Review Inputs

- Review surface: commit `3b17f04` (`M3: validate lifecycle and review gates`)
- Plan: `docs/plans/2026-06-26-content-schema-foundation.md`
- Spec: `specs/content-schema.md`
- Test spec: `specs/content-schema.test.md`
- Change metadata: `docs/changes/beginner-fitness-exercise-education-platform/change.yaml`
- Validation evidence: `generated/test-results.txt`, `generated/validation-report.json`, `generated/lifecycle-validation-report.json`, `generated/review-routing-validation-report.json`, `generated/privacy-scan-report.json`, `generated/manual-proof/MP1-lifecycle-state-sync.md`
- Reviewer-side checks:
  - `rg -n "review-routing-v1|REVIEW_ROUTE_GROUPS|content/policies|change_categories" tools/validation/validate_content.py tests/test_review_routing_m3.py content/policies/review-routing-v1.json`
  - `rg -n "test_.*equipment|test_.*training|test_.*template|test_.*media|test_.*translation|test_.*taxonomy|test_.*licens|equipment_setup|general_training_principle|standard_safety_template|media_equivalence|translation_equivalence|taxonomy_change|licensing" tests/test_review_routing_m3.py tests/fixtures/review-routing content/policies/review-routing-v1.json`
  - Temporary validator probe for a `review_expired -> approved` lifecycle event with `event_type = direct_system_mutation`

## Diff Summary

M3 adds lifecycle and review-routing validation:

- Adds review/publication transition constants, audit-event required-field checks, approval-event required-field and digest checks, review-sensitive edit checks, publication eligibility gates, and `--expect-mixed`.
- Adds data-shaped review-routing policy content at `content/policies/review-routing-v1.json`.
- Adds lifecycle and review-routing fixtures plus `tests/test_lifecycle_m3.py` and `tests/test_review_routing_m3.py`.
- Updates taxonomy/schema summaries, generated validation evidence, MP1 manual proof, and workflow routing metadata for M3 review handoff.

## Findings

## Finding CR-M3-1

- Finding ID: CR-M3-1
- Severity: major
- Location: `tools/validation/validate_content.py:244`; `tools/validation/validate_content.py:843`; `content/policies/review-routing-v1.json:2`; `docs/plans/2026-06-26-content-schema-foundation.md:214`
- Evidence: The M3 plan requires the review-routing matrix to be encoded as data, not hard-coded prose scattered through validation rules. The commit adds `content/policies/review-routing-v1.json`, but the validator does not load or reference that file. `rg` finds `content/policies/review-routing-v1.json` only in the policy file itself, while `tools/validation/validate_content.py` uses the in-code `REVIEW_ROUTE_GROUPS` constant and `required_review_groups()` reads from that constant. This means a reviewed policy fixture change can drift from executable validation without failing tests.
- Required outcome: Publication eligibility and missing-tier checks must be computed from the repository-native review-routing policy data, or an explicit generated/loaded policy fixture that is validated against the same source of truth.
- Safe resolution path: Load `content/policies/review-routing-v1.json` through a bounded validator input path, validate its shape, and pass the loaded route map into `required_review_groups()`/`validate_review_routing()`. Add a regression that mutates or uses a fixture-only policy route so tests fail if the validator ignores the policy data file.
- needs-decision rationale: none

## Finding CR-M3-2

- Finding ID: CR-M3-2
- Severity: major
- Location: `tools/validation/validate_content.py:197`; `tools/validation/validate_content.py:761`; `specs/content-schema.md:182`; `specs/content-schema.md:193`
- Evidence: The spec allows `review_expired -> approved` only through a recorded review completion event and forbids direct system mutation. The validator's allowed transition set includes `("review_expired", "approved")`, and `validate_lifecycle_event()` accepts that transition without checking `event_type` or requiring a matching approval completion event. A reviewer-side probe with a lifecycle event using `event_type = direct_system_mutation`, `review_status_before = review_expired`, and `review_status_after = approved` returned exit code `0`, report status `pass`, and no findings.
- Required outcome: A `review_expired -> approved` transition must be accepted only when the lifecycle event represents recorded review completion and the card has current digest-scoped approval evidence for the required tiers.
- Safe resolution path: Add a transition trigger check for `review_expired -> approved`, for example requiring a review-completion event type plus current approval evidence, and emit a stable error for direct mutation. Add a regression test and fixture proving direct mutation fails while a valid recorded review completion path passes.
- needs-decision rationale: none

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | block | CR-M3-2 shows a lifecycle transition violating the spec's recorded-review-completion condition. CR-M3-1 shows review-routing execution is not tied to the repository-native policy data required by the plan. |
| Test coverage | block | Tests cover trainer-only, PT-required, clinician-required, elevated-risk, blocked-rehab, cumulative missing tiers, approval digest, and audit status fields, but they do not prove policy-file loading or direct-mutation rejection for `review_expired -> approved`. |
| Edge cases | block | The named direct transition condition for `review_expired -> approved` lacks direct negative proof; review-routing matrix rows outside the current tests can drift from the policy file. |
| Error handling | pass | Existing M3 validation findings are structured and `--expect-mixed` gives correct mixed-fixture exit behavior. |
| Architecture boundaries | concern | The added policy file is repository-native, but executable validation currently duplicates the policy in code instead of consuming the policy artifact. |
| Compatibility | pass | CLI command shape and previous M1/M2 validator behavior remain available; no migration-affecting file format change was found in the reviewed diff. |
| Security/privacy | pass | Generated reports are privacy-scanned; no secrets or local absolute paths were exposed in the reviewed validation outputs. |
| Derived artifact currency | concern | Generated M3 reports reflect the committed tests, but they cannot prove policy-file synchronization because the validator does not load the policy file. |
| Unrelated changes | pass | The diff is scoped to M3 validator, schema summaries, fixtures, evidence, and workflow routing. |
| Validation evidence | concern | The recorded M3 commands pass, but reviewer-side probes show the selected checks are insufficient for two M3 contract requirements. |

## No-Finding Rationale

Not applicable; material findings were recorded.

## Residual Risks

- M3 does not yet exercise every review-routing matrix category named in T12. CR-M3-1 is the material blocker because loading and testing the policy data would make those rows harder to silently drift.
- CI is not configured, as expected by the approved plan.

## Milestone Handoff

M3 remains open and moves to `resolution-needed`. The next stage is `review-resolution` for CR-M3-1 and CR-M3-2. No automatic downstream handoff to M4 is allowed until M3 is fixed, rerun, and re-reviewed.
