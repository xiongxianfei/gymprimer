# Proposal: Necessary Image Prioritization and Tai Chi Exercise Page

## Status

accepted

This proposal records a content and media direction for GymPrimer:

1. evaluate the top 10 necessary images for one Tai Chi basics exercise page;
2. choose the top three images for a first image-generation loop;
3. add a new Tai Chi beginner exercise page using the accepted exercise-image standard.

This proposal does not generate images yet.
Image generation should happen later through the governed media workflow, after prompts, prompt records, provenance rows, review criteria, and validation expectations are accepted.

## Problem

Images are important for GymPrimer because beginners often cannot understand movement quality from text alone.
Accepted project direction already recognizes that exercise images should clarify setup, movement, or muscle attention, while remaining subordinate to Markdown text, citations, safety routing, and alt text.
The approved exercise-image spec also says generated raster exercise images need deterministic provenance, exact prompt records, and visual-safety review before they become promotable project assets.

The current problem has two parts.

First, image prioritization is missing for this exercise.
GymPrimer should not generate images randomly or mechanically for every possible Tai Chi cue.
It should evaluate which Tai Chi images are most necessary and generate the highest-value images first.

Second, Tai Chi is a good next exercise, but it is image-dependent.
Tai Chi uses slow movement, weight shifting, posture control, and breathing.
NCCIH describes tai chi as slow gentle movements, physical postures, a meditative state of mind, and controlled breathing. ([NCCIH][nccih_tai_chi])
That makes it difficult to teach with text alone.

## Goals

- Add a proposal-level process for ranking the top 10 necessary images for Tai Chi Basics.
- Choose the top three images to generate first.
- Add a beginner-facing Tai Chi page, likely `exercises/tai-chi-basics.md`.
- Treat Tai Chi as static beginner education, not martial-arts instruction, therapy, medical assessment, recovery programming, or fall-prevention programming.
- Use images to teach body position, weight shift, and broad muscle attention.
- Keep all instructions, muscle names, cues, safety notes, and citations in Markdown.
- Ensure every generated raster image has a row in `media/PROVENANCE.md` and an exact prompt record under the governed prompt-record path.
- Preserve the current image standard: setup, movement, and muscle-attention purposes; no in-image labels; neutral visuals; meaningful alt text; and manual visual-safety review.
- Use one proposal and multiple small downstream loops, rather than creating a separate proposal for every image batch.

## Non-goals

- No immediate image generation in this proposal.
- No full Tai Chi form, martial-arts curriculum, competition form, combat application, or lineage/style debate.
- No claim that Tai Chi treats disease, prevents falls for a specific reader, fixes posture, cures pain, or replaces medical care.
- No personalized balance program, recovery plan, return-to-exercise protocol, symptom-based recommendation, or adaptive coaching.
- No video, animation, camera form analysis, hosted image service, runtime app, database, or user-input flow.
- No borrowed web images, stock photos, commercial screenshots, branded equipment, identifiable people, or decorative hero art.
- No in-image text, Chinese characters, arrows with labels, safety warnings, citations, muscle names, correct/wrong badges, red pain marks, or clinical framing.
- No use of generated images as source-of-truth evidence for anatomy, technique, safety, medical assessment, treatment, recovery care, or programming.

## Vision fit

fits the current vision

This proposal fits GymPrimer's Markdown-first direction.
It adds a static, citation-backed beginner exercise page and uses images only as support assets.
It does not introduce personalized coaching, medical assessment, treatment, recovery-care behavior, hosted-app behavior, or media as source of truth.

It also follows the current exercise-image and muscle-guidance direction.
Images should help with setup, movement, or muscle attention; muscle guidance should stay broad, beginner-readable, and source-backed; and exact instruction should remain in Markdown.

## Context

The accepted exercise-image proposal says exercise documents should use images intentionally.
Each image teaches setup, movement, or muscle attention, with zero to three images depending on comprehension need.
Generated raster exercise images live under `media/exercises/<slug>/`, use the approved exercise-image purpose values, and need approved provenance before promotion.

