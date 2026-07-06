# Code Review M1 R1: Brisk Walking and Everyday Walking Guidance

## Result

- Skill: code-review
- Status: inconclusive
- Artifacts changed: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m1-r1.md`; `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`; `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`; `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/change.yaml`; `docs/plan.md`
- Open blockers: governing proposal/spec/plan/test-spec/change artifacts for this change are local but untracked, so this review cannot make a clean milestone conclusion under the code-review tracked-governing-authority rule
- Next stage: blocked
- Review status: inconclusive
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m1-r1.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M1
- Milestone closeout: blocked
- Remaining implementation milestones: M1, M2, M3
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Actual M1 diff inspected in `tools/checks/check_markdown_first.py`, `docs/templates/exercise-card.md`, `tests/test_exercise_method_guidance.py`, `tests/test_markdown_first_templates.py`, and `specs/exercise-method-guidance.md`.
- Active plan inspected at `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`.
- Approved walking spec inspected at `specs/brisk-walking-and-everyday-walking.md`.
- Active test spec inspected at `specs/brisk-walking-and-everyday-walking.test.md`.
- M1 validation ledger inspected at `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/validation-ledger.md`.
- Git state inspected with `git status --short --branch` and `git diff --stat`.

## Diff Summary

M1 adds scoped method support for `basic_cardio_activity`:

- `tools/checks/check_markdown_first.py` adds `EXERCISE_METHOD_BASIC_CARDIO_ACTIVITY_PATHS` scoped to `exercises/brisk-walking.md`, accepts that type only for the scoped path, and uses cardio-activity-specific required labels that omit the default rest label.
- `docs/templates/exercise-card.md` tells authors to use `Method type: basic_cardio_activity` for non-equipment cardio activity pages such as brisk walking and to shape guidance around time, talk-test effort, repeatability, progression, and stop rules.
- `tests/test_exercise_method_guidance.py` adds direct unit proof that `basic_cardio_activity` passes for `exercises/brisk-walking.md`, fails on an unrelated exercise path, and still requires the visible cardio labels.
- `tests/test_markdown_first_templates.py` adds template assertions for `basic_cardio_activity`, time, talk test, and repeatability.
- `specs/exercise-method-guidance.md` is amended to recognize approved downstream method-type amendments, add `basic_cardio_activity` label requirements, and scope `basic_cardio_activity` to `exercises/brisk-walking.md` plus later approved non-equipment aerobic activity pages.

## Findings

No material implementation findings were recorded from the inspected M1 diff.

The review result is inconclusive because the governing artifacts cited for the review are untracked in the current branch state. The code-review skill allows local-only governing artifacts as background understanding, but does not allow a clean milestone conclusion from missing tracked governing authority.

## Checklist Coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass for inspected diff; inconclusive for milestone closeout | M1 implements BWG-R7-R13 and BWG-R27-R29 surfaces by adding scoped `basic_cardio_activity` support before page implementation. Clean closeout is blocked by untracked governing artifacts. |
| Test coverage | pass for inspected diff | `tests/test_exercise_method_guidance.py` directly covers scoped activation and missing-label failure. `tests/test_markdown_first_templates.py` covers template cues. |
| Edge cases | pass for inspected diff | EC6 is directly covered by `test_basic_cardio_activity_passes_only_for_brisk_walking_scope`; the same test also checks unrelated-path rejection. |
| Error handling | pass | Invalid method type scope produces `exercise_method_inactive_type`; missing cardio labels produce `exercise_method_missing_label`. |
| Architecture boundaries | pass for inspected diff | Markdown remains the source of truth; no hidden metadata, tracker, runtime, user input, or generated data source of truth was added. |
| Compatibility | pass | Existing active method types remain unchanged; `basic_cardio_equipment` remains separately scoped; `loaded_carry` remains inactive. |
| Security/privacy | pass | M1 adds deterministic checker/test/template/spec text only; validation ledger records a passing privacy scan. |
| Derived artifact currency | not-applicable | No generated derived artifact is introduced in M1. |
| Unrelated changes | concern | The branch/workspace also contains prior workflow, source, architecture, proposal, spec, plan, and test-spec artifacts outside the M1 code diff. This review did not treat those as implementation findings, but their untracked state blocks clean milestone closeout. |
| Validation evidence | pass for inspected diff | Validation ledger records local passes for unittest coverage, Markdown-first checker, and privacy scan. CI was not observed and is not claimed. |

## Direct Proof Notes

- BWG-T1 / EC6: `test_basic_cardio_activity_passes_only_for_brisk_walking_scope` proves scoped acceptance for `exercises/brisk-walking.md` and rejection for an unrelated exercise path.
- BWG-T2: `test_basic_cardio_activity_requires_visible_cardio_labels` proves visible beginner starting point, effort, progression, and stop language are required for the cardio activity method shape.
- Template proof: `tests/test_markdown_first_templates.py` checks the authoring template names `basic_cardio_activity`, time, talk test, and repeatability.
- Validation evidence: `validation-ledger.md` records `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_templates tests.test_markdown_first_real_pages`, `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises`, and `python3 tools/checks/check_privacy.py specs/brisk-walking-and-everyday-walking.md specs/exercise-method-guidance.md docs/templates tools tests docs/changes/2026-07-05-brisk-walking-and-everyday-walking` as passing locally.

## Residual Risks

- M2 and M3 are not implemented; the walking pages, page-local source support, manual source audit, beginner proof, and optional image decision remain pending.
- CI was not observed.
- The current workspace has untracked governing artifacts for this change, so this review does not close M1 and does not claim branch readiness, PR readiness, final verification, or CI success.

## Milestone Handoff

M1 remains `review-requested`.

Before a clean M1 closeout can be recorded, the governing artifacts needed for the clean conclusion must be present in tracked governing branch state or the workflow must explicitly choose a different review authority rule.
