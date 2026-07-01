# Best-Practice Pattern Architecture and Forward Head Posture Proof Slice

## Status

accepted

## Problem

GymPrimer currently has one fully developed pattern page,
`patterns/anterior-pelvic-tilt.md`, and an active pattern template. That is
enough to prove one page, but not enough to make future pattern pages reliably
hit the same quality bar. The repository needs a durable best-practice pattern
architecture that future patterns can inherit: observable pattern first,
plain-language mechanism second, exercise options third, and no diagnosis or
correction promise.

Forward head posture is a common beginner search topic. Beginners notice their
head drifting forward during desk work, phone use, planks, rows, pulldowns, or
presses, or they hear a coach or video describe their neck position as "forward."
Most available fitness content jumps too quickly to "fix your posture" routines
or alarmist body-is-broken language. GymPrimer needs a page that explains the
visible pattern, why it may happen in general, and what movement options can
help the reader build better choices without implying diagnosis, treatment, or
guaranteed posture correction. This proposal therefore has two linked decisions:
standardize the pattern-page architecture, then use forward head posture as the
first proof slice for that architecture.

## Goals

- Define a durable best-practice pattern architecture for future GymPrimer
  pattern pages.
- Integrate that architecture into the appropriate downstream source-of-truth
  artifacts so future patterns maintain the same quality level.
- Use one next pattern page, `patterns/forward-head-posture.md`, as the proof
  slice for the architecture.
- Preserve the established pattern architecture from
  `docs/templates/pattern-page.md` and the APT page: red flags before
  self-management, neutral working definition, core contributors, uncertainty,
  exercise mapping, and professional-routing guidance.
- Make the pattern reason clear by explaining likely contributors in plain
  movement language: head-and-neck position, upper-cervical and lower-cervical
  control, thoracic position, scapular support, posterior upper-back strength,
  anterior neck/chest stiffness or tone, and daily-position load.
- Make the "what commonly helps" section concrete by mapping each linked
  exercise to a fix reason, primary and secondary muscles, and one important
  cue or caveat.
- Make the pattern architecture a complete loop: observed pattern -> likely
  contributors -> corresponding exercises -> muscles used -> important cue or
  caveat -> linked exercise page or same-slice exercise page.
- Use a high-quality generated raster illustration, after later review, to show
  neutral head/neck alignment versus forward head posture and the general
  movement-option map.
- Keep the page non-diagnostic, non-clinical, and non-prescriptive.

## Non-goals

- No diagnosis of neck pain, shoulder pain, nerve symptoms, headache, disc
  issues, thoracic outlet syndrome, or any medical condition.
- No individualized treatment plan, rehab protocol, posture-correction routine,
  or promise to fix posture.
- No symptom checker, decision tree, return-to-training prescription, or
  adaptive program.
- No immediate implementation of multiple pattern pages.
- No new page class, repository layout, generated-output path, CI workflow, or
  media policy beyond clarifying the existing pattern architecture.
- No final content implementation or approved media asset in this proposal.

## Vision fit

fits the current vision

The proposal fits the current GymPrimer vision because it is static,
citation-backed beginner education about an observable pattern. It stays within
the Markdown-first product model, uses red-flag routing, explains uncertainty,
and avoids diagnosis, personalized care, posture-correction promises,
rehabilitation pathways, or workout planning.

## Context

`docs/templates/pattern-page.md` already defines the active pattern-page shape.
It requires a page to explain what it is and is not, place red flags before
self-management themes, define the observable pattern, describe how to notice it
without diagnosing it, explain likely contributors, name uncertainty, map
exercise options to mechanisms, and route readers to professionals when needed.
That template is a strong start, but it is not yet enough architecture by
itself: future pattern pages also need a durable quality model that says why
each section exists, how contributors map to exercise options, how visuals are
allowed to support explanation, and which checks or review criteria keep the
page from drifting into posture treatment.

`patterns/anterior-pelvic-tilt.md` is the current proof that this pattern
architecture can work. It uses a side-view comparison image, a neutral working
definition, a core-reason section, uncertainty discussion, and exercise
annotations that name fix reason, used muscles, and important notes.

