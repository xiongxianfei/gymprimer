# Explain Change: Exercise Image Standard and Optimization

## Summary

This change implements the accepted Exercise Image Standard through four
reviewed milestones plus the M3A prompt-record amendment. It adds static
validation for exercise-image purposes, authoring guidance, a reviewed first
exercise-image batch, exact prompt-record support for generated raster
exercise images, and a remaining-page audit that avoids migration-only churn.

The repository remains Markdown-first. Images are support assets; Markdown
continues to carry setup, movement instructions, muscle wording, safety notes,
and citations.

## Problem

Exercise pages had inconsistent visual support and no durable way to distinguish
setup, movement, and muscle-attention images. The project also needed a
traceable provenance and prompt-record contract for generated raster exercise
images before adding more assets.

## Decision Trail

The accepted proposal chose one coherent exercise-image standard implemented
through small loops instead of separate proposals per image type or one broad
all-page rewrite.

The approved spec defines the observable contract:

- R1-R6 keep images optional and minimum-necessary.
- R7-R11 define setup, movement, and muscle-attention purposes.
- R12-R14, R28-R31 preserve visual-safety and beginner-comprehension review.
- R15-R24 define local paths, provenance, reviewer, and prompt-record rules.
- R32-R33 preserve existing legacy-compatible images without migration.
- R37-R38 preserve no-private-data and no-runtime boundaries.

Architecture and ADR updates keep generated raster media under the
Markdown-first media system, with `media/PROVENANCE.md` as the central
provenance index and repository-local prompt records under
`media/prompts/exercises/<slug>/<asset-stem>.md`.

## Diff Rationale

| Area | Change | Reason | Evidence |
| --- | --- | --- | --- |
| Checker | `tools/checks/check_markdown_first.py` now validates exercise image purposes, image counts, muscle-attention limits, alt text, generated-raster provenance, prompt records, and scoped M3 compatibility. | Implements the accepted exercise-image and prompt-record contracts without making images mandatory. | M1, M3A, and focused checker tests. |
| Tests | `tests/test_exercise_image_standard.py` covers text-only pages, purpose routing, provenance failures, prompt-record failures, M3 batch assets, compatibility scope, and M4 audit coverage. | Proves deterministic behavior and prevents regression in scoped compatibility and audit coverage. | 13 focused tests now pass. |
| Templates | `docs/templates/exercise-card.md` and evidence templates guide optional image use and review evidence. | Keeps authoring Markdown-first and support-only. | M2 review closed cleanly. |
| Exercise pages | Five forward-head support exercise pages now reference movement and muscle-attention images. | Adds the first reviewed image batch for beginner comprehension. | M3 visual-safety evidence and code-review R2. |
| Media assets | New/replaced PNGs live under `media/exercises/<slug>/`. | Keeps exercise media subject-co-located and repository-local. | Markdown checker and provenance rows pass. |
| Provenance | `media/PROVENANCE.md` includes `prompt_record` and exact rows for generated exercise images. | Makes generated raster assets traceable and reviewable. | M3A prompt-record tests and review. |
| Prompt records | Five replacement assets have exact full prompt records under `media/prompts/exercises/`. | Preserves prompts for newly generated replacement assets instead of relying on summaries. | Prompt-record validation passes. |
| Evidence | M3 visual-safety, beginner-comprehension, prompt backfill, and M4 audit evidence are recorded under the change directory. | Covers manual proof that static checks cannot prove. | Code-review M3/M3A/M4 records. |
| Lifecycle artifacts | Plan, plan index, change metadata, review log, and review-resolution were kept current through each gate. | Prevents workflow drift and preserves source-order traceability. | M3A R3 and M4 R1 closed cleanly. |

## Tests Added or Changed

- `test_text_only_exercise_page_passes_image_specific_checks`: proves images
  remain optional.
- Purpose and provenance tests: prove allowed purposes pass and wrong purposes,
  bad provenance, generic alt text, unsafe wording, bad paths, and excessive
  image counts fail.
- Prompt-record tests: prove missing, invalid, mismatched, or incomplete prompt
  records fail; explicit redaction can pass; M3 compatibility is scoped.
- M3 batch test: proves target pages reference expected assets with approved
  provenance and prompt records where required.
- M4 audit test: proves every current `exercises/*.md` page appears in the
  audit and migration-only edits remain prohibited.

## Validation Evidence Before Final Verify

Recent milestone and review validation includes:

- `python3 -m unittest tests.test_exercise_image_standard` passed with 13
  tests after M4 and during M4 review.
- `python3 -m unittest discover tests` passed with 102 tests after M4.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`
  passed after M4.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed during M3/M3A review.
- Scoped privacy checks over the current change artifacts passed.
- `git diff --check` and `git diff --check HEAD` passed in the recorded
  milestone and review evidence.

CI has not been observed, so this artifact does not claim CI passed.

## Review Resolution Summary

Material findings were resolved and re-reviewed:

- `CR-EIS-M1-1`: broad privacy validation ownership moved to verify after
  owner direction and test-spec review.
- `CR-EIS-M3-1`: wall-slide visual mismatch resolved by replacement and
  visual-safety re-review.
- `CR-EIS-M3-2`: reader-prompt evidence and post-replacement clarity
  confirmation recorded; M3 R2 accepted the resolution with scope noted.
- `CR-EIS-M3A-1`: prompt-record compatibility bypass scoped to recorded M3
  assets with regression coverage.
- `CR-EIS-M3A-2`: milestone state drift fixed; M3A R3 closed the milestone.

See `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
and `docs/changes/exercise-image-standard-and-optimization/review-log.md`.

## Alternatives Rejected

- Generating all images before validation was rejected because provenance,
  prompt records, and review rules needed to exist first.
- Migrating existing `equipment_identification` and
  `key_movement_illustration` images was rejected as low-value churn.
- Keeping all exercise pages text-only was rejected by the accepted proposal
  because images can help beginner comprehension when governed.
- Creating a new proposal for each small future exercise-image batch was
  rejected; small batches remain follow-up loops under the accepted standard.

## Scope Control

This change does not add a runtime app, CMS, database, hosted image delivery,
generated public JSON, user-input flow, video, animation, stock-photo library,
personalized coaching, clinical diagnosis, treatment plan, or README promotion.

No exercise page was edited solely to migrate a legacy image purpose.

## Risks and Follow-ups

Final verification still needs to run, including the broad privacy command
owned by lifecycle closeout / verify. PR readiness is not claimed here.

Future exercise-image batches should name a concrete comprehension gap,
preserve exact prompts, update provenance, and use the same visual-safety and
reader-evidence process before code review.
