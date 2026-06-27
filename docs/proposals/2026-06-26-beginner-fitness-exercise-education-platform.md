# Proposal: Beginner Fitness Exercise Education Platform

## Status

accepted

This proposal records an accepted product direction. It is not implementation-ready, medically validated, or ready for public release.

## Problem

Fitness beginners often enter the gym without a reliable mental model for what an exercise trains, how to set up common machines, how a movement breaks down into setup and execution phases, what muscles they should feel, and when a sensation is a stop sign rather than normal effort.

Existing fitness resources teach in fragments. Short-form videos show motion but often omit equipment setup and beginner cues. Exercise databases list muscles but do not reliably explain how a beginner should set up the machine, feel the movement, avoid common compensation, or choose an easier version. Workout apps often prescribe sets and reps before the user understands the exercise being prescribed.

GymPrimer should solve exercise literacy before it tries to solve programming, coaching, personalization, or rehabilitation.

## Goals

- Teach common beginner gym exercises with clear, plain-language cards.
- Explain equipment setup for machines, cables, benches, free weights, and cardio equipment.
- Identify primary muscles, secondary muscles, stabilizers, and beginner-friendly "what you should feel" cues.
- Break every movement into a repeatable card structure: purpose, setup, start position, movement phases, breathing and bracing, common mistakes, regressions, progressions, and safety notes.
- Include narrow beginner training-principles literacy where it helps users interpret exercise cards: movement patterns, effort language, warm-up basics, recovery concepts, pain rules, and the difference between exercise education and workout prescription.
- Support conservative progression by teaching easier versions before harder versions.
- Use English-first content with a locale-aware schema that keeps Chinese as a first-class future locale.
- Use reviewed SVG step cards as canonical media, with accessible text alternatives.
- Keep reviewed content as the source of truth so later interactive or AI features can only build on approved material.

## Non-goals

- Do not launch as a personalized workout generator, coaching platform, rehabilitation product, injury-diagnosis tool, or medical-advice product.
- Do not optimize the first release for advanced bodybuilding, powerlifting, Olympic lifting, sport-specific programming, pregnancy training, post-surgical rehab, acute pain, youth athletes, cardiovascular disease, neurological conditions, or complex medical histories.
- Do not use unconstrained AI-generated exercise guidance as source-of-truth content.
- Do not make original or community video the canonical movement source for launch.
- Do not require bilingual card publication before the English schema and review workflow are stable.
- Do not treat the number of exercises as the main success metric.

## Vision fit

fits the current vision

This proposal fits `VISION.md` by choosing a reviewed exercise-literacy platform upstream of workout prescription. It preserves the current vision's English-first launch, Chinese-ready schema, tiered review model, Apache 2.0 posture, SVG step-card media source of truth, refusal of medical advice, and preference for depth on roughly forty to sixty exercises rather than shallow breadth.

The provided draft included broader training-principles and media language. This proposal narrows those points to fit the vision: training principles are literacy modules, not workout programming, and video is later supplemental media, not canonical launch content.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
| --- | --- | --- |
| Help fitness beginners understand common exercises | in scope | Goals; Recommended Direction; Expected Behavior Changes |
| Help users understand gym equipment | in scope | Goals; Expected Behavior Changes; Architecture Impact |
| Teach basic training principles | in scope | Goals; Recommended Direction; Scope Budget |
| Explain which muscles should be engaged | in scope | Goals; Expected Behavior Changes |
| Break down each movement | in scope | Goals; Recommended Direction |
| Base the proposal on best practices | in scope | Context; Testing and Verification Strategy |
| Use notes about common machines, muscles, posture concerns, breathing, tempo, and safe progression | in scope | Context; Exercise Coverage Priorities |
| Build a personalized workout generator | deferred follow-up | Non-goals; Options Considered; Scope Budget |
| Diagnose pain, posture, or injury | out of scope | Non-goals; Risks and Mitigations |

## Context

`docs/project-map.md` records that the repository currently has vision and governance artifacts, but no source tree, content schema, exercise cards, architecture docs, specs, tests, package config, CI, deployment config, or release process. It recommends proposal work before architecture because direction-level choices remain open.

`VISION.md` has already resolved several product-direction choices that the supplied draft listed as open: the launch is English-first with Chinese as a first-class future locale, review uses a tiered mixed panel, and illustrated SVG step cards are canonical media.

