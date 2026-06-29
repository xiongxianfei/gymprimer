# ADR 2026-06-28: AI-Generated Raster Media Provenance

## Status

accepted

Amended by
`docs/adr/2026-06-29-expanded-raster-media-purposes.md` for expanded
Responsible Breadth page media purposes. This ADR remains active for original
Markdown-first v0.1 media and for the shared centralized provenance mechanism.

## Context

The Markdown-first v0.1 spec now allows pictures only when they are necessary
supporting visuals for beginner understanding. The first-slice media scope is
intentionally narrow: equipment identification and key movement illustration.

AI-generated raster illustrations can help when a simple original SVG is not
enough, but undocumented generated images would weaken the project's license,
provenance, safety, and review posture. The repository also needs a validation
boundary that is simple enough for a small Markdown-first project.

## Decision

Allow AI-generated raster illustrations in v0.1 only as optional support media.

For v0.1 promoted Markdown pages, media classification is deterministic and
extension-based:

- Original educational diagrams are `.svg` assets under `media/`.
- Raster assets under `media/` with extensions `.png`, `.jpg`, `.jpeg`, or
  `.webp` are classified as AI-generated raster illustrations.
- Remote image references, media paths outside `media/`, unsupported
  extensions, and missing local media files fail validation.
- The checker classifies media by path and extension before provenance lookup.

The repository uses this media architecture:

- `media/equipment/` stores optional equipment identification images.
- `media/movements/` stores optional key movement illustrations.
- `media/PROVENANCE.md` is the centralized provenance index for
  AI-generated raster illustrations.
- Each AI-generated raster asset has exactly one row in
  `media/PROVENANCE.md`.
- Provenance matching uses the exact normalized repository-relative
  `asset_path` referenced by Markdown pages.
- Valid AI raster provenance requires `asset_type = ai_generated_raster`,
  an allowed `media_purpose`, `review_status = approved`, non-blank required
  fields, and `page_refs` that include the page using the asset.
- Raster assets without an approved matching provenance row fail validation.
- Markdown text remains the instructional source of truth. Images support the
  page; they do not replace the written explanation, citations, or disclaimer.

Validation should report stable media failure codes including
`media_provenance_missing`, `media_provenance_incomplete`,
`media_provenance_not_approved`, `media_usage_out_of_scope`, and
`media_page_refs_mismatch`.

## Alternatives considered

- No images in v0.1: safest, but too restrictive for equipment recognition and
  movement-phase examples.
- Original SVG only: preferred when sufficient, but not always expressive
  enough for beginner equipment identification.
- Sidecar metadata per image: more scalable for large libraries, but too much
  file overhead for the first slice.
- Borrowed web images, stock photos, commercial screenshots, or anatomy
  posters: rejected because license review and scope risks are too high.
- AI-generated raster images without centralized provenance: rejected because
  reviewers and validators would not have deterministic source, license,
  purpose, or approval evidence.
- Original raster drawings or original photos without AI-raster provenance:
  rejected for v0.1 because they require a broader media-source taxonomy and a
  spec revision.

## Consequences

Benefits:

- The first slice can include helpful pictures without becoming media-first.
- Provenance remains readable in GitHub and easy to review in pull requests.
- Validation can deterministically map Markdown image references to provenance
  rows by `asset_path`.
- Validators can classify media before provenance lookup.
- Missing-provenance raster fixtures become deterministic test cases.
- Text-only pages remain valid when images are unnecessary.
- SVG diagrams remain the lightweight original-media format.

Costs and risks:

- Human review is required because generated exercise images may contain
  misleading posture, unsafe setup details, or irrelevant equipment features.
- `media/PROVENANCE.md` may become awkward if the media library grows.
- Contributors need clear guidance before adding generated images.
- Contributors cannot bypass provenance by adding raster images with local
  references only.
- Allowing non-AI raster images later will require a spec revision and a new or
  amended ADR.

Compatibility and migration:

- `asset_path` values in `media/PROVENANCE.md` become compatibility surfaces for
  validation and page references.
- A later proposal may replace the centralized table with sidecar metadata if
  the image library outgrows v0.1.
- Existing pages with no media remain valid.
- Existing SVG diagrams under `media/` remain valid without AI-raster
  provenance.

## Follow-up

- Review this ADR with the updated architecture package.
- Update the test spec for media provenance validation.
- Implement checker support for `media/PROVENANCE.md` only after architecture
  and test-spec review approve the boundary.
