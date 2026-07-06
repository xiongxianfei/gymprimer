# Proposal: Necessary Image Prioritization and Baduanjin Exercise Page

## Status

accepted

This proposal records a content and media direction for GymPrimer:

1. add a beginner-facing Baduanjin / Ba Duan Jin / Eight Pieces of Brocade exercise page;
2. evaluate the top 10 necessary image candidates for that page;
3. choose the top five images for the first image-generation loop;
4. keep the page static, Markdown-first, source-backed, non-clinical, and non-prescriptive.

This proposal does not generate images yet.
Image generation should happen later through the governed Codex/imagegen implementation path, after prompt records, provenance rows, review criteria, and validation expectations are accepted.

This proposal follows the accepted Tai Chi image-prioritization proposal model: evaluate a top-10 image candidate pool for one exercise page, select a smaller first generation batch, keep generated raster media subordinate to Markdown, require prompt records and provenance, and avoid treatment, recovery, balance-program, martial-curriculum, or exact-form claims.

## Problem

Images are especially important for Baduanjin because the practice is not a single static posture or one machine setup.
It is a short sequence of coordinated, slow movements involving posture, breathing, weight shift, arm path, trunk rotation, forward bending, and return-to-standing control.

Text alone can explain the sequence, but many beginners will still struggle to understand:

- how to stand at the start;
- how softly the knees should bend;
- how arms move without shoulder tension;
- how weight shifts without rushing;
- how trunk and neck rotation should stay comfortable;
- how the page differs from martial instruction, therapy, or a full traditional form lesson.

NCCIH describes qigong as involving body movement and posture, breath regulation, and attention, and it names Baduanjin as one qigong form. ([NCCIH][nccih-qigong])
A systematic review describes Baduanjin, also called Eight-Section Brocades, as a traditional Chinese qigong exercise with a long history; the same review notes that it contains eight simple movements and is comparatively easy to learn because it has lower physical and cognitive demands than more complex practices. ([PMC][baduanjin-review])

GymPrimer should therefore add Baduanjin with images, but it should not generate all possible images at once.
The page should use a ranked image list and start with the top five most necessary images.

## Goals

- Add a beginner-facing Baduanjin page, likely `exercises/baduanjin-basics.md`.
- Use the title `Baduanjin Basics`.
- Include aliases: `Also known as: Ba Duan Jin, Eight Pieces of Brocade, 八段锦`.
- Evaluate the top 10 image candidates for this one page.
- Select the top five images for the first generation loop.
- Use images to teach ready stance, upward reach, bow-drawing or side-stance pattern, alternating reach or trunk length, rotation or forward-bend control, and broad muscle attention.
- Keep all instructions, muscle names, cues, safety notes, and citations in Markdown.
- Treat Baduanjin as static beginner education, not medical qigong treatment, martial arts instruction, lineage teaching, fall-prevention programming, or recovery-care programming.
- Require generated raster images to have asset files under `media/exercises/baduanjin-basics/`.
- Require exact prompt records under `media/prompts/exercises/baduanjin-basics/`.
- Require approved rows in `media/PROVENANCE.md`.
- Require meaningful alt text and manual visual-safety review.

## Non-goals

- No immediate image generation in this proposal.
- No full traditional Baduanjin course.
- No claim that Baduanjin treats disease, prevents falls for a specific reader, cures pain, improves a medical condition, fixes posture, or replaces medical care.
- No personalized balance program.
- No recovery plan, symptom-based recommendation, return-to-exercise protocol, or adaptive coaching.
- No martial application, combat application, lineage/style debate, or performance standard.
- No video, animation, camera form analysis, hosted media service, runtime app, database, or user-input flow.
- No borrowed web images, stock photos, commercial screenshots, branded equipment, identifiable people, decorative hero art, or AI-generated image as source-of-truth evidence.
- No in-image text, Chinese characters, arrows with labels, safety warnings, citations, muscle names, correct/wrong badges, red pain marks, or clinical framing.

