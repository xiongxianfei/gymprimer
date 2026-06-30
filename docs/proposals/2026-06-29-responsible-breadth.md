# Responsible Breadth: Solving Three Core User Pain Points

## Status

accepted

## Problem

GymPrimer's current vision narrowly refuses three large content categories:
conditions, individualized programming, and rehab-adjacent guidance. That refusal
is primarily driven by safety and legal-exposure concerns, but it leaves three
beginner pain points unaddressed:

1. Beginners search for specific problems they cannot solve themselves, such as
   anterior pelvic tilt, forward head posture, sore neck, nagging low back pain,
   plantar fasciitis, and similar patterns or conditions. They need to know what
   is appropriate, what is dangerous, and when to stop using a primer and see a
   professional.
2. Beginners struggle to learn movement from text alone. Even a well-written
   exercise card cannot reliably teach what a correct movement looks like or
   what "engage your lats" should mean without clear visuals.
3. Beginners need enough structure to be consistent. They ask how often to train,
   how many sets and reps to do, when to add weight, and what a reasonable
   beginner week can look like.

Comparable educational resources address these questions by being specific,
well-cited, honest about authorship, and clear about safety routing. A
non-commercial Markdown-first primer can use the same proportionate model
without becoming a clinical product, personalized coach, or commercial fitness
app.

## Goals

1. Address common patterns and conditions with a responsible consumer-education
   structure: overview, when to see a professional, what commonly helps, and
   cited sources.
2. Establish a visual instruction standard so exercise pages show correct form,
   common mistakes, muscle activation, equipment setup when relevant, and
   alignment where useful.
3. Add programming-literacy content that explains frequency, sets, reps, rest,
   progression, weekly templates, warm-up, and recovery with cited ranges.
4. Add two or three established beginner-program examples as illustrations of
   how principles compose, without giving individualized prescriptions.
5. Maintain proportionate safety care through citation discipline, a red-flags
   reference, and honest single-author attribution.
6. Keep the project shape unchanged: Markdown-first source content in the
   repository, optional mdBook output, Apache-2.0 code licensing, CC BY 4.0
   content licensing, and community Issues and PRs as correction channels.

## Non-goals

- Personalized symptom-checker UIs, diagnostic decision trees, or any feature
  that takes user input and outputs a diagnosis or personalized prescription.
- Acute injury, post-surgical, pediatric, pregnancy, oncology-related,
  mental-health-adjacent, or other content categories where mainstream consensus
  is weak or the audience is not general fit adults learning to train.
- AI-generated content as a source of truth.
- Per-card disclaimer scaffolding, reader-visible tier classifications, terms of
  use, privacy policy, trademark registration, or similar commercial-grade legal
  apparatus.
- Claims of clinical authority or implied credentials beyond what the named
  author actually has.
- A commercial release path.
- A hosted application, CMS, account system, runtime API, or video-first media
  product.

## Vision fit

proposes a vision revision

This proposal does not fit `CONSTITUTION.md` or `VISION.md` as written on
2026-06-29. The constitution currently says GymPrimer teaches exercise literacy
before workout prescription, must not become a workout planner or clinical
rehabilitation product, and must avoid active-rehab guidance,
posture-correction promises, and injury-specific protocols. The current vision
says GymPrimer will not prescribe workouts, treat pain, provide rehabilitation
pathways, publish injury-specific advice, or serve users who want personalized
workout plans. It also frames the first slice as narrow exercise literacy before
workout prescription.

Acceptance of this proposal requires amending both `CONSTITUTION.md` and
`VISION.md` before any ADR, spec, architecture, plan, validation, or content work
relies on the expanded scope. The constitution amendment would preserve the
project's refusal to become a workout planner, clinical rehabilitation product,
injury-diagnosis tool, AI coach, or video-first source of truth, while permitting
static, citation-based consumer education for common patterns, conditions,
programming literacy, and program examples under the proposal's
non-diagnostic/non-prescriptive boundaries.

The amended vision would preserve GymPrimer as a beginner-first, Markdown-first,
citation-based educational primer, but narrow the refusal line to personalized
diagnosis or treatment plans; acute, post-surgical, pediatric, pregnancy,
oncology, or similar specialized contexts; AI-generated source-of-truth content;
and claims to clinical authority.

The proposal also requires superseding
`docs/adr/2026-06-27-markdown-first-citation-based-authority.md`, which currently
records conservative beginner scope, page-local disclaimers, and no medical
advice as active architectural commitments.

## Initial Intent Preservation

