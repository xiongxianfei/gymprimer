# Proposal: Per-Exercise Document Best-Practice Image Prioritization

## Status

accepted

This proposal records a cross-exercise content and media direction.
It does not generate images, edit exercise pages, update provenance, or authorize implementation by itself.

## Problem

GymPrimer now has enough exercise documents that page quality depends on consistent exercise-document best practices, not only on one-off page edits.
Some exercise pages already have strong support images for setup, movement, and muscle attention.
Other pages have only a compact sequence image, older section wording, or no broad muscle-attention image even when beginners would benefit from one.

The user specifically clarified that image evaluation should happen for each exercise document, not once across the whole repository.
For a given exercise page, the workflow should list that page's top 10 image candidates, treat the top five as a candidate backlog, and generate only the minimum needed subset when downstream artifacts approve that page-specific image batch.
That goal fits the project only if image generation stays governed by the accepted exercise-image standard, prompt-record ADR, provenance table, visual-safety review, citation-backed Markdown, and beginner-comprehension proof.

GymPrimer needs a durable proposal that defines a repeatable per-document image evaluation process and frames image generation as part of a broader best-practice cleanup, rather than generating images from chat alone.

## Goals

- Improve all current exercise documents against the accepted Markdown-first, citation-backed exercise-page model.
- Evaluate image needs separately for each exercise document.
- Rank the top 10 image candidates inside each exercise document being improved.
- Use the top five ranked images for that exercise document as candidate backlog, not an automatic generation target.
- Preserve the approved exercise-image count policy: pages use the minimum number of images needed, with the current three-image normal limit unless downstream approved artifacts justify a fourth or fifth image.
- Prefer images that fill a real beginner comprehension gap instead of replacing acceptable existing media.
- Keep setup, movement instructions, muscle names, cues, safety notes, and citations in Markdown.
- Keep generated raster images under the accepted prompt-record and `media/PROVENANCE.md` model.
- Preserve text-only validity where an exercise document does not need another image.
- Use calm safety routing without turning exercise pages into medical assessment, treatment, recovery-care protocol, or personalized coaching.

## Non-goals

- No immediate image generation in this proposal.
- No immediate rewrite of all exercise pages.
- No new exercise pages.
- No new media policy beyond the accepted exercise-image standard unless downstream review finds a gap.
- No video, animation, camera form analysis, hosted media service, CMS, database, user accounts, user-input flow, generated public API, or workout planner.
- No borrowed web images, stock photos, commercial screenshots, branded equipment emphasis, identifiable people, or unlicensed media.
- No in-image text, muscle labels, citations, warning badges, correct-or-wrong badges, red pain marks, clinical framing, medical-assessment claims, treatment claims, posture-correction promises, or recovery-care protocols.

## Vision fit

fits the current vision

The current vision says GymPrimer is a Markdown-first beginner primer whose exercise pages explain purpose, setup, muscles involved, movement breakdown, practical feel cues, common mistakes, safety notes, and sources.
This proposal fits that direction by improving exercise documents and images as support assets while keeping Markdown, citations, and safety boundaries as the source of truth.

## Context

The accepted exercise-image proposal, approved exercise-image spec, exercise document image-purposes ADR, and generated raster prompt-record ADR already define the media rules this proposal should use.
New generated raster exercise images use exercise setup, movement, or muscle-attention purposes, require prompt records under `media/prompts/exercises/<exercise-slug>/`, require approved provenance rows in `media/PROVENANCE.md`, and require visual-safety review before promotion.

The current `exercises/` directory contains a mix of newer pages with setup, movement, and muscle-attention images, and older or simpler pages with one sequence image.
The best near-term opportunity is not to create one repository-wide top-10 image list.
It is to apply the same evaluation model to each exercise document, choose that page's most useful image candidates, and then audit page wording, alt text, provenance, safety routing, and source support in page-sized or small-batch slices.

## Options Considered

### Option A: Generate the top five images immediately from chat

This would satisfy the visible image request quickly.

Advantages:

- Fastest visible output.
- Gives users more exercise visuals immediately.

Drawbacks:

- Conflicts with the repository rule that generated output and media-source changes need durable downstream artifacts first.
- Skips prompt records, provenance rows, visual-safety review, and validation planning.
- Risks creating images that cannot be promoted into the Markdown corpus.

