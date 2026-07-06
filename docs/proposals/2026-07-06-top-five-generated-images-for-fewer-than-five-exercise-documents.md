# Proposal: Top-Five Generated Images for Fewer-Than-Five Exercise Documents

## Status

accepted

This proposal records an accepted policy revision.
It does not authorize image generation, page edits, prompt records, provenance rows, or implementation by itself.

## Problem

GymPrimer has eighteen current exercise documents with fewer than five images.
The recently accepted exercise-document image prioritization workflow treats fewer-than-five image count as an evaluation trigger, treats each page's top five candidates as backlog, and generates only a minimum-needed subset.

The user now wants a stronger media-completion direction: generate the top five high-quality images for every listed exercise document in the fewer-than-five population.
That request conflicts with the current accepted proposal and approved spec unless the project deliberately revises the exercise-image count policy and the top-five backlog policy first.

The project needs a durable decision artifact that records the tradeoff before any generated raster assets are produced.

## Goals

- Decide whether GymPrimer should revise the current exercise-image policy so the listed fewer-than-five exercise documents are allowed to target five images per page.
- Preserve the user's requested included population:
  `exercises/band-pull-apart.md`, `exercises/bird-dog.md`, `exercises/brisk-walking.md`, `exercises/chest-press.md`, `exercises/chin-nod.md`, `exercises/dead-bug.md`, `exercises/glute-bridge.md`, `exercises/hip-hinge.md`, `exercises/incline-push-up.md`, `exercises/kneeling-hip-flexor-stretch.md`, `exercises/lat-pulldown.md`, `exercises/plank.md`, `exercises/prone-y-t.md`, `exercises/rowing-machine.md`, `exercises/seated-row.md`, `exercises/tai-chi-basics.md`, `exercises/thoracic-extension.md`, and `exercises/wall-slide.md`.
- Preserve the user's requested exclusion of `exercises/baduanjin-basics.md` because it already has five images.
- Keep each exercise document's top-five image set page-specific rather than using one repository-wide top-five list.
- Keep generated images as support assets for setup, movement, and one broad muscle-attention purpose, not as the source of truth for technique, anatomy, safety, or programming.
- Keep prompt records, provenance rows, alt text, source support, privacy checks, and rollback proof for every promoted generated image.
- Remove repository-local human-reviewer, review-owner, visual-safety-review evidence, and replacement accountability artifact requirements for this initiative.
- Make the policy change explicit enough that downstream specs, plans, tests, and reviews can reject ungoverned image generation.

## Non-goals

- No image generation in this proposal.
- No direct generation from chat.
- No page edits, media files, prompt records, or provenance rows in this proposal.
- No generated images for `exercises/baduanjin-basics.md` in this initiative.
- No borrowed web images, stock photos, screenshots, branded equipment emphasis, identifiable people, or unlicensed media.
- No video, animation, form-analysis feature, hosted media service, CMS, database, user accounts, public API, workout planner, clinical product, recovery-care protocol, or personalized coaching behavior.
- No in-image labels, citations, warnings, red pain marks, clinical assessment framing, treatment claims, correctness badges, posture-correction promises, or before-and-after framing. [Source][local-2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents-exercise-image-standard]

## Vision fit

fits the current vision

The current vision supports optional visuals that help beginners understand exercise purpose, setup, movement, muscles involved, common mistakes, safety notes, and sources.
This proposal can fit only if Markdown remains the primary product, citations and safety routing remain in text, generated images stay support-only, and repository-local media records keep provenance without requiring human-review fields.

## Context

The current exercise-image standard says exercise images are optional support assets, pages should use the minimum number needed, and more than three exercise images need downstream approved justification.
The accepted exercise-document image prioritization workflow later clarified that fewer-than-five pages enter evaluation, but the threshold does not require generation to five images.

This proposal intentionally asks whether that boundary should change for the named exercise documents.
If accepted, it would amend or supersede the relevant parts of:

- `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`;
- `specs/exercise-document-best-practice-image-prioritization.md`;
- `specs/exercise-image-standard.md`, especially the normal image-count behavior for this named population.