| Initial user goal | Proposal treatment | Where recorded |
| --- | --- | --- |
| Help beginners understand common exercises | in scope | Goals, Recommended Direction |
| Explain equipment setup | in scope | Visual Standard, Recommended Direction |
| Show muscles engaged | in scope | Visual Standard |
| Break down each movement | in scope | Goals, Visual Standard |
| Help beginners solve specific problems such as anterior pelvic tilt or sore neck | in scope | Goals, Recommended Direction |
| Teach how often and how much to train | in scope | Goals, Recommended Direction |
| Provide example programs | in scope | Goals, Recommended Direction |
| Avoid personalized diagnosis or treatment plans | out of scope | Non-goals |
| Avoid acute injury, post-surgical, oncology, pregnancy, and similar specialized content | out of scope | Non-goals |
| Preserve Markdown-first repository shape | in scope | Goals, Architecture Impact |
| Avoid commercial-grade legal scaffolding | in scope | Non-goals, Scope Budget |

## Context

The accepted Markdown-first direction made the repository itself the product.
Before the Responsible Breadth constitution amendment, `CONSTITUTION.md` defined
GymPrimer as an open-source Markdown primer for gym beginners that taught
exercise literacy before workout prescription. It also stated that the project
must not become a workout planner, clinical rehabilitation product,
injury-diagnosis tool, AI coach, or video-first source of truth.

That direction solved the first platform problem: keep content readable in
GitHub, source-backed, narrow, and verifiable before building machinery. The next
product question is whether the primer should stay at exercise literacy only or
address the broader questions beginners actually bring to exercise education.

Comparable open educational resources use a more specific but still bounded
model. Consumer medical sites such as Mayo Clinic and NHS UK commonly structure
condition pages around red flags, plain-language explanation, self-care ranges,
and professional-routing guidance. Fitness education resources such as the
r/Fitness wiki, Starting Strength, Stronglifts 5x5, Stronger by Science, and
PainScience.com build trust through specificity, citations, public correction,
and honest authorship rather than by refusing all programming or health-adjacent
topics.

This proposal treats those resources as directional evidence for a
non-commercial educational posture. It does not assert that GymPrimer has
clinical authority or can provide individualized care.

## Options Considered

### Option A: Keep current narrow scope

Continue refusing conditions, prescription, and programming content as the
current vision specifies.

Advantages: lowest implementation effort; no vision amendment needed; no
editorial-standard expansion.

Drawbacks: leaves all three stated beginner pain points unaddressed; risks a
primer that beginners outgrow quickly; keeps the project less useful than
comparable educational resources.

Disposition: rejected. The current refusal protects scope, but it also blocks
the highest-value beginner questions.

### Option B: Expand scope with heavy disclaimer and tier scaffolding

Widen content scope but add per-card disclaimer blocks, visible tier
classifications, formal review boards, and other commercial-grade safety
infrastructure.

Advantages: maximally cautious; easier to justify if the project later shifts
toward a commercial product.

Drawbacks: disproportionate for a non-commercial single-author primer; clutters
the reading experience; creates commitments such as review boards that the
project cannot currently honor.

Disposition: rejected. The overhead is not proportionate to the project shape.

### Option C: Expand scope with citation discipline and red-flag routing

Widen content scope to address all three pain points. Use citation discipline as
the accuracy mechanism, a red-flags reference linked from safety-relevant pages
as the routing mechanism, honest named authorship as the trust mechanism, and one
project-level disclaimer in the root README.

Advantages: directly addresses the user value; matches the repository's
Markdown-first shape; remains sustainable for a single author; keeps the project
educational rather than diagnostic or prescriptive.

Drawbacks: requires vision and ADR amendments; needs explicit editorial
standards; increases the risk and maintenance burden of content quality.

Disposition: recommended.

### Option D: Add interactive symptom-checker or decision-tree features

Build forms or decision trees that take user-symptom input and route to specific
content or recommend specific actions.

Advantages: could surface relevant content faster than static navigation.

Drawbacks: moves the project toward decision support; raises responsibility
considerations beyond static educational content; adds runtime complexity that
conflicts with the Markdown-first direction.

Disposition: deferred. Static content should prove its value before any
interactive layer is reconsidered.

## Recommended Direction

Choose Option C: expand GymPrimer's content scope with citation discipline,
red-flag routing, honest authorship, and explicit refusal of personalized
diagnosis or treatment.

The content surface becomes six sections:

