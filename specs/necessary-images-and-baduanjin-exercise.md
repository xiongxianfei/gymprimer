# Spec: Necessary Images and Baduanjin Exercise

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-06-necessary-images-and-baduanjin-exercise.md`
- Proposal review R1: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/proposal-review-r1.md`
- Related exercise-image spec: `specs/exercise-image-standard.md`
- Related exercise-method spec: `specs/exercise-method-guidance.md`
- Related exercise-muscle spec: `specs/exercise-muscle-guidance.md`
- Vision: `VISION.md`
- Constitution: `CONSTITUTION.md`

## Goal and context

This spec defines the observable contract for adding a beginner-facing Baduanjin Basics exercise page and selecting its first generated support images.

The change has two linked behaviors.
First, GymPrimer records a top-10 image candidate pool for the single Baduanjin Basics page.
Second, GymPrimer selects exactly five generated raster images for the first implementation loop: setup, two-hands lift, drawing bow, alternating reach, and broad muscle attention.

The page remains Markdown-first and citation-backed.
Images are support assets, not source-of-truth evidence for technique, anatomy, safety, treatment, martial form correctness, or programming.
The first implementation is allowed to exceed the normal three-image exercise default only because Baduanjin is a sequence-based gentle-movement page and this spec records the exception.
Candidates 6-10 are deferred alternatives or replacement candidates, not approval to generate or publish all 10 images.

## Glossary

- Baduanjin Basics page: The Markdown exercise page at `exercises/baduanjin-basics.md`.
- Baduanjin image candidate pool: The ranked list of ten possible support images for the Baduanjin Basics page.
- First image batch: The selected top five generated raster images for the first implementation loop.
- Five-image exception: The spec-approved exception allowing this sequence-based exercise page to publish exactly five first-batch exercise images.
- Deferred image candidate: A ranked candidate from positions 6-10 that is not part of the first image batch.
- Prompt record: A repository-local Markdown record preserving exact prompt text for a generated raster image.
- Visual-safety review: Human review that checks whether an image remains non-clinical, support-only, non-identifying, license-compatible, non-combat-framed, and consistent with nearby Markdown.

## Examples first

Example E1: first Baduanjin page uses exactly five generated support images
Given `exercises/baduanjin-basics.md` is implemented from this spec
When the page references generated raster exercise images
Then it references exactly five first-batch images with purposes for setup, movement, movement, movement, and muscle attention.

Example E2: deferred candidates do not add sixth through tenth images
Given the top-10 candidate pool includes look-back, forward-bend, horse-stance fist, heel-raise, and chair-supported candidates
When the first implementation is promoted
Then those deferred candidates are not referenced as additional images on the Baduanjin Basics page.

Example E3: generated image has prompt and provenance records
Given the page references `../media/exercises/baduanjin-basics/drawing-bow.png`
When provenance validation runs
Then `media/PROVENANCE.md` has an approved row for `media/exercises/baduanjin-basics/drawing-bow.png`
And `media/prompts/exercises/baduanjin-basics/drawing-bow.md` exists and points back to the same asset.

Example E4: text-only fallback remains valid after image rollback
Given a generated Baduanjin image fails visual-safety review
When the image reference, unused asset, provenance row, and prompt record are removed or revised
Then the text-only Baduanjin Basics page remains a valid fallback if all Markdown content requirements pass.

Example E5: method guidance uses low-load control drill labels
Given the Baduanjin Basics page includes `## How much to do`
When a reader opens that section
Then the page shows `Method type: low_load_control_drill` and visible beginner starting point, effort, rest, progression, and pause guidance. ([Veterans Affairs][va-tai-chi-qigong])

## Requirements

R1. The Baduanjin Basics exercise page MUST live at `exercises/baduanjin-basics.md`.

R2. The page title MUST be `# Baduanjin Basics`.

R3. The page MUST include the alias line `Also known as: Ba Duan Jin, Eight Pieces of Brocade, 八段锦`.

R4. The page MUST be a static beginner exercise page, not a medical qigong treatment page, martial-arts curriculum, fall-prevention program, recovery plan, individualized balance program, or adaptive coaching feature.