The included population from the user request is:

| Exercise document | Current image count | Treatment |
|---|---:|---|
| `exercises/band-pull-apart.md` | 2 | included |
| `exercises/bird-dog.md` | 1 | included |
| `exercises/brisk-walking.md` | 2 | included |
| `exercises/chest-press.md` | 2 | included |
| `exercises/chin-nod.md` | 2 | included |
| `exercises/dead-bug.md` | 1 | included |
| `exercises/glute-bridge.md` | 1 | included |
| `exercises/hip-hinge.md` | 1 | included |
| `exercises/incline-push-up.md` | 1 | included |
| `exercises/kneeling-hip-flexor-stretch.md` | 1 | included |
| `exercises/lat-pulldown.md` | 2 | included |
| `exercises/plank.md` | 2 | included |
| `exercises/prone-y-t.md` | 2 | included |
| `exercises/rowing-machine.md` | 3 | included |
| `exercises/seated-row.md` | 2 | included |
| `exercises/tai-chi-basics.md` | 3 | included |
| `exercises/thoracic-extension.md` | 2 | included |
| `exercises/wall-slide.md` | 2 | included |
| `exercises/baduanjin-basics.md` | 5 | excluded |

## Options Considered

### Option A: Keep the current minimum-needed policy

This would preserve the accepted workflow exactly.
Each fewer-than-five document would be evaluated, each page would get a top-10 candidate table, and the first slice would generate only the minimum-needed subset.

Advantages:

- Lowest policy churn.
- Best preserves Markdown-first restraint.
- Avoids a large generated-media batch before review capacity is proven.

Drawbacks:

- Does not satisfy the user's current request to generate top five images for every listed document.
- Leaves image coverage uneven when a page has fewer than five images.

Disposition: rejected for this proposal because it does not match the user's selected direction.

### Option B: Directly generate all top-five images from chat

This would immediately generate the requested assets without updating specs or review artifacts.

Advantages:

- Fastest visible result.
- Produces many candidate images immediately.

Drawbacks:

- Conflicts with repository source-order rules.
- Conflicts with the currently accepted prioritization spec.
- Skips durable prompt records, provenance, and validation.
- Risks producing media that cannot be promoted into the Markdown corpus.

Disposition: rejected.

### Option C: Revise the image-count policy for a governed named-population top-five initiative

This would explicitly change the current policy for the listed fewer-than-five documents.
Each included page would receive a page-specific top-10 evaluation and then target five total exercise images through governed implementation slices.
The generated batch would still use accepted image purposes, prompt records, provenance, page-local Markdown support, and rollback proof.
It would also revise the current human-reviewer, review-owner, visual-safety-review evidence, and replacement accountability artifact requirements for this named initiative.

Advantages:

- Matches the user's requested direction while respecting source-of-truth order.
- Makes the policy tradeoff reviewable before large media generation starts.
- Keeps each page's image set tied to page-specific beginner comprehension needs.
- Allows downstream specs and tests to enforce quality gates for a larger generated batch.

Drawbacks:

- Requires revision of approved specs before implementation.
- Creates a large media review burden across eighteen exercise documents.
- Risks over-visualizing pages where text or fewer images would have been enough.
- Adds future maintenance cost for prompt records, provenance rows, alt text, and image drift.

Disposition: recommended.

### Option D: Generate five images only for a small pilot page batch

This would revise policy only for a small first batch and decide later whether to expand to the full included population.

Advantages:

- Lower review burden than all eighteen documents.
- Produces practical evidence about whether five images per page improves beginner comprehension.

Drawbacks:

- Narrows the user's request.
- Still requires policy revision for the pilot pages.
- May create uneven visual coverage for longer than desired.

Disposition: viable fallback if proposal review finds the full batch too broad.

## Recommended Direction

Choose Option C.

GymPrimer should intentionally revise the current exercise-document image policy for the named fewer-than-five population.
For this initiative only, the listed included documents should be allowed to target five total exercise images per page after a page-local top-10 audit confirms five distinct teaching purposes.
The five-image target counts existing accepted images, including older accepted sequence images, plus newly generated images.

