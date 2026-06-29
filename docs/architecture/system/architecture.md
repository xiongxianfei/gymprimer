# GymPrimer Markdown-First Architecture

## Status

- draft amendment

This layout-view amendment is ready for architecture review.

Prior approved baselines:

- Responsible Breadth architecture review:
  `docs/changes/responsible-breadth/reviews/architecture-review-r1.md`
- Markdown-first architecture review:
  `docs/changes/markdown-first-gym-primer/reviews/architecture-review-r3.md`

## Related artifacts

- Proposal: `../../proposals/2026-06-27-markdown-first-gym-primer.md`
- Responsible Breadth proposal:
  `../../proposals/2026-06-29-responsible-breadth.md`
- Spec: `../../../specs/markdown-first-primer.md`
- Responsible Breadth spec: `../../../specs/responsible-breadth.md`
- Spec reviews:
  - `../../changes/markdown-first-gym-primer/reviews/spec-review-r1.md`
  - `../../changes/markdown-first-gym-primer/reviews/spec-review-r3.md`
  - `../../changes/responsible-breadth/reviews/spec-review-r2.md`
- ADRs:
  - `../../adr/2026-06-27-markdown-first-citation-based-authority.md`
  - `../../adr/2026-06-28-ai-generated-raster-media-provenance.md`
  - `../../adr/2026-06-29-responsible-breadth-static-content-boundaries.md`
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
- Make citation coverage, disclaimers, scope boundaries, media provenance, and
  privacy checkable.
- Allow only necessary v0.1 supporting visuals with deterministic provenance.
- Keep mdBook optional and derived.
- Add expanded static content without introducing diagnosis, treatment,
  individualized programming, symptom collection, or runtime decision support.
- Make red-flag routing, source quality, page metadata, and review cadence
  visible in Markdown and proof records.
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
  `conditions/`, `principles/`, `programs/`, and `exercises/`, with `about/`
  holding shared project-level references such as red flags.
- RigorLoop governance and workflow artifacts remain under `docs/proposals/`,
  `docs/adr/`, `docs/changes/`, `docs/plans/`, and `docs/learn/` per
  `docs/workflows.md`.
- Physical layout normalization, including moving original v0.1 exercise pages
  into `exercises/`, folding `01-getting-started/` into `principles/`, moving
  `about/red-flags.md`, or reorganizing media by content slug, requires a
  spec/ADR migration before implementation because current approved specs and
  tests name the existing paths.
- Full Chinese translation, external media assets, formal expert-review
  lifecycle, generated public JSON, hosted app, CMS, AI assistant, and
  deployment are out of scope for v0.1.
- Symptom-checker flows, diagnostic decision trees, personalized plans,
  treatment protocols, rehabilitation pathways, return-to-training
  prescriptions, and specialized-population content remain out of scope.
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
contributor rules, optional media, media provenance, manual proof, and check
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
- path-classified expanded static pages over a database or CMS taxonomy;
- page-local safety boundaries and review metadata over hidden lifecycle state;
- manual semantic proof records where source quality and prescription boundaries
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
| Project references | `README.md`, `CONTRIBUTING.md`, `SOURCES.md`, `CONTENT_LICENSE.md`, `about/red-flags.md` | Project entry, contribution rules, reusable source index, safety routing, and licensing. |
| Content | `01-getting-started/`, `02-machines/`, `03-bodyweight/`, `exercises/`, `patterns/`, `conditions/`, `principles/`, `programs/` | Canonical Markdown product pages. Current v0.1 compatibility keeps numbered exercise-literacy paths; target normalization is one canonical content directory per content type. |
| Media | `media/`, `media/PROVENANCE.md`, currently `media/equipment/` and `media/movements/` | Optional supporting illustrations referenced by Markdown. Target normalization is subject co-location under `media/<content-type>/<slug>/` after a migration spec. |
| Governance | `docs/proposals/`, `docs/adr/`, `docs/architecture/` | Accepted direction, durable decisions, and canonical architecture. These remain under `docs/` per RigorLoop workflow requirements. |
| Tooling and operations | `tools/`, `specs/`, `docs/changes/`, `docs/plans/`, `docs/learn/`, optional `book.toml` and `SUMMARY.md` | Validation, specs/test specs, plans, proof records, learning records, and optional derived-site configuration. These serve content but are not product content blocks. |