R5. The page MUST include these Markdown sections: `What this is for`, `Before you start`, `Setup`, `Muscles involved`, `Movement breakdown`, `What you should feel`, `Common mistakes`, `How much to do`, `Easier version`, `Harder version`, `Safety notes`, and `Sources`.

R6. The movement breakdown MUST stay limited to beginner basics: ready stance, two hands lift upward, drawing the bow, alternating reach, and return to quiet standing.

R7. The page MUST NOT teach all eight brocades, a lineage-specific form, martial application, combat application, medical protocol, or performance standard.

R8. The page MUST frame Baduanjin as gentle qigong movement, posture and breathing practice, coordination and body-awareness practice, or slow movement literacy.

R9. The page MUST NOT claim that Baduanjin treats disease, prevents falls for a specific reader, cures pain, improves a medical condition, fixes posture, replaces medical care, or guarantees a safety outcome.

R10. Setup guidance MUST include a clear flat practice area, comfortable clothing, non-slip footwear or stable foot contact, small initial movement range, and wall or stable-chair support when balance is uncertain.

R11. Safety notes MUST include calm pause-or-stop language for dizziness, chest pain, fainting, unusual shortness of breath, sharp pain, numbness, weakness, worsening symptoms, loss of balance control, or uncertainty caused by medical condition, medication, injury history, or balance concerns. ([Veterans Affairs][va-tai-chi-qigong])

R12. Safety and setup claims MUST have page-local source support.

R13. The page MUST use `Method type: low_load_control_drill` in `## How much to do`.

R14. The `## How much to do` section MUST include visible beginner starting point, effort, rest, progression, and pause guidance. ([Veterans Affairs][va-tai-chi-qigong])

R15. Method guidance MUST be static general education and MUST NOT adapt practice time, movement selection, depth, range, rest, or progression to an individual reader.

R16. The beginner starting point SHOULD use a short, low-effort practice duration such as 3-5 minutes when source support and downstream review accept the wording.

R17. Progression guidance MUST prioritize smoother control and slightly longer practice before larger, deeper, faster, or more complex movement.

R18. The `## Muscles involved` section MUST use broad role-based language.

R19. The `## Muscles involved` section MUST include at least legs/glutes for support and weight shift, trunk for posture and balance, shoulders/upper back for arm motion, and feet/ankles for foot control.

R20. Muscle guidance MUST avoid exact activation claims and MUST keep muscle names, cues, caveats, and citations in Markdown.

R21. The governing spec, test spec, plan, or change-local evidence MUST include a ranked top-10 image candidate pool for Baduanjin Basics before image generation starts.

R22. The first image batch MUST select exactly five generated raster images from the candidate pool.

R23. The selected first-batch images MUST be `setup.png`, `two-hands-lift.png`, `drawing-bow.png`, `alternating-reach.png`, and `muscle-attention.png` under `media/exercises/baduanjin-basics/`.

R24. `setup.png` MUST use `media_purpose = exercise_setup_illustration`.

R25. `two-hands-lift.png`, `drawing-bow.png`, and `alternating-reach.png` MUST use `media_purpose = exercise_movement_illustration`.

R26. `muscle-attention.png` MUST use `media_purpose = exercise_muscle_attention_illustration`.

R27. The five-image exception MUST apply only to this Baduanjin first batch and MUST NOT change the normal exercise-image limit for other exercise pages.

R28. Candidates 6-10 MUST NOT be treated as approval to publish more than five exercise images on the page.

R29. The page MUST NOT include more than one `exercise_muscle_attention_illustration`.

R30. Every generated raster Baduanjin image MUST have an approved `media/PROVENANCE.md` row before the page is promoted.

R31. Every generated raster Baduanjin image MUST have a repository-local prompt record under `media/prompts/exercises/baduanjin-basics/<asset-stem>.md`.

R32. Every generated raster Baduanjin prompt record MUST preserve exact full prompt text or an explicit redaction note allowed by the exercise-image standard.

