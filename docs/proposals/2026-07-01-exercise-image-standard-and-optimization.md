# Proposal: Exercise Image Standard and Exercise Document Optimization

## Status

accepted

This proposal records a product and content-governance direction. It does not authorize image generation, checker changes, provenance changes, exercise-page edits, README promotion, or implementation handoff until proposal review and downstream artifacts approve the direction.

## Problem

GymPrimer now has enough exercise pages that inconsistent visual support can become a quality problem. Some exercise pages already have provenance-backed images, while newer forward-head support exercise pages have no images. The current media-purpose vocabulary distinguishes equipment identification, key movement, pattern alignment, anatomical-region context, and compact exercise previews, but it does not clearly distinguish setup, full exercise movement, and muscle-attention images for exercise documents.

Beginners often need visual anchors to understand equipment or body-position setup, start and end positions, movement path, and the broad muscle region they should notice during an exercise. At the same time, exercise images can mislead readers if they imply diagnosis, correction, treatment, exact anatomy, unsupported technique, or personalized coaching. Prior review history also shows that exercise-specific claims need page-local source support; setup and technique claims cannot rely only on broad or indirect sources.

GymPrimer needs a durable exercise-image standard before generating or adding more exercise-document images.

## Goals

- Define a reusable exercise-image standard for current and future exercise documents.
- Keep image use intentional, with each image teaching one clear thing.
- Allow multiple images when beginner comprehension needs distinct setup, movement, or muscle-attention support.
- Add exercise-specific media-purpose vocabulary for setup, movement, and muscle attention.
- Keep images subordinate to Markdown text, citations, safety routing, and alt text.
- Keep muscle names, cues, safety notes, and citations in Markdown, not in the image.
- Preserve the Markdown-first, citation-backed, non-clinical product shape.
- Optimize current `exercises/*.md` pages over time under one proposal, with small downstream delivery loops instead of separate proposals for each small batch.

## Non-goals

- No immediate image generation.
- No immediate rewrite of all exercise pages.
- No decorative image library, stock-photo collection, video, animation, camera form analysis, hosted media service, runtime app, database, CMS, user-input flow, generated public JSON, or website delivery path.
- No in-image text, muscle labels, citations, safety notes, warning badges, or long visual instructions.
- No red pain marks, injury symbols, correct-or-wrong badges, before-or-after cure framing, diagnosis framing, posture-correction promises, treatment plans, or rehabilitation protocols.
- No claim that generated images are evidence for anatomy, technique, safety, diagnosis, treatment, or programming.
- No README promotion change from this proposal alone.
- No new exercise pages.
- No pattern-page, condition-page, video, animation, or hosted visual-delivery standard.

## Vision fit

fits the current vision

The current vision says GymPrimer is a Markdown-first beginner primer whose exercise pages explain purpose, setup, muscles involved, movement breakdown, practical feel cues, common mistakes, safety notes, and sources. It also says the repository remains the primary product and rejects coaching, diagnosis, treatment, hosted-app dependence, and media as a source of truth. This proposal fits that direction by treating images as optional support assets for Markdown exercise pages, not as clinical guidance or standalone instruction.

The direction still depends on downstream specification, architecture or ADR confirmation where needed, tests, review, and verification before any exercise image or validator change can rely on it.

## Context

The current repository already has an accepted Markdown-first spec, Responsible Breadth spec, AI-generated raster provenance ADR, and expanded raster media-purpose ADR. Those artifacts establish several constraints that this proposal should preserve.

First, Markdown remains the source of truth. Exercise setup, muscles, feel cues, common mistakes, safety notes, and sources belong in the Markdown page, with page-local citations where the claim needs support.

Second, generated raster media uses centralized provenance in `media/PROVENANCE.md`. The existing ADR classifies raster media deterministically by file extension before provenance lookup, and the checker can match a Markdown image reference to a provenance row by exact normalized `asset_path`.

Third, expanded visual purposes already exist for pattern alignment, condition anatomical-region context, and compact exercise previews. Full exercise documents need a clearer purpose vocabulary because setup images, movement images, and muscle-attention images have different teaching and review risks.

Fourth, prior forward-head support work kept exercise images out of that same slice. This proposal provides a governed path for adding exercise-document visuals later without merging policy, validation, provenance, generation, and page edits into one broad change.

## Options considered

### Option A: Generate images directly for the current forward-head support exercises

This would quickly improve the current image gap.

Advantages:

- Fastest visible improvement.
- Solves a concrete exercise-page gap.

Drawbacks:

- Skips the governed media-purpose and provenance path.
- Risks inconsistent image types.
- Makes review harder because policy, checker, provenance, and assets would change together.

Disposition: rejected as the primary approach.

### Option B: Create separate proposals for setup images, movement images, and muscle-attention images

This would split the standard by image type.

