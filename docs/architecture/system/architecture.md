# GymPrimer Markdown-First Architecture

## Status

- approved

This media-purpose amendment was approved by
`docs/changes/apt-pattern-architecture/reviews/architecture-review-r2.md`. The
prior layout-view amendment was approved by
`docs/changes/apt-pattern-architecture/reviews/architecture-review-r1.md`.
The repository-layout-normalization amendment was approved by
`docs/changes/repository-layout-normalization/reviews/architecture-review-r1.md`.

Prior approved baselines:

- Responsible Breadth architecture review:
  `docs/changes/responsible-breadth/reviews/architecture-review-r1.md`
- Markdown-first architecture review:
  `docs/changes/markdown-first-gym-primer/reviews/architecture-review-r3.md`

The forward-head-posture pattern architecture amendment was approved by
`docs/changes/forward-head-posture-pattern-architecture/reviews/architecture-review-r1.md`.
The central-disclaimer amendment was approved by
`docs/changes/forward-head-posture-pattern-architecture/reviews/architecture-review-r2.md`.

## Related artifacts

- Proposal: `../../proposals/2026-06-27-markdown-first-gym-primer.md`
- Responsible Breadth proposal:
  `../../proposals/2026-06-29-responsible-breadth.md`
- Spec: `../../../specs/markdown-first-primer.md`
- Responsible Breadth spec: `../../../specs/responsible-breadth.md`
- Repository layout normalization spec:
  `../../../specs/repository-layout-normalization.md`
- Spec reviews:
  - `../../changes/markdown-first-gym-primer/reviews/spec-review-r1.md`
  - `../../changes/markdown-first-gym-primer/reviews/spec-review-r3.md`
  - `../../changes/responsible-breadth/reviews/spec-review-r2.md`
  - `../../changes/apt-pattern-architecture/reviews/spec-review-r2.md`
  - `../../changes/repository-layout-normalization/reviews/spec-review-r2.md`
  - `../../changes/forward-head-posture-pattern-architecture/reviews/spec-review-r1.md`
  - `../../changes/forward-head-posture-pattern-architecture/reviews/spec-review-r2.md`
- Forward head posture pattern architecture:
  - Proposal:
    `../../proposals/2026-06-30-forward-head-posture-pattern-architecture.md`
  - Spec: `../../../specs/forward-head-posture-pattern-architecture.md`
- ADRs:
  - `../../adr/2026-06-27-markdown-first-citation-based-authority.md`
  - `../../adr/2026-06-28-ai-generated-raster-media-provenance.md`
  - `../../adr/2026-06-29-expanded-raster-media-purposes.md`
  - `../../adr/2026-06-29-direct-repository-layout-normalization.md`
  - `../../adr/2026-06-29-responsible-breadth-static-content-boundaries.md`
  - `../../adr/2026-06-30-central-red-flags-disclaimer.md`
  - `../../adr/2026-06-26-repository-native-reviewed-content.md` (superseded)

## Introduction and Goals

This architecture defines how GymPrimer is shaped as a Markdown-first beginner
primer. The repository itself is the product surface: readers should be able to
open Markdown pages directly, inspect sources, and understand the content
without an app, database, generated public JSON package, or hosted website.

The original v0.1 five-page exercise-literacy slice remains governed by the
Markdown-first spec. The accepted expanded-scope spec adds a second governed
static-content surface for non-diagnostic pattern education, consumer condition
education, programming principles, static program examples, and expanded
exercise pages.

Goals:

- Keep Markdown pages as canonical source.
- Make citation coverage, the central disclaimer, scope boundaries, media
  provenance, and privacy checkable.
- Allow only necessary supporting visuals with deterministic provenance.
- Keep mdBook optional and derived.
- Add expanded static content without introducing diagnosis, treatment,
  individualized programming, symptom collection, or runtime decision support.
- Make red-flag routing, source quality, page metadata, and review cadence
  visible in Markdown and review evidence.
- Preserve old platform artifacts as historical context without treating them as active implementation guidance.

## Architecture Constraints

- `CONSTITUTION.md`, `VISION.md`, `specs/markdown-first-primer.md`, and
  `specs/responsible-breadth.md` govern this architecture.
- The original Markdown-first first slice is exactly five English-first pages
  before broader content expansion.
- The expanded-scope first proof slice is exactly one red-flags reference,
  one pattern page, one condition page, one programming-principle page, and one
  program-example page before broader scaling.
