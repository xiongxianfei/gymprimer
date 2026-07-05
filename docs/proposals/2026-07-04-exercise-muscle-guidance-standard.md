# Proposal: Exercise Muscle Guidance Standard

## Status

accepted

This proposal records a content-quality direction for improving all GymPrimer exercise documents with clearer, safer, more useful guidance on how beginners should engage or pay attention to their muscles while exercising.

It does not authorize immediate rewrites of all exercise pages, checker changes, image generation, template changes, or broad repository edits until proposal review and downstream artifacts approve the direction.

## Problem

GymPrimer exercise pages already include muscle-related sections, but the current implementation is not fully consistent. Some pages use `## Muscles involved`, older pages use `## Used muscles`, and the amount of action-oriented muscle guidance varies across pages. A recent learning record found that the rowing-machine page made muscle guidance more useful by tying muscle groups to movement roles: legs and glutes start the drive, trunk transfers posture and force, and upper back, lats, and arms finish the pull.

Beginners do not only need a list of muscles. They need to understand:

- which broad muscle regions matter;
- what each region contributes to the movement;
- what they should feel;
- what they should avoid overusing;
- how muscle attention changes across setup, drive, pull, hold, return, or recovery phases;
- when a cue is only a broad learning aid, not a precise activation claim.

Without a standard, muscle sections can become either too vague:

```md
Muscles: back, arms, core.
```

or too overconfident:

```md
This exercise activates your lower trapezius and rotator cuff exactly if you do it correctly.
```

The project needs a durable exercise-muscle-guidance standard that helps beginners develop body awareness while preserving GymPrimer's Markdown-first, source-backed, non-clinical boundaries.

## Goals

- Standardize muscle guidance across all exercise documents.
- Prefer `## Muscles involved` as the section name for new and revised exercise pages.
- Make muscle guidance role-based, not just a list of anatomy terms.
- Tie muscle roles to movement phases when useful.
- Pair `## Muscles involved` with `## What you should feel`.
- Use beginner-readable language first, with technical names only when useful and source-supported.
- Explain common compensation patterns carefully without diagnosing the reader.
- Keep exact muscle names, cues, caveats, and citations in Markdown.
- Allow optional muscle-attention images when they materially improve comprehension.
- Preserve page-local source support for muscle, feel-cue, technique, and safety claims.
- Improve all current exercise documents over time through small implementation loops, not one broad rewrite.

## Non-goals

- No exact muscle activation percentages.
- No EMG interpretation as beginner instruction unless carefully framed.
- No individualized cueing.
- No diagnosis, rehabilitation, pain treatment, posture-correction promise, or "fix your dysfunction" language.
- No claim that a reader is using the "wrong" muscle because they do not feel the exercise exactly as described.
- No requirement that every page must have a muscle-attention image.
- No anatomy diagram as source of truth.
- No immediate migration of every existing page in one PR.
- No new exercise inventory.
- No personalized workout, symptom-based substitution, or adaptive coaching.

## Vision fit

fits the current vision

GymPrimer's current direction already expects exercise pages to explain purpose, setup, muscles involved, movement breakdown, practical feel cues, common mistakes, easier and harder versions, safety notes, and sources. The exercise-method proposal also identifies the existing exercise-page contract as including muscles and feel cues.

This proposal improves that existing contract. It does not change GymPrimer into a clinical product, rehab guide, personalized coaching tool, or anatomy reference.

## Context

The current learning record identifies a promising pattern: muscle guidance works best when it is tied to movement roles. The rowing-machine page is the clearest example: it explains which muscle groups contribute to the drive, posture/transfer, and finish, rather than listing muscles separately from the movement.

The same learning record recommends future proposal/spec/template work for an exercise-page muscle guidance standard, with best-practice candidates such as role-based guidance, beginner-readable language, phase-linked muscle roles, pairing `Muscles involved` with `What you should feel`, careful compensation wording, Markdown-first claims, optional muscle-attention images, page-local source support, and eventual section-name normalization.

The exercise-image standard already supports optional `exercise_muscle_attention_illustration` images, but keeps them broad, unlabeled, support-only, local, provenance-backed, and subordinate to Markdown. That aligns well with this proposal: images can help readers notice a broad region, but the actual muscle guidance should remain in text where it can be cited and reviewed.

Source discipline is important. A forward-head support exercise review found that setup, technique, muscle, feel-cue, common-mistake, and safety claims require page-local support; broad sources are not enough for specific exercise claims. Mayo Clinic similarly emphasizes proper form, controlled movement, breathing, balance across major muscle groups, and not relying on momentum when weight training. ([Mayo Clinic][1])