Advantages:

- Very small proposal units.
- Each proposal is easy to review in isolation.

Drawbacks:

- Creates governance overhead.
- Fragments one exercise-image standard.
- Forces downstream artifacts to reconcile overlapping decisions.

Disposition: rejected.

### Option C: One exercise-image standard proposal, multiple downstream delivery loops

This proposal defines the standard once, then downstream specs, tests, architecture amendments, and implementation plans can split delivery into small reviewable loops.

Advantages:

- Keeps the product decision coherent.
- Matches the preference to do one thing in one loop.
- Avoids separate proposals for small exercise-page batches.
- Allows small implementation changes with focused rollback.

Drawbacks:

- Requires careful downstream planning.
- The proposal covers all exercise documents, but implementation should not happen all at once.

Disposition: recommended.

### Option D: Keep exercise pages text-only

This avoids media governance complexity.

Advantages:

- Lowest media risk.
- Simplest validation path.

Drawbacks:

- Fails beginner comprehension needs for setup, movement path, and muscle attention when text alone is insufficient.
- Ignores prior reader feedback showing that pictures can improve comprehension, while still needing better per-page evidence.

Disposition: rejected.

## Recommended direction

Choose Option C: one exercise-image standard proposal, delivered through multiple small downstream loops.

The proposal owns one coherent product decision:

> Exercise documents should use a governed visual system where each image teaches one specific concept: setup, movement, or muscle attention.

The standard should allow zero to three images per exercise page depending on comprehension need:

| Image count | Use case |
|---:|---|
| 0 | Text is enough. |
| 1 | One setup, movement, or muscle-attention image solves the main comprehension gap. |
| 2 | Two distinct concepts need visual support, such as setup plus movement. |
| 3 | Setup, movement, and muscle attention are all independently useful and cannot be merged cleanly. |
| 4+ | Outside normal scope and should need explicit downstream justification. |

Most exercise pages should use zero to two images. Three should be reserved for pages where each image has a distinct teaching purpose.

Each generated raster exercise image should have one declared purpose:

| Purpose | Meaning | Example |
|---|---|---|
| `exercise_setup_illustration` | Shows equipment setup, grip, stance, bench, wall, floor, or body relationship. | Lat pulldown seat and thigh-pad setup. |
| `exercise_movement_illustration` | Shows start or end position, key position, or movement path. | Wall slide start and finish. |
| `exercise_muscle_attention_illustration` | Highlights the main muscle or body region to notice. | Band pull-apart upper-back and rear-shoulder region. |

Vague purposes such as `exercise_image`, `fitness_picture`, or `general_diagram` should stay out of the standard. Existing `key_movement_illustration` assets can remain legacy-compatible and migrate only when the owning page is otherwise touched for media, alt text, provenance, or content reasons.

Muscle-attention images should be allowed but limited. A page should have at most one `exercise_muscle_attention_illustration`. The image should highlight broad regions rather than precise anatomy, use subtle highlight, outline, or contrast, avoid in-image muscle names, and rely on nearby Markdown for muscle names, feel cues, caveats, and citations.

Exercise images should not contain muscle labels, correct-or-wrong labels, citations, safety warnings, arrows with text, long cues, diagnosis claims, or treatment claims. Markdown carries the explanation because it is searchable, translatable, citable, accessible, and easier to validate.

Exercise visuals should remain neutral and non-clinical. They should avoid red pain marks, injury symbols, bad-versus-fixed framing, before-or-after cure framing, medical diagrams, pathology emphasis, branded equipment, identifiable people, private environments, exaggerated deformity, and shame-based posture comparison.

The expected media path pattern is:

```text
media/exercises/<exercise-slug>/<purpose>.png
```