- Expanded-scope pages are path-classified under `patterns/`,
  `conditions/`, `principles/`, `programs/`, and `exercises/`.
- `RED-FLAGS.md` is the target canonical red-flags reference after repository
  layout normalization.
- `RED-FLAGS.md` owns the central GymPrimer disclaimer. Page templates route
  safety context to `RED-FLAGS.md` when needed instead of repeating disclaimer
  boilerplate on every page.
- RigorLoop governance and workflow artifacts remain under `docs/proposals/`,
  `docs/adr/`, `docs/changes/`, `docs/plans/`, and `docs/learn/` per
  `docs/workflows.md`.
- Physical layout normalization, including moving original v0.1 exercise pages
  into `exercises/`, folding `01-getting-started/` into `principles/`, moving
  `about/red-flags.md` to `RED-FLAGS.md`, reorganizing media by content slug,
  and removing old paths directly, requires dependency inventory, spec/ADR
  coverage, test-spec, and plan review before implementation because current
  approved specs and tests name existing paths.
- Full Chinese translation, external media assets, formal expert-review
  lifecycle, generated public JSON, hosted app, CMS, AI assistant, and
  deployment are out of scope for v0.1.
- Symptom-checker flows, diagnostic decision trees, personalized plans,
  treatment protocols, rehabilitation pathways, return-to-training
  prescriptions, and specialized-population content remain out of scope.
- Images are optional. Original Markdown-first v0.1 media remains limited to
  equipment identification and key movement illustration. Expanded Responsible
  Breadth pages may also use generated raster support images for pattern
  alignment, anatomical region context, and compact exercise previews when
  those images satisfy the stricter expanded media-purpose rules.
- AI-generated raster illustrations must be project-reviewed support assets
  with one matching row in `media/PROVENANCE.md`.
- Safety claims require claim-level citations and page-local sources.
- Markdown pages must remain readable without generated HTML, JavaScript, a local server, or search index.
- Existing structured-platform artifacts are historical when they conflict with current governance.
- The forward-head-posture proof slice is one pattern page plus five
  same-slice exercise pages:
  `patterns/forward-head-posture.md`, `exercises/chin-nod.md`,
  `exercises/thoracic-extension.md`, `exercises/wall-slide.md`,
  `exercises/prone-y-t.md`, and `exercises/band-pull-apart.md`.
- The forward-head-posture pattern page may use at most one support raster
  image under `media/patterns/forward-head-posture/`; the image is not an
  exercise routine, before/after cure claim, or source of truth for labels,
  safety claims, or instructions.
- README promotion for pattern pages remains gated on the approved pattern set,
  not on the forward-head-posture page alone.

## Context and Scope

The system boundary is the GymPrimer repository and optional local derived HTML.
Maintainers and contributors author Markdown content, source indexes,
contributor rules, optional media, media provenance, review evidence, and check
evidence.
Beginner readers browse Markdown directly in GitHub or a clone. mdBook, if
present, reads Markdown and emits derived HTML only.

Out of scope:

- Public web app, CMS, database, user accounts, analytics, and deployment.
- Generated public JSON as the product.
- Formal reviewer routing, review lifecycle state, and audit-event architecture.
- AI-generated exercise guidance as source of truth.
- User-input collection, symptom triage, diagnosis, personalized programming,
  treatment planning, and rehab decision support.
- Decorative, stock, screenshot, commercial-machine, borrowed anatomy-poster,
  diagnostic/pathology-implying, rehab-protocol, or identifying-person media.

See [diagrams/context.mmd](diagrams/context.mmd) for the C4 system context view.

## Solution Strategy

Use a small repository-native Markdown corpus before building platform machinery.

The architecture favors:

- self-contained pages over structured records;
- page-local sources over global-only bibliography;
- lightweight checks and recorded review evidence over schema/lifecycle gates;
- no image over unnecessary image use;
- high-quality human-reviewed raster over SVG for expanded pages when realistic
  body position, anatomical context, or beginner-readable movement detail is
  needed;
- simple original SVG only when it is sufficient for beginner comprehension;
- human-reviewed AI-generated raster only when needed for an allowed media
  purpose;
- centralized media provenance over sidecar-per-image metadata;
- centralized red-flags and disclaimer language over repeated per-page
  disclaimer scaffolding;