A second relevant constraint is cueing. Muscle attention is useful, but it should not replace clear task and movement cues. Research on attentional focus suggests that external focus can acutely improve strength performance, so GymPrimer should avoid making every cue an internal "feel this muscle" cue. The standard should combine muscle-attention cues with task-oriented form cues. ([PMC][2])

## Options considered

### Option A: Keep current muscle sections as-is

Leave each page to describe muscles in its own style.

Advantages:

- No immediate work.
- No migration burden.
- No new spec or template work.

Drawbacks:

- Muscle guidance remains inconsistent.
- Some pages may list muscles without explaining what they do.
- Beginners do not get reliable body-awareness cues across the repository.
- Future muscle-attention images may not align with page text.

Disposition: rejected.

### Option B: Require only a simple muscle list

Standardize every page to include a short list:

```md
Primary muscles:
Secondary muscles:
```

Advantages:

- Simple.
- Easy to validate.
- Familiar to readers.

Drawbacks:

- Lists do not explain how to use the muscles.
- Does not help beginners connect muscles to movement phases.
- Can encourage anatomy memorization instead of practical exercise literacy.

Disposition: rejected as insufficient.

### Option C: Add role-based muscle guidance to exercise pages

Standardize the muscle section around broad roles:

```text
driver
posture / transfer
finish / control
stabilizer
```

Then connect those roles to the movement phases and to `What you should feel`.

Advantages:

- Directly helps beginners understand how to engage muscles.
- Fits the successful rowing-machine pattern.
- Works across machine, bodyweight, band, mobility, and cardio-equipment pages.
- Keeps the text source-backed and beginner-readable.
- Supports optional muscle-attention images without turning images into source-of-truth anatomy.

Drawbacks:

- Requires template/spec updates.
- Requires page-by-page source audit.
- Some exercises may need softer language because muscle roles are less obvious or source support is limited.

Disposition: recommended.

### Option D: Build a separate anatomy or muscle atlas

Create a muscle reference section explaining every muscle in detail.

Advantages:

- Useful long-term reference.
- Could support future anatomy education.

Drawbacks:

- Too broad for the current exercise-document improvement.
- Risks turning GymPrimer into an anatomy product.
- Does not solve page-local exercise cueing directly.

Disposition: deferred follow-up.

## Recommended direction

Choose Option C: role-based muscle guidance for exercise pages.

Each exercise page should have a `## Muscles involved` section that answers:

1. Which broad muscle groups matter?
2. What does each group do in this movement?
3. When in the movement should the reader pay attention to them?
4. What should the reader feel?
5. What compensation should the reader avoid?
6. What claims are uncertain, optional, or not worth overthinking?

The section should be concise. It should not become an anatomy essay.

## Proposed page pattern

### Standard section order

```md
## Muscles involved

## What you should feel
```

The two sections should work together:

| Section | Purpose |
| --- | --- |
| `Muscles involved` | Explains broad roles: what each muscle group contributes. |
| `What you should feel` | Turns the roles into practical beginner body awareness. |

## Recommended `## Muscles involved` structure

Use a table or short bullets.

### Option 1: Table format

```md
## Muscles involved

| Role | Muscle region | What it helps do |
|---|---|---|
| Main driver | Upper back and lats | Start and control the pull. |
| Support | Arms and grip | Help finish the pull without taking over. |
| Posture / transfer | Trunk | Keeps the ribs and pelvis steady while the arms move. |
```

### Option 2: Short bullet format

```md
## Muscles involved

- **Main driver:** upper back and lats help create the pull.
- **Support:** arms and grip help finish the movement.
- **Posture / transfer:** trunk muscles help keep your body from swinging.
```

Use the table when there are three or more meaningful roles. Use bullets for simple drills.

## Recommended role vocabulary

| Role | Meaning | Example |
| --- | --- | --- |
| `main driver` | Muscle group doing most of the movement work. | Chest in a chest press. |
| `support` | Helps the main movement but should not dominate. | Triceps in a chest press. |
| `posture / transfer` | Helps maintain position or transfer force. | Trunk during a rower drive. |
| `finish / control` | Helps complete or control the end of movement. | Upper back during a row. |
| `stabilizer` | Helps keep a joint or body segment organized. | Shoulder-blade muscles during wall slides. |
| `mobility focus` | Area the drill is meant to move gently, not strengthen hard. | Upper back during thoracic extension. |

