# Code Review M1 R2: Brisk Walking and Everyday Walking Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m1-r2.md`; `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`; `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`; `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/change.yaml`; `docs/plan.md`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m1-r2.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M1
- Milestone closeout: closed
- Remaining implementation milestones: M2, M3
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Review surface: committed branch diff at `c1e5b6d Add walking guidance workflow and method support`.
- Tracked governing branch state: proposal, spec, architecture amendment, plan, test spec, validation ledger, review records, method contract changes, tests, and checker/template changes are present in tracked branch state.
- Active plan: `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`.
- Approved spec: `specs/brisk-walking-and-everyday-walking.md`.
- Active test spec: `specs/brisk-walking-and-everyday-walking.test.md`.
- Method contract spec: `specs/exercise-method-guidance.md`.
- Validation evidence: implementation ledger plus review-time reruns listed below.

## Diff Summary

M1 adds scoped, test-backed support for `basic_cardio_activity` before the walking pages are implemented:

- `tools/checks/check_markdown_first.py` scopes `basic_cardio_activity` to `exercises/brisk-walking.md` and uses cardio-activity label requirements: beginner starting point, effort, progression, and stop language.
- `docs/templates/exercise-card.md` adds author guidance for non-equipment cardio activity pages using time, talk-test effort, repeatability, progression, and stop rules rather than strength-training sets and repetitions.
- `tests/test_exercise_method_guidance.py` proves `basic_cardio_activity` passes for `exercises/brisk-walking.md`, fails on an unrelated exercise path, and fails when required cardio labels are missing.
- `tests/test_markdown_first_templates.py` checks that the exercise template names `basic_cardio_activity`, time, talk test, and repeatability.
- `specs/exercise-method-guidance.md` records the downstream method-contract amendment and keeps the method scoped to approved non-equipment aerobic activity pages.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | BWG-R7-R13 and BWG-R27-R29 are satisfied for M1 by visible scoped method support, static method-shape cues, and no tracker/adaptive/runtime additions. |
| Test coverage | pass | `test_basic_cardio_activity_passes_only_for_brisk_walking_scope`, `test_basic_cardio_activity_requires_visible_cardio_labels`, and template assertions cover the changed behavior. |
| Edge cases | pass | EC6 is directly covered by the scoped method-type test; unrelated-path rejection prevents broad activation. |
| Error handling | pass | Invalid method scope emits `exercise_method_inactive_type`; missing required cardio labels emit `exercise_method_missing_label`. |
| Architecture boundaries | pass | The implementation stays Markdown-first, keeps visible Markdown as source of truth, and does not introduce user input, hidden metadata, generated source-of-truth data, or runtime behavior. |
| Compatibility | pass | Existing active method types are unchanged; `basic_cardio_equipment` remains separately scoped; `loaded_carry` remains inactive. |
| Security/privacy | pass | No secrets, private data, trackers, accounts, user input, or storage were added; privacy scan passed. |
| Derived artifact currency | pass | No generated derived artifact is introduced by M1; lifecycle artifacts now agree on M1 review state after this record. |
| Unrelated changes | pass | The implementation slice is limited to the approved walking workflow artifacts, method contract, template, checker, tests, sources, and lifecycle records. |
| Validation evidence | pass | Review-time validation reruns passed locally; CI was not observed and is not claimed. |

## No-Finding Rationale

The diff implements the exact M1 contract: make `basic_cardio_activity` authorable and checkable before adding page content.

The checker accepts the method only for `exercises/brisk-walking.md`, so the new method type does not become broadly available.

The required cardio labels match the approved exception in the method contract: brisk walking may omit a rest label when repeatability or accumulated walking time is the method shape.

The tests prove the named method-scope edge case directly, and the template change gives authors enough visible guidance for M2 without adding personalization, hidden metadata, or generated data.

## Review-Time Validation

| Command | Result |
| --- | --- |
| `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_templates tests.test_markdown_first_real_pages` | pass; 29 tests |
| `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises` | pass; checked 24 Markdown files |
| `python3 tools/checks/check_privacy.py specs/brisk-walking-and-everyday-walking.md specs/exercise-method-guidance.md docs/templates tools tests docs/changes/2026-07-05-brisk-walking-and-everyday-walking` | pass; checked 80 files |

## Residual Risks

- M2 and M3 are not implemented yet, so the walking pages, page-local source support, manual source audit, beginner comprehension proof, and optional image decision remain pending.
- CI was not observed.
- This review closes M1 only; it does not claim branch readiness, PR readiness, final verification, or CI success.

## Milestone Handoff

M1 is closed.

The next stage is implementation of M2: walking Markdown pages and sources.
