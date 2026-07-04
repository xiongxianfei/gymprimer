# Proposal: Rowing Machine Basics and Beginner Workout Guidance

## Status

accepted

This proposal records a direction for adding rowing-machine education to GymPrimer. It does not authorize page implementation, image generation, checker changes, template changes, or promotion until proposal review and any required downstream artifacts approve the work.

## Problem

GymPrimer teaches exercise, movement, and training literacy through short, citation-backed Markdown pages. The current vision says GymPrimer teaches what an exercise is for, how to set up equipment, what movement should feel like, what common problems may mean in general, how basic training structure works, and when to stop and seek help.

A rowing machine is common gym equipment, but beginners often misuse it because it looks simple while the movement is technical. Common beginner questions include:

- How do I set up the foot straps?
- Is rowing mostly arms, back, or legs?
- What is the correct stroke sequence?
- What does the damper setting do?
- How hard should I row?
- Should I row for time, distance, intervals, or warm-up?
- What muscles should I pay attention to?
- When should I stop?

Without a dedicated rowing-machine page, GymPrimer has no clear place to teach rowing technique, setup, beginner workout method, and cardio-equipment safety.

## Goals

- Add a beginner-facing rowing-machine page to GymPrimer.
- Teach rowing as a skill-based cardio-equipment movement, not just "pulling hard."
- Explain setup, especially foot position, straps, damper, handle, and monitor basics.
- Teach the stroke phases: catch, drive, finish, and recovery.
- Teach the key sequence: drive is legs, then body, then arms; recovery is arms, then body, then legs.
- Explain broad muscle engagement: legs and glutes for the drive, trunk for posture and transfer, and upper back/lats and arms for the finish.
- Add a beginner `How much to do` section using the project exercise-method direction.
- Keep all guidance static, general, and educational.
- Keep citations page-local and authoritative.
- Use images only if they materially improve setup or movement comprehension.
- Keep rowing-machine guidance out of rehab, sport-specific rowing, high-intensity sprint programming, and personalized conditioning plans.

## Non-goals

- No personalized rowing plan.
- No 2k race training plan.
- No sport-rowing performance program.
- No high-intensity sprint protocol for beginners.
- No heart-rate-zone prescription.
- No weight-loss guarantee.
- No pain treatment, rehab plan, return-to-training decision, or diagnosis.
- No claim that rowing replaces all strength training.
- No video-first product.
- No hosted app, calculator, workout tracker, or user-input flow.
- No commercial-machine screenshots or borrowed web images.

## Vision fit

fits the current vision

This proposal fits GymPrimer's current direction. `VISION.md` describes GymPrimer as an open-source Markdown primer for gym beginners, with Markdown as the source of truth and optional media as support.

The rowing-machine page should be a static Markdown education page. It does not require a new product surface, app, database, hosted runtime, account system, coach flow, or personalized intake.

## Context

GymPrimer already has accepted exercise-method guidance that answers the beginner question "How much of this should I do?" by training type. That guidance explicitly defers `basic_cardio_equipment` until carry or cardio-equipment pages exist, so a rowing-machine page is a good first candidate for a focused downstream method amendment.

GymPrimer also has an accepted exercise-image standard. Images should support setup, movement, or muscle attention, remain subordinate to Markdown, avoid in-image labels and clinical framing, and use provenance-backed raster assets when generated. A rowing-machine page is a reasonable candidate for one or two images if text alone is not enough, especially setup and stroke-sequence images.

Technique sources are unusually strong for rowing because Concept2 and British Rowing both publish beginner-accessible technique guidance. Concept2 breaks the stroke into catch, drive, finish, and recovery, and British Rowing gives the memorable sequence "legs, body, arms, arms, body, legs." [Concept2][1] [British Rowing][2]

The safest beginner framing is: learn the stroke sequence first, use moderate or easy effort, keep the recovery controlled, and treat the rower as cardio equipment with skill rather than a random "pull as hard as possible" machine.

