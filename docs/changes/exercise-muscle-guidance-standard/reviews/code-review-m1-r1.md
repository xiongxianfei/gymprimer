# Code Review M1 R1: Exercise Muscle Guidance Contract Checks

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/exercise-muscle-guidance-standard/reviews/code-review-m1-r1.md`, `docs/changes/exercise-muscle-guidance-standard/review-resolution.md`, `docs/changes/exercise-muscle-guidance-standard/review-log.md`, `docs/changes/exercise-muscle-guidance-standard/change.yaml`, `docs/plans/2026-07-04-exercise-muscle-guidance.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-XMG-M1-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-muscle-guidance-standard/reviews/code-review-m1-r1.md`
- Review log: `docs/changes/exercise-muscle-guidance-standard/review-log.md`
- Review resolution: `docs/changes/exercise-muscle-guidance-standard/review-resolution.md`
- Reviewed milestone: M1
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M1, M2, M3
- Required review-resolution: yes
- Finding IDs: CR-XMG-M1-1
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: committed M1 handoff `dd1b3c0` (`M1: add exercise muscle guidance contract checks`).
- Tracked governing branch state: branch `proposal/exercise-muscle-guidance-standard`, clean working tree before review artifacts were recorded.
- Governing artifacts: `specs/exercise-muscle-guidance.md`, `specs/exercise-muscle-guidance.test.md`, `docs/plans/2026-07-04-exercise-muscle-guidance.md`, `docs/architecture/system/architecture.md`, and test-spec-review R1.
- Validation evidence: M1 validation notes in `docs/plans/2026-07-04-exercise-muscle-guidance.md`.
- Reviewed implementation files: `docs/templates/exercise-card.md`, `tools/checks/check_markdown_first.py`, `tests/test_markdown_first_templates.py`, and `tests/test_exercise_muscle_guidance.py`.

## Diff Summary

M1 adds role-based muscle guidance prompts to the exercise template, adds `validate_exercise_muscle_guidance()` to the Markdown-first checker, wires it into expanded exercise-page validation, and adds focused tests for heading adoption, legacy compatibility, role tables, phase tables, bare lists, deterministic forbidden wording, and stable failure categories.

## Findings

### Finding CR-XMG-M1-1

- Finding ID: CR-XMG-M1-1
- Severity: major
- Location: `tests/test_exercise_muscle_guidance.py:27`; `tools/checks/check_markdown_first.py:1330`
- Evidence: The approved test spec makes XMG-T8 required for M1 (`specs/exercise-muscle-guidance.test.md:147`) and defines it as fixtures/checker tests for page-local source definitions, global-only source references, missing sources, technical muscle names with citation, and concrete safety stop conditions (`specs/exercise-muscle-guidance.test.md:245`). The current focused test file covers headings, role shape, legacy compatibility, and wording, but has no source-support fixture or assertion. A direct review probe against `validate_exercise_muscle_guidance()` with `## Muscles involved` containing `- **Main driver:** chest helps press the handles forward.` and no citation returned `[]`.
- Required outcome: M1 must include deterministic source-surface coverage for adopted muscle guidance, at least proving that specific broad-role/source-sensitive muscle guidance cannot pass without page-local source structure where the checker can detect it, while still routing semantic source adequacy to manual review.
- Safe resolution path: Add a failing XMG-T8-focused test for missing/global-only source support on adopted muscle guidance and implement the minimal checker behavior to satisfy it without requiring semantic source truth or broad page migration. Keep untouched legacy pages compatible.
- needs-decision rationale: none

## Checklist Coverage

| Checklist item | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | concern | Template and wording checks align with R1-R23 and R31, but R24-R29 source-surface proof required by M1 is incomplete. |
| Test coverage | concern | `tests/test_exercise_muscle_guidance.py` covers XMG-T1-T5, XMG-T7, and XMG-T12-style cases, but not required XMG-T8 source-support surfaces. |
| Edge cases | concern | Named source edge cases EC4 and EC8 are not directly proved in M1 tests. |
| Error handling | pass | New checker findings use stable `exercise_muscle_*` categories and `Finding` paths for covered failure paths. |
| Architecture boundaries | pass | The checker keeps Markdown as source of truth and does not add runtime, metadata, app, or generated-data behavior. |
| Compatibility | pass | Untouched legacy `## Used muscles` pages remain compatible, and real-page validation passed without broad migration. |
| Security/privacy | pass | No secret, private data, user-input flow, or private health data was introduced; privacy scan evidence is recorded. |
| Derived artifact currency | pass | No generated artifacts are introduced; workflow artifacts were updated in tracked branch state. |
| Unrelated changes | pass | The implementation is scoped to the accepted proposal/spec/plan/test-spec artifacts and M1 checker/template/tests. |
| Validation evidence | pass | M1 validation commands are recorded, relevant, and credible for the covered behavior; the gap is coverage completeness, not command execution. |

## No-Finding Rationale

Not applicable; one material finding requires review-resolution.

## Residual Risks

Semantic source adequacy remains intentionally manual under XMG-M1, but the deterministic source-surface gap must be closed before M1 can be accepted.

## Milestone Handoff

M1 remains open and moves to `resolution-needed`. The next stage is review-resolution for CR-XMG-M1-1.
