# Explain Change: Necessary Images and Baduanjin Exercise

## Status

Implementation rationale for M1; code-review pending.

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

Generated media assets, prompt records, provenance rows, visual-safety review, beginner-comprehension proof, and rollback proof are intentionally unchanged through M2.
They belong to M3-M4 after the text-only page is reviewed.

## M2 Changes

`exercises/baduanjin-basics.md` adds the text-only Baduanjin Basics page with the required title, alias line, sections, beginner movement breakdown, source-backed setup and safety guidance, `low_load_control_drill` method labels, and broad role-based muscle guidance.

`docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/source-audit.md` records sampled source support for setup, safety, method, movement, muscle, feel, and pause-condition claims.

`tests/test_markdown_first_real_pages.py` adds real-page tests for Baduanjin page shape, scope boundaries, setup and safety sources, method guidance, broad muscle guidance, and M2 source-audit evidence.

`docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` now lists `exercises/baduanjin-basics.md` as a text-only page so the exercise-image inventory remains current after adding the new exercise page.

## Sources

- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