Generated raster images should continue to use `media/PROVENANCE.md` with stable fields including `asset_path`, `asset_type`, `media_purpose`, `generator`, `prompt_or_creation_notes`, `created_date`, `human_reviewer`, `license_assertion`, `source_inputs`, `review_status`, `page_refs`, and `notes`. The `human_reviewer` value should identify an accountable human maintainer or GitHub handle, not an AI tool.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Generate a revised proposal based on the current proposal | in scope | Full proposal |
| Follow best practices | in scope | Recommended direction; Testing and verification strategy; Risks and mitigations |
| Do one thing in one loop | in scope | Recommended direction; Rollout and rollback |
| Avoid creating separate proposals for small pieces | in scope | Options considered; Recommended direction; Rollout and rollback |
| Split into more implementation loops if the work is not too big | in scope | Recommended direction; Rollout and rollback; Next artifacts |
| Define exercise-image standard | in scope | Goals; Recommended direction |
| Allow more than one image when needed | in scope | Recommended direction |
| Include muscle-attention visuals | in scope | Recommended direction |
| Optimize all exercise documents | in scope | Scope budget; Rollout and rollback |
| Keep image generation governed by provenance | in scope | Recommended direction; Architecture impact; Testing and verification strategy |
| Avoid unsafe or clinical image framing | in scope | Non-goals; Recommended direction; Risks and mitigations |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Exercise-image quality standard | core to this proposal | Main product decision. |
| Exercise-specific media-purpose vocabulary | core to this proposal | Needed to distinguish setup, movement, and muscle-attention images. |
| Image-count policy | core to this proposal | Controls clarity without overloading pages. |
| Muscle-attention image rule | core to this proposal | Addresses beginner need to understand broad target regions without overprecise anatomy. |
| Provenance requirements | same-slice dependency | Generated raster media must remain traceable and reviewable. |
| Alt-text standard | same-slice dependency | Images must be accessible and meaningful. |
| Checker and test updates for media purposes | same-slice dependency | Needed before page edits can be validated. |
| All exercise-page audit | core to this proposal | The standard applies to all current `exercises/*.md` pages over time. |
| Image generation for needed pages | separate implementation slice | Generation should happen only after standard, spec, tests, and provenance rules are accepted. |
| Five forward-head support exercise images | first-slice candidate | Clear current gap and suitable first content batch after validation vocabulary is accepted. |
| Existing image normalization | separate implementation slice | Useful, but lower priority than defining and proving the standard. |
| Remaining exercise-page optimization | separate implementation slice | Apply the standard incrementally. |
| README promotion | out of scope | This proposal improves exercise documents, not navigation promotion. |
| Hosted image delivery or web app | out of scope | GymPrimer remains Markdown-first. |
| New exercise pages | out of scope | This proposal improves image standards, not exercise inventory. |
| Pattern or condition illustration rules | separate proposal | Related but not identical to full exercise-document images. |

## Expected behavior changes

After this proposal is accepted and downstream artifacts are implemented:

- Exercise pages can include zero, one, two, or three images depending on beginner comprehension need.
- Every exercise image has a declared teaching purpose.
- New full exercise-document images can use `exercise_setup_illustration`, `exercise_movement_illustration`, or `exercise_muscle_attention_illustration`.
- Images live under `media/exercises/<slug>/` and use relative Markdown references.
- Images have meaningful alt text and nearby Markdown support.
- Generated raster images have exact approved `media/PROVENANCE.md` rows.
- Exercise Markdown remains the source of truth for setup, movement, muscles, feel cues, mistakes, safety notes, and sources.
- Images do not contain labels, safety claims, warning text, citations, or unsupported anatomy claims.
- Existing compatible image purposes remain valid until touched.

## Architecture impact

Expected downstream impact:

| Surface | Expected change |
|---|---|
| Focused exercise-image spec or Responsible Breadth amendment | Define exercise-image purposes, image-count policy, provenance behavior, alt-text rules, and visual-safety boundaries. |
| `specs/markdown-first-primer.md` | Update only if shared media rules need compatibility notes. |
| `docs/architecture/system/architecture.md` | Confirm exercise images within the Markdown-first media system and current raster/SVG classification behavior. |
| AI-raster media ADRs | Amend only if the current ADRs do not already cover the new exercise-document purpose values. |
| `docs/templates/exercise-card.md` | Add optional image block guidance if the template exists and owns exercise-page structure. |
| `tools/checks/check_markdown_first.py` | Accept new purpose values and reject purpose/page-class mismatches after the spec and tests define them. |
| `media/PROVENANCE.md` | Add rows for generated raster assets only when assets are introduced. |
| Tests and fixtures | Cover valid and invalid image purposes, missing provenance, missing alt text, and media path errors. |

This proposal does not introduce a new runtime, database, hosted service, generated JSON path, CMS, or user-input feature.

## Testing and verification strategy

Automated validation should likely cover:

- image paths are relative and repository-local;
- exercise images live under `media/exercises/<slug>/`;
- referenced files exist;
- raster images have exact provenance rows;
- provenance rows have required fields;
- `review_status` is approved;
- `page_refs` includes the referencing page;
- media purpose is allowed for exercise pages;
- alt text is present and avoids generic placeholders;
- remote images are rejected;
- unsupported media extensions are rejected;
- deterministic unsafe wording in alt text or captions is rejected where feasible;
- privacy scans pass over Markdown and provenance records.

Manual visual review should likely cover:

- the image teaches exactly one concept;
- setup and movement visuals match the page text;
- muscle highlighting is subtle and not overprecise;
- no in-image text appears;
- no brand marks or identifying people appear;
- no diagnosis, cure, injury, pain, or before-or-after implication appears;
- color is not the only communication method;
- the image does not introduce a claim unsupported by Markdown.

