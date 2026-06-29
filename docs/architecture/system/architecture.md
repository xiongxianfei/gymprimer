# GymPrimer Markdown-First Architecture

## Status

- approved

## Related artifacts

- Proposal: `../../proposals/2026-06-27-markdown-first-gym-primer.md`
- Spec: `../../../specs/markdown-first-primer.md`
- Spec reviews:
  - `../../changes/markdown-first-gym-primer/reviews/spec-review-r1.md`
  - `../../changes/markdown-first-gym-primer/reviews/spec-review-r3.md`
- ADRs:
  - `../../adr/2026-06-27-markdown-first-citation-based-authority.md`
  - `../../adr/2026-06-28-ai-generated-raster-media-provenance.md`
  - `../../adr/2026-06-26-repository-native-reviewed-content.md` (superseded)

## Introduction and Goals

This architecture defines how GymPrimer is shaped as a Markdown-first beginner exercise-literacy primer for v0.1. The repository itself is the product surface: readers should be able to open Markdown pages directly, inspect sources, and understand the first five pages without an app, database, generated public JSON package, or hosted website.

Goals:

- Keep Markdown pages as canonical source.
- Make citation coverage, disclaimers, scope boundaries, media provenance, and
  privacy checkable.
- Allow only necessary v0.1 supporting visuals with deterministic provenance.
- Keep mdBook optional and derived.
- Preserve old platform artifacts as historical context without treating them as active implementation guidance.

## Architecture Constraints

- `CONSTITUTION.md`, `VISION.md`, and `specs/markdown-first-primer.md` govern this architecture.
- The first slice is exactly five English-first pages before broader content expansion.
- Full Chinese translation, external media assets, formal expert-review
  lifecycle, generated public JSON, hosted app, CMS, AI assistant, and
  deployment are out of scope for v0.1.
- Images are optional in v0.1 and may be used only when necessary for equipment
  identification or key movement illustration.
- AI-generated raster illustrations must be project-reviewed support assets
  with one matching row in `media/PROVENANCE.md`.
- Safety claims require claim-level citations and page-local sources.
- Markdown pages must remain readable without generated HTML, JavaScript, a local server, or search index.
- Existing structured-platform artifacts are historical when they conflict with current governance.

## Context and Scope

The system boundary is the GymPrimer repository and optional local derived HTML.
Maintainers and contributors author Markdown content, source indexes,
contributor rules, optional media, media provenance, and check evidence.
Beginner readers browse Markdown directly in GitHub or a clone. mdBook, if
present, reads Markdown and emits derived HTML only.

Out of scope:

- Public web app, CMS, database, user accounts, analytics, and deployment.
- Generated public JSON as the product.
- Formal reviewer routing, review lifecycle state, and audit-event architecture.
- AI-generated exercise guidance as source of truth.
- Decorative, stock, screenshot, commercial-machine, anatomy-poster,
  medical, rehab, or identifying-person media in v0.1.

See [diagrams/context.mmd](diagrams/context.mmd) for the C4 system context view.

## Solution Strategy

Use a small repository-native Markdown corpus before building platform machinery.

The architecture favors:

- self-contained pages over structured records;
- page-local sources over global-only bibliography;
- manual or lightweight checks over schema/lifecycle gates;
- no image over unnecessary image use;
- simple original SVG over generated raster when a vector diagram is enough;
- human-reviewed AI-generated raster only when needed for equipment
  identification or key movement illustration;
- centralized media provenance over sidecar-per-image metadata;
- stable Markdown paths over early website routing;
- optional mdBook output over a frontend framework.

The main tradeoff is reduced automation and search capability in exchange for
faster proof that beginners can understand the content. The media tradeoff is
that centralized provenance is simple and reviewable for v0.1, but it may need
to be replaced if the asset library grows substantially.

## Building Block View

Top-level artifact groups:

| Area | Responsibility |
| --- | --- |
| `README.md` | Product entry point and navigation to active Markdown pages. |
| `SOURCES.md` | Global index for sources reused across pages. |
| `CONTRIBUTING.md` | Contribution rules for citations, scope, licensing, and media rights. |
| `CONTENT_LICENSE.md` | Content and diagram licensing terms. |
| `01-getting-started/` | Beginner principle pages and primer safety framing. |
| `02-machines/` | Machine exercise pages. |
| `03-bodyweight/` | Beginner bodyweight progression pages. |
| `media/` | Optional supporting media, limited to original SVGs and approved AI-generated raster illustrations for v0.1. |
| `media/PROVENANCE.md` | Central provenance index for AI-generated raster illustrations, keyed by exact repository-relative `asset_path`. |
| `media/equipment/` | Optional equipment identification images. |
| `media/movements/` | Optional key movement illustrations. |
| `book.toml`, `SUMMARY.md` | Optional minimal mdBook configuration after Markdown pages work directly. |
| `tools/checks/` | Optional lightweight local checks for sources, disclaimers, scope, media paths, links, and privacy. |
| `docs/changes/` | Review records, manual proof, and workflow evidence. |
| Historical platform artifacts | Prior schema, validator, generated output, and ADR evidence; not active v0.1 product surfaces. |

