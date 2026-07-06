# Proposal: Safer Running Basics and High-Quality Running Images

## Status

accepted

This proposal records a content and media direction for GymPrimer:

1. add a beginner-facing running page focused on safer running basics;
2. avoid the misleading promise of "injury-free running" while preserving the search intent;
3. request a documented image-count exception for a dynamic running exercise page;
4. evaluate the top 10 necessary running image candidates;
5. choose the top six images as the first generation candidates after downstream approval.

This proposal does not generate images, create the exercise page, update provenance, or authorize implementation by itself.
Image generation should happen later through the governed media workflow after prompts, prompt records, provenance rows, review criteria, and validation expectations are accepted.

## Problem

Beginners often want to start running but do not understand how to reduce injury risk.
Common beginner mistakes include doing too much too soon, skipping rest days, starting with hard continuous running, running every session fast, misunderstanding form cues, and pushing through pain.

GymPrimer does not yet have a running page that explains:

- how to start running safely;
- how run/walk intervals work;
- how often to run at first;
- how to progress distance and time;
- what running effort should feel like;
- what muscles and body regions matter;
- how simple running form cues should look;
- what images can clarify better than text;
- when to stop and seek help. ([Mayo Clinic][mayo-exercise-chronic-disease])

The term "injury-free running" is useful as a user search phrase, but it is not an appropriate page promise.
The page should instead teach safer running basics and explain that injury risk can be reduced but not eliminated.

Running also needs more images than many static exercises.
A machine exercise might need one setup image and one movement image.
Running needs visuals for posture, landing, stride, warm-up, run/walk progression, and muscle attention.
GymPrimer's current exercise-image standard allows multiple images when each image teaches a distinct concept, but it treats more than three exercise images as an exception that needs explicit downstream approved justification.
This proposal requests that justification path for running because running is dynamic, whole-body, commonly misunderstood, and higher-risk when beginners progress too quickly.

## Goals

- Add a new running page candidate: `exercises/safer-running-basics.md`.
- Use the page title `Safer Running Basics`.
- Include the alias line `Also searched as: injury-free running, beginner running, running without getting hurt`.
- Teach running as a beginner cardio activity, not a race plan or injury-treatment protocol.
- Explain run/walk progression, easy effort, rest days, warm-up, load management, simple form cues, muscle guidance, and stop conditions. ([NHS][nhs-couch-to-5k]; [Mayo Clinic Health System][mchs-better-runner]; [Mayo Clinic][mayo-exercise-chronic-disease])
- Request a documented exception to the normal exercise-image count preference.
- Evaluate the top 10 necessary running images.
- Select the top six images as first generation candidates if downstream artifacts approve the exception.
- Keep all instructions, muscle names, safety notes, citations, and progression guidance in Markdown.
- Keep images free of in-image text, labels, pain symbols, medical framing, and correct/wrong badges.
- Require every generated raster image to have an exact prompt record and approved provenance before promotion.

## Non-goals

- No guarantee of injury-free running.
- No return-to-running-after-injury protocol.
- No identifying or treating shin splints, Achilles pain, plantar fasciitis, runner's knee, stress fracture, back pain, or any running-related condition.
- No individualized running plan.
- No race plan, marathon plan, 5K race plan, speed-work plan, hill-speed plan, or interval-performance program.
- No gait-retraining prescription.
- No foot-strike prescription such as "everyone must forefoot strike."
- No shoe-brand recommendation.
- No calorie, fat-loss, or weight-loss target.
- No heart-rate-zone prescription.
- No wearable, pace, cadence, or VO2 calculator.
- No video, animation, camera form analysis, hosted app, user-input flow, or adaptive coaching.
- No borrowed web images, branded images, identifiable people, stock photos, or commercial screenshots.
- No image generation or page implementation from this proposal alone.

## Vision fit

fits the current vision

This proposal fits GymPrimer's Markdown-first direction because it adds a static, citation-backed beginner education page.
It does not introduce medical condition identification, treatment, personalized coaching, a running app, or generated media as source of truth.

The proposal also follows GymPrimer's current image and muscle guidance direction.
Images should clarify setup, movement, or broad muscle attention, while exact instructions, muscle names, cues, caveats, and citations remain in Markdown.

## Context

GymPrimer already has a media direction that supports image-prioritized exercise pages.
The accepted Tai Chi proposal ranks top image candidates, selects a smaller first generation batch, and requires prompt records, provenance, visual-safety review, and beginner comprehension proof before promotion.

