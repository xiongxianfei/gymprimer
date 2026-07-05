# Proposal: Brisk Walking and Everyday Walking Guidance

## Status

accepted

This amended proposal records an accepted content-direction decision for adding brisk walking and everyday walking guidance to GymPrimer, including required support images for the brisk walking exercise document. It does not authorize implementation, checker changes, page publication, image generation, navigation promotion, or downstream handoff until required downstream artifacts approve the work.

## Problem

GymPrimer currently teaches exercise literacy through Markdown pages, but walking is not yet clearly represented.

That creates a beginner-content gap. Walking is often the first activity a beginner can perform consistently, but beginners still need guidance on:

- the difference between brisk walking and casual everyday walking;
- what moderate intensity feels like;
- how long to walk at first;
- how to progress without overdoing it;
- what muscles and body regions to pay attention to;
- how walking fits with strength training;
- when walking is enough for the day and when it is only a movement break;
- when to stop and seek help.

This is especially relevant because GymPrimer's accepted exercise-method direction identifies that different training types need different method shapes rather than one universal sets-and-reps line. That proposal defers `basic_cardio_equipment` for treadmill, bike, rower, and similar pages. Walking suggests an adjacent category for basic cardio activity that does not require equipment.

## Goals

- Add a clear GymPrimer standard for brisk walking as a beginner cardio exercise.
- Add a clear standard for everyday walking as daily movement and sitting interruption.
- Explain how beginners can tell whether walking is brisk enough to count as moderate-intensity activity.
- Teach walking method guidance using time, effort, frequency, and progression rather than sets and reps.
- Preserve GymPrimer's Markdown-first, citation-backed, non-clinical content model.
- Keep walking guidance static and educational, not personalized or adaptive.
- Explain muscles involved in beginner-readable, role-based language.
- Clarify that walking complements strength training rather than replacing all strength work.
- Use the proposal as a proof case for a non-equipment cardio-activity method type.
- Add necessary support images to the brisk walking exercise document when they improve exercise comprehension while keeping Markdown as the instructional source of truth.

## Non-goals

- No personalized walking plan.
- No weight-loss prescription.
- No calorie target.
- No step-count mandate such as "everyone must hit 10,000 steps."
- No heart-rate-zone prescription.
- No medical walking program.
- No return-to-walking protocol after injury, surgery, illness, pregnancy, or cardiac events.
- No pain treatment, gait diagnosis, posture correction, or rehabilitation pathway.
- No race-walking technique.
- No running progression.
- No hiking, rucking, loaded walking, treadmill protocol, or incline-walking program in the first slice.
- No tracker app, wearable integration, calculator, dashboard, user input, or adaptive recommendation flow.

## Vision fit

fits the current vision

This proposal fits the Markdown-first GymPrimer direction. It adds static, citation-backed beginner education and does not introduce a hosted app, user-intake flow, personalized coaching, diagnosis, rehabilitation, or generated content as source of truth.

It also aligns with recent project direction around exercise method guidance, muscle guidance, and exercise-image discipline: method guidance should vary by training type, muscle guidance should be role-based and beginner-readable, and images should support Markdown rather than replace it.

## Context

Walking is a low-barrier activity that fits GymPrimer's beginner audience. NHS describes walking as simple and free, says a brisk 10-minute daily walk can count toward the adult weekly exercise target, and explains brisk walking with a pace reference and talk-test language. ([NHS][nhs-walking-for-health])

CDC recommends adults get at least 150 minutes of moderate-intensity physical activity per week and at least two days of muscle-strengthening activity each week. CDC also says activity can be spread out during the week and broken into smaller chunks. ([CDC][cdc-adult-activity])

For intensity, CDC gives two useful beginner anchors:

- brisk walking at 2.5 mph or faster is an example of moderate-intensity activity;
- during moderate-intensity activity, a person can talk but not sing. ([CDC][cdc-physical-activity-intensity])

The American Heart Association similarly recommends 150 minutes per week of moderate-intensity aerobic activity, at least two days per week of muscle-strengthening activity, less sitting, and gradual progression. It also says short brisk walks of five or ten minutes can add up. ([AHA][aha-physical-activity-recommendations])

Mayo Clinic provides direct technique guidance for fitness walking: look forward, relax the neck, shoulders, and back, swing the arms freely, lightly engage the stomach muscles, keep the back straight, and roll smoothly from heel to toe. Mayo also recommends comfortable supportive shoes, safe routes, warming up, cooling down, and slowly building walking time or intensity. ([Mayo Clinic][mayo-walking])

## Options considered

### Option A: Do nothing

Keep walking out of GymPrimer.