## Options considered

### Option A: Do nothing

Leave rowing-machine guidance out of GymPrimer.

Advantages:

- No new content risk.
- No media or method-guidance work.
- No new cardio-equipment category to validate.

Drawbacks:

- Leaves a common gym machine unexplained.
- Misses a clear beginner equipment-use need.
- Keeps `basic_cardio_equipment` method guidance unproven.

Disposition: rejected.

### Option B: Add rowing only as a general principle page

Create a principle page such as:

```text
principles/how-to-use-cardio-equipment.md
```

and mention rowing inside it.

Advantages:

- Simple.
- Avoids detailed rowing technique.
- Could cover treadmill, bike, rower, and elliptical together.

Drawbacks:

- Does not answer rowing-specific setup and technique questions.
- Cannot properly explain drive/recovery sequence.
- Too abstract for a beginner standing in front of a rower.

Disposition: rejected as the main solution, but a later cardio-equipment principle page may be useful.

### Option C: Add a full rowing-machine exercise/equipment page

Create:

```text
exercises/rowing-machine.md
```

with setup, stroke phases, muscles, common mistakes, beginner method, safety notes, and sources.

Advantages:

- Matches the current repository structure.
- Gives beginners a direct page for a common machine.
- Tests the `basic_cardio_equipment` method type.
- Supports future cardio-equipment pages.
- Keeps Markdown as source of truth.

Drawbacks:

- Requires careful source support for setup, technique, and method claims.
- May need images and provenance if visuals are added.
- Must avoid drifting into sport-specific rowing or HIIT programming.

Disposition: recommended.

### Option D: Add a rowing workout program

Create a program page such as:

```text
programs/beginner-rowing-4-week-plan.md
```

Advantages:

- Practical for readers who want structure.
- Could reuse Concept2-style workout progressions.

Drawbacks:

- Moves too quickly into programming.
- Requires more safety and progression governance.
- Not necessary before a basic technique page exists.

Disposition: deferred follow-up.

## Recommended direction

Choose Option C: add a full rowing-machine page.

The first page should be:

```text
exercises/rowing-machine.md
```

The page should teach the rower as a beginner cardio-equipment exercise with a technical movement pattern. It should teach technique first and conditioning second.

Recommended page structure:

```md
# Rowing Machine

## What this is for

## Before you start

## Equipment setup

## Muscles involved

## Movement breakdown

### 1. Catch
### 2. Drive
### 3. Finish
### 4. Recovery

## What you should feel

## Common mistakes

## How much to do

## Easier version

## Harder version

## Safety notes

## Sources
```

Use this as the core instruction:

```text
Drive: legs -> body -> arms
Recovery: arms -> body -> legs
```

Concept2 supports this through its drive and recovery breakdown, and British Rowing states the same sequence explicitly. [Concept2][1] [British Rowing][2]

The setup section should include:

- foot strap crosses the ball or widest part of the foot;
- shins approach vertical at the catch without forcing range;
- grip is relaxed;
- shoulders are low and relaxed;
- spine stays long;
- damper is not a "difficulty level" to max out.

Concept2's foot-position guidance says the strap should cross the ball or widest part of the foot, and its technique page describes catch and drive positions with neutral head, relaxed shoulders, and shins vertical or as close as comfortable. [Concept2][3] [Concept2][1]

The page should explain the damper in plain language:

> The damper changes the feel of the flywheel. It is not a score of how hard you worked. You still create the work with your stroke.

Concept2's damper guidance says the user dictates the power applied in each stroke regardless of damper setting, and it reinforces that proper technique matters at any stroke rate or damper setting. [Concept2][4]

Use the `basic_cardio_equipment` training type after downstream approval or amendment. A safe beginner `How much to do` section could say:

```md
## How much to do

Method type: basic_cardio_equipment

Beginner starting point:
- Start with 3-5 minutes of easy rowing.
- Take a break to walk, breathe, or reset technique.
- If you still feel good, repeat up to four short rounds.

Progression:
- First, make the stroke smoother.
- Then add time.
- Then add moderate effort.
- Do not start by maxing the damper or sprinting.
```

Concept2's beginner workout guidance recommends starting with a 3-5 minute row, taking a break, and doing up to four short intervals if the person feels good. It also gives early stroke-rate experimentation examples at 20, 22, and 24 strokes per minute after technique feels good. [Concept2][8]

The page should include examples, not prescriptions:

| Example | Use |
| --- | --- |
| 3-5 min easy x 1-4 rounds | first exposure / technique practice |
| 10-15 min easy steady row | simple conditioning |
| 3 min easy/moderate intervals with 1 min rest | learning stroke rate and effort |
| 15 min steady row | early beginner cardio session |

Concept2's "Couch to Consistency" plan includes early sessions such as easy/rest intervals, 15 minutes at a steady maintainable pace, and moderate intervals with easy/rest intervals. [Concept2][9]

The page should explain where rowing fits in the week. Rowing can contribute to aerobic activity, but it should not be presented as replacing all strength work; CDC and WHO both recommend adults combine aerobic activity with muscle-strengthening activity on at least two days per week. [CDC][5] [World Health Organization][6]

The page should use standard GymPrimer safety routing:

- stop for chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, or symptoms that worsen;
- stop if technique breaks down and the movement becomes jerky, rushed, or painful;
- link to `RED-FLAGS.md`.

## Expected behavior changes

After this proposal is implemented:

- GymPrimer has a direct rowing-machine page.
- Beginners can learn rower setup without needing a video or app.
- The page explains the stroke sequence in plain language.
- The page gives a safe beginner method for trying rowing.
- The page distinguishes technique practice, steady cardio, and interval examples.
- The page explains that rowing contributes to aerobic training but does not replace all strength training.
- The project has a proof case for `basic_cardio_equipment` method guidance.
- Future treadmill, bike, or elliptical pages can reuse the pattern.

## Architecture impact

Expected touched surfaces:

| Surface | Impact |
| --- | --- |
| `exercises/rowing-machine.md` | New Markdown page. |
| `SOURCES.md` | Add reused rowing sources if they are used across future pages. |
| `docs/templates/exercise-card.md` | No required change unless the rower page exposes a missing cardio-equipment section. |
| `specs/exercise-method-guidance.md` | Focused amendment needed before activating `basic_cardio_equipment`. |
| `media/exercises/rowing-machine/` | Optional images for setup or movement sequence. |
| `media/PROVENANCE.md` | Required only if generated raster images are added. |
| `tools/checks/check_markdown_first.py` | No change unless new method-type validation is added. |
| `RED-FLAGS.md` | No change expected; rower page should link to it. |

No runtime architecture, hosted app, database, user account, workout tracker, or generated output path is needed.

Use images only if they clarify the page.

Recommended first-pass images:

| Image | Purpose |
| --- | --- |
| Setup image | foot strap, seat, handle, catch position |
| Stroke sequence image | catch -> drive -> finish -> recovery |

Do not use:

- commercial machine screenshots;
- borrowed web images;
- branded equipment photos;
- identifiable people;
- red pain marks;
- "wrong/correct" labels;
- in-image text instructions.

If generated raster images are used, they should follow the project's exercise-image standard and have approved provenance.

## Testing and verification strategy

Automated checks should cover the relevant changed files, likely including:

```text
exercises/rowing-machine.md
SOURCES.md
RED-FLAGS.md
media/PROVENANCE.md
```

Expected automated checks:

- required page sections exist;
- source section exists;
- page-local citations exist;
- source IDs are in `SOURCES.md` if reused;
- no forbidden diagnosis, rehab, treatment, or personalized-plan language;
- internal links resolve;
- image paths are local and relative;
- generated raster images have provenance rows if used;
- privacy scan passes.