The accepted per-exercise image prioritization proposal says each exercise document should receive its own top-10 image-candidate evaluation.
It also preserves the existing exercise-image standard: pages normally use the minimum number of images needed, with more than three images requiring explicit downstream approved justification.
This running proposal provides that exception rationale because running is a whole-body, dynamic, high-frequency beginner activity where text alone can leave important movement and load-management concepts unclear.

Public sources support a conservative beginner-running frame.
NHS Couch to 5K uses a nine-week progression with three runs per week, alternating walking and running, and rest days between runs. ([NHS][nhs-couch-to-5k])
Mayo Clinic Health System recommends that new runners start with low mileage, run three to four times per week, use a run-and-walk program, warm up for at least 3-5 minutes, avoid increasing mileage by more than 10% per week, and use a talk-test style easy-effort check. ([Mayo Clinic Health System][mchs-better-runner])
CDC adult guidelines frame running within broader weekly activity guidance: adults need aerobic activity plus muscle-strengthening activity on at least two days per week. ([CDC][cdc-adult-activity])

Evidence around specific injury-prevention exercises is more cautious than many fitness pages imply.
A 2024 systematic review found that exercise-based interventions did not clearly reduce running-related injury risk or rate compared with running only, and noted that supervision may matter. ([PubMed][pubmed-running-injury-exercise-prevention])
A 2025 scoping review identified strengthening, gait re-education, graduated running programs, footwear, recovery, and education as common injury-risk-reduction topics, while emphasizing support and multifactorial approaches. ([PMC][pmc-running-injury-support])
Therefore, GymPrimer should present strength and form work as capacity and education support, not as guaranteed injury prevention.

## Options Considered

### Option A: Add a page titled "Injury-Free Running"

This would match the user's phrase exactly.

Advantages:

- Strong search-language match.
- Clear user intent.

Drawbacks:

- Implies a guarantee the project cannot make.
- Creates safety and trust risk.
- Could make the page sound like injury-prevention treatment.

Disposition: rejected as the final page title.
Keep it as an alias/search phrase.

### Option B: Add a text-only running page

Create `exercises/safer-running-basics.md` with no images.

Advantages:

- Lowest media burden.
- Fastest writing path.

Drawbacks:

- Running form, overstriding, posture, warm-up movement, and muscle attention are hard to teach through text alone.
- Conflicts with the user's view that images are important for understanding this topic.

Disposition: rejected.

### Option C: Add an image-rich safer-running page with top-10 image prioritization

Rank the top 10 running image candidates and generate the top six first if downstream artifacts approve the image-count exception.

Advantages:

- Matches the user's request for more high-quality images.
- Controls image generation through ranking, prompt records, provenance, and review.
- Gives beginners visual support for posture, landing, stride, warm-up, method, and muscle attention.
- Extends the accepted Tai Chi and per-exercise image-prioritization model to a higher-image running page.

Drawbacks:

- Larger media burden than typical exercise pages.
- Requires explicit image-count exception because six images exceed the normal exercise-image policy.
- Requires strong prompt, provenance, visual-safety review, source audit, and beginner-comprehension discipline.

Disposition: recommended.

### Option D: Create a full beginner running program

Create a multi-week running plan.

Advantages:

- Very practical for beginners.
- Similar to Couch to 5K.

Drawbacks:

- Moves from exercise education into programming.
- Requires more safety and progression governance.
- Risks becoming a personalized training plan.

Disposition: deferred follow-up.
This proposal should first create a static safer-running basics page.

## Recommended Direction

Choose Option C.

GymPrimer should add a proposal-backed, image-rich running exercise/cardio page candidate:

```text
exercises/safer-running-basics.md
```

The page should use:

```text
Title: Safer Running Basics
Alias: Also searched as: injury-free running, beginner running, running without getting hurt
```

The page should teach:

- run/walk starting method;
- easy effort;
- warm-up and cool-down;
- gradual load progression;
- rest days;
- simple form cues;
- muscle roles;
- common mistakes;
- stop conditions; ([Mayo Clinic][mayo-exercise-chronic-disease])
- when to seek professional guidance.

The page should avoid:

- "injury-free" guarantee;
- race-specific programming;
- treatment of running injuries;
- foot-strike dogma;
- speed work for beginners;
- high-intensity intervals;
- medical claims.

### Top 10 necessary running image evaluation