Advantages:

- No new content scope.
- No new cardio activity category.
- No need to source walking technique or activity guidance.

Drawbacks:

- Misses one of the most accessible beginner activities.
- Leaves beginners without a clear distinction between casual walking and brisk walking.
- Fails to use walking as an approachable bridge into consistent physical activity.

Disposition: rejected.

### Option B: Add one broad principle page only

Create a page such as:

```text
principles/walking-more-each-day.md
```

This would explain walking in general but not treat brisk walking as an exercise page.

Advantages:

- Simple.
- Low safety risk.
- Good for daily movement and sitting interruption.

Drawbacks:

- Does not give enough page-local exercise guidance for brisk walking.
- Does not answer "how much should I do?" at the point of use.
- Does not test a cardio-activity method type.

Disposition: rejected as the only solution, but useful as part of the recommended direction.

### Option C: Add two complementary pages

Create:

```text
exercises/brisk-walking.md
principles/everyday-walking.md
```

`brisk-walking.md` teaches walking as a deliberate moderate-intensity cardio activity. `everyday-walking.md` teaches walking as daily movement, sitting interruption, and habit-building.

Advantages:

- Separates workout-style brisk walking from ordinary walking.
- Keeps the exercise page practical.
- Keeps the principle page habit-oriented.
- Fits GymPrimer's Markdown-first structure.
- Avoids overloading one page.

Drawbacks:

- Requires two pages instead of one.
- Requires cross-linking to avoid duplication.
- Needs a clear method-type decision.

Disposition: recommended.

### Option D: Add a walking program

Create a full beginner walking program, such as a four-week walking plan.

Advantages:

- Practical for beginners who want structure.
- Easy to follow.

Drawbacks:

- Moves toward programming before the basic walking pages are proven.
- Risks becoming a personalized plan or weight-loss plan.
- Requires more safety and progression governance.

Disposition: deferred follow-up.

## Recommended direction

Choose Option C: add two complementary pages.

### Page 1: `exercises/brisk-walking.md`

Purpose: teach brisk walking as a beginner cardio exercise.

Recommended structure:

```md
# Brisk Walking

## What this is for

## Before you start

## How to know the pace is brisk

## Muscles involved

## Walking technique

## What you should feel

## Common mistakes

## How much to do

## Easier version

## Harder version

## Safety notes

## Sources
```

### Page 2: `principles/everyday-walking.md`

Purpose: teach ordinary walking as daily movement and sitting interruption.

Recommended structure:

```md
# Everyday Walking

## What this is for

## Everyday walking vs. brisk walking

## Ways to add more walking

## How much counts

## What to pay attention to

## Common mistakes

## Safety notes

## Sources
```

### Best-practice content direction

GymPrimer should treat brisk walking and everyday walking as related but different:

| Type | What it means | How to guide beginners |
| --- | --- | --- |
| Brisk walking | A deliberate moderate-intensity walk. CDC lists brisk walking at 2.5 mph or faster as moderate-intensity activity, and the talk test says moderate activity means the person can talk but not sing. ([CDC][cdc-physical-activity-intensity]) | Teach it as a beginner cardio exercise with time, effort, progression, and stop rules. |
| Everyday walking | Normal walking accumulated through daily life: errands, commuting, stairs, walking breaks, parking farther away. | Teach it as movement habit-building and sitting interruption, not necessarily a workout unless intensity rises. |

Brisk walking should be defined by effort, not only speed. Use three beginner checks:

| Check | Beginner explanation |
| --- | --- |
| Talk test | You can talk, but you cannot comfortably sing. |
| Effort | About moderate effort, not a stroll and not an all-out pace. |
| Pace reference | Often around 2.5 mph or faster, but effort matters more than exact pace. |

Everyday walking should be framed as:

- a way to sit less;
- a way to make activity easier to repeat;
- a way to add movement without needing a gym;
- useful even when not brisk enough to count as deliberate moderate-intensity exercise.

Do not imply that every step is the same as a brisk walk. The distinction should be:

> Everyday walking helps you move more. Brisk walking is the version that usually counts as moderate-intensity cardio when the effort is high enough.

### Method guidance

This proposal should introduce a new training type:

```text
basic_cardio_activity
```

Reason: walking is not cardio equipment. The accepted exercise-method proposal includes `basic_cardio_equipment` as a deferred type for treadmill, bike, rower, or similar pages, but walking should not be forced into an equipment category.

| Method type | Use |
| --- | --- |
| `basic_cardio_activity` | Brisk walking, easy outdoor walking, walking breaks, and other non-equipment aerobic activities. |
| `basic_cardio_equipment` | Rower, treadmill, stationary bike, elliptical, and other equipment-based cardio pages. |