Disposition: rejected.

### Option B: Use one repository-wide top-10 image list

This would rank the ten most valuable image candidates across all exercise documents.

Advantages:

- Easy to summarize.
- Gives maintainers a single first queue.

Drawbacks:

- Does not respect the user's clarified intent.
- Helps some exercise pages while leaving other page-specific image needs unevaluated.
- Can over-prioritize common exercises and under-prioritize pages where a full image set is needed for comprehension.

Disposition: rejected.

### Option C: Rank the top 10 image candidates per exercise document and generate the minimum needed subset through governed page-specific slices

This keeps the user's image-first improvement goal, but routes the actual image generation through spec, plan, test, provenance, prompt-record, and review artifacts.

Advantages:

- Preserves the user's top-10 and top-five intent for each exercise document.
- Focuses generation on each page's largest beginner comprehension gaps.
- Keeps the work reviewable and reversible.
- Avoids a repository-wide ranking that hides page-specific needs.

Drawbacks:

- Slower than direct image generation.
- Requires careful page-by-page ranking and downstream proof before assets are added.
- May need explicit downstream justification when a page-specific top-five batch exceeds the usual exercise-image count preference.

Disposition: recommended.

### Option D: Pause image work and do only text cleanup

This would improve consistency without media risk.

Advantages:

- Lowest media governance burden.
- Useful for older exercise pages with section drift.

Drawbacks:

- Does not satisfy the user's clear image-improvement request.
- Leaves high-value visual gaps in beginner-facing exercise documents.

Disposition: rejected as the primary direction.

## Recommended Direction

Choose Option C.

GymPrimer should run a governed exercise-document improvement initiative that audits each current `exercises/*.md` page, uses fewer than five existing images as an evaluation trigger, ranks image gaps inside each selected page, and generates only the minimum page-specific image set approved by downstream artifacts.
The work should improve exercise pages as Markdown documents first, with images used only where they solve setup, movement, or broad muscle-attention confusion.

### Ranking criteria

Each image candidate is scored from 1 to 5 on five criteria.

| Criterion | Meaning |
|---|---|
| Beginner comprehension | The image explains something text alone does not explain well. |
| Safety/setup value | The image reduces setup, range, posture, or equipment confusion without medical framing. |
| Muscle-attention value | The image helps beginners understand broad regions to notice. |
| Page value | The image supports several sections of the same exercise page. |
| Readiness | The image can be generated, reviewed, cited in nearby Markdown, and validated without expanding scope. |

Maximum score: 25.

### Per-exercise top 10 candidate model

Each exercise document selected for improvement should receive its own top-10 candidate table.
The table should rank images only for that page.
Documents with fewer than five existing images are the first evaluation set.
This threshold is an evaluation trigger, not a requirement to bring every page to five images.
The first five ranked candidates form a page-specific candidate backlog.
Generation should select the minimum needed subset from that backlog, subject to downstream spec, plan, validation, visual-safety review, and the approved exercise-image count policy.

| Rank | Candidate image | Page section supported | Purpose | Why it matters | Score | Disposition |
|---:|---|---|---|---|---:|---|
| 1 | Highest-value image for this exercise document | Setup, movement, muscles, feel cues, common mistakes, or safety notes | `exercise_setup_illustration`, `exercise_movement_illustration`, or `exercise_muscle_attention_illustration` | Explains the largest beginner comprehension gap for this page. | 1-25 | First generation candidate |
| 2 | Second-highest-value image for this exercise document | Page-specific section | Accepted exercise-image purpose | Supports a distinct page need that image 1 does not cover. | 1-25 | First generation candidate when needed |
| 3 | Third-highest-value image for this exercise document | Page-specific section | Accepted exercise-image purpose | Adds necessary setup, movement, or broad attention context. | 1-25 | First generation candidate when needed |
| 4 | Fourth-highest-value image for this exercise document | Page-specific section | Accepted exercise-image purpose | Helps the page explain a distinct beginner confusion point. | 1-25 | Exception candidate when justified |
| 5 | Fifth-highest-value image for this exercise document | Page-specific section | Accepted exercise-image purpose | Completes the first useful visual set for this page. | 1-25 | Exception candidate when justified |
| 6-10 | Later candidates for this same exercise document | Page-specific sections | Accepted exercise-image purposes | Useful but lower priority than the first five. | 1-25 | Later candidate |

