# Explain Change: Necessary Images and Baduanjin Exercise

## Status

Implementation rationale through M3; code-review pending for M3.

## M1 Changes

The checker now keeps the default exercise-image limit at three and applies a path-scoped five-image exception only to `exercises/baduanjin-basics.md`.
This implements the approved sequence-based exception without broadening image capacity for other exercise pages.

`tests/test_exercise_image_standard.py` now includes temporary Baduanjin fixtures for the planned five-image batch, sixth-image rejection, second muscle-attention rejection, prompt-record failure, visual-semantic failure, and unchanged default behavior for unrelated pages.
These tests prove the media contract before real Baduanjin assets exist.

`tests/test_exercise_method_guidance.py` now includes Baduanjin-shaped `low_load_control_drill` fixtures.
The passing fixture keeps the method static and general; the failing fixture rejects adaptive, recovery-care, treatment, symptom-based, and medication-response wording.

`image-candidate-pool.md` records the ranked top-10 image candidate pool as change-local evidence.
It identifies the exact first five asset paths and records candidates 6-10 as deferred alternatives rather than permission to publish more images.

## Unaffected Surfaces

Beginner-comprehension proof and rollback proof are intentionally unchanged through M3.
They belong to M4 after the governed image batch is reviewed.

## M2 Changes

`exercises/baduanjin-basics.md` adds the text-only Baduanjin Basics page with the required title, alias line, sections, beginner movement breakdown, source-backed setup and safety guidance, `low_load_control_drill` method labels, and broad role-based muscle guidance.

`docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/source-audit.md` records sampled source support for setup, safety, method, movement, muscle, feel, and pause-condition claims.

`tests/test_markdown_first_real_pages.py` adds real-page tests for Baduanjin page shape, scope boundaries, setup and safety sources, method guidance, broad muscle guidance, and M2 source-audit evidence.

`docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` now lists `exercises/baduanjin-basics.md` as a text-only page so the exercise-image inventory remains current after adding the new exercise page.

## M3 Changes

`exercises/baduanjin-basics.md` now references exactly five first-batch support images: setup, two-hands-lift, drawing-bow, alternating-reach, and muscle-attention.
The page keeps the written Markdown as source of truth and introduces the images as broad visual references.

`media/exercises/baduanjin-basics/` now contains the five generated raster assets selected by the approved candidate pool.

`media/prompts/exercises/baduanjin-basics/` now contains one exact prompt record per generated raster asset.
Each prompt record names the asset path, generator, creation date, human reviewer, approval status, exact prompt, and selected-output notes.

`media/PROVENANCE.md` now has approved rows for the five Baduanjin assets with local prompt-record paths, expected exercise image purposes, and `exercises/baduanjin-basics.md` page refs.

`docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/visual-safety-review.md` records manual visual review evidence for the five selected images.

`tests/test_markdown_first_real_pages.py` now proves the real Baduanjin page uses exactly five local, prompt-backed, approved generated raster images with meaningful alt text.

`docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` now lists `exercises/baduanjin-basics.md` as a five-image page with governed first-batch images.

## Sources

- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
