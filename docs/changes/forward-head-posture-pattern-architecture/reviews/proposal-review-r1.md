# Proposal Review R1: Forward Head Posture Pattern Architecture

## Result

- Skill: proposal-review
- Review status: changes-requested
- Material findings: PR-FHP-1, PR-FHP-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/forward-head-posture-pattern-architecture/reviews/proposal-review-r1.md`
- Review log: `docs/changes/forward-head-posture-pattern-architecture/review-log.md`
- Review resolution: `docs/changes/forward-head-posture-pattern-architecture/review-resolution.md`
- Open blockers: PR-FHP-1 and PR-FHP-2 must be resolved before spec relies on this proposal
- Immediate next stage: isolated stop

## Material Findings

## Finding PR-FHP-1

- Finding ID: PR-FHP-1
- Severity: major
- Location: `docs/proposals/2026-06-30-forward-head-posture-pattern-architecture.md:443`
- Evidence: The proposal has a formal `Initial Intent Preservation` table, but the latest user decisions are recorded only in `Resolved Decisions`: use the title "Forward Head Posture", select five detailed exercises, gate README promotion on the full pattern set, and automatically check exercise-link and image-asset existence. Those user goals are not classified with an initial-goal treatment enum in the preservation table.
- Required outcome: Add the latest user decisions to `Initial Intent Preservation` with explicit treatments, using the proposal-review enum values such as `in scope` or `deferred follow-up`.
- Safe resolution path: Add rows for the title decision, selected five-exercise complete loop, broader collected exercise list, README pattern-set promotion gate, and automated link/image existence checks. Point each row to `Resolved Decisions`, `Scope Budget`, `Decision Log`, or `Testing and Verification Strategy` as applicable.
- needs-decision rationale: none

## Finding PR-FHP-2

- Finding ID: PR-FHP-2
- Severity: major
- Location: `docs/proposals/2026-06-30-forward-head-posture-pattern-architecture.md:323`, `docs/proposals/2026-06-30-forward-head-posture-pattern-architecture.md:246`, `docs/proposals/2026-06-30-forward-head-posture-pattern-architecture.md:477`
- Evidence: The proposal makes five corresponding exercise pages a `same-slice dependency`, and the complete-loop rule says each detailed exercise option must link an existing page or create one in the same reviewed implementation slice. However, `Architecture Impact` lists only the pattern page, media, provenance, source index, tests, checker, and lifecycle artifacts. It does not name the five exercise page paths, their source requirements, or their validation surface. The recommended four-source set supports red flags, posture uncertainty, shoulder/scapular context, and general resistance-training framing, but not necessarily exercise-specific technique, muscle, and safety claims for chin-nod/deep-neck-flexor awareness, thoracic extension, wall-slide, prone Y/T, and band pull-apart.
- Required outcome: Clarify whether the first implementation slice creates five exercise pages, links to existing exercise pages, or keeps some selected exercises as pattern-only annotations until later. If the five pages are same-slice dependencies, enumerate expected page paths and add their citation, media, and validation obligations to architecture impact and testing strategy. If they are not same-slice dependencies, reclassify them in the scope budget and revise the complete-loop rule accordingly.
- Safe resolution path: Choose one of two paths before spec. Path A: same-slice exercise pages; add exact `exercises/...md` paths, source-support expectations for exercise instruction and safety claims, page-contract tests, link checks, and privacy/media checks. Path B: pattern-only proof slice; limit detailed annotations to existing linked exercise pages and move new exercise pages into a separate implementation slice with follow-up routing.
- needs-decision rationale: Owner decision is needed at proposal/spec boundary because it changes implementation size, source obligations, validation scope, and whether the first slice is a pattern-page proof or a pattern-plus-five-exercise-pages proof.

## Review Dimensions

- Problem clarity: pass. The proposal clearly names the problem: one strong APT page and a template do not yet make a reusable pattern architecture.
- User value: pass. The beginner value is concrete: explain forward head posture without diagnosis, alarmism, or corrective-routine promises.
- Option diversity: pass. The proposal compares awareness-only, implicit-template, corrective-routine, reusable-architecture, and alternate-pattern options.
- Decision rationale: pass. Option D follows the stated criteria and rejects posture-correction routine framing for vision fit.
- Scope control: concern. PR-FHP-1 and PR-FHP-2 show that recent decisions and same-slice exercise obligations need clearer classification.
- Architecture awareness: concern. The proposal names spec, architecture, template, media, provenance, and tests, but omits the five exercise pages from architecture impact despite making them same-slice dependencies.
- Testability: concern. Link and image existence are testable, but exercise-page creation/source coverage must be made explicit before the spec can map tests cleanly.
- Risk honesty: concern. The risks name prescription and overconfidence, but do not yet name the delivery/source risk introduced by five detailed exercise pages.
- Rollout realism: concern. The README promotion gate is realistic, but the first implementation slice is too ambiguous between one pattern page and a pattern-plus-exercise bundle.
- Readiness for spec: block. The proposal is close, but PR-FHP-1 and PR-FHP-2 should be resolved before downstream spec work relies on it.

## Scope Preservation Review

- Scope-preservation result: changes requested. Earlier goals are mostly preserved, but the latest user decisions must be added to the formal `Initial Intent Preservation` table so downstream reviewers do not have to infer their treatment from `Resolved Decisions`.

## Recommended Proposal Edits

- Add `Initial Intent Preservation` rows for:
  - Use "Forward Head Posture" as the page title.
  - Select five detailed exercises for the complete loop.
  - List all collected exercises in the pattern document while limiting detailed treatment to the selected five.
  - Gate README promotion on the full approved pattern set.
  - Automatically check exercise-link existence and image-asset existence in the first slice.
- Resolve the same-slice exercise ambiguity by either:
  - naming exact same-slice exercise page paths and source/test obligations, or
  - moving new exercise pages to a separate implementation slice and limiting the first slice to existing exercise links.
- Add a risk or rollout note for exercise-page scope growth and source coverage.
- Align `Architecture Impact`, `Testing and Verification Strategy`, `Scope Budget`, and `Next Artifacts` after the exercise-scope decision.

## Recommendation

- Recommendation: changes requested. Do not move this proposal into spec yet. The direction fits the current vision and is strategically sound, but the proposal needs a small revision pass to preserve the latest user decisions formally and clarify whether the first slice includes five new exercise pages with their own source and validation obligations. This review is isolated; no automatic downstream handoff is implied.