R33. Every generated raster Baduanjin image provenance row MUST include `asset_path`, `asset_type`, `media_purpose`, `prompt_record`, `generator`, `prompt_or_creation_notes`, `created_date`, `human_reviewer`, `license_assertion`, `source_inputs`, `review_status`, `page_refs`, and `notes`.

R34. Every generated raster Baduanjin image provenance row MUST use `asset_type = ai_generated_raster` and `review_status = approved` before promotion.

R35. Every generated raster Baduanjin image provenance row MUST list `exercises/baduanjin-basics.md` in `page_refs`.

R36. Baduanjin image alt text MUST be present and meaningful enough to identify the exercise context and teaching purpose.

R37. Baduanjin image alt text MUST NOT be generic placeholder text.

R38. Baduanjin images MUST NOT contain in-image text, labels, Chinese characters, citations, safety warnings, correctness badges, red pain marks, clinical framing, brand marks, identifiable people, weapons, targets, or combat framing.

R39. The muscle-attention image MUST highlight broad regions only and MUST NOT use exact anatomy labels or pain/injury marks.

R40. Visual-safety review evidence MUST record whether each selected image teaches one concept, matches nearby Markdown, has no in-image text, has no identifiable person or brand mark, avoids clinical framing, avoids combat framing, avoids unsupported claims, remains color-accessible, and fits the selected purpose.

R41. Beginner comprehension proof MUST record whether a beginner reader can explain what Baduanjin practice is for, how to stand at the start, what the upward reach teaches, what drawing the bow means on this page, what alternating reach means, what body regions to pay attention to, when to pause, and whether the five images helped more than text alone.

R42. The implementation MUST preserve a text-only rollback path by allowing removal of image references, unused assets, provenance rows, and prompt records without removing the Baduanjin Basics page.

R43. The change MUST NOT introduce a hosted app, CMS, database, user account, user-input flow, generated public JSON API, video-first media path, personalized coaching behavior, or generated exercise guidance as source of truth.

## Inputs and outputs

Inputs:

- Accepted Baduanjin proposal.
- Existing exercise-image, exercise-method, and exercise-muscle specs.
- Page-local Baduanjin and qigong sources.
- Generated raster assets for the first image batch.
- Prompt records for generated raster assets.
- `media/PROVENANCE.md` rows.
- Visual-safety review evidence.
- Beginner comprehension proof evidence.

Outputs:

- `exercises/baduanjin-basics.md`.
- Optional first-batch image references in that Markdown page.
- Generated raster files under `media/exercises/baduanjin-basics/`.
- Prompt records under `media/prompts/exercises/baduanjin-basics/`.
- `media/PROVENANCE.md` rows for generated raster assets.
- Validation failures or pass evidence for page structure, sources, method guidance, media provenance, prompt records, visual review, beginner comprehension, rollback, and privacy.

## State and invariants

- Markdown remains the source of truth for instructions, cues, muscles, safety notes, and citations.
- Text-only Baduanjin Basics remains a valid fallback when images are absent or removed.
- The first implementation references exactly five exercise images when media is promoted.
- The five-image exception is scoped only to this page and first batch.
- Candidates 6-10 remain alternatives unless a later approved artifact revises the image batch.
- Generated raster images are promotable only after approved provenance and prompt records exist.
- AI-generated images do not establish technique, safety, anatomy, treatment, martial-form, or programming claims.

## Error and boundary behavior

- Missing required page sections fail page-structure validation.
- Missing page-local source support for safety, setup, method, or movement claims fails content review or validation.
- A sixth exercise image fails unless a later approved spec or plan records explicit justification.
- A second muscle-attention image fails.
- A generated raster image without an approved provenance row fails.
- A generated raster image without a matching prompt record fails.
- A prompt record whose asset path does not match the provenance row fails.
- A generated image with out-of-scope purpose fails.
- Remote image references, image paths outside `media/`, unsupported image extensions, missing alt text, or generic alt text fail.
- Unsafe visual semantics require image removal, replacement, or failed review before promotion. ([Veterans Affairs][va-tai-chi-qigong])

## Compatibility and migration

This spec adds a new exercise page and new media assets.
It does not migrate existing exercise pages or existing media assets.

