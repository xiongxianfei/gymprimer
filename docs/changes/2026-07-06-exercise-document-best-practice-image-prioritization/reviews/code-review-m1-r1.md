## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/code-review-m1-r1.md`, `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-log.md`, `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`, `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`, `docs/plan.md`, `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-EDIP-M1-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/code-review-m1-r1.md`
- Review log: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-log.md`
- Review resolution: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`
- Reviewed milestone: M1
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M1, M2, M3
- Required review-resolution: yes
- Finding IDs: CR-EDIP-M1-1
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: commit `f69d1e1` (`M1: implement exercise document image audit proof`).
- Tracked governing branch state: committed proposal/spec/test-spec/plan/review artifacts, M1 helper, M1 tests, M1 evidence, and lifecycle metadata on `main`.
- Governing artifacts: `specs/exercise-document-best-practice-image-prioritization.md`, `specs/exercise-document-best-practice-image-prioritization.test.md`, `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`, `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/test-spec-review-r1.md`.
- Validation evidence reviewed: commit body and active plan validation notes for `python3 -m unittest tests.test_exercise_document_image_prioritization`, Markdown-first check, privacy check, state-sync inspection, and `git diff --check`.

## Diff summary

M1 adds the per-exercise image-prioritization governing artifacts, a pure helper at `tools/checks/exercise_document_image_prioritization.py`, focused tests at `tests/test_exercise_document_image_prioritization.py`, change-local audit criteria evidence, an explain-change surface, and lifecycle state updates routing M1 to code-review.
It does not edit exercise pages, media assets, prompt records, provenance rows, or templates.

## Findings

### CR-EDIP-M1-1 - Top-five generation dispositions can bypass backlog semantics

Finding ID: CR-EDIP-M1-1

Severity: major

Location: `tools/checks/exercise_document_image_prioritization.py:130`

Evidence:

The approved spec says "The top five ranked candidates MUST be treated as a candidate backlog, not an automatic generation target" and the test spec says EDIP-T5 must prove that "Top-five backlog without generation passes; generated subset must be separately justified."
The implementation only rejects top-five candidates whose disposition is exactly `automatic_generation`.
It still allows rank 1-5 candidates with `generate_now` or `first_generation_candidate`, because the `GENERATE_DISPOSITIONS` check is applied only when `rank > 5`.
The focused test covers `automatic_generation` for rank 1-5 and `generate_now` for rank 6, but it does not cover `generate_now` or `first_generation_candidate` for rank 1-5.

Required outcome:

M1 validation must reject or require explicit separate generation-decision justification for any top-five candidate disposition that selects generation directly.
The focused tests must include rank 1-5 cases for `generate_now` and `first_generation_candidate`, or an equivalent direct proof that top-five backlog status cannot become an automatic generated-image batch.

Safe resolution path:

Extend EDIP-T5 tests with top-five `generate_now` and `first_generation_candidate` fixtures.
Update `validate_candidate_table` or related audit validation so generation dispositions in ranks 1-5 are rejected unless the audit records a separate generation decision with the required M1/M2-safe justification.
Rerun M1 validation and return M1 to code-review.

## Checklist coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | concern | CR-EDIP-M1-1 shows partial mismatch with R9 and EDIP-T5. Other M1 surfaces align with the no-page-edit/no-media-edit scope. |
| Test coverage | concern | Focused tests cover inventory, required fields, candidate scores, `automatic_generation`, sixth-candidate generation, style-only replacement, and template deferral, but miss top-five `generate_now` and `first_generation_candidate`. |
| Edge cases | concern | EDIP-T5's named top-five backlog boundary is not fully proved. |
| Error handling | pass | Invalid missing fields, score mismatches, short-table rationale, style-only replacement, and premature template updates return stable errors. |
| Architecture boundaries | pass | The change is helper/test/evidence-only and does not alter media architecture, prompt-record architecture, or validation architecture. |
| Compatibility | pass | Existing exercise pages and media are not changed; M1 evidence records current counts without migration. |
| Security/privacy | pass | No secrets or private data were observed in the reviewed helper, tests, or evidence; privacy validation was recorded. |
| Derived artifact currency | pass | Plan, plan index, change metadata, review log, and evidence route M1 to code-review before this review; this review updates routing to review-resolution. |
| Unrelated changes | pass | The diff is scoped to this change's governing artifacts, helper, tests, evidence, and lifecycle state. |
| Validation evidence | concern | The recorded M1 commands are relevant, but the focused test suite does not prove the top-five generation-disposition boundary identified in CR-EDIP-M1-1. |

## No-finding rationale

Not applicable.
This review records one material finding.

## Residual risks

No additional material findings were identified in this first-pass review.
M2 and M3 remain unimplemented and were not reviewed for closeout.

## Milestone handoff

M1 remains open with `Milestone state: resolution-needed`.
Next stage is review-resolution for CR-EDIP-M1-1.
No branch readiness, PR readiness, final verification, or CI status is claimed.

## Sources

- `tools/checks/exercise_document_image_prioritization.py`
- `tests/test_exercise_document_image_prioritization.py`
- `specs/exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-document-best-practice-image-prioritization.test.md`
- `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`