- path-classified expanded static pages over a database or CMS taxonomy;
- page-local safety boundaries and review metadata over hidden lifecycle state;
- recorded semantic review evidence where source quality and prescription boundaries
  cannot be fully automated;
- stable Markdown paths over early website routing;
- optional mdBook output over a frontend framework.

The main tradeoff is reduced automation and search capability in exchange for
faster proof that beginners can understand the content. The media tradeoff is
that centralized provenance is simple and reviewable for v0.1, but it may need
to be replaced if the asset library grows substantially.

## Building Block View

The durable architecture view has five logical blocks. Product content,
governance, and operations are intentionally separated so the content surface
does not get flattened together with workflow evidence or tooling.

| Block | Current paths | Responsibility |
| --- | --- | --- |
| Project references | `README.md`, `CONTRIBUTING.md`, `SOURCES.md`, `CONTENT_LICENSE.md`, `RED-FLAGS.md` | Project entry, contribution rules, reusable source index, central disclaimer, safety routing, and licensing. |
| Content | `exercises/`, `patterns/`, `conditions/`, `principles/`, `programs/` | Canonical Markdown product pages. Equipment type is page metadata, not a folder split. |
| Media | `media/<content-type>/<slug>/...`, `media/PROVENANCE.md` | Optional supporting raster illustrations referenced by Markdown. Raster assets use provenance purpose values to distinguish equipment, movement, pattern alignment, anatomy context, and exercise previews. |
| Governance | `docs/proposals/`, `docs/adr/`, `docs/architecture/` | Accepted direction, durable decisions, and canonical architecture. These remain under `docs/` per RigorLoop workflow requirements. |
| Tooling and operations | `tools/`, `specs/`, `docs/changes/`, `docs/plans/`, `docs/learn/`, optional `book.toml` and `SUMMARY.md` | Validation, specs/test specs, plans, review evidence, learning records, and optional derived-site configuration. These serve content but are not product content blocks. |

Layout normalization target:

| Target surface | Target path | Migration note |
| --- | --- | --- |
| Exercise pages | `exercises/<slug>.md` | Fold `02-machines/` and `03-bodyweight/` into one exercise namespace. Equipment type becomes page metadata, not a folder split. Remove old numbered paths directly. |
| Beginner principles | `principles/beginner-training-principles.md` | Fold `01-getting-started/beginner-training-principles.md` into principles. Remove old numbered path directly. |
| Pattern pages | `patterns/<slug>.md` | Already matches the target. |
| Condition pages | `conditions/<slug>.md` | Already matches the target. |
| Program examples | `programs/<slug>.md` | Already matches the target. |
| Red flags | `RED-FLAGS.md` | Move `about/red-flags.md` to root. Remove the old `about/red-flags.md` path directly after links and checks are updated. |
| Media | `media/<content-type>/<slug>/...` | Promoted media is subject-co-located by the content page it supports. |
| Governance | `docs/proposals/`, `docs/adr/` | Keep these paths; root-level `proposals/` and `adr/` are rejected for this repository because `docs/workflows.md` standardizes RigorLoop artifact locations. |

Logical containers:

- **Project references**: root entry, contribution, source-index, license,
  central-disclaimer, and safety-routing files.
- **Content corpus**: active source pages, currently split between original
  v0.1 paths and expanded content paths until a migration spec normalizes the
  tree.
- **Expanded static content pages**: path-classified pages under `patterns/`,
  `conditions/`, `principles/`, `programs/`, and `exercises/`.
- **Contribution and license contract**: contributor-facing documentation that
  governs inbound content and media.
- **Red-flags and sources references**: shared root `RED-FLAGS.md` owns the
  central disclaimer and red-flag routing; `SOURCES.md` owns reusable source
  identifiers. Safety-relevant pages link `RED-FLAGS.md` when they mention
  pain, symptoms, professional care, or self-management themes.
- **Optional media assets**: original SVGs or approved AI-generated raster
  illustrations referenced from Markdown by relative path.
- **Media provenance index**: one row per AI-generated raster asset, with
  generator, creation notes, license assertion, human review status, media
  purpose, page references, and exact asset path.
- **Tooling and operations**: specs, validation scripts, change-local evidence,
  plans, learning records, and optional mdBook configuration.
