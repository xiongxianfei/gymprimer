# Spec: Necessary Images and Tai Chi Exercise

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-05-necessary-images-and-tai-chi-exercise.md`
- Proposal review R1: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/proposal-review-r1.md`
- Proposal review R2: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/proposal-review-r2.md`
- Review resolution: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-resolution.md`
- Related exercise-image spec: `specs/exercise-image-standard.md`
- Related exercise-method spec: `specs/exercise-method-guidance.md`
- Related exercise-muscle spec: `specs/exercise-muscle-guidance.md`
- Vision: `VISION.md`
- Constitution: `CONSTITUTION.md`

## Goal and context

This spec defines the observable contract for adding a beginner-facing Tai Chi Basics exercise page and selecting its first generated support images.

The change has two linked behaviors.
First, GymPrimer records a top-10 image candidate pool for the single Tai Chi Basics page.
Second, GymPrimer selects exactly three generated raster images for the first implementation loop: setup, weight shift, and broad muscle attention.

The page remains Markdown-first and citation-backed.
Images are optional support assets, not source-of-truth evidence for technique, anatomy, safety, treatment, or programming.
The first implementation is capped at three images.
Candidates 4-10 are deferred alternatives or future replacement candidates unless a downstream approved spec or plan explicitly justifies a page version with more than three images.

## Glossary

- Tai Chi Basics page: The Markdown exercise page at `exercises/tai-chi-basics.md`.
- Tai Chi image candidate pool: The ranked list of ten possible support images for the Tai Chi Basics page.
- First image batch: The selected top three generated raster images for the first implementation loop.
- Deferred image candidate: A ranked candidate from positions 4-10 that is not part of the first image batch.
- Replacement candidate: A deferred candidate that may replace one of the first three images in a later reviewed revision.
- More-than-three-image exception: A downstream approved spec or plan justification required before the Tai Chi Basics page may publish more than three exercise images.
- Prompt record: A repository-local Markdown record preserving exact prompt text for a generated raster image.
- Visual-safety review: Human review that checks whether an image remains non-clinical, support-only, non-identifying, license-compatible, and consistent with nearby Markdown.

## Examples first

Example E1: first Tai Chi page uses exactly three generated support images
Given `exercises/tai-chi-basics.md` is implemented from this spec
When the page references generated raster exercise images
Then it references exactly these first-batch purposes: `exercise_setup_illustration`, `exercise_movement_illustration`, and `exercise_muscle_attention_illustration`.

Example E2: deferred candidate does not add a fourth image
Given the top-10 candidate pool includes a later chair-supported image
When the first implementation is promoted
Then that deferred candidate is not referenced as a fourth image on the Tai Chi Basics page.

Example E3: later candidate may replace an image
Given a later revision chooses the side-view posture candidate instead of the original setup image
When the page still has no more than three images
Then the revision can proceed through normal downstream spec, plan, test, review, and provenance gates without a more-than-three-image exception.

Example E4: fourth image requires explicit exception
Given `exercises/tai-chi-basics.md` already references three exercise images
When a later change wants to add the chair-supported option as a fourth image
Then that change fails readiness unless a downstream approved spec or plan records explicit justification for exceeding the normal three-image limit.

Example E5: method guidance uses low-load control drill labels
Given the Tai Chi Basics page includes `## How much to do`
When a reader opens that section
Then the page shows `Method type: low_load_control_drill` and visible beginner starting point, effort, rest, progression, and stop guidance.

Example E6: generated image has prompt and provenance records
Given the page references `../media/exercises/tai-chi-basics/weight-shift.png`
When provenance validation runs
Then `media/PROVENANCE.md` has an approved row for `media/exercises/tai-chi-basics/weight-shift.png`
And `media/prompts/exercises/tai-chi-basics/weight-shift.md` exists and points back to the same asset.

Example E7: text-only fallback remains valid after image rollback
Given a generated Tai Chi image fails visual-safety review
When the image reference, unused asset, provenance row, and prompt record are removed or revised
Then the text-only Tai Chi Basics page remains a valid fallback if all Markdown content requirements pass.

## Requirements

R1. The Tai Chi Basics exercise page MUST live at `exercises/tai-chi-basics.md`.

R2. The page title MUST be `# Tai Chi Basics`.