`docs/project-map.md` records the current repository as a Markdown-first corpus
with active content directories, `RED-FLAGS.md`, `SOURCES.md`,
`media/PROVENANCE.md`, local checker scripts, and no hosted CI. It also records
that new material content should continue through proposal/spec workflow because
Markdown contracts, safety language, citations, and media policy are governed
surfaces.

A preview-only concept image was generated during proposal authoring with the
`imagegen` skill. That image is not a project asset yet. A later implementation
should generate or select the final asset, place it under
`media/patterns/forward-head-posture/`, add a matching
`media/PROVENANCE.md` row, and pass the media/provenance checks.

## Options Considered

### Option A: Create only a short posture-awareness page

This would explain the visible pattern and uncertainty, then stop before
exercise mapping.

Advantages: lowest risk and easiest to review.

Drawbacks: does not satisfy the user need to understand why the pattern happens
or how exercise options map to the pattern. It also fails to test the strongest
part of the pattern architecture: contributor-to-exercise mapping.

Disposition: rejected.

### Option B: Keep architecture implicit in the template and APT page

This would create the forward-head-posture page by copying the current template
and APT style, but would not update architecture or downstream specs to
make the quality model explicit for future patterns.

Advantages: fastest path to the next page; minimal artifact work.

Drawbacks: leaves future pattern quality dependent on informal imitation. It
does not answer the user's updated goal to define a best-practice pattern and
integrate it into architecture.

Disposition: rejected.

### Option C: Create a corrective routine page

This would frame the page around a fixed sequence such as stretch the chest,
strengthen the upper back, and do a daily routine.

Advantages: simple and familiar to fitness readers.

Drawbacks: conflicts with GymPrimer's refusal to provide treatment plans,
rehab-like protocols, or posture-correction promises. It risks making posture
look like a diagnosis and movement options look like a prescription.

Disposition: rejected.

### Option D: Define reusable pattern architecture and prove it with one page

This would make the pattern quality model explicit in downstream spec,
architecture, template, and validation surfaces, then prove it with the
forward-head-posture page. The page would explain the observable
pattern, likely contributors, uncertainty, red flags, general movement options,
linked exercises, used muscles, visual support, and professional routing.

Advantages: best fit for the current pattern architecture and updated user
request. It makes the reason and exercise mapping clear, preserves safety
boundaries, and gives future pattern pages a reusable standard.

Drawbacks: requires careful sourcing and review because neck-position claims can
drift into medical advice or posture-correction promises. It also touches more
downstream artifacts than a single-page-only proposal.

Disposition: recommended.

### Option E: Choose a different next pattern

Possible alternatives include rounded shoulders, knee valgus, foot pronation, or
excessive lumbar arching during planks.

Advantages: some alternatives may be more exercise-specific and less
pain-adjacent.

Drawbacks: forward head posture is the requested focus and stress-tests the
same pattern architecture that APT established while keeping rounded shoulders
available as a separate later pattern.

Disposition: not selected for this slice.

## Recommended Direction

Choose Option D: define a reusable best-practice pattern architecture and prove
it with one concrete page, `patterns/forward-head-posture.md`.

The best-practice architecture should make every future pattern page answer the
same reader journey:

1. What did the beginner notice?
2. What observable pattern does that describe?
3. What red flags make GymPrimer the wrong tool?
4. What are the likely movement contributors?
5. What is uncertain, overstated, or commonly misunderstood?
6. Which exercise options train the missing movement choices?
7. Which muscles and cues make each option relevant?
8. When should the reader use a clinician, physical therapist, or coach instead
   of a static page?

The downstream architecture integration should preserve the existing content
block under `patterns/`, but make pattern quality explicit as a reusable
contract. That contract should cover the page skeleton, contributor taxonomy,
exercise annotation format, visual role, source-quality expectations, red-flag
placement, and validation/proof obligations.

The reusable pattern architecture should live in three artifacts with separate
responsibilities:

| Artifact | Responsibility |
| --- | --- |
| `specs/responsible-breadth.md` | Normative page contract: required sections, forbidden claims, red-flag routing, source quality, and exercise annotation rules. |
| `docs/architecture/system/architecture.md` | System boundary: pattern pages as static Markdown source, with citations, media, provenance, and checkers as supporting contracts. |
| `docs/templates/pattern-page.md` | Authoring skeleton: headings and prompts contributors use to write the page. |