- **Review evidence records**: change-local evidence under
  `docs/changes/<change-id>/` for semantic source quality, safety boundaries,
  visual necessity, page review metadata, and reader comprehension where those
  checks cannot be fully automated.
- **Optional mdBook renderer**: derived static HTML output.

Forward-head-posture proof-slice building blocks:

- **Pattern page**: `patterns/forward-head-posture.md` owns the observable
  pattern explanation, red-flag routing, uncertainty framing, core reasons,
  detailed exercise annotations, broader collected exercise list, next links,
  sources, and author/review metadata.
- **Same-slice exercise pages**: `exercises/chin-nod.md`,
  `exercises/thoracic-extension.md`, `exercises/wall-slide.md`,
  `exercises/prone-y-t.md`, and `exercises/band-pull-apart.md` own setup,
  muscles involved, movement breakdown, feel cues, common mistakes, variations,
  safety notes, and exercise-page-local sources.
- **Optional pattern media**: at most one comparison raster image may live under
  `media/patterns/forward-head-posture/`, with exact approved provenance in
  `media/PROVENANCE.md` and no in-image text.
- **Validation hooks**: tooling checks detailed exercise-link existence from the
  pattern page, existence of any referenced pattern image asset, page-local
  sources, media provenance, privacy, and forbidden diagnostic, treatment,
  rehab, posture-correction, and personalized-programming language.

See [diagrams/container.mmd](diagrams/container.mmd) for the C4 container view.

## Runtime View

Primary reader flow:

1. A reader opens `README.md` in GitHub or a clone.
2. The reader follows a relative link to one of the five first-slice pages.
3. The page presents beginner explanation, safety notes, sources, and links to centralized red-flag routing when needed.
4. The reader can inspect source links from the same page.

Authoring and promotion flow:

1. A contributor drafts a non-canonical spike page.
2. Maintainers check page shape, the central `RED-FLAGS.md` disclaimer, claim-level safety citations,
   page-local sources, excluded scope, media provenance, privacy, and links.
3. At least one beginner read test records whether the exercise pages communicate purpose, setup, steps, and stop conditions.
4. A page is promoted only when checks and evidence satisfy the spec.

Expanded static-content authoring and promotion flow:

1. A contributor drafts an expanded page under exactly one path-classified page
   class: `patterns/`, `conditions/`, `principles/`, `programs/`, or
   `exercises/`.
2. The page remains draft-only until checks classify the page class and verify
   required sections, review metadata, source count, source-index references,
   red-flag links where required, central-disclaimer availability, media
   path/provenance rules, and privacy.
3. Maintainers record review evidence under the relevant
   `docs/changes/<change-id>/` directory for semantic source quality,
   non-diagnostic/non-prescriptive language, source support for safety claims,
   visual necessity where media exists, review cadence, and comprehension
   outcomes.
4. A pattern or condition page is promoted only when red-flag routing appears
   before self-management discussion and the review evidence confirms the page
   does not diagnose the reader.
5. A program-example page is promoted only when the review evidence confirms that
   the page is a static illustration and not a personal prescription.
6. README, SUMMARY, or other active navigation links must not expose
   expanded pages as promoted content until the expanded slice passes
   the reviewed workflow.

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
9. For original Markdown-first v0.1 pages, allowed `media_purpose` values
   remain `equipment_identification` and `key_movement_illustration`.
10. For expanded Responsible Breadth pages, allowed `media_purpose` values are
   `equipment_identification`, `key_movement_illustration`,
   `pattern_alignment_illustration`, `anatomical_region_illustration`, and
   `exercise_preview_illustration`.
11. Remote image URLs, image paths outside `media/`, unsupported extensions,
   missing local media files, missing provenance, incomplete provenance,
   non-approved provenance, out-of-scope purpose, or mismatched `page_refs`
   block promotion.

The checker does not use an existing provenance row to decide whether an asset
is raster media. Provenance lookup occurs only after extension-based
classification.

Repository layout normalization flow:

1. The migration inventory identifies active references to every file that will
   be moved or removed, including Markdown links, README navigation,
   `SUMMARY.md`, `book.toml`, source references, tests, checkers, review records,
   change metadata, and provenance rows.
2. Dependency references are updated or explicitly removed before the old file
   path is removed.
3. Numbered exercise and getting-started Markdown paths are folded into
   `exercises/` and `principles/`, then the old numbered paths are removed
   directly without compatibility stubs.
