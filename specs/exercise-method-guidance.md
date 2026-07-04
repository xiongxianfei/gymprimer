# Spec: Exercise Method Guidance

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-04-exercise-method-guidance.md`
- Proposal review: `docs/changes/exercise-method-guidance/reviews/proposal-review-r2.md`
- Review log: `docs/changes/exercise-method-guidance/review-log.md`
- Related baseline spec: `specs/markdown-first-primer.md`
- Related expanded-scope spec: `specs/responsible-breadth.md`
- Vision: `VISION.md`
- Constitution: `CONSTITUTION.md`

## Goal and context

This spec defines the observable contract for adding page-local exercise method
guidance to GymPrimer exercise pages. The new contract answers the beginner
question "How much of this should I do?" without turning exercise pages into
personalized programming, diagnosis, treatment, rehabilitation, or adaptive
workout planning.

The contract is Markdown-first. The visible Markdown text is the source of truth
for the method section, method type, starter range, effort, rest, progression,
and stop guidance. Optional validation tooling may parse that visible text, but
hidden metadata is not required and must not become a second source of truth in
the first version.

This spec extends the existing exercise-page contract from
`specs/markdown-first-primer.md` and aligns with pattern-page starter-range
behavior from `specs/responsible-breadth.md`.

## Glossary

- Exercise page: A Markdown page under `exercises/` that teaches one exercise
  or equipment pattern.
- Method guidance: The page-local section that describes a general beginner
  starting amount, effort, rest, progression, and stop condition for one
  exercise.
- Method type: A visible structured value inside `How much to do` that explains
  which training method shape the exercise uses.
- Editorial starter range: A general source-informed default range used by
  authors as a starting point; it is not a personal prescription.
- Dynamic resistance: A repeated strength movement using machine, dumbbell,
  cable, band, or bodyweight loading.
- Bodyweight progression: A bodyweight exercise where difficulty commonly
  changes by leverage, incline, range, or variation.
- Low-load control drill: A low-effort practice exercise emphasizing awareness,
  smooth control, or coordination rather than fatigue.
- Isometric hold: An exercise where the primary work is holding a position for
  time.
- Mobility drill: A controlled movement used to practice comfortable range of
  motion.
- Stretch hold: A gentle held position used to feel a stretch without bouncing
  or forcing pain.
- Pattern-page exercise preview: A compact exercise annotation inside a pattern
  page's `What commonly helps` section.
- Same-slice dependency: A page or validation behavior that must be included in
  the first implementation slice for the exercise-method contract to be usable.

## Examples first

Example E1: dynamic resistance page shows sets and reps
Given `exercises/chest-press.md` is updated under this spec
When a reader opens the exercise page
Then the page includes `## How much to do`
And the section includes `Method type: dynamic_resistance`
And the section explains a beginner starting point, effort, rest, progression,
and stop condition using general education language.

Example E2: stretch page uses hold guidance instead of reps
Given `exercises/kneeling-hip-flexor-stretch.md` is updated under this spec
When a reader opens `## How much to do`
Then the page uses `Method type: stretch_hold`
And the starting point is framed around gentle hold duration and rounds rather
than resistance-training sets and repetitions.

Example E3: visible method type is the source of truth
Given an exercise page includes a hidden metadata field that says
`method_type: isometric_hold`
And the visible Markdown says `Method type: dynamic_resistance`
When the page is reviewed or checked
Then the visible Markdown value is authoritative for this spec
And the page fails validation if hidden metadata is treated as the only method
type.

Example E4: pattern preview aligns with linked exercise page
Given a pattern page preview links to `exercises/plank.md`
And the preview gives a starter range for plank
When the linked exercise page is checked
Then `exercises/plank.md` includes `## How much to do`
And its method type and range shape do not contradict the pattern-page preview.

Example E5: individualized programming is rejected
Given an exercise page asks the reader about pain, goals, equipment, or training
response
When the page uses those inputs to change sets, reps, load, rest, exercise
choice, or progression
Then the page fails this spec because it has become adaptive programming.

