# Proposal: Advanced Rowing Machine Tutorial Upgrade

## Status

accepted

This proposal records a direction for upgrading GymPrimer's rowing-machine content for more advanced users.
It does not authorize immediate page edits, image generation, prompt records, provenance changes, checker changes, or promotion until proposal review and downstream artifacts approve the work.

## Problem

The current `rowing-machine.md` page is beginner-oriented.
It explains the rowing machine as cardio equipment with a skill component, teaches setup, the basic stroke sequence, broad muscle roles, beginner mistakes, and a simple `basic_cardio_equipment` starting method.

That page is valuable, but it does not yet serve readers who already understand the beginner stroke and want to improve technique, pacing, rhythm, monitor literacy, drag-factor use, interval structure, and performance consistency.

Advanced rowing-machine users need guidance on:

- how to improve stroke efficiency without simply rowing harder;
- how stroke rate, split, watts, and drag factor relate;
- how to use the PM5 monitor as feedback;
- how to use force-curve feedback without overinterpreting it;
- how to structure steady rows, intervals, rate ladders, and benchmark preparation;
- how to avoid turning the page into a race plan, injury-recovery protocol, or personalized coaching program.

The current page already uses five images and includes setup, muscle-attention, drive, stroke-sequence, and finish-position visuals.
For advanced users, more images may be justified because advanced rowing instruction requires separate visuals for stroke timing, monitor literacy, force curve, rate and power relationships, and interval structure.

## Goals

- Add an advanced rowing-machine tutorial layer without weakening the beginner page.
- Teach advanced rowing as performance literacy, not personalized coaching.
- Explain stroke rate, split or pace per 500m, watts, drag factor, force curve, rhythm and recovery ratio, steady rowing, intervals, rate ladders, and benchmark preparation.
- Preserve the beginner page as the entry point.
- Add a separate advanced page or clearly separated advanced section.
- Use more high-quality images where they teach distinct advanced concepts.
- Keep all numeric targets, workout examples, safety rules, and caveats source-backed.
- Keep images subordinate to Markdown, citations, alt text, prompt records, and provenance.
- Define a force-intensity visual system that uses color intensity, outline, and texture to show relative muscular effort across rowing phases.
- Preserve accessibility by ensuring force intensity is not conveyed by color alone.
- Establish reusable image-instruction packets for generated exercise images.
- Avoid personalized training plans, injury-recovery programming, race coaching, and adaptive programming.

## Non-goals

- No personalized rowing plan.
- No adaptive program based on user input.
- No injury-specific return-to-rowing protocol.
- No back-pain rowing treatment.
- No race guarantee, 2k outcome promise, or competition coaching.
- No elite athlete program.
- No heart-rate-zone prescription unless a future spec explicitly accepts that scope.
- No calculator, tracker, wearable integration, or PM5 data-analysis app.
- No video, animation, form-analysis camera, or hosted media product.
- No borrowed PM5 screenshots, branded screenshots, third-party photos, or identifiable people.
- No exact force measurement, EMG heatmap, biomechanical measurement claim, or claim that color intensity proves correct technique.
- No red pain-map styling or injury-risk heatmap.
- No color-only communication of force levels.
- No in-image text, labels, warnings, or citations unless a later visual-spec exception is approved for monitor diagrams.

## Vision fit

fits the current vision

GymPrimer is now a Markdown-first exercise, movement, and training-literacy primer for a general audience.
The current vision allows advanced technique literacy when it remains static, citation-backed education rather than personalized coaching, clinical care, or sport-specific competition programming.

This proposal fits that direction if "advanced" is narrowly defined as advanced exercise literacy for general readers who have already mastered the beginner rowing page, not as elite rowing coaching, race programming, or personalized performance training.
Proposal review should still confirm the scope boundaries before any spec or implementation relies on the proposal.

## Context

The accepted rowing-machine basics proposal added a beginner-facing rowing-machine direction with setup, stroke phases, broad muscle engagement, beginner method guidance, safety notes, and sources.
It explicitly kept rowing-machine guidance out of injury-recovery programming, sport-specific rowing, all-out interval programming, and personalized conditioning plans.

The existing rowing page already teaches the basic rower workflow: setup, broad muscle roles, stroke sequence, common mistakes, beginner amount guidance, easier and harder versions, and safety notes.
It also uses a phase-linked muscle table, which aligns with GymPrimer's muscle-guidance learning: rowing works well when muscle groups are tied to movement phases such as drive, transfer, finish, and recovery.