Recommended brisk walking starter guidance:

```md
## How much to do

Method type: basic cardio activity

Beginner starting point:
- Start with 5-10 minutes of brisk walking.
- Use the talk test: you should be able to talk, but not sing.
- If that feels manageable, repeat once or twice later in the day or on another day.

Progression:
- First add more total minutes.
- Then add more brisk minutes.
- Then add hills or faster sections if the walk still feels comfortable.

Do not start by turning every walk into a hard workout.
```

This is consistent with CDC and AHA guidance that activity can be accumulated in smaller chunks and that gradual progression is appropriate. ([CDC][cdc-adult-activity]) ([AHA][aha-physical-activity-recommendations])

### Muscle guidance

Walking pages should use role-based muscle guidance, not an anatomy list. This aligns with the accepted muscle-guidance direction: muscle guidance works best when it explains what the muscle group helps do in the movement, using common beginner-readable terms and phase-linked roles where useful.

Suggested `## Muscles involved` for brisk walking:

```md
## Muscles involved

| Role | Muscle region | What it helps do |
|---|---|---|
| Main driver | Glutes, thighs, and calves | Move you forward and push the ground away. |
| Posture / transfer | Trunk | Helps you stay tall and steady as the legs move. |
| Arm swing support | Shoulders and upper back | Helps rhythm and balance without tension. |
| Foot control | Feet and ankles | Help the foot roll smoothly from heel to toe. |
```

Suggested `## What you should feel`:

```md
You should feel warm, more alert, and slightly out of breath, but still able to talk. Your legs and calves may feel like they are working. Your neck, shoulders, and hands should not feel tense.
```

### Technique guidance

Use a concise technique checklist:

- look forward, not down;
- keep neck and shoulders relaxed;
- swing arms naturally;
- keep hands relaxed;
- stay tall without arching the back;
- roll smoothly from heel to toe;
- start easy for a few minutes, then pick up the pace;
- slow down for a few minutes at the end.

This should be source-supported by Mayo Clinic's walking technique guidance. ([Mayo Clinic][mayo-walking])

### Safety guidance

Walking pages should include simple stop rules.

Stop and seek appropriate help if walking causes:

- chest pain;
- fainting or severe dizziness;
- unusual shortness of breath;
- new severe pain;
- numbness, weakness, or neurological symptoms;
- symptoms that worsen or do not settle.

The pages should also route readers to `RED-FLAGS.md`.

Do not add symptom-specific walking advice for chronic disease, pregnancy, post-surgery, injury recovery, or cardiopulmonary conditions in this first slice.

### Image guidance

The brisk walking exercise document should include the necessary support images for a beginner to understand the movement and the broad muscle regions involved.

Images must follow the accepted exercise-image standard: images should teach setup, movement, or muscle attention; remain subordinate to Markdown; avoid in-image labels and clinical framing; and use provenance-backed generated raster assets when generated.

Recommended first-slice media decision:

| Page | Image recommendation |
| --- | --- |
| `exercises/brisk-walking.md` | Required one `exercise_movement_illustration` showing upright posture, arm swing, and heel-to-toe stride; required one `exercise_muscle_attention_illustration` showing broad walking-related attention regions. |
| `principles/everyday-walking.md` | No image needed. |

The movement image should teach visible walking form: upright posture, forward gaze, relaxed neck and shoulders, natural arm swing, relaxed hands, and heel-to-toe stride.

The muscle-attention image should teach broad regions only: glutes, thighs, calves, trunk, shoulders or upper back, and feet or ankles.

Do not add labels, red pain marks, wrong/correct framing, exposed musculature, exact anatomy, clinical framing, or any image that becomes the source of truth for technique, muscles, safety, or programming.

Do not add an image to `principles/everyday-walking.md` in this slice.

## Expected behavior changes

After this proposal is accepted and downstream artifacts are implemented:

- GymPrimer has a direct page for brisk walking.
- GymPrimer has a separate page for everyday walking.
- Beginners can tell the difference between a stroll, everyday walking, and brisk moderate-intensity walking.
- Walking pages use time, effort, and progression rather than sets and reps.
- Brisk walking can serve as the first proof of `basic_cardio_activity`.
- Brisk walking has support images for movement form and broad muscle attention.
- Everyday walking can support the "move more, sit less" message without pretending that every walk is a workout.
- Walking content remains static, general, and non-clinical.

## Architecture impact

Expected touched surfaces:

| Surface | Impact |
| --- | --- |
| `exercises/brisk-walking.md` | New exercise/cardio-activity page. |
| `principles/everyday-walking.md` | New daily-movement principle page. |
| `SOURCES.md` | Add walking, intensity, and activity-guideline sources if reused. |
| `docs/templates/exercise-card.md` | No immediate change unless walking exposes a cardio-activity method need. |
| `specs/exercise-method-guidance.md` or equivalent | Add `basic_cardio_activity` if accepted. |
| `tools/checks/check_markdown_first.py` | No change unless method-type validation is active. |
| `media/exercises/brisk-walking/` | Add required movement and muscle-attention raster images. |
| `media/prompts/exercises/brisk-walking/` | Add exact prompt records for generated raster images. |
| `media/PROVENANCE.md` | Add approved provenance rows for generated raster media. |

No runtime, app, tracker, database, or generated JSON is needed.

## Testing and verification strategy

Automated checks should run existing Markdown-first checks over:

```text
exercises/brisk-walking.md
principles/everyday-walking.md
SOURCES.md
RED-FLAGS.md
```

Likely checks:

- required sections exist;
- page-local citations exist;
- reused source IDs appear in `SOURCES.md`;
- no diagnosis, treatment, rehab, personalized plan, or weight-loss guarantee language;
- internal links resolve;
- privacy scan passes;
- required brisk walking images have local paths, meaningful alt text, prompt records, approved provenance, page references, supported image purpose, and visual-safety evidence.

The project previously found that structural source checks alone are not enough: source IDs need validation against `SOURCES.md`, and semantic source support still needs review for exercise-specific claims.

Manual source review should sample claims about:

- brisk walking intensity;
- talk-test wording;
- 150 minutes per week activity target;
- "move more, sit less" everyday walking framing;
- walking technique cues;
- starter duration and progression guidance;
- stop conditions.

Beginner comprehension proof should ask:

- What is the difference between everyday walking and brisk walking?
- How do you know if the pace is brisk?
- How long would you start with?
- What should your body feel?
- What would make you stop?
- Which source would you click to verify the intensity claim?
- Do the movement and muscle-attention images clarify the page without replacing the written instructions?

A prior GymPrimer review found that general approval from a beginner reader was not enough; manual proof should record per-page comprehension outcomes.

## Rollout and rollback

Rollout should proceed through normal artifact order:

1. Review this proposal.
2. Add `basic_cardio_activity` to the exercise-method contract.
3. Draft or amend the relevant spec before content implementation.
4. Draft `exercises/brisk-walking.md`.
5. Draft `principles/everyday-walking.md`.
6. Add page-local sources and update `SOURCES.md` for reused sources.
7. Add the required brisk walking movement and muscle-attention images with prompt records, provenance rows, alt text, visual-safety evidence, and page references.
8. Run automated checks, manual source review, visual-safety review, and beginner read-test proof before promotion.

Rollback options:

- If the two-page split is too much, keep `exercises/brisk-walking.md`, fold everyday walking into a short section, and defer `principles/everyday-walking.md`.
- If brisk walking method guidance becomes too prescriptive, reduce it to "try 5-10 minutes" and link to a principle page.
- If a walking image is not helpful or fails visual-safety/provenance review, regenerate, revise, or remove that image and re-review the media decision before promotion; reverting the brisk page to text-only requires another approved proposal/spec decision.

## Risks and mitigations

| Risk | Impact | Mitigation |
| --- | ---: | --- |
| Walking page becomes a weight-loss prescription | Medium | Avoid calorie and weight-loss targets; frame health and activity literacy only. |
| Beginner treats casual walking as equivalent to brisk cardio | Medium | Clearly distinguish everyday walking from brisk moderate-intensity walking. |
| Page becomes too medical | High | No disease-specific walking plans; link red flags and route to professionals. |
| Method guidance feels like a personalized plan | Medium | Use "beginner starting point" and general education wording. |
| Step-count claims become overconfident | Medium | Avoid fixed step-count mandates in first slice. |
| Images add little value | Medium | Require only two support images for the exercise page, keep them subordinate to Markdown, and validate them with visual-safety and beginner proof. |
| Muscle-attention image becomes too anatomical or clinical | Medium | Use broad regions only; avoid labels, red marks, exact anatomy, and exposed musculature. |
| Source support is too broad | Medium | Use direct sources for intensity and technique claims. |
| Everyday walking page becomes motivational fluff | Medium | Keep it practical: sitting breaks, short walks, errands, stairs, consistency. |

## Open questions

None blocking proposal-review R2.

Downstream spec or implementation can decide only contract details:

- exact requirement wording for `exercises/brisk-walking.md`;
- exact requirement wording for `principles/everyday-walking.md`;
- exact `basic_cardio_activity` method-contract wording and validation timing;
- source ID naming and `SOURCES.md` reuse details;
- exact asset paths, prompt-record paths, and alt text for the required brisk walking images;
- exact beginner read-test wording.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
| --- | --- | --- |
| Explain best practices for brisk walking | in scope | Recommended direction; Context |
| Explain best practices for everyday walking | in scope | Recommended direction; Context |
| Generate a proposal | in scope | Full proposal |
| Follow best practices | in scope | Context; Testing and verification strategy; Risks and mitigations |
| Fit GymPrimer project direction | in scope | Vision fit; Architecture impact |
| Avoid unsafe medical or personalized guidance | in scope | Non-goals; Safety guidance; Risks and mitigations |
| Add all necessary images for the exercise document | in scope | Image guidance; Architecture impact; Testing and verification strategy |

## Scope budget

| Work item | Treatment | Reason |
| --- | --- | --- |
| Brisk walking page | core to this proposal | Main deliberate exercise/cardio-activity page. |
| Everyday walking page | core to this proposal | Separates daily movement from workout-intensity walking. |
| `basic_cardio_activity` method type | same-slice dependency | Walking does not fit equipment-based cardio cleanly. |
| Walking technique guidance | core to this proposal | Beginners need posture, arm swing, and foot-roll cues. |
| Walking intensity guidance | core to this proposal | Distinguishes brisk walking from strolling. |
| Muscle guidance | same-slice dependency | Walking page should use role-based muscle guidance. |
| Brisk walking movement image | core to this proposal | Helps beginners see posture, arm swing, and heel-to-toe stride. |
| Brisk walking muscle-attention image | core to this proposal | Helps beginners connect the role-based muscle guidance to broad body regions without exact anatomy. |
| Step-count guidance | deferable follow-up | Avoids overcomplicating first slice. |
| Walking program | deferable follow-up | Too prescriptive before basic pages are proven. |
| Treadmill walking page | separate implementation slice | Related but equipment-specific. |
| Running progression | out of scope | Different risk and training category. |
| Medical walking plans | out of scope | Requires clinical governance. |

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-05 | Add walking guidance as two complementary pages. | Separates brisk cardio from daily movement habit-building. | Do nothing; one broad page only; walking program first. |
| 2026-07-05 | Treat brisk walking as `basic_cardio_activity`. | Walking is cardio but not equipment-based. | Force into sets/reps or cardio equipment. |
| 2026-07-05 | Use talk test and moderate-intensity framing. | Directly supported by CDC and NHS and beginner-readable. | Heart-rate zones or calorie targets. |
| 2026-07-05 | Avoid step-count mandates in first slice. | Step targets can distract from intensity and consistency. | 10,000-step rule or fixed daily step prescription. |
| 2026-07-05 | Keep everyday walking as movement habit guidance. | Useful for reducing sitting and building consistency. | Treat every walk as a formal workout. |
| 2026-07-05 | Require two support images for `exercises/brisk-walking.md`. | Maintainer clarified that the exercise document should include all necessary images according to best practices. | Keep brisk walking text-only; add only one optional movement image. |

## Next artifacts

1. Proposal review for this amended image decision.
2. Spec-review R2 resolution and amended spec re-review.
3. Downstream architecture, plan, and test-spec updates as needed.
4. Implement required brisk walking images with prompt records, provenance, and visual-safety proof.
5. Beginner read-test proof before promotion.

## Follow-on artifacts

- Proposal review R1: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/proposal-review-r1.md`
- Proposal review R2: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/proposal-review-r2.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-resolution.md`
- Spec: `specs/brisk-walking-and-everyday-walking.md`
- Spec review R2: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r2.md`

## Readiness

This amended proposal is accepted and ready for spec re-review.

It is not ready for implementation until proposal review accepts the amended image decision and downstream artifacts define or confirm the exact `basic_cardio_activity` contract, the `exercises/brisk-walking.md` page contract, the `principles/everyday-walking.md` page contract, validation timing, source IDs, required image handling, visual-safety proof, and beginner read-test proof.

[cdc-physical-activity-intensity]: https://www.cdc.gov/physical-activity-basics/measuring/index.html
[cdc-adult-activity]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
[aha-physical-activity-recommendations]: https://www.heart.org/en/healthy-living/exercise-and-physical-activity/fitness-basics/aha-recs-for-physical-activity-in-adults
[mayo-walking]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/walking/art-20046261
[nhs-walking-for-health]: https://www.nhs.uk/live-well/exercise/walking-for-health/