The proposal intentionally does not choose one repository-wide top-five image batch.
Downstream artifacts should select all exercise documents with fewer than five images as the evaluation population, then fill the concrete top-10 table for each selected page.
If an exercise document already has sufficient images, its top-10 evaluation can record that no generation is needed and justify text-only or low-image treatment.

### Slice decisions

The first slice should use five ranked candidates as the default evaluation cap for each selected exercise document.
This proposal does not revise the existing exercise-image standard's normal image-count policy.
Generated images should normally keep the final page within the current zero-to-three image range.
A fourth or fifth image should be allowed only when downstream approved artifacts record page-specific justification under the existing exercise-image standard.
Images beyond the top five should be deferred unless a downstream approved spec or plan records why delaying a tightly related candidate would create worse churn.

Older sequence images should be preserved unless the owning page is being touched and the audit finds a concrete problem.
Replacement or normalization should be justified by a clear issue such as unsafe visual implication, missing required provenance or prompt record, alt text that cannot be corrected without asset change, misleading common-mistake framing, incompatible purpose, low readability, or duplicate coverage after better images are added. [Source][local-2026-07-06-exercise-document-best-practice-image-prioritization-exercise-image-standard]
Style consistency alone is not enough reason to replace an older sequence image.

The first slice should record audit criteria in a change-local proof artifact.
The exercise template should be updated only after the first slice proves that the criteria are stable and reusable.

Pull requests will be merged only after the author reviews and agrees with the PR.
This proposal does not add new PR-review rules.
Generated image promotion remains governed by the existing exercise-image standard, provenance contract, and visual-safety review requirements.

## Expected Behavior Changes

After downstream artifacts are approved and implemented:

- Exercise-document audits will identify missing or weak best-practice elements for each selected exercise page before page edits are made.
- Every exercise document with fewer than five images will enter the first evaluation population.
- Each selected exercise document will have its own top-10 image-candidate evaluation.
- The top five ranked candidates will be a candidate backlog, not an automatic generation target.
- The first image slice will generate only the minimum needed subset for a selected exercise document, preserving the current three-image normal limit unless downstream approved artifacts justify a fourth or fifth image.
- New generated images will have prompt records, provenance rows, meaningful alt text, and nearby Markdown support.
- Existing acceptable images will remain unless a page-specific audit records a reason to replace them.
- Older sequence images will not be replaced for style alone.
- Exercise pages will become more consistent in purpose, setup, muscle guidance, movement breakdown, feel cues, common mistakes, easier and harder versions, safety notes, sources, and image support.
- Text-only pages or pages with fewer images will remain acceptable when the audit finds no additional image is needed.

## Architecture Impact

Expected downstream impact is mostly within existing media and Markdown validation surfaces.

| Surface | Expected change |
|---|---|
| Existing exercise-image spec | May need an amendment or companion spec for per-exercise-document image prioritization and broad exercise-document audit criteria. |
| Existing media ADRs | Likely no new architecture if current prompt-record and provenance decisions cover the first slice. |
| `docs/templates/exercise-card.md` | May need clearer optional image placement guidance if the audit finds section-level inconsistency. |
| `media/exercises/<exercise-slug>/` | Adds page-specific generated image files after approval. |
| `media/prompts/exercises/<exercise-slug>/` | Adds exact prompt records for generated raster images. |
| `media/PROVENANCE.md` | Adds approved rows for generated raster images. |
| Validation tooling and tests | May need fixtures for page-specific top-five image references, prompt records, provenance rows, alt text, and audit evidence. |
| Change-local evidence | Needs page audit criteria, visual-safety review, source audit, beginner-comprehension proof, and rollback proof for the image batch. |

This proposal does not add a new runtime, hosted service, database, CMS, generated public JSON path, or user-input feature.

## Testing and Verification Strategy

Automated checks should cover the existing exercise-image requirements for the new assets:

- local relative image paths;
- images under `media/exercises/<exercise-slug>/`;
- valid exercise image purpose values;
- no more than one muscle-attention image per exercise page;
- generated raster provenance rows with approved review status;
- prompt-record presence and reverse asset-path match;
- `page_refs` matching the referencing exercise document;
- meaningful alt text;
- privacy and no-secrets scans.

