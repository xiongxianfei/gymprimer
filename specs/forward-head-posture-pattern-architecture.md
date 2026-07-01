# Forward Head Posture Pattern Architecture

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-06-30-forward-head-posture-pattern-architecture.md`
- Proposal review:
  `docs/changes/forward-head-posture-pattern-architecture/reviews/proposal-review-r2.md`
- Governing specs:
  - `specs/markdown-first-primer.md`
  - `specs/responsible-breadth.md`
- Related templates:
  - `docs/templates/pattern-page.md`
  - `docs/templates/exercise-card.md`

## Goal and context

This spec defines the observable contract for the forward-head-posture proof
slice and the reusable pattern architecture it exercises.

The slice adds one pattern page, five same-slice exercise pages, one optional
pattern comparison image, provenance for any generated raster media, and
validation coverage for required links, source support, media existence, and
forbidden claims. The content remains static Markdown. It must not become a
diagnosis, posture-correction protocol, rehabilitation pathway, treatment plan,
personalized workout plan, or source-of-truth AI guidance.

The proof slice exists to make future pattern pages repeatable: a beginner
arrives with an observation, the page names the observable pattern, routes red
flags first, explains likely contributors and uncertainty, maps a bounded
exercise menu to the contributors, and links to exercise pages that carry full
exercise instruction.

## Glossary

- Forward head posture: an observable head, neck, upper-back, and rib-cage
  relationship where the head appears forward relative to the torso. It is not
  a diagnosis in GymPrimer.
- Pattern page: a non-diagnostic Markdown page under `patterns/` that explains
  an observable movement or posture pattern.
- Complete loop: the pattern-page chain from reader observation, to likely
  contributor, to exercise option, to muscles used, to cue or caveat, to a
  linked exercise page.
- Detailed exercise option: one of the five selected exercises that must have
  a linked same-slice exercise page and a pattern-page annotation.
- Broader collected exercise list: secondary examples named in the pattern
  page without detailed complete-loop treatment.
- Pattern comparison image: one generated raster support image that compares
  neutral side-view posture with forward-head side-view posture and contains no
  in-image text.
- Page-local source support: source links and source definitions on the page
  that support that page's claims without relying only on `SOURCES.md`.

## Examples first

Example E1: valid pattern page links a same-slice detailed exercise
Given `patterns/forward-head-posture.md` exists
When it lists chin nod as a detailed exercise option
Then the option links to `../exercises/chin-nod.md`
And the option includes a fix reason, used muscles, and important note
And `exercises/chin-nod.md` exists.

Example E2: valid pattern image is support only
Given `patterns/forward-head-posture.md` references one raster image
When the image is checked
Then the image path exists under `media/patterns/forward-head-posture/`
And `media/PROVENANCE.md` contains a matching approved row
And the image has no in-image text
And the Markdown text and citations remain the source of truth.

Example E3: invalid missing exercise page
Given `patterns/forward-head-posture.md` links to
`../exercises/wall-slide.md`
When `exercises/wall-slide.md` is absent
Then the slice fails validation and the pattern page remains unpromoted.

Example E4: invalid corrective routine
Given `patterns/forward-head-posture.md` says "do these five exercises every
day to fix your posture"
When scope guardrails run
Then the page fails because it prescribes a corrective routine and promises
posture correction.

Example E5: valid README behavior
Given `patterns/forward-head-posture.md` passes local validation
When only this one pattern page is complete
Then `README.md` still does not promote it as active pattern-set content.

## Requirements

R1. The slice MUST create or update `patterns/forward-head-posture.md` as a
Markdown pattern page titled "Forward Head Posture".

R2. The pattern page MUST follow the pattern-page architecture from
`docs/templates/pattern-page.md`: what the page is, what it is not, red flags,
why beginners come to the page, working definition, how to notice the pattern,
core reason, uncertainty, what commonly helps, what to avoid, professional
routing, next links, sources, and author/review date.

R3. Red-flag routing MUST appear before exercise options or self-management
themes and MUST link to `../RED-FLAGS.md`.

R4. The pattern page MUST state that it does not diagnose the reader, prove a
posture is harmful, provide individualized care, promise correction, or explain
all pain.

R5. The pattern page MUST define forward head posture as an observable pattern
of head, neck, upper-back, and rib-cage position, not as a medical condition.

R6. The pattern page MUST include three to five beginner observations or search
phrases that bring readers to the page.

R7. The pattern page MUST include two to four self-observation methods and
label them as observation, not diagnosis.

R8. The core-reason section MUST cover likely contributors using plain movement
language, including daily-position load, head-and-neck control, thoracic
position or extension options, scapular support, posterior upper-back strength,
and anterior neck or chest stiffness or tone.

R9. Each contributor claim in the core-reason section MUST have page-local
source support or be removed.

R10. The pattern page MUST include an uncertainty section that avoids claiming
individual posture correction, individual pain relief, or a single proven cause
for a reader's posture.

R11. The pattern page MUST use this four-claim-family source set for pattern
claims: neck red flags and professional routing, posture-pattern evidence and
uncertainty, shoulder/scapular and rotator-cuff context, and general
resistance-training framing.

R12. The pattern page MUST include the following detailed exercise options:
chin nod or deep-neck-flexor awareness, thoracic extension, wall slide, prone
Y/T, and band pull-apart.

R13. Each detailed exercise option MUST include a pattern-specific fix reason,
used muscles, and one important cue or caveat.

R14. Each detailed exercise option MUST link to the matching same-slice
exercise page:
`../exercises/chin-nod.md`,
`../exercises/thoracic-extension.md`,
`../exercises/wall-slide.md`,
`../exercises/prone-y-t.md`, or
`../exercises/band-pull-apart.md`.

R15. The slice MUST create the same-slice exercise pages
`exercises/chin-nod.md`, `exercises/thoracic-extension.md`,
`exercises/wall-slide.md`, `exercises/prone-y-t.md`, and
`exercises/band-pull-apart.md`.

R16. Each same-slice exercise page MUST follow the exercise-page contract from
`docs/templates/exercise-card.md`: purpose, setup, muscles involved, movement
breakdown, feel cues, common mistakes, easier version, harder version, safety
notes, sources, and safety routing to `../RED-FLAGS.md` when the page mentions
pain, symptoms, or professional care.

R17. Exercise setup, technique, muscle, feel-cue, common-mistake, and safety
claims on the five same-slice exercise pages MUST have page-local source
support independent of the pattern page's four-source set.

R18. The pattern page MAY list a broader collected exercise set, such as seated
row, lat pulldown, plank, dead bug, and other low-risk pulling or trunk-control
examples, only as clearly secondary options without detailed complete-loop
treatment unless those exercises also have linked pages and full annotations.

R19. The pattern page MUST NOT present the detailed exercise options as a
sequence, frequency, daily routine, prescription, treatment plan, or guaranteed
fix.

R20. The pattern page MUST include no more than one pattern comparison image.

R21. If a pattern comparison image is used, the image MUST live under
`media/patterns/forward-head-posture/`, have a matching approved
`media/PROVENANCE.md` row, use the permitted pattern media purpose, and be
referenced by the pattern page.

R22. The pattern comparison image MUST have no in-image text, no exercise
thumbnails, no red injury marks, no diagnostic pain symbols, and no before/after
cure implication.

R23. Image labels, anatomical explanations, safety claims, and exercise
instructions MUST remain in Markdown text with citations, not inside the image.

R24. The slice MUST automatically check detailed exercise-link existence from
the pattern page to the five same-slice exercise pages.

R25. The slice MUST automatically check existence of any referenced pattern
image asset.

R26. The slice MUST validate page-local source sections, source-index reuse
where applicable, media provenance, privacy, and forbidden diagnostic,
treatment, rehab, posture-correction, and personalized-programming language.

R27. `README.md` MUST NOT promote `patterns/forward-head-posture.md` as active
pattern-set content until the full approved pattern set passes downstream
review and verification.

R28. The slice MUST NOT add a new page class, runtime application, database,
generated output path, CI workflow, hosted app, CMS, symptom checker, decision
tree, or user-input flow.

R29. The spec, architecture, and template artifacts MUST preserve separate
responsibilities: the spec owns normative behavior, architecture locates the
pattern-page system boundary, and templates provide authoring prompts.

R30. The final implementation MUST report exact local validation commands and
MUST NOT claim hosted CI passed unless a CI run was observed.

R31. The same-slice exercise pages SHOULD avoid optional exercise images unless
the image is needed for beginner comprehension and can satisfy the existing
media/provenance contract.

R32. If the existing checker cannot express a required deterministic constraint,
the change MUST add a focused assertion or checker behavior before claiming the
constraint is covered.

## Inputs and outputs

Inputs:

- `docs/proposals/2026-06-30-forward-head-posture-pattern-architecture.md`
- `docs/templates/pattern-page.md`
- `docs/templates/exercise-card.md`
- `specs/markdown-first-primer.md`
- `specs/responsible-breadth.md`
- `SOURCES.md`
- `RED-FLAGS.md`
- Existing exercise pages and media/provenance conventions.

Outputs:

- `patterns/forward-head-posture.md`
- `exercises/chin-nod.md`
- `exercises/thoracic-extension.md`
- `exercises/wall-slide.md`
- `exercises/prone-y-t.md`
- `exercises/band-pull-apart.md`
- Optional image under `media/patterns/forward-head-posture/`
- Matching `media/PROVENANCE.md` row when a generated raster image is used
- Source additions to `SOURCES.md` only when sources are reused across pages
- Focused validation updates or tests.

## State and invariants

- Markdown remains the canonical source of truth.
- `patterns/forward-head-posture.md` remains draft/unpromoted until this slice
  passes review and verification.
- The five same-slice exercise pages are content dependencies of the pattern
  proof slice.
- Red flags always appear before exercise options.
- Exercise pages carry full exercise instruction; pattern-page exercise
  annotations are previews, not replacements for exercise pages.
- Media is optional support and cannot become the source of truth.
- Page-local citations are required for safety and technique claims.
- README promotion waits for the approved pattern set, not the single page.

## Error and boundary behavior

- If any of the five same-slice exercise pages is missing, validation fails.
- If a detailed exercise link points to a missing or wrong path, validation
  fails.
- If the pattern image path is missing, validation fails.
- If a generated raster image lacks approved provenance, validation fails.
- If the pattern image contains in-image text or exercise thumbnails, the page
  fails the first-slice image constraint.
- If the pattern page promises correction, diagnoses the reader, or prescribes a
  routine, validation fails.
- If an exercise page gives injury-specific rehab, pain treatment, or
  individualized programming advice, validation fails.
- If a source supports only the pattern page but is used to justify exercise
  technique or safety, the exercise claim fails source-support review.
- If a broader collected exercise item is presented like a detailed option
  without a linked page and annotation, the page fails the complete-loop rule.

## Compatibility and migration

This spec adds a focused proof slice under existing content paths. It does not
move existing pages or change public routing.

Existing pages under `patterns/`, `exercises/`, `conditions/`, `principles/`,
and `programs/` continue to follow their current governing specs. Existing
pattern-page requirements in `specs/responsible-breadth.md` remain active. This
spec narrows the contract for the forward-head-posture proof slice and should
be folded into broader Responsible Breadth pattern rules only after review.

Rollback is content removal from active navigation and deletion or draft marking
of the new pattern page, five exercise pages, optional media asset, provenance
row, and focused tests. Historical proposal, spec, and review artifacts remain
under `docs/`.

## Observability

Validation output SHOULD identify:

- missing required pattern sections;
- missing exercise-page sections;
- missing or broken detailed exercise links;
- missing image asset paths;
- missing or mismatched media provenance rows;
- missing page-local source sections;
- forbidden diagnostic, treatment, rehab, posture-correction, routine, or
  personalized-programming language;
- privacy findings by file path; and
- exact local commands run.

The final verification record MUST state whether hosted CI was observed.

## Security and privacy

The slice MUST NOT include secrets, credentials, private contact details, local
private machine paths, private reviewer details, sensitive health information,
or real user health profiles.

Reader examples MUST be generic and non-identifying. The pages MUST NOT ask the
reader to provide symptoms, medical history, goals, equipment constraints, age,
pregnancy status, injury status, or training response to choose content.

AI-generated images MAY be used only as reviewed support media with provenance.
AI-generated exercise guidance MUST NOT become source-of-truth content.

## Accessibility and UX

The pattern page and exercise pages MUST be readable as plain Markdown without
JavaScript, generated HTML, a local server, an account, or a database.

The pattern image, if present, MUST have meaningful alt text and adjacent
Markdown explanation. The image MUST NOT rely on embedded text to communicate
the concept. Links to red flags, exercise pages, source definitions, and next
steps MUST be repository-relative Markdown links.

The exercise menu MUST be scannable as an educational menu and not formatted as
a timed routine, checklist prescription, or program.

## Performance expectations

Local validation for this slice SHOULD remain lightweight enough to run with
the existing Python `unittest` and checker workflow. The implementation MUST
report command durations when practical if adding new checker behavior makes
validation materially slower.

No runtime performance contract applies because the product surface is static
Markdown.

## Edge cases

EC1. The pattern page says "you have forward head posture": fails because the
page diagnoses the reader.

EC2. The pattern page says the five exercises will fix posture: fails because
it promises correction.

EC3. The pattern page lists wall slide as a detailed option but does not link
`../exercises/wall-slide.md`: fails the complete-loop rule.

EC4. `exercises/prone-y-t.md` exists but has no sources section: fails the
exercise-page source contract.

EC5. `exercises/chin-nod.md` describes neck-pain treatment progression: fails
the no-treatment and no-rehab boundary.

EC6. The pattern page uses two comparison images: fails the one-image first
slice constraint.

EC7. The image path exists but the provenance row references a different
`page_refs` value: fails media provenance.

EC8. The image shows red pain marks or "bad posture" text: fails image safety
and no in-image text constraints.

EC9. The pattern page links README promotion before the full pattern set is
approved: fails promotion boundary.

EC10. A broader collected exercise is listed without link or annotation but is
clearly labeled secondary: passes if it is not presented as a detailed option.

## Non-goals

- No diagnosis of neck pain, shoulder pain, nerve symptoms, headache, disc
  issues, thoracic outlet syndrome, or any medical condition.
- No individualized treatment plan, rehab protocol, return-to-training
  prescription, posture-correction routine, or promise to fix posture.
- No symptom checker, decision tree, user-input intake, personalization,
  adaptive programming, or workout planner.
- No immediate implementation of rounded shoulders or other pattern pages.
- No README promotion of this page alone.
- No new page class, repository layout, generated-output path, CI workflow,
  runtime app, hosted site, database, CMS, or media policy beyond the focused
  proof-slice constraints.
- No exercise thumbnails on the pattern page in the first slice.

## Acceptance criteria

AC1. Proposal status is accepted based on
`docs/changes/forward-head-posture-pattern-architecture/reviews/proposal-review-r2.md`.

AC2. `patterns/forward-head-posture.md` exists and contains all required
pattern-page sections.

AC3. The pattern page title is exactly "Forward Head Posture".

AC4. Red flags appear before exercise options and link to `../RED-FLAGS.md`.

AC5. The pattern page contains the four required source-claim families.

AC6. The pattern page contains detailed annotations for chin nod, thoracic
extension, wall slide, prone Y/T, and band pull-apart.

AC7. Each detailed annotation includes fix reason, used muscles, important note,
and a valid link to the matching same-slice exercise page.

AC8. All five same-slice exercise pages exist and satisfy the exercise-page
contract.

AC9. Exercise-instruction, muscle, technique, and safety claims on same-slice
exercise pages have page-local source support.

AC10. The broader collected exercise list, if present, is visually and
semantically secondary to the five detailed options.

AC11. The pattern page references no more than one pattern comparison image.

AC12. Any referenced pattern comparison image exists, has alt text, has no
in-image text, uses a permitted pattern media purpose, and has approved
provenance.

AC13. Validation fails if any detailed exercise link or referenced image path is
missing.

AC14. Validation fails on diagnostic, treatment, rehab, posture-correction,
routine-prescription, or personalized-programming language.

AC15. Privacy checks pass over the pattern page, exercise pages, media
provenance row, and change-local artifacts.

AC16. README does not promote the forward-head-posture page alone.

AC17. Exact local validation commands are recorded before implementation
completion is claimed.

## Open questions

None for spec review. Source selection for the five exercise pages remains a
test-spec and implementation responsibility, but the source-support obligation
is defined here.

## Next artifacts

- Execution plan and plan review for the forward-head-posture pattern
  architecture.
- Test spec or proof-map update for pattern sections, exercise-page contract,
  link existence, image existence, source-set coverage, media provenance, and
  forbidden language after plan review.

## Follow-on artifacts

- Architecture review:
  `docs/changes/forward-head-posture-pattern-architecture/reviews/architecture-review-r1.md`
- 2026-06-30 central-disclaimer amendment: per-page exercise disclaimers were
  removed from this proof-slice contract after owner clarification that
  `RED-FLAGS.md` owns the central disclaimer.

## Readiness

Ready for spec-review of the central-disclaimer amendment. The prior approved
plan and implementation evidence must not rely on this amendment until
spec-review closes.