4. `about/red-flags.md` is moved to root `RED-FLAGS.md`, then the old path is
   removed directly.
5. Promoted media is moved to `media/<content-type>/<slug>/`, provenance rows
   and Markdown references are updated in the same change, and old media-bucket
   paths are removed directly.
6. Historical structured-platform artifacts are removed directly when no active
   approved spec, test, workflow guide, or validation command relies on them.
   If an active dependency still requires retention, the artifact is labeled
   historical or archived.
7. Validation fails if any active reference still points at a removed path, if
   a compatibility stub remains, or if provenance no longer matches the moved
   raster asset.

Failure paths:

- Missing central `RED-FLAGS.md` disclaimer, missing page-local sources, global-only safety citation,
  excluded scope, missing or invalid media provenance, private data, or
  unverified safety wording blocks promotion.
- Missing Responsible Breadth page classification, missing page-contract
  sections, missing red-flag routing, weak source quality, missing review
  metadata, or missing required review evidence keeps an expanded page draft-only.
- Diagnosis, treatment-plan, rehab-progression, posture-correction promise,
  personalized programming, symptom collection, or injury-specific protocol
  language blocks expanded-page promotion.
- Missing local tools are recorded as validation gaps, not passing results.
- Repository layout migration fails if dependency inventory is missing, old
  paths remain referenced, compatibility stubs remain, moved media lacks
  updated provenance, or historical artifacts are removed while still actively
  referenced.

Forward-head-posture proof-slice authoring flow:

1. A contributor drafts `patterns/forward-head-posture.md` and the five
   same-slice exercise pages in the same implementation slice.
2. The pattern page links only detailed exercise annotations to existing
   same-slice exercise pages and keeps broader collected exercises secondary
   unless they also have full exercise pages and annotations.
3. If an image is used, the Markdown references one local asset under
   `media/patterns/forward-head-posture/` and `media/PROVENANCE.md` carries the
   exact approved `asset_path`, allowed purpose, and page reference.
4. Local checks verify required page contracts, detailed exercise-link
   existence, image-asset existence, source sections, source-index reuse where
   applicable, media provenance, privacy, and forbidden language.
5. README, SUMMARY, or other active navigation promotion waits for the full
   approved pattern set, even when this proof page passes local validation.

## Deployment View

v0.1 has no hosted deployment.

Expanded static content does not add a hosted deployment, runtime, CMS, API, search
index, user-input flow, account system, analytics, or external service.

Environments:

- **Repository browsing**: GitHub or local clone is the primary reader environment.
- **Authoring**: local editor or pull request.
- **Local checks**: optional scripts and manual inspections run in a contributor environment.
- **Derived HTML**: local mdBook output if mdBook remains minimal.

Packaging boundaries:

- Markdown, source index, contributor docs, license docs, original SVGs,
  approved AI-generated raster illustrations, and `media/PROVENANCE.md` are
  source assets.
- Expanded static content pages, red-flags references, shared source
  indexes, review evidence records, and validation reports are repository source or
  workflow evidence.
- mdBook output is generated and disposable.
- Historical generated JSON and validator evidence are not v0.1 release packages.
- Repository layout normalization is a source-tree migration only. It does not
  introduce deployment, hosting, generated HTML authority, CMS, runtime API, or
  search infrastructure.

## Crosscutting Concepts

Source authority:

- Markdown files are canonical after promotion.
- Generated HTML and generated validation output are derived evidence or convenience output.

Citation and safety:

- Safety claims need claim-level citations.
- Every page needs page-local sources.
- Global `SOURCES.md` supports reuse but does not replace page-local citation.
- `RED-FLAGS.md` owns the central disclaimer and red-flag routing reference.
  Page templates should link to it when safety context is relevant and should
  not scaffold repeated disclaimer blocks.

Scope control:

- For the original five-page v0.1 slice, Markdown-first R21/R22 scope
  exclusions continue to apply.
- For expanded static content page classes only, expanded pattern, condition,
  programming-principle, static program-example, and expanded exercise education
  is allowed under `specs/responsible-breadth.md`.
- Diagnosis, personalized treatment, personalized programming, rehab protocols,
  acute injury guidance, post-surgical guidance, specialized-population
  guidance, AI-generated source-of-truth content, and clinical-authority claims
  remain blocked before promotion.
