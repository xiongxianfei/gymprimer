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

## Changed Surfaces

| Surface | Why it changed | Governing requirement |
|---|---|---|
| `tools/checks/exercise_document_image_prioritization.py` | Adds the pure helper used by focused tests and future audit proof. | R1-R9, R19-R22 |
| `tests/test_exercise_document_image_prioritization.py` | Adds M1 proof for inventory, audit fields, candidate scoring, backlog semantics, replacement reasons, and template deferral. | EDIP-T1 through EDIP-T5, EDIP-T10, EDIP-T11 |
| `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/m1-audit-criteria.md` | Records the first-slice audit criteria and current fewer-than-five evaluation population. | R1, R2, R5-R9, R19-R22 |
| `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md` | Records M1 implementation progress, validation evidence, and review-requested handoff. | Implement skill plan-update requirement |
| `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/change.yaml` and `docs/plan.md` | Keep lifecycle routing synchronized for M1 code-review handoff. | Workflow metadata |

## Unaffected Surfaces

| Surface | Rationale |
|---|---|
| `exercises/` | M1 is audit contract work only; page-specific edits belong to M2. |
| `media/` and `media/PROVENANCE.md` | M1 does not generate or promote images. |
| `docs/templates/exercise-card.md` | The approved direction requires first-slice criteria to be proven change-locally before template updates. |

## Sources

- `specs/exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-document-best-practice-image-prioritization.test.md`
- `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`
