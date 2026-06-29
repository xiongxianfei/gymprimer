# Proposal: Markdown-First Gym Primer

## Status

accepted

This proposal records an accepted direction-change proposal after `docs/changes/markdown-first-gym-primer/reviews/proposal-review-r2.md`. It does not claim spec readiness, implementation readiness, verification readiness, or compatibility with the current higher-ranked project artifacts until `VISION.md`, `CONSTITUTION.md`, and the superseding ADR are revised.

## Problem

The current project direction has accumulated more governance, validation, and generated-output machinery than the project can justify before it has proven the core content format.

The accepted direction treats GymPrimer as a structured, reviewed content platform: exercise cards, schema validation, expert review states, publication eligibility, generated public output, and possible hosted UI/search. That path is coherent, but it depends on resources the project does not currently have:

- a formal reviewer board;
- stable expert-review obligations;
- enough content to justify generated-output infrastructure;
- enough operational capacity to maintain a hosted site;
- enough implementation maturity to make schema, review routing, lifecycle state, generated output, and tests worth the ongoing complexity.

The immediate risk is not that GymPrimer lacks a website. The risk is that it spends more effort building publication machinery than writing beginner-readable exercise education.

## Goals

- Make Markdown files the primary user-facing product.
- Keep each exercise or principle page readable directly on GitHub.
- Make each card reachable and shareable as a stable repository URL.
- Replace unavailable expert-review promises with citation-based authority until named reviewers exist.
- Back safety-relevant statements with named public sources that readers can verify.
- Narrow the first content scope to lower-risk beginner content: machines, bodyweight movements, easy dumbbell patterns, equipment basics, and general training principles.
- Keep mdBook as optional local and future-publishable HTML output.
- Ship a small real content slice quickly by writing five complete Markdown cards before restructuring the entire repository.
- Keep contribution standards lightweight but real through issues, pull requests, citations, disclaimers, scope discipline, and community review.

## Non-goals

- Do not build a hosted web application in the first slice.
- Do not maintain a formal expert-review board before reviewers exist.
- Do not preserve the old schema, review-state, lifecycle, and generated-public-package design as the primary product direction.
- Do not include barbell squat, deadlift, bench press, Olympic lifting, kettlebell ballistic lifts, plyometrics, sprint programming, or rehab protocols in the first release.
- Do not diagnose pain, injuries, posture disorders, or medical conditions.
- Do not implement camera form analysis, personalized programming, user accounts, progress tracking, AI coaching, CMS workflows, or trainer dashboards.
- Do not make mdBook output the source of truth. Markdown source remains the product; HTML is a derived convenience output.
- Do not add full-card Chinese translation in v0.1. Chinese aliases may be included where useful, but the first content slice is English-only.

## Vision fit

proposes a vision revision

This proposal conflicts with the current `VISION.md` and parts of `CONSTITUTION.md`, which commit GymPrimer to reviewed exercise cards, a locale-aware schema, tiered review metadata, canonical SVG step media, visible reviewer identity, public review history, and equipment-anchored discovery. The proposed direction keeps the repository-native and beginner-literacy commitments, but changes the trust model, distribution model, media expectations, schema posture, and near-term scope.

If accepted, this proposal needs a paired vision and constitution revision before implementation can rely on the new direction.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
| --- | --- | --- |
| Treat `.md` files as the primary product, not a fallback | in scope | Goals; Recommended Direction |
| Use open-source educational repos as precedent | in scope | Context; Options Considered |
| Replace unavailable expert review with citation-based authority | in scope | Goals; Recommended Direction; Testing and Verification Strategy |
| Add prominent disclaimers | in scope | Goals; Expected Behavior Changes; Risks and Mitigations |
| Narrow scope to lower-risk beginner content | in scope | Goals; Non-goals; Scope Budget |
| Keep optional local/static HTML through mdBook | in scope | Recommended Direction; Architecture Impact; Rollout and Rollback |
| Avoid Astro, Hugo, Next.js, and hosted-site complexity | in scope | Non-goals; Options Considered |
| Amend `VISION.md` | in scope | Vision Fit; Next Artifacts |
| Supersede ADR 0002 or the current repository-native reviewed-content ADR | in scope | Next Artifacts |
| Amend or supersede the existing accepted proposal | in scope | Next Artifacts |
| Write three to five cards this week to test the format | in scope | Resolved Direction Decisions; Rollout and Rollback; Readiness |
| Keep Apache 2.0 for project code and CC BY 4.0 for content | in scope | Recommended Direction; Risks and Mitigations |
| Preserve future website possibility | deferred follow-up | Architecture Impact; Scope Budget |
| Preserve formal expert review someday | deferred follow-up | Non-goals; Scope Budget |
| Build full structured validator/public JSON package | rejected option | Options Considered; Decision Log |