The approved exercise-image spec adds an exact prompt-record obligation.
For new generated raster exercise images, `media/PROVENANCE.md` rows are not enough by themselves.
The generated asset should also have a repository-local prompt record, normally under `media/prompts/exercises/<exercise-slug>/<asset-stem>.md`, that preserves the exact full prompt text for the accepted image.

The muscle-guidance direction recommends role-based, beginner-readable muscle guidance.
It also says muscle-attention images should support the Markdown section, not replace it, and that exact cues, caveats, and citations should stay in Markdown.

For Tai Chi specifically, public sources support a conservative beginner framing.
Harvard Health describes tai chi as low-impact, slow-motion exercise with circular, usually unforced movements, relaxed muscles, and joints not fully extended or bent.
Harvard also recommends short forms and smaller, slower movements for beginners, especially older or less-conditioned learners. ([Harvard Health][harvard_tai_chi])
The VA describes Tai Chi and Qigong as gentle movement practices using slow movement, breathing, and focus, and notes they can be done seated or standing. ([Veterans Affairs][va_tai_chi_qigong])

## Options Considered

### Option A: Generate Tai Chi images immediately

Generate images first, then write the page around them.

Advantages:

- Fast visible progress.
- Matches the view that images are important.

Drawbacks:

- Skips the governed media workflow.
- Risks unclear image purpose, missing prompt records, missing provenance, and inconsistent style.
- Images may accidentally imply therapy, balance treatment, martial instruction, or exact form correctness.

Disposition: rejected.

### Option B: Add Tai Chi as text-only first

Write `exercises/tai-chi-basics.md` with no images.

Advantages:

- Lowest media risk.
- Fastest content path.

Drawbacks:

- Tai Chi's value depends heavily on posture, weight shift, and continuous movement.
- Text-only Tai Chi would likely be hard for beginners to understand.

Disposition: rejected as the primary direction.

### Option C: Evaluate top 10 Tai Chi image needs, generate the top three, and add Tai Chi as the first image-priority exercise

Rank the most necessary images for the Tai Chi Basics page, choose the top three, and generate only those first.
Use Tai Chi as the next page because it naturally needs setup, movement, and muscle-attention visuals.

Advantages:

- Matches the user's image-first priority.
- Keeps image generation controlled.
- Produces a visible improvement.
- Avoids generating unnecessary images.
- Tests the exercise-image standard on a movement where images are genuinely useful.

Drawbacks:

- Requires more upfront judgment than simple page writing.
- Requires prompt records, provenance discipline, visual-safety review, and beginner comprehension proof before promotion.

Disposition: recommended.

### Option D: Create a separate proposal only for Tai Chi, and another for image prioritization

Split the work into two proposals.

Advantages:

- Smaller proposals.

Drawbacks:

- Artificially separates the key product decision: Tai Chi is valuable partly because it is a good test of image-prioritized exercise education.
- Creates extra governance overhead.

Disposition: rejected.
Use one proposal and split implementation into small downstream loops if needed.

## Recommended Direction

Choose Option C.

GymPrimer should evaluate the top 10 necessary image candidates for a new `exercises/tai-chi-basics.md` page, choose the top three for the first generation loop, and use those images to support the first Tai Chi Basics implementation.
Candidates 4-10 are deferred alternatives or future candidates, not approval to place more than three images on the page.
Any version of `exercises/tai-chi-basics.md` with more than three images needs explicit downstream approved spec or plan justification under the existing exercise-image limit.

### Tai Chi page scope

The Tai Chi page should teach only beginner basics:

- relaxed standing posture;
- slow breathing;
- soft knees;
- upright trunk;
- relaxed shoulders;
- weight shifting;
- simple opening movement;
- broad muscle attention.

Broad muscle attention should cover:

| Region | Beginner role |
|---|---|
| Legs and glutes | Support and weight transfer. |
| Trunk | Posture and balance. |
| Shoulders and upper back | Relaxed arm movement. |
| Feet and ankles | Ground contact and balance adjustment. |