Concept2's PM5 documentation explains monitor displays for pace, watts, calories, time, distance, stroke rate, drag factor, and force curve. [Concept2 PM5][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-pm5]
Concept2 also explains that stroke rate is not the same thing as workout intensity; intensity depends on how and when the user applies power, and higher rates can be harder to coordinate well. [Concept2 stroke rate][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-stroke-rate]

British Rowing's indoor-rowing technique page supports the core sequence: drive equals legs, body, arms; recovery equals arms, body, legs.
It also gives a broad power split of 60% legs, 30% body, and 10% arms. [British Rowing technique][local-2026-07-07-advanced-rowing-machine-tutorial-british-rowing-technique]

For training examples, Concept2's 2k training plan uses 5-10 minutes of warm-up, 24-34 strokes per minute during workouts, three rowing workouts per week plus an optional fourth, and very easy rowing as interval rest. [Concept2 2k plan][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-2k-plan]
Concept2's Workout of the Day page frames workouts by intensity, says users can adjust intensity, recommends warm-up and cool-down, and notes that higher stroke rates generally fit shorter workouts while lower rates fit longer workouts. [Concept2 WOD][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-wod]
British Rowing's training-plan page distinguishes beginner, intermediate, advanced, and adaptive plans, including advanced plans for people training four times per week or more and pursuing race fitness or personal-best goals. [British Rowing plans][local-2026-07-07-advanced-rowing-machine-tutorial-british-rowing-plans]

The accepted exercise-image standard says exercise images should teach setup, movement, or muscle attention.
It treats four or more images as outside normal scope and requiring explicit downstream justification.
This proposal provides a candidate justification for an advanced rowing page, but the exception should still be reviewed in a downstream spec or spec amendment before images are generated or promoted.

## Options Considered

### Option A: Expand the existing beginner page only

Add advanced material directly to:

```text
exercises/rowing-machine.md
```

Advantages:

- One page to maintain.
- Users do not need to navigate to a second page.
- Easier internal linking.

Drawbacks:

- The existing page may become too long.
- Beginners may be overwhelmed by stroke-rate, split, watts, force curve, drag factor, and interval details.
- Harder to preserve the current beginner teaching path.

Disposition: rejected as the main approach.

### Option B: Add a separate advanced companion page

Create:

```text
exercises/rowing-machine-advanced.md
```

Keep `exercises/rowing-machine.md` as the beginner page, and link to the advanced page from the end of the beginner page.

Advantages:

- Preserves beginner clarity.
- Allows richer advanced images and sections.
- Makes scope boundaries clearer.
- Easier to review advanced content separately.
- Easier to roll back if advanced scope becomes too broad.

Drawbacks:

- Adds a second rowing page.
- Requires navigation and cross-linking.
- Needs more source and image governance.

Disposition: recommended.

### Option C: Create an advanced rowing program page

Create:

```text
programs/advanced-rowing-machine-program.md
```

Advantages:

- Could directly satisfy advanced users who want structured training.
- Natural place for multi-week progression.

Drawbacks:

- Too close to personalized or race-programming territory.
- Requires heavier method and safety governance.
- Conflicts with the current exercise-method non-goals around advanced sport-specific programming.

Disposition: deferred follow-up.

### Option D: Keep advanced rowing out of GymPrimer

Leave rowing-machine content limited to the existing beginner page.

Advantages:

- Lowest safety and scope risk.
- Keeps GymPrimer narrow.

Drawbacks:

- Misses a clear user request.
- Leaves users with a beginner page but no path to more advanced rowing-machine literacy.
- Does not use the existing rower page as a foundation for a richer skill progression.

Disposition: rejected.

## Recommended Direction

Choose Option B: add a separate advanced rowing-machine companion page.

Recommended path:

```text
exercises/rowing-machine-advanced.md
```

Recommended title:

```md
# Rowing Machine: Advanced Technique and Workouts
```

Add a link at the bottom of the beginner page after downstream approval:

```md
Next: [Advanced rowing machine technique and workouts](rowing-machine-advanced.md)
```

The advanced page should start with a prerequisite note:

```md
Use this page only after you can row 10-15 minutes with a smooth stroke and can explain the sequence: legs -> body -> arms, then arms -> body -> legs.
```

This threshold is an editorial boundary, not a medical or performance qualification.

