# Review Resolution: APT Pattern Architecture

## Open findings

| Finding ID | Source review | Status | Summary |
| --- | --- | --- | --- |
| SR-APT-SPEC-1 | `docs/changes/apt-pattern-architecture/reviews/spec-review-r1.md` | addressed-pending-review | Generated raster support for pattern and condition visuals lacked a deterministic `media_purpose` compatibility rule with the inherited Markdown-first provenance enum. |

## Spec-review R1 resolution

### SR-APT-SPEC-1 - Generated pattern and condition visuals need media-purpose compatibility

Status: addressed pending spec-review R2.

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

Ready to request spec-review R2.