## Vision fit

fits the current vision

This proposal fits GymPrimer's Markdown-first direction.
It adds a static, citation-backed beginner exercise page and uses images only as support assets.
It does not introduce personalized coaching, medical assessment, treatment, recovery-care behavior, hosted-app behavior, or media as source of truth.

It also follows the accepted Tai Chi proposal pattern: one exercise page, a ranked top-10 image candidate pool, a limited first image-generation batch, prompt records, provenance, and manual visual-safety proof before promotion.

## Context

The accepted Tai Chi proposal already established a useful structure for image-heavy gentle movement pages: rank the top 10 image candidates for one exercise, select the most necessary images first, keep generated media governed by prompt records and provenance, and keep the exercise page non-clinical and non-martial.

Baduanjin is similar in that it is a gentle movement practice that benefits from visual explanation.
It differs from Tai Chi Basics because it is commonly presented as a set of eight movements, so five images may be justified as a first-pass exception to the usual "up to three images" exercise-page pattern.
The top five should still be tightly controlled: each image should teach one thing, and candidates 6-10 remain deferred.

The VA describes Tai Chi and Qigong as gentle practices using slow movements, deep breathing, and focus, and notes that Qigong combines breathing, posture, focus, and slow movement. ([Veterans Affairs][va-tai-chi-qigong])
NCCIH describes qigong as involving posture, attention, and breathing, and names Baduanjin among qigong forms. ([NCCIH][nccih-qigong])
These sources support a conservative GymPrimer framing: Baduanjin can be taught as gentle movement literacy, but not as treatment, medical assessment, or a disease-specific intervention.

## Options Considered

### Option A: Generate all eight Baduanjin movement images immediately

Generate one image for each brocade plus setup and muscle-attention images.

Advantages:

- Covers the whole sequence visually.
- Gives readers many visual anchors.

Drawbacks:

- Too many images for a first pass.
- Higher prompt/provenance/review burden.
- Greater risk of inconsistent style or form.
- More likely to imply that GymPrimer is teaching a complete traditional form.

Disposition: rejected.

### Option B: Add Baduanjin as text-only first

Create `exercises/baduanjin-basics.md` without images.

Advantages:

- Lowest media governance burden.
- Fastest page draft.

Drawbacks:

- Baduanjin is movement-sequence dependent.
- Text-only explanation will likely be insufficient for beginners.
- Fails the user's clear direction that images are important.

Disposition: rejected.

### Option C: Evaluate top 10 Baduanjin image needs and generate top five

Rank the most necessary Baduanjin images, choose the top five, and generate only those first.

Advantages:

- Matches the user's image-first priority.
- Gives more visual coverage than Tai Chi's top-three batch.
- Still avoids generating every possible image.
- Fits Baduanjin's eight-movement structure.
- Keeps media governance testable.

Drawbacks:

- Five images are heavier than the normal exercise-image default.
- Requires explicit downstream justification for exceeding the usual three-image preference.
- Requires careful manual visual review to avoid martial, medical, or exact-form implications.

Disposition: recommended.

### Option D: Create separate proposals for Baduanjin content and Baduanjin images

Split the content page and image-prioritization work.

Advantages:

- Smaller proposals.

Drawbacks:

- Artificially separates the central product decision: Baduanjin needs images to be understandable.
- Creates extra governance overhead.
- Repeats work already solved by the accepted Tai Chi proposal pattern.

Disposition: rejected.

## Recommended Direction

Choose Option C.

GymPrimer should add a new Baduanjin beginner page and treat it as an image-prioritized gentle-movement exercise.

Recommended file path:

```text
exercises/baduanjin-basics.md
```

Recommended title:

```md
# Baduanjin Basics

Also known as: Ba Duan Jin, Eight Pieces of Brocade, 八段锦
```

The page should teach only beginner basics:

- ready stance;
- comfortable breathing;
- soft knees;
- upright trunk;
- relaxed shoulders;
- slow arm movement;
- gentle weight shift;
- small range of motion;
- broad muscle attention.

