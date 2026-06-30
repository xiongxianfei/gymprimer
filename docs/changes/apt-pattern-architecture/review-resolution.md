# Review Resolution: APT Pattern Architecture

## Findings

| Finding ID | Source review | Status | Summary |
| --- | --- | --- | --- |
| SR-APT-SPEC-1 | `docs/changes/apt-pattern-architecture/reviews/spec-review-r1.md` | resolved | Generated raster support for pattern and condition visuals lacked a deterministic `media_purpose` compatibility rule with the inherited Markdown-first provenance enum. |

## Spec-review R1 resolution

### SR-APT-SPEC-1 - Generated pattern and condition visuals need media-purpose compatibility

Status: resolved by `docs/changes/apt-pattern-architecture/reviews/spec-review-r2.md`.

Required outcome: revise `specs/responsible-breadth.md` so generated raster
images used by pattern and condition pages have a deterministic provenance
purpose rule before test-spec, planning, or implementation rely on the amended
media requirements.

Resolution:

- Chose Option B because the project direction is to use high-quality generated
  raster images instead of hard-to-understand SVG diagrams for expanded pattern,
  condition, and exercise visuals.
- Updated `specs/responsible-breadth.md` to add expanded-page
  `media_purpose` values:
  `pattern_alignment_illustration`, `anatomical_region_illustration`, and
  `exercise_preview_illustration`.
- Added purpose-specific requirements so generated raster images remain support
  assets and cannot become diagnostic, treatment, safety, anatomy, or movement
  source of truth.
- Added edge cases for wrong media-purpose mapping and diagnosis-implying
  anatomical images.
- Added acceptance coverage requiring deterministic expanded-page media-purpose
  values.

Spec-review R2 approved the amended spec with no material findings. The next
stage is architecture because the new expanded-page media-purpose enum affects
architecture/ADR validation boundaries before test-spec or implementation can
rely on it.
