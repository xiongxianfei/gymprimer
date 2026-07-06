# Code Review R1: Necessary Images and Baduanjin Exercise M1

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-r1.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-log.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/change.yaml`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-M1-001
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-r1.md`
- Review log: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-log.md`
- Review resolution: required
- Reviewed milestone: M1
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M1 resolution, then M2, M3, M4
- Required review-resolution: yes
- Finding IDs: CR-M1-001
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `8b08f0b` (`M1: implement Baduanjin validation proof map`).
- Tracked governing branch state: `proposal/baduanjin-exercise-images` at `8b08f0b`.
- Governing artifacts: `specs/necessary-images-and-baduanjin-exercise.md`, `specs/necessary-images-and-baduanjin-exercise.test.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`.
- Validation evidence: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md`.
- Relevant implementation files: `tools/checks/check_markdown_first.py`, `tests/test_exercise_image_standard.py`, `tests/test_exercise_method_guidance.py`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/image-candidate-pool.md`.

## Diff Summary

M1 adds workflow artifacts for the Baduanjin change, a path-scoped image-count exception for `exercises/baduanjin-basics.md`, Baduanjin image-standard fixtures, Baduanjin low-load method fixtures, candidate-pool evidence, and validation notes.

## Findings

## Finding CR-M1-001

- Finding ID: CR-M1-001
- Severity: major
- Location: `tests/test_exercise_image_standard.py:291`, `tests/test_exercise_method_guidance.py:301`, `specs/necessary-images-and-baduanjin-exercise.test.md:96`, `specs/necessary-images-and-baduanjin-exercise.test.md:194`
- Evidence: The M1 proof map requires `BJ-T8` before M1 code-review, and BJ-T8 requires negative fixtures for treatment, full-form, combat, fall-prevention, recovery-care, and adaptive coaching language. The added Baduanjin tests cover adaptive/recovery-care method wording and one combat-framed image note, but they do not directly test the treatment, full-form, fall-prevention, or adaptive-coaching forbidden-scope page fixtures required by BJ-T8.
- Required outcome: M1 must include direct automated proof for the BJ-T8 forbidden-scope fixtures assigned to M1, or the governing test spec and plan must be revised and re-reviewed to defer that coverage.
- Safe resolution path: Add focused Baduanjin negative fixtures to the existing checker/unit test surface that fail on treatment, full-form, fall-prevention, and adaptive-coaching wording while preserving the accepted non-clinical, non-martial, static-page boundary; rerun the M1 validation commands and return M1 to code-review.
- needs-decision rationale: none

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | concern | The image-limit exception is scoped to `exercises/baduanjin-basics.md`, matching R27, but BJ-T8 proof for R4, R7-R9, and R43 is incomplete for M1. |
| Test coverage | block | M1 proof map requires BJ-T8 before code-review; the added tests do not cover all named forbidden-scope fixture categories. |
| Edge cases | block | Named BJ-T8 edge cases for treatment, full-form, fall-prevention, and adaptive coaching lack direct proof. |
| Error handling | pass | The image-count failure path and muscle-attention failure path are directly exercised by Baduanjin fixtures. |
| Architecture boundaries | pass | The checker change preserves a path-scoped exception and does not introduce runtime, media generation, or app behavior. |
| Compatibility | pass | The default exercise image limit remains three for unrelated pages, covered by `test_baduanjin_exception_does_not_change_default_three_image_limit`. |
| Security/privacy | pass | Validation notes record the privacy scan over change-local evidence; the diff does not add secrets or personal data. |
| Derived artifact currency | pass | No generated media or derived output is introduced in M1; downstream media artifacts remain assigned to later milestones. |
| Unrelated changes | pass | Changed files align with the workflow artifacts, checker, and tests named by M1. |
| Validation evidence | concern | Reported commands are relevant, but they do not prove the missing BJ-T8 forbidden-scope fixture categories. |

## No-Finding Rationale

Not applicable. This review has one material finding.

## Direct-Proof Gaps

- BJ-T8 lacks direct M1 proof for treatment, full-form, fall-prevention, and adaptive-coaching negative fixtures.

## Milestone Handoff State

- Reviewed milestone: M1
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M1 resolution, then M2, M3, M4
- Next stage: review-resolution
- Final closeout readiness: not ready because M1 has an unresolved review finding and M2-M4 remain unimplemented.

## Sources

- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
- [M1 validation notes](../validation-notes.md)