The spec should own policy, the architecture should place that policy inside
the system, and the template should make the policy usable. Normative policy
should not live only in the template.

The page should frame the pattern as an observable head, neck, upper-back, and
rib-cage position. It should avoid saying the reader "has" a condition or that
the posture is automatically harmful.

The core-reason section should organize likely contributors into clear movement
categories:

- **Daily-position load:** repeated desk, phone, driving, or screen positions can
  make a forward-head position familiar, but they are not proof of damage.
- **Head-and-neck control:** deep neck flexors, suboccipital region control, and
  cervical extensor endurance may matter for keeping the head from drifting
  forward during movement.
- **Thoracic position and extension options:** the upper back may have fewer
  comfortable options for extending or rotating, which can make the neck work
  harder during rows, presses, planks, and overhead movements.
- **Scapular support:** the shoulder blades and rib cage influence where the
  neck rests during pulling, pressing, and reaching, even when the main visible
  pattern is the head position.
- **Posterior upper-back strength:** middle and lower trapezius, rhomboids, rear
  deltoids, and cervical extensors may need more practice supporting a stable
  upper-back and neck relationship.
- **Anterior neck and chest stiffness or tone:** sternocleidomastoid,
  scalenes, pectoralis major, pectoralis minor, anterior deltoid, and nearby
  tissues may limit comfortable head, rib-cage, or shoulder positioning for
  some readers.

The exercise menu should be educational rather than prescriptive. The first
complete-loop implementation should give detailed pattern-page annotations for
the five most relevant options:

- **Chin-nod or deep-neck-flexor awareness drill**
  - Fix reason: provides a low-load motor-learning option for noticing head and
    upper-neck position.
  - Used muscles: deep neck flexors with light cervical extensor control.
  - Important note: this is an awareness option, not a neck-pain treatment.
- **Thoracic extension**
  - Fix reason: provides a low-load motor-learning option for upper-back motion
    that may reduce how much the neck compensates.
  - Used muscles: thoracic extensors, lower trapezius, serratus anterior, and
    rotator cuff depending on the variation.
  - Important note: this is an option, not proof that posture is broken.
- **Wall slide**
  - Fix reason: practices shoulder-blade motion and rib-cage control while the
    head and neck stay quiet.
  - Used muscles: serratus anterior, lower trapezius, rotator cuff, thoracic
    extensors, and trunk stabilizers.
  - Important note: use an easy range and avoid forcing the neck forward.
- **Prone Y/T**
  - Fix reason: practices upper-back support for head and neck position without
    turning the pattern page into a routine.
  - Used muscles: middle trapezius, lower trapezius, rhomboids, rear deltoids,
    and rotator cuff.
  - Important note: keep the neck quiet and choose an easy version first.
- **Band pull-apart**
  - Fix reason: practices simple upper-back and rear-shoulder work while the
    neck stays relaxed.
  - Used muscles: rear deltoids, rhomboids, middle trapezius, rotator cuff, and
    grip muscles.
  - Important note: keep the movement light enough that it does not become a
    shrug or chin poke.

The pattern page may also list the broader collected exercise set as options
without detailed exercise-page treatment, such as seated row, lat pulldown,
plank, dead bug, and other low-risk pulling or trunk-control examples. Those
broader items should remain clearly secondary until linked exercise pages and
same-slice annotations exist.

The complete-loop rule is that each detailed exercise option must either link an
existing exercise page or explicitly create that exercise page in the same
reviewed implementation slice. This prevents the pattern page from becoming a
disconnected list of concepts while still allowing a clearly secondary collected
exercise list.

The visual should be one reviewed generated raster comparison image only for
the first proof slice. It should have no in-image text and no exercise
thumbnails. It should show a neutral side-view head/neck comparison and a
forward-head side-view comparison, plus simple non-prescriptive visual cues for
neck control, upper-back support, rib-cage position, shoulder-blade region, and
front-neck/chest region. If the image indicates commonly noticed discomfort
areas, it should use neutral shaded regions rather than red injury marks or
diagnostic pain symbols. The page text should carry the labels and citations
because generated image text is unreliable and harder to validate.