R3. The page MUST be a static beginner exercise page, not a martial-arts curriculum, fall-prevention program, recovery plan, treatment protocol, individualized balance program, or adaptive coaching feature.

R4. The page MUST include these Markdown sections: `What this is for`, `Before you start`, `Setup`, `Muscles involved`, `Movement breakdown`, `What you should feel`, `Common mistakes`, `How much to do`, `Easier version`, `Harder version`, `Safety notes`, and `Sources`.

R5. The movement breakdown MUST stay limited to beginner basics: ready stance, weight shift, simple opening movement, and return to quiet standing.

R6. The page MUST NOT teach a named long form, lineage-specific form, martial application, competition form, combat application, or full Tai Chi curriculum.

R7. The page MUST frame Tai Chi as low-impact mindful movement, coordination practice, relaxed posture and breathing practice, or movement literacy.

R8. The page MUST NOT claim that Tai Chi treats disease, prevents falls for a specific reader, fixes posture, cures pain, replaces medical care, or guarantees a safety outcome.

R9. Setup guidance MUST include a clear flat practice area, non-slip footwear or stable foot contact, small slow movements, and wall or stable-chair support when balance is uncertain.

R10. Safety notes MUST include calm stop-or-pause language for dizziness, chest pain, fainting, unusual shortness of breath, sharp pain, worsening symptoms, loss of balance control, or uncertainty caused by medical condition, medication, injury history, or balance concerns.

R11. Safety and setup claims MUST have page-local source support.

R12. The page MUST use `Method type: low_load_control_drill` in `## How much to do`.

R13. The `## How much to do` section MUST include visible beginner starting point, effort, rest, progression, and stop guidance.

R14. Method guidance MUST be static general education and MUST NOT adapt practice time, movement selection, depth, range, rest, or progression to an individual reader.

R15. The beginner starting point SHOULD use a short, low-effort practice duration such as 3-5 minutes when source support and downstream review accept the wording.

R16. Progression guidance MUST prioritize smoother control and slightly longer practice before larger, deeper, faster, or more complex movement.

R17. The `## Muscles involved` section MUST use broad role-based language.

R18. The `## Muscles involved` section MUST include at least legs/glutes for support and weight transfer, trunk for posture and balance, shoulders/upper back for relaxed arm movement, and feet/ankles for ground contact and balance adjustment.

R19. Muscle guidance MUST avoid exact activation claims and MUST keep muscle names, cues, caveats, and citations in Markdown.

R20. The page MUST include a ranked top-10 image candidate pool for Tai Chi Basics in the governing spec, test spec, plan, or change-local evidence before image generation starts.

R21. The first image batch MUST select exactly three generated raster images from the candidate pool.

R22. The selected first-batch images MUST be `setup.png`, `weight-shift.png`, and `muscle-attention.png` under `media/exercises/tai-chi-basics/`.

R23. The selected setup image MUST use `media_purpose = exercise_setup_illustration`.

R24. The selected weight-shift image MUST use `media_purpose = exercise_movement_illustration`.

R25. The selected muscle-attention image MUST use `media_purpose = exercise_muscle_attention_illustration`.

R26. Candidates 4-10 MUST NOT be treated as approval to publish more than three exercise images on the page.

R27. Candidates 4-10 MAY replace one of the first three images in a later reviewed revision when the page still references no more than three exercise images.

R28. Any page version with more than three exercise images MUST have explicit downstream approved spec or plan justification before implementation.

R29. The page MUST NOT include more than one `exercise_muscle_attention_illustration`.

R30. Every generated raster Tai Chi image MUST have an approved `media/PROVENANCE.md` row before the page is promoted.

R31. Every generated raster Tai Chi image MUST have a repository-local prompt record under `media/prompts/exercises/tai-chi-basics/<asset-stem>.md`.

R32. Every generated raster Tai Chi prompt record MUST preserve exact full prompt text or an explicit redaction note allowed by the exercise-image standard.

R33. Every generated raster Tai Chi image provenance row MUST include `asset_path`, `asset_type`, `media_purpose`, `prompt_record`, `generator`, `prompt_or_creation_notes`, `created_date`, `human_reviewer`, `license_assertion`, `source_inputs`, `review_status`, `page_refs`, and `notes`.