- Pattern pages may explain non-diagnostic patterns and mainstream
  self-management themes; they must not promise correction or prescribe a
  corrective routine.
- Condition pages may provide general consumer education with red-flag routing;
  they must not present treatment plans or help readers self-diagnose.
- Program-example pages may show static worked examples; they must not adapt to
  symptoms, goals, equipment, constraints, or training response.

Expanded static content page contracts:

- Page class is derived from path for the first expanded slice:
  `patterns/*.md`, `conditions/*.md`, `principles/*.md`, `programs/*.md`, and
  `exercises/*.md`.
- Pattern and condition pages require the page sections defined by
  `specs/responsible-breadth.md`, including "What this page is", "What this
  page is not", red flags, mainstream agreement, uncertainty, self-management
  themes, avoidances, professional routing, sources, and author/review date.
- Every expanded static content page carries author, created date, last reviewed
  date, next review due date, and review scope metadata.
- Red-flag routing must appear before self-management discussion on safety-
  relevant expanded pages.

Source quality and review evidence:

- Source count is necessary but not sufficient. Expanded pages require the
  source-quality mix defined by page class.
- Source-index validity and page-local source presence remain shared
  Markdown-first checks.
- Semantic source quality, scope-boundary judgment, and claim support require
  recorded review evidence when checks cannot verify them.
- Review evidence records live under the relevant `docs/changes/<change-id>/`
  directory.
- Forward-head-posture pattern claims use four source families: red flags and
  professional routing, posture-pattern evidence and uncertainty,
  shoulder/scapular and rotator-cuff context, and general resistance-training
  framing.
- Same-slice exercise pages require page-local source support for setup,
  technique, muscle, feel-cue, common-mistake, and safety claims; the pattern
  page's four-source set does not substitute for exercise-instruction support.

Media:

- Images are optional; a text-only page can be valid.
- Original Markdown-first v0.1 media purposes are `equipment_identification`
  and `key_movement_illustration`.
- Expanded Responsible Breadth media purposes add
  `pattern_alignment_illustration`, `anatomical_region_illustration`, and
  `exercise_preview_illustration`.
- Expanded pages should prefer high-quality human-reviewed raster
  illustrations over SVG diagrams when the visual needs realistic body
  position, anatomical context, or beginner-readable movement detail.
- SVG diagrams remain valid only when simple enough for beginner comprehension
  and when they pass visual-necessity review.
- In v0.1 promoted pages, original educational diagrams are SVG files under
  `media/`.
- Any raster image under `media/` with extension `.png`, `.jpg`, `.jpeg`, or
  `.webp` is treated as an AI-generated raster illustration.
- AI-generated raster illustrations require one centralized provenance row in
  `media/PROVENANCE.md`.
- Provenance matching is exact by normalized repository-relative `asset_path`.
- `pattern_alignment_illustration` is limited to non-diagnostic visual
  comparison or alignment education on pattern pages.
- `anatomical_region_illustration` is limited to plain anatomical region
  context on condition pages and must not imply diagnosis, pathology, or
  treatment.
- `exercise_preview_illustration` is limited to compact exercise support images
  referenced from pattern or condition pages; the linked exercise page remains
  the source of truth for setup and movement instructions.
- The forward-head-posture proof slice uses no exercise thumbnails on the
  pattern page in its first implementation slice.
- Original raster drawings, original photos, third-party licensed raster
  assets, screenshots, stock assets, and commercial machine images are out of
  scope unless a later spec revision changes the media contract.
- External images, screenshots, decorative art, stock-style images,
  commercial-machine screenshots, anatomy posters, medical or rehab
  illustrations, and images with identifying people are excluded.

Repository layout:

- Each content type has one canonical location after migration:
  `exercises/`, `patterns/`, `conditions/`, `principles/`, and `programs/`.
- `RED-FLAGS.md` is the canonical root safety-routing reference after
  migration and the central disclaimer owner.
- Governance and workflow artifacts remain under `docs/`.
- Old numbered content paths, old media-bucket paths, and the old
  `about/red-flags.md` path are removed directly; compatibility stubs are not
  used.
- Before moving or removing a file, active dependencies must be inventoried and
  updated or removed.
- Subject-co-located media paths under `media/<content-type>/<slug>/` are the
  target for promoted media referenced by content.

Privacy:

- Content, examples, generated evidence, and reader-test notes must not contain sensitive health information, private contacts, secrets, or local paths.