The source set for the proof slice should support four distinct claim families:

| Source need | Recommended source | Proposal use |
| --- | --- | --- |
| Neck red flags and professional routing | NICE CKS non-specific neck pain guidance: `https://cks.nice.org.uk/topics/neck-pain-non-specific/` | Support red-flag routing and the boundary that serious symptoms belong outside GymPrimer. |
| Posture-pattern evidence and uncertainty | 2024 systematic review/meta-analysis on therapeutic exercise for forward head posture, rounded shoulders, and thoracic kyphosis: `https://pmc.ncbi.nlm.nih.gov/articles/PMC10832142/` | Support the evidence that exercise can change posture angles while avoiding individual correction or pain-relief promises. |
| Shoulder/scapular and rotator-cuff context | AAOS shoulder impingement / rotator-cuff tendinitis education: `https://orthoinfo.aaos.org/en/diseases--conditions/shoulder-impingementrotator-cuff-tendinitis/` | Support shoulder-blade and rotator-cuff context without copying clinical treatment plans into GymPrimer. |
| General resistance-training framing | ACSM 2026 resistance-training guidance: `https://acsm.org/resistance-training-guidelines-update-2026/` | Support presenting exercise options as general training choices built around consistency, not a corrective protocol. |

## Expected Behavior Changes

- The repository gains a reviewed proposal for a reusable pattern-page quality
  architecture and the next pattern proof slice.
- Downstream spec and architecture work has a clear standard for future pattern
  pages, not only one target page.
- Downstream spec work has a clear target page, scope boundary, visual direction,
  and mechanism-to-exercise structure to turn into testable requirements.
- No user-facing content changes yet, because this proposal does not add the
  final pattern page or media asset.

## Architecture Impact

Expected touched surfaces in downstream work:

- `specs/responsible-breadth.md` or a focused pattern-architecture spec
  amendment, to make the best-practice pattern contract explicit.
- `docs/architecture/system/architecture.md`, to record pattern pages as a
  reusable content architecture with contributor-to-exercise mapping and visual
  support rules.
- `docs/templates/pattern-page.md`, if the current template needs adjustment
  after the architecture contract is reviewed.
- `patterns/forward-head-posture.md`
- `exercises/chin-nod.md`
- `exercises/thoracic-extension.md`
- `exercises/wall-slide.md`
- `exercises/prone-y-t.md`
- `exercises/band-pull-apart.md`
- `media/patterns/forward-head-posture/`
- `media/PROVENANCE.md`
- `SOURCES.md`, only if source reuse crosses page boundaries
- `tests/test_responsible_breadth_m1.py` or a new focused pattern assertion if
  existing checks do not cover the new page's expected structure
- `tools/checks/check_markdown_first.py` only if existing pattern checks cannot
  express the required constraints
- lifecycle artifacts under `docs/changes/<change-id>/`

No new content class, runtime, database, generated output, public API, or
repository layout change is expected.

The five same-slice exercise pages must use the existing exercise-page contract
from `docs/templates/exercise-card.md`. Each page must include page-local
sources for exercise setup, technique, muscles involved, and safety claims.
The four-source pattern set supports the pattern page; it does not by itself
support exercise-instruction claims on the new exercise pages. Exercise-page
sources may be added to `SOURCES.md` when reused across pages, but every safety
or technique claim still needs page-local citation support.

## Testing and Verification Strategy

Downstream work should prove the page through targeted checks before broad
smoke:

- Architecture/spec checks confirm the pattern quality contract exists before
  page implementation relies on it.
- Template checks confirm future pattern pages inherit the required sequence:
  observation, red flags, definition, contributors, uncertainty, exercise
  mapping, visual support, and professional routing.
- Pattern-page structure and metadata match `docs/templates/pattern-page.md`.
- Red flags appear before exercise or self-management options and link to
  `../RED-FLAGS.md`.
- The page avoids forbidden diagnostic, treatment, posture-correction, and
  personalized-programming language.
