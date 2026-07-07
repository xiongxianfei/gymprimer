# Spec: Advanced Rowing Machine Tutorial

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-07-advanced-rowing-machine-tutorial.md`
- Proposal review: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/proposal-review-r1.md`
- Review log: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md`
- Related beginner rowing spec: `specs/rowing-machine-basics-and-beginner-workouts.md`
- Related exercise image spec: `specs/exercise-image-standard.md`
- Related exercise method spec: `specs/exercise-method-guidance.md`
- Vision: `VISION.md`
- Constitution: `CONSTITUTION.md`

## Goal and context

This spec defines the observable contract for adding an advanced rowing-machine companion tutorial to GymPrimer.
The advanced page teaches static exercise literacy for readers who already understand the beginner rowing page.

The change preserves `exercises/rowing-machine.md` as the entry point and adds an advanced companion page at `exercises/rowing-machine-advanced.md`.
It teaches monitor literacy, drag factor, rhythm, stroke rate, force curve, workout-type literacy, and selected image-rich technical concepts without becoming individualized coaching, a race plan, clinical care, or a training application.

The advanced page is Markdown-first.
Images, monitor diagrams, force-intensity overlays, prompt records, and provenance are support artifacts.
They do not replace page-local Markdown, citations, safety routing, alt text, or human review.

## Glossary

- Advanced rowing page: The Markdown exercise page at `exercises/rowing-machine-advanced.md`.
- Beginner rowing page: The existing Markdown exercise page at `exercises/rowing-machine.md`.
- Advanced exercise literacy: Static education for readers who already understand the beginner stroke and want clearer concepts, not personalized coaching.
- Split: Pace per 500 meters.
- Stroke rate: Strokes per minute.
- Watts: A monitor output representing power.
- Drag factor: A measurable flywheel-drag value used for comparing feel across machines.
- Damper: The machine setting that changes flywheel feel.
- Force curve: Monitor feedback showing power application during the stroke.
- Force-intensity overlay: A visual layer that uses a 0-3 relative scale for broad muscle effort or attention emphasis.
- Image-instruction packet: A prompt-record Markdown file that records asset path, page reference, media purpose, instructional layer, teaching goal, force map when relevant, visual rules, exact prompt, and review notes.
- Technical diagram exception: A narrow allowance for minimal in-image labels on monitor, graph, or interval diagrams when duplicated in Markdown and alt text.

## Examples first

Example E1: advanced page keeps the beginner page clear
Given `exercises/rowing-machine.md` remains the beginner tutorial
When a reader reaches its ending navigation
Then the page may link to `rowing-machine-advanced.md`
And the beginner page does not absorb advanced monitor, force-curve, or interval detail.

Example E2: advanced page starts with prerequisite boundary
Given `exercises/rowing-machine-advanced.md` exists
When a reader opens the top of the page
Then the page states that it is for readers who can row 10-15 minutes with a smooth stroke
And can explain legs -> body -> arms, then arms -> body -> legs.

Example E3: monitor literacy remains static education
Given the advanced page explains split, watts, stroke rate, distance/time, and force curve
When a reviewer checks the section
Then each metric is explained as a concept
And the page does not calculate personalized paces, targets, or race outcomes.

Example E4: force-intensity overlay avoids measurement claims
Given `stroke-timing.png` uses a force-intensity overlay
When a reviewer checks the image integration
Then nearby Markdown says the 0-3 scale is relative instructional emphasis
And the page does not claim exact force output, EMG activation, injury risk, or correctness.

Example E5: image-instruction packet exists before generated image promotion
Given `media/exercises/rowing-machine-advanced/stroke-timing.png` is referenced
When generated-raster media validation runs
Then `media/prompts/exercises/rowing-machine-advanced/stroke-timing.md` exists
And it records the teaching goal, exact prompt, visual rules, review notes, and force-intensity map when applicable.

Example E6: technical diagram labels are narrow
Given `monitor-metrics.png` or `force-curve.png` needs labels to be understandable
When visual review checks the image
Then minimal labels may appear inside the technical diagram
And the same information appears in Markdown and alt text.

Example E7: workout examples are not programs
Given the page describes steady rows, rate ladders, power-per-stroke work, intervals, and benchmark preparation
When a reviewer checks the wording
Then the examples are static literacy examples
And benchmark preparation links to official plans instead of creating a full plan.

## Requirements

R1. The system MUST preserve `exercises/rowing-machine.md` as the beginner rowing-machine tutorial.

R2. The system MUST add the advanced companion page at `exercises/rowing-machine-advanced.md`.

R3. The advanced page MUST be readable directly as Markdown without generated HTML, JavaScript, video, database, user account, tracker, calculator, or local server.

R4. The beginner page MAY link to the advanced page after downstream approval.

R5. The advanced page MUST include these top-level sections: `## What this page is for`, `## What this page is not`, `## Prerequisites`, `## Advanced setup: damper and drag factor`, `## Monitor basics: split, watts, stroke rate, and distance`, `## Rhythm and recovery ratio`, `## Force curve and power application`, `## Stroke-rate control`, `## Workout types`, `## Muscles involved`, `## What you should feel`, `## Common advanced mistakes`, `## High-quality image guide`, `## Force-intensity visual system`, `## Rowing phase force map`, `## Safety notes`, and `## Sources`.