Logical containers:

- **Markdown corpus**: active source pages plus navigation and source index.
- **Contribution and license contract**: contributor-facing documentation that governs inbound content and media.
- **Optional media assets**: original SVGs or approved AI-generated raster
  illustrations referenced from Markdown by relative path.
- **Media provenance index**: one row per AI-generated raster asset, with
  generator, creation notes, license assertion, human review status, media
  purpose, page references, and exact asset path.
- **Lightweight validation checks**: local scripts or manual proof records, with no mandatory schema platform for v0.1.
- **Optional mdBook renderer**: derived static HTML output.
- **Historical platform evidence**: old structured-platform artifacts retained for traceability.

See [diagrams/container.mmd](diagrams/container.mmd) for the C4 container view.

## Runtime View

Primary reader flow:

1. A reader opens `README.md` in GitHub or a clone.
2. The reader follows a relative link to one of the five first-slice pages.
3. The page presents a disclaimer, beginner explanation, safety notes, and sources.
4. The reader can inspect source links from the same page.

Authoring and promotion flow:

1. A contributor drafts a non-canonical spike page.
2. Maintainers check page shape, disclaimer, claim-level safety citations,
   page-local sources, excluded scope, media provenance, privacy, and links.
3. At least one beginner read test records whether the exercise pages communicate purpose, setup, steps, and stop conditions.
4. A page is promoted only when checks and evidence satisfy the spec.

Optional mdBook flow:

1. Minimal `book.toml` and `SUMMARY.md` are added after Markdown pages work directly.
2. `mdbook build` reads Markdown and emits derived HTML.
3. mdBook failure blocks only derived HTML, unless it reveals broken Markdown navigation.

Media validation flow:

1. A Markdown page may reference no media, an original SVG, or an AI-generated
   raster illustration by relative path.
2. Before provenance lookup, checks classify every Markdown image reference by
   resolved repository path and lowercase file extension.
3. No image reference means the page is text-only and remains valid.
4. `.svg` files under `media/` are classified as original educational diagrams
   and do not require AI-raster provenance.
5. `.png`, `.jpg`, `.jpeg`, and `.webp` files under `media/` are classified as
   AI-generated raster illustrations.
6. AI-generated raster illustrations require an approved matching row in
   `media/PROVENANCE.md`.
7. Checks normalize the raster Markdown reference to a repository-relative
   `asset_path`, then find the exact matching row in `media/PROVENANCE.md`.
8. The row must have required fields, `asset_type = ai_generated_raster`, an
   allowed `media_purpose`, `review_status = approved`, and `page_refs` that
   include the referencing Markdown page.
9. Remote image URLs, image paths outside `media/`, unsupported extensions,
   missing local media files, missing provenance, incomplete provenance,
   non-approved provenance, out-of-scope purpose, or mismatched `page_refs`
   block promotion.

The checker does not use an existing provenance row to decide whether an asset
is raster media. Provenance lookup occurs only after extension-based
classification.

Failure paths:

- Missing disclaimer, missing page-local sources, global-only safety citation,
  excluded scope, missing or invalid media provenance, private data, or
  unverified safety wording blocks promotion.
- Missing local tools are recorded as validation gaps, not passing results.

## Deployment View

v0.1 has no hosted deployment.

Environments:

- **Repository browsing**: GitHub or local clone is the primary reader environment.
- **Authoring**: local editor or pull request.
- **Local checks**: optional scripts and manual inspections run in a contributor environment.
- **Derived HTML**: local mdBook output if mdBook remains minimal.

Packaging boundaries:

- Markdown, source index, contributor docs, license docs, original SVGs,
  approved AI-generated raster illustrations, and `media/PROVENANCE.md` are
  source assets.
- mdBook output is generated and disposable.
- Historical generated JSON and validator evidence are not v0.1 release packages.

## Crosscutting Concepts

Source authority:

- Markdown files are canonical after promotion.
- Generated HTML and generated validation output are derived evidence or convenience output.

Citation and safety:

- Safety claims need claim-level citations.
- Every page needs page-local sources.
- Global `SOURCES.md` supports reuse but does not replace page-local citation.

Scope control:

- Excluded advanced lifting, rehab, diagnosis, pain-treatment, posture-correction, and programming topics are blocked before promotion.

Media:

- Images are optional; a text-only page can be valid.
- Allowed v0.1 media purposes are `equipment_identification` and
  `key_movement_illustration`.
- Media choice follows this preference order: no image, simple original SVG,
  then AI-generated raster illustration when SVG is not enough.
- In v0.1 promoted pages, original educational diagrams are SVG files under
  `media/`.