- Every safety or pain-adjacent claim has page-local citation support.
- Exercise links are checked automatically and point only to existing pages or
  pages created in the same reviewed slice.
- Exercise annotations include fix reason, used muscles, and important note.
- The five same-slice exercise pages satisfy the exercise-page contract:
  purpose, setup, muscles involved, movement breakdown, feel cues, common
  mistakes, easier and harder versions, safety notes, and page-local sources.
- Exercise-instruction and safety claims on the five same-slice exercise pages
  have page-local source support independent of the pattern page's four-source
  posture evidence set.
- The complete-loop rule is checked: every pattern contributor that recommends
  exercise support maps to a corresponding exercise page or same-slice exercise
  page, and each mapped exercise names muscles and a cue/caveat.
- The generated image path is checked automatically for existence and has alt
  text, no in-image text, no diagnosis or cure implication, a matching
  `media/PROVENANCE.md` row, allowed media purpose, and page reference.
- Image validation checks the first-slice constraint: one comparison image, no
  exercise thumbnails, no in-image text, neutral visual cues, and no red injury
  marks or diagnostic pain symbols.
- Same-slice exercise-page validation includes page-contract tests, link
  checks from `patterns/forward-head-posture.md` to each new exercise page,
  privacy checks over all new pages, and media/provenance checks for any
  exercise images introduced by those pages.
- Local validation should include the Responsible Breadth tests,
  Markdown-first checker over active content/templates, privacy checker over
  touched artifacts, and `git diff --check`.

Do not require separate proof artifacts for this proposal's acceptance path. Use explicit
checks for required sections, exercise-link existence, image-asset existence,
no in-image text, source-set coverage, exercise-loop coverage, media provenance,
and forbidden-claim language. If a later review decides a human visual review
record is still needed for generated media, that should be introduced by the
media/spec stage, not assumed here.

## Rollout and Rollback

Rollout should be a small branch that first updates the reviewed pattern
architecture contract, then applies it to one pattern page with its directly
required media/provenance/test updates after proposal review, spec, architecture
assessment, plan, and test-spec review.

The page should not be linked from README as promoted content by itself. README
promotion should wait until the approved pattern set passes the reviewed
downstream gates. Rounded shoulders should remain a separate future pattern
that follows the same reviewed architecture after this proof slice settles. If
review finds the reusable architecture too heavy, rollback is to keep the
existing template-only pattern contract and omit the architecture amendment. If
review finds the topic too clinical or the exercise mapping too prescriptive,
rollback is straightforward: remove the new pattern page, media asset,
provenance row, and tests, leaving the proposal as historical evidence.

## Risks and Mitigations

- Risk: The page reads like diagnosis or posture treatment.
  Mitigation: Use observation language, uncertainty section, red flags, and
  explicit "not diagnosis, not correction promise" boundaries.
- Risk: The exercise menu becomes a routine.
  Mitigation: Present exercises as options mapped to movement contributors, not
  a sequence, frequency, or prescription.
- Risk: Muscle explanations become overconfident.
  Mitigation: Cite each contributor and use "may contribute" language where
  evidence is mixed.
- Risk: The generated image implies before/after cure.
  Mitigation: Use neutral comparison, no arrows, no cure symbols, no pain marks,
  no in-image text, one comparison image only, and provenance validation before
  use.
- Risk: Existing validation does not fully check exercise annotations, the
  complete-loop rule, image text absence, or the architecture-level pattern
  standard.
  Mitigation: Add focused assertions for the pattern page, source-set coverage,
  no in-image text, one comparison image, complete-loop exercise mapping, and
  architecture/template ownership.
- Risk: Existing workflow guide and constitution current-assumptions text are
  stale after PR #5.
  Mitigation: Treat those as orientation risks for workflow cleanup, but do not
  let them silently change this proposal's scope.

## Resolved Decisions

- Use the page title "Forward Head Posture".
- Generate detailed information for the five most relevant corresponding
  exercises: chin-nod or deep-neck-flexor awareness, thoracic extension,
  wall-slide, prone Y/T, and band pull-apart.
- List the broader collected exercise set in the pattern document, but keep
  detailed complete-loop treatment to the selected five unless more exercise
  pages are added in the same reviewed slice.
