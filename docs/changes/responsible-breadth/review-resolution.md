# Review Resolution: Responsible Breadth

## Status

closed

## Findings

| Finding ID | Review | Status | Required owner action |
| --- | --- | --- | --- |
| PR-RB-1 | `docs/changes/responsible-breadth/reviews/proposal-review-r2.md` | resolved | Resolved by `docs/changes/responsible-breadth/reviews/proposal-review-r3.md`. |
| SR-RB-1 | `docs/changes/responsible-breadth/reviews/spec-review-r1.md` | resolved | Resolved by `docs/changes/responsible-breadth/reviews/spec-review-r2.md`. |
| TSR-RB-1 | `docs/changes/responsible-breadth/reviews/test-spec-review-r1.md` | resolved | Resolved by lifecycle/status and handoff normalization in `docs/plans/2026-06-29-responsible-breadth.md`, `docs/plan.md`, and `docs/changes/responsible-breadth/change.yaml`. |

## Resolution notes

- 2026-06-29: Opened PR-RB-1 from proposal-review R2. The proposal handles `VISION.md` and ADR conflicts but omits the required constitution amendment path.
- 2026-06-29: Resolved PR-RB-1 in proposal-review R3 after the proposal added the constitution conflict, constitution same-slice dependency, constitution-first next artifact, governance-risk mitigation, decision-log entry, and readiness blocking language.
- 2026-06-29: Opened SR-RB-1 from spec-review R1. Responsible Breadth spec needs explicit compatibility with the existing approved Markdown-first spec before approval.
- 2026-06-29: Addressed SR-RB-1 for spec-review R2 by adding an explicit same-rank compatibility contract to the Responsible Breadth spec and a reciprocal compatibility note to the Markdown-first spec.
- 2026-06-29: Resolved SR-RB-1 in spec-review R2. No material findings remain open.
- 2026-06-29: Opened TSR-RB-1 from test-spec-review R1. The plan-review record is approved, but the plan artifact still says draft, plan not yet reviewed, next stage plan-review, and ready only for plan-review.
- 2026-06-29: Resolved TSR-RB-1 by normalizing only lifecycle/status and handoff text in the plan, plan index, and change metadata. Milestone scope, validation obligations, requirements, and test mappings were not changed.

## Test-spec-review R1 resolution

### TSR-RB-1 - Plan lifecycle state contradicts approved plan-review record

Resolution: resolved.

Owner action completed:

- Updated `docs/plans/2026-06-29-responsible-breadth.md` so status, lifecycle state, current handoff, and readiness reflect plan-review R1 approval, the drafted test spec, and the need for test-spec-review R2.
- Updated `docs/plan.md` so the plan index reflects the same current state.
- Updated `docs/changes/responsible-breadth/change.yaml` so routing points back to test-spec-review.
- Preserved milestone scope, validation obligations, requirements, and test mappings.

Resolution evidence:

- The plan status is now active.
- The current handoff says plan-review R1 approved the plan and test-spec-review R2 is next.
- The plan index and change metadata point to test-spec-review.
- No M1-M4 milestone content, validation commands, requirement coverage, or test-spec mappings were changed.

## Spec-review R1 resolution

### SR-RB-1 - Same-rank compatibility with Markdown-first spec

Resolution: resolved by `docs/changes/responsible-breadth/reviews/spec-review-r2.md`.

Owner action completed:

- Revised `specs/responsible-breadth.md` to state exactly how it relates to `specs/markdown-first-primer.md`.
- Updated `specs/markdown-first-primer.md` with a compatibility note for Responsible Breadth expanded page classes.
- Preserved the original five-page Markdown-first v0.1 contract.
- Ready to request spec-review R2.

Resolution evidence:

- Added a compatibility section stating that Markdown-first remains governing for the original five-page v0.1 slice.
- Added a rule that Responsible Breadth governs only accepted expanded page classes.
- Added a rule that Responsible Breadth supersedes Markdown-first R21/R22 content-scope restrictions only for Responsible Breadth page classes.
- Added a governing-requirements matrix.
- Added treatment of prior v0.1 exclusions, distinguishing education from diagnosis, treatment, rehabilitation, and personalized prescription.
- Added a conflict-resolution order for same-rank requirements.
- Added page-class definitions for pattern, condition, programming-principle, program-example, and expanded exercise pages.
- Added compatibility acceptance criteria.
- Added a compatibility note to `specs/markdown-first-primer.md`.

## Proposal-review R2 resolution

### PR-RB-1 - Constitution conflict omitted from amendment path

Resolution: resolved by `docs/changes/responsible-breadth/reviews/proposal-review-r3.md`.

Required owner action:

- Revise `docs/proposals/2026-06-29-responsible-breadth.md` so its governance path starts with `CONSTITUTION.md`.
- Add a same-slice constitution amendment dependency to the scope budget.
- Update risk mitigation, next artifacts, decision log, and readiness to reflect constitution amendment before vision/ADR/spec reliance.
- Request proposal-review R3 after revision.

Safe resolution path:

- Preserve the proposal's strict non-diagnostic and non-prescriptive boundaries.
- Do not weaken the constitution into allowing workout planning, clinical rehabilitation, diagnosis, individualized treatment, or AI-generated source-of-truth content.
- Limit the constitution change to static, citation-based consumer education for patterns, conditions, and programming literacy under the proposal's refusal lines.

Resolution evidence:

- `Vision fit` now states the proposal conflicts with both `CONSTITUTION.md` and `VISION.md`.
- `Vision fit` now states acceptance requires amending both artifacts before ADR, spec, architecture, plan, validation, or content work relies on the expanded scope.
- `Scope Budget` now lists `Constitution amendment` as a `same-slice dependency`.
- `Risks and Mitigations` now starts governance mitigation with `CONSTITUTION.md`.
- `Decision Log` now records the decision to revise constitution-level scope boundaries before relying on vision or ADR changes.
- `Next Artifacts` now routes to proposal-review R3, constitution amendment, vision amendment, ADR supersession, then spec/architecture/plan.
- `Readiness` now blocks any downstream reliance until constitution, vision, and ADR conflicts are resolved in source-of-truth order.