R6. The prerequisites section MUST state that the page is for readers who can row 10-15 minutes with a smooth stroke and can explain legs -> body -> arms, then arms -> body -> legs.

R7. The prerequisite threshold MUST be framed as an editorial boundary, not as a medical, safety, performance, or eligibility test.

R8. The page MUST frame advanced rowing as static exercise literacy, not personalized coaching.

R9. The page MUST NOT provide individualized training, racing strategy, return-to-rowing guidance, or performance guarantees.

R10. The page MUST explain damper setting and drag factor as related but distinct concepts.

R11. The page MUST NOT present damper 10 as proof of strength, better technique, or inherently better work.

R12. The monitor basics section MUST explain split or pace per 500m, watts, stroke rate, distance/time, and force curve.

R13. Monitor metric explanations MUST remain conceptual and MUST NOT calculate personalized targets or prescribe personal paces.

R14. The rhythm and stroke-rate sections MUST explain that higher stroke rate is not automatically higher quality or higher intensity.

R15. The force-curve section MUST present force curve as feedback for power application and MUST NOT present it as a form verdict.

R16. Workout-type examples MUST be static educational examples.

R17. Benchmark preparation MUST link to official plans or describe the concept without writing a full training plan.

R18. The page MUST use `Method type: basic_cardio_equipment` when it includes method-style rowing examples.

R19. The page MUST NOT introduce `advanced_basic_cardio_equipment` unless a later approved method spec adds that method type.

R20. The page MUST keep page-local sources for concrete claims about damper, drag factor, monitor metrics, stroke rate, force curve, warm-up, interval rest, and workout examples.

R21. Reused source IDs MUST appear in `SOURCES.md` when existing source-index rules require them.

R22. The advanced page is an explicit image-rich exception and MAY use up to eight first-batch generated images after downstream approval.

R23. The first-batch image paths MUST be limited to `media/exercises/rowing-machine-advanced/stroke-timing.png`, `rhythm-ratio.png`, `monitor-metrics.png`, `force-curve.png`, `stroke-rate-ladder.png`, `damper-drag-factor.png`, `power-per-stroke.png`, and `interval-structure.png` unless a later approved artifact changes the batch.

R24. Each advanced image MUST have one primary teaching purpose.

R25. Generated advanced rowing images MUST have approved provenance rows in `media/PROVENANCE.md` before promotion.

R26. Generated advanced rowing images MUST have prompt records under `media/prompts/exercises/rowing-machine-advanced/`.

R27. Prompt records for advanced rowing images MUST function as image-instruction packets.

R28. Image-instruction packets MUST record asset path, page reference, media purpose, instructional layer, teaching goal, visual rules, exact prompt, and review notes.

R29. Image-instruction packets for force-intensity images MUST include a force-intensity map or state why no map is applicable.

R30. `stroke-timing.png`, `rhythm-ratio.png`, `force-curve.png`, and `power-per-stroke.png` MAY use force-intensity overlays.