- README promotion waits for the full approved pattern set, not this page alone.
- The first slice must automatically check exercise-link existence and image
  asset existence. Other semantic checks can stay review-only unless the
  existing checker can enforce them cleanly without a separate proof artifact.

## Initial Intent Preservation

| Initial user goal | Proposal treatment | Where recorded |
| --- | --- | --- |
| Create a proposal | in scope | Status, Recommended Direction, Next Artifacts |
| Follow best practices | in scope | Context, Options Considered, Testing and Verification Strategy, Risks and Mitigations |
| Follow the best pattern architecture | in scope | Goals, Context, Recommended Direction |
| Make the reason of the pattern clear | in scope | Goals, Recommended Direction |
| Make how to address this pattern clear | in scope | Goals, Recommended Direction |
| Define a best-practice pattern for future patterns | in scope | Goals, Recommended Direction, Architecture Impact |
| Integrate the pattern standard into architecture | in scope | Goals, Architecture Impact, Next Artifacts |
| Include core reason | in scope | Recommended Direction |
| Include exercises and muscles | in scope | Recommended Direction |
| Use imagegen for high-quality explanatory information | in scope | Context, Recommended Direction, Testing and Verification Strategy |
| Avoid unsafe or overbroad posture content | in scope | Non-goals, Risks and Mitigations |
| Split rounded shoulders and forward head posture into two patterns | in scope | Recommended Direction, Scope Budget |
| Focus this proposal on `patterns/forward-head-posture.md` | in scope | Goals, Recommended Direction, Architecture Impact |
| Include corresponding exercises so the pattern creates a complete loop | in scope | Goals, Recommended Direction, Testing and Verification Strategy |
| Use the four-part source set for red flags, uncertainty, shoulder/scapular context, and resistance-training framing | in scope | Recommended Direction, Testing and Verification Strategy |
| Use one comparison image only | in scope | Recommended Direction, Testing and Verification Strategy |
| Highlight important user information in the image without in-image text | in scope | Recommended Direction, Testing and Verification Strategy |
| Put reusable pattern architecture in spec, architecture, and template | in scope | Recommended Direction, Architecture Impact |
| Do not require separate proof artifacts; check required sections and no in-image text | in scope | Testing and Verification Strategy |
| Use "Forward Head Posture" as the page title | in scope | Resolved Decisions, Decision Log |
| Select five detailed exercises for the complete loop | in scope | Resolved Decisions, Recommended Direction, Scope Budget, Decision Log |
| List the broader collected exercise set in the pattern document | in scope | Resolved Decisions, Recommended Direction, Scope Budget |
| Gate README promotion on the full approved pattern set | in scope | Resolved Decisions, Rollout and Rollback, Scope Budget, Decision Log |
| Automatically check exercise-link existence and image-asset existence | in scope | Resolved Decisions, Testing and Verification Strategy, Scope Budget, Decision Log |

## Scope Budget