Observability:

- Local checks and review evidence records identify the page and rule that passed or failed.
- Disclaimer validation targets `RED-FLAGS.md`; page-level checks validate
  routing links and safety/source boundaries rather than repeated disclaimer
  boilerplate.
- Media validation findings use stable codes such as
  `media_provenance_missing`, `media_provenance_incomplete`,
  `media_provenance_not_approved`, `media_usage_out_of_scope`, and
  `media_page_refs_mismatch`.
- Media validation findings also report the extension-based classification
  result and use stable classification failure codes such as
  `external_media_reference`, `media_outside_allowed_directory`,
  `unsupported_media_type`, and `media_asset_missing`.
- Expanded static content validation should identify page class, missing section,
  missing metadata, missing red-flag link, source-count failure, source-index
  failure, excluded-scope failure, media-provenance failure, and privacy failure
  with stable messages.
- Review evidence records identify the page, requirement IDs or acceptance
  criteria checked, files inspected, reviewer/author role, non-identifying
  reader type when comprehension is tested, observed outcome, and residual
  validation gaps.
- Forward-head-posture validation reports detailed exercise-link existence,
  referenced pattern-image existence, missing page-contract sections, missing
  page-local sources, source-index failures, provenance failures, privacy
  failures, and forbidden diagnostic or prescriptive language.

## Architecture Decisions

- [ADR 2026-06-27: Markdown-first citation-based authority](../../adr/2026-06-27-markdown-first-citation-based-authority.md) - Make Markdown the v0.1 source of truth and use citation-based authority.
- [ADR 2026-06-28: AI-generated raster media provenance](../../adr/2026-06-28-ai-generated-raster-media-provenance.md) - Allow narrow AI-generated raster support assets with centralized provenance.
- [ADR 2026-06-29: Expanded raster media purposes](../../adr/2026-06-29-expanded-raster-media-purposes.md) - Add expanded-page raster purposes for pattern alignment, anatomical region context, and exercise previews.
- [ADR 2026-06-29: Direct repository layout normalization](../../adr/2026-06-29-direct-repository-layout-normalization.md) - Normalize physical repository paths by direct removal, root red flags, subject-co-located media, and dependency-first migration.
- [ADR 2026-06-29: Responsible Breadth static content boundaries](../../adr/2026-06-29-responsible-breadth-static-content-boundaries.md) - Add path-classified expanded static content classes with higher-bar review evidence, red-flag routing, and no runtime personalization.
- [ADR 2026-06-30: Central red-flags disclaimer boundary](../../adr/2026-06-30-central-red-flags-disclaimer.md) - Centralize the prominent disclaimer in `RED-FLAGS.md` and keep templates focused on safety routing.
- [ADR 2026-06-26: Repository-native reviewed content](../../adr/2026-06-26-repository-native-reviewed-content.md) - Superseded structured-platform decision retained as history.

## Quality Requirements

| Quality | Scenario | Measure |
| --- | --- | --- |
| Readability | A beginner opens a first-slice page on GitHub. | The page can be understood without app navigation, generated HTML, or local tooling. |
| Traceability | A reviewer checks a safety warning. | The claim has a page-local citation and source entry. |
| Scope safety | A contributor adds rehab, diagnosis, pain treatment, or advanced lifting content. | The page is blocked before promotion. |
| Media licensing | A page references media. | The media is original or clearly project-licensed and referenced by relative path. |
| Media provenance | A page references an AI-generated raster image. | The image has one approved `media/PROVENANCE.md` row with exact `asset_path`, valid purpose, required fields, and matching `page_refs`. |
| Expanded media purpose | A pattern page references an alignment image. | The provenance row uses `pattern_alignment_illustration`, not a generic movement purpose. |
| Condition image safety | A condition page references an anatomical-region image. | The image gives region context without implying diagnosis, pathology, or treatment. |
| Page classification | An expanded static content page is reviewed. | Its path maps to exactly one page class or the page declares one equivalent class before promotion. |
| Red-flag routing | A pattern or condition page discusses self-management themes. | The page links the red-flags reference before self-management discussion. |
| Central disclaimer | A page or checker needs the project-level disclaimer. | `RED-FLAGS.md` contains the required disclaimer near the top; page templates route to it instead of repeating it. |
| Source quality | A condition page cites three weak sources. | The page fails until it has the required institutional, guideline, patient-education, or supporting source mix. |
| Prescription boundary | A program example adapts to symptoms or goals. | The page fails promotion as personalized programming. |
| Review evidence | A semantic safety or source-quality claim cannot be automated. | A review evidence record under the relevant `docs/changes/<change-id>/` directory records the review and outcome. |
| Pattern complete loop | A forward-head-posture detailed exercise annotation links chin nod, thoracic extension, wall slide, prone Y/T, or band pull-apart. | The target same-slice exercise page exists and carries its own page-local source support for instruction and safety claims. |
| Layout migration dependency safety | A file is moved or removed. | Active references are inventoried and updated before the old path is removed. |
| Canonical content paths | A promoted exercise page is referenced. | The page lives under `exercises/`; old numbered content paths are not required and no compatibility stub remains. |
| Red-flags routing path | A safety-relevant page links red flags. | The link targets root `RED-FLAGS.md`, not `about/red-flags.md`. |
| Media co-location | A promoted page references moved media. | The asset path lives under `media/<content-type>/<slug>/` and the provenance row uses the exact new path. |
| Portability | mdBook is removed or unavailable. | README-linked Markdown pages remain usable. |
| Privacy | Validation evidence or reader-test notes are shared. | No secrets, private contacts, sensitive health information, or local paths appear. |
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
- Expanded anatomy and alignment raster images may imply diagnosis or pathology
  if prompted or reviewed poorly; purpose-specific manual visual review remains
  mandatory.
