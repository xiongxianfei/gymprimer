# Explain Change: Exercise Document Best-Practice Image Prioritization

## Status

active

## Scope

This reasoning surface covers the M1 implementation handoff for the exercise-document image-prioritization workflow.
It will need refresh after later implementation milestones change exercise pages, media, or proof evidence.

## M1 Change Rationale

M1 adds a focused audit helper and test suite for the proof contract approved by the spec and test spec.
The helper counts current exercise-page image references, identifies the fewer-than-five evaluation population, and validates page-local audit records for required fields, candidate scoring, top-five backlog semantics, sixth-candidate generation rationale, existing-image replacement reasons, and template deferral.

The change-local M1 evidence records the current evaluation population and reusable audit criteria without editing exercise pages or generating images.
That keeps "fewer than five images" as an evaluation trigger instead of an automatic generation target.

## M2 Change Rationale

M2 applies the approved audit workflow to one selected exercise document: `exercises/bird-dog.md`.
The page is in the fewer-than-five evaluation population and has one existing sequence image.
The page-local audit records a top-10 candidate backlog, preserves the existing image, and selects zero generated images for this slice.
Review-resolution for CR-EDIP-M2-1 added an adjacent per-rank scoring matrix so ranks 1-10 record beginner comprehension, setup value, muscle-attention value, page value, readiness, and total score.

The helper and tests now cover M2 boundaries for image-count exceptions, accepted candidate and generated-image purposes, second muscle-attention prevention, forbidden image-adjacent claims, and small first-slice scope.

## Changed Surfaces

| Surface | Why it changed | Governing requirement |
|---|---|---|
| `tools/checks/exercise_document_image_prioritization.py` | Adds the pure helper used by focused tests and future audit proof. | R1-R9, R19-R22 |
| `tests/test_exercise_document_image_prioritization.py` | Adds M1 and M2 proof for inventory, audit fields, candidate scoring, backlog semantics, image-count exceptions, purpose boundaries, replacement reasons, forbidden claims, small-slice scope, and template deferral. | EDIP-T1 through EDIP-T12 |
| `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/m1-audit-criteria.md` | Records the first-slice audit criteria and current fewer-than-five evaluation population. | R1, R2, R5-R9, R19-R22 |
| `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/m2-bird-dog-page-audit.md` | Records the first page-specific top-10 candidate backlog, per-rank scoring fields, and zero-image generated subset decision. | R3-R18, R23, AC2-AC6 |
| `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md` | Records milestone progress, validation evidence, and review-requested handoffs. | Implement skill plan-update requirement |
| `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml` and `docs/plan.md` | Keep lifecycle routing synchronized for milestone handoffs. | Workflow metadata |

## Unaffected Surfaces

| Surface | Rationale |
|---|---|
| `exercises/` | M2 audits `exercises/bird-dog.md` but does not change reader-facing page content. |
| `media/` and `media/PROVENANCE.md` | M2 selects zero generated images and does not promote media. |
| `docs/templates/exercise-card.md` | The approved direction requires first-slice criteria to be proven change-locally before template updates. |

## Sources

- `specs/exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-document-best-practice-image-prioritization.test.md`
- `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`