The policy revision should not make five images a general rule for all exercise pages.
It should apply only to the named population and only after downstream specs define the exception, validation, and rollback behavior.

The proposed top-five model should work like this:

| Rank | Default role | Required distinction |
|---:|---|---|
| 1 | Highest-value generation candidate | Covers the largest page-specific setup, movement, or broad attention gap. |
| 2 | Generation candidate | Covers a distinct section or confusion point not solved by rank 1. |
| 3 | Generation candidate | Completes the normal setup, movement, or broad attention support set when needed. |
| 4 | Policy-revision generation candidate | Adds a distinct beginner-comprehension purpose that justifies exceeding the current three-image normal range. |
| 5 | Policy-revision generation candidate | Adds a distinct beginner-comprehension purpose that justifies the page-specific five-image target. |

Each included page should still use no more than one muscle-attention image.
Ranks 4 and 5 should normally be setup or movement variants, common position clarification, equipment relationship, key position, or beginner-safe range illustration rather than another muscle-attention image.

The downstream spec should also define a coverage limit.
If a page-local audit cannot identify five distinct, source-supported, beginner-useful image purposes, that page should record fewer than five total image targets and return to the minimum-needed policy rather than inventing low-value visuals.

The downstream spec should remove the separate generated-image human-reviewer requirement for this initiative only.
The downstream spec should not replace that field with another repository-local accountability artifact.
Human review is expected before PR merge, but this initiative should not require repository files or validation checks to record that review.
That revision is a deliberate conflict with the current exercise-image standard and should be reviewed before implementation.

## Expected Behavior Changes

If accepted and implemented through downstream artifacts:

- The named eighteen exercise documents would become the top-five generation population.
- `exercises/baduanjin-basics.md` would remain excluded from this initiative because it already has five images.
- Fewer-than-five image count would become a generation trigger for this named initiative, not only an evaluation trigger.
- Each included exercise document would receive a page-specific top-10 image candidate table.
- The top five eligible candidates for each included document would become the intended total-image target, subject to page-local distinct-purpose and review criteria.
- The current three-image normal limit would be revised or given a named-population exception for this initiative.
- Every generated image would still need accepted exercise-image purpose, prompt record, provenance row, alt text, source support, privacy proof, and rollback proof.
- Generated raster images in this initiative would not need a separate accountable human-reviewer field, review-owner field, visual-safety-review evidence artifact, or replacement accountability artifact if downstream spec review accepts that policy revision.
- Existing acceptable images would be retained and counted toward the five-image target unless page-local audit records a concrete replacement reason.
- Existing older sequence images would count toward the five-image target when the page-local audit accepts them.
- Pages would not receive duplicate muscle-attention images.
- A page that cannot justify five distinct support images would record the reason and remain below five instead of forcing filler images.

## Architecture Impact

The likely architecture impact is a policy and validation amendment, not a new runtime architecture.

| Surface | Expected change |
|---|---|
| `specs/exercise-document-best-practice-image-prioritization.md` | Amend top-five backlog and fewer-than-five trigger behavior for the named population. |
| `specs/exercise-image-standard.md` | Add a scoped image-count exception or revised count policy for approved top-five exercise-document initiatives. |
| `docs/adr/2026-07-03-exercise-document-image-purposes.md` | Likely remains valid unless downstream review finds the three-purpose model cannot support top-five pages cleanly. |
| `media/exercises/<exercise-slug>/` | Adds generated raster assets for included documents. |
| `media/prompts/exercises/<exercise-slug>/` | Adds exact prompt records for every accepted generated image. |
| `media/PROVENANCE.md` | Adds provenance rows and removes repository-local reviewer field requirements for this named initiative. |
| Validation tooling | Needs tests for the named top-five exception, coverage limit, no duplicate muscle-attention image, prompt-record links, provenance rows, and page references. [Source][local-2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents-exercise-image-standard] |
| Change-local evidence | Needs per-page top-10 audits, top-five justification, beginner-comprehension proof, and rollback proof. |

This proposal does not add a hosted app, database, CMS, account system, public API, or video pipeline.

