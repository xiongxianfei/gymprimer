# M3A Prompt Record Backfill

Date: 2026-07-03

## Scope

This record covers M3A prompt-record backfill for the in-flight M3 generated raster exercise images:

- `media/exercises/chin-nod/movement.png`
- `media/exercises/chin-nod/muscle-attention.png`
- `media/exercises/thoracic-extension/movement.png`
- `media/exercises/thoracic-extension/muscle-attention.png`
- `media/exercises/wall-slide/movement.png`
- `media/exercises/wall-slide/muscle-attention.png`
- `media/exercises/prone-y-t/movement.png`
- `media/exercises/prone-y-t/muscle-attention.png`
- `media/exercises/band-pull-apart/movement.png`
- `media/exercises/band-pull-apart/muscle-attention.png`

## Finding

Exact full generation prompts for these already-generated M3 images were not present in repository-local evidence. The repository had only concise prompt summaries in `media/PROVENANCE.md` and review notes in change evidence.

Because exact prompts were not recoverable from durable evidence, M3A did not invent prompt text and did not create synthetic prompt records for these assets.

After CR-EIS-M3-2 owner clarity feedback, five assets were replaced with newly
generated images whose exact prompts are preserved in repository-local prompt
records. Those replacement assets are no longer on the pre-amendment
compatibility path.

## Available prompt summaries

These are the repository-local prompt summaries already preserved in `media/PROVENANCE.md`. They are useful review context, but they are not exact full prompt records and do not satisfy the future `prompt_record` requirement.

| Asset | Available prompt summary |
|---|---|
| `media/exercises/chin-nod/movement.png` | Superseded by CR-EIS-M3-2 replacement; exact prompt now recorded at `media/prompts/exercises/chin-nod/movement.md`. |
| `media/exercises/chin-nod/muscle-attention.png` | Neutral front-neck attention reference for chin nod with subtle blue broad-region highlight and no embedded writing, logos, or identifying features |
| `media/exercises/thoracic-extension/movement.png` | Superseded by CR-EIS-M3-2 replacement; exact prompt now recorded at `media/prompts/exercises/thoracic-extension/movement.md`. |
| `media/exercises/thoracic-extension/muscle-attention.png` | Neutral upper-back attention reference for thoracic extension with subtle blue broad-region highlight and no embedded writing, logos, or identifying features |
| `media/exercises/wall-slide/movement.png` | Two-panel neutral movement reference for forearms-on-wall wall slide, showing lower and raised arm positions against a plain wall with no embedded writing, logos, or identifying features |
| `media/exercises/wall-slide/muscle-attention.png` | Neutral shoulder-blade and side-rib attention reference for wall slide with subtle blue broad-region highlight and no embedded writing, logos, or identifying features |
| `media/exercises/prone-y-t/movement.png` | Superseded by CR-EIS-M3-2 replacement; exact prompt now recorded at `media/prompts/exercises/prone-y-t/movement.md`. |
| `media/exercises/prone-y-t/muscle-attention.png` | Neutral upper-back and shoulder-blade attention reference for prone Y and T with subtle blue broad-region highlight and no embedded writing, logos, or identifying features |
| `media/exercises/band-pull-apart/movement.png` | Superseded by CR-EIS-M3-2 replacement; exact prompt now recorded at `media/prompts/exercises/band-pull-apart/movement.md`. |
| `media/exercises/band-pull-apart/muscle-attention.png` | Superseded by CR-EIS-M3-2 replacement; exact prompt now recorded at `media/prompts/exercises/band-pull-apart/muscle-attention.md`. |

## Compatibility decision

The five unreplaced M3 rows in `media/PROVENANCE.md` keep a blank
`prompt_record` value and record this exact limitation in `notes`:

```text
M3 pre-amendment prompt unavailable; compatibility limitation recorded
```

This is the explicit pre-amendment compatibility path allowed by the approved M3A plan and proof map. It is not a precedent for future generated raster exercise images. The compatibility path currently applies only to:

- `media/exercises/chin-nod/muscle-attention.png`
- `media/exercises/thoracic-extension/muscle-attention.png`
- `media/exercises/wall-slide/movement.png`
- `media/exercises/wall-slide/muscle-attention.png`
- `media/exercises/prone-y-t/muscle-attention.png`

The CR-EIS-M3-2 replacement assets must satisfy normal prompt-record
validation.

## Future requirement

Future governed generated raster exercise images must preserve the exact full prompt in a repository-local prompt record under:

```text
media/prompts/exercises/<exercise-slug>/<asset-stem>.md
```

The `media/PROVENANCE.md` row must link that file through `prompt_record`, and the prompt record must point back to the exact same `asset_path`.