Example E6: first proof slice covers all active method types
Given the first implementation slice is ready for review
When proof-slice coverage is checked
Then it includes `exercises/chest-press.md`,
`exercises/incline-push-up.md`, `exercises/chin-nod.md`,
`exercises/plank.md`, `exercises/thoracic-extension.md`, and
`exercises/kneeling-hip-flexor-stretch.md`
And those pages cover the six active method types defined in this spec.

Example E7: supporting principle page explains terms once
Given a reader does not know what sets, reps, holds, rest, or progression mean
When an updated exercise page references deeper method context
Then the reader can follow a link to
`principles/sets-reps-holds-rest-and-progression.md`
instead of relying on repeated long explanations in every exercise page.

## Requirements

R1. Exercise pages updated under this spec MUST include a page-local section
headed exactly `## How much to do`.

R2. The `## How much to do` section MUST include a visible `Method type:` line
using one active method type value from this spec.

R3. The active method type values MUST be exactly:
`dynamic_resistance`, `bodyweight_progression`, `low_load_control_drill`,
`isometric_hold`, `mobility_drill`, and `stretch_hold`.

R4. The first version MUST NOT require hidden metadata, YAML front matter, a
shared taxonomy file, or generated data as the source of truth for method type.

R5. If hidden metadata is added later, the visible `Method type:` line MUST
remain present and MUST remain authoritative unless a later approved spec
supersedes this source-of-truth rule.

R6. The `## How much to do` section MUST include these visible labels or
equivalent plain-language lines: `Beginner starting point:`, `Effort:`,
`Rest:`, `Progression:`, and `Stop if:`.

R7. Method guidance MUST be framed as static general education for healthy adult
beginners or returning beginners, not as a personal instruction to follow.

R8. Method guidance MUST NOT adapt sets, reps, hold time, rest, load, exercise
choice, or progression based on reader symptoms, goals, equipment, medical
history, body measurements, or training response.

R9. Method guidance MUST NOT diagnose pain, treat pain, prescribe
rehabilitation, promise posture correction, provide return-to-training
guidance, or guarantee a fix.

R10. Method guidance MUST use concise stop language and route broader safety
concerns to `RED-FLAGS.md` when the page mentions pain, symptoms, or
professional care.

R11. Amount, effort, rest, progression, and safety claims in method guidance
MUST have page-local source support when they make a concrete claim beyond
generic wording.

R12. A page-local source is sufficient for method guidance only when the source
appears in the exercise page's `Sources` section and supports the cited claim
at the level being made.

R13. Global-only source indexing in `SOURCES.md` MUST NOT be the only support
for a method guidance safety claim.

R14. The `dynamic_resistance` starter-range shape MUST use sets, repetitions,
controlled form, rest, and progression by repetitions before small load
increases.

R15. The editorial default for `dynamic_resistance` SHOULD be 1-3 sets of
8-15 repetitions, 60-120 seconds of rest, and progression by adding repetitions
before a small load increase.

R16. The `bodyweight_progression` starter-range shape MUST use sets with
repetitions or time, variation selection, form-quality stopping, and progression
by harder variation before extra volume.

R17. The editorial default for `bodyweight_progression` SHOULD be 1-3 sets of
5-12 repetitions or 10-30 seconds.

R18. The `low_load_control_drill` starter-range shape MUST use short practice
sets with slow repetitions or brief holds, low effort, rest as needed, and
progression by smoother control instead of fatigue.

R19. The editorial default for `low_load_control_drill` SHOULD be 1-2 short
practice sets of 5-10 slow repetitions or 5-10 second holds.

R20. The `isometric_hold` starter-range shape MUST use hold count, hold
duration, breathing, rest, and a stop condition for loss of bracing, posture, or
breathing.

R21. The editorial default for `isometric_hold` SHOULD be 2-3 holds of
10-30 seconds with 30-90 seconds of rest.

R22. The `mobility_drill` starter-range shape MUST use slow repetitions or
brief comfortable holds, easy range, and no forced end range.

R23. The editorial default for `mobility_drill` SHOULD be 1-2 rounds of 5-10
slow repetitions or brief comfortable holds.

