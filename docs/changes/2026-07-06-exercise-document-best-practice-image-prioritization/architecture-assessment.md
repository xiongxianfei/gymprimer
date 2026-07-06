# Architecture Assessment: Exercise Document Best-Practice Image Prioritization

## Result

- Assessment: architecture-not-required
- Architecture package update: not required
- ADR update: not required
- Next stage: plan

## Rationale

This change adds a page-audit and proof workflow for existing exercise documents.
It does not introduce a new runtime component, storage model, generated-output source of truth, media classification rule, prompt-record location, provenance table shape, validation architecture, deployment path, adapter, or long-lived system boundary.

The approved exercise-image standard, exercise-document image-purposes ADR, and generated-raster prompt-record ADR already cover the generated media paths this workflow may later use.
The new contract is a content-governance layer: select exercise documents for evaluation, record page-local top-10 candidate tables, treat top-five candidates as backlog, preserve the three-image normal limit, and collect first-slice proof.

If a downstream implementation discovers that current validation cannot represent audit evidence, image-count exceptions, or prompt/provenance checks without changing the shared validation architecture, that downstream slice must return to architecture before implementation proceeds.

## Sources

- `specs/exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-image-standard.md`
- `docs/adr/2026-07-03-exercise-document-image-purposes.md`
- `docs/adr/2026-07-03-generated-raster-prompt-records.md`
