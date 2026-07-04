# Exercise Method Guidance by Training Type

## Status

accepted

## Problem

GymPrimer exercise pages explain purpose, setup, muscles, movement steps, feel
cues, mistakes, easier versions, harder versions, safety notes, and sources.
They do not yet give readers a consistent answer to the next beginner question:
"How much of this should I do?"

That gap makes exercise pages less practical. A beginner can learn what a chin
nod, wall slide, chest press, plank, or kneeling hip-flexor stretch is, but the
page may not tell them whether to use repetitions, timed holds, short practice
sets, stretch holds, rest intervals, or a progression cue. Adding one generic
sets-and-reps line to every page would also be wrong, because different training
types need different beginner methods.

The product problem is to make exercise pages practically usable while
preserving GymPrimer's boundary: static, citation-based education for general
beginners, not a personalized workout prescription, rehab protocol, or adaptive
program.

## Goals

- Add a reusable beginner method section to exercise pages that gives a general
  starter range for amount, effort, rest, and progression.
- Support different training types instead of forcing every exercise into the
  same repetitions-per-set format.
- Keep exercise pages educational and non-prescriptive by framing ranges as
  examples or starting points for healthy adult beginners.
- Make pattern-page exercise previews and full exercise pages align, so a
  preview's starter range does not conflict with the linked exercise page.
- Preserve citation discipline for effort, progression, safety, and training
  volume claims.
- Provide enough structure that future validation can check for missing method
  guidance, forbidden personalization, broken safety routing, and stale source
  support.

## Non-goals

- No individualized workout plan, adaptive program, symptom-based
  substitution, or goal-specific prescription.
- No injury-specific return-to-training guidance, rehabilitation protocol,
  diagnosis, pain treatment, or posture-correction routine.
- No optimization advice for advanced lifters, athletes, powerlifting,
  Olympic lifting, kettlebell ballistic lifting, sprinting, plyometrics, or
  sport-specific programming.
- No calculator, user intake, training log, progression algorithm, or hosted
  app behavior.
- No requirement that every existing exercise page be rewritten in one
  unreviewed batch.

## Vision fit

fits the current vision

The current vision says GymPrimer teaches exercise, movement, and training
literacy through short, citation-backed Markdown pages. It also says exercise
pages explain what an exercise is for, setup, muscles, movement, feel cues,
mistakes, easier and harder versions, safety notes, and sources. The
constitution permits general starter ranges such as sets, reps, hold times,
rest, frequency, and progression cues when they are static beginner education
and not individualized prescriptions.

This proposal fits that boundary by improving practical exercise literacy. It
does not revise GymPrimer into a workout planner, clinical product, AI coach,
or personalized programming tool.

## Context

The accepted Markdown-first primer spec defines the baseline exercise-page
contract, including purpose, setup, muscles, movement breakdown, feel cues,
common mistakes, easier and harder versions, safety notes, and sources.

The accepted Responsible Breadth direction already recognizes the beginner
pain point around "how many sets and reps to do" and allows programming
literacy, generic program examples, and pattern-page starter ranges under
non-prescriptive boundaries. `specs/responsible-breadth.md` also states that
pattern-page exercise previews can include starter ranges, while full exercise
instructions remain in the linked exercise page.

The current exercise template, `docs/templates/exercise-card.md`, has no
dedicated section for amount, effort, rest, or progression. Existing exercise
pages sometimes mention control or progression inside `Harder version`, but
that placement is inconsistent and does not teach different training methods.

Recent source review supports a flexible approach. CDC adult activity guidance
uses a broad public-health frame: muscle-strengthening activities for major
muscle groups on two or more days per week. Mayo Clinic weight-training
guidance says beginners can start with a weight they can lift comfortably
12 to 15 times, and its stretching guidance supports gentle stretching, no
bouncing, backing off from pain, roughly 30-second holds, and repeated rounds.
ACSM's updated resistance-training guidance emphasizes consistency, effort, and
individualization over rigid one-size-fits-all prescriptions, while still
discussing useful ranges for sets, load, and volume. Those sources support
beginner starter ranges, not exact personal prescriptions.

Source-basis references for the downstream spec:

| Source | Proposal use |
| --- | --- |
| [CDC - Adding Physical Activity as an Adult](https://www.cdc.gov/physical-activity-basics/adding-adults/index.html) | Public-health context for weekly adult activity and muscle-strengthening frequency. |
| [Mayo Clinic - Weight training technique](https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842) | Beginner resistance-training setup, 12-15 comfortable repetitions, form, breathing, rest, and pain stop language. |
| [Mayo Clinic - A guide to basic stretches](https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/stretching/art-20546848) | Stretch hold duration, gentle effort, no bouncing, repeated rounds, and pain backoff language. |
| [ACSM - 2026 resistance training guidelines update](https://acsm.org/resistance-training-guidelines-update-2026/) | Consistency-first framing, resistance-training participation, and flexible non-one-size-fits-all approach. |

## Options Considered

### Option A: Do nothing

Leave exercise pages as technique-only pages and rely on principle or program
pages for training amount.

Advantages: smallest scope and lowest safety risk.

Disadvantages: exercise pages remain incomplete for beginners who need a simple
starting method at the point of use. Pattern-page previews can name starter
ranges while the full exercise page may not explain them.

Disposition: rejected. The user pain point is real and already recognized by
the accepted Responsible Breadth direction.

### Option B: Add one standard sets-and-reps line to every exercise

Add a single default such as "2-3 sets of 8-12 reps" to all exercise pages.

Advantages: simple to write, easy to validate, familiar to readers.

Disadvantages: inaccurate for holds, stretches, mobility drills, low-load
awareness drills, carries, and cardio equipment. It also risks sounding like a
prescription when the page should teach a method.

Disposition: rejected. One range cannot fit the repository's exercise variety.

### Option C: Add method guidance by training type

Classify each exercise page by a small set of beginner training types and add a
method section whose starter range matches the type.

Advantages: practical for readers, compatible with existing exercise pages,
and easier to keep non-prescriptive because each method can explain what the
range means. It can support dynamic resistance exercises, bodyweight
progressions, low-load control drills, isometric holds, mobility drills,
stretch holds, loaded carries, and cardio-machine entries if those appear in
scope.

Disadvantages: requires a spec update, template update, content audit, source
support, and validation rules. Some exercises may reasonably fit more than one
type.

Disposition: recommended.

### Option D: Put all method guidance only in programming-principle pages

Keep exercise pages technique-only, and create or expand principle pages about
sets, reps, holds, rest, progression, and training frequency.

Advantages: centralizes training concepts and reduces repeated wording.

Disadvantages: does not answer the page-local "how do I try this exercise?"
question. It forces beginners to combine a technique page with a principle page
before they can act.

Disposition: rejected as the primary solution, but useful as supporting
context. Principle pages can explain concepts more deeply while exercise pages
carry concise starter guidance.

## Recommended Direction

Choose Option C: add beginner method guidance by training type to exercise
pages.

Each exercise page should identify the kind of training method it uses and give
a concise, cited starter range. The section should be called `How much to do`.

The proposed training-type menu is:

| Training type | Method guidance shape |
| --- | --- |
| `dynamic_resistance` | Sets, reps, effort, rest, and when to add load or reps. |
| `bodyweight_progression` | Sets, reps or time, easier/harder variation cue, and form-quality stop. |
| `low_load_control_drill` | Short practice sets, slow reps or brief holds, low effort, and control-first progression. |
| `isometric_hold` | Sets, hold duration, breathing cue, rest, and stop condition for bracing or shaking form loss. |
| `mobility_drill` | Slow repetitions or short holds, comfortable range, and no forcing end range. |
| `stretch_hold` | Hold duration, number of rounds, relaxed effort, and no sharp or worsening symptoms. |

The ranges should be educational starter ranges for general healthy beginners,
not commands to follow exactly. Exercise pages should also link to a broader
programming-principle page when the reader needs context about weekly frequency,
sets, reps, progression, or recovery.

Use `loaded_carry` and `basic_cardio_equipment` later only when carry or cardio
equipment pages exist again in scope.

The visible page shape should be:

```md
## How much to do

Method type: dynamic_resistance

Beginner starting point: ...
Effort: ...
Rest: ...
Progression: ...
Stop if: ...
```

`How much to do` should be the section heading because it matches the beginner's
question directly. `Method type` should be visible structured text, not hidden
metadata or YAML front matter, so Markdown remains the source of truth. A future
checker can parse the visible line.

The editorial starter-range defaults are:

| Training type | Editorial starter range |
| --- | --- |
| `dynamic_resistance` | 1-3 sets of 8-15 reps; stop with controlled form; rest 60-120 seconds; progress by adding reps first, then a small load increase. |
| `bodyweight_progression` | 1-3 sets of 5-12 reps or 10-30 seconds; choose an easier variation if form breaks; progress by harder variation before adding volume. |
| `low_load_control_drill` | 1-2 short practice sets of 5-10 slow reps or 5-10 second holds; low effort; rest as needed; progress by smoother control, not fatigue. |
| `isometric_hold` | 2-3 holds of 10-30 seconds; breathe normally; rest 30-90 seconds; stop when bracing, posture, or breathing breaks. |
| `mobility_drill` | 1-2 rounds of 5-10 slow reps or brief comfortable holds; use easy range; do not force end range. |
| `stretch_hold` | 1-3 rounds of 10-30 seconds, or about 30 seconds; relaxed effort; no bouncing; stop or back off for pain. |

These ranges are editorial defaults. Page-level method guidance still needs
direct source support where the page makes specific amount, progression, effort,
or safety claims.

The first proof slice should use six exercise pages, one for each currently
adopted method type:

| Page | Training type |
| --- | --- |
| `exercises/chest-press.md` | `dynamic_resistance` |
| `exercises/incline-push-up.md` | `bodyweight_progression` |
| `exercises/chin-nod.md` | `low_load_control_drill` |
| `exercises/plank.md` | `isometric_hold` |
| `exercises/thoracic-extension.md` | `mobility_drill` |
| `exercises/kneeling-hip-flexor-stretch.md` | `stretch_hold` |

The first implementation should also create or update
`principles/sets-reps-holds-rest-and-progression.md` before broad rollout. That
principle page should briefly explain sets, reps, timed holds, easy/moderate/hard
effort, one-variable-at-a-time progression, and why starter ranges are
educational examples rather than personal prescriptions.

## Expected Behavior Changes

- Exercise pages gain a consistent place where beginners can find starter
  amount, effort, rest, and progression guidance.
- A stretch page can use hold time, a plank page can use timed holds, a wall
  slide can use controlled practice reps, and a machine lift can use sets and
  reps.
- Pattern pages that preview exercises can point to full exercise pages whose
  method guidance agrees with the preview.
- Contributors get a clearer authoring contract for adding or reviewing
  exercises.
- Readers see stronger plain-language boundaries: the ranges are starting
  education, not personalized programming.

## Architecture Impact

The change affects Markdown content contracts, templates, validation tooling,
and citation expectations. It does not require a hosted application, database,
runtime API, generated HTML dependency, user account, or tracking system.

## Normative Artifact Path

Exercise method guidance should be specified in a focused spec:

`specs/exercise-method-guidance.md`

Markdown-first and Responsible Breadth should receive compatibility notes only
where needed. The focused spec owns the training-type menu, section structure,
starter-range shapes, source-support rules, non-prescriptive wording boundaries,
and pattern-page preview alignment.

Expected touched surfaces:

- `specs/exercise-method-guidance.md` as the normative source for this change.
- `specs/markdown-first-primer.md` only for compatibility notes where the
  baseline exercise-page contract needs to reference the focused spec.
- `specs/responsible-breadth.md` only for compatibility notes where pattern-page
  starter ranges need alignment with full exercise-page method guidance.
- `docs/templates/exercise-card.md` for the new method section.
- Exercise Markdown files under `exercises/` as content is updated in reviewed
  slices.
- Markdown validation checks if required-section, forbidden-language, source,
  and cross-link rules are automated.
- Existing principle pages or a new principle page for deeper explanation of
  sets, reps, holds, rest, and progression.

No architecture decision should be needed for visible structured Markdown text.
Architecture review becomes relevant only if a later spec revision introduces
a shared taxonomy file, generated index, machine-readable metadata, or a
cross-page data model.

## Testing and Verification Strategy

Verification should combine automated checks with manual content review.

Likely automated checks:

- Exercise pages contain the chosen method section after the contract is
  adopted.
- Method sections avoid personalized-programming language, diagnosis, treatment,
  rehab, guaranteed-fix wording, and symptom-based adaptation.
- Method sections link to page-local sources where training amount, effort,
  progression, or safety claims need support.
- Pattern-page starter ranges do not exist without a linked exercise page or
  explicit draft-only treatment.
- Markdown-first and privacy checks continue to pass.

Likely manual proof:

- Source audit samples confirm that cited sources actually support the training
  amount, effort, progression, or safety claims being made.
- Beginner comprehension evidence confirms that a reader can explain what to do
  first, what effort should feel like, when to stop, and why the page is not a
  personal program.
- Review samples check at least one exercise from each adopted training type
  before broad rollout.

## Rollout and Rollback

Rollout should be staged:

1. Settle this proposal through proposal review.
2. Update the relevant spec or create a focused exercise-method spec.
3. Update the exercise template and validation expectations.
4. Apply the method section to a small proof slice covering different training
   types.
5. Expand to the remaining exercise pages after review and verification.

Rollback is straightforward because Markdown is the source of truth. If review
finds the section too prescriptive or poorly sourced, remove or narrow the
method section from the affected pages and keep the existing exercise technique
contract. If a training type proves too ambiguous, move that type back to an
open question before broad content updates.

## Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| Starter ranges read like a personal prescription. | Use wording such as "beginner starting point" and "general education"; prohibit adaptive language based on symptoms, goals, or training response. |
| Different exercise types are classified inconsistently. | Define a small training-type menu in the spec and include examples from current repository pages. |
| Method guidance is under-sourced. | Require page-local support for amount, effort, progression, and safety claims, with source-audit sampling before promotion. |
| Existing exercise pages are rewritten too broadly. | Use a proof slice first and avoid broad batch rewrites until the contract is reviewed. |
| Ranges conflict with principle or program pages. | Link method sections to the relevant principle page and add review checks for obvious contradictions. |
| Safety routing becomes too heavy. | Keep stop conditions concise and link to `RED-FLAGS.md` for professional-care routing. |
| Card pages become too long. | Keep the method section compact and move deeper explanation to principle pages. |

## Resolved Decisions for First Implementation

| Question | Decision |
| --- | --- |
| Section heading | Use `How much to do`. |
| Training type representation | Use visible structured text as the source of truth, e.g. `Method type: dynamic_resistance`. Do not use hidden-only metadata in the first version. |
| Training types now | Adopt `dynamic_resistance`, `bodyweight_progression`, `low_load_control_drill`, `isometric_hold`, `mobility_drill`, and `stretch_hold`. |
| Training types later | Defer `loaded_carry` and `basic_cardio_equipment` until those page categories exist. |
| Starter ranges | Use the starter-range table in this proposal as editorial defaults; page-level claims still need source support. |
| Principle page dependency | Add or update a short principle page for sets, reps, holds, rest, and progression as a same-slice dependency before broad rollout. |
| First proof slice size | Use six exercise pages, one per currently adopted training type. |

## Open Questions

None for proposal-review R2. The downstream spec can still refine exact wording
examples and validation fixtures without reopening the proposal's core
direction.

## Initial Intent Preservation

| Initial user goal | Proposal treatment | Where recorded |
| --- | --- | --- |
| Provide specific exercise instructions for each exercise, including repetitions per set and sets per exercise. | in scope | Problem, Goals, Recommended Direction, Expected Behavior Changes |
| Provide appropriate methods for different types of training. | in scope | Goals, Options Considered, Recommended Direction, Scope Budget |
| Improve exercises in the repository. | in scope | Goals, Rollout and Rollback, Scope Budget |
| Avoid drifting into personalized workout planning. | in scope | Non-goals, Vision fit, Risks and Mitigations |

## Scope Budget

| Work item | Treatment | Reason |
| --- | --- | --- |
| Exercise-page method contract | core to this proposal | The main decision is whether exercise pages should include amount, effort, rest, and progression guidance. |
| Training-type menu | core to this proposal | Different exercises need different method shapes, so the menu is part of the product direction. |
| Exercise template update | same-slice dependency | Authors need a stable place to put the method guidance after the spec settles. |
| Validation checks | same-slice dependency | The project needs a way to catch missing sections and forbidden prescription language. |
| First proof-slice exercise updates | first-slice candidate | Six pages should test dynamic resistance, bodyweight progression, low-load control, isometric hold, mobility, and stretch guidance before broad rollout. |
| Broad update of every exercise page | separate implementation slice | Updating all pages at once increases review and sourcing risk. |
| New programming-principle page for sets, reps, holds, rest, and progression | same-slice dependency | Exercise pages should link to one short concept page instead of repeating long explanations. |
| Program examples or weekly routines | out of scope | The proposal improves exercise pages, not static program examples. |

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-04 | Recommend exercise-page method guidance by training type. | It answers the user's practical instruction need without forcing every exercise into one sets-and-reps format. | Do nothing; one universal sets-and-reps line; principle-page-only guidance. |
| 2026-07-04 | Keep guidance static and non-prescriptive. | This preserves GymPrimer's Markdown-first education boundary and avoids personalized programming. | Adaptive programming, symptom-based substitution, goal-specific plans. |
| 2026-07-04 | Use a proof slice before broad exercise updates. | Training-type wording, source support, and validation need review before repository-wide edits. | Rewrite all exercise pages immediately. |
| 2026-07-04 | Use a focused exercise-method-guidance spec. | The method section changes the exercise-page contract and needs one clear normative home. | Put all rules into Markdown-first; put all rules into Responsible Breadth; leave artifact choice to spec. |

## Next Artifacts

- Proposal-review R2 for product fit, scope boundaries, and downstream
  readiness.
- Focused spec at `specs/exercise-method-guidance.md`, including section name,
  training-type menu, source rules, wording boundaries, examples, and acceptance
  criteria.
- Spec review before template, validation, or content implementation.
- Architecture assessment only if the spec introduces machine-readable metadata,
  shared taxonomy files, generated indexes, or new validation architecture.
- Execution plan and test specification for the first proof slice after the
  spec is approved.

## Follow-on Artifacts

- Spec: `specs/exercise-method-guidance.md`

## Readiness

Accepted and handed off to `specs/exercise-method-guidance.md`.