Do not require every page to use every role.

## Guidance by exercise type

### Machine and resistance exercises

Examples: chest press, lat pulldown, seated row, band pull-apart.

Recommended muscle guidance:

- identify the main driver;
- identify assisting muscles;
- identify trunk or shoulder-blade control where relevant;
- explain what should not take over.

Example:

```md
## Muscles involved

| Role | Muscle region | What it helps do |
|---|---|---|
| Main driver | Chest | Presses the handles away from the body. |
| Support | Triceps and front shoulders | Help finish the press. |
| Stabilizer | Upper back and shoulder blades | Help keep the shoulders from rolling forward. |
```

Mayo Clinic's weight-training guidance emphasizes controlled movement, full range of motion, balanced muscle training, and avoiding momentum, which supports keeping muscle guidance tied to form rather than isolated anatomy. ([Mayo Clinic][1])

### Low-load control drills

Examples: chin nod, wall slide, prone Y/T.

Recommended muscle guidance:

- keep language soft;
- use "pay attention to" and "practice control";
- avoid saying the drill will fix a posture pattern;
- avoid precise activation claims unless directly sourced.

Example:

```md
## Muscles involved

- **Control focus:** the front-of-neck control muscles help make the chin movement small and smooth.
- **Posture support:** upper-back and shoulder-blade muscles may help keep the shoulders relaxed.
```

### Holds and trunk exercises

Examples: plank, dead bug, bird dog.

Recommended muscle guidance:

- explain bracing and control, not just "abs";
- identify what should stay quiet or relaxed;
- pair muscle guidance with breathing.

Example:

```md
## Muscles involved

| Role | Muscle region | What it helps do |
|---|---|---|
| Main control | Abdomen and side trunk | Help keep the ribs and pelvis steady. |
| Support | Glutes and shoulders | Help hold the body position. |
```

### Mobility and stretch pages

Examples: thoracic extension, kneeling hip-flexor stretch.

Recommended muscle guidance:

- do not describe the target as a hard contraction;
- distinguish "area being moved or stretched" from "muscle being strengthened";
- emphasize gentle range and stop conditions.

Example:

```md
## Muscles involved

- **Mobility focus:** the upper back is the region being moved.
- **Support:** abdomen and neck muscles help keep the movement from turning into low-back arching or neck strain.
```

### Cardio equipment

Example: rowing machine.

Recommended muscle guidance:

- tie muscles to phases;
- avoid treating cardio equipment as a normal sets/reps lift;
- explain broad effort roles.

Example pattern:

```md
## Muscles involved

| Phase | Muscle region | What it helps do |
|---|---|---|
| Drive | Legs and glutes | Push the machine away. |
| Transfer | Trunk | Keeps posture and transfers force. |
| Finish | Upper back, lats, and arms | Complete the pull. |
| Recovery | Trunk and hips | Return with control. |
```

This follows the rowing-machine learning observation and should become a reusable model for phase-based exercises.

## Wording rules

Prefer:

```text
Pay attention to...
You may feel...
This muscle group helps...
Try to keep...
Avoid letting X take over...
```

Avoid:

```text
You must feel...
This proves...
This fixes...
This activates exactly...
Your weak muscle is...
Your posture is wrong because...
If you feel it elsewhere, you are doing it wrong.
```

## Source-support rules

Every page should follow this source-support model:

| Claim type | Source expectation |
| --- | --- |
| Broad role claim | Exercise-specific instruction source or reliable anatomy/context source. |
| Specific muscle claim | Direct source support preferred. |
| Exact setup or movement cue | Direct exercise-instruction source required. |
| Feel cue | Direct source or soft language. |
| Common compensation | Direct source or soft practical cue. |
| Safety stop condition | Institutional or clinical source preferred. |

If source support is weak, the page should soften the claim rather than overstate it.

Example:

```md
The upper back may help you control the shoulder-blade position.
```

is safer than:

```md
This exercise activates your lower trapezius.
```

unless the exact activation claim is directly supported.

## Relationship to images

Muscle-attention images are useful but optional.

The exercise-image proposal already says exercise pages may include zero to three images, with `exercise_muscle_attention_illustration` used to highlight a broad region to notice, while muscle names, cues, and citations stay in Markdown.

This proposal should reuse that rule:

- at most one muscle-attention image per exercise page;
- broad region highlight only;
- no in-image labels;
- no exact anatomy diagrams as source of truth;
- no red pain marks;
- no "wrong/correct" framing;
- provenance required for generated raster assets.