- Expanded static content source quality and non-prescription boundaries are
  partly semantic and will depend on disciplined review evidence until tooling
  matures.
- The forward-head-posture proof slice increases one pattern implementation to
  six content pages, so source-support debt can spread from pattern claims into
  exercise-instruction claims if same-slice exercise pages are treated as mere
  appendices.
- Expanded top-level directories may create navigation sprawl if README and
  SUMMARY promotion gates are not kept strict.
- Red-flag language and review cadence introduce maintenance debt; stale pages
  must be treated as not current when source changes or review dates lapse.
- Path-based page classification is simple for the first expanded slice but may
  need front matter if future content types share directories.
- Direct removal of old paths may break external bookmarks because the project
  intentionally avoids compatibility stubs for this migration.
- Dependency inventory can miss references in prose, review records, or tests if
  validation relies only on simple link parsing.
- Moving `about/red-flags.md` to `RED-FLAGS.md` improves root visibility but
  requires every safety-relevant page, checker, and review record to update links
  together.
- Moving media paths and provenance rows in one change creates a larger diff,
  but avoids split-brain asset references.
- Historical artifact removal can erase useful context if active dependencies
  are not distinguished from historical citations.

## Glossary

- **Canonical Markdown**: The promoted Markdown files that define the product content.
- **Claim-level citation**: A citation adjacent to the claim it supports.
- **Derived HTML**: Static HTML produced from Markdown that does not replace Markdown authority.
- **AI-generated raster illustration**: A bitmap support image generated by an
  AI image tool and reviewed by a human maintainer before use.
- **Non-canonical spike**: Draft content used to test the format before promotion.
- **Media provenance index**: `media/PROVENANCE.md`, the centralized table that
  records AI-generated raster asset provenance.
- **Expanded static content page class**: One of `pattern_page`, `condition_page`,
  `programming_principle_page`, `program_example_page`, or
  `expanded_exercise_page`.
- **Review evidence record**: Change-local Markdown evidence that records
  semantic review results that cannot be fully automated.
- **Dependency inventory**: The migration record of active references that must
  be updated or removed before a path is deleted.
- **Subject-co-located media**: Media stored under
  `media/<content-type>/<slug>/` for the content page or content type it
  supports.

## Next artifacts

- Execution plan and plan review for the forward-head-posture pattern
  architecture.
- Test-spec mapping for the forward-head-posture pattern architecture after
  plan review.

## Follow-on artifacts

- New ADR: `../../adr/2026-06-29-direct-repository-layout-normalization.md`.
- Forward-head-posture spec:
  `../../../specs/forward-head-posture-pattern-architecture.md`.

## Readiness

This architecture package has completed architecture-review for the
forward-head-posture pattern architecture amendment. The pattern page, five
same-slice exercise pages, optional media, provenance, and validation changes
are not implementation-ready until plan, plan-review, test-spec, and
test-spec-review are complete.