1. Exercises: the original card library, with the visual standard, citations,
   and a consistent structure covering purpose, setup, phases, muscles, cues,
   mistakes, regressions, and progressions.
2. Patterns: consumer-education pages for non-diagnostic postural or movement
   patterns such as anterior pelvic tilt or forward head posture. Each page
   opens with a red-flags link, explains the pattern in plain language,
   summarizes mainstream source agreement and uncertainty, describes general
   self-management themes, and routes readers to a professional for
   individualized assessment.
3. Conditions: consumer-education pages for common well-studied conditions such
   as non-specific chronic low back pain, plantar fasciitis, patellofemoral pain,
   and rotator cuff-related shoulder pain. Each page uses red-flag routing,
   non-diagnostic language, uncertainty disclosure, and professional-routing
   guidance.
4. Principles: programming-literacy pages covering frequency, sets and reps,
   rest intervals, progressive overload, weekly templates, warm-up, cool-down,
   and recovery basics.
5. Programs: two or three established beginner program examples presented as
   illustrations of how principles compose, not as the reader's personalized
   prescription.
6. About, Red Flags, and Sources: the project-level honesty artifacts, including
   author identity and disclosures, red-flag checklist, professional-routing
   guidance, disclaimer, and complete bibliography.

The trust model is citation-backed education first: citations are the accuracy
mechanism, red-flags routing is the safety mechanism, and named single-author
honesty is the credential.

## First Slice Candidate

The first expanded-scope proof slice should test the new safety and programming
boundaries without forcing exercise-card expansion into the same proof:

- `about/red-flags.md`
- `patterns/anterior-pelvic-tilt.md`
- `conditions/non-specific-chronic-low-back-pain.md`
- `principles/how-many-days-a-week.md`
- `programs/generic-3-day-full-body-example.md`

This slice is a proof of the framework, not an implementation milestone. If the
slice does not hold up to self-review and informal beginner-reader feedback, the
offending section should be narrowed before scaling.

Existing exercise-page work should remain a separate proof path. Expanded
patterns, conditions, or program pages should not publish until the current
Markdown-first first-slice comprehension proof discipline is closed and
confirmed, including per-page outcomes for purpose, setup or body position,
movement steps where relevant, stop condition, and source verification.

## Visual Standard

Exercise pages should include only the visuals necessary for beginner
comprehension. Machine pages normally need equipment setup images and key
movement frames. Muscle overlays, wrong-frame comparisons, and alignment diagrams
are recommended when they materially reduce confusion, but they are not mandatory
for every first-slice page or regression.

Pattern pages should use an alignment silhouette when it clarifies the pattern
against neutral alignment. Condition pages should use an anatomical region
diagram when it clarifies relevant structures without pathologizing the reader.

Regression visuals are change-based:

| Regression change | Visual treatment |
| --- | --- |
| Same equipment, easier range or load | No new equipment image; add a key-position note or inset only when needed |
| Different equipment | Add a setup image for the regression equipment |
| Different body position | Add start/end or key-position frames for the regression |
| Different target muscle emphasis | Add or update the muscle overlay |
| Same target and movement pattern | Reuse the main page's muscle explanation |
| Common beginner mistake changes | Add a wrong-frame comparison only for that regression |

The preferred production approach is a reusable original vector style built from
a single body-silhouette template. Anatomy reference assets can use
license-compatible public-domain or CC BY sources when attribution requirements
are satisfied. A short illustration style guide should fix figure proportions,
line weight, muscle palette, viewpoint conventions, arrows, and annotation style
before the visual layer scales.

## Editorial Standard

Each content page across the content sections should:

1. Cite at least three named authoritative sources, with inline footnotes or
   links to public URLs where possible.
2. Be signed by the named author with a date.
3. Use plain language for a beginner reader.
4. Link to the red-flags reference when the page addresses a pattern, condition,
   or other safety-relevant content.
5. Distinguish mainstream agreement from contested or mixed evidence.

The boundary is educational generality. In-scope content describes what
mainstream sources say and gives examples. Out-of-scope content takes user input
and outputs an individualized diagnosis, treatment plan, or program.

Citation count is a floor, not the whole quality rule:

| Page type | Minimum source quality |
| --- | --- |
| Exercise page | One or two authoritative technique or institutional sources, plus anatomy source support when needed |
| Pattern page | At least two institutional, clinical, or public-health sources plus one supporting source |
| Condition page | At least two institutional, clinical-guideline, or patient-education sources plus one supporting source |
| Programming-principle page | Public-health guidance plus resistance-training guidance and supporting evidence where needed |
| Program example | Public-health guidance, resistance-training guidance, and a cited beginner-program illustration source |