## Testing and Verification Strategy

Downstream test specs should cover the policy revision before implementation.

Automated checks should cover:

- the named included and excluded exercise-document population;
- image-count validation that permits the scoped top-five exception only where downstream approval exists;
- rejection of a sixth image unless a later approved artifact authorizes it;
- rejection of duplicate muscle-attention images;
- accepted exercise-image purpose values;
- local image paths under `media/exercises/<exercise-slug>/`;
- prompt-record presence and reverse asset-path match;
- complete approved provenance rows;
- `page_refs` matching the exercise document;
- meaningful alt text;
- privacy and no-secrets checks.

Manual proof should cover:

- per-page top-10 evaluation and top-five distinct-purpose justification;
- source-support review tying nearby Markdown to the image's teaching purpose;
- beginner-comprehension review for each changed page;
- rollback proof showing each page remains usable if a generated image is removed.

Completion reports should name exact local validation commands.
CI should be claimed only if a CI run is actually observed.

## Rollout and Rollback

Rollout should be staged because the full request can produce a large number of generated assets.

First, downstream specs should revise the current image-count and top-five backlog policy for this named population.
Then architecture assessment should confirm that existing media provenance and prompt-record ADRs still cover the larger batch.
Then the plan should divide the eighteen included documents into two or three reviewable milestones rather than one page at a time.
Each milestone should finish page-local audit, prompt records, generated assets, provenance rows, page edits, and validation before moving to the next milestone.

Rollback is additive.
If one generated image fails review, remove that image reference, remove the unused asset and prompt record, remove or revise the provenance row, and keep the exercise page readable.
If the policy revision proves too broad, roll back to the existing minimum-needed policy by superseding this proposal and reverting unpromoted generated assets.
Already-promoted images should be removed only through page-local audit so useful reviewed images are not discarded mechanically.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| The change turns image count into a vanity metric. | Require five distinct, page-local teaching purposes and allow a coverage limit below five. |
| The generated batch overwhelms review capacity. | Use two or three milestones and keep generated-image human review outside repository-local validation, with PR merge as the human acceptance gate. |
| Images drift from Markdown source-of-truth. | Keep setup, movement, muscles, cues, caveats, safety, and citations in Markdown; require source-support review. |
| Five images create duplicate or low-value visuals. | Score candidates and reject duplicate purposes, especially duplicate muscle-attention images. |
| The policy exception leaks to all exercise documents. | Scope the exception to the named population unless a later proposal broadens it. |
| Prompt/provenance records become incomplete. | Extend tests before implementation and reject generated raster references without complete records. |
| Removing repository-local reviewer requirements weakens media accountability. | Accept this as an owner-selected tradeoff for this initiative; human review happens before PR merge and is not recorded as a repository validation requirement. |
| Visuals imply medical, treatment, or individualized coaching claims. | Preserve prohibited prompt/image content, source-support checks, and Markdown source-of-truth boundaries. |
| Large binary asset churn makes rollback harder. | Keep slices small and make each image's prompt record, provenance row, and page reference independently removable. |

## Open Questions

None.

Resolved by user direction on 2026-07-06:

- The top-five target means five total images per page, including existing accepted images.
- Existing older sequence images count toward the five-image target when the page-local audit accepts them.
- This initiative should not require a separate accountable human reviewer, review owner, visual-safety-review evidence artifact, or replacement accountability artifact in the repository.
- The implementation should cover all included documents through two or three milestones rather than separate page-by-page slices.
- The related spec needs to be updated before implementation.

## Initial Intent Preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Generate top five high-quality images for the listed exercise documents. | in scope | Goals, Recommended Direction, Expected Behavior Changes |
| Include every listed exercise document with fewer than five images. | in scope | Goals, Context, Expected Behavior Changes |
| Exclude `exercises/baduanjin-basics.md` because it already has five images. | in scope | Goals, Context, Expected Behavior Changes |
| Follow best practices rather than direct ungoverned generation. | in scope | Recommended Direction, Testing and Verification Strategy, Risks and Mitigations |
| Preserve page-specific evaluation rather than one repository-wide evaluation. | in scope | Goals, Recommended Direction |
| Count existing accepted images toward the five-image target. | in scope | Recommended Direction, Expected Behavior Changes |
| Count accepted older sequence images toward the five-image target. | in scope | Recommended Direction, Expected Behavior Changes |
| Avoid repository-local human-reviewer and replacement accountability requirements. | in scope | Goals, Recommended Direction, Open Questions |
| Implement across two or three milestones. | deferred follow-up | Rollout and Rollback, Scope Budget |