Each image candidate is scored from 1 to 5 on five criteria.

| Criterion | Meaning |
|---|---|
| Beginner comprehension | Does the image explain something text cannot explain well? |
| Safety/load value | Does the image reduce a common beginner risk? |
| Movement value | Does the image clarify dynamic running mechanics? |
| Muscle-attention value | Does the image help users understand what to pay attention to? |
| Readiness | Can the image be generated and reviewed without expanding scope? |

Maximum score: 25.

### Ranked top 10 running image candidates

| Rank | Candidate image | Purpose | Why it matters | Score | Disposition |
|---:|---|---|---|---:|---|
| 1 | Beginner running posture side view | `exercise_movement_illustration` | Shows tall posture, slight forward lean, relaxed shoulders, and arm swing. | 25 | Generate first if exception is approved |
| 2 | Foot landing close to body / short stride | `exercise_movement_illustration` | Helps explain avoiding overreaching without prescribing one foot strike. | 24 | Generate first if exception is approved |
| 3 | Run/walk interval flow | `exercise_movement_illustration` | Shows that walking breaks are part of beginner running, not failure. | 23 | Generate first if exception is approved |
| 4 | Warm-up sequence | `exercise_movement_illustration` | Shows walking, easy jogging, and dynamic preparation before running. | 23 | Generate first if exception is approved |
| 5 | Broad muscle-attention image for running | `exercise_muscle_attention_illustration` | Highlights glutes, thighs, calves, feet/ankles, trunk, and relaxed shoulders. | 22 | Generate first if exception is approved |
| 6 | Common overstride comparison, neutral framing | `exercise_movement_illustration` | Shows long reaching step versus shorter step without correct/wrong labels. | 22 | Generate first if exception is approved |
| 7 | Easy-effort / talk-test visual | `exercise_movement_illustration` | Useful but hard to show without text; better explained in Markdown. | 18 | Later candidate |
| 8 | Running surface and route setup | `exercise_setup_illustration` | Shows smooth, clear, visible route; useful but lower priority. | 18 | Later candidate |
| 9 | Cool-down walk | `exercise_movement_illustration` | Useful for routine structure but simple enough for text. | 16 | Later candidate |
| 10 | Shoe and clothing setup | `exercise_setup_illustration` | Useful but risks brand/style distraction. | 15 | Later candidate |

The first six are selected because running needs more visual support than many static exercises.
This is an explicit proposal-level request for an exception to the normal exercise-image count default.
Downstream approved specs or plans still need to record the exception before a six-image page is promoted.

### First six images to generate

These images should be generated later through the governed Codex/imagegen implementation path after prompt records, provenance fields, and review criteria are accepted.

| Asset path | Purpose | Teaching goal |
|---|---|---|
| `media/exercises/safer-running-basics/posture.png` | `exercise_movement_illustration` | Show beginner running posture and relaxed arm swing. |
| `media/exercises/safer-running-basics/landing.png` | `exercise_movement_illustration` | Show foot landing close to the body with a short, quiet stride. |
| `media/exercises/safer-running-basics/run-walk.png` | `exercise_movement_illustration` | Show alternating easy running and walking recovery. |
| `media/exercises/safer-running-basics/warm-up.png` | `exercise_movement_illustration` | Show a simple pre-run warm-up sequence. |
| `media/exercises/safer-running-basics/muscle-attention.png` | `exercise_muscle_attention_illustration` | Show broad running muscle regions to notice. |
| `media/exercises/safer-running-basics/overstride-comparison.png` | `exercise_movement_illustration` | Show overreaching stride versus shorter stride, with neutral framing and no labels. |

Each generated raster image should also have a prompt record under the governed prompt-record path and an approved row in `media/PROVENANCE.md`.
The media provenance review previously required deterministic provenance fields and exact mapping between referenced assets and provenance records.

### Proposed page structure

```md
# Safer Running Basics

Also searched as: injury-free running, beginner running, running without getting hurt

## What this is for

## What this page cannot promise

## Before you start

## Warm up

## Running form basics

## Muscles involved

## What you should feel

## How much to do

## Common mistakes

## Easier version

## Harder version

## Safety notes

## Sources
```

The page should say plainly that no page can guarantee injury-free running.
It should teach general beginner practices that may reduce common risk factors, such as doing too much too soon, skipping rest, and running with avoidable form tension.

### Recommended content guidance