It should not teach a complete lineage-specific form or claim medical outcomes.

### Top 10 necessary image evaluation

Each image candidate is scored from 1-5 on five criteria:

| Criterion | Meaning |
|---|---|
| Beginner comprehension | Does the image explain something text cannot explain well? |
| Safety/setup value | Does the image reduce setup, balance, range, or posture confusion? |
| Muscle-attention value | Does the image help users understand what to pay attention to? |
| Page value | Can the image support multiple sections of this Baduanjin page? |
| Readiness | Can the image be generated and reviewed without expanding scope? |

Maximum score: 25.

### Ranked top 10 Baduanjin image candidates

| Rank | Candidate image | Page | Purpose | Why it matters | Score | Disposition |
|---:|---|---|---|---|---:|---|
| 1 | Baduanjin ready stance / Wuji setup | `exercises/baduanjin-basics.md` | `exercise_setup_illustration` | Shows safe beginner posture: feet, soft knees, upright trunk, relaxed shoulders. | 24 | Generate first |
| 2 | Two hands lift upward / holding up the sky pattern | `exercises/baduanjin-basics.md` | `exercise_movement_illustration` | A simple upward-reaching movement introduces slow breathing, shoulder relaxation, and trunk length. | 24 | Generate first |
| 3 | Bow-drawing side stance | `exercises/baduanjin-basics.md` | `exercise_movement_illustration` | Visually teaches stance width, side orientation, arm path, and calm upper-body control. | 23 | Generate first |
| 4 | Alternating one hand up / one hand down reach | `exercises/baduanjin-basics.md` | `exercise_movement_illustration` | Shows asymmetrical reach and trunk length without needing traditional theory terms. | 22 | Generate first |
| 5 | Broad muscle-attention image for Baduanjin | `exercises/baduanjin-basics.md` | `exercise_muscle_attention_illustration` | Helps beginners notice legs, glutes, trunk, shoulders, upper back, feet, and ankles without exact anatomy labels. | 22 | Generate first |
| 6 | Gentle look-back / neck-and-trunk rotation | `exercises/baduanjin-basics.md` | `exercise_movement_illustration` | Useful for teaching comfortable rotation, but higher risk of neck-overstretch misunderstanding. | 20 | Later candidate |
| 7 | Forward bend / hands-to-feet pattern with reduced range | `exercises/baduanjin-basics.md` | `exercise_movement_illustration` | Helps avoid forcing range, but may look too much like stretching or recovery care if not handled carefully. | 19 | Later candidate |
| 8 | Horse-stance fist movement | `exercises/baduanjin-basics.md` | `exercise_movement_illustration` | Part of many Baduanjin sequences, but can look martial or intense if over-emphasized. | 18 | Later candidate |
| 9 | Heel raise / closing return-to-standing | `exercises/baduanjin-basics.md` | `exercise_movement_illustration` | Good for ending control, but lower priority than setup and core sequence visuals. | 17 | Later candidate |
| 10 | Chair-supported or small-range option | `exercises/baduanjin-basics.md` | `exercise_setup_illustration` | Useful for easier-version guidance, but could imply balance therapy if presented too prominently. | 16 | Later candidate |

The selected top five are the first generation batch because they cover the minimum distinct visual concepts needed for a Baduanjin beginner page: setup, upward movement, side/stance movement, alternating reach, and broad muscle attention.
Candidates 6-10 are deferred alternatives.
They may replace a selected image later, but they do not authorize generating or publishing all 10 images.

### First five images to generate

These images should be generated later through the governed Codex/imagegen implementation path.

