# Required Image Decision

## Decision

decision: required-images-approved

The media-bearing walking slice adds exactly two generated raster support images to `exercises/brisk-walking.md`:

- `media/exercises/brisk-walking/movement.png` with `exercise_movement_illustration`;
- `media/exercises/brisk-walking/muscle-attention.png` with `exercise_muscle_attention_illustration`.

`principles/everyday-walking.md` remains text-only.

## Scope

Pages covered:

- `exercises/brisk-walking.md`
- `principles/everyday-walking.md`

## Rationale

The amended proposal and approved spec require one movement image and one muscle-attention image for the brisk walking exercise document.

The movement image supports posture, arm swing, and heel-to-toe stride comprehension.

The muscle-attention image supports broad body-region awareness for the `## Muscles involved` section.

Both images are support-only.
The Markdown remains the source of truth for technique, effort, progression, safety, muscle wording, and citations.

## Accepted Assets

| Asset path | Media purpose | Prompt record | Page reference | Decision |
| --- | --- | --- | --- | --- |
| `media/exercises/brisk-walking/movement.png` | `exercise_movement_illustration` | `media/prompts/exercises/brisk-walking/movement.md` | `exercises/brisk-walking.md` | approved |
| `media/exercises/brisk-walking/muscle-attention.png` | `exercise_muscle_attention_illustration` | `media/prompts/exercises/brisk-walking/muscle-attention.md` | `exercises/brisk-walking.md` | approved |

## Provenance

Both assets have approved `media/PROVENANCE.md` rows with:

- `asset_type = ai_generated_raster`;
- local asset paths;
- exact prompt-record paths;
- `source_inputs = none`;
- `review_status = approved`;
- `page_refs` containing `exercises/brisk-walking.md`.

## Residual Risk

residual risk: generated images can only provide broad visual support.
They do not prove exact technique, exact muscle activation, safety, or personalized walking readiness.
Those claims remain in Markdown and page-local sources.
