# M1 Audit Framework: Top-Five Generated Images

## Scope

This framework applies only to the named top-five exercise-image initiative approved in `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`.
It is the M1 proof surface for validation and audit structure before generated media batches begin.

## Named population

Included documents:

| Exercise document | M1 treatment |
|---|---|
| `exercises/band-pull-apart.md` | included |
| `exercises/bird-dog.md` | included |
| `exercises/brisk-walking.md` | included |
| `exercises/chest-press.md` | included |
| `exercises/chin-nod.md` | included |
| `exercises/dead-bug.md` | included |
| `exercises/glute-bridge.md` | included |
| `exercises/hip-hinge.md` | included |
| `exercises/incline-push-up.md` | included |
| `exercises/kneeling-hip-flexor-stretch.md` | included |
| `exercises/lat-pulldown.md` | included |
| `exercises/plank.md` | included |
| `exercises/prone-y-t.md` | included |
| `exercises/rowing-machine.md` | included |
| `exercises/seated-row.md` | included |
| `exercises/tai-chi-basics.md` | included |
| `exercises/thoracic-extension.md` | included |
| `exercises/wall-slide.md` | included |

Excluded document:

| Exercise document | M1 treatment |
|---|---|
| `exercises/baduanjin-basics.md` | excluded |

## Audit record fields

Each page-local audit for M2 and M3 must include:

| Field | Meaning |
|---|---|
| `initiative` | Must equal `top_five_generated_images_for_fewer_than_five_exercise_documents`. |
| `exercise_document` | One included exercise document path. |
| `current_image_count` | Current Markdown image reference count before the page batch changes. |
| `accepted_existing_image_count` | Existing accepted image count that contributes to the five-total target. |
| `accepted_older_sequence_image_count` | Existing accepted sequence image count, when present. |
| `new_generated_image_need` | `max(0, 5 - accepted_existing_image_count)`. |
| `existing_image_purposes` | Accepted purposes already represented by preserved images. |
| `existing_image_decisions` | Preserve, replace, or normalize decisions for existing images. |
| `candidate_table` | Page-specific ranked candidates, normally ranks 1-10. |
| `top_five_generation_target` | Candidate ranks selected for preservation or generation until the page reaches five total accepted images. |
| `coverage_limit_outcome` | The target total and rationale when fewer than five useful image purposes exist. |
| `generation_decision` | Selected count, decision, rationale, and selected purposes. |
| `validation_expectations` | Commands or checks expected for the page batch. |
| `rollback_path` | Paths or edits that can be removed while keeping the page readable. |

## Per-rank scoring matrix

Each candidate rank uses these 1-5 scores:

| Score field | Score meaning |
|---|---|
| `beginner_comprehension` | Helps a beginner understand the page without replacing Markdown. |
| `safety_setup_value` | Helps setup, positioning, or boundaries described by the page. |
| `muscle_attention_value` | Helps one allowed broad muscle-attention purpose when not already present. |
| `page_value` | Supports a concrete page section and avoids duplicate coverage. |
| `readiness` | Has enough source support, prompt readiness, and rollback clarity to implement. |

The candidate `score` must equal the sum of these five fields.
Ranks 1-5 may use `generate_now` or `first_generation_candidate` only for this named initiative.
Rank 6 or later must not generate unless later approved page-specific authorization exists.

## Validation behavior

M1 implemented deterministic validation for:

| Behavior | Validation surface |
|---|---|
| Exact named population and Baduanjin exclusion | `validate_named_top_five_population` |
| Five-total image need | `top_five_image_need` and `validate_audit_record` |
| Existing image and older sequence image counting | `validate_audit_record` |
| Top-five generation dispositions for ranks 1-5 | `validate_candidate_table` |
| Sixth-image rejection | `validate_candidate_table` and exercise image summary checks |
| Duplicate muscle-attention rejection | `validate_generation_decision` and exercise image summary checks |
| Blank provenance `human_reviewer` only for named pages | `validate_raster_provenance` |
| Blank prompt-record reviewer only for named pages | `validate_prompt_record` |
| Prompt-record, provenance, page reference, status, and media-purpose requirements retained | `check_markdown_first.py` tests |
| Repository-local visual review evidence not required for this named initiative | `validate_closeout_proof` |

## Unaffected surfaces

These surfaces are unchanged in M1:

| Surface | Rationale |
|---|---|
| Exercise Markdown pages | M1 establishes validation before M2-M3 page media batches. |
| Generated raster assets | M1 does not generate images. |
| Prompt records and `media/PROVENANCE.md` rows | M1 validates the contract before new rows are added. |
| `exercises/baduanjin-basics.md` | Explicitly excluded from this initiative. |

## Sources

- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md`
- `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