The public Markdown path `exercises/baduanjin-basics.md` becomes a compatibility surface once published.
The first image asset paths and prompt-record paths become compatibility surfaces once referenced by promoted Markdown and provenance rows.
The five-image exception is a compatibility surface only for this page's approved first batch.

## Observability

Observable evidence includes the page, source IDs, image references, prompt records, provenance rows, validation output, visual-safety review, beginner comprehension proof, rollback proof, review records, and final validation notes.

## Security and privacy

The change MUST NOT introduce secrets, private contact details, private local paths, private health information, identifiable generated people, or reader health profiles.
Manual proof records MUST be non-identifying.
Prompt records and provenance rows MUST avoid private or secret data.

## Accessibility and UX

Image alt text MUST identify the Baduanjin teaching purpose without replacing the Markdown instructions.
Images SHOULD use clear uncluttered compositions and color choices that remain useful without relying only on color.
The page MUST remain useful as plain Markdown without generated images.

## Performance expectations

No runtime performance budget applies because this is static Markdown and repository-local media.
Local validation SHOULD remain in the same lightweight Python-checker and unittest model used by existing exercise pages.

## Edge cases

- EC1. Text-only Baduanjin page exists before generated images.
- EC2. The page references exactly five first-batch images.
- EC3. Candidate 6-10 is mistakenly added as a sixth image.
- EC4. A second muscle-attention image is added.
- EC5. A drawing-bow image looks like combat training.
- EC6. A forward-bend image is promoted as recovery-care guidance.
- EC7. A prompt record exists but points to a different asset path.
- EC8. Approved provenance exists without a prompt record.
- EC9. Muscle-attention image uses exact anatomy labels or pain marks.
- EC10. Beginner comprehension evidence shows residual confusion about drawing the bow or alternating reach.
- EC11. Method guidance uses a non-approved method type.
- EC12. Reused source IDs are missing from `SOURCES.md` when required.

## Non-goals

- No image generation during spec authoring.
- No full eight-movement Baduanjin course.
- No medical qigong treatment, fall-prevention program, recovery protocol, martial curriculum, lineage teaching, or performance standard.
- No video, animation, camera analysis, hosted media service, app, database, account, tracker, or generated public JSON.
- No borrowed web images, stock photos, commercial screenshots, branded media, or identifiable people.

## Acceptance criteria

| Acceptance criterion | Requirements |
|---|---|
| AC1. Baduanjin Basics page path, title, aliases, sections, and beginner scope are defined. | R1-R9 |
| AC2. Setup, safety, method, and muscle guidance remain static, sourced, and non-clinical. | R10-R20 |
| AC3. Top-10 candidate-pool behavior and first-five image selection are defined with a narrow five-image exception. | R21-R29 |
| AC4. Generated raster assets have approved provenance, exact prompt records, page refs, and meaningful alt text. | R30-R39 |
| AC5. Manual visual-safety, beginner comprehension, rollback, privacy, and excluded-scope proof obligations are defined. | R40-R43 |

## Open questions

None blocking spec review.

Downstream artifacts still need to choose exact prompts, reviewer handle, final page wording, and the evidence format for visual-safety and beginner-comprehension proof.

## Next artifacts

1. Spec review.
2. Architecture update and architecture review for the Baduanjin five-image exception and media flow.
3. Execution plan.
4. Test spec.
5. Test-spec review.
6. Implementation milestones only after the proof map is approved.

## Follow-on artifacts

- Spec review R1: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/spec-review-r1.md`

## Readiness

This spec is approved after spec-review R1 and status settlement in the workflow-managed auto-run.

It is not implementation-ready until architecture, plan, test spec, and their required reviews are complete.

## Sources

- `docs/proposals/2026-07-06-necessary-images-and-baduanjin-exercise.md`
- `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/proposal-review-r1.md`
- `specs/exercise-image-standard.md`
- `specs/exercise-method-guidance.md`
- `specs/exercise-muscle-guidance.md`

[va-tai-chi-qigong]: https://www.va.gov/WHOLEHEALTH/cih/Tai_Chi_and_Qigong.asp