External guidance supports the proposal's emphasis on plain language, accessibility, conservative progression, and technique. WHO describes adult activity guidance that combines aerobic activity with muscle-strengthening activity on two or more days per week. CDC health-literacy guidance says plain language makes health information easier to understand and use. W3C WCAG 2.2 provides testable accessibility success criteria for web content. Mayo Clinic emphasizes proper weight-training technique and warns that poor technique can lead to injury. ACSM's 2026 resistance-training update emphasizes consistency, individualization, and avoiding unnecessary complexity for general adults.

Sources:

- [WHO: Physical activity](https://www.who.int/initiatives/behealthy/physical-activity)
- [CDC: Plain Language Materials & Resources](https://www.cdc.gov/health-literacy/php/develop-materials/plain-language.html)
- [W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Mayo Clinic: Weight training technique](https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842)
- [ACSM: 2026 resistance training guidelines update](https://acsm.org/resistance-training-guidelines-update-2026/)
- [NSCA: Resistance training risk discussion](https://www.nsca.com/education/articles/ptq/the-safest-and-riskiest-forms-of-resistance-training/)

## Options Considered

### Option A: Static exercise encyclopedia

Build a searchable library of exercise pages with text, muscles worked, common mistakes, and media.

Advantages: fastest to launch, easier to review, lower product risk, and useful for search discovery.

Drawbacks: passive learning only, weak support for equipment setup and beginner uncertainty, and limited ability to test comprehension.

Disposition: rejected as the full direction, but retained as the content foundation.

### Option B: AI fitness chatbot first

Launch as an AI assistant that answers beginner questions such as "How do I use this machine?" or "What muscles should I feel?"

Advantages: flexible interaction, natural-language input, and possible later personalization.

Drawbacks: high safety risk, hallucination risk, weaker auditability, and conflict with the vision's refusal to use AI-generated content as source of truth.

Disposition: rejected for MVP. A constrained retrieval layer can be considered later after reviewed content exists.

### Option C: Structured exercise-literacy platform

Build a reviewed content library with standardized exercise cards, equipment setup, muscle cues, movement phases, common errors, regressions, progressions, safety notes, SVG step cards, and comprehension checks.

Advantages: strongest fit for beginner education, reviewable by the tiered panel, compatible with locale-aware content, supports accessibility, and creates a safe foundation for later interactive features.

Drawbacks: slower than a static encyclopedia, requires disciplined content operations, needs validation tooling, and requires careful safety language.

Disposition: recommended.

### Option D: Trainer-facing programming and client-management tool

Build software for coaches to prescribe workouts, track clients, and manage communication.

Advantages: clear professional workflow and possible monetization path.

Drawbacks: does not directly solve beginner self-education first, adds client data and compliance complexity, and moves toward coaching and prescription.

Disposition: deferred follow-up outside the first product direction.

## Recommended Direction

Build Option C: a structured exercise-literacy platform.

The product should have three bounded layers:

1. Exercise card layer: reviewed exercise cards with equipment setup, muscles, phases, cues, mistakes, regressions, progressions, safety notes, review metadata, and canonical SVG step cards.
2. Literacy support layer: glossary and short explanations for movement patterns, effort language, warm-up basics, recovery concepts, pain rules, and how exercise education differs from workout prescription.
3. Guided comprehension layer: search, equipment lookup, "what should I feel?" checks, short quizzes, and beginner-readable readiness cues.

The first release should focus on helping a beginner answer:

- What does this exercise train?
- How do I set up this machine or equipment?
- What are the steps?
- What should I feel?
- What mistakes should I avoid?
- What is an easier version?
- When should I stop or ask a qualified professional?

## Exercise Coverage Priorities

The first content set should cover roughly forty to sixty beginner exercises and machines.

Priority 1: common gym machines and cardio equipment, such as lat pulldown, seated cable row, chest press machine, pec deck, leg press, leg extension, leg curl, cable face pull, cable triceps pressdown, cable biceps curl, assisted pull-up or dip machine, hip abduction and adduction machine, rowing machine, stationary bike, and treadmill basics.

Priority 2: foundational free-weight and bodyweight patterns, such as goblet squat, split squat, reverse lunge, Romanian deadlift, hip thrust or glute bridge, push-up progression, dumbbell row, dumbbell chest press, dumbbell shoulder press, farmer carry, suitcase carry, plank, side plank, dead bug, bird dog, and Pallof press.

Priority 3: low-risk mobility and movement-literacy drills, such as hip flexor stretch, thoracic extension drill, wall slide, chin tuck, band pull-apart, lateral band walk, calf raise, hamstring mobility drill, and hip hinge drill. These should be framed as movement education, not guaranteed posture correction or pain treatment.

## Expected Behavior Changes

After the product exists, a beginner should be able to:

- Search for a machine or exercise by name, equipment, body area, movement pattern, or beginner difficulty.
- Open a reviewed guide that explains the exercise in plain language.
- See primary and secondary muscles, stabilizers, and "what you should feel" cues.
- Learn how to adjust equipment before starting.
- Follow the movement through clearly labeled phases.
- Understand breathing and bracing cues.
- Compare intended execution against common mistakes.
- Choose a regression when an exercise feels too difficult.
- Treat progressions as optional next steps tied to readiness cues.
- Read basic literacy guidance without receiving a personalized training plan.
- Recognize stop signs and escalation prompts.

## Architecture Impact

The architecture will need to separate reviewed content from presentation, validation, optional interactivity, analytics, and any later AI layer.

Expected components and boundaries:

| Component | Responsibility |
| --- | --- |
| Exercise content repository | Structured, reviewed, versioned exercise entries |
| Locale-aware content schema | English launch fields with Chinese-ready locale keys |
| Muscle and movement taxonomy | Shared names for muscles, equipment, patterns, difficulty, and safety categories |
| SVG media system | Canonical step cards, alt text, and style-guide validation |
| Learning UI | Exercise pages, search, equipment lookup, glossary, and comprehension checks |
| Safety and escalation rules | Stop signs, referral prompts, contraindication language, and out-of-scope detection |
| Review workflow | Tiered review, reviewer identity, review dates, stale-content checks, and public review history |
| Analytics | Search failures, comprehension gaps, content freshness, and confusion points |
| Optional AI boundary | Later retrieval-only answers from reviewed content with citations and refusals |

Expected data flow:

1. Authors create or revise structured exercise content.
2. Tiered reviewers approve content versions according to risk.
3. SVG step cards and accessible text alternatives attach to reviewed content.
4. Validation checks enforce schema, taxonomy, locale, review metadata, licensing, safety, and media rules.
5. The product renders beginner-facing guides from reviewed content.
6. Search, comprehension checks, and analytics identify gaps for review.
7. Any future AI layer retrieves from reviewed content and refuses out-of-scope requests.

## Testing and Verification Strategy

Content verification:

- Expert review for every published exercise card.
- Separate safety-language review for stop rules, pain language, contraindications, and elevated-risk content.
- Schema and taxonomy validation for muscles, movement patterns, equipment, difficulty, locale keys, review metadata, and media references.
- Version-history checks for changes to safety notes, progressions, and contraindication language.

Beginner comprehension testing:

- Test with people in their first ninety days of regular gym training or returning after a long break.
- Ask users to explain what the exercise trains, how to set up equipment, the first movement phase, what they should feel, one common mistake, and when to stop.
- Treat repeated failure on those checks as a content failure, matching `VISION.md`.

Usability and accessibility testing:

- In-gym search tests such as "find how to use this machine."
- Equipment-name lookup tests.
- Keyboard navigation, screen-reader labels, text alternatives, color contrast, captions or transcripts for any supplemental video, and WCAG 2.2 AA-oriented checks.

Safety testing:

- Review unsafe requests and edge cases involving pain, injury, extreme loading, medical conditions, rapid progression, and diagnosis-seeking.
- Ensure the product routes users to qualified professionals when symptoms are sharp, radiating, worsening, unusual, or emergency-like.

AI-specific testing, only if AI is added later:

- Retrieval-only responses from reviewed content.
- Required citations to reviewed entries.
- Refusal tests for diagnosis, treatment, unsafe progression, extreme loading, and unsupported claims.

## Rollout and Rollback

Rollout should be staged:

| Stage | Scope | Purpose |
| --- | --- | --- |
| Internal prototype | 10-15 cards | Validate schema, tone, SVG style, and page structure |
| Expert-reviewed alpha | 25-30 cards | Validate review workflow and stale-content process |
| Beginner pilot | 40-60 cards | Test comprehension in realistic gym scenarios |
| Public beta | Reviewed library, search, glossary, and comprehension checks | Expand access with conservative safety boundaries |
| Later expansion | Supplemental video, constrained AI, coach-facing exports, or personalization | Add only after source content is stable |

Rollback options:

- Hide an exercise card if safety review finds a defect.
- Revert a content entry to the last reviewed version.
- Disable progressions while retaining regressions and setup guidance.
- Disable supplemental video or AI without removing reviewed static cards.
- Add warning banners to content categories under review.
- Pause public onboarding if safety incidents exceed the threshold defined in a later safety spec.

## Legal, Licensing, and Disclaimers

This proposal records product-direction intent, not legal advice. Final public-beta language should be reviewed by qualified counsel.

Immediate zero-cost posture:

- Put a plain-language disclaimer in every exercise-card footer and the site footer: "GymPrimer is educational content, not medical advice. Talk to a qualified professional before starting a new exercise program; stop and seek qualified help for sharp, radiating, worsening, or unusual symptoms."
- Keep the existing Apache 2.0 `LICENSE` for code.
- Add `LICENSE-content.md` before accepting content contributions, documenting that educational content is licensed under CC BY 4.0 with attributed contribution.
- Adopt DCO sign-offs for contributions.
- Do not add a CLA unless a future proposal identifies a concrete relicensing or contributor-rights need.

Before public beta:

- Draft Terms of Use and Privacy Policy.
- Prefer collecting no personally identifiable information in v1 unless a spec explicitly justifies it.
- Hire a health-tech or consumer-app attorney for a focused review of disclaimer wording, terms, privacy, and contributor license posture.
- Create an incident-response one-pager for reports that a card caused injury, contains factual errors, or has unsafe guidance. The maintainer team should triage within 48 hours, decide whether to hide, revert, or fix the content, and run a postmortem for material incidents.

After public beta has measurable reach:

- Consider USPTO wordmark registration for "GymPrimer" to reduce brand-squatting risk.

Deliberately deferred:

- HIPAA analysis beyond a light counsel check, because the intended v1 is educational content and should not collect health records.
- FDA software-as-medical-device review unless future functionality moves beyond education into diagnosis, treatment, or individualized medical recommendations.
- Professional liability insurance unless counsel recommends it based on actual product scope, review process, or distribution model.

## Risks and Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| User injury from misunderstood instruction | High | Expert-reviewed cards, conservative progressions, common mistakes, stop rules, beginner comprehension tests |
| Product drifts into medical advice | High | Explicit non-goals, safety review policy, referral prompts, no diagnosis language |
| AI hallucination | High | No AI source of truth; later retrieval-only AI from reviewed content |
| Content inconsistency | Medium | Structured schema, taxonomy, validation checks, review metadata |
| Too much anatomy jargon | Medium | Plain language, glossary, everyday terms beside anatomy names |
| Accessibility gaps | Medium | WCAG 2.2 AA-oriented checks, text alternatives, keyboard support |
| Licensing or media mismatch | Medium | Apache-compatible source posture, SVG canonical media, explicit licensing for supplemental assets |
| Contributor-license ambiguity | Medium | Separate code and content licensing, `LICENSE-content.md`, DCO sign-offs, and counsel review before public beta |
| Legal or disclaimer gaps | High | Plain-language disclaimer immediately; Terms of Use, Privacy Policy, incident response, and attorney review before public beta |
| Locale migration debt | Medium | Locale-aware schema from day one even when launch cards are English |
| Review bottlenecks | Medium | Tiered review model and safety-policy review rather than clinician review of every low-risk setup detail |
| Scope creep into programming | Medium | Training principles limited to literacy; workout plans remain out of scope |

## Scope Budget

| Work item | Treatment | Reason |
| --- | --- | --- |
| Structured exercise-card schema | core to this proposal | Foundation for reviewable exercise literacy |
| Beginner exercise library | core to this proposal | Main user-facing value |
| Equipment setup guidance | core to this proposal | Directly addresses gym confusion |
| Muscle engagement explanations | core to this proposal | Required for beginner comprehension |
| Movement phase template | core to this proposal | Required for consistent instruction |
| SVG step-card media standard | core to this proposal | Canonical media source under current vision |
| Locale-aware English-first schema | same-slice dependency | Prevents Chinese support from becoming a migration later |
| Tiered expert review workflow | same-slice dependency | Required for trustworthy publication |
| Safety and escalation rules | same-slice dependency | Required before public use |
| Disclaimer, terms, privacy, and incident-response posture | same-slice dependency | Required before public beta because the product is health-adjacent |
| Code/content licensing and DCO posture | same-slice dependency | Required before accepting public content contributions |
| Accessibility and plain-language standards | same-slice dependency | Required for beginner comprehension and inclusive access |
| Beginner training-principles literacy | first-slice candidate | Useful only where it supports exercise literacy without prescribing plans |
| Search and equipment lookup | first-slice candidate | Needed for in-gym discovery, but exact UX belongs in spec |
| Comprehension checks | first-slice candidate | Supports falsifiability, but exact interaction can be staged |
| Supplemental community video | deferable follow-up | Useful later, not source of truth |
| Constrained AI Q&A | separate implementation slice | Requires stable reviewed content and safety guardrails |
| Personalized workout generator | separate proposal | Moves into prescription and higher safety burden |
| Coach dashboard | deferable follow-up | Not needed for beginner exercise literacy |
| Camera-based form analysis | separate proposal | High privacy, safety, and technical risk |
| Injury rehab pathways | out of scope | Requires clinical governance beyond current vision |
| Advanced athlete programming | out of scope | Not aligned with beginner-first scope |

## Open Questions

- What implementation stack, package manager, runtime, and hosting model should the first build use?
- Should reviewed content live as repository files, CMS-managed content, generated static data, or another storage model?
- What exact schema shape should represent locale-aware fields, review metadata, SVG media, taxonomy, and safety notes?
- What minimum validation tooling should exist before the first content cards are accepted?
- Who owns maintainer and security contact addresses before public contribution begins?
- Which exact 40-60 exercises are in the first reviewed pilot?
- Who will own the legal-review relationship and budget approval before public beta?

These questions do not block proposal review. They should be resolved in specs, architecture, and review-governance artifacts before implementation.

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-26 | Recommend a structured exercise-literacy platform | Best fit for beginner understanding, safety, reviewability, and current vision | Static-only encyclopedia; AI-first chatbot |
| 2026-06-26 | Treat AI as a later constrained layer | Reduces hallucination and safety risk | AI-first assistant |
| 2026-06-26 | Prioritize 40-60 reviewed exercises over a large database | Improves quality, comprehension testing, and review cadence | Hundreds of shallow entries |
| 2026-06-26 | Use reviewed text and SVG step cards as source of truth | Matches current vision and keeps media diffable, accessible, and language-neutral | Video-first launch |
| 2026-06-26 | Keep training principles literacy bounded | Helps beginners interpret exercise cards without turning GymPrimer into a workout planner | Full training program curriculum |
| 2026-06-26 | Stage legal, licensing, and disclaimer work | Keeps early contribution posture clear while reserving counsel review for public beta | CLA-first approach; public beta without terms/privacy review |

## Next Artifacts

1. Proposal review for this artifact.
2. Content and schema spec covering exercise cards, locale-aware fields, taxonomy, review metadata, SVG media, and validation rules.
3. Safety and governance spec covering disclaimers, stop rules, excluded use cases, tiered review, escalation language, and incident thresholds.
4. Contribution and licensing spec covering Apache 2.0 code licensing, CC BY 4.0 content licensing, DCO sign-offs, content attribution, and no-CLA rationale.
5. Public-beta legal operations artifact covering Terms of Use, Privacy Policy, attorney review, and incident response.
6. UX spec covering exercise pages, search, equipment lookup, glossary, comprehension checks, and accessibility expectations.
7. Architecture package after the specs stabilize, covering content storage, validation pipeline, review workflow, frontend, analytics, media boundaries, licensing boundaries, and optional AI boundary.
8. Test specification mapping schema, content validation, accessibility, safety refusal, comprehension, review-currency, licensing, and incident-response checks.

## Follow-on Artifacts

- Proposal review: `docs/changes/beginner-fitness-exercise-education-platform/reviews/proposal-review-r1.md`
- Content and schema spec: `specs/content-schema.md`

## Readiness

This proposal is accepted as product direction after clean proposal review.

It is ready to feed downstream specs. It is not ready for architecture, planning, implementation, public release, or medical/legal reliance until the required specs are written and reviewed.