Pattern, condition, and program-example PRs use a higher review bar than ordinary
exercise-page edits. They require source traceability, red-flag routing,
non-diagnostic language, no individualized treatment or programming, and
maintainer confirmation that the page remains consumer education rather than
treatment or prescription.

Pattern and condition pages should use this page contract:

```md
# Page title

## What this page is
## What this page is not
## Red flags: when to stop reading and seek care
## Plain-language overview
## What mainstream sources generally agree on
## What is uncertain or mixed
## Commonly recommended self-management themes
## What to avoid
## When to see a professional
## Sources
## Author and review date
```

These headings are out of scope for pattern and condition pages:

```md
## Treatment plan
## Diagnosis
## Fix this in 30 days
## Corrective routine for you
```

Program examples are allowed only as static educational worked examples:

| Illustration | Prescription |
| --- | --- |
| Static example for general healthy beginners | Adapts to reader inputs |
| Explains how principles compose | Tells the reader what they should personally do |
| Uses broad cited ranges | Selects load, exercise, or progression based on symptoms |
| Includes scope warning | Handles pain, injury, rehab, or medical context |

Published pages should use risk-based review cadence plus triggered review:

| Page type | First review after publication | Normal cadence | Triggered review |
| --- | --- | --- | --- |
| Exercise pages | 90 days | Annually after the first review | Reader confusion, changed source, safety complaint, or media issue |
| Pattern pages | 90 days | Every 6 months for the first year, then annually if stable | Safety concern, new source, repeated confusion, or scope-boundary concern |
| Condition pages | 90 days | Every 6 months | Source change, red-flag update, PR dispute, or reader misinterpretation |
| Programming-principle pages | 90 days | Annually after the first review | Guideline changes or repeated reader misunderstanding |
| Program examples | 90 days | Every 6 months | Any sign readers treat the example as a personal prescription |
| Red-flags reference | 90 days | Every 6 months | Immediately when a cited red-flag source changes |

Each published page should carry simple review metadata:

```md
Author: <name>
Created: YYYY-MM-DD
Last reviewed: YYYY-MM-DD
Next review due: YYYY-MM-DD
Review scope: sources, red flags, scope boundary, comprehension
```

## Expected Behavior Changes

After this proposal is implemented, a beginner can:

1. Look up an exercise and see clear images of correct form, what muscles are
   doing, and what to avoid.
2. Look up a common postural pattern and find a plain explanation, cited
   contributor discussion, commonly recommended actions, and professional-routing
   guidance.
3. Look up a well-studied condition and find structured education with red-flag
   routing.
4. Look up a programming question and find evidence-based ranges with citations.
5. Read an example beginner program and understand how principles compose into a
   week.
6. Recognize red-flag symptoms that should bypass the project entirely.
7. Understand when a PT, GP, urgent care, or emergency care may be more
   appropriate than repository content.

## Architecture Impact

The architecture impact is intentionally limited but not zero.

The source of truth remains Markdown files in the repository. The proposed
content organization is:

- `exercises/`
- `patterns/`
- `conditions/`
- `principles/`
- `programs/`
- `about/`
- `assets/` or `media/` for illustration assets, with subdirectories by content
  type if needed.

Optional HTML generation via mdBook remains derived output. No frontend app, CMS,
database, API, account system, personalization engine, or runtime decision logic
is introduced.

Because this proposal changes content scope, safety posture, visual standards,
and source authority, it requires updates to `VISION.md`, the active ADR trail,
and likely the approved Markdown-first spec before implementation.

## Testing and Verification Strategy

Likely verification should combine automated checks and bounded audit review:

- Content quality: author verifies each substantive claim against cited sources
  and distinguishes mainstream agreement from mixed evidence.
- Citation quality: automated checks verify source-index validity and minimum
  source count, while manual semantic review verifies that sources are
  authoritative enough for the claim being made.
- Safety routing: automated check confirms each pattern or condition page links
  to the red-flags reference.
- Scope boundaries: audit records confirm that pattern and condition
  pages remain non-diagnostic and that program examples remain static
  illustrations rather than individualized prescriptions.
- Link integrity: automated internal-link and external-link checks where tooling
  exists.
- Media quality: validation checks for asset paths, alt text, license and
  provenance entries, and necessary visuals by page class.
- Build smoke test: mdBook or equivalent generated output builds cleanly when
  generation is configured.
