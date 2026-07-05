# Muscle Image Alignment

## Scope

- Change ID: `exercise-muscle-guidance-standard`
- Milestone: M3
- Proof ID: XMG-M3
- Pages checked: proof-slice pages that include `exercise_muscle_attention_illustration` images.
- Criteria: compare image path, purpose, alt text, nearby Markdown, page-local citations, and provenance for broad-region support-only alignment.
- Check date: 2026-07-04
- Privacy statement: no private reader data, private health information, faces, identifying details, or secrets were recorded.

## Result

Pass for M3 implementation handoff.

Every proof-slice muscle-attention image is optional support media, has Markdown alt text, has an approved `media/PROVENANCE.md` row, and is subordinate to nearby `## Muscles involved` and `## What you should feel` text.

## Alignment Checks

| Image path | Page | nearby Markdown | alt text | provenance | broad region | no in-image labels | no red pain marks | no wrong/correct framing | no precise anatomy | no diagnosis or treatment | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `media/exercises/rowing-machine/muscle-attention.png` | `exercises/rowing-machine.md` | Phase table names legs/glutes, trunk, upper back/lats/arms, and recovery control. Feel cue names leg-driven push, steady trunk, and light upper-back/arm finish. | Broad highlights on legs, glutes, trunk, upper back, lats, and arms. | Approved row with `exercise_muscle_attention_illustration`, page ref, and prompt record. | pass | pass | pass | pass | pass | pass | pass |
| `media/exercises/chin-nod/muscle-attention.png` | `exercises/chin-nod.md` | Role bullets name front-of-neck control muscles and nearby support; feel cue stays light and soft. | Front-neck region subtly highlighted. | Approved row with `exercise_muscle_attention_illustration`; prompt-record compatibility limitation already recorded. | pass | pass | pass | pass | pass | pass | pass |
| `media/exercises/thoracic-extension/muscle-attention.png` | `exercises/thoracic-extension.md` | Role bullets distinguish upper-back mobility focus from trunk/neck support; feel cue names gentle upper-back movement. | Upper-back region subtly highlighted. | Approved row with `exercise_muscle_attention_illustration`; prompt-record compatibility limitation already recorded. | pass | pass | pass | pass | pass | pass | pass |
| `media/exercises/band-pull-apart/muscle-attention.png` | `exercises/band-pull-apart.md` | Role table names upper back/rear shoulders, shoulder-girdle/arms, and neck/ribs/trunk control; feel cue names upper-back/rear-shoulder region. | Upper-back and rear-shoulder region subtly highlighted. | Approved row with `exercise_muscle_attention_illustration`, page ref, and prompt record. | pass | pass | pass | pass | pass | pass | pass |

## Text-Only Proof-Slice Pages

Initial M3 proof recorded `exercises/chest-press.md` and `exercises/plank.md` as text-only compatible pages because muscle-attention images are optional. The post-PR follow-up now adds one support-only muscle-attention image to each page while keeping Markdown authoritative.

## Post-PR Follow-Up Image

| Image path | Page | nearby Markdown | alt text | provenance | broad region | no in-image labels | no red pain marks | no wrong/correct framing | no precise anatomy | no diagnosis or treatment | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `media/exercises/chest-press/muscle-attention.png` | `exercises/chest-press.md` | Role table names chest, triceps/front shoulders, and upper-back/shoulder-blade support. Feel cue names controlled push, arm support, low shoulders, and steady handles. | Broad highlights on chest, front shoulders, triceps, and upper-back support area. | Approved row with `exercise_muscle_attention_illustration`, page ref, and prompt record. | pass | pass | pass | pass | pass | pass | pass |
| `media/exercises/plank/muscle-attention.png` | `exercises/plank.md` | Role table names abdomen/side trunk, glutes/shoulders, legs, and upper back. Feel cue names steady abdomen/side-trunk effort and ribs/pelvis control. | Broad highlights on abdomen, side trunk, glutes, shoulders, upper back, and legs. | Approved row with `exercise_muscle_attention_illustration`, page ref, and prompt record. | pass | pass | pass | pass | pass | pass | pass |
| `media/exercises/seated-row/muscle-attention.png` | `exercises/seated-row.md` | Role table names upper back/lats, arms/grip, and trunk posture support. Feel cue names upper-back effort, arm support, and quiet torso. | Broad highlights on upper back, arms, grip, and trunk posture area. | Approved row with `exercise_muscle_attention_illustration`, page ref, and prompt record. | pass | pass | pass | pass | pass | pass | pass |

## Residual Risk

This review checks the repository-visible image references, alt text, provenance rows, and nearby Markdown. It does not re-render or regenerate images. Any future image edit, alt-text change, provenance change, or nearby muscle guidance change should rerun this alignment review.