Layout normalization target:

| Target surface | Target path | Migration note |
| --- | --- | --- |
| Exercise pages | `exercises/<slug>.md` | Fold `02-machines/` and `03-bodyweight/` into one exercise namespace. Equipment type becomes page metadata, not a folder split. |
| Beginner principles | `principles/<slug>.md` | Fold `01-getting-started/` into principles or keep only a root orientation file if a later spec chooses that route. |
| Pattern pages | `patterns/<slug>.md` | Already matches the target. |
| Condition pages | `conditions/<slug>.md` | Already matches the target. |
| Program examples | `programs/<slug>.md` | Already matches the target. |
| Red flags | `about/red-flags.md` currently | Root `RED-FLAGS.md` is a possible future simplification, but it requires a spec update because current pages and checks reference `about/red-flags.md`. |
| Media | `media/<content-type>/<slug>/...` | Replace image-type buckets such as `media/equipment/` and `media/movements/` after link migration and provenance update. |
| Governance | `docs/proposals/`, `docs/adr/` | Keep these paths; root-level `proposals/` and `adr/` are rejected for this repository because `docs/workflows.md` standardizes RigorLoop artifact locations. |

Logical containers:

- **Project references**: root entry, contribution, source-index, license, and
  safety-routing files.
- **Content corpus**: active source pages, currently split between original
  v0.1 paths and expanded content paths until a migration spec normalizes the
  tree.
- **Expanded static content pages**: path-classified pages under `patterns/`,
  `conditions/`, `principles/`, `programs/`, and `exercises/`.
- **Contribution and license contract**: contributor-facing documentation that
  governs inbound content and media.
- **Red-flags and sources references**: shared Markdown references under
  `about/` and root source indexes, linked from safety-relevant pages.
- **Optional media assets**: original SVGs or approved AI-generated raster
  illustrations referenced from Markdown by relative path.
- **Media provenance index**: one row per AI-generated raster asset, with
  generator, creation notes, license assertion, human review status, media
  purpose, page references, and exact asset path.
- **Tooling and operations**: specs, validation scripts, change-local proof,
  plans, learning records, and optional mdBook configuration.
- **Manual proof records**: change-local evidence under `docs/changes/<change-id>/`
  for semantic source quality, safety boundaries, visual necessity, page review
  metadata, and reader comprehension.
- **Optional mdBook renderer**: derived static HTML output.

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

Expanded static-content authoring and promotion flow:

1. A contributor drafts an expanded page under exactly one path-classified page
   class: `patterns/`, `conditions/`, `principles/`, `programs/`, or
   `exercises/`.
2. The page remains draft-only until checks classify the page class and verify
   required sections, review metadata, source count, source-index references,
   red-flag links where required, media path/provenance rules, and privacy.
3. Maintainers record manual proof under the relevant `docs/changes/<change-id>/`
   directory for semantic source quality,
   non-diagnostic/non-prescriptive language, source support for safety claims,
   visual necessity where media exists, review cadence, and comprehension
   outcomes.
4. A pattern or condition page is promoted only when red-flag routing appears
   before self-management discussion and the proof record confirms the page
   does not diagnose the reader.
5. A program-example page is promoted only when the proof record confirms that
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
- Missing Responsible Breadth page classification, missing page-contract
  sections, missing red-flag routing, weak source quality, missing review
  metadata, or missing manual semantic proof keeps an expanded page draft-only.
- Diagnosis, treatment-plan, rehab-progression, posture-correction promise,
  personalized programming, symptom collection, or injury-specific protocol
  language blocks expanded-page promotion.
- Missing local tools are recorded as validation gaps, not passing results.

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
  indexes, manual proof records, and validation reports are repository source or
  workflow evidence.
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

Source quality and proof:

- Source count is necessary but not sufficient. Expanded pages require the
  source-quality mix defined by page class.