W3C guidance says informative images need text alternatives that convey the image's meaning, so any muscle-attention image should also have meaningful alt text. ([W3C][3])

## Expected behavior changes

After this proposal is implemented:

- New exercise pages use `## Muscles involved`, not `## Used muscles`.
- Revised older pages migrate toward `## Muscles involved`.
- Muscle guidance becomes role-based and phase-linked where useful.
- `## What you should feel` becomes more consistent.
- Muscle-attention images, when used, align with nearby Markdown.
- Contributors know when a muscle claim needs a stronger source.
- Reviewers can sample muscle claims alongside setup, technique, feel cues, common mistakes, and safety claims.
- Beginners get clearer guidance on what to pay attention to without being told they have a dysfunction.

## Architecture impact

Expected downstream impact:

| Surface | Expected change |
| --- | --- |
| Focused exercise-muscle-guidance spec | Define section name, role vocabulary, wording rules, source rules, image relationship, and migration behavior. |
| `docs/templates/exercise-card.md` | Update the muscle section prompt and add `What you should feel` pairing guidance. |
| `specs/exercise-image-standard.md` | Reference optional muscle-attention images if not already covered. |
| `tools/checks/check_markdown_first.py` | Later checker support may require new pages to use `## Muscles involved` and flag legacy `## Used muscles` only when migration is in scope. |
| Exercise pages | Updated in small slices, not all at once. |
| `SOURCES.md` | Add source IDs only when sources are reused across pages. |
| Manual proof records | Add source-audit sampling for muscle claims and feel cues. |

No runtime, database, hosted app, user-input flow, generated JSON, AI coach, or personalized program logic is needed.

## Testing and verification strategy

### Automated checks

After the contract is accepted, automated checks can eventually verify:

- new exercise pages contain `## Muscles involved`;
- new exercise pages contain `## What you should feel`;
- `## Used muscles` is treated as legacy-compatible only until touched;
- forbidden wording such as diagnosis, cure, guaranteed correction, or personalized coaching is absent;
- muscle-attention image purpose is valid when used;
- generated raster muscle-attention images have provenance;
- alt text exists for any image;
- page-local source sections exist.

Automated validation should not try to prove semantic correctness of muscle claims. That remains review work.

### Manual source audit

Manual review should sample:

- one main-driver claim;
- one support/stabilizer claim;
- one feel cue;
- one compensation cue;
- one safety cue;
- one image-to-Markdown alignment check if a muscle-attention image is present.

This follows prior review experience: structural checks can prove that sections and sources exist, but semantic source-support review is still needed for exercise-specific setup, technique, muscle, feel-cue, common-mistake, and safety claims.

### Beginner comprehension proof

For the first proof slice, ask a beginner reader:

- Which muscle region should you pay attention to?
- What does that muscle region help do?
- What should you feel?
- What should you avoid overusing?
- When should you stop?
- Which source would you click to verify the claim?

The prior Markdown-first read-test review found that general approval was not enough; evidence should record page-level comprehension outcomes.

## Rollout and rollback

Rollout:

1. Spec/template loop: define `## Muscles involved`, define role vocabulary, define source-support rules, and update the exercise-card template.
2. First proof slice: choose five to six representative pages: rowing machine; chest press or seated row; plank or dead bug; wall slide or chin nod; thoracic extension or hip-flexor stretch; band pull-apart.
3. Legacy normalization: migrate `## Used muscles` pages only when touched for content updates.
4. All-exercise audit: audit remaining pages in batches and decide per page whether to keep as-is, rename section only, rewrite role guidance, add or revise `What you should feel`, or add an optional muscle-attention image.
5. Checker support: add automation only after the spec and first proof slice stabilize.

Rollback:

- If the role-based format proves too long or confusing, revert affected page sections to shorter muscle bullets, keep `## Muscles involved` as the section name, remove optional role tables, and preserve `What you should feel` only where it improves comprehension.
- If muscle-attention images mislead readers, remove image references, keep Markdown guidance, remove or mark provenance rows inactive, and continue with text-only muscle guidance.

## Risks and mitigations