It should not teach a full form, martial application, medical protocol, fall-prevention program, or individualized balance training.

### Top 10 necessary image evaluation

Each image candidate is scored from 1 to 5 on five criteria:

| Criterion | Meaning |
|---|---|
| Beginner comprehension | Does the image explain something text cannot explain well? |
| Safety/setup value | Does the image reduce setup or form confusion? |
| Muscle-attention value | Does the image help users understand what to pay attention to? |
| Page value | Can the image support more than one section or future revision of this page? |
| Readiness | Can the image be generated and reviewed without expanding scope? |

Maximum score: 25.

### Ranked top 10 Tai Chi image candidates

| Rank | Candidate image | Page | Purpose | Why it matters | Score | Disposition |
|---:|---|---|---|---|---:|---|
| 1 | Tai Chi ready stance / Wuji setup | `exercises/tai-chi-basics.md` | `exercise_setup_illustration` | Shows feet, soft knees, upright trunk, relaxed shoulders, and calm starting posture. | 24 | Generate first |
| 2 | Tai Chi weight shift / empty-full foot concept | `exercises/tai-chi-basics.md` | `exercise_movement_illustration` | Weight shifting is central to Tai Chi and difficult to explain with text alone. | 24 | Generate first |
| 3 | Tai Chi opening movement with broad muscle attention | `exercises/tai-chi-basics.md` | `exercise_muscle_attention_illustration` | Shows relaxed arms while highlighting broad lower-body and trunk support without anatomy labels. | 22 | Generate first |
| 4 | Opening movement arm path sequence | `exercises/tai-chi-basics.md` | `exercise_movement_illustration` | Shows the arms rising and lowering without shrugging or stiff elbows. | 21 | Later candidate |
| 5 | Side-view posture and soft-knee depth | `exercises/tai-chi-basics.md` | `exercise_setup_illustration` | Helps beginners avoid locked knees, deep squatting, or leaning while trying to stand relaxed. | 20 | Later candidate |
| 6 | Foot pressure and light-foot concept | `exercises/tai-chi-basics.md` | `exercise_movement_illustration` | Makes the empty-full idea visible without turning it into a technical form lesson. | 19 | Later candidate |
| 7 | Return to quiet standing | `exercises/tai-chi-basics.md` | `exercise_movement_illustration` | Shows how the beginner resets posture and breathing after a small movement. | 18 | Later candidate |
| 8 | Chair-supported or seated option | `exercises/tai-chi-basics.md` | `exercise_setup_illustration` | Supports the easier-version section without making the page a balance program. | 18 | Later candidate |
| 9 | Small step and weight transfer | `exercises/tai-chi-basics.md` | `exercise_movement_illustration` | Shows a possible harder version after the reader understands standing weight shift. | 17 | Later candidate |
| 10 | Clear practice space with wall or chair nearby | `exercises/tai-chi-basics.md` | `exercise_setup_illustration` | Helps readers understand safe setup context while keeping the page non-clinical. | 16 | Later candidate |

All ten candidates are for the same Tai Chi Basics exercise page.
The selected top three are the first generation batch because they cover the minimum distinct visual concepts: setup, weight shift, and broad muscle attention.
Candidates 4-10 remain deferred alternatives or future candidates.
They may replace one of the selected first three in a later revision, but they do not authorize publishing more than three images on the page without explicit downstream approved spec or plan justification.

### First three images to generate

These images should be generated later through the governed Codex/imagegen implementation path.

| Asset path | Purpose | Teaching goal |
|---|---|---|
| `media/exercises/tai-chi-basics/setup.png` | `exercise_setup_illustration` | Show beginner-ready Tai Chi standing posture. |
| `media/exercises/tai-chi-basics/weight-shift.png` | `exercise_movement_illustration` | Show smooth weight transfer from one leg to the other. |
| `media/exercises/tai-chi-basics/muscle-attention.png` | `exercise_muscle_attention_illustration` | Show broad regions to pay attention to. |