- Comprehension check: after a delay, the author rereads each page against its
  intended beginner question. Audit records should capture page-level
  outcomes for purpose, body position or setup where relevant, movement or
  principle steps, stop condition, and source verification. Where possible, one
  or two beginner readers review the first slice before scaling.

If no tooling exists for a check, the implementation plan should record the
audit verification method and the residual automation gap.

## Rollout and Rollback

Rollout should happen page by page after the first expanded-scope slice validates
the editorial standard and after the current Markdown-first first-slice
comprehension proof discipline is closed or reconfirmed. The likely expansion
order is patterns and conditions first, then principles, then exercises, then
programs, based on beginner search pain and scope risk.

Rollback is content-level: correct, narrow, or remove a page through the normal
Issue and PR process. If the first slice exposes an unsafe or unsustainable
section, the project should narrow or defer that section before scaling.

No runtime rollback, migration flag, or compatibility bridge is needed because
the project remains static Markdown.

## Risks and Mitigations

| Risk | Likelihood | Mitigation |
| --- | --- | --- |
| Incorrect content | Medium | Citation discipline, community Issues and PRs, first-slice proof before scaling |
| Reader mistakes a pattern page for a diagnosis | Low-Medium | Plain "this does not diagnose you" language on pattern pages and red-flag routing |
| Reader pushes through pain after reading a page | Medium | Red-flags reference, stop/seek-care guidance, professional-routing sections |
| Author burnout from editorial workload | Medium | First-slice scope control, scale only after framework proof, explicit non-goals |
| Scope drift into refused categories | Medium | Vision amendment with clear refusals, contribution rejection criteria, review checks |
| Source links rot | Low-Medium | Central sources index, periodic link checks, preference for institutional sources |
| Visual standard inconsistency | Medium | Illustration style guide before scaling visuals |
| Visual workload crowds out content proof | Medium | Use necessary visuals by page type instead of a fixed image package |
| Program example is treated as a personal prescription | Medium | Static-example boundary, no input adaptation, manual scope proof |
| Governance conflict with current artifacts | High until resolved | Amend `CONSTITUTION.md`, amend `VISION.md`, then supersede the active ADR before any expanded-scope work relies on the new direction |

## Scope Budget

| Work item | Treatment | Reason |
| --- | --- | --- |
| Six-section content surface | core to this proposal | Directly addresses the three beginner pain points while separating patterns from conditions |
| Constitution amendment | same-slice dependency | The highest-ranked source currently conflicts with the proposed health-adjacent and programming-literacy scope |
| Vision amendment | same-slice dependency | Current vision conflicts with the proposed scope |
| Superseding ADR | same-slice dependency | Active architecture commitments conflict with the proposed trust and scope model |
| Illustration style guide | core to this proposal | Launch-blocking standard for visual consistency |
| Red-flags reference | core to this proposal | Safety routing mechanism for patterns and conditions |
| Sources index updates | core to this proposal | Quality and trust mechanism |
| Project-level README disclaimer | core to this proposal | Single trust and scope artifact for readers |
| First expanded-scope proof slice | first-slice candidate | Proof of pattern, condition, principle, and program boundaries before scaling |
| Exercise-card expansion | separate implementation slice | Existing exercise-page proof work should not be coupled to the expanded-scope proof |
| Per-card disclaimer scaffolding | out of scope | Disproportionate to non-commercial educational scope |
| Reader-visible tier classifications | out of scope | Adds confusion without matching project capacity |
| Terms of use, privacy policy, wordmark registration | out of scope | Not needed for the proposed non-commercial static corpus |
| Symptom-checker or decision-tree UI | deferable follow-up | Different product shape; reconsider only after static content stabilizes |
| Bilingual English/Chinese content | deferable follow-up | Translation should follow stable English source content |
| Hosted website | deferable follow-up | mdBook or repository browsing is enough for this direction |
| AI-assisted retrieval | deferable follow-up | Reconsider only after curated static content exists |

## Resolved Decisions