R24. The `stretch_hold` starter-range shape MUST use hold duration, rounds,
relaxed effort, no bouncing, and stop-or-back-off language for pain.

R25. The editorial default for `stretch_hold` SHOULD be 1-3 rounds of
10-30 seconds or about 30 seconds.

R26. The first implementation slice MUST NOT use `loaded_carry` or
`basic_cardio_equipment` as active method types.

R27. `loaded_carry` and `basic_cardio_equipment` MAY be introduced only by a
later approved spec or spec amendment after carry or cardio-equipment pages are
in scope.

R28. The first proof slice MUST include these six exercise pages:
`exercises/chest-press.md`, `exercises/incline-push-up.md`,
`exercises/chin-nod.md`, `exercises/plank.md`,
`exercises/thoracic-extension.md`, and
`exercises/kneeling-hip-flexor-stretch.md`.

R29. The first proof slice MUST map the six proof pages to these method types:
`chest-press.md` to `dynamic_resistance`, `incline-push-up.md` to
`bodyweight_progression`, `chin-nod.md` to `low_load_control_drill`,
`plank.md` to `isometric_hold`, `thoracic-extension.md` to
`mobility_drill`, and `kneeling-hip-flexor-stretch.md` to `stretch_hold`.

R30. The first implementation slice MUST create or update
`principles/sets-reps-holds-rest-and-progression.md`.

R31. `principles/sets-reps-holds-rest-and-progression.md` MUST explain sets,
repetitions, timed holds, easy/moderate/hard effort, rest, one-variable-at-a-time
progression, and why starter ranges are educational examples rather than
personal prescriptions.

R32. Exercise pages updated under this spec SHOULD link to
`principles/sets-reps-holds-rest-and-progression.md` when they use terms such as
sets, repetitions, holds, effort, rest, or progression that a beginner may need
explained.

R33. Pattern-page exercise previews that include starter ranges SHOULD align
with the linked exercise page's method type and range shape.

R34. A pattern-page exercise preview MUST NOT contradict the linked exercise
page's method guidance when both pages are in the same promoted slice.

R35. If a pattern-page exercise preview links to an exercise page that has not
yet adopted this spec, the pattern page MUST either remain draft-only or avoid
presenting the preview as complete full exercise instructions.

R36. The exercise template at `docs/templates/exercise-card.md` MUST be updated
with the `## How much to do` section before broad exercise-page rollout.

R37. Validation SHOULD check for the `## How much to do` section, active method
type values, required visible labels, forbidden personalized-programming
phrases, and pattern-preview alignment where practical.

R38. Validation SHOULD fail with file path and stable finding category when an
exercise page omits a required method section, uses an inactive method type,
uses hidden-only method metadata, or contains forbidden personalized programming
language.

R39. Manual source audit MUST sample at least one page from each active method
type before broad rollout.

R40. Beginner comprehension evidence MUST confirm that a reader can explain the
exercise's beginner starting point, effort, stop condition, and that the page is
not a personal program.

R41. This spec MUST NOT require the original Markdown-first v0.1 five-page
slice to adopt exercise method guidance retroactively before v0.1 closeout,
unless those pages are included in a later implementation slice under this
spec.

R42. Compatibility notes SHOULD be added to `specs/markdown-first-primer.md` and
`specs/responsible-breadth.md` only where needed to point to this focused spec
as the normative home for method guidance.

## Inputs and outputs

Inputs:

- Exercise Markdown pages under `exercises/`.
- Pattern Markdown pages that include exercise previews.
- Principle Markdown page
  `principles/sets-reps-holds-rest-and-progression.md`.
- Page-local source lists and the global `SOURCES.md` index.
- Optional validation commands that parse Markdown content.

Outputs:

- Exercise pages with `## How much to do` method guidance.
- A visible `Method type:` line using an active method type value.
- Source-supported beginner starting point, effort, rest, progression, and stop
  guidance.
- Pattern-page previews that do not contradict linked exercise-page method
  guidance.
