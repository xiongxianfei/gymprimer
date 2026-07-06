# Code Review R2: M1 Top-Five Image Audit Validation

## Result

- Skill: code-review
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/code-review-r2.md`
- Review log: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M1
- Milestone closeout: closed
- Remaining implementation milestones: M2, M3
- Next stage: implement M2
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: M1 implementation plus review-resolution changes after `code-review-r1`
- Prior review: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/code-review-r1.md`
- Review resolution: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-resolution.md`
- Governing spec: `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- Test spec: `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md`
- Plan: `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- M1 evidence: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/m1-audit-framework.md`
- Validators inspected: `tools/checks/exercise_document_image_prioritization.py`, `tools/checks/check_markdown_first.py`
- Tests inspected: `tests/test_exercise_document_image_prioritization.py`, `tests/test_exercise_image_standard.py`

## Diff Summary

M1 now uses the approved `setup_value` score field in validator logic, fixtures, regression tests, and audit evidence.
Rank 1-5 `automatic_generation` is rejected in all contexts before the named-initiative allowance for `generate_now` and `first_generation_candidate`.
The review-resolution artifact records both `code-review-r1` findings as resolved and keeps M1 at `review-requested` for this rereview.

## Findings

No blocking or required-change findings.

## Prior Finding Reconciliation

| Finding ID | R2 result | Evidence |
|---|---|---|
| CR-T5IMG-M1-1 | resolved | `SCORE_FIELDS` uses `setup_value`; `test_named_top_five_audit_uses_setup_value_score_field` proves `setup_value` passes and missing `setup_value` fails. |
| CR-T5IMG-M1-2 | resolved | `validate_candidate_table` rejects rank 1-5 `automatic_generation`; `test_named_top_five_target_accepts_rank_one_to_five_generation_only` proves `generate_now` and `first_generation_candidate` pass while `automatic_generation` fails. |

## Checklist Coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | pass | R10 score fields match `setup_value`; R11 generation target behavior allows named ranks 1-5 without allowing automatic generation by rank alone. |
| Test coverage | pass | M1 tests cover named population, five-total image need, older sequence count, `setup_value`, named generation dispositions, sixth-image rejection, duplicate muscle-attention rejection, and scoped reviewer exception. |
| Edge cases | pass | Direct tests cover Baduanjin exclusion, missing prompt record despite reviewer exception, non-named reviewer rejection, sixth candidate rejection, missing `setup_value`, and named `automatic_generation` rejection. |
| Error handling | pass | Invalid audit records produce deterministic error IDs, and media validation keeps prompt-record/provenance/page-reference failures intact. |
| Architecture boundaries | pass | Changes stay in repository-local validation, tests, and change evidence; no runtime, network, hosted app, or generated media path is added in M1. |
| Compatibility | pass | Legacy non-named audit behavior still rejects direct top-five generation dispositions and preserves the default three-image limit outside exceptions. |
| Security/privacy | pass | Reviewer exception is path-scoped and does not remove prompt records, provenance rows, review status, source inputs, privacy checks, or rollback evidence. |
| Derived artifact currency | pass | `m1-audit-framework.md`, active plan, review-resolution, and change metadata reflect the resolved validator behavior. |
| Unrelated changes | pass | Reviewed M1 changes are scoped to top-five workflow artifacts, tests, and validators; unrelated unstaged `SOURCES.md` and running proposal files are excluded from this review. |
| Validation evidence | pass | Focused unit, Markdown, privacy, and whitespace commands passed after the review-resolution changes. |

## Validation Evidence

- `python3 -m unittest tests.test_exercise_document_image_prioritization tests.test_exercise_image_standard` passed with 47 tests.
- `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed.
- `python3 tools/checks/check_privacy.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed.
- `git diff --check` passed.

## No-Finding Rationale

The rereview directly checked both prior findings against the governing spec, the validator, test fixtures, audit evidence, and targeted validation.
The previously missing field-name and automatic-generation negative cases now have direct regression coverage.
No remaining M1 requirement gap was found in the inspected surfaces.

## Residual Risks

M2 will introduce generated media and real exercise-page edits, so M2 still needs page-local audits, source-support evidence, prompt records, provenance rows, rollback proof, and batch validation.

## Recommendation

- Recommendation: clean-with-notes for M1.
- Required review-resolution: no.
- Next stage: implement M2.

## Sources

- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/code-review-r1.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-resolution.md`
- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md`
- `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/m1-audit-framework.md`
- `tools/checks/exercise_document_image_prioritization.py`
- `tests/test_exercise_document_image_prioritization.py`