R31. `stroke-rate-ladder.png` MAY use a force-intensity overlay only if downstream review records why it is needed to explain rate versus power.

R32. `monitor-metrics.png`, `damper-drag-factor.png`, and `interval-structure.png` MUST NOT use muscle force-intensity overlays.

R33. Force-intensity overlays MUST use a 0-3 relative scale.

R34. Force-intensity overlays MUST be described as relative instructional emphasis, not exact force output, EMG activation, injury risk, or proof of correct form.

R35. Force-intensity overlays MUST use color plus at least one non-color visual cue such as outline thickness, texture, opacity, Markdown legend, alt text, or phase table.

R36. Force-intensity images MUST be understandable in grayscale during manual visual review.

R37. Force-intensity images MUST avoid red pain-map styling.

R38. Force-intensity overlays SHOULD prefer a single blue/purple intensity scale unless downstream visual review accepts a different accessible palette.

R39. Body, movement, muscle, and force-intensity images MUST NOT contain in-image labels.

R40. Monitor, graph, and interval technical diagrams MAY use minimal in-image labels only when labels are necessary, duplicated in Markdown, and covered by alt text.

R41. Advanced rowing images MUST NOT use borrowed screenshots, copied PM5 UI, brand marks, identifiable people, correct/wrong badges, red pain marks, elite-race framing, or unsupported performance promises.

R42. Advanced rowing image alt text MUST name the teaching purpose and the main emphasized regions or diagram concepts.

R43. Nearby Markdown MUST include a legend for any force-intensity overlay.

R44. Nearby Markdown MUST include a phase table or explanation for any force-intensity overlay.

R45. Visual-safety review MUST check one teaching purpose, no copied UI, no identifying person, no clinical framing, no unsupported claims, and alt-text fit.

R46. Visual-safety review for force-intensity images MUST check grayscale distinguishability and no exact-measurement implication.

R47. The implementation MUST NOT add a hosted app, runtime API, calculator, tracker, wearable integration, generated public JSON, video platform, or personalized coaching engine.

R48. The implementation MUST NOT introduce medical judgment, individualized medical advice, treatment plans, active recovery protocols, injury-specific protocols, or sport-specific competition programming.

R49. Reader comprehension proof MUST ask advanced-rowing questions about split, stroke rate, drag factor, damper, force curve, rate changes, non-personalized scope, and the most helpful image.

R50. Validation MUST report exact commands and outcomes before any completion claim.

## Inputs and outputs

Inputs:

- Accepted proposal and clean proposal-review record.
- Existing beginner rowing page.
- Related rowing-machine, exercise-image, and exercise-method specs.
- Page-local Concept2, British Rowing, and W3C sources.
- Optional generated images, prompt records, provenance rows, source-index entries, and visual-review evidence.

Outputs:

- `exercises/rowing-machine-advanced.md`.
- A link from `exercises/rowing-machine.md` when downstream approval permits it.
- Optional generated media under `media/exercises/rowing-machine-advanced/`.
- Image-instruction packets under `media/prompts/exercises/rowing-machine-advanced/`.
- `media/PROVENANCE.md` rows for generated raster assets.
- `SOURCES.md` entries for reused sources when required.
- Automated validation output and manual source, visual-safety, grayscale, and reader-comprehension evidence.

No runtime data model, user profile, database, hosted service, generated data package, or user-input flow is introduced.

## State and invariants

- Markdown remains the source of truth.
- The beginner rowing page remains the entry point.
- The advanced page remains a static companion tutorial.
- Images remain support assets and cannot become evidence for exact force, form correctness, safety, or programming.
- Force-intensity overlays are relative teaching aids.
- `basic_cardio_equipment` remains the method type for rowing examples unless a later approved spec changes it.
- Generated media is promotable only with exact prompt records, approved provenance, meaningful alt text, and visual-safety review.
- Page-local source support remains required for concrete technique, monitor, setup, safety, and workout-example claims.

## Error and boundary behavior

