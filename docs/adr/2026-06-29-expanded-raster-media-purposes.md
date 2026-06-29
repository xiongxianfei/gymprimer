# ADR 2026-06-29: Expanded Raster Media Purposes

## Status

proposed

## Context

The approved Responsible Breadth spec amendment expands GymPrimer's visual
contract for pattern, condition, and expanded exercise pages. The project now
prefers high-quality human-reviewed raster illustrations over SVG diagrams when
the visual needs realistic body position, anatomical context, or
beginner-readable movement detail.

The existing AI-generated raster media ADR intentionally limited original
Markdown-first v0.1 media purposes to `equipment_identification` and
`key_movement_illustration`. That closed enum is still correct for the original
five-page slice, but it is too narrow for expanded pages. Pattern alignment
images, condition anatomical-region images, and compact exercise previews need
deterministic provenance purpose values so validators and reviewers do not
guess.

## Decision

Keep the centralized `media/PROVENANCE.md` mechanism and extension-based raster
classification from ADR 2026-06-28.

For original Markdown-first v0.1 pages, allowed AI-generated raster
`media_purpose` values remain:

- `equipment_identification`
- `key_movement_illustration`

For expanded Responsible Breadth pages, allowed AI-generated raster
`media_purpose` values are:

- `equipment_identification`
- `key_movement_illustration`
- `pattern_alignment_illustration`
- `anatomical_region_illustration`
- `exercise_preview_illustration`

Purpose boundaries:

- `pattern_alignment_illustration` is only for non-diagnostic visual comparison
  or alignment education on pattern pages.
- `anatomical_region_illustration` is only for plain anatomical region context
  on condition pages and must not imply diagnosis, pathology, or treatment.
- `exercise_preview_illustration` is only for compact exercise support images
  referenced from pattern or condition pages. The linked exercise page remains
  the source of truth for setup and movement instructions.

Generated raster images remain support assets. Markdown text, page-local
citations, and reviewed source lists remain the source of truth for anatomy,
exercise technique, safety, diagnosis boundaries, treatment boundaries, and
programming boundaries.

## Alternatives considered

- Keep only the original two media purposes: rejected because expanded pattern
  and condition pages would have no deterministic provenance value for alignment
  or anatomical-region images.
- Use a single broad `educational_illustration` purpose: rejected because it
  would hide the safety difference between movement, alignment, anatomy, and
  exercise-preview images.
- Return to SVG-only pattern and condition diagrams: rejected because the first
  pattern-page review found SVG visuals hard for users to understand.
- Allow external anatomy images or stock illustrations: rejected because the
  project still excludes borrowed web images, stock assets, medical posters,
  and unclear-license media from this slice.

## Consequences

Benefits:

- Validators can distinguish expanded-page raster image purposes without
  guessing.
- Pattern and condition pages can use beginner-readable generated visuals while
  preserving Markdown as source of truth.
- Condition anatomical images get a stricter no-diagnosis/no-pathology boundary.
- Pattern alignment images get a non-diagnostic purpose separate from movement
  instruction.

Costs and risks:

- Validation tooling must know which page classes may use which expanded
  purpose values.
- `media/PROVENANCE.md` gains more enum values and therefore more review
  responsibility.
- Human visual review remains mandatory because generated body-position and
  anatomy images can look plausible while being misleading.
- Existing architecture and tests must be updated before implementation relies
  on the new purposes.

Compatibility and migration:

- Existing v0.1 pages and provenance rows using `equipment_identification` or
  `key_movement_illustration` remain valid.
- The new purposes are allowed only for expanded Responsible Breadth pages.
- Existing SVG assets remain valid when they are clear enough, but expanded
  pages should prefer high-quality raster illustrations when SVG is not
  beginner-readable.
- No physical media path migration is introduced by this ADR.

## Follow-up

- Review this ADR with the architecture amendment.
- Update the Responsible Breadth test spec to map expanded media-purpose values
  to automated validation and manual visual-safety proof.
- Update validation tooling before promoting pages that rely on
  `pattern_alignment_illustration`, `anatomical_region_illustration`, or
  `exercise_preview_illustration`.
