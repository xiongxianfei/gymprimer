# ADR 2026-07-03: Exercise Document Image Purposes

## Status

accepted

Amended by `docs/adr/2026-07-03-generated-raster-prompt-records.md` for exact
prompt-record links on generated raster exercise images.

## Context

The accepted Exercise Image Standard proposal and approved Exercise Image
Standard spec add a governed visual standard for full exercise documents.
Existing media architecture already classifies raster assets under `media/` by
extension before provenance lookup and requires exact approved rows in
`media/PROVENANCE.md`.

The current expanded media-purpose enum distinguishes equipment identification,
key movement, pattern alignment, anatomical-region context, and compact
exercise previews. That is not precise enough for full exercise documents,
where setup images, movement images, and muscle-attention images carry different
review risks and validation boundaries.

The new exercise-specific purposes must preserve Markdown as source of truth,
centralized provenance, deterministic raster classification, legacy exercise
image compatibility, and non-clinical visual safety.

## Decision

Keep the centralized `media/PROVENANCE.md` mechanism and extension-based raster
classification from ADR 2026-06-28.

For new generated raster images referenced from full exercise documents,
allowed `media_purpose` values are:

- `exercise_setup_illustration`
- `exercise_movement_illustration`
- `exercise_muscle_attention_illustration`

Purpose boundaries:

- `exercise_setup_illustration` is only for equipment setup, grip, stance,
  bench, wall, floor, or body relationship on an exercise document.
- `exercise_movement_illustration` is only for start position, end position,
  key position, or movement path on an exercise document.
- `exercise_muscle_attention_illustration` is only for one broad body or muscle
  region to notice on an exercise document.

Existing generated raster exercise images using `equipment_identification` or
`key_movement_illustration` remain valid without media-purpose migration when
their provenance rows are otherwise valid.

New generated raster exercise images live under
`media/exercises/<exercise-slug>/` and use the active provenance fields:
`asset_path`, `asset_type`, `media_purpose`, `generator`,
`prompt_or_creation_notes`, `created_date`, `human_reviewer`,
`license_assertion`, `source_inputs`, `review_status`, `page_refs`, and
`notes`.

Exercise images remain support assets. Markdown text, page-local citations, and
reviewed source lists remain the source of truth for setup, movement, muscles,
feel cues, mistakes, safety, diagnosis boundaries, treatment boundaries, and
programming boundaries.

## Alternatives considered

- Reuse only `key_movement_illustration`: rejected because setup, movement, and
  muscle-attention images have different teaching purposes and review risks.
- Migrate existing exercise images immediately: rejected because the accepted
  spec preserves existing `equipment_identification` and
  `key_movement_illustration` exercise images without media-purpose migration.
- Use a single broad `exercise_image` purpose: rejected because it would hide
  whether the image teaches setup, movement, or muscle attention.
- Put muscle labels, cues, warnings, or citations in images: rejected because
  Markdown must remain searchable, accessible, citable, translatable, and easier
  to validate.
- Add a separate sidecar metadata file per exercise image now: rejected because
  the current centralized provenance table remains sufficient for this scope.

## Consequences

Benefits:

- Validators can distinguish full exercise-document setup, movement, and
  muscle-attention images without guessing.
- Existing exercise images remain compatible.
- Muscle-attention images get a narrower safety boundary than generic anatomy
  images.
- Exercise images remain subordinate to Markdown text and page-local sources.

Costs and risks:

- Validation tooling must add more context-sensitive media-purpose rules.
- `media/PROVENANCE.md` gains three more allowed purpose values for a specific
  page context.
- Manual visual-safety review remains mandatory because generated exercise
  images may look plausible while implying unsupported anatomy, technique,
  diagnosis, treatment, or correction.
- Test fixtures must cover both new exercise-specific purposes and legacy
  compatible exercise purposes.

Compatibility and migration:

- Existing exercise images using `equipment_identification` or
  `key_movement_illustration` remain valid without migration.
- The new purpose values apply to new generated raster images on full exercise
  documents.
- Pattern, condition, and exercise-preview media-purpose rules from ADR
  2026-06-29 remain unchanged.
- No physical media path migration is introduced by this ADR.

## Follow-up

- Update the exercise-image test spec to cover new purposes, legacy compatible
  purposes, image count, muscle-attention limit, visual-safety evidence, alt
  text, and provenance behavior.
- Update validation tooling only after architecture review and test-spec review.