- Missing required advanced page sections fail this spec.
- An advanced page that replaces or bloats the beginner page fails the beginner-preservation boundary.
- A page that calculates personalized paces, targets, or training progressions fails the non-personalization boundary.
- A page that provides race strategy or a full benchmark plan fails this spec.
- A force-intensity overlay that implies exact force, EMG activation, injury risk, or correct form fails this spec.
- A force-intensity overlay that relies only on color fails this spec.
- A force-intensity image that collapses into indistinct regions in grayscale fails manual visual review.
- A generated image without exact prompt record, approved provenance, meaningful alt text, or visual-safety review fails promotion.
- A body or muscle image with in-image text labels fails this spec.
- A technical diagram with labels that are not duplicated in Markdown and alt text fails this spec.
- A page that uses copied screenshots, copied PM5 UI, remote images, brand marks, or identifiable people fails media review.
- A page that introduces clinical care, personalized programming, or sport-specific competition programming fails the safety and scope boundary.

## Compatibility and migration

This spec is additive.
It does not remove or rewrite `exercises/rowing-machine.md`.
It adds a companion page and optional link from the beginner page.

The image-rich exception is scoped to `exercises/rowing-machine-advanced.md`.
It does not globally raise the normal exercise-image count limit for other exercise pages.

The force-intensity overlay system is introduced through the advanced rowing page and may later be generalized by an exercise-image spec amendment if downstream review confirms it is reusable.

Rollback is Markdown-first.
If the advanced page is too broad, remove the beginner-page link and keep or archive the draft advanced page.
If eight images are too many, keep only the minimum approved subset.
If force-intensity overlays fail visual review, remove the overlays or remove the affected image references before promotion.

## Observability

Automated validation should report:

- missing required sections;
- missing page-local sources;
- reused sources missing from `SOURCES.md` when required;
- forbidden personalized-programming, clinical, or sport-specific wording;
- local image path failures;
- missing image-instruction packets;
- missing prompt records;
- missing or non-approved provenance rows;
- missing or generic alt text;
- force-intensity overlays without nearby legend;
- force-intensity overlays without packet, phase map, or matching provenance notes when required.

Manual proof must record:

- source audit for damper, drag factor, monitor metrics, stroke rate, force curve, workout-type examples, and safety boundaries;
- visual-safety review for each generated image;
- grayscale review for force-intensity images;
- advanced-reader comprehension outcomes.

Local reports must name exact validation commands and outcomes.
Hosted CI must not be claimed unless a CI run is observed.

## Security and privacy

The advanced page, prompt records, provenance rows, review evidence, and reader-comprehension evidence MUST NOT include secrets, credentials, private reviewer data, private user data, private machine paths, private health information, or identifiable reader-test notes.

The page MUST NOT ask readers for symptoms, medical history, performance goals, body measurements, account details, training logs, wearable data, or PM5 data exports.

Generated image prompts MUST NOT include identifiable people, private settings, third-party screenshots, copied branded UI, or private source material.

## Accessibility and UX

The page MUST be understandable as plain Markdown.

Images MUST have meaningful alt text and nearby Markdown explanation.

Force intensity MUST NOT be conveyed by color alone.

Force-intensity overlays MUST use non-color cues and be manually checked in grayscale.

Technical diagram labels, when allowed, MUST be minimal and duplicated in Markdown and alt text.

The page SHOULD use compact tables where they improve scanability for monitor metrics, phase maps, image roles, and workout types.

Safety routing SHOULD remain calm and visible without overpowering the technical tutorial.

## Performance expectations

No runtime performance requirements apply.
The page remains a static Markdown artifact and must not require a server, build, app, account, or network request to read.

Validation should remain suitable for local repository checks over the changed Markdown, media, prompt-record, provenance, and source-index files.

## Edge cases

EC1. A reader opens the advanced page without reading the beginner page.
The prerequisites section must route expectations back to the beginner stroke sequence.

EC2. A monitor diagram is unreadable without labels.
The technical diagram exception may allow minimal labels if Markdown and alt text duplicate the information.

EC3. A body image needs labels to explain muscle regions.
The image must remain label-free and use Markdown, legend, alt text, and nearby explanation instead.

EC4. A force-intensity overlay looks good in color but not in grayscale.
The image fails manual visual review until revised.

EC5. A force-intensity map conflicts with cited technique sources.
The page must narrow or revise the map before promotion.

