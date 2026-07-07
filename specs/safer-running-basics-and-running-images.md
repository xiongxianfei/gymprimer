# Safer Running Basics and High-Quality Running Images Spec

Status: approved

Change ID: `2026-07-06-safer-running-basics-and-running-images`

Proposal: `docs/proposals/2026-07-06-safer-running-basics-and-running-images.md`

## Purpose

This spec defines the observable contract for a beginner-facing GymPrimer running page and its first controlled image set.

The change preserves the search intent behind "injury-free running" without promising that running can be made free of injury risk. The page MUST teach general risk-reduction practices for beginner running and MUST remain Markdown-first, citation-backed, non-clinical, and static.

## Scope

In scope:

- Create the page `exercises/safer-running-basics.md`.
- Use the page title `Safer Running Basics`.
- Include the alias line `Also searched as: injury-free running, beginner running, running without getting hurt`.
- Use `Method type: basic_cardio_activity`.
- Teach run/walk intervals, easy effort, rest days, gradual progression, warm-up, simple form cues, broad muscle roles, common mistakes, and safety routing.
- Authorize exactly six first-batch local generated raster images for this page.
- Require prompt records, provenance rows, meaningful alt text, visual-safety review, and beginner comprehension proof for every published generated image.
- Record a page-specific image-count exception because running is dynamic and whole-body.

Out of scope:

- A guarantee of injury-free running.
- A race plan, 5K plan, marathon plan, speed-work plan, hill-repeat plan, or individualized running program.
- A return-to-running-after-injury protocol or condition-specific pain-care page.
- Medical assessment, treatment advice, gait retraining, or a universal foot-strike prescription.
- Shoe-brand recommendations, wearable integrations, heart-rate-zone calculators, calorie goals, weight-loss targets, hosted apps, adaptive coaching, video, animation, or user input flows.
- Borrowed web images, branded images, identifiable people, stock photos, commercial screenshots, or generated media as source of truth.

## Requirements

### R1. Page identity

R1.1 The implementation MUST create `exercises/safer-running-basics.md`.

R1.2 The page MUST have the H1 `# Safer Running Basics`.

R1.3 The page MUST include this alias line near the top:

```md
Also searched as: injury-free running, beginner running, running without getting hurt
```

R1.4 The page MUST NOT use `Injury-Free Running` as the H1 or as a promise.

### R2. Required sections

R2.1 The page MUST include these sections, using these exact headings:

- `## What this is for`
- `## What this page cannot promise`
- `## Before you start`
- `## Warm up`
- `## Running form basics`
- `## Muscles involved`
- `## What you should feel`
- `## How much to do`
- `## Common mistakes`
- `## Easier version`
- `## Harder version`
- `## Safety notes`
- `## Sources`

R2.2 The `What this page cannot promise` section MUST state that no page can guarantee injury-free running.

R2.3 The page MUST keep citations page-local in `## Sources`.

### R3. Method and progression

R3.1 The page MUST identify its method type as `basic_cardio_activity`.

R3.2 The page MUST teach run/walk intervals as the preferred beginner starting method.

R3.3 The page MUST recommend easy early effort using plain language such as being able to speak in short sentences.

R3.4 The page MUST recommend rest days between early running days.

R3.5 The page MUST teach gradual loading and MUST NOT encourage adding distance, speed, hills, and extra running days all at once.

R3.6 The page MAY mention three running days per week as a beginner pattern only when citation-supported and framed as general education. NHS Couch to 5K uses three runs per week with rest days between runs. [NHS Couch to 5K][nhs-couch-to-5k]

R3.7 The page MAY mention avoiding sudden mileage increases only when citation-supported and framed as general education. Mayo Clinic Health System advises new runners to avoid increasing mileage by more than 10% per week. [Mayo Clinic Health System][mchs-better-runner]

### R4. Warm-up and form guidance

R4.1 The page MUST recommend a short gradual warm-up before running. Mayo Clinic Health System recommends warming up for 3 to 5 minutes before running. [Mayo Clinic Health System][mchs-better-runner]

R4.2 Form cues MUST be simple and non-dogmatic:

- run tall;
- keep shoulders relaxed;
- let arms swing naturally;
- keep steps short enough that the foot does not reach far in front of the body;
- land quietly;
- keep early effort easy;
- avoid forcing a specific foot strike.

R4.3 The page MUST NOT prescribe a universal forefoot, midfoot, or heel strike.

### R5. Muscle and feel guidance

R5.1 The page MUST include a `Muscles involved` table with beginner-readable roles.

R5.2 The table MUST cover at least:

- glutes, thighs, and calves for support and push-off;
- feet, ankles, calves, and thighs for landing control;
- trunk for posture and transfer;
- shoulders, upper back, and arms for rhythm and balance.

