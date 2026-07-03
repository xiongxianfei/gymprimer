# Spec: Exercise Image Standard

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-01-exercise-image-standard-and-optimization.md`
- Proposal review: `docs/changes/exercise-image-standard-and-optimization/reviews/proposal-review-r1.md`
- Vision: `VISION.md`
- Constitution: `CONSTITUTION.md`

## Goal and context

This spec defines the observable contract for full exercise-document images in GymPrimer. It turns the accepted exercise-image proposal into requirements for when exercise pages may use images, how many images a page may use, which image purposes are valid, how generated raster image provenance works, and how visual-safety, alt-text, source-of-truth, accessibility, and compatibility boundaries are verified.

GymPrimer remains a Markdown-first, citation-backed beginner primer. Exercise images are optional support assets. They help readers understand setup, movement, and broad muscle attention only when Markdown text alone is not enough. They do not replace page-local sources, safety routing, movement instructions, or human review.

## Glossary

- Exercise document: A Markdown page under `exercises/` that teaches one exercise or exercise support movement.
- Exercise image: An image referenced by an exercise document to support beginner comprehension of that exercise.
- Exercise setup image: An image whose purpose is equipment setup, grip, stance, bench, wall, floor, or body relationship.
- Exercise movement image: An image whose purpose is a start position, end position, key position, or movement path for the exercise.
- Exercise muscle-attention image: An image whose purpose is a broad body region or muscle region the reader should notice during the movement.
- Generated raster image: A `.png`, `.jpg`, `.jpeg`, or `.webp` file under `media/` classified by the active media architecture as an AI-generated raster illustration.
- Prompt record: A repository-local Markdown artifact that preserves the exact full prompt text used to generate or revise one generated raster image.
- Prompt summary: A concise `media/PROVENANCE.md` `prompt_or_creation_notes` value that summarizes the prompt or creation context without replacing the exact prompt record.
- Original SVG diagram: A `.svg` file under `media/` classified by the active media architecture as an original educational diagram.
- Declared image purpose: The purpose value or nearby Markdown explanation that identifies whether the image teaches setup, movement, or muscle attention.
- Page-local source support: Citations and source list entries in the same exercise document as the claim being supported.
- Visual-safety review: Human review that checks whether an image remains non-clinical, support-only, license-compatible, non-identifying, and consistent with the Markdown page.

## Examples first

Example E1: text-only exercise page remains valid
Given `exercises/chin-nod.md` is understandable without an image
When the page is validated
Then the page can pass without media references or provenance rows.

Example E2: setup image uses the setup purpose
Given `exercises/thoracic-extension.md` references `../media/exercises/thoracic-extension/setup.png`
And `media/PROVENANCE.md` has an approved row for `media/exercises/thoracic-extension/setup.png`
When media validation checks the row
Then `media_purpose` is `exercise_setup_illustration` and `page_refs` includes `exercises/thoracic-extension.md`.

Example E3: movement image uses the movement purpose
Given `exercises/wall-slide.md` references `../media/exercises/wall-slide/movement.png`
When a reviewer checks the image and nearby Markdown
Then the image teaches a start, end, key position, or movement path and does not introduce unsupported technique claims.

Example E4: muscle-attention image remains broad and support-only
Given `exercises/band-pull-apart.md` references `../media/exercises/band-pull-apart/muscle-attention.png`
When the page is reviewed
Then the image highlights only a broad upper-back or rear-shoulder region, contains no muscle labels, and nearby Markdown carries the muscle names, feel cues, caveats, and citations.

Example E5: too many images require explicit justification
Given an exercise document references four images
When the page is validated for promotion
Then the page fails unless a downstream approved spec or plan records explicit justification for more than three exercise images.

Example E6: wrong-purpose image fails
Given an exercise document references a generated raster image
And the matching provenance row uses `pattern_alignment_illustration`
When exercise-image validation runs
Then the page fails because pattern alignment is not a full exercise-document image purpose.

Example E7: existing exercise image purposes remain compatible
Given an existing exercise document already references a generated raster image with `media_purpose = equipment_identification` or `media_purpose = key_movement_illustration`
When the page is validated under this spec
Then the existing image can remain valid without changing its media purpose.

Example E8: exact prompt record is preserved for a generated raster exercise image
Given `exercises/wall-slide.md` references `../media/exercises/wall-slide/movement.png`
And `media/PROVENANCE.md` has an approved row for `media/exercises/wall-slide/movement.png`
When provenance is reviewed
Then the row's `prompt_record` field is a repository-local prompt-record path such as `media/prompts/exercises/wall-slide/movement.md`
And that prompt record preserves the exact full prompt text used for the accepted image.

Example E9: missing prompt record fails promotion
Given `media/PROVENANCE.md` has an approved generated raster row for `media/exercises/chin-nod/muscle-attention.png`
And the row has no non-blank `prompt_record` value
When generated raster media validation runs after this amendment is implemented
Then the referencing exercise document fails promotion until the exact prompt record is added and linked.

## Requirements

R1. Exercise documents MUST remain valid when they contain no images.

R2. Exercise images MUST be optional support assets for beginner comprehension, not source-of-truth evidence for anatomy, exercise technique, safety, diagnosis, treatment, or programming.

R3. Exercise documents MUST keep setup, movement instructions, muscle names, feel cues, caveats, safety notes, and citations in Markdown text.

R4. Exercise documents MUST use the minimum number of images needed for beginner comprehension.

R5. Exercise documents MUST NOT include more than three exercise images unless a downstream approved spec or plan records explicit justification for the exception.

R6. Each exercise image MUST teach one primary concept: setup, movement, or muscle attention.

R7. New generated raster exercise images MUST use one of these `media/PROVENANCE.md` `media_purpose` values: `exercise_setup_illustration`, `exercise_movement_illustration`, or `exercise_muscle_attention_illustration`.

R8. `exercise_setup_illustration` MUST be used only for equipment setup, grip, stance, bench, wall, floor, or body relationship on an exercise document.

R9. `exercise_movement_illustration` MUST be used only for start position, end position, key position, or movement path on an exercise document.

R10. `exercise_muscle_attention_illustration` MUST be used only for a broad body region or muscle region the reader should notice on an exercise document.

R11. An exercise document MUST NOT include more than one `exercise_muscle_attention_illustration`.

R12. Exercise muscle-attention images MUST highlight broad regions rather than precise anatomy.

R13. Exercise images MUST NOT contain in-image muscle labels, correctness labels, citations, safety warnings, long written cues, diagnosis claims, treatment claims, or warning badges.

R14. Exercise images MUST NOT use red pain marks, injury symbols, bad-versus-fixed framing, before-or-after cure framing, medical-diagram framing, pathology emphasis, exaggerated deformity, shame-based posture comparison, identifiable people, private environments, or misleading brand emphasis.

R15. Exercise images MUST use relative repository-local Markdown references.

R16. Exercise images SHOULD live under `media/exercises/<exercise-slug>/` because subject-co-located media keeps exercise assets and provenance reviewable.

R17. New generated raster exercise images MUST live under `media/exercises/<exercise-slug>/`.

R18. New generated raster exercise image filenames SHOULD describe the image purpose, such as `setup.png`, `movement.png`, or `muscle-attention.png`.

R19. Generated raster exercise images MUST satisfy the active `media/PROVENANCE.md` contract before the referencing exercise document is promoted.

R20. A generated raster exercise image provenance row MUST include non-blank `asset_path`, `asset_type`, `media_purpose`, `prompt_record`, `generator`, `prompt_or_creation_notes`, `created_date`, `human_reviewer`, `license_assertion`, `source_inputs`, `review_status`, `page_refs`, and `notes`.

R20A. A generated raster exercise image provenance row's `prompt_record` value MUST be a repository-local Markdown path to the prompt record that preserves the exact full prompt text for the accepted image.

R20B. A generated raster exercise image prompt record MUST live under `media/prompts/exercises/<exercise-slug>/<asset-stem>.md` unless a downstream approved spec or architecture amendment defines a more specific generated-raster prompt-record location.

R20C. A generated raster exercise image prompt record MUST identify the generated asset path, generator, created date, human reviewer or review owner, review status, and the exact full prompt text.

R20D. A generated raster exercise image prompt record SHOULD record selected-output notes, rejected-variant notes, or revision notes when they materially explain why the accepted image was chosen.

R20E. The exact full prompt text MUST be preserved verbatim except for required privacy or safety redaction.

R20F. If exact prompt text is redacted, the prompt record MUST mark the redaction explicitly and state the reason without exposing private, secret, or unsafe content.

R20G. Prompt records MUST NOT be embedded in reader-facing exercise Markdown.

R20H. `prompt_or_creation_notes` in `media/PROVENANCE.md` MUST remain a concise prompt summary or creation note and MUST NOT be treated as a substitute for the exact prompt record.

R21. A generated raster exercise image provenance row MUST use `asset_type = ai_generated_raster`.

R22. A generated raster exercise image provenance row MUST use `review_status = approved` before the referencing exercise document is promoted.

R23. A generated raster exercise image provenance row MUST include every referencing exercise document in `page_refs`.

R24. The `human_reviewer` field for a generated raster exercise image MUST identify an accountable human maintainer or GitHub handle and MUST NOT identify an AI tool as the reviewer.

R25. Exercise image alt text MUST be present and meaningful enough to identify the exercise context and the image's teaching purpose.

R26. Exercise image alt text MUST NOT be a generic placeholder such as `image`, `exercise image`, `diagram`, `picture`, `photo`, or `illustration` without exercise-specific detail.

R27. Exercise muscle-attention image alt text MUST describe the broad highlighted region without naming exact anatomy that is not also supported in nearby Markdown.

R28. Exercise image alt text, captions, nearby text, provenance notes, and prompt records MUST NOT introduce diagnosis, treatment, cure, individualized coaching, or unsupported safety claims.

R29. Exercise images MUST pass visual-safety review before promotion.

R30. Visual-safety review MUST record whether each reviewed image teaches one concept, matches nearby Markdown, has no in-image text, has no identifying person or misleading brand mark, avoids clinical framing, avoids unsupported claims, and remains color-accessible.

R31. For exercise-image batches that materially change beginner comprehension, review evidence MUST include a beginner comprehension check for purpose, setup or body position, movement steps, what to notice or feel, stop condition, and source verification.

R32. Existing generated raster exercise images using `equipment_identification` or `key_movement_illustration` MAY remain valid without changing their media purpose.

R33. This spec MUST NOT require existing generated raster exercise images to migrate from `equipment_identification` to `exercise_setup_illustration` or from `key_movement_illustration` to `exercise_movement_illustration`.

R34. `pattern_alignment_illustration`, `anatomical_region_illustration`, and `exercise_preview_illustration` MUST NOT be used as full exercise-document image purposes.

R35. Exercise image validation MUST fail promoted exercise documents for remote image references, image paths outside `media/`, unsupported image extensions, missing local image files, missing required alt text, missing required provenance for generated raster images, incomplete provenance, non-approved provenance, missing prompt records, prompt-record asset-path mismatches, out-of-scope `media_purpose`, or `page_refs` mismatch.

R36. Exercise image validation SHOULD report stable failure categories for path, extension, alt-text, provenance, prompt-record, purpose, page-reference, image-count, and visual-safety evidence failures.

R37. Exercise-image changes MUST preserve the repository's no-secrets, no-private-data, and no-private-health-information rules in Markdown, provenance rows, prompt records, prompts or creation notes, review evidence, and validation output.

R38. Exercise-image changes MUST NOT introduce a hosted app, CMS, database, user account, user-input flow, generated public JSON API, video-first media path, or personalized coaching behavior.

## Inputs and outputs

Inputs:

- Exercise Markdown pages under `exercises/`.
- Markdown image references in exercise pages.
- Original SVG diagrams under `media/`.
- Generated raster images under `media/exercises/<exercise-slug>/`.
- `media/PROVENANCE.md` rows for generated raster images.
- Prompt records under `media/prompts/exercises/<exercise-slug>/<asset-stem>.md`.
- Page-local sources and nearby Markdown explanation.
- Visual-safety review evidence.
- Beginner comprehension evidence for material image batches.

Outputs:

- Exercise pages that remain readable directly in Markdown.
- Accepted or rejected exercise image references.
- Approved or rejected generated raster provenance rows.
- Accepted or rejected generated raster prompt records.
- Validation failures for path, extension, alt-text, provenance, purpose, page-reference, image-count, or visual-safety evidence problems.
- Review evidence that records human visual-safety decisions and residual risk.

## State and invariants

- Markdown exercise pages remain the source of truth.
- Text-only exercise pages remain valid.
- Generated raster media is classified before provenance lookup by the active media architecture.
- `media/PROVENANCE.md` remains the central provenance index for generated raster images.
- Exact prompt records remain repository-local audit artifacts linked from provenance rows.
- A generated raster image is promotable only when exactly matched to an approved provenance row by normalized `asset_path`.
- A generated raster image with a prompt-record obligation is promotable only when the provenance row's `prompt_record` path exists, is repository-local, and the prompt record points back to the same normalized `asset_path`.
- Exercise image purpose values are compatibility surfaces once used in promoted provenance rows.
- Exercise images remain subordinate to page-local source support.
- Existing legacy-compatible `equipment_identification` and `key_movement_illustration` rows remain valid without media-purpose migration.

## Error and boundary behavior

- An exercise page with no image references passes exercise-image-specific media checks.
- A generated raster image without an approved exact provenance row fails promotion.
- A generated raster image with `media_purpose = exercise_muscle_attention_illustration` fails when another muscle-attention image is already referenced by the same exercise document.
- A generated raster image with no non-blank `prompt_record` provenance value fails after prompt-record validation is implemented for its provenance row.
- A generated raster image with a `prompt_record` value outside the repository or outside the required prompt-record path shape fails.
- A prompt record whose asset path does not match the generated raster asset path fails.
- A generated raster image with a pattern, condition, preview, vague, or unknown media purpose fails as a full exercise-document image.
- A fourth exercise image fails unless the downstream approved spec or plan records explicit justification.
- A remote image URL fails.
- A path outside `media/` fails.
- A missing local asset fails.
- A supported raster extension outside the generated-raster provenance contract fails.
- Alt text that is missing or generic fails.
- Unsafe visual semantics that cannot be proven mechanically require manual review failure or removal before promotion.

## Compatibility and migration

Existing text-only exercise pages remain valid. Existing original SVG diagrams remain valid when they satisfy general media path and accessibility rules. Existing generated raster exercise images using `equipment_identification` or `key_movement_illustration` remain valid without media-purpose migration.

The new exercise-specific purpose values are additive for new full exercise-document images. They do not remove the Responsible Breadth purposes for pattern, condition, or compact exercise-preview contexts. They do not require migration of existing exercise images.

Prompt-record requirements are additive for generated raster exercise images governed by this spec amendment. Downstream migration planning MUST decide whether and how to backfill exact prompt records for generated raster exercise images that predate this amendment. If exact prompt text is unavailable for an older generated raster image, downstream artifacts MUST either record that limitation explicitly or leave the older image under the pre-amendment provenance compatibility path until a replacement image is generated.

Rollback for a failed image is additive: remove the Markdown image reference, remove the asset when unused, remove or revise the provenance row, keep the text-only page, and rerun validation.

## Observability

- Validation output SHOULD identify the affected Markdown page, normalized asset path, failure category, and relevant provenance field when an exercise image check fails.
- Prompt-record validation output SHOULD identify the affected asset path, `prompt_record` path, failure category, and mismatched or missing field when prompt-record checks fail.
- Visual-safety review evidence MUST identify the reviewed image path, referencing page, review criteria, pass or fail result, reviewer role or handle, and residual risk.
- Beginner comprehension evidence for material image batches MUST identify the exercise pages checked, comprehension prompts or criteria, outcome, and residual confusion without storing private health information.
- Local validation reports MUST name exact commands run and outcomes before completion claims.

## Security and privacy

Exercise-image work MUST NOT commit secrets, private reviewer data, private reader data, private machine paths, private health information, or identifiable images of private people.

Generated image prompts, prompt records, creation notes, provenance rows, review records, and beginner comprehension evidence MUST avoid private or health-identifying information. Review evidence may identify an accountable maintainer or GitHub handle for image approval.

Exercise images MUST NOT imply diagnosis, individualized medical advice, treatment, rehabilitation protocols, posture-correction promises, or personalized coaching.

## Accessibility and UX

Exercise images MUST have meaningful alt text. Nearby Markdown MUST carry the explanatory content needed by readers who cannot see the image. Color MUST NOT be the only way an exercise image communicates its teaching purpose when the distinction is necessary for comprehension.

Exercise pages SHOULD place each image near the Markdown section it supports so readers can connect the visual to the cited text. Images SHOULD avoid visual clutter and should not interrupt the page when text is enough.

## Performance expectations

Exercise-image validation SHOULD remain suitable for local pre-commit-style checks over the repository's Markdown and media files. The spec does not set byte-size limits for image assets, but downstream plans may add file-size or dimension constraints if validation or repository weight becomes a problem.

## Edge cases

EC1. An exercise page contains no images.

EC2. An exercise page references one setup image.

EC3. An exercise page references setup and movement images.

EC4. An exercise page references setup, movement, and muscle-attention images.

EC5. An exercise page references four images without explicit downstream justification.

EC6. An exercise page references two muscle-attention images.

EC7. A generated raster exercise image has no provenance row.

EC8. A generated raster exercise image has a provenance row with missing required fields.

EC8A. A generated raster exercise image has a provenance row but no non-blank `prompt_record` value.

EC8B. A generated raster exercise image has a `prompt_record` value that points outside the repository or outside the required prompt-record path shape.

EC8C. A prompt record exists but points to a different `asset_path`.

EC8D. A prompt record exists but omits exact full prompt text.

EC8E. An older generated raster exercise image predates the prompt-record amendment and exact prompt text is unavailable.

EC9. A generated raster exercise image has `review_status = needs_revision` or `review_status = rejected`.

EC10. A generated raster exercise image has `page_refs` that omit the referencing exercise page.

EC11. A generated raster full exercise-document image uses `pattern_alignment_illustration`, `anatomical_region_illustration`, or `exercise_preview_illustration`.

EC12. A generated raster exercise image uses a vague purpose such as `exercise_image`, `fitness_picture`, or `general_diagram`.

EC13. An existing exercise image uses `equipment_identification` or `key_movement_illustration`.

EC14. A muscle-attention image highlights precise anatomy or includes muscle labels.

EC15. An image contains correct-or-wrong labels, arrows with text, citations, or safety warnings.

EC16. An image depicts pain marks, injury symbols, diagnosis framing, treatment framing, or before-or-after cure framing.

EC17. An image includes a visible brand mark or identifiable private person.

EC18. Alt text is missing or generic.

EC19. Alt text or nearby text makes unsupported diagnosis, treatment, cure, or individualized coaching claims.

EC20. A Markdown image reference points to a remote URL, path outside `media/`, unsupported extension, or missing local file.

## Non-goals

- No immediate image generation.
- No immediate optimization of every exercise page.
- No new exercise inventory.
- No pattern-page, condition-page, video, animation, or hosted visual-delivery standard.
- No stock-photo collection, borrowed web images, commercial-machine screenshots, or decorative image library.
- No runtime app, database, CMS, user account, user-input flow, generated public JSON, hosted media service, or personalized coaching feature.
- No claim that generated images prove anatomy, technique, safety, diagnosis, treatment, rehabilitation, or programming.
- No replacement of Markdown, page-local citations, red-flag routing, or human review.

## Acceptance criteria

AC1. The spec defines additive exercise-specific purpose values for setup, movement, and muscle attention.

AC2. The spec preserves text-only exercise pages as valid.

AC3. The spec limits normal exercise pages to zero through three images and defines failure behavior for four or more images.

AC4. The spec limits muscle-attention images to one per exercise page.

AC5. The spec defines provenance requirements for generated raster exercise images through `media/PROVENANCE.md`.

AC5A. The spec defines exact full prompt preservation requirements for generated raster exercise images through linked repository-local prompt records.

AC6. The spec preserves legacy-compatible `equipment_identification` and `key_movement_illustration` behavior for existing exercise images without requiring media-purpose migration.

AC7. The spec rejects pattern, condition, preview, vague, unknown, or out-of-scope media purposes for full exercise-document images.

AC8. The spec defines alt-text requirements and generic-placeholder failure behavior.

AC9. The spec defines visual-safety requirements that keep images non-clinical, support-only, non-identifying, and free of in-image labels or claims.

AC10. The spec defines automated and manual observability expectations sufficient for a downstream test spec.

AC11. The spec preserves Markdown as source of truth and prohibits generated images as evidence for anatomy, technique, safety, diagnosis, treatment, rehabilitation, or programming.

AC12. The spec does not introduce runtime, hosting, CMS, database, user-input, generated JSON, or personalized coaching behavior.

## Open questions

None blocking spec review.

Downstream artifacts should decide:

- exact checker failure code names;
- exact test fixture filenames;
- whether architecture and ADR updates are amendments or confirmations;
- exact Markdown template wording for optional exercise image blocks;
- exact first-batch prompt language and reviewer handle format.

## Next artifacts

1. Spec review for this exact-prompt preservation amendment.
2. Architecture or ADR assessment to confirm or amend prompt-record placement, provenance linking, and generated-raster validation flow.
3. Test spec amendment mapping prompt-record requirements to automated checks and migration fixtures.
4. Execution plan amendment for prompt-record backfill and checker support after spec review and architecture assessment.

## Follow-on artifacts

- Spec review R1: `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r1.md`
- Spec review R2: `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r2.md`
- Spec review R3: `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r3.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Prompt-record amendment review: `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r3.md`

## Readiness

Approved after spec-review R4 for the prompt-record amendment. This spec does not authorize implementation, image generation, checker changes, provenance edits, prompt-record backfill, or exercise-page edits until required downstream architecture, architecture review, planning, test-spec, and test-spec-review artifacts are complete.
