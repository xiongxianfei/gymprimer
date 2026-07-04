# Media Decision: Rowing Machine Basics and Beginner Workout Guidance

## Status

media added after follow-up readability request

## Scope

- Change ID: `rowing-machine-basics-and-beginner-workouts`
- Milestone: M3
- Proof ID: RMB-M3
- Audited page: `exercises/rowing-machine.md`
- Audit date: 2026-07-04
- Related proof:
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/source-audit.md`
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/beginner-comprehension.md`

## Decision

Original M3 decision: keep the first implementation text-only because the
source audit and beginner comprehension proof passed without an unresolved
visual comprehension gap.

The source audit passes after adding the page-local Concept2 muscles source, and
the beginner comprehension proof passes for rower purpose, foot strap position,
drive sequence, recovery sequence, beginner first step, stop condition, and
technique-source verification. No unresolved comprehension gap requires a setup
or stroke-sequence image.

Follow-up decision on 2026-07-04: add three support images after the user asked
for necessary images to make the document more readable and understandable,
then clarified that users need muscle engagement and targeting cues. The images
are limited to concepts already identified by the proposal and image guidance:

- setup reference for foot strap, seat, handle, and catch position;
- muscle-attention reference for broad muscles engaged during rowing;
- movement sequence reference for catch, drive, finish, and recovery.

The images support Markdown comprehension. They do not replace the written
setup, source citations, sequence, method guidance, or safety routing.

## Media Compliance Impact

- Added `media/exercises/rowing-machine/setup.png`.
- Added `media/exercises/rowing-machine/movement.png`.
- Added `media/exercises/rowing-machine/muscle-attention.png`.
- Added `media/PROVENANCE.md` rows for both generated raster images.
- Added prompt records under `media/prompts/exercises/rowing-machine/`.
- Added `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/visual-safety-review.md`.
- Updated `exercises/rowing-machine.md` with local image references and
  meaningful alt text.

## Re-Run Trigger

Re-run this decision after substantive text changes that affect comprehension,
after beginner-comprehension evidence changes, or before adding/removing
rowing-machine media.