The advanced rowing page should introduce a reusable force-intensity overlay model for technical exercise images.
The model uses a 0-3 relative scale to show which broad muscle regions are primary, supporting, or lightly controlling each rowing phase.
It remains a teaching aid, not a measurement.

Advanced rowing content teaches concepts and static examples for readers who already understand the beginner stroke.
It does not provide individualized training, racing strategy, return-to-rowing guidance, or performance guarantees.

Recommended page structure:

```md
# Rowing Machine: Advanced Technique and Workouts

## What this page is for
## What this page is not
## Prerequisites
## Advanced setup: damper and drag factor
## Monitor basics: split, watts, stroke rate, and distance
## Rhythm and recovery ratio
## Force curve and power application
## Stroke-rate control
## Workout types
### Steady aerobic rows
### Rate ladders
### Power-per-stroke work
### Intervals
### Benchmark preparation
## Muscles involved
## What you should feel
## Common advanced mistakes
## High-quality image guide
## Force-intensity visual system
## Rowing phase force map
## Safety notes
## Sources
```

### Advanced setup: damper and drag factor

The advanced page should explain that damper setting changes flywheel feel, but drag factor is the more comparable metric between machines.
Concept2 explains that different machines can have different drag-factor ranges at the same damper setting and recommends starting around damper 3-5 while focusing on technique. [Concept2 damper][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-damper]

Recommended page guidance:

```md
Do not use damper 10 as a proof of strength. For advanced users, learn what drag factor is and use it to make workouts feel consistent across machines.
```

### Monitor basics

The page should explain PM5 metrics as literacy concepts:

| Metric | What to teach |
| --- | --- |
| Split / pace per 500m | Lower number means faster pace. |
| Watts | Higher watts means more power output. |
| Stroke rate | Number of strokes per minute. |
| Distance/time | Total work target. |
| Force curve | Visual feedback for power application. |

Concept2's PM5 documentation supports pace, watts, calories, time or distance, stroke rate, and force curve as monitor concepts. [Concept2 PM5][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-pm5]

### Rhythm and stroke rate

The advanced page should teach that stroke rate is a tool, not a target to chase blindly.
Concept2 says stroke rate is the number of strokes per minute and that intensity is not determined simply by high cadence. [Concept2 stroke rate][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-stroke-rate]

Recommended page guidance:

```md
Advanced rowing is not just higher stroke rate. First hold technique and pace at lower rates. Then increase rate only when the stroke remains organized.
```

### Force curve

Use the PM5 force curve as technique feedback, but avoid pretending GymPrimer can judge a user's form from a curve.

Recommended page guidance:

```md
The force curve can help you notice whether power is applied smoothly. It is feedback, not a form verdict. Use it together with video review, coaching, or direct technique practice when possible.
```

Concept2 describes the force curve as a graph of power application during the stroke and says it can help improve technique. [Concept2 PM5][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-pm5] [Concept2 understanding PM5][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-understanding-pm5]

### Workout types

Keep workout examples static and educational.

| Workout type | Educational example |
| --- | --- |
| Steady aerobic row | 20-30 minutes easy-to-sustainable effort. |
| Rate ladder | Several short blocks at different stroke rates, focusing on technique. |
| Power-per-stroke practice | Low stroke rate with strong controlled drive. |
| Intervals | Work/rest format such as 3-5 minute repeats, with rest as easy rowing. |
| Benchmark prep | Link to official Concept2 or British Rowing plans instead of writing a full plan. |

Concept2's Workout of the Day examples range from 20-45 minutes and use intensity categories rather than fixed personal paces.
Concept2's 2k plan uses warm-up, 24-34 spm, three weekly rowing workouts plus optional fourth, and easy-rowing rest. [Concept2 WOD][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-wod] [Concept2 2k plan][local-2026-07-07-advanced-rowing-machine-tutorial-concept2-2k-plan]

### Force-intensity visual system

Advanced rowing images may use varying color intensity to show relative muscle effort across stroke phases.

The color system is instructional, not a biomechanical measurement.
It does not show exact force output, EMG activation, injury risk, or whether a reader's form is correct.

Use a four-level relative scale:

| Level | Meaning | Visual treatment |
| ---: | --- | --- |
| 0 | Not emphasized in this phase | neutral body color |
| 1 | Low control or stabilizing role | light tint plus thin outline |
| 2 | Moderate support role | medium tint plus medium outline |
| 3 | Primary effort or main driver | strong tint plus thicker outline or texture |

Force intensity should not be conveyed by color alone.
Every image using this system needs:

- a Markdown legend near the image;
- alt text that names the main emphasized regions;
- a phase table or nearby explanation in Markdown;
- visual differentiation that still works in grayscale.

W3C's Use of Color guidance says color should not be the only visual way to convey information, and its non-text contrast guidance says meaningful parts of graphics need sufficient contrast against adjacent colors. [W3C use of color][local-2026-07-07-advanced-rowing-machine-tutorial-w3c-use-of-color] [W3C non-text contrast][local-2026-07-07-advanced-rowing-machine-tutorial-w3c-non-text-contrast]

Do not use red pain-map styling.
Prefer a single blue/purple intensity scale.
Do not use exact anatomy labels inside body or muscle images.

Recommended Markdown legend:

```md
Color intensity guide:
- Level 0: not emphasized in this phase
- Level 1: low control role
- Level 2: moderate support role
- Level 3: primary effort role

This is a relative teaching guide, not a force measurement.
```

### Rowing phase force map

The advanced rowing page should use this broad phase map as a teaching model:

| Stroke phase | Level 3 primary effort | Level 2 support | Level 1 control |
| --- | --- | --- | --- |
| Catch | none; ready position | trunk posture | arms long, grip relaxed |
| Drive: leg push | legs and glutes | trunk | upper back and arms |
| Drive: body swing | legs/glutes tapering | trunk and hips | upper back and arms |
| Finish | upper back/lats and arms | trunk | legs extended, grip controlled |
| Recovery | none; low effort | trunk and hips | arms, shoulders, and slide control |

The map is relative and educational.
It should be reviewed against the page's cited technique sources and should not be presented as exact force measurement.

### Image-rich advanced tutorial standard

This advanced page should be an explicit image-rich exception if downstream artifacts accept the scope.

The current exercise-image standard generally allows zero to three images and says four or more images require justification.
Advanced rowing may justify more images because it needs separate visuals for monitor data, force curve, rate control, and workout structure, not just body position.

Top image candidates:

| Rank | Image | Purpose | Force-intensity use | Why it matters | Disposition |
| ---: | --- | --- | --- | --- | --- |
| 1 | Advanced stroke sequence with timing emphasis | `exercise_movement_illustration` | yes | Main phase-by-phase muscle-effort map. | Generate first |
| 2 | Drive vs recovery rhythm diagram | `exercise_movement_illustration` | yes, light | Teaches drive effort versus lower-effort recovery control. | Generate first |
| 3 | PM5 metric overview, generic monitor diagram | `exercise_setup_illustration` | no | Helps users understand split, watts, stroke rate, and distance/time without screenshots. | Generate first |
| 4 | Force-curve concept diagram | `exercise_movement_illustration` | yes | Maps smooth force application to the curve concept without making a form verdict. | Generate first |
| 5 | Stroke-rate ladder visual | `exercise_movement_illustration` | optional | Shows rate changes as a training tool without making high rate equal high quality. | Generate first |
| 6 | Drag factor / damper concept visual | `exercise_setup_illustration` | no | Explains damper feel versus measurable drag factor. | Generate first |
| 7 | Low-rate power-per-stroke image | `exercise_movement_illustration` | yes | Teaches low-rate strong drive without rushing stroke rate. | Generate first |
| 8 | Interval structure visual | `exercise_movement_illustration` | no | Shows work/rest blocks as static examples. | Generate first |
| 9 | Advanced common mistake: rushing the slide | `exercise_movement_illustration` | optional | Useful if beginner and advanced readers still rush recovery. | Later candidate |
| 10 | Advanced common mistake: overleaning finish | `exercise_movement_illustration` | no | Useful if source support and visual clarity are strong. | Later candidate |
| 11 | Warm-up progression visual | `exercise_movement_illustration` | no | Useful, but can be explained in text. | Later candidate |
| 12 | Benchmark-prep overview | `exercise_movement_illustration` | no | Higher risk of becoming a program. | Defer |

Generate eight images first only if the downstream spec accepts the image-rich exception:

```text
media/exercises/rowing-machine-advanced/stroke-timing.png
media/exercises/rowing-machine-advanced/rhythm-ratio.png
media/exercises/rowing-machine-advanced/monitor-metrics.png
media/exercises/rowing-machine-advanced/force-curve.png
media/exercises/rowing-machine-advanced/stroke-rate-ladder.png
media/exercises/rowing-machine-advanced/damper-drag-factor.png
media/exercises/rowing-machine-advanced/power-per-stroke.png
media/exercises/rowing-machine-advanced/interval-structure.png
```