- Any raster image under `media/` with extension `.png`, `.jpg`, `.jpeg`, or
  `.webp` is treated as an AI-generated raster illustration.
- AI-generated raster illustrations require one centralized provenance row in
  `media/PROVENANCE.md`.
- Provenance matching is exact by normalized repository-relative `asset_path`.
- Original raster drawings, original photos, third-party licensed raster
  assets, screenshots, stock assets, and commercial machine images are out of
  scope unless a later spec revision changes the media contract.
- External images, screenshots, decorative art, stock-style images,
  commercial-machine screenshots, anatomy posters, medical or rehab
  illustrations, and images with identifying people are excluded.

Privacy:

- Content, examples, generated evidence, and reader-test notes must not contain private health information, private contacts, secrets, or local machine paths.

Observability:

- Local checks and manual proof records identify the page and rule that passed or failed.
- Media validation findings use stable codes such as
  `media_provenance_missing`, `media_provenance_incomplete`,
  `media_provenance_not_approved`, `media_usage_out_of_scope`, and
  `media_page_refs_mismatch`.
- Media validation findings also report the extension-based classification
  result and use stable classification failure codes such as
  `external_media_reference`, `media_outside_allowed_directory`,
  `unsupported_media_type`, and `media_asset_missing`.

## Architecture Decisions

- [ADR 2026-06-27: Markdown-first citation-based authority](../../adr/2026-06-27-markdown-first-citation-based-authority.md) - Make Markdown the v0.1 source of truth and use citation-based authority.
- [ADR 2026-06-28: AI-generated raster media provenance](../../adr/2026-06-28-ai-generated-raster-media-provenance.md) - Allow narrow AI-generated raster support assets with centralized provenance.
- [ADR 2026-06-26: Repository-native reviewed content](../../adr/2026-06-26-repository-native-reviewed-content.md) - Superseded structured-platform decision retained as history.

## Quality Requirements

| Quality | Scenario | Measure |
| --- | --- | --- |
| Readability | A beginner opens a first-slice page on GitHub. | The page can be understood without app navigation, generated HTML, or local tooling. |
| Traceability | A reviewer checks a safety warning. | The claim has a page-local citation and source entry. |
| Scope safety | A contributor adds rehab, diagnosis, pain treatment, or advanced lifting content. | The page is blocked before promotion. |
| Media licensing | A page references media. | The media is original or clearly project-licensed and referenced by relative path. |
| Media provenance | A page references an AI-generated raster image. | The image has one approved `media/PROVENANCE.md` row with exact `asset_path`, valid purpose, required fields, and matching `page_refs`. |
| Portability | mdBook is removed or unavailable. | README-linked Markdown pages remain usable. |
| Privacy | Validation evidence or reader-test notes are shared. | No secrets, private contacts, private health information, or local paths appear. |
| Performance | Local checks run on the v0.1 slice. | Checks complete within 30 seconds excluding network-dependent link checking. |

## Risks and Technical Debt

- Citation quality depends on maintainer judgment until check tooling and source guidance are implemented.
- GitHub navigation may become weak as the corpus grows.
- The old structured-platform artifacts may confuse contributors until superseded or archived visibly.
- mdBook can pull attention toward website work if custom styling or plugins are allowed too early.
- Beginner read-test evidence is manual and low sample size in v0.1.
- Exact link checker, Markdown linter, and source-check tooling remain undecided.
- The centralized media provenance table can become awkward if the media
  library grows beyond the first slice.
- AI-generated raster illustrations may look plausible while showing unsafe or
  misleading setup details; human review remains mandatory.

## Glossary

- **Canonical Markdown**: The promoted Markdown files that define the product content.
- **Claim-level citation**: A citation adjacent to the claim it supports.
- **Derived HTML**: Static HTML produced from Markdown that does not replace Markdown authority.
- **AI-generated raster illustration**: A bitmap support image generated by an
  AI image tool and reviewed by a human maintainer before use.
- **Non-canonical spike**: Draft content used to test the format before promotion.
- **Historical platform artifact**: Prior schema, validator, generated-output, ADR, or review evidence retained for traceability but not active v0.1 guidance.
- **Media provenance index**: `media/PROVENANCE.md`, the centralized table that
  records AI-generated raster asset provenance.

## Next artifacts

- Architecture review for the media provenance amendment.

## Follow-on artifacts

- Test specification update for media provenance checks.
- Plan update for first-slice content, contributor guidance, license
  clarification, media provenance, and optional mdBook.
- Archive or supersession record for old platform artifacts.

## Readiness

This architecture package is approved after
`docs/changes/markdown-first-gym-primer/reviews/architecture-review-r3.md`.
It is ready for downstream test-spec and plan updates for the media provenance
boundary. It is not implementation-ready, verification-ready, branch-ready, or
PR-ready until downstream artifacts are updated and reviewed.