R5.3 The `What you should feel` section MUST explain that effort should feel warm and slightly out of breath, not panicked or strained.

R5.4 The `What you should feel` section MUST route chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, weakness, worsening symptoms, or persistent pain to the project safety path and appropriate professional help. Mayo Clinic identifies chest pain, dizziness, and unusual shortness of breath as symptoms that may require stopping exercise and seeking care in relevant contexts. [Mayo Clinic][mayo-exercise-chronic-disease]

R5.5 The page MUST link to `RED-FLAGS.md` from the safety-facing text.

### R6. Common mistakes and variants

R6.1 The page MUST include a `Common mistakes` table.

R6.2 The table MUST cover:

- running too far too soon;
- making every run hard;
- skipping rest days;
- overstriding;
- tense shoulders or hands;
- ignoring sharp, worsening, unusual, or red-flag-like symptoms. [Mayo Clinic][mayo-exercise-chronic-disease]

R6.3 `Easier version` MUST include shorter total time, more walking, flatter routes, and fewer running days.

R6.4 `Harder version` MUST remain conservative and MUST NOT introduce race programming, hard intervals, hill-repeat programming, or speed-work as the next step.

### R7. Image-count exception

R7.1 This spec authorizes a page-specific exception to the normal exercise-image default: `exercises/safer-running-basics.md` MAY publish up to six first-batch images because running is dynamic, whole-body, and commonly misunderstood by beginners.

R7.2 The exception applies only to this page and only to the six asset paths in R8.

R7.3 The six images MUST each teach a distinct concept.

R7.4 The page MUST NOT publish more than one muscle-attention image in the first batch.

R7.5 The top-10 image ranking in R9 is prioritization evidence. Candidates ranked 7 through 10 are deferred and are NOT approved for first-batch publication by this spec.

### R8. Required first-batch image assets

R8.1 The first implementation MUST use exactly these six local image paths if the images are published:

| Asset path | Purpose | Teaching goal |
|---|---|---|
| `media/exercises/safer-running-basics/posture.png` | `exercise_movement_illustration` | Show beginner running posture and relaxed arm swing. |
| `media/exercises/safer-running-basics/landing.png` | `exercise_movement_illustration` | Show foot landing close to the body with a short, quiet stride. |
| `media/exercises/safer-running-basics/run-walk.png` | `exercise_movement_illustration` | Show alternating easy running and walking recovery. |
| `media/exercises/safer-running-basics/warm-up.png` | `exercise_movement_illustration` | Show a simple pre-run warm-up sequence. |
| `media/exercises/safer-running-basics/muscle-attention.png` | `exercise_muscle_attention_illustration` | Show broad running muscle regions to notice. |
| `media/exercises/safer-running-basics/overstride-comparison.png` | `exercise_movement_illustration` | Show an overreaching stride beside a shorter stride with neutral framing and no labels. |

R8.2 Each image reference in the page MUST use a local relative path.

R8.3 Each image reference MUST include meaningful alt text that names the teaching concept without adding unsupported claims.

R8.4 Each generated image MUST have a matching prompt record under `media/prompts/exercises/safer-running-basics/`.

R8.5 Each generated image MUST have an approved row in `media/PROVENANCE.md`.

### R9. Image prioritization evidence

R9.1 The implementation evidence MUST preserve this top-10 ranking:

| Rank | Candidate image | Purpose | Score | Disposition |
|---:|---|---|---:|---|
| 1 | Beginner running posture side view | `exercise_movement_illustration` | 25 | Generate first |
| 2 | Foot landing close to body / short stride | `exercise_movement_illustration` | 24 | Generate first |
| 3 | Run/walk interval flow | `exercise_movement_illustration` | 23 | Generate first |
| 4 | Warm-up sequence | `exercise_movement_illustration` | 23 | Generate first |
| 5 | Broad muscle-attention image for running | `exercise_muscle_attention_illustration` | 22 | Generate first |
| 6 | Common overstride comparison, neutral framing | `exercise_movement_illustration` | 22 | Generate first |
| 7 | Easy-effort / talk-test visual | `exercise_movement_illustration` | 18 | Later candidate |
| 8 | Running surface and route setup | `exercise_setup_illustration` | 18 | Later candidate |
| 9 | Cool-down walk | `exercise_movement_illustration` | 16 | Later candidate |
| 10 | Shoe and clothing setup | `exercise_setup_illustration` | 15 | Later candidate |

R9.2 The first-batch generation prompts MUST be derived from the top-six teaching goals, not from aesthetic preference alone.

### R10. Image safety and provenance

R10.1 Generated images MUST contain no in-image text, labels, badges, arrows that imply medical certainty, brand marks, visible logos, commercial screenshots, or identifiable people.