The first batch remains eight images, but only selected images should use force-intensity overlays:

- `stroke-timing.png`;
- `rhythm-ratio.png`;
- `force-curve.png`;
- `power-per-stroke.png`.

`stroke-rate-ladder.png` may use a force-intensity overlay only if downstream review finds it necessary to explain rate versus power.
The monitor, damper/drag-factor, and interval-structure images should not show muscle force intensity.

Each image should have a prompt record and an approved `media/PROVENANCE.md` row.
The accepted per-exercise image-prioritization proposal uses a similar pattern: rank image candidates first, generate only the selected first batch later, and require prompt records, provenance rows, review criteria, and validation before assets become promotable.

Images should have:

- no in-image text unless the focused exercise-image spec explicitly grants a monitor-diagram exception;
- no screenshots of Concept2 PM5 or other branded UI;
- no identifiable person;
- no red pain marks;
- no correct/wrong badges;
- no race-win or elite-athlete framing;
- meaningful alt text;
- nearby Markdown explaining the concept.

Technical diagrams may use a narrow text exception only when labels are necessary and duplicated in Markdown and alt text.
Body, movement, muscle, and force-intensity images should remain label-free.

| Image type | In-image text |
| --- | --- |
| Body / movement / muscle / force-intensity images | no |
| Monitor-metric diagram | minimal labels allowed |
| Force-curve concept diagram | minimal axis or curve labels allowed if duplicated in Markdown |
| Interval structure diagram | minimal labels allowed if duplicated in Markdown |

WCAG 2.2 is the current W3C recommendation for web content accessibility, and the proposal should use it as the downstream accessibility reference for technical diagrams and color-dependent graphics. [WCAG 2.2][local-2026-07-07-advanced-rowing-machine-tutorial-w3c-wcag22]

### Image-instruction packet method

Every generated advanced rowing image should have a small, reviewable image-instruction packet before generation.
Use the prompt-record path as the packet path:

```text
media/prompts/exercises/rowing-machine-advanced/asset-stem.md
```

Recommended packet shape:

```md
# Image instruction packet

Asset path:
media/exercises/rowing-machine-advanced/stroke-timing.png

Page reference:
exercises/rowing-machine-advanced.md

Media purpose:
exercise_movement_illustration

Instructional layer:
force_intensity_overlay

Teaching goal:
Show how relative muscle effort shifts across catch, drive, finish, and recovery.

Force-intensity map:
| Phase | Level 3 | Level 2 | Level 1 |
|---|---|---|---|
| Drive | legs/glutes | trunk | arms/upper back |
| Finish | upper back/lats/arms | trunk | legs |

Visual rules:
- no red pain-map colors
- no in-image text for body or muscle diagrams
- no logos
- no identifiable person
- no correct/wrong badges
- color intensity plus outline or texture
- must work in grayscale

Full prompt:
[exact prompt used for image generation]

Review notes:
[filled after visual review]
```

Future image-heavy exercise documents should use this workflow:

1. Write the teaching goal.
2. Write the force/intensity map when relevant.
3. Write the exact prompt.
4. Generate the image through the governed image workflow.
5. Review the image for one teaching purpose, visual safety, source fit, and accessibility.
6. Add provenance.
7. Add Markdown integration with image reference, alt text, nearby explanation, legend, and source citations.
8. Run validation and manual proof.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
| --- | --- | --- |
| Upgrade rowing-machine tutorials | in scope | Problem; Recommended Direction |
| Serve advanced users | in scope | Goals; Non-goals; Vision fit |
| Regenerate or create the proposal | in scope | Full proposal |
| Use best practices | in scope | Context; Testing and Verification Strategy; Risks and Mitigations |
| Add more images without hesitation if needed | in scope | Image-rich advanced tutorial standard; Scope budget |
| Preserve GymPrimer safety boundaries | in scope | Non-goals; Risks and Mitigations |
| Use color intensity for rowing muscle effort | in scope | Force-intensity visual system; Rowing phase force map |
| Keep color intensity instructional, not measurement | in scope | Non-goals; Force-intensity visual system |
| Make image instructions reusable | in scope | Image-instruction packet method; Architecture Impact |
| Preserve accessibility for color-coded images | in scope | Force-intensity visual system; Testing and Verification Strategy |

## Scope budget

