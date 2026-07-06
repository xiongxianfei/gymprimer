# Code Review M2 R1: Bird Dog Page Audit Slice

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/code-review-m2-r1.md`, `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-log.md`, `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`, `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml`, `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-EDIP-M2-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/code-review-m2-r1.md`
- Review log: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-log.md`
- Review resolution: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`
- Reviewed milestone: M2
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M2, M3
- Required review-resolution: yes
- Finding IDs: CR-EDIP-M2-1
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `d20f8f7` plus current tracked state for M2.
- Governing artifacts: `specs/exercise-document-best-practice-image-prioritization.md`, `specs/exercise-document-best-practice-image-prioritization.test.md`, `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`, and M1 evidence.
- Reviewed implementation evidence: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/m2-bird-dog-page-audit.md`, `tests/test_exercise_document_image_prioritization.py`, and `tools/checks/exercise_document_image_prioritization.py`.
- Validation evidence reviewed from the plan: focused unittest, Markdown-first, privacy, state-sync, broad changed-artifact, and `git diff --check` commands were recorded as passing for M2.

## Diff Summary

M2 adds a Bird Dog page-local audit evidence file, extends the exercise document image prioritization tests, expands the audit helper with generation-decision validation, and updates workflow state for M2 code-review handoff.
The slice selects zero generated images and does not edit `exercises/bird-dog.md`, media assets, prompt records, or provenance.

## Finding CR-EDIP-M2-1

- Finding ID: CR-EDIP-M2-1
- Severity: major
- Location: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/m2-bird-dog-page-audit.md:55`
- Evidence: M1 requires each candidate row to record rank, candidate image, page section, accepted purpose, rationale, five scoring fields, total score, and disposition. The M2 top-10 table records only one total `Score` column, and the scoring notes state that the table records total score only.
- Required outcome: The Bird Dog page-local candidate table must record the five per-candidate scoring fields required by M1, while retaining the total score and disposition for each rank.
- Safe resolution path: Expand the M2 audit evidence table or add an adjacent per-rank scoring matrix with beginner comprehension, setup value, muscle-attention value, page value, and readiness scores for ranks 1-10. Rerun Markdown/privacy validation and route M2 back to code-review.
- needs-decision rationale: none

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | concern | M2 preserves the evaluation-trigger distinction and selects zero generated images, but CR-EDIP-M2-1 leaves the page-local audit evidence short of the approved candidate scoring contract. |
| Test coverage | pass | Focused tests cover image-count exceptions, accepted purposes, second muscle-attention prevention, forbidden claims, and slice scope. |
| Edge cases | pass | The changed helper rejects fourth/fifth image additions without exception approval and prevents second muscle-attention images in generation decisions. |
| Error handling | pass | Invalid generation decisions return explicit validation errors instead of silently passing malformed records. |
| Architecture boundaries | pass | The change stays in change-local evidence, focused tests, and a focused helper; no shared media architecture or template update is introduced. |
| Compatibility | concern | The M2 human-readable audit evidence omits required per-field scores, which weakens compatibility with the M1 proof contract. |
| Security/privacy | pass | The reviewed diff introduces no secrets, private data, hosted behavior, or medical/coaching claims. |
| Derived artifact currency | pass | Plan index, active plan, change metadata, review log, and review-resolution are updated by this review record. |
| Unrelated changes | pass | The M2 implementation surface is limited to the audit slice, tests, helper, explanation, and lifecycle artifacts. |
| Validation evidence | concern | Recorded validation commands are relevant, but they do not detect the missing per-field scores in the Markdown evidence file. |

## Direct-Proof Gaps

CR-EDIP-M2-1 is a proof-artifact gap.
The structured helper tests prove the intended scoring schema for fixture records, but the actual M2 Markdown audit evidence does not carry those per-candidate fields.

## Milestone Handoff

- Reviewed milestone: M2
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes, CR-EDIP-M2-1
- Remaining implementation milestones: M2, M3
- Next stage: review-resolution for M2
- Final closeout readiness: not ready because M2 has an open review finding and M3 remains unimplemented.

## Sources

- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/m1-audit-criteria.md`
- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/m2-bird-dog-page-audit.md`
- `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-document-best-practice-image-prioritization.test.md`
