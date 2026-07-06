# Code Review R1: M1 Top-Five Image Audit Validation

## Result

- Skill: code-review
- Review status: changes-requested
- Material findings: CR-T5IMG-M1-1, CR-T5IMG-M1-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/code-review-r1.md`
- Review log: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-log.md`
- Review resolution: required
- Reviewed milestone: M1
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M1, M2, M3
- Next stage: review-resolution
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `9c00446` (`M1: implement top-five image audit validation`)
- Governing spec: `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- Test spec: `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md`
- Plan: `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- M1 evidence: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/m1-audit-framework.md`
- Tests inspected: `tests/test_exercise_document_image_prioritization.py`, `tests/test_exercise_image_standard.py`
- Validators inspected: `tools/checks/exercise_document_image_prioritization.py`, `tools/checks/check_markdown_first.py`

## Diff Summary

M1 adds a named top-five exercise population, audit-field validation, five-total image counting, candidate-disposition checks, image-count exceptions for named exercise pages, reviewer-field exceptions for named page media, prompt-record reviewer exceptions, closeout-proof reviewer-evidence exceptions, M1 audit evidence, and lifecycle routing to code-review.

## Findings

### CR-T5IMG-M1-1

Finding ID: CR-T5IMG-M1-1

Severity: major

Location: `tools/checks/exercise_document_image_prioritization.py:36`

Evidence:
The approved spec says candidate scoring must use `beginner comprehension`, `setup value`, `muscle-attention value`, `page value`, and `readiness`.
The implementation still requires `safety_setup_value` in `SCORE_FIELDS`, and the M1 audit framework records `safety_setup_value` as the required score field.
A direct fixture using the approved `setup_value` field is rejected with `candidate_score_out_of_range: rank 1 safety_setup_value` and `candidate_score_mismatch`.

Required outcome:
The audit validator, tests, and M1 audit framework must use the approved score field shape, including `setup_value`, or the governing spec must be revised before implementation relies on the older field name.

Safe resolution path:
Update `SCORE_FIELDS`, fixtures, tests, and `m1-audit-framework.md` to use `setup_value`; add a regression test that a named top-five audit with `setup_value` passes and a record missing it fails.

### CR-T5IMG-M1-2

Finding ID: CR-T5IMG-M1-2

Severity: major

Location: `tools/checks/exercise_document_image_prioritization.py:287`

Evidence:
The M1 audit framework says ranks 1-5 may use `generate_now` or `first_generation_candidate` only for this named initiative.
The code suppresses all rank 1-5 generation-disposition errors when `is_top_five_initiative(record)` is true, so rank 1 with `automatic_generation` returns no audit errors.
The added test covers `generate_now` and `first_generation_candidate` but does not cover `automatic_generation` for the named initiative.

Required outcome:
The named top-five initiative must reject `automatic_generation` for ranks 1-5, while still allowing the approved `generate_now` and `first_generation_candidate` dispositions.

Safe resolution path:
Change `validate_candidate_table` so rank 1-5 `automatic_generation` always fails, and add a named-initiative regression fixture proving that `automatic_generation` is rejected while `generate_now` and `first_generation_candidate` still pass.

## Checklist Coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | block | CR-T5IMG-M1-1 and CR-T5IMG-M1-2 show M1 audit behavior does not fully match approved scoring and disposition requirements. |
| Test coverage | block | Tests cover positive named dispositions but miss approved `setup_value` and named `automatic_generation` rejection. |
| Edge cases | concern | Named population, Baduanjin exclusion, missing prompt record, sixth-image rejection, and duplicate muscle-attention paths have direct tests; the two findings identify missing named edge cases. |
| Error handling | pass | Invalid prompt records, missing provenance, sixth image, and duplicate muscle-attention cases produce deterministic validation errors. |
| Architecture boundaries | pass | The diff stays in repository-local Markdown, tests, and validation tooling. |
| Compatibility | concern | The field-name mismatch may reject future M2/M3 audit evidence written to the approved spec. |
| Security/privacy | pass | The reviewer exception remains path-scoped in media validation and does not remove prompt-record, provenance, page-ref, review-status, or privacy proof obligations. |
| Derived artifact currency | concern | M1 audit framework mirrors the wrong `safety_setup_value` field, matching the implementation but not the approved spec. |
| Unrelated changes | pass | Reviewed commit is scoped to the top-five workflow artifacts, tests, and validators. Uncommitted `SOURCES.md` and running proposal changes were not part of the reviewed commit. |
| Validation evidence | pass | The named M1 commands were recorded and are relevant, but passing them does not cover the two missing proof cases. |

## No-Finding Rationale

Not applicable because material findings were identified.

## Residual Risks

M2 should not start until review-resolution updates the validator and audit framework, reruns the M1 unit and artifact checks, and returns M1 to code-review.

## Recommendation

- Recommendation: changes requested.
- Required review-resolution: yes.
- Next stage: review-resolution for CR-T5IMG-M1-1 and CR-T5IMG-M1-2.

## Sources

- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md`
- `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/m1-audit-framework.md`
- `tools/checks/exercise_document_image_prioritization.py`
- `tests/test_exercise_document_image_prioritization.py`
