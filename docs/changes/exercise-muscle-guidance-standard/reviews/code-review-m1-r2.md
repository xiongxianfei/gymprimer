# Code Review M1 R2: Exercise Muscle Guidance Contract Checks

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/exercise-muscle-guidance-standard/reviews/code-review-m1-r2.md`, `docs/changes/exercise-muscle-guidance-standard/review-resolution.md`, `docs/changes/exercise-muscle-guidance-standard/review-log.md`, `docs/changes/exercise-muscle-guidance-standard/change.yaml`, `docs/plans/2026-07-04-exercise-muscle-guidance.md`, `docs/plan.md`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-muscle-guidance-standard/reviews/code-review-m1-r2.md`
- Review log: `docs/changes/exercise-muscle-guidance-standard/review-log.md`
- Review resolution: `docs/changes/exercise-muscle-guidance-standard/review-resolution.md`
- Reviewed milestone: M1
- Milestone closeout: closed
- Remaining implementation milestones: M2, M3
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: M1 implementation through `5c2d20f` on branch `proposal/exercise-muscle-guidance-standard`.
- Tracked governing branch state: clean working tree before this review record was written.
- Governing artifacts: `specs/exercise-muscle-guidance.md`, `specs/exercise-muscle-guidance.test.md`, `docs/plans/2026-07-04-exercise-muscle-guidance.md`, `docs/architecture/system/architecture.md`, test-spec-review R1, and code-review M1 R1 finding `CR-XMG-M1-1`.
- Validation evidence: M1 and review-resolution validation notes in `docs/plans/2026-07-04-exercise-muscle-guidance.md`.
- Reviewed implementation files: `docs/templates/exercise-card.md`, `tools/checks/check_markdown_first.py`, `tests/test_markdown_first_templates.py`, and `tests/test_exercise_muscle_guidance.py`.

## Diff Summary

The M1 implementation adds role-based muscle guidance authoring prompts, focused muscle guidance validation, and unit coverage. The R2 resolution adds the missing XMG-T8 source-surface proof: explicit role or phase muscle guidance now requires a citation in `## Muscles involved`, and citations in muscle or feel sections must have page-local reference definitions. The checker still avoids semantic source-truth evaluation and preserves untouched legacy `## Used muscles` compatibility.

## Findings

No blocking or required-change findings.

## Prior Finding Reconciliation

| Finding ID | Status | Evidence |
| --- | --- | --- |
| CR-XMG-M1-1 | resolved | `tests/test_exercise_muscle_guidance.py` includes `test_source_sensitive_role_guidance_requires_page_local_source_surface`; direct review probe returned `exercise_muscle_source_missing` for no citation, `exercise_muscle_source_missing_definition` for undefined source ID, and no findings for a page-local source definition. |

## Checklist Coverage

| Checklist item | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | pass | M1 covers template prompts, adopted heading/feel-section checks, role/phase shape, deterministic wording boundaries, source-surface checks, and legacy compatibility without broad migration. |
| Test coverage | pass | `tests/test_exercise_muscle_guidance.py` now covers XMG-T1-T5, XMG-T7, XMG-T8, and XMG-T12-style stable finding categories; template tests cover XMG-T1. |
| Edge cases | pass | Direct proof covers missing citation, undefined source ID, valid page-local source definition, untouched legacy heading compatibility, migrated legacy heading misuse, bare list, bad table columns, exact activation, EMG, and "must feel or wrong" wording. |
| Error handling | pass | New failures use stable `exercise_muscle_*` finding codes and include file paths through the existing `Finding` path field. |
| Architecture boundaries | pass | Markdown remains the source of truth; no runtime, metadata source of truth, image governance fork, generated data, or app behavior is introduced. |
| Compatibility | pass | Existing real exercise pages pass the checker, and untouched legacy `## Used muscles` pages remain compatible until migration scope. |
| Security/privacy | pass | Privacy validation passed and no private data, secrets, user-input flow, or private health evidence was introduced. |
| Derived artifact currency | pass | No generated artifacts are introduced; plan, change metadata, review log, and review-resolution are synchronized for M1 closeout. |
| Unrelated changes | pass | The code/test changes are limited to M1 checker/template/test surfaces and the required workflow artifacts. |
| Validation evidence | pass | Focused tests, template/real-page tests, checker integration, privacy scan, direct source-surface probe, and whitespace check all pass. |

## No-Finding Rationale

The R2 diff directly addresses the only M1 R1 finding with executable tests and minimal structural checker behavior. The checker proves source-surface presence without attempting semantic source validation, which remains assigned to manual audit in later milestones. Existing page compatibility is preserved by the real-page and checker integration commands.

## Residual Risks

Semantic source support and beginner comprehension are intentionally not closed by M1. They remain M2/M3 proof obligations under XMG-M1 and XMG-M2.

## Milestone Handoff

M1 is closed. The next lifecycle stage is implementation of M2, the representative proof-slice exercise pages.