| Work item | Treatment | Reason |
| --- | --- | --- |
| Advanced rowing companion page | core to this proposal | Main user-facing improvement. |
| Keep beginner page separate | core to this proposal | Prevents beginner overload. |
| PM5 / monitor literacy | core to this proposal | Advanced users need split, watts, stroke rate, and force-curve understanding. |
| Drag factor / damper guidance | core to this proposal | Common advanced rower confusion. |
| Stroke-rate and rhythm guidance | core to this proposal | Central advanced technique topic. |
| Static workout-type examples | core to this proposal | Needed for advanced training literacy. |
| Image-rich exception | same-slice dependency | Eight images exceed the normal exercise-image default and need explicit governance. |
| Force-intensity overlay system | same-slice dependency | Selected advanced rowing images need relative effort emphasis without implying measurement. |
| Image-instruction packets | same-slice dependency | Generated images need teaching goals, force maps, prompts, and review notes before promotion. |
| Prompt records and provenance rows | same-slice dependency | Required by the current media workflow when images are generated. |
| Beginner page link update | same-slice dependency | Provides clean navigation from basic to advanced. |
| Full race plan | out of scope | Too close to sport-specific coaching. |
| Adaptive training or user-input plan | out of scope | Would become personalized programming. |
| Video / animation / form analysis | out of scope | Separate media product. |

## Expected Behavior Changes

After downstream approval and implementation:

- `rowing-machine.md` remains the beginner tutorial.
- `rowing-machine-advanced.md` becomes the advanced companion tutorial.
- Advanced users can learn monitor metrics, drag factor, stroke rate, force curve, rhythm, and workout types.
- The page teaches training literacy without becoming a personal program.
- The project gains an explicit precedent for image-rich technical cardio-equipment pages only if downstream artifacts approve that exception.
- Selected advanced rowing images use a 0-3 force-intensity overlay system as relative instructional emphasis, not measurement.
- Generated images use image-instruction packets that record teaching goal, prompt, visual rules, and review notes.
- Advanced rowing images have prompt records, provenance, and visual-safety review before promotion.

## Architecture Impact

Expected touched surfaces:

| Surface | Impact |
| --- | --- |
| `exercises/rowing-machine.md` | Add link to advanced page. |
| `exercises/rowing-machine-advanced.md` | New advanced companion page. |
| `media/exercises/rowing-machine-advanced/` | New generated image directory if images are approved. |
| `media/prompts/exercises/rowing-machine-advanced/` | Image-instruction packets and prompt records for generated images if images are approved. |
| `media/prompts/exercises/rowing-machine-advanced/*.md` | Stores image-instruction packets with exact prompts and force-intensity maps where applicable. |
| `media/PROVENANCE.md` | New rows for advanced rowing images if images are approved; notes may record `instructional_layer = force_intensity_overlay` where relevant. |
| `SOURCES.md` | Add reused Concept2 / British Rowing advanced sources if reused. |
| `specs/exercise-image-standard.md` | Add explicit image-rich exception for technical cardio-equipment pages, force-intensity overlay rules, accessibility constraints, and grayscale review expectations if accepted. |
| `specs/exercise-method-guidance.md` | Confirm advanced `basic_cardio_equipment` examples remain static and non-prescriptive. |
| `tools/checks/check_markdown_first.py` | No change unless image-count exception, prompt-record validation, or page-class validation needs new rules. |

No hosted app, runtime API, calculator, tracker, video platform, generated JSON, or personalized coaching engine is needed.

## Testing and Verification Strategy

Automated checks should run over:

```text
exercises/rowing-machine.md
exercises/rowing-machine-advanced.md
media/exercises/rowing-machine-advanced/
media/prompts/exercises/rowing-machine-advanced/
media/PROVENANCE.md
SOURCES.md
RED-FLAGS.md
```

Checks should verify:

- required sections exist;
- citations are page-local;
- reused source IDs appear in `SOURCES.md`;
- no medical-judgment, injury-recovery, treatment, or personalized-program wording;
- image paths are local and relative;
- prompt records exist for generated raster assets;
- provenance rows match exact asset paths;
- `review_status` is approved before promotion;
- alt text is meaningful;
- image-count exception is explicitly approved;
- images declared with `force_intensity_overlay` have an image-instruction packet, Markdown legend, meaningful alt text, matching provenance row, and no forbidden clinical or pain-map wording nearby;
- privacy scan passes.

Manual source audit should sample claims for:

- drag factor versus damper;
- PM5 split, watts, and stroke-rate definitions;
- force-curve explanation;
- stroke-rate guidance;
- 2k benchmark references;
- warm-up and interval-rest language;
- advanced workout-type examples.

Manual visual-safety review should check each advanced image for:

- one teaching purpose;
- no in-image text unless exception approved;
- no brand marks or copied UI;
- no identifiable person;
- no medical, injury-recovery, or pain framing;
- no unsupported performance promise;
- no elite/race-only framing unless explicitly described as benchmark context;
- alt text matching the image.
- color not being the only cue for force intensity;
- intensity levels remaining distinguishable in grayscale;
- force intensity matching the page's phase table;
- no implication of exact measurement, injury risk, or form verdict.

Advanced reader comprehension proof should ask a reader who already understands the beginner page:

- What is split?
- What is stroke rate?
- What is drag factor?
- How is damper different from drag factor?
- What does the force curve help you notice?
- How should rate change across steady rows versus shorter intervals?
- Why is this not a personal training plan?
- Which image helped most?

## Rollout and Rollback

Rollout:

1. Review this proposal.
2. Confirm that advanced rowing remains framed as static exercise literacy under the current vision.
3. Add or amend a spec for an advanced technical-cardio page and image-rich exception.
4. Draft `exercises/rowing-machine-advanced.md`.
5. Add a link from the beginner rower page.
6. Prepare image-instruction packets and top-eight image prompts.
7. Generate images through the governed image workflow.
8. Add prompt records and provenance rows.
9. Run automated checks.
10. Run manual source audit.
11. Run visual-safety and grayscale review.
12. Run advanced reader comprehension proof.

Rollback if advanced scope is too broad:

- keep the beginner `rowing-machine.md`;
- remove the advanced page link;
- archive the draft advanced page;
- keep source notes as future research.

Rollback if eight images are too many:

- keep only stroke timing, PM5 metrics, force curve, stroke-rate ladder, and damper/drag factor;
- defer the rest.

Rollback if workout examples look too much like a plan:

- reduce them to workout type descriptions;
- link out to official Concept2 or British Rowing training plans;
- remove detailed sample sessions.

## Risks and Mitigations

| Risk | Impact | Mitigation |
| --- | ---: | --- |
| Advanced tutorial becomes race coaching | High | Frame as literacy; link official plans instead of writing a full plan. |
| Page becomes personalized programming | High | Static examples only; no user intake, no adaptive progression. |
| Too many images make page noisy | Medium | Top-12 ranking; first batch of eight only if each image teaches a distinct concept. |
| Monitor diagrams copy branded UI | Medium | Use generic diagrams; no screenshots or copied PM5 interface. |
| Force curve is overinterpreted | Medium | Present as feedback, not a form verdict. |
| Stroke-rate guidance becomes prescriptive | Medium | Explain ranges by context; avoid "always use this rate." |
| Drag factor advice becomes over-specific | Medium | Explain concept and consistency; avoid universal target unless sourced. |
| Advanced scope outruns the general-audience vision | High | Keep the page static and literacy-focused; require proposal review before spec. |
| Image provenance incomplete | High | Prompt records and `media/PROVENANCE.md` rows required before promotion. |
| Force-intensity images imply exact force or EMG claims | High | Define the 0-3 scale as relative instructional emphasis only; require Markdown legend and review. |
| Color-only force communication excludes readers | Medium | Require outline, texture, alt text, phase tables, and grayscale review. |
| Technical diagram labels spread into body images | Medium | Allow minimal labels only for monitor, graph, or interval diagrams and duplicate them in Markdown. |

## Open Questions

None blocking proposal review.

Downstream spec or implementation should decide:

- whether advanced rowing needs any extra scope boundary beyond the current general-audience vision: recommended answer is advanced literacy, not advanced coaching;
- whether the page path should be `rowing-machine-advanced.md` or `advanced-rowing-machine.md`: recommended answer is `exercises/rowing-machine-advanced.md`;
- whether to generate all first eight images or reduce to five: recommended answer is keep eight, with force overlays only where they teach something;
- whether monitor diagrams may contain minimal labels or must remain label-free: recommended answer is a narrow technical diagram exception;
- whether `advanced_basic_cardio_equipment` is a method subtype or just a page-level section: recommended answer is keep `basic_cardio_equipment` with advanced literacy examples.

Recommended defaults:

