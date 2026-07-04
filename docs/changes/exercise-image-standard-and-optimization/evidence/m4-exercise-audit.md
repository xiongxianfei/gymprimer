# M4 Exercise Image Audit

Audit date: 2026-07-03

Auditor: xiongxianfei

Scope: all current `exercises/*.md` pages.

## Decision

M4 does not change exercise pages, image assets, media-purpose values, or
provenance rows. Existing generated raster exercise images remain in place.
Legacy-compatible `equipment_identification` and `key_movement_illustration`
rows are not migrated solely for the exercise-image standard.

No current exercise page needs an immediate additional image batch. Future
image work should happen only as a reviewed follow-up loop when reader feedback
or page review identifies a concrete beginner comprehension gap.

## Audit Table

| Exercise page | Current image count | Current image purposes | M4 category | Follow-up routing |
| --- | ---: | --- | --- | --- |
| `exercises/band-pull-apart.md` | 2 | `exercise_muscle_attention_illustration`, `exercise_movement_illustration` | keep existing image | No additional image needed now; keep prompt-backed M3 images. |
| `exercises/bird-dog.md` | 1 | `key_movement_illustration` | keep existing image | Keep legacy-compatible sequence image; no migration-only edit. |
| `exercises/chest-press.md` | 1 | `equipment_identification` | keep existing image | Keep legacy-compatible machine image; future setup/movement work needs a reviewed batch. |
| `exercises/chin-nod.md` | 2 | `exercise_muscle_attention_illustration`, `exercise_movement_illustration` | keep existing image | No additional image needed now; keep M3 images. |
| `exercises/dead-bug.md` | 1 | `key_movement_illustration` | keep existing image | Keep legacy-compatible sequence image; no migration-only edit. |
| `exercises/glute-bridge.md` | 1 | `key_movement_illustration` | keep existing image | Keep legacy-compatible sequence image; no migration-only edit. |
| `exercises/hip-hinge.md` | 1 | `key_movement_illustration` | keep existing image | Keep legacy-compatible sequence image; no migration-only edit. |
| `exercises/incline-push-up.md` | 1 | `key_movement_illustration` | keep existing image | Keep legacy-compatible movement image; no migration-only edit. |
| `exercises/kneeling-hip-flexor-stretch.md` | 1 | `key_movement_illustration` | keep existing image | Keep legacy-compatible sequence image; no migration-only edit. |
| `exercises/lat-pulldown.md` | 2 | `equipment_identification`, `key_movement_illustration` | keep existing image | Keep legacy-compatible equipment and movement images; no migration-only edit. |
| `exercises/plank.md` | 1 | `key_movement_illustration` | keep existing image | Keep legacy-compatible sequence image; no migration-only edit. |
| `exercises/prone-y-t.md` | 2 | `exercise_muscle_attention_illustration`, `exercise_movement_illustration` | keep existing image | No additional image needed now; keep M3 images. |
| `exercises/rowing-machine.md` | 3 | `exercise_setup_illustration`, `exercise_muscle_attention_illustration`, `exercise_movement_illustration` | follow-up images added | Follow-up rowing media enhancement added setup, muscle-attention, and movement images with provenance, prompt records, and visual-safety review. |
| `exercises/seated-row.md` | 1 | `equipment_identification` | keep existing image | Keep legacy-compatible machine image; future setup/movement work needs a reviewed batch. |
| `exercises/thoracic-extension.md` | 2 | `exercise_muscle_attention_illustration`, `exercise_movement_illustration` | keep existing image | No additional image needed now; keep M3 images. |
| `exercises/wall-slide.md` | 2 | `exercise_muscle_attention_illustration`, `exercise_movement_illustration` | keep existing image | No additional image needed now; keep M3 images. |

## Follow-up Rules

- Do not create a new proposal for a small future exercise-image batch that
  remains within full exercise-document images and the accepted image standard.
- Do create or amend upstream artifacts if future work expands into pattern,
  condition, video, animation, hosted delivery, user-submitted media, or
  personalized coaching.
- Do not edit an exercise page solely to migrate an existing
  `equipment_identification` or `key_movement_illustration` image purpose.
- Future image batches should name the concrete comprehension gap before
  generating assets.

## Validation Note

This audit is a routing artifact, not a generated public index. It records the
current page inventory and does not authorize immediate image generation.