| Asset path | Purpose | Teaching goal |
|---|---|---|
| `media/exercises/baduanjin-basics/setup.png` | `exercise_setup_illustration` | Show beginner-ready standing posture. |
| `media/exercises/baduanjin-basics/two-hands-lift.png` | `exercise_movement_illustration` | Show the slow upward-reaching pattern. |
| `media/exercises/baduanjin-basics/drawing-bow.png` | `exercise_movement_illustration` | Show side stance and arm path without combat framing. |
| `media/exercises/baduanjin-basics/alternating-reach.png` | `exercise_movement_illustration` | Show one hand reaching upward while the other lowers. |
| `media/exercises/baduanjin-basics/muscle-attention.png` | `exercise_muscle_attention_illustration` | Show broad body regions to pay attention to. |

### Image guidance

The setup image should show a neutral adult figure, comfortable stance, soft knees, upright trunk, relaxed shoulders, arms resting naturally, and a clear uncluttered background.
It should avoid meditation iconography, clinical balance-program framing, martial posture intensity, and in-image labels.

The two-hands-lift image should show arms rising overhead or near overhead within comfortable range, a long trunk, relaxed shoulders, soft knees, calm facial/body expression, and no exaggerated backbend.
This image should teach the broad idea of slow upward reach, not exact traditional form.

The drawing-bow image should show a moderate stance, one arm extending as if drawing a bow, the other arm pulled back, torso upright, calm non-combat expression, and no weapon, arrow, target, or martial aggression.
This image should not look like combat training.

The alternating-reach image should show one hand reaching upward, the opposite hand pressing or lowering gently, trunk upright and long, relaxed shoulders, and small comfortable range.
It should avoid traditional-medicine labels or organ claims.

The muscle-attention image should show broad subtle highlights on legs and glutes, trunk, shoulders and upper back, feet, and ankles.
It should not show exact anatomy, muscle labels, red marks, or clinical overlays.
Nearby Markdown should explain the muscle roles.

### Proposed Baduanjin page structure

```md
# Baduanjin Basics

Also known as: Ba Duan Jin, Eight Pieces of Brocade, 八段锦

## What this is for

## Before you start

## Setup

## Muscles involved

## Movement breakdown

### 1. Ready stance

### 2. Two hands lift upward

### 3. Drawing the bow

### 4. Alternating reach

### 5. Return to quiet standing

## What you should feel

## Common mistakes

## How much to do

## Easier version

## Harder version

## Safety notes

## Sources
```

This page intentionally teaches a beginner introduction, not the full eight brocades.

### Recommended Baduanjin content guidance

The page should frame Baduanjin as gentle qigong movement, posture and breathing practice, coordination and body-awareness practice, and slow movement literacy.
NCCIH identifies Baduanjin as a qigong form, and qigong includes body movement and posture, breath regulation, and attention. ([NCCIH][nccih-qigong])

Beginner setup should say to practice on a clear flat surface, wear comfortable clothing, use shoes or socks that do not slip, keep movements small at first, keep a wall or stable chair nearby if balance is uncertain, and stop if dizziness, chest pain, fainting, unusual shortness of breath, sharp pain, or worsening symptoms occur. ([Veterans Affairs][va-tai-chi-qigong])
The VA frames Tai Chi and Qigong as gentle movement practices using slow movements, breathing, and focus, while noting they can be done seated or standing. ([Veterans Affairs][va-tai-chi-qigong])

The `## Muscles involved` section should use broad role-based language:

| Role | Muscle region | What it helps do |
|---|---|---|
| Support and weight shift | Legs and glutes | Help you stay grounded and move weight slowly. |
| Posture and balance | Trunk | Helps you stay tall while the arms move. |
| Arm motion | Shoulders and upper back | Help the arms rise, open, and lower without shrugging. |
| Foot control | Feet and ankles | Help you feel the ground and adjust balance. |

Avoid exact activation claims.
The project's muscle-guidance learning recommends broad role-based guidance, beginner-readable terms, and pairing `Muscles involved` with `What you should feel`.

The movement breakdown should stay small and beginner-safe:

```md
### 1. Ready stance

Stand tall with feet comfortable, knees soft, and shoulders relaxed.

### 2. Two hands lift upward

Let the arms rise slowly while the trunk stays long and the breath stays easy.

### 3. Drawing the bow

Step or shift into a comfortable stance and open the arms as if drawing a bow, without forcing the shoulders or knees.

### 4. Alternating reach

Let one hand reach upward while the other lowers, keeping the movement smooth and comfortable.

### 5. Return to quiet standing

Bring the body back to a relaxed standing position and breathe normally.
```

The page should not teach full style-specific details.

The `## How much to do` section should use `low_load_control_drill` unless the accepted exercise-method spec later defines a more specific `qigong_sequence` type:

```md
## How much to do

Method type: low_load_control_drill

Beginner starting point:
- Practice for 3-5 minutes.
- Use small, slow movements.
- Stop before balance, posture, breathing, or attention breaks down. ([Veterans Affairs][va-tai-chi-qigong])

Effort:
- Keep the movement easy and controlled.
- You should be able to breathe normally.

Rest:
- Rest as needed between short practice rounds.

Progression:
- First make the movement smoother.
- Then practice for a little longer.
- Do not make the stance deeper or the range larger just to make it harder.
```

The project's exercise-method proposal defines method guidance by training type and includes low-load control drills as short practice sets or slow reps with control-first progression.

Safety notes should include starting with small range, avoiding deep knee bending in the first version, avoiding forced neck/shoulder/back/hamstring range, using a wall or chair nearby if balance is uncertain, seeking qualified help if balance, dizziness, medical condition, medication, or injury history makes practice uncertain, and stopping for chest pain, fainting, severe dizziness, unusual shortness of breath, sharp pain, numbness, weakness, or worsening symptoms. ([Veterans Affairs][va-tai-chi-qigong])
The page should link to `RED-FLAGS.md`.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Refer to the Tai Chi proposal | in scope | Context; Recommended direction |
| Generate a Baduanjin proposal | in scope | Full proposal |
| Use top five images to expand the exercise | in scope | Top 10 evaluation; First five images |
| Follow best practices | in scope | Context; Testing and verification strategy; Risks and mitigations |
| Keep media governed by imagegen/provenance workflow | in scope | Goals; Architecture impact; Rollout and rollback |
| Preserve safety and non-clinical boundaries | in scope | Non-goals; Risks and mitigations |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Baduanjin beginner exercise page | core to this proposal | Main content addition. |
| Top-10 image evaluation | core to this proposal | Required to prioritize visual work. |
| First five selected images | core to this proposal | Required by the user's direction. |
| Five-image exception for sequence-based exercise | same-slice dependency | Needed because the accepted Tai Chi model used three images; Baduanjin's sequence justifies more. |
| Image prompt engineering | first-slice candidate | Needed before generation. |
| Codex/imagegen generation | separate implementation slice | Should happen after prompts, prompt records, provenance rows, and review criteria are accepted. |
| `media/PROVENANCE.md` rows | same-slice dependency | Required when generated raster assets are introduced. |
| Prompt records | same-slice dependency | Required by the accepted image workflow. |
| Manual visual-safety review | same-slice dependency | Required before promotion. |
| Beginner comprehension proof | same-slice dependency | Needed to show images improve understanding. |
| Full eight-movement Baduanjin course | out of scope | Too broad and style-specific. |
| Medical qigong or fall-prevention program | out of scope | Requires clinical governance. |
| Video or animation | out of scope | Different media product. |

## Expected Behavior Changes

After downstream implementation:

- GymPrimer has a clear Baduanjin beginner page.
- The Baduanjin page has a ranked top-10 image candidate pool.
- The first image-generation loop has exactly five selected images.
- The five images teach setup, key movement patterns, and broad muscle attention.
- Generated Baduanjin images have prompt records, approved provenance rows, useful alt text, and manual visual-safety review evidence.
- The page remains static, Markdown-first, citation-backed, and non-clinical.
- Future Baduanjin visual work can reuse the ranking process instead of choosing images ad hoc.