| Question | Decision |
| --- | --- |
| First-wave patterns and conditions beyond anterior pelvic tilt and non-specific chronic low back pain | Add forward head posture or non-specific neck pain, plantar fasciitis, patellofemoral pain, and rotator cuff-related shoulder pain. Keep Achilles tendinopathy and shin splints as second-wave candidates. |
| PR standard for patterns and conditions | Use a higher review bar than exercise pages: source trace, red-flag link, non-diagnostic language, no individualized treatment, and maintainer safety-boundary review. |
| Program illustration versus prescription | Static worked examples are allowed; user-adaptive, symptom-adaptive, individualized, or injury-specific programming is out of scope. |
| Visual standard for regressions | Visuals are change-based. Different equipment requires a setup visual; different body position requires a key-position visual; unchanged movement and muscle emphasis can reuse the existing explanation. |
| Review cadence | Use a 90-day first review; six-month cadence for safety-relevant pages and program examples until stable; annual review for stable exercise and principle pages; triggered review for source, safety, confusion, or scope changes. |

## Open Questions

None for proposal acceptance. Downstream specs still need to turn the resolved
decisions into testable page contracts, validation rules, and audit evidence
records.

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-29 | Propose expanding content scope to patterns, conditions, principles, and program examples | Directly serves the three core beginner pain points | Keep narrow refusal; add heavy disclaimer scaffolding; add interactive symptom checker |
| 2026-06-29 | Use citation discipline, honest authorship, and red-flag routing as the trust model | Sustainable for a single-author non-commercial primer | Formal review board; AI-generated source of truth; clinician-authored-only content |
| 2026-06-29 | Drop commercial-grade legal scaffolding from the recommended option | Disproportionate for static open educational Markdown | Per-card disclaimer blocks; reader-visible tiers; terms-of-use document |
| 2026-06-29 | Use necessary visuals by page type instead of a fixed image package | Movement comprehension matters, but a mandatory multi-image package creates too much first-slice media workload | Text-only pages; photo-first pages; video-first product; mandatory three-image package |
| 2026-06-29 | Include example programs as illustrations | Programming literacy requires seeing how principles compose | Refuse all program examples; build a personalized program generator |
| 2026-06-29 | Separate `patterns/` from `conditions/` | Separating non-diagnostic patterns from condition education reduces diagnostic overreach | Combined `patterns-and-conditions/` section |
| 2026-06-29 | Use a higher review bar for patterns, conditions, and program examples | These pages carry more safety and prescription-boundary risk than ordinary exercise edits | Same review bar for all content pages; formal clinician board |
| 2026-06-29 | Gate expanded publication on first-slice comprehension proof discipline | Broader safety-relevant content should not publish until existing comprehension proof practice is closed or reconfirmed | Publish expanded pages immediately after proposal acceptance |
| 2026-06-29 | Revise constitution-level scope boundaries before relying on vision or ADR changes | `CONSTITUTION.md` is the highest-ranked source of truth and currently conflicts with the expanded health-adjacent and programming-literacy direction | Rely on vision amendment alone; rely on ADR supersession alone; record a one-off exception |

## Next Artifacts

1. Proposal review R3 for this revised draft direction.
2. If accepted, amend `CONSTITUTION.md` to permit static, citation-based
   consumer education for common patterns, conditions, programming literacy, and
   program examples under non-diagnostic and non-prescriptive boundaries, while
   preserving refusals of workout planning, clinical rehabilitation, diagnosis,
   individualized treatment, AI coaching, and video-first source truth.
3. If accepted, amend `VISION.md` to narrow refusals from broad rehab and
   prescription refusal to the proposed personalized-diagnosis,
   personalized-treatment, specialized-population, AI-source-of-truth, and
   clinical-authority refusals.
4. If accepted, supersede
   `docs/adr/2026-06-27-markdown-first-citation-based-authority.md` with the
   citation-based authority, red-flag routing, visual-standard, and honest
   single-author model.
5. Write or amend the relevant spec for content sections, page contracts,
   citation quality, safety routing, media requirements, review cadence,
   program-boundary rules, and validation checks.
6. Create architecture updates only where needed for repository layout, media
   storage, validation boundaries, or generated output.
7. Plan the first slice after proposal, spec, architecture, and required reviews
   are complete.

## Follow-on Artifacts

- Proposal review R3: `docs/changes/responsible-breadth/reviews/proposal-review-r3.md`
- Constitution amendment: `CONSTITUTION.md`
- Vision amendment: `VISION.md`
- Vision positioning update: `docs/vision/strategic-positioning.md`
- Draft spec: `specs/responsible-breadth.md`
- Change rationale: `docs/changes/responsible-breadth/explain-change.md`

## Readiness

This proposal has been accepted and approved by proposal-review R3. The
constitution and vision amendments are complete, and the draft Responsible
Breadth spec exists. Expanded-scope ADR, architecture, plan, validation, and
content work remain blocked until the spec is reviewed and downstream artifacts
are updated in source-of-truth order.
