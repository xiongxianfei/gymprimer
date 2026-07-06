# Spec: Exercise Document Best-Practice Image Prioritization

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- Proposal review:
  - `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/proposal-review-r1.md`
  - `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/proposal-review-r2.md`
- Review resolution: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`
- Governing exercise-image spec: `specs/exercise-image-standard.md`
- Vision: `VISION.md`
- Constitution: `CONSTITUTION.md`

## Goal and context

This spec defines the observable contract for evaluating image needs and best-practice cleanup opportunities per exercise document.
It turns the accepted proposal into requirements for choosing the evaluation population, recording top-10 image-candidate rankings, treating the top five as candidate backlog, preserving the approved image-count policy, and proving the first implementation slice before generated exercise images or page edits are promoted.

GymPrimer remains a Markdown-first, citation-backed beginner primer.
Exercise images are optional support assets.
This spec does not make five images mandatory, does not revise the exercise-image standard's normal zero-to-three image range, and does not authorize direct generation from chat.

## Glossary

- Exercise document: A Markdown page under `exercises/` that teaches one exercise or exercise support movement.
- Evaluation population: The set of exercise documents selected for page-specific image and best-practice audit.
- Fewer-than-five trigger: The rule that exercise documents with fewer than five existing image references enter the first evaluation population.
- Top-10 candidate table: A page-specific ranked list of up to ten possible support images for one exercise document.
- Top-five candidate backlog: The first five ranked image candidates for one exercise document, treated as possible future work rather than an automatic generation batch.
- Minimum-needed subset: The smallest generated image set needed to address approved page-specific comprehension gaps while preserving the exercise-image standard.
- Page-local audit: Change-local evidence that records image count, current image purposes, text-section quality, source support, replacement rationale, candidate ranking, generation decision, and rollback path for one exercise document.
- Older sequence image: An existing image that shows a sequence, common mistake, or compact movement concept and may predate the current exercise-image purpose vocabulary.

## Examples first

Example E1: fewer than five images triggers evaluation, not generation
Given `exercises/example.md` has two existing image references
When the first evaluation population is built
Then the page is included in the audit
And the audit may still decide that no additional generated image is needed.

Example E2: selected page receives a page-specific top-10 table
Given an exercise document is in the evaluation population
When its page-local audit is recorded
Then the audit includes a ranked top-10 candidate table for that page, or records fewer than ten candidates with a rationale.

Example E3: top five are backlog, not a target
Given a page's top-10 table ranks five high-value candidates
When the first implementation slice chooses generated images
Then it selects only the minimum-needed subset approved for that page.

Example E4: fourth image needs explicit justification
Given a selected exercise document would end with four exercise images
When the downstream page-specific slice is planned
Then an approved spec or plan records why the exception is needed under `specs/exercise-image-standard.md`.

Example E5: older sequence image is preserved
Given an older sequence image is readable, safe, source-compatible, and has fixable nearby Markdown or alt text
When the owning page is audited
Then the image is preserved unless the audit records a concrete replacement reason.

Example E6: change-local proof precedes template changes
Given the first slice exposes useful audit criteria
When implementation records the first page-local audit
Then the criteria remain in change-local evidence unless a later approved slice updates `docs/templates/exercise-card.md`.

## Requirements

R1. The first evaluation population MUST include every current exercise document under `exercises/` with fewer than five existing image references at audit time.

R2. The fewer-than-five trigger MUST be treated as an evaluation trigger, not as a requirement to add images until the page reaches five images.

R3. The audit process MUST evaluate image needs separately for each selected exercise document.

R4. Each selected exercise document MUST have a page-local audit before generated images or page edits are promoted for that document.

R5. Each page-local audit MUST record the exercise document path, current image count, existing image purposes when identifiable, current section coverage, source-support issues, image-replacement issues, top-10 candidate table, generation decision, validation expectations, and rollback path.

R6. Each selected exercise document MUST include a ranked top-10 candidate table, unless the audit records why fewer than ten meaningful candidates exist.

R7. Each candidate table row MUST record rank, candidate image description, page section supported, accepted exercise-image purpose, why it matters, 1-25 score, and disposition.

R8. Candidate scoring MUST use beginner comprehension, safety/setup value, muscle-attention value, page value, and readiness, each scored from 1 to 5.

R9. The top five ranked candidates MUST be treated as a candidate backlog, not an automatic generation target.

R10. A first implementation slice MUST select only the minimum-needed subset of generated images for each edited exercise document.

R11. A first implementation slice MUST NOT generate a sixth image candidate for a selected exercise document unless a downstream approved spec or plan records why delaying the tightly related candidate would create worse churn.

R12. The image-count behavior in `specs/exercise-image-standard.md` MUST remain authoritative: exercise documents use the minimum number of images needed and MUST NOT include more than three exercise images unless a downstream approved spec or plan records explicit justification.

R13. A fourth or fifth exercise image MUST be justified by page-specific downstream approval; the fewer-than-five trigger alone MUST NOT justify that exception.

R14. A selected exercise document MUST NOT include more than one `exercise_muscle_attention_illustration`.

R15. New generated raster exercise images produced by this workflow MUST use only accepted exercise-image purposes from `specs/exercise-image-standard.md`.

R16. New generated raster exercise images produced by this workflow MUST satisfy prompt-record, provenance, human-reviewer, alt-text, page-reference, privacy, visual-safety, and beginner-comprehension requirements from `specs/exercise-image-standard.md`.

R17. Exercise document Markdown MUST remain the source of truth for setup, movement instructions, muscle names, feel cues, caveats, safety notes, and citations.

R18. Candidate descriptions, prompts, alt text, nearby Markdown, and review evidence MUST NOT introduce clinical assessment, treatment, cure, individualized coaching, recovery-care protocol, exact anatomy as image authority, or workout-planner behavior. [Source][local-exercise-document-best-practice-image-prioritization-exercise-image-standard]

R19. Existing acceptable images MUST be preserved unless the page-local audit records a concrete replacement reason.

R20. Older sequence images MUST NOT be replaced for style consistency alone.

R21. Valid image replacement reasons include unsafe visual implication, missing required provenance or prompt record where required, alt text that cannot be corrected without asset change, misleading common-mistake framing, incompatible purpose, low readability, or duplicate coverage after better images are added. [Source][local-exercise-document-best-practice-image-prioritization-exercise-image-standard]

R22. The first slice MUST record audit criteria in change-local proof evidence before updating `docs/templates/exercise-card.md`.

R23. The first implementation slice MUST be limited to one selected exercise document or a deliberately small page batch.

R24. Rollback for a failed generated image MUST remove the Markdown image reference, remove unused generated assets and prompt records, remove or revise provenance rows, and leave the page readable in text form.

R25. This spec MUST NOT add a new PR-review rule beyond the repository's existing lifecycle and owner-review practice.

R26. This spec MUST NOT add a hosted app, CMS, database, user account, user-input flow, generated public API, video-first media path, or personalized coaching behavior.

## Inputs and outputs

Inputs:

- Current exercise Markdown pages under `exercises/`.
- Existing Markdown image references in those pages.
- Existing media assets under `media/`.
- `media/PROVENANCE.md` and prompt records when generated raster images are present.
- Accepted exercise-image, prompt-record, Markdown-first, and privacy requirements.
- Change-local audit evidence for selected pages.

Outputs:

- Evaluation population inventory for exercise documents with fewer than five images.
- Page-local audits with top-10 candidate tables for selected exercise documents.
- Optional page-specific generated image subset, prompt records, provenance rows, and page edits in later implementation slices.
- Validation and review evidence for any generated image batch.
- Rollback evidence showing the page remains readable without failed new images.

## State and invariants

- Markdown exercise pages remain valid with no images.
- Markdown exercise pages remain the source of truth when images exist.
- The existing exercise-image standard remains authoritative for image count, purpose, provenance, prompt records, alt text, visual safety, and beginner-comprehension proof.
- The fewer-than-five trigger selects pages for evaluation only.
- Top-five candidate backlog status does not imply top-five generation.
- Existing acceptable images are not migration targets.
- Change-local audit proof precedes any template change.

## Error and boundary behavior

- A selected page with fewer than ten meaningful image candidates passes audit only when the audit records why fewer than ten candidates exist.
- A selected page with fewer than five images may pass the first slice with no new generated image when the audit records that current images and Markdown are sufficient.
- A page attempting to add a fourth or fifth image fails planning or validation unless downstream approved artifacts record page-specific exception justification.
- A second muscle-attention image fails under the exercise-image standard.
- A candidate table using non-exercise media purposes fails review.
- A style-only replacement rationale fails audit review.
- A page-local audit that omits rollback proof blocks implementation closeout for generated images.

## Compatibility and migration

Existing text-only exercise pages remain valid.
Existing exercise images and older sequence images remain valid unless page-local audit finds a concrete problem.
This spec does not require migrating existing generated raster image purpose values, prompt records, provenance rows, or assets.
Downstream slices may update page-local wording, alt text, evidence, or assets only when the owning page is in scope and the audit records the reason.

## Observability

- The evaluation population inventory SHOULD name each included exercise document and its current image count.
- Page-local audits MUST name candidate ranks, scores, dispositions, and generated-image decisions.
- Validation evidence MUST name exact commands run and outcomes.
- Review evidence MUST identify visual-safety, source-support, beginner-comprehension, privacy, and rollback proof artifacts when generated images are promoted.
- Local reports MUST distinguish evaluation, candidate backlog, generated subset, and deferred candidates.

## Security and privacy

Audit evidence, prompts, prompt records, provenance rows, review notes, and validation output MUST NOT include secrets, private data, private health information, identifying private-person imagery, or private machine paths.
Generated image prompts MUST avoid private, clinical, treatment, personalized coaching, and unsafe content. [Source][local-exercise-document-best-practice-image-prioritization-exercise-image-standard]

## Accessibility and UX

Generated image subsets MUST improve beginner comprehension without overwhelming the page.
Meaningful alt text is required for promoted image references.
Images must remain support-only and must not carry in-image text, labels, citations, warning badges, or source-of-truth claims.
Text-only or low-image pages remain acceptable when the audit supports that outcome.

## Performance expectations

Audit and validation work is repository-local Markdown and Python check work.
The first implementation slice SHOULD keep validation focused enough for local review while preserving required image-standard checks.
No runtime performance, network, hosting, or database behavior is introduced.

## Edge cases

- EC1. Text-only exercise page enters evaluation because it has fewer than five images, then records no generated image is needed.
- EC2. Page has one older sequence image and preserves it after audit.
- EC3. Page has three images and a top-five backlog but selects no fourth image because no exception is justified.
- EC4. Page has four existing images and needs audit because one image may be duplicate or unsafe. [Source][local-exercise-document-best-practice-image-prioritization-exercise-image-standard]
- EC5. Page has fewer than ten meaningful candidates.
- EC6. Candidate 6 is tightly related to the same section as candidate 5, but is deferred unless downstream approval records worse churn.
- EC7. Candidate uses `exercise_muscle_attention_illustration` when the page already has one muscle-attention image.
- EC8. Generated image prompt record redacts unsafe content and records the reason. [Source][local-exercise-document-best-practice-image-prioritization-exercise-image-standard]
- EC9. Rollback removes a failed image and leaves the Markdown page usable.

## Non-goals

- Generate images in this spec.
- Revise the exercise-image standard's image-count policy.
- Require every exercise document to reach five images.
- Create one repository-wide top-10 image list.
- Replace acceptable images for style consistency.
- Update the exercise template before first-slice audit criteria are proven.
- Add new exercise pages, video, animation, borrowed media, stock photos, hosted media delivery, or personalized coaching.

## Acceptance criteria

- AC1. The implementation can produce an inventory of exercise documents with fewer than five images without treating that inventory as a generation target.
- AC2. Each selected exercise document has a page-local audit with required fields and a top-10 candidate table or fewer-than-ten rationale.
- AC3. Top-five candidates are recorded as backlog; generated subsets are separately justified as minimum-needed.
- AC4. Any fourth or fifth image has page-specific downstream approval under the exercise-image standard.
- AC5. Existing acceptable and older sequence images are preserved unless concrete page-local replacement reasons are recorded.
- AC6. Generated images, when later added, satisfy prompt-record, provenance, visual-safety, privacy, alt-text, and beginner-comprehension proof obligations.
- AC7. Rollback evidence leaves the exercise page readable without failed new images.
- AC8. No new runtime, hosted, clinical, coaching, video-first, or PR-rule behavior is introduced.

## Open questions

None.

## Next artifacts

- Architecture assessment for whether existing media architecture and ADRs cover this workflow.
- Execution plan for first-slice audit, validation, proof artifacts, and minimum-needed image generation path.
- Test spec mapping requirements to automated and manual proof.

## Follow-on artifacts

- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/spec-review-r1.md`

## Readiness

Approved for architecture assessment and planning after clean spec review.
Implementation is not allowed until plan, plan review, test spec, and test-spec review are complete.

## Sources

- `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-image-standard.md`
- `docs/adr/2026-07-03-exercise-document-image-purposes.md`
- `docs/adr/2026-07-03-generated-raster-prompt-records.md`
- `CONSTITUTION.md`
- `VISION.md`

[local-exercise-document-best-practice-image-prioritization-exercise-image-standard]: exercise-image-standard.md
