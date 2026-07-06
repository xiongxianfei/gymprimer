# Code Review R2: Necessary Images and Baduanjin Exercise M1

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-r2.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-log.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-resolution.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/change.yaml`, `docs/plan.md`
- Open blockers: none
- Next stage: implement M2
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-r2.md`
- Review log: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-log.md`
- Review resolution: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-resolution.md`
- Reviewed milestone: M1
- Milestone closeout: closed
- Remaining implementation milestones: M2, M3, M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `473e18c` (`Resolve M1 Baduanjin forbidden-scope review finding`) plus M1 implementation state.
- Tracked governing branch state: `proposal/baduanjin-exercise-images` at `473e18c`.
- Governing artifacts: `specs/necessary-images-and-baduanjin-exercise.md`, `specs/necessary-images-and-baduanjin-exercise.test.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`.
- Prior finding: CR-M1-001 in `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-r1.md`.
- Review-resolution evidence: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-resolution.md`.
- Validation evidence: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md`.
- Relevant implementation files: `tools/checks/check_markdown_first.py`, `tests/test_exercise_image_standard.py`.

## Diff Summary

The review-resolution commit adds focused forbidden-scope patterns for treatment protocol, full-form, all-eight-brocades, fall-prevention-program, and adaptive-coaching wording.
It adds `test_baduanjin_forbidden_scope_wording_fails`, which runs temporary `exercises/baduanjin-basics.md` fixtures through the Markdown checker and asserts `RB006`.
It also records the CR-M1-001 resolution and returns M1 to code-review.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | pass | The fix directly supports R4, R7-R9, R43, and BJ-T8 by rejecting treatment protocol, full-form / all eight brocades, fall-prevention program, and adaptive coaching wording. |
| Test coverage | pass | `test_baduanjin_forbidden_scope_wording_fails` covers the missing CR-M1-001 cases, and validation notes record the relevant M1 commands. |
| Edge cases | pass | The missing BJ-T8 edge cases are now directly exercised; existing M1 tests still cover image count, prompt-record, visual wording, and method failures. |
| Error handling | pass | The checker reports the existing forbidden-scope code `RB006`; the fixture asserts nonzero checker output and the expected code. |
| Architecture boundaries | pass | The change remains in Markdown validation and tests; it introduces no runtime app, media generation, hosted service, or generated exercise guidance. |
| Compatibility | pass | The new phrases extend existing forbidden-scope validation and do not alter path layout, media contracts, or the scoped five-image exception. |
| Security/privacy | pass | The resolution evidence records targeted privacy checks, and the diff adds no secrets, private data, or identifiable reader data. |
| Derived artifact currency | pass | No generated media or derived output is introduced in M1; downstream media artifacts remain assigned to later milestones. |
| Unrelated changes | pass | The rereview diff is limited to checker patterns, Baduanjin tests, and change-local lifecycle evidence for CR-M1-001. |
| Validation evidence | pass | Validation notes record `python3 -m unittest tests.test_exercise_image_standard`, `python3 -m unittest tests.test_exercise_method_guidance`, combined image/real-page tests, full unittest discovery, and `git diff --check`; the focused suite was also rerun during rereview. |

## No-Finding Rationale

CR-M1-001 is resolved because the missing forbidden-scope categories now have direct automated proof in `tests/test_exercise_image_standard.py`.
The checker additions are phrase-specific and align with the approved Baduanjin non-goals without broadening implementation beyond M1.
M1 remains limited to validation and proof-map work; the Baduanjin page, generated media, prompt records, provenance rows, visual-safety review, beginner-comprehension proof, and rollback proof are still correctly deferred to M2-M4.

## Residual Risks

- M2 must still add real-page structure, source support, method guidance, and text-only fallback behavior.
- M3 and M4 must still prove generated media, prompt records, provenance, manual visual-safety review, beginner comprehension, and rollback.

## Milestone Handoff State

- Reviewed milestone: M1
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining in-scope implementation milestones: M2, M3, M4
- Next stage: implement M2
- Final closeout readiness: not ready because M2-M4 remain unimplemented and downstream review, final verification, and PR handoff have not happened.

## Sources

- [Code review R1](code-review-r1.md)
- [Review resolution](../review-resolution.md)
- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