```text
Page path: exercises/rowing-machine-advanced.md
Title: Rowing Machine: Advanced Technique and Workouts
Image batch: eight images
Method type: basic_cardio_equipment, advanced examples only
Force-intensity overlays: selected images only
Technical diagram labels: narrow exception, duplicated in Markdown and alt text
```

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-07 | Add a separate advanced rowing page. | Preserves beginner page while serving advanced readers. | Put all advanced content into the current page. |
| 2026-07-07 | Treat advanced content as literacy, not coaching. | Avoids personalized programming and race-plan scope. | Full race plan, adaptive program. |
| 2026-07-07 | Use more images for advanced rowing only after downstream approval. | Advanced rowing concepts are visual and data-driven, but image count exceeds the normal policy. | Text-only advanced page; generate images directly from chat. |
| 2026-07-07 | Rank 12 image candidates and generate top eight first only if approved. | Gives enough visual support while keeping generation controlled. | Generate images opportunistically. |
| 2026-07-07 | Keep monitor images generic. | Avoids copying PM5 UI or branded screenshots. | Use screenshots or branded monitor graphics. |
| 2026-07-07 | Add a force-intensity overlay system for selected rowing images. | Advanced rowing needs to show relative effort across stroke phases, but the page must avoid exact force or EMG claims. | Plain muscle highlights only; exact heatmap-style force claims. |
| 2026-07-07 | Keep force-intensity information out of color alone. | Accessibility and comprehension require non-color cues, Markdown legend, and alt text. | Color-only force scale. |
| 2026-07-07 | Use image-instruction packets before generation. | Prompt records should include teaching goal, force map, visual rules, prompt text, and review notes before assets are approved. | Generate images first and document after the fact. |
| 2026-07-07 | Allow minimal in-image text only for monitor and graph diagrams. | Technical diagrams may need labels, but body and muscle images should remain label-free. | Ban all diagram labels; allow labels everywhere. |

## Next Artifacts

1. Proposal review.
2. Focused spec or spec amendment for:
   - advanced rowing page contract;
   - image-rich technical-cardio exception;
   - advanced `basic_cardio_equipment` wording boundaries.
3. Prompt set for the first approved image batch.
4. Image-instruction packets for generated assets.
5. Draft `exercises/rowing-machine-advanced.md`.
6. Prompt records for generated assets.
7. `media/PROVENANCE.md` rows for generated assets.
8. Manual source audit.
9. Manual visual-safety and grayscale review.
10. Advanced reader comprehension proof.

## Follow-on Artifacts

None yet

## Readiness

This proposal was accepted after clean proposal review.

It is not ready for implementation until proposal review confirms the advanced rowing-machine literacy boundary under the current general-audience vision.
The first implementation should stay narrow: one advanced rowing companion page, one link from the beginner page, source-backed Markdown, and a governed image-rich media batch with prompt records, provenance, visual review, and comprehension proof.

[local-2026-07-07-advanced-rowing-machine-tutorial-concept2-pm5]: https://concept2.com/support/monitors/pm5/how-to-use
[local-2026-07-07-advanced-rowing-machine-tutorial-concept2-stroke-rate]: https://concept2.com/blog/rowing-stroke-rate-explained
[local-2026-07-07-advanced-rowing-machine-tutorial-british-rowing-technique]: https://www.britishrowing.org/indoor-rowing/go-row-indoor/how-to-indoor-row/british-rowing-technique/
[local-2026-07-07-advanced-rowing-machine-tutorial-concept2-2k-plan]: https://concept2.com/training/plans/2k-erg-test-12-week
[local-2026-07-07-advanced-rowing-machine-tutorial-concept2-wod]: https://concept2.com/training/wod
[local-2026-07-07-advanced-rowing-machine-tutorial-british-rowing-plans]: https://www.britishrowing.org/indoor-rowing/go-row-indoor/how-to-indoor-row/british-rowing-training-plans/
[local-2026-07-07-advanced-rowing-machine-tutorial-concept2-damper]: https://concept2.com/training/articles/damper-setting
[local-2026-07-07-advanced-rowing-machine-tutorial-concept2-understanding-pm5]: https://concept2.com/training/articles/understanding-pm5
[local-2026-07-07-advanced-rowing-machine-tutorial-w3c-use-of-color]: https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html
[local-2026-07-07-advanced-rowing-machine-tutorial-w3c-non-text-contrast]: https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html
[local-2026-07-07-advanced-rowing-machine-tutorial-w3c-wcag22]: https://www.w3.org/TR/WCAG22/