## Context

`VISION.md` currently describes GymPrimer as an English-first, locale-aware, reviewed exercise-literacy reference with tiered expert review and canonical illustrated SVG step cards. `CONSTITUTION.md` reinforces that model by requiring the content model to preserve locale-aware fields, English launch content, reviewed exercise cards, tiered review metadata, canonical SVG step media, visible reviewer identity and review date, public review history, and equipment-anchored discovery.

The accepted proposal at `docs/proposals/2026-06-26-beginner-fitness-exercise-education-platform.md` recommends a structured exercise-literacy platform. The accepted ADR at `docs/adr/2026-06-26-repository-native-reviewed-content.md` chooses repository-native reviewed content as the source of truth, with deterministic validation and generated publication-ready output.

This proposal challenges those accepted assumptions because the project has not yet proven that its beginner-facing exercise format works. Markdown-first educational projects are a legitimate delivery model. The `getify/you-dont-know-js` repository delivers a book series through GitHub, and OSSU's computer-science repository uses repository navigation and online resources as a curriculum-style delivery model.

The technical tool choice also fits the proposed direction. mdBook is a utility for creating online books from Markdown files, and `mdbook build` generates a `book` directory containing HTML output.

Fitness content needs tighter safety discipline than typical programming tutorials. WHO and CDC adult activity guidance both combine aerobic activity targets with muscle-strengthening activity on two or more days per week. Mayo Clinic's weight-training guidance emphasizes warm-up, controlled movement, and avoiding rushed lifting. ACSM's 2026 resistance-training update emphasizes that consistency and participation in resistance training matter more for most adults than complex programming variables.

For readability, the project should use plain language. CDC describes plain-language resources as tools for clear communication, and the CDC Clear Communication Index is presented as a research-based tool for developing and assessing public communication materials.

Sources:

- [You Don't Know JS Yet](https://github.com/getify/you-dont-know-js)
- [OSSU Computer Science](https://github.com/ossu/computer-science)
- [mdBook repository](https://github.com/rust-lang/mdBook)
- [mdBook creating a book](https://rust-lang.github.io/mdBook/guide/creating.html)
- [mdBook introduction](https://rust-lang.github.io/mdBook/)
- [WHO: Physical activity](https://www.who.int/initiatives/behealthy/physical-activity)
- [CDC: Adult activity overview](https://www.cdc.gov/physical-activity-basics/guidelines/adults.html)
- [Mayo Clinic: Weight training technique](https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842)
- [ACSM: Resistance training guidelines update](https://acsm.org/resistance-training-guidelines-update-2026/)
- [CDC: Plain language materials and resources](https://www.cdc.gov/health-literacy/php/develop-materials/plain-language.html)
- [CDC Clear Communication Index](https://www.cdc.gov/ccindex/index.html)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)
- [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/deed.en)

## Options Considered

### Option A: Continue the structured reviewed-content platform

Keep the current schema, lifecycle, review-routing, validator, generated public output, and eventual hosted UI/search direction.

Advantages:

- Strong formal governance.
- Clear path to hosted UI and structured search later.
- Good fit if expert reviewers, validators, and publication infrastructure are available.
- Better fit for large-scale content operations.

Drawbacks:

- Too much infrastructure before content-market fit.
- Depends on expert-review resources the project does not currently have.
- Delays the most important proof: whether beginners can learn from the cards.

Disposition: rejected as the near-term primary direction. Preserve only the structure that directly improves Markdown quality.

### Option B: Markdown-first repository only

Make GitHub-rendered Markdown the only product. Do not add generated HTML, schema validation, or static site output.

Advantages:

- Fastest to ship.
- Minimal infrastructure.
- Easy for contributors to understand.
- Directly aligns with book repos and curated curriculum repos.

Drawbacks:

- GitHub navigation can become weak as the library grows.
- Search depends on GitHub's interface.
- Local offline browsing is less polished.
- A future website path may require restructuring.

Disposition: viable, but slightly too austere. Use it as the baseline and add only cheap derived output.

### Option C: Markdown-first repository with optional mdBook HTML

Make Markdown files the source of truth and primary product, while adding mdBook as optional derived output for local browsing and possible GitHub Pages publishing later.

Advantages:

- Keeps source simple and GitHub-readable.
- Adds searchable, navigable static HTML with one build command.
- Avoids hosted app infrastructure.
- Does not require deployment.
- Leaves a clean future path to GitHub Pages.
- Fits tutorial, course, and documentation material better than app frameworks.

Drawbacks:

- Requires maintaining `SUMMARY.md` or equivalent navigation.
- mdBook-flavored Markdown constraints may influence file layout.
- HTML output can tempt the project back toward website product scope if not bounded.

Disposition: recommended.

### Option D: Hosted static site using Astro, Hugo, or Next.js

Build a polished website around the content from the start.

Advantages:

- Better visual control.
- Better SEO and analytics.
- Easier custom UI for exercise categories, filters, and quizzes.
- More polished for non-GitHub users.

Drawbacks:

- Adds frontend framework, build, deployment, routing, styling, and maintenance complexity.
- Pulls attention away from writing cards.
- Creates an operational surface the project does not yet need.
- Makes the repository less obviously usable as the product.

Disposition: rejected for the current phase.

### Option E: AI-assisted exercise explainer

Use AI to answer exercise questions from cards or public sources.

Advantages:

- Conversational learning could help beginners.
- Could explain terms and compare exercises.
- Could later sit on top of citation-backed Markdown content.

Drawbacks:

- Unsafe as a first product for fitness guidance.
- Requires stronger guardrails and source grounding.
- Adds liability and trust risks.
- Does not solve the initial need to create accurate cards.

Disposition: out of scope. Revisit only after the Markdown corpus is stable.

### Option F: Content-only spike before repository restructuring

Write five Markdown cards in a temporary spike directory without changing governance, mdBook, or the active repository layout.

Advantages:

- Tests the card format before changing higher-ranked artifacts.
- Keeps the cost of failure low.
- Lets beginner readers react to real content instead of abstract process.
- Avoids prematurely treating the Markdown-first direction as active source of truth.

Drawbacks:

- Does not resolve source-of-truth, licensing, contribution, and governance conflicts.
- Can create confusion if spike files look like canonical project content.
- Still needs citation, disclaimer, scope, and privacy discipline because fitness content is safety-adjacent.

Disposition: useful as a validation step, but insufficient as the final direction. A non-canonical spike may happen before governance revision; active Markdown-first implementation begins only after the proposal is accepted and higher-ranked artifacts are revised.

## Recommended Direction

Adopt Option C: Markdown-first repository with optional mdBook HTML.

GymPrimer should become a beginner fitness primer delivered as self-contained Markdown files, with optional mdBook output generated from the same files. The source of truth is not a database, generated JSON package, schema, hosted UI, or expert-review workflow. The source of truth is the Markdown corpus plus citations.

The trust model should become:

> This is community-curated educational content summarizing public authoritative sources. It is not medical advice, not personalized coaching, and not expert-reviewed unless a specific page says so with named reviewer evidence.

The project should use citations in place of unavailable expert-review promises. The reader should be able to verify claims through public sources. For example:

- weekly activity targets should cite WHO, CDC, ACSM, or similar public guidance;
- weight-training technique advice should cite Mayo Clinic, ACSM, NSCA, AAOS, or peer-reviewed sources;
- safety stop signs should cite medical or public-health sources;
- "what you should feel" cues should be conservative, framed as beginner orientation, and backed where possible by authoritative instruction.

The first content library should be intentionally narrow.

| Category | Include now | Defer |
| --- | --- | --- |
| Machine exercises | lat pulldown, seated row, chest press, pec deck, leg press, leg extension, hamstring curl, cable face pull | advanced cable variations, high-risk shoulder positions |
| Bodyweight | wall push-up, incline push-up, bodyweight squat to box, dead bug, bird dog, plank, side plank | advanced calisthenics, explosive push-ups |
| Dumbbell basics | goblet squat, dumbbell row, dumbbell floor press, farmer carry, suitcase carry | heavy bilateral barbell patterns |
| Cardio equipment | rowing machine basics, treadmill walking, stationary bike setup | high-intensity sprint protocols |
| Principles | warm-up, controlled reps, progressive overload, RPE/RIR basics, soreness vs pain, weekly balance | periodization, sport-specific programming |
| Safety | disclaimer, stop rules, when to seek professional help | rehab pathways, injury diagnosis, posture-correction protocols |

Resolved direction decisions for v0.1:

| Question | Decision |
| --- | --- |
| Existing repository or clean repository? | Restructure in place on a new branch. Keep prior proposals, ADRs, reviews, plans, and decisions as traceable institutional memory. |
| First language? | English-only v0.1, with Chinese aliases where useful. Do not translate full cards in the first slice. |
| Bilingual structure later? | Use separate locale files or directories, not bilingual sections inside one file. Defer that structure until translation becomes near-term. |
| Citation style? | Use claim-level reference links plus a per-card `Sources` section and global `SOURCES.md`. |
| First five cards? | `01-getting-started/beginner-training-principles.md`, `02-machines/lat-pulldown.md`, `02-machines/seated-row.md`, `02-machines/chest-press.md`, and `03-bodyweight/incline-push-up.md`. |
| Media? | Original simple SVG diagrams only, or no image. Do not use third-party screenshots, stock photos, borrowed public assets, or commercial machine screenshots in v0.1. |
| Licensing? | Apache-2.0 for code/tooling; CC BY 4.0 for written content and original diagrams; explicit inbound contribution terms in `CONTRIBUTING.md`. |
| Old artifacts? | Mark as superseded and archive, not delete. Do not leave old schema/spec/plan/review trails looking active. |
| mdBook timing? | Write the first five GitHub-readable Markdown pages first, then add minimal `book.toml` and `SUMMARY.md` only if it remains trivial and non-blocking. |

Suggested future locale shape, only when translation becomes near-term:

```text
en-US/
  02-machines/
    lat-pulldown.md

zh-Hans/
  02-machines/
    lat-pulldown.md
```

Suggested contributor licensing language:

```md
By submitting a pull request, you agree that:
- code and tooling contributions are provided under Apache-2.0;
- written content, diagrams, and educational materials are provided under CC BY 4.0;
- you have the right to contribute the submitted material;
- you are not submitting copyrighted third-party media unless its license is documented and compatible.
```

Recommended repository shape:

```text
README.md
SOURCES.md
CONTRIBUTING.md
LICENSE
CONTENT_LICENSE.md
book.toml
SUMMARY.md

01-getting-started/
  how-to-use-this-primer.md
  safety-disclaimer.md
  beginner-training-principles.md

02-machines/
  lat-pulldown.md
  seated-row.md
  chest-press.md

03-bodyweight/
  incline-push-up.md

media/
  lat-pulldown/
    movement-phases.svg
```

Recommended card structure:

```md
# Lat Pulldown

> Disclaimer: This is community-curated educational content summarizing public sources. It is not medical advice or personalized coaching.

## What this exercise is for

## Equipment setup

## Muscles involved

## Movement breakdown

### 1. Set up

### 2. Pull

### 3. Pause

### 4. Return

## What you should feel

## Common mistakes

## Easier version

## Harder version

## Safety notes

## Sources

[mayo-weight-training]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842
[cdc-adult-activity]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
```

Every card should stand alone. A reader who lands on `02-machines/lat-pulldown.md` directly from GitHub should not need a site renderer, database, generated index, or app navigation to understand it.

Safety claims need claim-level citations. Global sources are not enough. Each card needs a `Sources` section, and every source reused across multiple cards should also appear in `SOURCES.md`. Reference-style links are preferred over footnotes for v0.1 because they are portable across GitHub-rendered Markdown and mdBook.

## Expected Behavior Changes

After this proposal is adopted and higher-ranked artifacts are revised:

- Users browse the primer through GitHub, a cloned repository, downloaded Markdown files, or optional local mdBook HTML.
- Exercise cards are ordinary `.md` files, not database records.
- The root `README.md` becomes the main navigation and product landing page.
- `SOURCES.md` becomes the global source index.
- Each card includes its own source list.
- Every safety-relevant page includes a prominent disclaimer.
- Trust comes from verifiable citations, not unnamed expert approval.
- Contributors open issues or pull requests against Markdown files.
- Pull request review checks source quality, citation quality, scope, clarity, and disclaimer presence.
- mdBook output is generated for convenience, not treated as the canonical product.
- Barbell, rehab, injury, pain-treatment, and advanced programming content are held out of the first scope.
- v0.1 content is English-only except optional Chinese aliases for exercise names.
- v0.1 media uses original SVG diagrams or no media; no third-party images or commercial machine screenshots are included.

## Architecture Impact

The canonical product would become:

```text
README.md
01-getting-started/*.md
02-machines/*.md
03-bodyweight/*.md
04-dumbbells-and-carries/*.md
05-cardio-equipment/*.md
06-safety-and-scope/*.md
SOURCES.md
media/*
```

The optional generated output would become:

```text
book/
```

or whatever output path mdBook produces.

Components retained:

| Component | Treatment |
| --- | --- |
| Markdown content | core source of truth |
| Relative media files | core source assets |
| Root README navigation | core source of truth |
| `SOURCES.md` | core source of truth |
| `CONTRIBUTING.md` | core contributor contract |
| mdBook | optional derived output |
| GitHub Issues/PRs | community feedback and review channel |
| Privacy scan | lightweight local quality check |
| Link checker | useful local quality check |
| Markdown linter | useful local quality check |

Components removed or deferred:

| Component | Treatment |
| --- | --- |
| Formal review-status lifecycle | remove from near-term product model |
| Publication-status state machine | remove from near-term product model |
| Expert reviewer tiers | remove until named reviewers exist |
| Generated public JSON package | remove or archive as superseded |
| Pagefind/Astro assumptions | remove |
| Hosted site deployment | defer |
| AI assistant | defer |
| CMS/editorial backend | out of scope |

mdBook should be added as a local build convenience:

```sh
mdbook build
```

That command produces static HTML from Markdown. The generated HTML can be opened locally or later published to GitHub Pages.

## Testing and Verification Strategy

Use lightweight, content-centered checks instead of platform-style publication gates.

| Check | Purpose |
| --- | --- |
| Markdown renders on GitHub | confirms the primary product works |
| mdBook build succeeds | confirms optional HTML path |
| Link check passes | catches broken references |
| Source check passes | each card has source section and citations |
| Disclaimer check passes | safety-relevant files include disclaimer |
| Scope check passes | no barbell/rehab/pain-treatment content in first release |
| Media path check passes | relative images resolve |
| Privacy scan passes | no local private paths, secrets, PHI-like examples, or accidental personal data |
| Beginner read test | confirms one or two beginners can understand the card |

The existing plan-review history identified that plain `rg` has wrong semantics for negative-match privacy scans; a clean scan is the passing condition, so privacy scanning should use either negated `rg` or a helper that exits `0` only when forbidden patterns are absent.

For each card:

- every safety claim should have a claim-level source;
- every "do not do X" warning should have a source or be reframed as conservative beginner guidance;
- every source should be listed in the card and reused sources should also appear in `SOURCES.md`;
- sources should be public, stable, and preferably authoritative;
- unsupported coaching claims should be removed or marked as practical cueing, not medical fact.

Citation policy:

| Claim type | Citation requirement |
| --- | --- |
| Safety warning | Claim-level source required |
| Weekly activity guideline | Public-health source required |
| Exercise technique claim | Authoritative instructional source preferred |
| "What you should feel" cue | Cite if framed as anatomy or safety; otherwise label as practical cueing |
| Common mistake | Source preferred; otherwise phrase conservatively |
| Personal coaching opinion | Remove or clearly mark as non-medical practical guidance |

For the first five cards, ask one or two beginner readers:

- What is the exercise for?
- How would you set up the equipment?
- What are the steps?
- What should you feel?
- What would make you stop?
- Which source would you click to verify a safety claim?

This is not formal usability testing. It is the smallest useful proof that the Markdown-first format works.

The first slice is successful only if:

- five Markdown pages render correctly on GitHub;
- every page has a disclaimer;
- every safety-relevant claim has a claim-level source;
- no page covers pain diagnosis, rehab, barbell lifts, advanced programming, or posture-correction protocols;
- at least one beginner can correctly explain the purpose, setup, steps, and stop condition after reading each exercise card;
- mdBook either builds with default configuration or is explicitly deferred because it would require custom plugins, layout churn, or non-trivial styling.

Possible local commands:

```sh
mdbook build
markdownlint "**/*.md"
lychee README.md "01-getting-started/**/*.md" "02-machines/**/*.md"
python tools/checks/check_card_sources.py
python tools/checks/check_disclaimers.py
python tools/checks/privacy_scan.py -- README.md 01-getting-started 02-machines 03-bodyweight
```

The exact tools can change. The important point is that the checks validate Markdown quality, source completeness, disclaimers, link health, local media paths, and privacy safety.

## Rollout and Rollback

Rollout:

1. Revise this proposal with proposal-review feedback.
2. Run proposal-review R2.
3. If accepted, amend `VISION.md` to say the primary product is a Markdown-first, citation-based beginner primer.
4. Amend `CONSTITUTION.md` where it currently requires the old reviewed-schema model.
5. Supersede the accepted ADR that assumes repository-native reviewed content with lifecycle and generated-output gates.
6. Supersede the existing accepted proposal that assumes structured cards, generated output, Pagefind/Astro, or formal review gates.
7. Write a non-canonical first-card spike with five pages: `01-getting-started/beginner-training-principles.md`, `02-machines/lat-pulldown.md`, `02-machines/seated-row.md`, `02-machines/chest-press.md`, and `03-bodyweight/incline-push-up.md`.
8. Add minimal `book.toml` and `SUMMARY.md` only if the five Markdown pages already work on GitHub and mdBook stays trivial.
9. Run source, disclaimer, link, privacy, render, and optional mdBook checks.
10. Ask one or two beginners to read the cards and report confusion.
11. Decide whether to promote the spike into active Markdown-first structure.

A non-canonical first-card spike may be drafted before governance revision to test the format, but it should not be treated as active project source of truth. Mainline Markdown-first implementation begins only after `VISION.md`, `CONSTITUTION.md`, and the superseding ADR are accepted.

Rollback:

- If the Markdown-first format fails, keep the cards as source material, stop mdBook work, and return to structured schema only if there is a clear reason.
- If mdBook adds friction, remove `book.toml` and `SUMMARY.md`, keep GitHub-rendered Markdown as the complete product, and revisit static HTML later.
- Do not revive expert-review promises unless reviewers are actually available.

## Risks and Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Users mistake the primer for medical or personalized coaching | High | Prominent disclaimers in README and safety-relevant files; no diagnosis, rehab, or injury treatment |
| Citation-based authority is weaker than expert review | Medium | Be explicit that content is community-curated; require public authoritative sources; narrow scope |
| Fitness claims become unsupported | High | Require source sections and citation checks; remove unsupported safety claims |
| Scope creeps into rehab or advanced lifting | High | Maintain excluded-content list; reject pull requests outside v1 scope |
| GitHub UX is poor for beginners | Medium | Strong README, numbered directories, optional mdBook output |
| mdBook becomes a website project by stealth | Medium | Treat HTML as derived output only; avoid custom app framework |
| Content becomes inconsistent across cards | Medium | Use a card template and contributor checklist |
| Broken links undermine trust | Medium | Add link checking and periodic source review |
| License confusion between code and content | Medium | Use Apache 2.0 for code/tooling and CC BY 4.0 for written content, with explicit files and contribution terms |
| Images or diagrams have unclear rights | High | Prefer original diagrams or public-domain/appropriately licensed assets; record media source and license |
| Community pull requests introduce bad advice | High | Require citations, scope checks, and maintainer review before merge |
| No formal reviewers means lower credibility | Medium | Do not claim expert review; invite credentialed contributors later with transparent attribution |
| Markdown-only content is less interactive | Low | Use inline self-check questions; defer richer interactivity |
| Local commands become too heavy | Medium | Keep checks small; avoid rebuilding the schema platform |
| Current constitution conflicts with this direction | High | Revise `CONSTITUTION.md` before implementation relies on the Markdown-first trust model |

## Scope budget

| Work item | Treatment | Reason |
| --- | --- | --- |
| Markdown-first source structure | core to this proposal | Defines the new primary product |
| Root README navigation | core to this proposal | GitHub browsing depends on it |
| Self-contained exercise cards | core to this proposal | Main user value |
| Citation-based authority model | core to this proposal | Replaces unavailable expert-review promise |
| Prominent disclaimer model | same-slice dependency | Required for safer fitness education |
| Narrow v1 exercise scope | same-slice dependency | Reduces safety and accuracy risk |
| `SOURCES.md` | same-slice dependency | Makes citations auditable |
| `CONTRIBUTING.md` | same-slice dependency | Defines community pull request standard |
| mdBook optional output | first-slice candidate | Useful and cheap, but not source of truth |
| Lightweight lint/link/source checks | first-slice candidate | Supports maintainability without platform complexity |
| `VISION.md` revision | same-slice dependency | Required because this proposal changes project identity |
| `CONSTITUTION.md` revision | same-slice dependency | Required because current governance mandates the old reviewed-schema model |
| Existing schema/lifecycle/review-routing validator | separate proposal | Belongs to old platform direction |
| Non-canonical first-card spike | first-slice candidate | Useful for format proof before active implementation, but not project source of truth until governance is revised |
| Generated public JSON package | out of scope | Not needed for Markdown-first product |
| Pagefind/Astro stack | out of scope | Too much website complexity |
| Hosted GitHub Pages publication | deferable follow-up | Easy later, not required now |
| Formal expert reviewer board | deferable follow-up | Desirable later, unavailable now |
| Credentialed contributor attribution | deferable follow-up | Useful once actual contributors exist |
| Full Chinese translation | deferable follow-up | Translation doubles review and citation burden before the English card format is proven |
| AI assistant | out of scope | Too risky before corpus stabilizes |
| Rehab/pain/injury content | out of scope | Requires clinical governance |
| Barbell/advanced lifts | out of scope | Higher-risk and harder to explain safely |

## Open Questions

- Who is the initial maintainer empowered to accept citation quality and scope decisions?
- What exact wording should `CONSTITUTION.md` use to permit citation-based authority while preserving safety, no-medical-advice, privacy, and source-of-truth discipline?
- Where should superseded structured-platform artifacts be archived if moving them would create excessive diff churn?

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-27 | Propose treating Markdown files as the primary product | Fastest path to real beginner-readable content; proven repository-first education model | Hosted app first; generated public JSON first |
| 2026-06-27 | Propose citation-based authority instead of expert-review promise | Formal reviewers are not currently available | Unnamed expert approval; formal reviewer board before content exists |
| 2026-06-27 | Propose narrowing v1 to lower-risk beginner content | Fitness safety requires conservative scope | Barbell lifts, rehab, pain correction, advanced programming |
| 2026-06-27 | Propose keeping mdBook as optional derived output | It adds searchable static HTML without requiring deployment | Astro, Hugo, Next.js, CMS |
| 2026-06-27 | Propose community issues and pull requests as feedback channel | Fits open-source Markdown content model | Gatekept review workflow |
| 2026-06-27 | Propose superseding old platform assumptions | Current review path is too heavy for the project's constraints | Continuing schema/reviewer/generated-output platform as v1 |
| 2026-06-27 | Resolve v0.1 first slice as five English-only pages with optional Chinese aliases | Proves the card format without translation overhead | Bilingual first slice; Chinese-only first slice; broad content launch |
| 2026-06-27 | Resolve citations as claim-level reference links plus per-card and global source lists | Citation authority replaces unavailable expert review, so source traceability has to be page-local | Global-only source index; footnote-only style |
| 2026-06-27 | Resolve v0.1 media as original SVG only or no image | Avoids licensing and equipment-specific confusion | Public web images; screenshots; stock photos; borrowed assets |
| 2026-06-27 | Resolve old artifact disposition as supersede and archive, not delete | Preserves institutional memory while preventing stale implementation guidance | Delete old artifacts; leave old artifacts active |
| 2026-06-27 | Allow a non-canonical content spike before full governance revision | Lets the project test real Markdown pages without treating them as active source of truth | Direct implementation; waiting for all downstream artifacts before writing any sample content |

## Next Artifacts

1. Run proposal-review R2 for this revised proposal.
2. Amend `VISION.md`.
   - Replace expert-review-first platform language with Markdown-first, citation-based authority.
   - State that optional HTML is derived from Markdown, not the product source.
   - State that v1 scope is lower-risk beginner education only.
3. Amend `CONSTITUTION.md`.
   - Remove or revise governance rules that require the old reviewed-schema and tiered-review model as the only valid content model.
   - Preserve the safety, privacy, source-of-truth, workflow, and no-medical-advice constraints.
4. Supersede `docs/adr/2026-06-26-repository-native-reviewed-content.md`.
   - Keep the old ADR as historical record.
   - Add a new ADR for Markdown-first, citation-based authority.
   - Record the shift from expert tiers and generated-output gates to citations-as-trust.
5. Supersede or amend `docs/proposals/2026-06-26-beginner-fitness-exercise-education-platform.md`.
   - Remove Pagefind/Astro assumptions.
   - Remove formal review-state lifecycle from v1.
   - Replace structured card platform with self-contained Markdown cards.
6. Create a card template.
   - Define headings, disclaimer, source section, citation expectations, safety wording, and scope boundaries.
7. Create contributor guidance.
   - Define accepted sources, citation rules, pull request checklist, media licensing, and out-of-scope content.
8. Create a first-card spike.
   - Draft the five selected English-only cards and test them with beginner readers.

## Follow-on Artifacts

None yet

## Readiness

This revised proposal is ready for proposal-review R2 as a direction-change proposal.

It is not ready for implementation because it conflicts with current `VISION.md`, `CONSTITUTION.md`, the accepted proposal, and the accepted repository-native reviewed-content ADR. If the proposal is accepted, those higher-ranked artifacts need to be revised or superseded before Markdown-first implementation work proceeds.

Resolved direction decisions now cover repository disposition, first language, future bilingual layout, citation style, first five cards, media policy, licensing posture, old artifact disposition, and mdBook timing. Remaining questions are governance wording and maintainer authority, not product-direction blockers.

The immediate next stage is:

```text
proposal revision -> proposal-review R2 -> VISION.md / CONSTITUTION.md revision -> superseding ADR -> first-card spike
```

Do not proceed directly to spec. The proposal intentionally changes project identity, trust model, governance, and source of truth, so governance alignment comes before mainline implementation.