EC6. `stroke-rate-ladder.png` is proposed with a force overlay.
The downstream spec, plan, or visual review must record why rate versus power needs that overlay.

EC7. A generated image prompt record exists but lacks the force map for a force-intensity image.
The asset fails the image-instruction packet requirement.

EC8. The page includes 2k benchmark preparation.
It must link to official plans or describe benchmark literacy without creating a full plan.

EC9. The page includes interval examples.
They must remain static examples and must not become adaptive programming.

EC10. Text alone explains one visual concept well enough.
The corresponding image may be deferred or omitted despite being in the candidate list.

EC11. The image-rich exception is cited by another exercise page.
That page still needs its own approved justification unless a later spec generalizes the exception.

EC12. A source supports sport rowing but not indoor-rowing monitor literacy.
The claim must narrow or use a more direct source.

## Non-goals

- No personalized rowing plan.
- No adaptive program based on user input.
- No injury-specific return-to-rowing protocol.
- No back-pain rowing treatment.
- No race guarantee, 2k outcome promise, or competition coaching.
- No elite athlete program.
- No heart-rate-zone prescription.
- No calculator, tracker, wearable integration, PM5 data-analysis app, hosted service, or generated public API.
- No video, animation, form-analysis camera, or media-first product.
- No borrowed PM5 screenshots, branded screenshots, third-party photos, copied UI, or identifiable people.
- No exact force measurement, EMG heatmap, biomechanical measurement claim, injury-risk heatmap, or color-only force scale.
- No global image-count policy change for all exercise pages.
- No new method type named `advanced_basic_cardio_equipment`.

## Acceptance criteria

AC1. The spec-review result confirms that the advanced page contract is clear enough for architecture assessment.

AC2. The spec preserves `exercises/rowing-machine.md` as the beginner tutorial and adds `exercises/rowing-machine-advanced.md` as a companion page.

AC3. The spec defines required advanced page sections and prerequisite boundary.

AC4. The spec defines monitor, drag-factor, rhythm, force-curve, workout-type, and benchmark-preparation boundaries without personal programming.

AC5. The spec defines the eight-image first-batch exception and its exact candidate paths.

AC6. The spec defines force-intensity overlay requirements, including the 0-3 relative scale, non-measurement wording, non-color cues, and grayscale review.

AC7. The spec defines image-instruction packet requirements for generated advanced rowing images.

AC8. The spec defines the narrow technical diagram label exception.

AC9. The spec defines automated and manual validation expectations sufficient for a downstream test spec.

AC10. The spec does not authorize implementation before required downstream architecture assessment, planning, test-spec, review, and verification gates.

## Open questions

None blocking spec review.

Downstream artifacts should decide:

- exact checker failure category names;
- whether force-intensity overlay validation is implemented in existing Markdown-first checks or in a focused media/prompt checker;
- whether `instructional_layer` becomes a structured prompt-record field, a provenance note convention, or both;
- whether the image-rich exception belongs only in this spec or also amends `specs/exercise-image-standard.md`;
- whether architecture requires an ADR amendment for prompt-record packet semantics.

## Next artifacts

1. Spec review.
2. Architecture assessment.
3. Architecture or ADR update if required by the assessment.
4. Plan.
5. Plan review.
6. Test spec.
7. Test-spec review.

## Follow-on artifacts

None yet

## Readiness

This spec is ready for spec review.

It does not authorize implementation, image generation, page edits, provenance edits, checker changes, or promotion until required downstream artifacts and reviews are complete.

## Sources

[local-advanced-rowing-machine-tutorial-spec-proposal]: ../docs/proposals/2026-07-07-advanced-rowing-machine-tutorial.md
[local-advanced-rowing-machine-tutorial-spec-review]: ../docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/proposal-review-r1.md
[local-advanced-rowing-machine-tutorial-spec-rowing-basics]: rowing-machine-basics-and-beginner-workouts.md
[local-advanced-rowing-machine-tutorial-spec-image-standard]: exercise-image-standard.md
[local-advanced-rowing-machine-tutorial-spec-method-guidance]: exercise-method-guidance.md