Manual proof should cover:

- visual-safety review for each generated image;
- source audit confirming nearby Markdown supports muscle and cue language;
- beginner-comprehension check for each edited page;
- rollback proof showing each page remains usable if the new image reference is removed.

Local completion reports should name the exact validation commands run.
CI should not be claimed unless a CI run is observed.

## Rollout and Rollback

Rollout should use small slices.

First, downstream artifacts should confirm the audit criteria and identify all exercise documents with fewer than five images as the evaluation population.
Then each selected exercise document should receive its own top-10 image evaluation.
The first implementation slice should choose one selected exercise document or a deliberately small page batch, generate only the minimum needed subset from each page's top-five candidate backlog, add prompt records and provenance rows, edit only the affected pages, and collect review evidence.
Later slices can handle candidates 6-10 for that page, top-five candidate backlogs for additional exercise documents, and any text-only best-practice cleanup found by the audit.

Rollback is additive.
If an image fails review or validation, remove the Markdown image reference, remove the unused asset and prompt record, remove or revise the provenance row, and keep the exercise page readable in text form.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Generated images imply exact anatomy or muscle activation. | Keep muscle-attention images broad, unlabeled, and supported by nearby Markdown. |
| Image work crowds out citation-backed exercise education. | Require page audit and source review before promotion. |
| Top-five candidate ranking becomes broad page rewrite. | Limit implementation slices to one selected exercise document or a deliberately small page batch. |
| Existing acceptable images get replaced for style alone. | Treat replacement as later-candidate work that needs page-specific justification. |
| Image prompts or review notes leak private or unsafe content. | Use repository-local prompt records with privacy review and explicit redaction notes when needed. [Source][local-2026-07-06-exercise-document-best-practice-image-prioritization-constitution] [Source][local-2026-07-06-exercise-document-best-practice-image-prioritization-exercise-image-standard] |
| Pages exceed the accepted image-count guidance. | Treat fewer than five images as an evaluation trigger only, keep one muscle-attention image per page, and require downstream justification for any page exceeding three exercise images. |
| Visuals imply coaching, medical assessment, treatment, or recovery-care programming. | Apply the existing non-clinical visual-safety criteria and keep safety routing in Markdown. [Source][local-2026-07-06-exercise-document-best-practice-image-prioritization-exercise-image-standard] |

## Open Questions

None for proposal review.
The user resolved the initial open questions: evaluate all exercise documents with fewer than five images; treat the top five as the page-specific candidate backlog rather than an automatic generation target; preserve older sequence images unless page-local audit justifies replacement; record first-slice audit criteria change-locally before changing the exercise template; and rely on existing PR author review before merge without adding new PR-review rules.

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-06 | Drafted a cross-exercise best-practice and image-prioritization proposal. | The user requested top-10 image ranking, top-five generation, and all-exercise document improvement. | Direct generation from chat; regenerate all images; text-only cleanup. |
| 2026-07-06 | Revised the direction from one repository-wide top-10 list to per-exercise-document top-10 evaluations. | The user clarified that evaluation is for each exercise document instead of the whole repository. | Repository-wide top-10 ranking. |
| 2026-07-06 | Resolved open questions for first-slice selection, slice size, older sequence images, audit evidence, and human review. | The user selected all documents with fewer than five images, adopted top-five candidate ranking, chose change-local audit proof first, and stated that the PR author will review and agree before merge. | Leaving these as open questions for proposal review. |
| 2026-07-06 | Revised five-image language after proposal review. | PR-EDIP-001 found that "five" could override the approved three-image normal limit; the owner chose not to revise the exercise-image count policy. | Treating five images as an automatic page target. |
| 2026-07-06 | Removed proposal-specific PR-review rule language. | The owner clarified that PRs merge only after author review and agreement, so this proposal should not add new PR-review rules. | Adding a new PR author review rule in this proposal. |
| 2026-07-06 | Accepted the proposal after proposal-review R2. | The owner approved the proposal after PR-EDIP-001 and PR-EDIP-002 were resolved and proposal-review R2 recorded approval. | Keeping the proposal in draft status. |