- Source-index validity and page-local source presence remain shared
  Markdown-first checks.
- Semantic source quality, scope-boundary judgment, and claim support require
  manual proof when checks cannot verify them.
- Manual proof records live under the relevant `docs/changes/<change-id>/`
  directory.

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
- Expanded static content validation should identify page class, missing section,
  missing metadata, missing red-flag link, source-count failure, source-index
  failure, excluded-scope failure, media-provenance failure, and privacy failure
  with stable messages.
- Manual proof records identify the page, requirement IDs or acceptance
  criteria checked, files inspected, reviewer/author role, non-identifying
  reader type when comprehension is tested, observed outcome, and residual
  validation gaps.

## Architecture Decisions

- [ADR 2026-06-27: Markdown-first citation-based authority](../../adr/2026-06-27-markdown-first-citation-based-authority.md) - Make Markdown the v0.1 source of truth and use citation-based authority.
- [ADR 2026-06-28: AI-generated raster media provenance](../../adr/2026-06-28-ai-generated-raster-media-provenance.md) - Allow narrow AI-generated raster support assets with centralized provenance.
- [ADR 2026-06-29: Responsible Breadth static content boundaries](../../adr/2026-06-29-responsible-breadth-static-content-boundaries.md) - Add path-classified expanded static content classes with higher-bar proof, red-flag routing, and no runtime personalization.
- [ADR 2026-06-26: Repository-native reviewed content](../../adr/2026-06-26-repository-native-reviewed-content.md) - Superseded structured-platform decision retained as history.

## Quality Requirements

| Quality | Scenario | Measure |
| --- | --- | --- |
| Readability | A beginner opens a first-slice page on GitHub. | The page can be understood without app navigation, generated HTML, or local tooling. |
| Traceability | A reviewer checks a safety warning. | The claim has a page-local citation and source entry. |
| Scope safety | A contributor adds rehab, diagnosis, pain treatment, or advanced lifting content. | The page is blocked before promotion. |
| Media licensing | A page references media. | The media is original or clearly project-licensed and referenced by relative path. |
| Media provenance | A page references an AI-generated raster image. | The image has one approved `media/PROVENANCE.md` row with exact `asset_path`, valid purpose, required fields, and matching `page_refs`. |
| Page classification | An expanded static content page is reviewed. | Its path maps to exactly one page class or the page declares one equivalent class before promotion. |
| Red-flag routing | A pattern or condition page discusses self-management themes. | The page links the red-flags reference before self-management discussion. |
| Source quality | A condition page cites three weak sources. | The page fails until it has the required institutional, guideline, patient-education, or supporting source mix. |
| Prescription boundary | A program example adapts to symptoms or goals. | The page fails promotion as personalized programming. |
| Manual proof | A semantic safety or source-quality claim cannot be automated. | A proof record under the relevant `docs/changes/<change-id>/` directory records the review and outcome. |
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
- Expanded static content source quality and non-prescription boundaries are partly
  semantic and will depend on disciplined manual proof until tooling matures.
- Expanded top-level directories may create navigation sprawl if README and
  SUMMARY promotion gates are not kept strict.
- Red-flag language and review cadence introduce maintenance debt; stale pages
  must be treated as not current when source changes or review dates lapse.
- Path-based page classification is simple for the first expanded slice but may
  need front matter if future content types share directories.
- The current physical tree still mixes three exercise locations and two media
  buckets. That is acceptable as compatibility debt under the current specs but
  should be resolved by a future repository-layout spec before more content is
  scaled.

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
- **Manual proof record**: Change-local Markdown evidence that records semantic
  review results that cannot be fully automated.

## Next artifacts

- Architecture review for this repository-layout view update.
- A future spec/ADR migration for physical directory normalization before
  moving published Markdown paths or media paths.

## Follow-on artifacts

- None for implementation from this architecture update alone. Physical
  directory migration requires a spec amendment, architecture-review approval,
  test-spec updates, and a migration plan.

## Readiness

This architecture package is ready for architecture review for the layout-view
update. It is not implementation-ready for physical directory migration until
the governing specs and ADRs are amended and reviewed.
