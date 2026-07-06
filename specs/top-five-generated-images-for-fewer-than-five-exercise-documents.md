# Spec: Top-Five Generated Images for Fewer-Than-Five Exercise Documents

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- Prior accepted proposal: `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- Prior approved spec: `specs/exercise-document-best-practice-image-prioritization.md`
- Governing exercise-image spec to amend if this draft is approved: `specs/exercise-image-standard.md`
- Vision: `VISION.md`
- Constitution: `CONSTITUTION.md`

## Goal and context

This draft spec defines a proposed named-population exception for generating enough high-quality exercise images that each included fewer-than-five exercise document reaches five total accepted images.
The five-image target counts existing accepted images, including accepted older sequence images.

This draft intentionally changes the current prioritization behavior.
The approved prioritization spec treats fewer-than-five as an evaluation trigger, treats top-five candidates as backlog, and preserves the normal zero-to-three image range.
This draft instead proposes that the named fewer-than-five population use top-five page-local candidates as a generation target until the page reaches five total accepted images.

This draft also records the user's requested reviewer-policy change.
For this initiative, generated raster images would not require repository-local `human_reviewer`, review-owner, visual-safety-review evidence, or replacement accountability artifacts.
Human review is expected before PR merge, but this initiative does not record that review as a repository validation requirement.
That conflicts with the current approved exercise-image standard and blocks implementation until spec review accepts or revises the reviewer contract.

## Glossary

- Named top-five population: The exercise documents listed in R1 that had fewer than five image references when this proposal was drafted.
- Five total images: The target count of five accepted exercise images referenced by one exercise document, counting existing accepted images and newly generated images together.
- Accepted existing image: An existing image that a page-local audit preserves because it is readable, source-compatible, safe for the page purpose, and not duplicate coverage.
- Accepted older sequence image: An existing sequence or compact movement image that remains valid after page-local audit and counts toward five total images.
- New generated image need: The difference between five total images and the accepted existing image count for a page.
- Top-five generation target: The page-specific ranked candidates selected for generation or preservation until the page reaches five total accepted images.
- Milestone batch: One of two or three implementation milestones that covers a group of included exercise documents.
- Repository reviewer exception: The proposed removal of repository-local `human_reviewer`, review-owner, visual-safety-review evidence, and replacement accountability artifact requirements for this named initiative.

## Examples first

Example E1: existing images count toward five total images
Given `exercises/band-pull-apart.md` has two accepted existing images
When the page-local audit targets five total images
Then the new generated image need is three images.

Example E2: older sequence image counts when accepted
Given `exercises/bird-dog.md` has one older sequence image
And the page-local audit preserves that image
When the page targets five total images
Then the older sequence image counts as one of the five.

Example E3: fewer-than-five becomes generation trigger for named population
Given `exercises/dead-bug.md` is in the named top-five population
When downstream implementation runs for its milestone batch
Then the page receives page-local audit and enough generated image candidates to reach five total accepted images unless the coverage limit applies.

Example E4: coverage limit prevents filler images
Given a page-local audit identifies only four distinct, source-supported, beginner-useful image purposes
When the implementation milestone selects images
Then the page records four total image targets and does not generate a low-value fifth image.

Example E5: no sixth image by default
Given an included exercise document reaches five accepted images
When the milestone considers candidate rank 6
Then rank 6 is deferred unless a later approved artifact explicitly authorizes a sixth image.

Example E6: repository reviewer exception is explicit
Given a generated raster image is produced for this named initiative
When its provenance row is validated under this draft after approval
Then the row is not rejected solely because `human_reviewer` is blank and no replacement accountability artifact is present.

## Requirements

R1. The named top-five population MUST contain these included exercise documents and no others for this initiative: `exercises/band-pull-apart.md`, `exercises/bird-dog.md`, `exercises/brisk-walking.md`, `exercises/chest-press.md`, `exercises/chin-nod.md`, `exercises/dead-bug.md`, `exercises/glute-bridge.md`, `exercises/hip-hinge.md`, `exercises/incline-push-up.md`, `exercises/kneeling-hip-flexor-stretch.md`, `exercises/lat-pulldown.md`, `exercises/plank.md`, `exercises/prone-y-t.md`, `exercises/rowing-machine.md`, `exercises/seated-row.md`, `exercises/tai-chi-basics.md`, `exercises/thoracic-extension.md`, and `exercises/wall-slide.md`.

R2. `exercises/baduanjin-basics.md` MUST be excluded from this initiative because it already has five images.

R3. For the named top-five population, fewer than five accepted images MUST be treated as a generation trigger after page-local audit, not only as an evaluation trigger.

R4. The top-five target MUST mean five total accepted images per page, not five newly generated images in addition to existing images.

R5. Accepted existing images MUST count toward the five total images.

R6. Accepted older sequence images MUST count toward the five total images.

R7. Each included exercise document MUST have a page-local audit before new generated images are promoted for that document.

R8. Each page-local audit MUST record current image count, accepted existing image count, accepted older sequence image count when applicable, new generated image need, top-10 candidate ranking, top-five generation target, coverage-limit outcome, validation expectations, and rollback path.

R9. Each included exercise document MUST receive a page-specific top-10 candidate table unless the audit records why fewer than ten meaningful candidates exist.

R10. Candidate scoring MUST use beginner comprehension, setup value, muscle-attention value, page value, and readiness, each scored from 1 to 5.

R11. Candidate ranks 1 through 5 MUST be considered the default target set for preserving existing images or generating new images until the page reaches five total accepted images.

R12. A page MUST NOT generate more new images than needed to reach five total accepted images.

R13. A page MUST use a coverage limit below five total images when the audit cannot identify five distinct, source-supported, beginner-useful image purposes.

R14. A sixth image MUST NOT be generated for an included exercise document unless a later approved artifact records explicit page-specific justification.

R15. The initiative MUST NOT add more than one `exercise_muscle_attention_illustration` to any exercise document.

R16. New generated raster images MUST use only accepted exercise-image purposes: `exercise_setup_illustration`, `exercise_movement_illustration`, or `exercise_muscle_attention_illustration`.

R17. New generated raster images MUST live under `media/exercises/<exercise-slug>/`.

R18. New generated raster images MUST have repository-local prompt records under `media/prompts/exercises/<exercise-slug>/`.

R19. New generated raster images MUST have provenance rows in `media/PROVENANCE.md`.

R20. For this named initiative only, generated raster provenance rows MUST NOT be rejected because the `human_reviewer` field is blank.

R21. For this named initiative only, generated raster prompt records MUST NOT be required to identify a human reviewer, review owner, or reviewer-accountability owner.

R22. For this named initiative only, repository-local validation MUST NOT require visual-safety-review evidence or replacement accountability artifacts for generated raster images.

R22A. The repository reviewer exception MUST NOT remove requirements for prompt record, generator, prompt summary, created date, license assertion, source inputs, review status, page references, notes, alt text, source support, privacy checks, beginner-comprehension evidence, or rollback evidence.

R23. Exercise document Markdown MUST remain the source of truth for setup, movement instructions, muscle names, feel cues, caveats, safety notes, and citations.

R24. Candidate descriptions, prompts, alt text, nearby Markdown, and audit records MUST NOT introduce clinical assessment, treatment, cure, individualized coaching, recovery-care protocol, exact anatomy as image authority, or workout-planner behavior. [Source][local-top-five-generated-images-for-fewer-than-five-exercise-documents-exercise-image-standard]

R25. Existing acceptable images MUST be preserved unless the page-local audit records a concrete replacement reason.

R26. Image replacement reasons MUST be limited to concrete page-local issues such as unsafe visual implication, missing required provenance or prompt record where required, alt text that cannot be corrected without asset change, misleading common-mistake framing, incompatible purpose, low readability, or duplicate coverage after better images are added. [Source][local-top-five-generated-images-for-fewer-than-five-exercise-documents-prioritization-spec]

R27. Implementation MUST cover all included exercise documents through two or three milestone batches rather than one page-only slice per exercise document.

R28. Each milestone batch MUST finish page-local audits, generated assets, prompt records, provenance rows, page edits, validation, and rollback evidence for its included documents before the next milestone batch starts.

R29. This spec MUST NOT add a new PR-review rule beyond the repository's existing lifecycle and owner-review practice.

R30. This spec MUST NOT add a hosted app, CMS, database, user account, user-input flow, generated public API, video-first media path, or personalized coaching behavior.

## Inputs and outputs

Inputs:

- The named exercise Markdown pages under `exercises/`.
- Existing Markdown image references in those pages.
- Existing media assets under `media/`.
- Existing prompt records and `media/PROVENANCE.md` rows.
- Page-local sources and nearby Markdown.
- Page-local top-10 audit evidence.

Outputs:

- Page-local audits for all included exercise documents.
- Top-five generation target records for all included exercise documents.
- Generated raster assets for documents that need new images to reach five total accepted images.
- Prompt records for new generated raster assets.
- Provenance rows for new generated raster assets.
- Markdown image references and alt text for promoted images.
- Milestone validation and rollback evidence.

## State and invariants

- Markdown exercise pages remain the source of truth.
- `exercises/baduanjin-basics.md` remains out of scope for this initiative.
- Existing accepted images count toward the five total images.
- Accepted older sequence images count toward the five total images.
- The target count is five total images, not five new images.
- No included page may have more than one muscle-attention image.
- Human review is expected before PR merge, but this initiative does not require repository-local review evidence for generated image promotion.
- This draft cannot be used for implementation until review resolves the conflict with the approved exercise-image standard.

## Error and boundary behavior

- A document outside the named top-five population fails this initiative's population check.
- `exercises/baduanjin-basics.md` fails this initiative's population check.
- A page attempting to generate five new images without counting accepted existing images fails audit review.
- A page attempting to replace an accepted older sequence image for style alone fails audit review.
- A page attempting to generate a second muscle-attention image fails validation.
- A page attempting to add a sixth image fails unless later approved artifacts authorize it.
- A page with fewer than five distinct image purposes records a coverage-limit outcome instead of forcing a fifth image.
- A generated raster image missing prompt record, provenance row, page reference, source support, alt text, privacy proof, beginner-comprehension evidence, or rollback evidence fails promotion.
- A generated raster image in this initiative does not fail because `human_reviewer` is blank or because repository-local review evidence is absent after this draft is approved and implemented in validation.

## Compatibility and migration

This draft would supersede the current minimum-needed and top-five-backlog behavior only for the named top-five population.
The existing exercise-image standard would continue to govern all other exercise documents unless a later accepted proposal broadens the exception.

Existing accepted images do not need migration.
Existing older sequence images do not need replacement when page-local audit accepts them.
Existing generated raster images with a `human_reviewer` value remain compatible.
New generated raster images for this initiative may leave `human_reviewer` blank and omit repository-local review evidence only after this draft is approved and validation is updated.

Rollback is additive.
Failed images can be removed from Markdown, unused assets can be removed, prompt records can be removed, provenance rows can be removed or revised, and the exercise page remains readable.

## Observability

- Population evidence MUST name the included and excluded exercise documents.
- Page-local audits MUST name accepted existing images, new generated image need, candidate ranks, candidate scores, dispositions, and coverage-limit outcomes.
- Milestone reports MUST name which exercise documents were completed.
- Validation evidence MUST name exact commands run and outcomes.
- Reports MUST distinguish total accepted images from newly generated images.
- Reports MUST distinguish repository reviewer exception behavior from other provenance requirements.

## Security and privacy

Prompt records, provenance rows, audit evidence, generated image prompts, and validation output MUST NOT include secrets, private data, private health information, identifying private-person imagery, or private machine paths.
Generated image prompts MUST avoid private, clinical, treatment, personalized coaching, and unsafe content. [Source][local-top-five-generated-images-for-fewer-than-five-exercise-documents-exercise-image-standard]

## Accessibility and UX

Generated images MUST improve beginner comprehension without overwhelming the page.
Meaningful alt text is required for promoted image references.
Images must remain support-only and must not carry in-image text, labels, citations, warning badges, or source-of-truth claims.
Pages with a coverage-limit outcome below five images remain acceptable when the audit supports that outcome.

## Performance expectations

Audit and validation work is repository-local Markdown, media, and Python check work.
Milestone validation SHOULD remain practical to run locally for each batch.
No runtime performance, network, hosting, or database behavior is introduced.

## Edge cases

EC1. Included page has two accepted existing images and needs three new images.

EC2. Included page has one accepted older sequence image and needs four new images.

EC3. Included page has three accepted images and needs two new images.

EC4. Included page has fewer than five distinct useful image purposes and records a coverage-limit outcome.

EC5. Candidate rank 6 is useful but deferred because the page already reaches five total accepted images.

EC6. Existing image is rejected by page-local audit and no longer counts toward five total images.

EC7. Existing image is preserved but needs alt-text or nearby Markdown cleanup.

EC8. Generated image provenance row leaves `human_reviewer` blank under the proposed repository reviewer exception.

EC9. Generated image has blank `human_reviewer` but missing prompt record; it still fails promotion.

EC9A. Generated image has no repository-local review evidence; it does not fail for that reason under this named initiative after approval.

EC10. `exercises/baduanjin-basics.md` is accidentally included in a milestone batch.

## Non-goals

- Generate images in this spec.
- Approve this draft without spec review.
- Add images for `exercises/baduanjin-basics.md`.
- Generate five new images in addition to existing accepted images.
- Replace acceptable images for style consistency.
- Add more than one muscle-attention image to a page.
- Add new exercise pages, video, animation, borrowed media, stock photos, hosted media delivery, or personalized coaching.

## Acceptance criteria

- AC1. The implementation can identify the exact named top-five population and excluded Baduanjin page.
- AC2. Each included exercise document has a page-local audit with accepted existing image count and new generated image need.
- AC3. Existing accepted images and accepted older sequence images count toward five total images.
- AC4. Top-five generation targets produce no more new images than needed to reach five total accepted images.
- AC5. Coverage-limit outcomes allow fewer than five total images when five distinct useful purposes do not exist.
- AC6. Validation rejects a sixth image unless later approved artifacts authorize it.
- AC7. Validation rejects duplicate muscle-attention images.
- AC8. Generated images satisfy prompt-record, provenance, page-reference, privacy, alt-text, beginner-comprehension, and rollback obligations.
- AC9. The repository reviewer exception is implemented only for this named initiative and only after review resolves the conflict with the approved exercise-image standard.
- AC10. Implementation is grouped into two or three milestone batches covering all included exercise documents.

## Open questions

None.

## Next artifacts

- Proposal review for `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`.
- Spec review for this draft after proposal review accepts the direction.
- Architecture assessment for whether existing prompt-record and provenance ADRs cover this repository reviewer exception and larger batch.
- Execution plan with two or three milestone batches.
- Test spec for population, image-count, repository reviewer exception, provenance, prompt-record, and rollback checks.

## Follow-on artifacts

- Spec-review R1: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/spec-review-r1.md`

## Readiness

Approved for architecture assessment and planning.
Implementation is not allowed until architecture assessment, plan, plan review, test spec, and test-spec review are complete.

## Sources

- `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-image-standard.md`
- `CONSTITUTION.md`
- `VISION.md`

[local-top-five-generated-images-for-fewer-than-five-exercise-documents-exercise-image-standard]: exercise-image-standard.md
[local-top-five-generated-images-for-fewer-than-five-exercise-documents-prioritization-spec]: exercise-document-best-practice-image-prioritization.md