The setup image should show a neutral adult figure, comfortable stance, soft knees, upright trunk, relaxed shoulders, and arms resting naturally.
It should avoid labels, martial-combat framing, medical framing, and therapy framing.

The weight-shift image should use two ghosted body positions or a simple two-panel composition.
It should show one leg receiving more weight while the other becomes light, with a calm upper body and no correct/wrong labels or text arrows.

The muscle-attention image should use broad, subtle highlighting on the legs/glutes and trunk, with optional subtle shoulder or upper-back emphasis.
It should avoid exact muscle labels, anatomy-chart framing, red marks, pain implication, and injury framing.
Nearby Markdown should carry the muscle explanation.

### Proposed Tai Chi page structure

```md
# Tai Chi Basics

## What this is for

## Before you start

## Setup

## Muscles involved

## Movement breakdown

### 1. Ready stance

### 2. Weight shift

### 3. Opening movement

### 4. Return to quiet standing

## What you should feel

## Common mistakes

## How much to do

## Easier version

## Harder version

## Safety notes

## Sources
```

### Recommended Tai Chi content guidance

The page should frame Tai Chi as low-impact mindful movement, balance and coordination practice, relaxed posture and breathing practice, and gentle movement literacy.
NCCIH describes tai chi as slow gentle movements, postures, meditative attention, and controlled breathing. ([NCCIH][nccih_tai_chi])

Beginner setup should say to wear comfortable clothing, choose shoes that do not slip, practice on a clear flat surface, keep a wall or stable chair nearby if balance is uncertain, and start with small slow movements.
Harvard recommends loose clothing and comfortable flexible shoes with enough support to help balance, and it recommends checking with a clinician if a person has a limiting musculoskeletal problem, medical condition, or medication that may cause dizziness or lightheadedness. ([Harvard Health][harvard_tai_chi])
NHS balance-exercise guidance also recommends loose clothing, water, building up slowly, and doing balance exercises near a wall or stable chair when needed. ([NHS][nhs_balance_exercises])

The `## Muscles involved` section should use broad role-based language:

| Role | Muscle region | What it helps do |
|---|---|---|
| Support and weight shift | Legs and glutes | Help you move weight from one foot to the other. |
| Posture and balance | Trunk | Helps you stay tall and steady. |
| Relaxed arm motion | Shoulders and upper back | Help the arms move smoothly without shrugging. |
| Foot control | Feet and ankles | Help you feel the ground and adjust balance. |

The movement breakdown should stay simple:

```md
### 1. Ready stance

Stand tall with soft knees and relaxed shoulders.

### 2. Weight shift

Slowly move more weight into one foot, then return toward center.

### 3. Opening movement

Let the arms rise and lower smoothly while the body stays relaxed.

### 4. Return to quiet standing

Finish by standing still and breathing normally.
```

The page should not teach a named long form.
Harvard recommends shorter forms and smaller, slower movements at the beginning, especially for older or less-conditioned learners. ([Harvard Health][harvard_tai_chi])

The `## How much to do` section should use the accepted low-load control drill shape rather than forcing a sets-and-reps prescription:

```md
## How much to do

Method type: low_load_control_drill

Beginner starting point:
- Practice for 3-5 minutes.
- Move slowly enough that you can breathe normally.
- Pause before balance, posture, or attention breaks down.

Effort:
- Keep the movement easy and controlled.
- You should be able to breathe normally and stay relaxed.

Rest:
- Rest as needed between short practice rounds.
- Start again only when posture and attention feel steady.

Progression:
- First make the movement smoother.
- Then practice for a little longer.
- Do not make the movement bigger or deeper just to make it harder.

Stop if: ([Harvard Health][harvard_tai_chi])
- Stop if balance, posture, or breathing no longer feels controlled. ([Harvard Health][harvard_tai_chi])
- Stop for dizziness, chest pain, fainting, unusual shortness of breath, sharp pain, or worsening symptoms. ([Harvard Health][harvard_tai_chi])
```