- Validation output that identifies missing or invalid method guidance with file
  path and stable finding category when automated checks are implemented.
- Manual source-audit and beginner-comprehension evidence for requirements that
  cannot be fully automated.

No runtime API, database record, user profile, hidden metadata contract, hosted
service, or generated public data package is introduced by this spec.

## State and invariants

- Markdown remains the source of truth for exercise method guidance.
- The visible `Method type:` line remains authoritative in the first version.
- Method guidance remains static education, not personalized programming.
- The six active method type values remain the only active values until a later
  approved spec or amendment expands them.
- Editorial starter ranges are defaults, not mandatory exact prescriptions for
  every page.
- Page-level method wording may narrow or vary an editorial default only when
  source support and non-prescriptive wording are preserved.
- Exercise pages keep their existing purpose, setup, muscles, movement,
  feel-cue, mistake, easier/harder version, safety, and source obligations.
- Pattern-page previews remain compact previews; full exercise instructions
  remain in the linked exercise page.

## Error and boundary behavior

- An exercise page updated under this spec but missing `## How much to do`
  fails the method contract.
- A method section with no visible `Method type:` line fails the method
  contract.
- A method type outside the active enum fails unless a later approved spec or
  amendment expands the enum.
- Hidden-only method metadata fails the first-version contract.
- A method section that adapts to reader symptoms, goals, equipment, medical
  history, body measurements, or training response fails the scope boundary.
- A method section that diagnoses, treats, prescribes rehabilitation, promises
  posture correction, gives return-to-training guidance, or guarantees a fix
  fails the safety boundary.
- A concrete safety or progression claim without page-local source support fails
  source review.
- A pattern-page preview that contradicts a linked exercise page's method
  guidance fails preview alignment when both pages are in the same promoted
  slice.
- Existing exercise pages not yet updated under this spec may remain valid under
  their prior governing contract until they are brought into an implementation
  slice for this spec.

## Compatibility and migration

This spec is additive for exercise pages. It does not remove the existing
Markdown-first exercise-page sections or Responsible Breadth pattern-page
requirements.

Migration should be staged:

1. Approve this spec after spec review.
2. Update compatibility notes in related specs only where needed.
3. Update `docs/templates/exercise-card.md`.
4. Add or update `principles/sets-reps-holds-rest-and-progression.md`.
5. Update the six proof-slice exercise pages.
6. Add or update validation checks and manual proof records.
7. Expand remaining exercise pages in later reviewed slices.

Rollback is Markdown-only. If method guidance proves too prescriptive or
under-sourced, remove or narrow `## How much to do` from affected pages and keep
the existing exercise-page contract. If an active method type proves ambiguous,
pause broad rollout and revise this spec before adding more pages.

## Observability

Automated validation should report:

- Missing `## How much to do`.
- Missing or inactive `Method type:`.
- Missing visible method labels.
- Hidden-only method metadata.
- Forbidden personalized-programming or treatment language.
- Pattern-preview links whose full exercise page is missing or contradictory.
- Source-section gaps where detectable.

Manual validation should record:

- Source-audit samples for at least one page per active method type.
- Beginner-comprehension outcomes for the six-page proof slice.
- Any residual risk when automated checks cannot prove semantic source support,
  non-prescriptive tone, or beginner comprehension.

Validation reports must not claim CI passed unless a CI run was actually
observed.

## Security and privacy

This spec introduces no user input, accounts, analytics, private health data,
or runtime storage.

Content and validation artifacts must not include private health information,
private reviewer data, secrets, credentials, private machine paths, or
identifiable reader-test details.

Method guidance must not invite readers to submit symptoms, injuries, goals,
medical history, body measurements, or training logs.

## Accessibility and UX

The method section must be readable as plain Markdown without a renderer beyond
standard GitHub-style Markdown. The section heading and visible labels must make
the guidance easy to scan.

Exercise pages should use plain language for method guidance and should avoid
jargon without a nearby explanation or a link to the supporting principle page.

The method section must not rely on images, color, icons, tables, scripts, or
interactive controls to communicate the starting point, effort, rest,
progression, or stop condition.

