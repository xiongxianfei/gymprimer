# Media Decision: Rowing Machine Basics and Beginner Workout Guidance

## Status

text-only accepted

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

Do not add rowing-machine images in this slice.

The source audit passes after adding the page-local Concept2 muscles source, and
the beginner comprehension proof passes for rower purpose, foot strap position,
drive sequence, recovery sequence, beginner first step, stop condition, and
technique-source verification. No unresolved comprehension gap requires a setup
or stroke-sequence image.

## Media Compliance Impact

- No files are added under `media/exercises/rowing-machine/`.
- No generated raster image is added.
- No `media/PROVENANCE.md` row is required.
- No prompt record under `media/prompts/exercises/rowing-machine/` is required.
- No rowing visual-safety review file is required for M3 because no media is
  referenced.

## Re-Run Trigger

Re-run this decision after substantive text changes that affect comprehension,
after beginner-comprehension evidence changes, or before adding/removing
rowing-machine media.