R34. Every generated raster Tai Chi image provenance row MUST use `asset_type = ai_generated_raster` and `review_status = approved` before promotion.

R35. Every generated raster Tai Chi image provenance row MUST list `exercises/tai-chi-basics.md` in `page_refs`.

R36. Tai Chi image alt text MUST be present and meaningful enough to identify the exercise context and teaching purpose.

R37. Tai Chi image alt text MUST NOT be generic placeholder text.

R38. Tai Chi images MUST NOT contain in-image text, labels, Chinese characters, citations, safety warnings, correctness badges, red pain marks, clinical framing, brand marks, identifiable people, or combat framing.

R39. The muscle-attention image MUST highlight broad regions only and MUST NOT use exact anatomy labels or pain/injury marks.

R40. Visual-safety review evidence MUST record whether each selected image teaches one concept, matches nearby Markdown, has no in-image text, has no identifiable person or brand mark, avoids clinical framing, avoids unsupported claims, remains color-accessible, and fits the selected purpose.

R41. Beginner comprehension proof MUST record whether a beginner reader can explain what Tai Chi practice is for, how to stand at the start, what weight shifting means, what to feel in the body, when to pause, and whether the images helped more than text alone.

R42. The implementation MUST preserve a text-only rollback path by allowing removal of image references, unused assets, provenance rows, and prompt records without removing the Tai Chi Basics page.

R43. The change MUST NOT introduce a hosted app, CMS, database, user account, user-input flow, generated public JSON API, video-first media path, personalized coaching behavior, or generated exercise guidance as source of truth.

## Inputs and outputs

Inputs:

- Accepted Tai Chi proposal.
- Existing exercise-image, exercise-method, and exercise-muscle specs.
- Page-local Tai Chi sources.
- Generated raster assets for the first image batch.
- Prompt records for generated raster assets.
- `media/PROVENANCE.md` rows.
- Visual-safety review evidence.
- Beginner comprehension proof evidence.

Outputs:

- `exercises/tai-chi-basics.md`.
- Optional first-batch image references in that Markdown page.
- Generated raster files under `media/exercises/tai-chi-basics/`.
- Prompt records under `media/prompts/exercises/tai-chi-basics/`.
- `media/PROVENANCE.md` rows for generated raster assets.
- Validation failures or pass evidence for page structure, sources, method guidance, media provenance, prompt records, visual review, and privacy.

## State and invariants

- Markdown remains the source of truth for instructions, cues, muscles, safety notes, and citations.
- Text-only Tai Chi Basics remains a valid fallback when images are absent or removed.
- The first implementation references no more than three exercise images.
- Candidates 4-10 remain alternatives unless a downstream approved spec or plan justifies exceeding three images.
- Generated raster images are promotable only after approved provenance and prompt records exist.
- AI-generated images do not establish technique, safety, anatomy, treatment, or programming claims.

## Error and boundary behavior

- Missing required page sections fail page-structure validation.
- Missing page-local source support for safety, setup, method, or movement claims fails content review or validation.
- A fourth exercise image fails unless explicit downstream approved spec or plan justification exists.
- A second muscle-attention image fails.
- A generated raster image without an approved provenance row fails.
- A generated raster image without a matching prompt record fails.
- A prompt record whose asset path does not match the provenance row fails.
- A generated image with out-of-scope purpose fails.
- Remote image references, image paths outside `media/`, unsupported image extensions, missing alt text, or generic alt text fail.
- Unsafe visual semantics require image removal, replacement, or failed review before promotion.

## Compatibility and migration

This spec adds a new exercise page and new media assets.
It does not migrate existing exercise pages or existing media assets.

The public Markdown path `exercises/tai-chi-basics.md` becomes a compatibility surface once published.
The first image asset paths and prompt-record paths become compatibility surfaces once referenced by promoted Markdown and provenance rows.

Rollback is additive: remove Markdown image references, remove or replace failed assets, remove or update provenance rows and prompt records, and keep the text-only page when the text contract passes.

## Observability

- Markdown validation SHOULD identify missing sections, forbidden scope wording, source-index issues, and source-support failures.
- Media validation SHOULD identify asset path, prompt record, provenance, purpose, page-reference, alt-text, and image-count failures.
- Visual-safety review evidence MUST identify reviewed image path, reviewer role or handle, review result, criteria checked, and residual risk.
- Beginner comprehension proof MUST identify the checked page, prompts or criteria, outcome, and residual confusion without storing private health information.
- Local validation reports MUST name exact commands run and outcomes.