| Risk | Impact | Mitigation |
| --- | ---: | --- |
| Muscle guidance becomes too anatomical | Medium | Use common language first; technical names only when useful. |
| Claims become overprecise | High | Ban exact activation claims unless directly sourced. |
| Readers think they are "wrong" if they do not feel a muscle | Medium | Use "you may feel" and "pay attention to," not "you must feel." |
| Internal focus harms movement quality | Medium | Pair muscle cues with task/form cues; avoid making all cues internal. |
| Review burden grows | Medium | Use proof slices and source-audit sampling. |
| Older pages become inconsistent during migration | Medium | Treat `## Used muscles` as legacy-compatible until touched. |
| Muscle-attention images overpromise precision | High | Highlight broad regions only; keep labels and citations in Markdown. |
| Checker enforces too much too early | Medium | Add validation only after proposal/spec/template approval. |
| Contributors add unsupported muscle claims | High | Require page-local support for specific muscle and feel-cue claims. |

## Open questions

None blocking proposal review.

Downstream spec should decide:

- exact role labels;
- whether role tables or bullets are preferred by default;
- first proof-slice page list;
- checker error codes;
- whether old `## Used muscles` pages get a warning or remain silent until touched.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
| --- | --- | --- |
| Improve all exercise documents | in scope | Goals; Rollout and rollback; Scope budget |
| Add clear guidance on muscle engagement | in scope | Recommended direction |
| Use best practices | in scope | Context; Testing and verification strategy; Risks and mitigations |
| Avoid unsafe overclaiming | in scope | Non-goals; Wording rules; Risks and mitigations |
| Keep guidance beginner-friendly | in scope | Goals; Recommended direction |
| Use muscle-attention visuals where helpful | in scope | Relationship to images |
| Avoid one massive implementation batch | in scope | Rollout and rollback; Scope budget |

## Scope budget

| Work item | Treatment | Reason |
| --- | --- | --- |
| Exercise muscle guidance standard | core to this proposal | Main product decision. |
| Section-name normalization | core to this proposal | Needed to make pages consistent. |
| Role-based muscle guidance | core to this proposal | Main improvement over simple muscle lists. |
| `What you should feel` pairing | core to this proposal | Turns muscle roles into beginner body awareness. |
| Source-support rules | same-slice dependency | Prevents unsupported anatomy or activation claims. |
| Template update | same-slice dependency | Authors need stable prompts. |
| First proof-slice exercise updates | first-slice candidate | Tests whether the format works across exercise types. |
| All exercise-page migration | separate implementation slice | Too broad for one PR. |
| Checker updates | separate implementation slice | Should follow accepted contract. |
| Muscle-attention images | deferable follow-up | Useful but not required for every page. |
| Anatomy atlas | separate proposal | Broader product surface. |
| Personalized muscle cueing | out of scope | Would become coaching or adaptive guidance. |

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-04 | Propose an exercise muscle guidance standard. | Existing pages vary, and role-based guidance improves beginner comprehension. | Leave pages as-is. |
| 2026-07-04 | Prefer `## Muscles involved`. | Clearer and already used by newer exercise-page direction. | Keep mixed `Used muscles` / `Muscles involved`. |
| 2026-07-04 | Make muscle guidance role-based. | Explains how users should engage muscles, not just what muscles exist. | Simple muscle list only. |
| 2026-07-04 | Pair muscle roles with `What you should feel`. | Helps beginners translate anatomy into body awareness. | Anatomy-only section. |
| 2026-07-04 | Keep muscle images optional and support-only. | Prevents images from becoming source-of-truth anatomy. | Require muscle-attention image on every page. |
| 2026-07-04 | Migrate in small slices. | Reduces review and source-support risk. | Rewrite all exercise pages immediately. |

## Next artifacts

1. Proposal review.
2. Focused spec or spec amendment for exercise muscle guidance.
3. Exercise-card template amendment.
4. Test spec for structure, source-audit proof, and optional image alignment.
5. First proof-slice plan.
6. Implementation loop for the proof-slice pages.
7. Later all-exercise audit.

## Follow-on artifacts

- Proposal review: `docs/changes/exercise-muscle-guidance-standard/reviews/proposal-review-r1.md`

## Readiness

This proposal has a clean recorded proposal review and is accepted for downstream spec authoring.

It is not ready for implementation until a focused spec or spec amendment defines the accepted section structure, role vocabulary, wording boundaries, source-support expectations, and migration rules for legacy `## Used muscles` pages.

[1]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842 "Weight training: Do's and don'ts of proper technique - Mayo Clinic"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8622562/ "Acute and Long-Term Effects of Attentional Focus Strategies on Muscular Strength"
[3]: https://www.w3.org/WAI/tutorials/images/ "Images Tutorial | Web Accessibility Initiative (WAI)"