For major exercise-image batches, beginner comprehension evidence should check whether the images improve understanding of purpose, setup or body position, movement steps, what to notice or feel, stop condition, and source verification. Prior read-test feedback that pictures helped is useful context, but future evidence should record per-page comprehension outcomes.

## Rollout and rollback

Rollout should use one accepted proposal with multiple small downstream delivery loops. The exact milestone order belongs in the implementation plan, but the proposal recommends separating at least these concerns: purpose vocabulary and validation, the first exercise content batch, existing image normalization, and the remaining exercise-page audit.

The first content batch can reasonably start with:

- `exercises/chin-nod.md`
- `exercises/thoracic-extension.md`
- `exercises/wall-slide.md`
- `exercises/prone-y-t.md`
- `exercises/band-pull-apart.md`

Those pages are a good first candidate because they are a clear current gap and have already been subject to source-support review. A new proposal should be needed only if the project expands beyond full exercise-document images, such as pattern-page visuals, condition-page anatomy diagrams, videos, animations, user-submitted media, or hosted visual delivery.

Rollback is simple because images are additive. If an image fails review, remove the Markdown image reference, remove the asset, remove or revise the provenance row, keep the text-only page, and rerun checks. If a new purpose value proves too broad, stop using it in new pages and revise the spec or checker through a focused follow-up.

## Risks and mitigations

| Risk | Impact | Mitigation |
|---|---:|---|
| Images imply diagnosis, cure, or correction | High | Ban clinical framing, pain marks, before-or-after visuals, and correction promises. |
| Images become source of truth for technique | High | Keep Markdown authoritative and reject images that introduce unsupported claims. |
| Too many images make pages noisy | Medium | Default to fewer images and require a distinct teaching purpose for each image. |
| Muscle highlights become misleading | Medium | Highlight broad regions only and keep anatomy names and citations in Markdown. |
| Provenance drifts from assets | High | Validate exact `asset_path`, `page_refs`, purpose, review status, and required fields. |
| Existing images create migration churn | Medium | Keep legacy-compatible purposes until an owning page is touched. |
| First implementation PR becomes too large | High | Use multiple downstream delivery loops under one proposal. |
| Static checks miss visual semantics | Medium | Require manual visual-safety review. |
| Alt text becomes generic | Medium | Add generic-placeholder checks and manual review. |
| Source-support problems reappear near images | High | Keep source-supported Markdown near images and do not let images carry claims. |

## Open questions

None blocking proposal review.

Downstream spec, test-spec, architecture, or plan work should resolve:

- exact fixture names;
- exact checker error codes;
- exact first-batch image prompts;
- exact reviewer handle format;
- exact Markdown image block template;
- whether the exercise-specific purposes amend Responsible Breadth, Markdown-first, or a focused exercise-image spec.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-01 | Use one proposal for the exercise-image standard. | The standard is one coherent product decision. | Separate proposals per image purpose or exercise batch. |
| 2026-07-01 | Use multiple downstream delivery loops under the same proposal. | Controls change size without fragmenting governance. | One large PR for all exercise pages; one proposal per batch. |
| 2026-07-01 | Allow zero to three images per exercise page. | Some pages need more than one image, but image bloat should be controlled. | Strict one-image cap; unlimited images. |
| 2026-07-01 | Add setup, movement, and muscle-attention image purposes. | Current purpose vocabulary is too coarse for full exercise-document images. | Reuse only `key_movement_illustration`. |
| 2026-07-01 | Limit muscle-attention images to one per page. | Prevents anatomy overload and misleading precision. | Multiple muscle overlays per page. |
| 2026-07-01 | Keep labels, cues, warnings, and citations in Markdown. | Markdown is searchable, accessible, translatable, and verifiable. | Put muscle names or correctness labels in the image. |
| 2026-07-01 | Keep existing `key_movement_illustration` assets legacy-compatible. | Avoids low-value migration churn. | Immediate migration of all existing media purposes. |

## Next artifacts

1. Proposal review for governance dependencies, scope, and readiness.
2. Focused spec or spec amendment for exercise-image purposes, image-count policy, provenance obligations, alt-text rules, and visual-safety boundaries.
3. Test spec mapping media-purpose validation, provenance validation, alt-text validation, manual visual review, and beginner comprehension evidence.
4. Architecture or ADR update only if the current media architecture and ADRs do not already cover exercise-document image purposes.
5. Implementation plan that sequences small loops after the spec, test-spec, and any required architecture work are approved.

## Follow-on artifacts

- Proposal review: `docs/changes/exercise-image-standard-and-optimization/reviews/proposal-review-r1.md`

## Readiness

This proposal is ready for proposal review.

It is not ready for spec, planning, image generation, checker changes, or exercise-page edits until proposal review confirms the scope and downstream artifact path. The most important principle is to keep one proposal for the coherent exercise-image standard, then use small downstream loops to deliver it safely.