## Scope Budget

| Work item | Treatment | Reason |
|---|---|---|
| Policy revision for top-five generation target | core to this proposal | The request conflicts with the current accepted minimum-needed policy unless this is decided first. |
| Spec amendments | same-slice dependency | Implementation cannot proceed until the approved specs reflect the new image-count policy and removal of repository-local reviewer requirements. |
| Architecture assessment | same-slice dependency | The larger generated-media batch may still use existing ADRs, but that should be checked before planning. |
| Per-page top-10 audits | separate implementation slice | Audits are execution evidence, not proposal content. |
| Two or three implementation milestones for all included documents | separate implementation slice | Media generation and promotion need specs, plan, tests, review, and verification first. |
| Generated image assets, prompt records, provenance rows, and page edits | separate implementation slice | Media generation and promotion need specs, plan, tests, review, and verification first. |
| Template update | deferable follow-up | Template changes should follow proven audit criteria rather than precede the first governed slices. |

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-06 | Draft a new proposal instead of generating images directly. | Current accepted artifacts do not authorize top-five generation as an automatic target. | Direct chat-driven generation. |
| 2026-07-06 | Recommend a named-population policy revision. | This best preserves the user's request while keeping source-order governance intact. | Keeping current policy unchanged as the primary recommendation. |
| 2026-07-06 | Exclude `exercises/baduanjin-basics.md` from this initiative. | The user marked it excluded because it already has five images. | Re-auditing all exercise documents in the first generation population. |
| 2026-07-06 | Count existing accepted images, including accepted older sequence images, toward five total images per page. | The user clarified the target means five total images, not five new images. | Generating five new images in addition to existing images. |
| 2026-07-06 | Record the user's request to remove repository-local human-reviewer and replacement accountability requirements as a policy revision. | The current approved exercise-image standard requires a human reviewer field and visual-safety review, so the change needs spec review before implementation. | Silently ignoring the conflict or implementing from chat. |
| 2026-07-06 | Treat PR merge after human review as outside repository-local validation. | The user clarified that the repository should not carry these requirements. | Adding change-local replacement accountability artifacts. |
| 2026-07-06 | Prefer two or three implementation milestones for the full included population. | The user asked to implement all documents without page-by-page slices. | One page per slice. |

## Next Artifacts

- Proposal review for policy fit, scope, review burden, and conflict with the accepted exercise-image standards.
- Draft spec amendment for the named top-five initiative, including the five-total-images target and repository-local reviewer-policy removal.
- Spec amendment for the exercise-document prioritization workflow if the proposal is accepted.
- Spec amendment for the exercise-image standard's image-count and repository-local reviewer behavior if the proposal is accepted.
- Architecture assessment for whether existing prompt-record and provenance ADRs cover the larger batch.
- Plan and test spec for page-batch sequencing, validation, and rollback.

## Follow-on Artifacts

- Proposal-review R1: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/proposal-review-r1.md`
- Review resolution: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-resolution.md`
- Proposal-review R2: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/proposal-review-r2.md`
- Draft spec amendment: `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`

## Readiness

Accepted for downstream spec review.
Not ready for planning, implementation, image generation, or PR handoff until spec review, architecture assessment, plan, plan review, test spec, and test-spec review are complete.

## Sources

- `CONSTITUTION.md`
- `VISION.md`
- `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-image-standard.md`
- `docs/adr/2026-07-03-exercise-document-image-purposes.md`
- `docs/adr/2026-07-03-generated-raster-prompt-records.md`

[local-2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents-exercise-image-standard]: ../../specs/exercise-image-standard.md