The project previously found that source-index validation matters: a checker gap allowed a page-local unknown source ID to pass even when missing from `SOURCES.md`, so the rowing page should preserve the global source-index discipline.

Manual review should sample:

- foot setup claim support;
- damper claim support;
- stroke-sequence claim support;
- beginner method claim support;
- `What you should feel` wording;
- stop conditions;
- no sport-performance or HIIT drift;
- beginner comprehension.

A beginner read test should ask:

- What is the rower for?
- Where should the foot strap go?
- What is the drive sequence?
- What is the recovery sequence?
- What should you do first if you are new?
- What would make you stop?
- Which source would you click to verify technique?

This should be recorded as non-identifying evidence, consistent with the project's manual-proof expectations. A prior M3 review found that general approval after images were added was not enough; the manual proof needed per-page comprehension outcomes.

## Rollout and rollback

Rollout:

1. Review and accept this proposal.
2. Confirm whether `basic_cardio_equipment` needs a focused exercise-method spec amendment.
3. Draft `exercises/rowing-machine.md`.
4. Add page-local rowing sources.
5. Add `SOURCES.md` entries for reused sources.
6. Add optional setup/movement images only if needed.
7. Add provenance rows if generated raster images are used.
8. Run Markdown-first, source, privacy, and media checks.
9. Run a manual source-support review.
10. Run a beginner read test before promotion.

Rollback:

- If rowing scope proves too broad, keep the page as draft, remove any README navigation, remove image references and assets, remove provenance rows for unused images, and keep sources in `SOURCES.md` only if reused elsewhere.
- If technique claims cannot be supported cleanly, narrow the page to rowing-machine basics, remove advanced workout examples, and defer intervals to a future principle page.

## Risks and mitigations

| Risk | Impact | Mitigation |
| --- | ---: | --- |
| Page becomes a rowing training plan | Medium | Keep examples static and short; avoid sport goals, 2k tests, or multi-week progression. |
| Beginner rows too hard too soon | High | Technique first; easy starts; no max damper; no beginner sprinting. |
| Setup claims are under-sourced | Medium | Use Concept2 and British Rowing for direct setup/technique claims. |
| Damper is misunderstood as resistance level | Medium | Explain that user effort creates power; cite Concept2 damper guidance. |
| Rowing replaces strength training in reader's mind | Medium | State that rowing supports aerobic work but does not replace the weekly muscle-strengthening guideline. |
| Page becomes too long | Medium | Keep detailed workouts to a later principle page; keep the exercise page concise. |
| Images introduce unsupported technique | High | Keep instructions in Markdown; use images only for setup/movement; review visual semantics manually. |
| Pain or medical advice drift | High | Link red flags; avoid pain-treatment language. |

## Open questions

None blocking proposal review.

Downstream spec or implementation should decide:

- whether the page path is `exercises/rowing-machine.md` or a future `cardio-equipment/rowing-machine.md`;
- whether one setup image is enough or whether a second stroke-sequence image is needed;
- whether `basic_cardio_equipment` needs a focused exercise-method spec amendment before implementation;
- whether rowing examples should remain inside the page or move to a future principle page.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
| --- | --- | --- |
| Explain best practices for using a rowing machine | in scope | Recommended direction; beginner guidance |
| Generate a proposal for GymPrimer | in scope | Full proposal |
| Fit the current project shape | in scope | Vision fit; Context; Architecture impact |
| Keep guidance beginner-safe | in scope | Non-goals; Risks and mitigations; Safety notes |
| Include workout guidance | in scope | Recommended direction; Expected behavior changes |
| Avoid overbroad programming | in scope | Non-goals; Risks and mitigations; Rollout and rollback |
| Use best practices and sources | in scope | Context; Testing and verification strategy; Sources |