## Security and privacy

The change MUST NOT commit secrets, private reviewer data, private reader data, private health information, private machine paths, or identifiable private people.

Generated image prompts, prompt records, provenance rows, visual-review records, and beginner comprehension evidence MUST avoid private or health-identifying information.

The page MUST distinguish general education from personalized care.
It MUST NOT provide individualized medical advice, treatment, recovery programming, diagnosis, or adaptive exercise decisions.

## Accessibility and UX

Images MUST have meaningful alt text.
Nearby Markdown MUST carry the explanation needed by readers who cannot see the image.
Color MUST NOT be the only way a muscle-attention image communicates the teaching purpose.

Images SHOULD appear near the Markdown section they support.
The first image batch SHOULD avoid visual clutter and keep the page readable directly on GitHub.

## Performance expectations

Not applicable for runtime performance.

Repository weight SHOULD remain reasonable for Markdown-first browsing.
Downstream planning MAY define image dimensions or file-size expectations if generated assets become heavy.

## Edge cases

EC1. The Tai Chi page is implemented text-only before generated images are ready.

EC2. The page references exactly the three first-batch images.

EC3. A deferred candidate replaces one of the first-batch images.

EC4. A deferred candidate is added as a fourth image without exception justification.

EC5. A generated image has an approved provenance row but no prompt record.

EC6. A prompt record exists but points to a different asset path.

EC7. The muscle-attention image uses exact anatomy labels.

EC8. The setup image implies therapy, clinic use, or fall-prevention treatment.

EC9. The weight-shift image uses combat framing or correctness badges.

EC10. A beginner comprehension proof records residual confusion about weight shifting.

EC11. The page uses a non-approved method type or omits low-load control labels.

EC12. Source IDs are page-local but reused source IDs are not added to `SOURCES.md` when required.

## Non-goals

- No immediate image generation from this spec alone.
- No implementation without approved downstream plan and test-spec review.
- No full Tai Chi form, martial-arts curriculum, competition form, combat application, or lineage debate.
- No fall-prevention program, recovery plan, medical assessment, symptom-based recommendation, or adaptive coaching.
- No video, animation, camera form analysis, hosted image service, runtime app, database, user account, or user-input flow.
- No borrowed web images, stock photos, commercial screenshots, branded equipment, identifiable people, or decorative hero art.
- No generated image as source-of-truth exercise guidance.

## Acceptance criteria

| Acceptance criterion | Requirements covered |
|---|---|
| AC1. Tai Chi Basics page path, title, required sections, and beginner scope are defined. | R1-R8 |
| AC2. Setup, safety, source-support, method, and muscle guidance contracts are defined. | R9-R19 |
| AC3. Top-10 candidate-pool behavior and first-three image selection are defined without bypassing the three-image limit. | R20-R29 |
| AC4. Generated raster asset, prompt-record, provenance, page-reference, and review-status contracts are defined. | R30-R35 |
| AC5. Alt text and visual-safety boundaries are defined. | R36-R40 |
| AC6. Beginner comprehension proof and text-only rollback are defined. | R41-R42 |
| AC7. Product boundary, security, privacy, accessibility, and no-hosted-app constraints are preserved. | R43; Security and privacy; Accessibility and UX |

## Open questions

None blocking spec review.

Downstream artifacts should decide:

- exact source IDs and whether Tai Chi sources should be added to `SOURCES.md`;
- exact generated-image prompts;
- exact reviewer handle or role for visual-safety review;
- exact beginner comprehension proof artifact path;
- whether the architecture assessment records architecture as required or not required.

## Next artifacts

1. Spec review.
2. Recorded architecture assessment.
3. Architecture and architecture review if required.
4. Execution plan.
5. Plan review.
6. Test spec.
7. Test-spec review.

## Follow-on artifacts

None yet

## Readiness

This spec is ready for spec review.
It does not authorize implementation, image generation, checker changes, provenance edits, prompt-record creation, or page edits until downstream architecture assessment, planning, test specification, and required reviews are complete.
