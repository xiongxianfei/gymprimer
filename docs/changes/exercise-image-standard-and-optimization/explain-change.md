# Explain Change: Exercise Image Standard and Optimization

## Current milestone

M1 implements the Exercise Image Validation Contract. It changes automated
validation and focused tests only. It does not change existing exercise images,
generate new images, migrate legacy media purposes, or edit exercise-page image
references.

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

## Remaining work

M1 is ready for code-review. M2 still owns authoring-template guidance and
review-evidence surfaces. M3 and later milestones own generated image batches
and manual visual-safety evidence.