## Scope budget

| Work item | Treatment | Reason |
| --- | --- | --- |
| Rowing-machine Markdown page | core to this proposal | Main user-facing deliverable. |
| Technique and setup guidance | core to this proposal | Main safety and comprehension need. |
| Beginner method guidance | core to this proposal | Answers "how much should I do?" for rowing. |
| `basic_cardio_equipment` method type | same-slice dependency | Needed if method guidance validation is active. |
| Setup/movement images | first-slice candidate | Useful if they improve comprehension. |
| Generated image provenance | same-slice dependency | Required if generated raster assets are used. |
| `SOURCES.md` updates | same-slice dependency | Reused rowing sources should be auditable. |
| Beginner read-test evidence | same-slice dependency | Required before promotion for confidence in comprehension. |
| Full rowing training plan | deferable follow-up | Too much for first page. |
| Treadmill/bike/elliptical pages | deferable follow-up | Rowing can prove the cardio-equipment pattern first. |
| Sport rowing performance content | out of scope | Not beginner gym-literacy content. |
| Rehab or pain-specific rowing guidance | out of scope | Requires clinical governance. |

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-04 | Add a rowing-machine page as `exercises/rowing-machine.md`. | Fits current repository structure and gives beginners direct equipment guidance. | Do nothing; principle-only page; full rowing program first. |
| 2026-07-04 | Treat rowing as `basic_cardio_equipment` after downstream approval. | Rowing needs time, effort, technique, and progression guidance rather than normal strength sets/reps. | Force rowing into dynamic resistance sets/reps. |
| 2026-07-04 | Teach technique before conditioning. | Rowing is skill-based; Concept2 and British Rowing emphasize proper sequence and technique. | Start with hard intervals or damper settings. |
| 2026-07-04 | Use static examples, not personalized programs. | Preserves GymPrimer's Markdown-first educational boundary. | Adaptive program, race plan, symptom-based substitutions. |
| 2026-07-04 | Use images only if they teach setup or movement. | Avoids decorative or misleading media. | Image-heavy page or no-media rule. |

## Next artifacts

1. Proposal review.
2. Focused spec amendment for `basic_cardio_equipment`.
3. Draft `exercises/rowing-machine.md`.
4. Source-support review for setup, technique, damper, and method claims.
5. Optional exercise-image plan for setup and stroke-sequence visuals.
6. Test-spec or proof-map update if this is the first `basic_cardio_equipment` page.
7. Beginner read-test record before promotion.

## Follow-on artifacts

- Proposal review: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/proposal-review-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Spec: `specs/rowing-machine-basics-and-beginner-workouts.md`

## Readiness

This proposal was accepted after clean proposal review.

It is not ready for implementation until downstream specification, review, architecture assessment, planning, test specification, and required reviews define the focused path for activating `basic_cardio_equipment`. The first implementation should keep the rowing page narrow: setup, stroke sequence, beginner method, common mistakes, safety notes, and sources.

[1]: https://concept2.com/training/rowing-technique "Indoor Rowing Technique on the Concept2 RowErg"
[2]: https://www.britishrowing.org/indoor-rowing/go-row-indoor/how-to-indoor-row/british-rowing-technique/ "British Rowing Technique - British Rowing"
[3]: https://concept2.com/blog/find-your-optimal-foot-position-on-the-rowerg "Find Your Optimal Foot Position on the RowErg"
[4]: https://concept2.com/blog/what-is-the-best-damper-setting-for-me "What is the Best Damper Setting?"
[5]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html "Adult Activity: An Overview | Physical Activity Basics | CDC"
[6]: https://www.who.int/initiatives/behealthy/physical-activity "Physical activity"
[8]: https://concept2.com/blog/getting-started-try-these-workouts "Getting Started? Try these Workouts"
[9]: https://concept2.com/training/plans/couch-to-consistency "Beginner's Training Plan for Concept2"
