# Explain Change: Exercise Image Standard and Optimization

## Current milestone

M3 implements the First New Exercise Image Batch milestone. It adds one
generated movement illustration to each of the five forward-head support
exercise pages, with provenance rows and change-local review evidence.

M3 does not change existing exercise images or migrate legacy media purposes.
It uses new `exercise_movement_illustration` rows only for the new generated
assets.

M1 remains the implemented checker contract underneath this guidance.
M2 remains the implemented authoring guidance and evidence surface underneath
this batch.

## Why the checker changed

The accepted spec adds three exercise-document image purposes:

- `exercise_setup_illustration`
- `exercise_movement_illustration`
- `exercise_muscle_attention_illustration`

The checker now accepts those purposes for full exercise pages while continuing
to accept the legacy-compatible `equipment_identification` and
`key_movement_illustration` purposes. It rejects out-of-context purposes on
exercise pages so pattern, condition, preview, vague, or unknown media purposes
do not become exercise-document image metadata.

M1 also adds deterministic checks for the parts of the standard that automation
can prove:

- no more than three exercise images per page;
- no more than one muscle-attention image per page;
- non-generic alt text for exercise images;
- generated raster exercise images live under `media/exercises/<slug>/`;
- generated raster exercise images have approved provenance rows;
- provenance `page_refs` include the referencing exercise page;
- exercise-image provenance uses an accountable human reviewer rather than an
  AI-tool placeholder;
- deterministic unsafe wording in exercise-image alt text and provenance notes
  is rejected.

## Why template handling changed

Test-spec review found that planned template validation could not rely on the
existing product-page checker behavior. M1 therefore adds a template path
boundary for `docs/templates/`: templates can contain placeholders and
template-language examples without being treated as promoted product content,
but image references inside templates still go through media-contract
validation.

This supports the planned M2 template guidance without weakening media checks.

## Tests added

`tests/test_exercise_image_standard.py` provides isolated temporary-repository
fixtures for the M1 contract. The tests cover text-only pages, new and rejected
purposes, provenance failures, count limits, path and alt-text boundaries,
legacy-purpose compatibility, and template-aware validation.

`tests/test_markdown_first_templates.py` now proves that the exercise template
contains optional exercise-image guidance and that the visual-safety and
beginner-comprehension evidence templates exist with the required review
prompts.

The M3 addition to `tests/test_exercise_image_standard.py` proves that the five
target pages reference the expected movement images, that each asset exists,
that each asset has exactly one approved `exercise_movement_illustration`
provenance row with the referencing page in `page_refs`, and that the M3
visual-safety and beginner-comprehension evidence files exist.

## Why the M2 guidance changed

The exercise-card template now includes an optional exercise-image block that
keeps images support-only. It tells authors to use images only when they add
beginner comprehension, choose one teaching purpose, keep explanation and
citations in Markdown, and avoid in-image labels, warning badges, pain marks,
or diagnosis/treatment claims.

The new visual-safety review template records the review scope, reviewer role
or handle, pass/fail criteria, decision, and residual risk for generated image
batches. The beginner-comprehension template records non-identifying outcomes
for purpose, setup or body position, movement steps, what to notice or feel,
stop condition, source verification, and residual confusion.

## Why the M3 image batch changed

M3 adds one movement image per target page instead of multiple images. This
keeps the first generated batch small while addressing the common beginner
comprehension gap: seeing the start-to-finish movement shape.

Each page keeps the written setup, movement steps, feel cues, safety notes, and
sources in Markdown. The added sentence near each image tells readers to treat
the image as a simple movement reference and keep following the written setup
and safety notes.

The new assets are:

- `media/exercises/chin-nod/movement.png`
- `media/exercises/thoracic-extension/movement.png`
- `media/exercises/wall-slide/movement.png`
- `media/exercises/prone-y-t/movement.png`
- `media/exercises/band-pull-apart/movement.png`

## Validation

- `python3 -m unittest tests.test_exercise_image_standard` failed before
  implementation with expected missing M1 behavior.
- `python3 -m unittest tests.test_exercise_image_standard` passed after
  implementation.
- `python3 -m unittest tests.test_markdown_first_guardrails tests.test_responsible_breadth_m1 tests.test_exercise_image_standard`
  passed after implementation.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed after implementation.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates media/PROVENANCE.md`
  passed after implementation.
- `python3 -m unittest discover tests` passed after implementation.
- `git diff --check` passed after implementation.
- The broad planned privacy command failed on pre-existing command examples in
  the superseded content-schema plan; the scoped current-change privacy command
  passed across the active exercise-image artifacts and code paths.
- `python3 -m unittest tests.test_markdown_first_templates` failed before M2
  documentation changes with the expected missing optional exercise-image
  guidance and evidence templates.
- `python3 -m unittest tests.test_markdown_first_templates` passed after M2
  implementation.
- `python3 -m unittest tests.test_markdown_first_templates tests.test_exercise_image_standard`
  passed after M2 implementation.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates media/PROVENANCE.md`
  passed after M2 implementation.
- `python3 tools/checks/check_privacy.py -- docs/templates docs/changes/exercise-image-standard-and-optimization`
  passed after M2 implementation.
- `git diff --check` passed after M2 implementation.
- `python3 -m unittest tests.test_exercise_image_standard` failed before M3
  content changes with expected missing target page image references, assets,
  provenance rows, and evidence files.
- `python3 -m unittest tests.test_exercise_image_standard` passed after M3
  implementation.
- `python3 -m unittest discover tests` passed after M3 implementation.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed after M3 implementation.
- `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md docs/changes/exercise-image-standard-and-optimization exercises media/PROVENANCE.md`
  passed after M3 implementation.
- `git diff --check` passed after M3 implementation.

## Remaining work

M3 is ready for code-review. M4 still owns the remaining exercise audit, and
lifecycle closeout still owns final explain-change, verification, and PR
handoff.
