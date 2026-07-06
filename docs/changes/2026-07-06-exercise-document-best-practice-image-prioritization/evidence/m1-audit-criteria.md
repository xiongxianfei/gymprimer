# M1 Audit Criteria and Evaluation Population

Audit date: 2026-07-06

Scope: current `exercises/*.md` pages.

## Decision

M1 records the audit contract for per-exercise-document image prioritization.
It does not edit exercise pages, generate images, update media assets, update prompt records, update `media/PROVENANCE.md`, or update `docs/templates/exercise-card.md`.

The fewer-than-five threshold is an evaluation trigger only.
It does not mean a page should be brought to five images.

## Evaluation Population

Pages with fewer than five current Markdown image references enter the first evaluation population.

| Exercise page | Current image count | M1 evaluation status |
|---|---:|---|
| `exercises/band-pull-apart.md` | 2 | included |
| `exercises/bird-dog.md` | 1 | included |
| `exercises/brisk-walking.md` | 2 | included |
| `exercises/chest-press.md` | 2 | included |
| `exercises/chin-nod.md` | 2 | included |
| `exercises/dead-bug.md` | 1 | included |
| `exercises/glute-bridge.md` | 1 | included |
| `exercises/hip-hinge.md` | 1 | included |
| `exercises/incline-push-up.md` | 1 | included |
| `exercises/kneeling-hip-flexor-stretch.md` | 1 | included |
| `exercises/lat-pulldown.md` | 2 | included |
| `exercises/plank.md` | 2 | included |
| `exercises/prone-y-t.md` | 2 | included |
| `exercises/rowing-machine.md` | 3 | included |
| `exercises/seated-row.md` | 2 | included |
| `exercises/tai-chi-basics.md` | 3 | included |
| `exercises/thoracic-extension.md` | 2 | included |
| `exercises/wall-slide.md` | 2 | included |
| `exercises/baduanjin-basics.md` | 5 | excluded from the fewer-than-five population |

## Required Page-Local Audit Fields

Each page-local audit must record:

- `exercise_document`
- `current_image_count`
- `existing_image_purposes`
- `section_coverage`
- `source_support_issues`
- `existing_image_decisions`
- `candidate_table`
- `generation_decision`
- `validation_expectations`
- `rollback_path`
- `top_five_are_backlog`
- `template_update_status`

## Candidate Table Criteria

Each selected page should record ten candidates unless the audit records why fewer meaningful candidates exist.
Each candidate row must record rank, candidate image, page section supported, accepted exercise-image purpose, why it matters, five scoring fields, total score, and disposition.

The five scoring fields are:

- beginner comprehension
- setup value
- muscle-attention value
- page value
- readiness

The first five candidates are candidate backlog.
They are not an automatic generated-image batch.
Candidate 6 or later may not be generated in the same slice without downstream rationale that delaying the related candidate would create worse churn.

## Existing Image Decision Criteria

Existing acceptable images should be preserved.
Style consistency alone is not an accepted replacement reason.

Accepted replacement reasons are:

- unsafe visual implication [Source][local-m1-audit-criteria-exercise-image-standard]
- missing required provenance or prompt record
- alt text that cannot be corrected without asset change
- misleading common-mistake framing
- incompatible purpose
- low readability
- duplicate coverage after better images are added

## Template Boundary

The first slice records criteria in this change-local evidence.
`docs/templates/exercise-card.md` remains unchanged in M1.
A later template update needs downstream approval after first-slice criteria prove reusable.

## Validation

M1 validation is recorded in the active plan.

## Sources

- `specs/exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-image-standard.md`

[local-m1-audit-criteria-exercise-image-standard]: ../../../../specs/exercise-image-standard.md
