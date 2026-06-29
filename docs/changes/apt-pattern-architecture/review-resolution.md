# Review Resolution: APT Pattern Architecture

## Open findings

| Finding ID | Source review | Status | Summary |
| --- | --- | --- | --- |
| SR-APT-SPEC-1 | `docs/changes/apt-pattern-architecture/reviews/spec-review-r1.md` | open | Generated raster support for pattern and condition visuals lacks a deterministic `media_purpose` compatibility rule with the inherited Markdown-first provenance enum. |

## Spec-review R1 resolution

### SR-APT-SPEC-1 - Generated pattern and condition visuals need media-purpose compatibility

Status: open.

Required outcome: revise `specs/responsible-breadth.md` so generated raster
images used by pattern and condition pages have a deterministic provenance
purpose rule before test-spec, planning, or implementation rely on the amended
media requirements.

Safe resolution path:

- Option A: limit this amendment's generated raster support to existing
  `equipment_identification` and `key_movement_illustration` purposes, and keep
  pattern alignment or condition anatomical-region raster images out of scope
  until a later media-purpose amendment.
- Option B: extend the expanded-page media-purpose enum with explicit values
  such as `pattern_alignment_illustration` and
  `anatomical_region_illustration`, then update compatibility, validation,
  edge-case, acceptance-criteria, and ADR language before implementation.
