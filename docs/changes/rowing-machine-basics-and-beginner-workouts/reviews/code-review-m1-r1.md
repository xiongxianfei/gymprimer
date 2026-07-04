# Code Review M1 R1: Rowing Machine Basics and Beginner Workout Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m1-r1.md`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m1-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M1
- Milestone closeout: closed
- Remaining implementation milestones: M2, M3, M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `28ff7ee` for M1 implementation, especially
  `tools/checks/check_markdown_first.py` and
  `tests/test_exercise_method_guidance.py`.
- Tracked governing branch state: commit `28ff7ee` includes the accepted
  proposal, approved spec, approved architecture update, active plan, active
  test spec, test-spec-review R2, M1 implementation, and M1 validation notes.
- Governing artifacts:
  - `specs/rowing-machine-basics-and-beginner-workouts.md`
  - `specs/rowing-machine-basics-and-beginner-workouts.test.md`
  - `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/test-spec-review-r2.md`
  - `specs/exercise-method-guidance.md`
- Validation evidence:
  - plan validation notes for M1;
  - commit message validation evidence in `28ff7ee`;
  - independent reviewer rerun of
    `python3 -m unittest tests.test_exercise_method_guidance`.

## Diff Summary

M1 adds path-aware activation for `basic_cardio_equipment` in
`tools/checks/check_markdown_first.py`. The method type remains listed as
deferred globally, but `is_active_exercise_method_type` accepts it when the
validated path is `exercises/rowing-machine.md`. `loaded_carry` remains
inactive.

The checker also replaces the single required-label list with label groups so
the existing `Rest:` and `Stop if:` labels still work while cardio wording can
use `Rest/reset:` and `Stop condition:`. Tests now exercise the rowing-machine
valid path, an unrelated invalid path, missing cardio label handling, existing
active method pages, deferred `loaded_carry`, hidden-only metadata, and
forbidden method wording.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | pass | R15-R17 and R39-R40 require scoped `basic_cardio_equipment`, visible labels, no broad activation, and `loaded_carry` deferral. The diff accepts cardio only for `exercises/rowing-machine.md` and keeps `loaded_carry` outside active types. |
| Test coverage | pass | `test_basic_cardio_equipment_passes_only_for_rowing_machine_scope` directly proves the valid rowing path and unrelated invalid path; existing tests still cover active method types, hidden-only metadata, and forbidden wording. |
| Edge cases | pass | EC9 is directly covered by the path-scoped cardio test; `loaded_carry` deferral remains covered by `test_unknown_and_deferred_method_types_fail`; missing labels remain covered by `test_basic_cardio_equipment_still_requires_visible_labels`. |
| Error handling | pass | Invalid method types still return `exercise_method_inactive_type`; missing label groups still return `exercise_method_missing_label`; empty label content still returns `exercise_method_empty_label`. |
| Architecture boundaries | pass | The implementation keeps visible Markdown as the source of truth and adds no runtime, API, hidden metadata, generated output, or broad cardio-equipment rollout. |
| Compatibility | pass | Existing six proof-slice method pages still pass the same checker through `test_six_proof_slice_pages_have_method_sections_and_mappings`; prior labels remain accepted. |
| Security/privacy | pass | The diff touches validation code, tests, and lifecycle records only; privacy scan evidence is recorded in the plan, and no secrets or private data appear in the reviewed code surface. |
| Derived artifact currency | pass | No generated artifact or derived output is introduced by M1. |
| Unrelated changes | pass | The implementation diff is limited to method checker behavior, method tests, and lifecycle artifacts required by the approved workflow. |
| Validation evidence | pass | M1 validation notes record all required commands. Reviewer reran `python3 -m unittest tests.test_exercise_method_guidance`, which passed with 13 tests. |

## No-Finding Rationale

The implementation satisfies the narrow M1 contract: it makes
`basic_cardio_equipment` usable for the approved rowing-machine path, rejects
the same method type on an unrelated exercise path, preserves all previously
active method types, and keeps `loaded_carry` inactive. The tests are targeted
at the changed public checker function and include direct negative coverage for
the main broad-activation risk.

The label-alias change is acceptable because `specs/exercise-method-guidance.md`
requires the listed labels or equivalent plain-language lines, and the rowing
spec requires cardio wording for rest/reset and stop condition. The existing
`Rest:` and `Stop if:` labels remain valid, so current content compatibility is
preserved.

## Residual Risks

M2 still needs real-page tests and source/content drafting for
`exercises/rowing-machine.md`. This M1 review does not claim the rowing page,
manual proof, final verification, branch readiness, PR readiness, or CI success.