## Performance expectations

No runtime performance requirements apply. Validation should remain suitable for
local repository checks and should report deterministic file-level failures when
checks are automated.

## Edge cases

EC1. An exercise reasonably fits two method types. The page must choose one
primary visible `Method type:` for the first version and may explain the
secondary context in plain language if it remains source-supported and
non-prescriptive.

EC2. A page uses an editorial starter range exactly but has no page-local source
support for concrete amount, effort, progression, or safety claims. The page
fails source review.

EC3. A page says "Do 3 sets of 12 every Monday, Wednesday, and Friday." The page
fails because it reads like a personal routine rather than page-local exercise
education.

EC4. A page says "If your shoulder hurts, switch to this exercise for 2 weeks."
The page fails because it adapts to symptoms and gives injury-related guidance.

EC5. A page says "Use whatever sets and reps your body needs" without a starter
range. The page fails because it does not answer the beginner method question.

EC6. A method section says `Method type: loaded_carry` in the first slice. The
page fails because `loaded_carry` is deferred.

EC7. A pattern page gives a plank preview of "3 sets of 12 reps" while
`exercises/plank.md` uses `isometric_hold`. The promoted slice fails alignment
review.

EC8. A page has YAML front matter with a valid method type but no visible
`Method type:` line. The page fails because hidden-only metadata is not the
source of truth.

EC9. A stretch page uses a 30-second hold and cites a source that supports
gentle stretching and hold duration. The page may pass if it also preserves
non-prescriptive wording and safety routing.

EC10. A current exercise page has not yet been selected for an implementation
slice under this spec. The page may remain valid under the previous exercise
contract until selected.

## Non-goals

- No personalized workout plans, generated plans, adaptive programming, or
  training calculators.
- No diagnosis, treatment, rehabilitation protocol, posture-correction routine,
  return-to-training prescription, or injury-specific substitution.
- No user intake, account system, training log, symptom checker, API, database,
  or hosted application.
- No hidden metadata or generated data source of truth for method type in the
  first version.
- No broad rewrite of every exercise page in the first implementation slice.
- No activation of `loaded_carry` or `basic_cardio_equipment` method types in
  the first slice.
- No advanced athlete, sport-specific, powerlifting, Olympic lifting,
  kettlebell ballistic, plyometric, sprint, or competition programming content.

## Acceptance criteria

AC1. The spec review confirms that `## How much to do`, visible `Method type:`,
active method type enum, starter-range shapes, source rules, and safety
boundaries are clear enough for implementation planning.

AC2. The proposal status has been normalized to `accepted` based on recorded
approval before this spec is relied on.

AC3. `docs/templates/exercise-card.md` can be updated from this spec without
needing a new product decision.

AC4. The six proof-slice exercise pages can each be assigned exactly one active
method type from this spec.

AC5. `principles/sets-reps-holds-rest-and-progression.md` has a defined
contract for the first implementation slice.

AC6. Automated validation can be planned for section presence, method type enum,
required labels, hidden-only metadata rejection, and forbidden personalization
language.

AC7. Manual validation can be planned for source-audit sampling and beginner
comprehension evidence.

AC8. Pattern-page preview alignment can be tested or manually audited without
changing the pattern-page architecture.

AC9. No requirement in this spec requires a hosted app, database, user input,
account, generated public data package, or hidden metadata source of truth.

AC10. No requirement in this spec authorizes diagnosis, treatment,
rehabilitation, posture-correction promises, individualized programming, or
advanced performance programming.

## Open questions

None for spec-review. Future spec amendments may add `loaded_carry`,
`basic_cardio_equipment`, machine-readable metadata, or additional proof-slice
requirements after those topics are in scope.

## Next artifacts

- Execution plan for template, principle page, validation, six proof-slice
  exercise updates, manual source audit, and beginner comprehension proof.
- Test specification mapping requirements to automated checks and manual proof
  records after plan review and before implementation.

## Follow-on artifacts

- Architecture package: `docs/architecture/system/architecture.md`

## Readiness

Approved and handed off to planning after clean architecture review.