## Initial Intent Preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| List top 10 images for each exercise document | in scope | Recommended Direction |
| Generate at least the top five images for the selected exercise document | deferred follow-up | Revised by later owner decision: the top five are a candidate backlog, and generation uses the minimum needed subset under the approved image-count policy. |
| Improve all exercise documents | in scope | Problem; Goals; Expected Behavior Changes |
| Follow best practices | in scope | Context; Testing and Verification Strategy; Risks and Mitigations |
| Make exercise documents good for users | in scope | Problem; Goals; Ranking criteria |
| Evaluate each exercise document instead of the whole repository | in scope | Problem; Options Considered; Recommended Direction; Decision Log |
| Select all documents that do not have five images | in scope | Recommended Direction; Rollout and Rollback; Decision Log |
| Treat fewer than five images as evaluation trigger, not generation target | in scope | Recommended Direction; Expected Behavior Changes; Decision Log |
| Keep existing exercise-image count policy | in scope | Goals; Recommended Direction; Risks and Mitigations; Decision Log |
| Preserve older sequence images unless page-local audit justifies replacement | in scope | Recommended Direction; Expected Behavior Changes; Decision Log |
| Use change-local audit proof before updating the template | in scope | Recommended Direction; Architecture Impact; Decision Log |
| Have the author review and agree before PR merge | in scope | Recommended Direction; Decision Log |

## Scope Budget

| Work item | Treatment | Reason |
|---|---|---|
| Cross-exercise best-practice audit | core to this proposal | Needed to improve all exercise documents without treating images as isolated assets. |
| Per-exercise-document top-10 image ranking | core to this proposal | Directly preserves the user's clarified request. |
| Evaluate all documents with fewer than five images | core to this proposal | User selected this population for the first page-specific evaluation pass; it is an evaluation trigger, not a generation target. |
| Page-specific top-five candidate backlog | core to this proposal | The top-five list ranks possible images for each selected page without requiring all five to be generated. |
| Page-specific generated image subset | first-slice candidate | Generation should happen only after downstream spec, plan, tests, prompt records, provenance, and reviews are ready, and should use the minimum needed images under the approved image-count policy. |
| Candidates 6-10 for a selected exercise document | separate implementation slice | Useful after that page's first batch proves the workflow. |
| Additional exercise documents | separate implementation slice | Each page needs its own evaluation, proof, and rollback path. |
| Existing image replacement for style consistency | out of scope | Older sequence images should not be replaced for style alone. |
| Exercise template clarification | deferable follow-up | First slice should prove criteria in a change-local proof artifact before template changes. |
| Validation tooling updates | same-slice dependency | Needed if current checks do not cover the first-slice proof obligations. |
| New exercise pages | out of scope | The user asked to improve exercise documents, not expand inventory. |
| Hosted app, video, or planner features | out of scope | Conflicts with the current Markdown-first product boundary. |

## Next Artifacts

- Proposal review for `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`.
- Spec or spec amendment for per-exercise-document audit criteria, the first selected document set, top-five candidate backlogs, and any page-specific four- or five-image exceptions.
- Architecture assessment confirming whether existing media ADRs cover this slice.
- Execution plan for page-specific minimum-needed generation from each top-five candidate backlog, prompt records, provenance rows, page edits, review evidence, and rollback.
- Test spec for validation and manual proof obligations.

## Follow-on Artifacts

None yet

## Readiness

Ready for proposal review.
Not ready for image generation, exercise-page edits, implementation planning, or verification until downstream artifacts are reviewed in source-of-truth order.

## Sources

- `CONSTITUTION.md`
- `VISION.md`
- `specs/exercise-image-standard.md`
- `docs/adr/2026-07-03-exercise-document-image-purposes.md`
- `docs/adr/2026-07-03-generated-raster-prompt-records.md`

[local-2026-07-06-exercise-document-best-practice-image-prioritization-constitution]: ../../CONSTITUTION.md
[local-2026-07-06-exercise-document-best-practice-image-prioritization-vision]: ../../VISION.md
[local-2026-07-06-exercise-document-best-practice-image-prioritization-exercise-image-standard]: ../../specs/exercise-image-standard.md
[local-2026-07-06-exercise-document-best-practice-image-prioritization-exercise-image-purposes-adr]: ../adr/2026-07-03-exercise-document-image-purposes.md
[local-2026-07-06-exercise-document-best-practice-image-prioritization-prompt-records-adr]: ../adr/2026-07-03-generated-raster-prompt-records.md