## Architecture Impact

Expected touched surfaces:

| Surface | Impact |
|---|---|
| `exercises/baduanjin-basics.md` | New exercise page. |
| `media/exercises/baduanjin-basics/` | New generated image directory when assets are introduced. |
| `media/prompts/exercises/baduanjin-basics/` | New prompt-record directory when assets are introduced. |
| `media/PROVENANCE.md` | Add rows for generated raster images. |
| `SOURCES.md` | Add reused Baduanjin/Qigong sources if shared beyond the page. |
| `specs/exercise-image-standard.md` | May need a narrow exception or clarification for five images on sequence-based exercises. |
| `specs/exercise-method-guidance.md` | Confirm use of `low_load_control_drill` or introduce a later `qigong_sequence` method type. |
| `tools/checks/check_markdown_first.py` | No change unless current validation cannot enforce prompt records, provenance, image purposes, or image-count exception. |

No runtime, hosted app, video platform, generated JSON, user account, personalized coaching, or tracker is needed.

## Testing and Verification Strategy

Automated checks should cover:

```text
exercises/baduanjin-basics.md
media/exercises/baduanjin-basics/
media/prompts/exercises/baduanjin-basics/
media/PROVENANCE.md
SOURCES.md
RED-FLAGS.md
```

Checks should verify:

- the page has required exercise sections;
- citations are page-local;
- reused source IDs appear in `SOURCES.md` when required;
- wording avoids medical assessment, treatment, recovery programming, fall-prevention protocol, martial instruction, and personalized programming;
- image paths are local and relative;
- image alt text is meaningful;
- each generated raster image has a matching approved provenance row;
- each generated raster image has a matching prompt record;
- image purpose is allowed;
- `review_status` is approved before promotion;
- privacy scan passes.

Manual visual-safety review should confirm:

- each image teaches one concept;
- no in-image text;
- no identifiable person;
- no brand marks;
- no pain marks;
- no clinical or recovery-care framing;
- no combat framing;
- no exact anatomy claim;
- Baduanjin posture looks calm, beginner-safe, and non-aggressive;
- muscle highlighting is broad and subtle;
- alt text matches the image purpose.

Beginner comprehension proof should ask whether a beginner reader can explain:

- what Baduanjin practice is for;
- how to stand at the start;
- what the upward reach teaches;
- what drawing the bow means in this page;
- what alternating reach means;
- what body regions to pay attention to;
- when to pause;
- whether the five images helped more than text alone.

Prior GymPrimer review found that general approval after images were added is not enough.
Manual proof should record whether the reader can explain page-level comprehension outcomes.

## Rollout and Rollback

Rollout:

1. Review this proposal.
2. Confirm the top-10 image ranking.
3. Confirm the first five Baduanjin images.
4. Draft a focused spec or spec amendment for the Baduanjin page contract, top-10 image ranking, top-five first generation batch, and five-image exception for sequence-based gentle movement.
5. Prepare exact prompts for the top five images.
6. Generate images through Codex/imagegen in an implementation loop.
7. Add generated assets under `media/exercises/baduanjin-basics/`.
8. Add prompt records under `media/prompts/exercises/baduanjin-basics/`.
9. Add `media/PROVENANCE.md` rows.
10. Add Markdown image references and alt text.
11. Run automated checks.
12. Run manual visual-safety review and beginner comprehension proof.

Rollback:

- If a generated image fails review, remove the Markdown reference, remove or replace the asset, remove or update the provenance row, remove or update the prompt record if the asset is not retained, and keep the text-only page.
- If five images prove too many, keep the setup, one key movement, and muscle-attention images; defer the remaining two images; and update the image ranking and page evidence accordingly.
- If Baduanjin scope becomes too broad, narrow the page to ready stance, two-hands-lift, and return-to-standing; keep the remaining image candidates as future alternatives.

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---:|---|
| Images imply therapy, medical qigong treatment, or fall-prevention programming | High | Use neutral education framing; avoid clinical and outcome-guarantee language. |
| Page becomes a martial-arts or lineage curriculum | Medium | Teach only beginner basics and avoid style-specific authority claims. |
| User with balance issues tries unsupported practice | High | Include wall/chair support, small range, stop criteria, and routing to qualified help. ([Veterans Affairs][va-tai-chi-qigong]) |
| Five images create visual overload | Medium | Each image should teach one concept; keep candidates 6-10 deferred. |
| Drawing-bow image looks aggressive or combat-focused | Medium | No weapon, target, facial aggression, or martial-intensity framing. |
| Muscle highlighting becomes too anatomical | Medium | Highlight broad regions only; keep muscle names and sources in Markdown. |
| Image provenance or prompt records are incomplete | High | Require exact prompt records and approved `media/PROVENANCE.md` rows before promotion. |
| Source claims overstate Baduanjin evidence | High | Use cautious general-education language; avoid treatment or prevention claims. |
| Cultural oversimplification | Medium | Use Baduanjin respectfully as a movement practice; avoid unnecessary spiritual, medical, or lineage claims. |

## Open Questions

None blocking proposal review.

Downstream implementation can decide:

- exact image prompts;
- exact provenance reviewer handle;
- whether file path should be `baduanjin-basics.md` or `ba-duan-jin-basics.md`;
- whether `low_load_control_drill` is sufficient or a future `qigong_sequence` method type is needed;
- whether title should favor `Baduanjin Basics` or `Ba Duan Jin Basics`.

Recommended default:

```text
File path: exercises/baduanjin-basics.md
Title: Baduanjin Basics
Alias line: Also known as Ba Duan Jin, Eight Pieces of Brocade, 八段锦
```

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-06 | Add Baduanjin as a new beginner exercise page. | It is beginner-relevant and image-dependent. | Delay Baduanjin; add generic qigong page first. |
| 2026-07-06 | Evaluate top 10 Baduanjin image candidates before generation. | Prevents random or excessive image generation. | Generate images opportunistically. |
| 2026-07-06 | Generate top five first. | Baduanjin is sequence-based and needs more visual support than a single posture page. | Generate all 10; use only one image. |
| 2026-07-06 | Keep Baduanjin static and non-clinical. | Preserves GymPrimer's educational boundary. | Medical qigong, therapy protocol, martial curriculum. |
| 2026-07-06 | Use `baduanjin-basics.md` as default path. | Concise, searchable, and consistent with English pinyin usage. | `ba-duan-jin-basics.md` unless maintainers prefer separated pinyin. |

## Next Artifacts

1. Proposal review.
2. Focused spec or spec amendment for the Baduanjin page contract, top-10 image candidate evaluation, top-five image generation selection, and five-image exception for sequence-based gentle movement.
3. Prompt set for the first five Baduanjin images.
4. Draft `exercises/baduanjin-basics.md`.
5. Prompt records for generated assets.
6. `media/PROVENANCE.md` rows for generated assets.
7. Manual visual-safety review.
8. Beginner comprehension proof.

## Follow-on Artifacts

- Proposal review R1: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/proposal-review-r1.md`
- Owner acceptance: recorded from user approval on 2026-07-06.

## Readiness

This proposal is accepted after proposal-review R1 and owner approval.

It is not ready for implementation until the project confirms:

- the first five image prompts;
- prompt-record paths;
- provenance rows;
- reviewer handle;
- visual-safety review criteria;
- beginner-comprehension proof format;
- whether a five-image exception is accepted for this sequence-based page.

The first implementation should stay narrow: one Baduanjin page, five generated support images, source-backed Markdown, and manual proof that the images improve beginner comprehension.

[nccih-qigong]: https://www.nccih.nih.gov/health/qigong-what-you-need-to-know
[baduanjin-review]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5359459/
[va-tai-chi-qigong]: https://www.va.gov/WHOLEHEALTH/cih/Tai_Chi_and_Qigong.asp