The warm-up section should recommend a short gradual warm-up before running.
Mayo Clinic Health System recommends at least a 3-5 minute warm-up at the start of a run, and NHS Couch to 5K starts each run with a five-minute warm-up walk. ([Mayo Clinic Health System][mchs-better-runner]; [NHS][nhs-couch-to-5k])

The form section should use simple, non-dogmatic cues:

- run tall;
- keep shoulders relaxed;
- let arms swing naturally;
- keep steps short enough that the foot does not reach far in front of the body;
- land quietly;
- keep effort easy at first;
- avoid forcing a specific foot strike.

ACSM's running-form guidance frames several habits around reducing risk-related mechanical features such as impact loading, braking force, and over-striding.
GymPrimer should keep this as general education rather than formal gait retraining. ([ACSM][acsm-running-form])

The muscles section should use role-based muscle guidance, not a detailed anatomy chart.
Suggested section shape:

| Role | Muscle region | What it helps do |
|---|---|---|
| Support and push-off | Glutes, thighs, and calves | Help support each step and push the ground away. |
| Landing control | Feet, ankles, calves, and thighs | Help absorb and control each landing. |
| Posture and transfer | Trunk | Helps you stay tall while the legs move. |
| Rhythm and balance | Shoulders, upper back, and arms | Help arm swing stay relaxed and coordinated. |

The feel section should explain that the reader should feel warm and slightly out of breath, but not panicked or strained.
Sharp pain, worsening pain, chest pain, dizziness, or unusual shortness of breath are not normal running goals. ([Mayo Clinic][mayo-exercise-chronic-disease])
Stop-condition language should link to `RED-FLAGS.md` and page-local sources. ([Mayo Clinic][mayo-exercise-chronic-disease])
Mayo Clinic notes that dizziness, unusual shortness of breath, chest pain, or irregular heartbeat can be reasons to stop exercise in relevant contexts. ([Mayo Clinic][mayo-exercise-chronic-disease])

The method section should use a running-specific version of `basic_cardio_activity` unless a downstream spec amendment creates `run_walk_progression`.
Suggested visible method type:

```md
Method type: basic_cardio_activity / run_walk_progression
```

The section should explain a general beginner starting point of 10-20 minutes total, alternating short easy running with walking, keeping effort easy enough to speak in short sentences, and taking rest days between running days.
Progression should first make running feel smoother and easier, then add a little total time, then add more running time within the same session.
It should avoid adding distance, speed, hills, and extra running days all at once.

## Expected Behavior Changes

After downstream artifacts are approved and implemented:

- GymPrimer has a beginner-facing safer-running page.
- "Injury-free running" intent is preserved as an alias, but not as a guarantee.
- Running guidance uses run/walk progression, easy effort, gradual loading, and rest days.
- The page contains a richer image set than typical exercise pages if the image-count exception is approved.
- The six generated images explain posture, landing, run/walk structure, warm-up, muscle attention, and overstride risk.
- The page remains Markdown-first, source-backed, and non-clinical.
- The project has a reviewed precedent candidate for image-rich dynamic exercise pages.

## Architecture Impact

Expected touched surfaces:

| Surface | Impact |
|---|---|
| `exercises/safer-running-basics.md` | New running exercise/cardio page. |
| `media/exercises/safer-running-basics/` | New generated image directory if image generation is approved. |
| `media/prompts/exercises/safer-running-basics/` | Prompt-record directory for generated images if image generation is approved. |
| `media/PROVENANCE.md` | Add rows for generated raster images if image generation is approved. |
| `SOURCES.md` | Add reused running sources if shared beyond the page. |
| `specs/exercise-image-standard.md` | Add or confirm the exception path for image-rich dynamic exercises. |
| `specs/exercise-method-guidance.md` | Confirm `basic_cardio_activity` coverage or add a `run_walk_progression` method-type amendment. |
| `docs/templates/exercise-card.md` | No required change unless running exposes a missing cardio-activity block. |
| `tools/checks/check_markdown_first.py` | No change unless current validation cannot enforce image-count exception, prompt records, provenance, or method type. |

No runtime app, database, tracker, wearable integration, generated public JSON, video platform, user account, or adaptive coaching is needed.

## Testing and Verification Strategy

Automated checks should cover:

```text
exercises/safer-running-basics.md
media/exercises/safer-running-basics/
media/prompts/exercises/safer-running-basics/
media/PROVENANCE.md
SOURCES.md
RED-FLAGS.md
```

Checks should verify:

- page has required sections;
- citations are page-local;
- reused source IDs appear in `SOURCES.md`;
- page avoids medical-condition identification, treatment, recovery-protocol, return-to-running, race-plan, and personalized-program wording;
- image paths are local and relative;
- image alt text is meaningful;
- each generated raster image has a matching prompt record;
- each generated raster image has an approved provenance row;
- media purpose is allowed;
- image-count exception is explicitly approved;
- privacy scan passes.

Manual visual-safety review should confirm:

- each image teaches one concept;
- no in-image text;
- no correct/wrong badge;
- no red pain marks;
- no medical, recovery-protocol, or treatment framing;
- no identifiable person;
- no brand marks;
- the overstride comparison is neutral and not shame-based;
- muscle highlighting is broad and subtle;
- alt text and Markdown explain the image.

Beginner comprehension proof should ask:

- What can this page help you do?
- Can it guarantee injury-free running?
- How would you start your first running session?
- What does run/walk mean?
- What should your effort feel like?
- What does the posture image teach?
- What does the landing image teach?
- What listed symptom would make the page tell you to stop? ([Mayo Clinic][mayo-exercise-chronic-disease])
- Which source would you click to verify the progression or safety guidance?

The Markdown-first checker previously needed deterministic source-index behavior, and semantic source support remains a manual review responsibility for exercise-specific claims.
Local completion reports should name exact validation commands run.
CI should not be claimed unless a CI run is observed.

## Rollout and Rollback

Rollout should keep the first implementation narrow: one running page, one approved image-count exception, six generated support images if the exception is approved, source-backed Markdown, and manual proof that the images improve beginner comprehension.

Downstream artifacts should confirm:

- the title and alias treatment;
- the top-10 image ranking;
- the top-six first-generation images;
- the image-count exception;
- the method type, either `basic_cardio_activity` or `run_walk_progression`;
- exact image prompts;
- prompt-record fields;
- provenance rows;
- visual-safety review criteria;
- beginner comprehension proof format.

Rollback is additive.
If six images are too many, keep posture, landing, run/walk, and muscle-attention images; defer warm-up and overstride comparison; and record the image-count reduction in review evidence.
If the page drifts into injury treatment, narrow the page, remove treatment-like claims, and remove return-to-running or condition-specific sections.
If an image fails review, remove the Markdown reference, remove or replace the asset, remove or update the prompt record, remove or update the provenance row, and keep the text-only page section.

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---:|---|
| "Injury-free" sounds like a guarantee | High | Use `Safer Running Basics` as title and keep "injury-free running" as alias only. |
| Page becomes return-to-running recovery care | High | Explicitly exclude injury return, pain treatment, and condition-specific advice. |
| Six images overload the page | Medium | Each image should teach one distinct concept; images can be reduced after review. |
| Overstride image becomes shame/correct-wrong framing | Medium | No labels, no red marks, neutral Markdown explanation. |
| Strength guidance overpromises injury prevention | Medium | Present strength as capacity support and acknowledge evidence is mixed. |
| Beginner starts too hard | High | Emphasize run/walk, easy effort, rest days, and gradual progression. |
| Foot-strike advice becomes dogmatic | Medium | Avoid universal foot-strike prescription; focus on short stride and landing close to body. |
| Source support is too broad | High | Use direct sources for progression, warm-up, form, and safety claims. |
| Images introduce unsupported claims | High | Markdown remains source of truth; manual visual-safety review is required. |
| Image provenance or prompt records are incomplete | High | Require prompt records and approved `media/PROVENANCE.md` rows before promotion. |

## Open Questions

None blocking proposal review.

Downstream implementation can decide:

- whether the page path should be `safer-running-basics.md` or `running-basics.md`;
- exact image prompts;
- exact reviewer handle;
- whether `run_walk_progression` becomes its own method type;
- whether the warm-up image or overstride image should be deferred if six images feel too dense.

Recommended default:

```text
File path: exercises/safer-running-basics.md
Title: Safer Running Basics
Alias: injury-free running
First image batch: six images, only after explicit exception approval
```

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-06 | Use `Safer Running Basics` instead of `Injury-Free Running`. | Avoids injury-free guarantee while preserving search intent. | Page titled `Injury-Free Running`. |
| 2026-07-06 | Add a running exercise/cardio page candidate. | Running is a common beginner activity and needs static guidance. | Do nothing; full running program first. |
| 2026-07-06 | Use top-10 image evaluation and top-six first generation candidates. | Running needs more visual support than most static exercise pages. | Text-only page; generate all images opportunistically. |
| 2026-07-06 | Teach run/walk and easy effort before continuous running. | Better beginner progression and less abrupt loading. | Continuous running from day one; speed work first. |
| 2026-07-06 | Keep strength and form guidance non-guaranteed. | Evidence for specific injury-prevention interventions is mixed. | Claim strength/form work prevents injury. |
| 2026-07-06 | Keep page non-clinical and outside recovery care. | Preserves GymPrimer's educational boundary. | Return-to-running protocol or injury treatment page. |

## Next Artifacts

1. Proposal review.
2. Focused spec or spec amendment for safer-running page contract, running image-count exception, top-10 image evaluation, and top-six image generation selection.
3. Exercise-method amendment for `basic_cardio_activity` coverage or `run_walk_progression`, if needed.
4. Architecture assessment for media and validation impact if the image-count exception or method-type addition changes cross-component behavior.
5. Execution plan after the spec and architecture gates are settled.
6. Test specification for Markdown page checks, media checks, prompt-record checks, provenance checks, visual-safety review, source audit, and beginner comprehension proof.

## Follow-on Artifacts

None yet

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Explain best practices for injury-free running | in scope | Problem; Recommended Direction; Risks and Mitigations |
| Reframe "injury-free running" safely | in scope | Goals; Non-goals; Decision Log |
| Generate a proposal | in scope | Status; all required proposal sections |
| Use best practices | in scope | Context; Recommended Direction; Testing and Verification Strategy |
| Require more high-quality images | in scope | Goals; Top 10 necessary running image evaluation; First six images to generate |
| Make it an exercise document | in scope | Goals; Architecture Impact |
| Preserve safety and avoid misleading injury claims | in scope | Non-goals; Risks and Mitigations |
| Do not generate images yet | in scope | Status; Non-goals; Rollout and Rollback |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Safer running page | core to this proposal | Main user-facing deliverable candidate. |
| "Injury-free" reframing | core to this proposal | Prevents unsupported guarantee. |
| Top-10 running image evaluation | core to this proposal | Required to prioritize high-quality images. |
| Top-six first image batch | core to this proposal | Required to make the running page image-rich if exception is approved. |
| Image-count exception | same-slice dependency | Needed because six images exceed the normal exercise-image default. |
| Running method guidance | same-slice dependency | Running needs time, run/walk, effort, rest, and progression guidance. |
| Prompt records | same-slice dependency | Required when generated raster media is produced. |
| `media/PROVENANCE.md` rows | same-slice dependency | Required when generated raster assets are produced. |
| Manual visual-safety review | same-slice dependency | Required before image promotion. |
| Beginner comprehension proof | same-slice dependency | Needed to prove images improve understanding. |
| Full 5K plan | deferable follow-up | Useful later but too programmatic for the first page. |
| Return-to-running after injury | out of scope | Requires clinical governance and would violate this page boundary. |
| Running injury condition pages | separate proposal | Shin splints, plantar fasciitis, runner's knee, and related topics are condition pages, not this exercise page. |
| Video or animation | out of scope | Different media product. |

## Readiness

This proposal has been reviewed and accepted.

It is not ready for implementation until downstream workflow confirms:

- the safe title and alias treatment;
- the image-count exception;
- the first six image prompts;
- prompt-record paths;
- provenance rows;
- reviewer handle;
- visual-safety review criteria;
- beginner comprehension proof format;
- whether `run_walk_progression` is a new method type or a subtype of `basic_cardio_activity`.

The first downstream implementation should stay narrow: one running page, six generated support images only if the exception is approved, source-backed Markdown, and manual proof that the images improve beginner comprehension.

[mchs-better-runner]: https://www.mayoclinichealthsystem.org/hometown-health/speaking-of-health/how-can-i-become-a-better-runner-and-avoid-injury
[nhs-couch-to-5k]: https://www.nhs.uk/better-health/get-active/get-running-with-couch-to-5k/couch-to-5k-running-plan/
[cdc-adult-activity]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
[acsm-running-form]: https://acsm.org/distance-running-form-tips/
[mayo-exercise-chronic-disease]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-and-chronic-disease/art-20046049
[pubmed-running-injury-exercise-prevention]: https://pubmed.ncbi.nlm.nih.gov/38261240/
[pmc-running-injury-support]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11986186/