R10.2 Generated images MUST avoid pain marks, alarm coloring, medical framing, and correct/wrong badges.

R10.3 The overstride image MUST be neutral and MUST NOT shame the runner or label one side as correct or wrong inside the image.

R10.4 The muscle-attention image MUST use broad and subtle region emphasis. Exact muscle names and caveats belong in Markdown, not inside the image.

R10.5 Generated image prompt records MUST record prompt text, intended file path, purpose, review criteria, and provenance expectations.

R10.6 `media/PROVENANCE.md` rows MUST map exactly to referenced raster assets.

### R11. Source and safety boundaries

R11.1 All claims about warm-up, frequency, progression, safety routing, adult activity guidance, form guidance, and evidence limits MUST be supported by page-local sources.

R11.2 Reused source IDs MUST appear in `SOURCES.md` when the project checker requires shared source registration.

R11.3 Strength work MAY be described as general capacity support, but MUST NOT be presented as guaranteed injury prevention. A 2024 systematic review found that exercise-based prevention programs do not clearly reduce running-related injury risk. [PubMed][pubmed-running-injury-exercise-prevention]

R11.4 The page MAY reference adult activity guidance to connect running with broader cardio and strengthening guidance. CDC adult guidance includes aerobic activity plus muscle-strengthening activity on at least two days per week. [CDC][cdc-adult-activity]

### R12. Verification evidence

R12.1 Implementation MUST include automated checks for page structure, section presence, method type, image paths, image count, prompt records, provenance rows, and source registration.

R12.2 Implementation MUST include manual visual-safety review evidence for the six images before they are considered accepted.

R12.3 Implementation MUST include beginner comprehension proof showing that a beginner can answer:

- what the page can help them do;
- whether the page can guarantee injury-free running;
- how to start a first running session;
- what run/walk means;
- what effort should feel like;
- what the posture image teaches;
- what the landing image teaches;
- what would make them stop or seek help. [Mayo Clinic][mayo-exercise-chronic-disease]

R12.4 The implementation handoff MUST report exact local validation commands and MUST NOT claim CI passed unless CI was observed.

## Examples

### E1. Accepted alias treatment

```md
# Safer Running Basics

Also searched as: injury-free running, beginner running, running without getting hurt
```

This is valid because the alias preserves search intent without using `injury-free` as a promise.

### E2. Invalid page title

```md
# Injury-Free Running
```

This is invalid because it implies an unsupported guarantee.

### E3. Accepted method framing

```md
Method type: basic_cardio_activity
```

This is valid because the approved first slice uses the existing cardio method type while teaching run/walk as the beginner method inside the page.

### E4. Invalid image expansion

Publishing `media/exercises/safer-running-basics/shoes.png` in the first batch is invalid under this spec because the shoe candidate is ranked 10 and deferred.

## Compatibility

This spec extends the existing Markdown-first exercise content model. It does not introduce a runtime app, database, API, generated JSON, hosted service, video platform, account system, or adaptive coaching.

The image-count exception is page-specific and does not relax the default exercise-image standard for unrelated pages.

## Rollback

If the image batch cannot pass review, the implementation MAY keep the text page and remove failed image references, prompt records, and provenance rows.

If six images are too dense, rollback MUST keep only the highest-value approved images and record which deferred assets were removed.

If the page drifts into condition-specific pain care or individualized programming, rollback MUST remove those sections and return the page to beginner education.

## Acceptance Criteria

AC1 The proposal status is accepted and downstream workflow artifacts trace to this spec.

AC2 `exercises/safer-running-basics.md` satisfies R1 through R6 and R11.

AC3 The image set satisfies R7 through R10.

AC4 Validation evidence satisfies R12.

AC5 No implementation artifact contradicts `CONSTITUTION.md`, `VISION.md`, the accepted proposal, or this spec.

## Sources

- [NHS Couch to 5K][nhs-couch-to-5k]
- [Mayo Clinic Health System running guidance][mchs-better-runner]
- [Mayo Clinic exercise and chronic disease guidance][mayo-exercise-chronic-disease]
- [PubMed systematic review on running injury prevention programs][pubmed-running-injury-exercise-prevention]
- [CDC adult physical activity guidance][cdc-adult-activity]

[nhs-couch-to-5k]: https://www.nhs.uk/better-health/get-active/get-running-with-couch-to-5k/couch-to-5k-running-plan/
[mchs-better-runner]: https://www.mayoclinichealthsystem.org/hometown-health/speaking-of-health/how-can-i-become-a-better-runner-and-avoid-injury
[mayo-exercise-chronic-disease]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-and-chronic-disease/art-20046049
[pubmed-running-injury-exercise-prevention]: https://pubmed.ncbi.nlm.nih.gov/38261240/
[cdc-adult-activity]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