Safety notes should include pausing for dizziness, chest pain, fainting, unusual shortness of breath, sharp pain, or worsening symptoms, with source-backed final wording in the downstream page. ([Harvard Health][harvard_tai_chi])
They should also include using a wall or chair if balance is uncertain, avoiding deep knee bends in the first version, keeping movements small and comfortable, and asking a qualified instructor or clinician if balance, dizziness, a medical condition, or injury history makes practice uncertain. ([Harvard Health][harvard_tai_chi]) ([NHS][nhs_balance_exercises])
Harvard says a class may be the best way to learn tai chi because a teacher can give feedback, and it recommends looking for an experienced teacher who can accommodate health concerns or coordination and fitness levels. ([Harvard Health][harvard_tai_chi])
The VA notes that trained instructors can guide movements and that Tai Chi/Qigong practices may be done standing, seated, or with support. ([Veterans Affairs][va_tai_chi_qigong])

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Images are important for understanding | in scope | Problem; Goals; Recommended direction |
| Evaluate top 10 necessary images for one exercise | in scope | Recommended direction |
| Choose at least top three images | in scope | Recommended direction |
| Use imagegen skill in Codex | deferred follow-up | Rollout and rollback; Next artifacts |
| Add Tai Chi exercise next | in scope | Recommended direction; Expected behavior changes |
| Follow best practices | in scope | Context; Testing and verification strategy; Risks and mitigations |
| Keep project safe and non-clinical | in scope | Non-goals; Risks and mitigations |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Top-10 image evaluation | core to this proposal | Main image-prioritization decision. |
| First three selected images | core to this proposal | Required by the user's request. |
| Tai Chi beginner exercise page | core to this proposal | Next content addition and proof exercise. |
| Image prompt engineering | first-slice candidate | Needed before the first three generated images can be reviewed. |
| Codex/imagegen generation | separate implementation slice | Should happen after prompts, prompt records, provenance rows, and review criteria are accepted. |
| `media/PROVENANCE.md` rows | same-slice dependency | Required when generated raster assets are introduced. |
| Prompt records | same-slice dependency | Required by the approved exercise-image spec for new generated raster exercise images. |
| Manual visual-safety review | same-slice dependency | Required before promotion. |
| Beginner comprehension proof | same-slice dependency | Needed to show images help comprehension. |
| Remaining Tai Chi image candidates | deferable follow-up | Top 10 records Tai Chi-specific alternatives; later candidates may replace a selected image, but more than three page images need explicit downstream approved spec or plan justification. |
| Full Tai Chi form | out of scope | Too broad and style-specific. |
| Medical or fall-prevention program | out of scope | Requires clinical governance and is outside GymPrimer's current boundary. |
| Video or animation | out of scope | Different media product. |

## Expected Behavior Changes

After downstream implementation:

- GymPrimer has a clear Tai Chi beginner page.
- The Tai Chi Basics page has a ranked top-10 image candidate pool.
- The first image-generation loop has exactly three selected images.
- Candidates 4-10 remain deferred alternatives subject to the existing three-image page limit.
- Generated Tai Chi images teach setup, movement, and muscle attention.
- Tai Chi images have prompt records, approved provenance rows, meaningful alt text, and visual-safety review evidence.
- The Tai Chi page remains static, Markdown-first, citation-backed, and non-clinical.
- Future Tai Chi image work can reuse the ranking process instead of choosing images ad hoc.

## Architecture Impact

Expected touched surfaces:

| Surface | Impact |
|---|---|
| `exercises/tai-chi-basics.md` | New exercise page. |
| `media/exercises/tai-chi-basics/` | New generated image directory when assets are introduced. |
| `media/prompts/exercises/tai-chi-basics/` | New prompt-record directory when assets are introduced. |
| `media/PROVENANCE.md` | Add rows for generated raster images when assets are introduced. |
| `SOURCES.md` | Add reused Tai Chi sources if shared beyond the page. |
| `docs/templates/exercise-card.md` | No required change unless Tai Chi exposes a missing low-load movement pattern. |
| `specs/exercise-image-standard.md` | Should already support the selected image purposes and prompt-record requirements; downstream work may only need a narrow Tai Chi selection spec or spec amendment. |
| `specs/exercise-method-guidance.md` | Should already support `low_load_control_drill`; downstream work should confirm naming and page wording. |
| `tools/checks/check_markdown_first.py` | No change unless current validation cannot enforce prompt records, provenance, image purposes, or Tai Chi page checks already specified. |

No runtime, hosted app, video platform, generated JSON, user account, personalized coaching, or tracker is needed.

## Testing and Verification Strategy

Automated checks should cover the Tai Chi page, image references, provenance, prompt records, and source index.

Likely checked surfaces:

```text
exercises/tai-chi-basics.md
media/exercises/tai-chi-basics/
media/prompts/exercises/tai-chi-basics/
media/PROVENANCE.md
SOURCES.md
RED-FLAGS.md
```

Checks should verify:

- the page has required exercise sections;
- citations are page-local;
- reused source IDs appear in `SOURCES.md` when required;
- wording avoids medical-assessment, treatment, recovery-program, fall-prevention protocol, and personalized programming claims;
- image paths are local and relative;
- image alt text is meaningful;
- each generated raster image has a matching approved provenance row;
- each generated raster image has a matching prompt record that points back to the accepted asset;
- `media_purpose` is one of `exercise_setup_illustration`, `exercise_movement_illustration`, or `exercise_muscle_attention_illustration`;
- `review_status` is approved before promotion;
- privacy scan passes.

Manual visual-safety review should confirm:

- each image teaches one concept;
- no in-image text;
- no identifiable person;
- no brand marks;
- no pain marks;
- no clinical or recovery-care framing;
- no exact anatomy claim;
- Tai Chi posture looks calm, beginner-safe, and non-combat-oriented;
- muscle highlighting is broad and subtle;
- alt text matches the image purpose.

Beginner comprehension proof should ask whether a beginner reader can explain:

- what Tai Chi practice is for;
- how to stand at the start;
- what weight shifting means;
- what they should feel in the body;
- when they should pause;
- whether the three images helped more than text alone.

Prior project review found that general approval after images were added is not enough.
Manual proof should record whether the reader can explain required page-level comprehension outcomes.

## Rollout and Rollback

Rollout should be split into downstream artifacts and small implementation loops:

1. Review this proposal.
2. Confirm the top-10 image ranking.
3. Confirm the first three Tai Chi images.
4. Draft a focused spec or spec amendment for the Tai Chi page contract, image-ranking record, and first-image selection.
5. Prepare exact prompts for the top three Tai Chi images.
6. Generate images through Codex/imagegen in an implementation loop.
7. Add generated assets under `media/exercises/tai-chi-basics/`.
8. Add prompt records under `media/prompts/exercises/tai-chi-basics/`.
9. Add `media/PROVENANCE.md` rows.
10. Add Markdown image references and alt text.
11. Run automated checks.
12. Run manual visual-safety review and beginner comprehension proof.

Future candidates 4-10 may replace one of the first three images when a later revision makes that useful.
They should not be added as fourth or later images unless a downstream approved spec or plan records explicit justification for exceeding the normal three-image limit.

If a generated image fails review:

- remove the Markdown reference;
- remove or replace the asset;
- remove or update the provenance row;
- remove or update the prompt record if the asset is not retained;
- keep the text-only page.

If Tai Chi scope becomes too broad:

- narrow the page to ready stance and weight shift only;
- defer opening movement;
- keep the remaining Tai Chi image candidates as future alternatives subject to the three-image limit.

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---:|---|
| Images imply therapy or fall-prevention treatment | High | Use neutral education framing; avoid clinical, cure, and outcome-guarantee language. |
| Tai Chi becomes a martial-arts curriculum | Medium | Teach only ready stance, weight shift, and opening movement. |
| User with balance issues tries unsupported practice | High | Include wall/chair support, small movement, pause criteria, and routing to qualified help. |
| Images show exact form as correct | Medium | Avoid correct/wrong labels; explain that images are beginner visual aids. |
| Muscle highlighting becomes too anatomical | Medium | Highlight broad regions only; keep muscle names and sources in Markdown. |
| Too many images are generated at once | Medium | Generate only the top three first. |
| Image provenance or prompt records are incomplete | High | Require exact prompt records and approved `media/PROVENANCE.md` rows before promotion. |
| Source claims overstate Tai Chi evidence | High | Use cautious general-education language and avoid treatment or prevention claims. |
| Cultural oversimplification | Medium | Use Tai Chi respectfully as a movement practice; avoid unnecessary spiritual, medical, or lineage claims. |

## Open Questions

None blocking proposal review.

Downstream implementation can decide:

- exact image prompts;
- exact provenance reviewer handle;
- exact prompt-record owner and review wording;
- whether Tai Chi belongs only under `exercises/` or later also under a `principles/` page.

Recommended default:

```text
File path: exercises/tai-chi-basics.md
Title: Tai Chi Basics
```

This uses the common English-language name and the requested filename.

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-05 | Add Tai Chi as the next exercise page. | It is beginner-relevant and image-dependent. | Delay Tai Chi; add generic balance page first. |
| 2026-07-05 | Evaluate top 10 Tai Chi image candidates before generation. | Prevents random or excessive image generation for one exercise page while keeping later candidates subject to the existing three-image limit. | Generate images opportunistically. |
| 2026-07-05 | Generate top three first. | Controls scope while proving image workflow. | Generate all 10 at once. |
| 2026-07-05 | Make the first three images the Tai Chi first batch. | Tai Chi Basics needs setup, movement, and muscle-attention visuals before lower-priority alternatives. | Generate all ten Tai Chi images at once; publish more than three images without downstream exception justification. |
| 2026-07-05 | Keep Tai Chi static and non-clinical. | Preserves GymPrimer's educational boundary. | Fall-prevention protocol, recovery program, martial-arts curriculum. |
| 2026-07-05 | Include prompt records in the image workflow. | The approved exercise-image spec requires exact prompt preservation for new generated raster exercise images. | Provenance-only image tracking. |

## Next Artifacts

1. Proposal review.
2. Focused spec or spec amendment for the top-10 image evaluation record, top-three generation selection, Tai Chi page contract, and prompt-record expectations.
3. Image prompt set for the first three Tai Chi images.
4. Draft `exercises/tai-chi-basics.md`.
5. Prompt records for generated assets.
6. `media/PROVENANCE.md` rows for generated assets.
7. Manual visual-safety review.
8. Beginner comprehension proof.

## Follow-on Artifacts

- Proposal review R1: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/proposal-review-r1.md`
- Proposal review R2: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/proposal-review-r2.md`
- Review log: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-log.md`
- Review resolution: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-resolution.md`

## Readiness

This proposal is accepted after proposal-review R2 and owner approval.

It is ready for downstream specification.
It is not ready for implementation until the project confirms the image-generation path, prompt set, prompt records, provenance rows, and review evidence for the top three selected images.
The first implementation should stay narrow: one Tai Chi page, three generated support images, source-backed Markdown, and manual proof that the images improve beginner comprehension.

## Sources

[nccih_tai_chi]: https://www.nccih.nih.gov/health/tai-chi-what-you-need-to-know
[harvard_tai_chi]: https://www.health.harvard.edu/exercise-and-fitness/the-health-benefits-of-tai-chi
[va_tai_chi_qigong]: https://www.va.gov/WHOLEHEALTH/cih/Tai_Chi_and_Qigong.asp
[nhs_balance_exercises]: https://www.nhs.uk/live-well/exercise/balance-exercises/
