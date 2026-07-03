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

## Compatibility decision

Each affected M3 row in `media/PROVENANCE.md` keeps a blank `prompt_record` value and records this exact limitation in `notes`:

```text
M3 pre-amendment prompt unavailable; compatibility limitation recorded
```

This is the explicit pre-amendment compatibility path allowed by the approved M3A plan and proof map. It is not a precedent for future generated raster exercise images.

## Future requirement

Future governed generated raster exercise images must preserve the exact full prompt in a repository-local prompt record under:

```text
media/prompts/exercises/<exercise-slug>/<asset-stem>.md
```

The `media/PROVENANCE.md` row must link that file through `prompt_record`, and the prompt record must point back to the exact same `asset_path`.
