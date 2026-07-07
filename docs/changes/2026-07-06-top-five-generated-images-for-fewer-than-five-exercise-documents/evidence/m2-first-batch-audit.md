# M2 First Batch Audit

Date: 2026-07-06

## Batch selection

M2 implements `exercises/band-pull-apart.md` and `exercises/bird-dog.md`.
This pairs one page with existing modern exercise images and one page with an accepted older sequence image.

## Page outcomes

| Exercise document | Existing accepted images | New promoted images | Total promoted images | Outcome |
|---|---:|---:|---:|---|
| `exercises/band-pull-apart.md` | 2 | 2 | 4 | Coverage-limit outcome: the fifth generated candidate duplicated the existing movement reference, so it was not promoted. |
| `exercises/bird-dog.md` | 1 | 4 | 5 | Reaches the named top-five target with setup, movement, shorter-reach, and muscle-attention support. |

## Candidate scoring matrix

Scores use 1-5 values for `beginner_comprehension`, `setup_value`, `muscle_attention_value`, `page_value`, and `readiness`.
Disposition values follow the M1 audit framework.

### `exercises/band-pull-apart.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `muscle-attention.png` | 5 | 1 | 5 | 5 | 5 | existing_accepted | Broad upper-back and rear-shoulder reference already supports the muscle section. |
| 2 | Existing `movement.png` | 5 | 2 | 1 | 5 | 5 | existing_accepted | Two-panel start and finish reference already supports the movement section. |
| 3 | New `setup.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Adds distinct setup coverage for band slack, stance, and chest-height start. |
| 4 | New `quiet-ribs-neck.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Adds posture-control coverage for neck, ribs, and arm height without duplicating muscle attention. |
| 5 | Generated chest-height path candidate | 3 | 2 | 1 | 2 | 3 | rejected_duplicate_coverage | Too close to the existing movement reference after visual inspection. |
| 6 | Grip-width close-up | 3 | 3 | 1 | 2 | 2 | defer | Could be useful later but is not needed for the same page section in this batch. |
| 7 | Easier lighter-band variation | 3 | 2 | 1 | 2 | 2 | defer | The written easier-version note is sufficient for now. |
| 8 | Return-control view | 3 | 1 | 1 | 2 | 2 | defer | Movement reference already covers the return concept indirectly. |
| 9 | Side-view rib position | 3 | 2 | 1 | 2 | 2 | defer | Would compete with the promoted posture-control image. |
| 10 | Equipment-only band image | 1 | 2 | 1 | 1 | 2 | reject | Equipment is simple enough in Markdown and setup image. |

### `exercises/bird-dog.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `bird-dog-sequence.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Sequence image already covers setup, reach, and a common form reference. |
| 2 | New `setup.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Adds a larger standalone setup reference. |
| 3 | New `level-pelvis-reach.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Adds a larger standalone controlled reach reference. |
| 4 | New `short-reach.png` | 5 | 3 | 1 | 5 | 5 | generate_now | Supports the written shorter-reach cue. |
| 5 | New `muscle-attention.png` | 5 | 1 | 5 | 5 | 5 | generate_now | Adds the only muscle-attention image for the page. |
| 6 | Hands-and-knees side close-up | 3 | 3 | 1 | 2 | 2 | defer | Standalone setup image provides enough setup value. |
| 7 | Knee-only support detail | 1 | 2 | 1 | 1 | 2 | reject | Too narrow for beginner comprehension. |
| 8 | Slow-return frame | 3 | 1 | 1 | 2 | 2 | defer | Movement text already covers the return. |
| 9 | Side-switching view | 3 | 1 | 1 | 2 | 2 | defer | Mirror-side detail is not necessary for this page. |
| 10 | Mat-only setup cue | 1 | 2 | 1 | 1 | 2 | reject | Equipment is simple enough in Markdown. |

## Visual and contract evidence

| Asset | Page section | Evidence |
|---|---|---|
| `media/exercises/band-pull-apart/setup.png` | Equipment setup | No embedded writing, no brand marks, faceless figure, clear band setup. |
| `media/exercises/band-pull-apart/quiet-ribs-neck.png` | What you should feel | No embedded writing, no brand marks, faceless figure, distinct posture-control purpose. |
| `media/exercises/bird-dog/setup.png` | Equipment and setup | No embedded writing, no brand marks, faceless figure, clear hands-and-knees setup. |
| `media/exercises/bird-dog/level-pelvis-reach.png` | Movement phases | No embedded writing, no brand marks, faceless figure, clear opposite arm and leg reach. |
| `media/exercises/bird-dog/short-reach.png` | Important notes | No embedded writing, no brand marks, faceless figure, visibly smaller controlled reach with bent reaching limbs. |
| `media/exercises/bird-dog/muscle-attention.png` | Used muscles | No embedded writing, no brand marks, faceless figure, broad attention regions only. |

## Rollback proof

Each promoted image is independently removable by deleting its page image reference, generated asset, prompt record, and `media/PROVENANCE.md` row.
The band pull-apart fifth candidate was not promoted, and the repo copy was removed before validation.

## Validation

M2 validation commands are recorded in the plan after local execution.

## Sources

- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/m1-audit-framework.md`
- `exercises/band-pull-apart.md`
- `exercises/bird-dog.md`
- `media/PROVENANCE.md`