| Work item | Treatment | Reason |
| --- | --- | --- |
| Reusable best-practice pattern architecture | core to this proposal | This is the updated direction and protects quality for future patterns. |
| `patterns/forward-head-posture.md` proof page | first-slice candidate | The forward-head page proves the reusable standard. |
| Rounded shoulders pattern page | separate proposal | The user asked to split the combined pattern and focus this proposal on forward head posture. |
| Spec and architecture integration | same-slice dependency | The user explicitly wants the pattern standard integrated into architecture before future patterns rely on it. |
| Final pattern-page content | separate implementation slice | Content requires spec, review, source validation, and tests before implementation. |
| Generated explanatory visual | first-slice candidate | A preview image was generated, but final project media needs provenance, review, and validation. |
| Five corresponding exercise pages for complete loop | same-slice dependency | Create `exercises/chin-nod.md`, `exercises/thoracic-extension.md`, `exercises/wall-slide.md`, `exercises/prone-y-t.md`, and `exercises/band-pull-apart.md` so the detailed pattern annotations have linked exercise pages. |
| Broader collected exercise list | page content, secondary detail | The pattern document may list all collected options, but only the selected five receive detailed complete-loop treatment in the first slice. |
| New exercise pages beyond the selected five | separate implementation slice | Additional exercises broaden the content surface and should be explicitly scoped downstream. |
| Checker/test updates | same-slice dependency | Required for source-set coverage, complete-loop mapping, required sections, exercise-link existence, image-asset existence, no in-image text, one-image constraint, and media provenance. |
| README promotion | pattern-set follow-up | Promotion should wait until the full approved pattern set passes downstream review and verification. |
| Workflow-guide or constitution stale-text cleanup | separate proposal | The refreshed project map identifies this risk, but it is not part of the pattern-page direction. |

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-30 | Draft a single combined rounded-shoulders/forward-head pattern proposal. | This was the initial candidate because it connected to existing pull, press, and trunk-control pages. | Short awareness-only page, corrective routine page, and different next pattern. |
| 2026-06-30 | Treat imagegen output as preview-only during proposal. | Project media requires provenance, review, and validation before it can become content. | Commit generated media directly during proposal authoring. |
| 2026-06-30 | Keep exercise mapping non-prescriptive. | GymPrimer can explain movement options, but must not provide posture-treatment routines. | Fixed routine, frequency prescription, or "fix your posture" framing. |
| 2026-06-30 | Expand the proposal to define reusable pattern architecture before the page proof. | Future patterns need the same quality bar, not one-off imitation of APT. | Single-page-only proposal without architecture integration. |
| 2026-06-30 | Split rounded shoulders and forward head posture; focus this proof slice on `patterns/forward-head-posture.md`. | The user selected forward head posture as the immediate focus. | Combined rounded-shoulders/forward-head page. |
| 2026-06-30 | Make complete-loop exercise mapping part of the pattern standard. | Future patterns should connect reason, exercise, muscles, and cue/caveat instead of stopping at explanation. | Pattern page with unsupported exercise categories. |
| 2026-06-30 | Use one comparison image only for the first proof slice. | Exercise thumbnails belong on exercise pages, and the pattern page should not read like a visual routine. | Comparison image plus exercise thumbnails. |
| 2026-06-30 | Put reusable pattern architecture in spec, architecture, and template. | Spec owns policy, architecture locates it in the system, and template makes it usable. | Template-only governance. |
| 2026-06-30 | Prefer automated/checkable validation over separate proof artifacts for this proposal. | Required sections, no in-image text, source coverage, complete loop, and provenance can be directly checked. | Defaulting to separate audit records for this slice. |
| 2026-06-30 | Use "Forward Head Posture" as the page title. | The user chose the established pattern name over a plainer beginner paraphrase. | "Head Sits Forward" as the page title. |
| 2026-06-30 | Use five detailed corresponding exercises in the first complete loop. | The selected set covers neck awareness, thoracic motion, shoulder-blade control, upper-back support, and rear-shoulder/upper-back strength without becoming a routine. | Smaller subset or detailed treatment for every collected exercise. |
| 2026-06-30 | Gate README promotion on the full approved pattern set. | A single pattern page should not be promoted ahead of the reviewed set-level pattern architecture. | Promote README after the forward-head page alone. |
| 2026-06-30 | Automate exercise-link and image-asset existence checks in the first slice. | Broken links and missing media are deterministic and should not rely on review-only validation. | Review-only link and image existence checks. |

## Next Artifacts

- Proposal review for this draft.
- If accepted, a focused spec or spec amendment for the best-practice pattern
  architecture and forward-head-posture proof slice.
- Architecture amendment for the reusable pattern-page contract unless
  proposal-review determines the existing architecture already fully covers it.
- Template update only if the reviewed spec/architecture finds gaps in
  `docs/templates/pattern-page.md`.
- Test-spec or proof-map update for architecture/template assertions,
  pattern-specific assertions, source-set coverage, complete-loop coverage, and
  media proof.
- Implementation slice for the pattern page, five same-slice exercise pages,
  final pattern image asset, provenance row, and directly affected tests.

## Follow-on Artifacts

None yet

## Readiness

Ready for proposal-review. The direction is narrow enough to review, and open
questions can be resolved during spec authoring without blocking proposal
review.
