## Result

- Skill: proposal-review
- Review status: changes-requested
- Material findings: PR-RB-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/responsible-breadth/reviews/proposal-review-r2.md`
- Review log: `docs/changes/responsible-breadth/review-log.md`
- Review resolution: `docs/changes/responsible-breadth/review-resolution.md`
- Open blockers: PR-RB-1
- Immediate next stage: isolated stop; revise proposal before acceptance

## Material Findings

## Finding PR-RB-1

- Finding ID: PR-RB-1
- Severity: high
- Location: `docs/proposals/2026-06-29-responsible-breadth.md` lines 67-87, 107-112, 469, 475-477, and 521-536; `CONSTITUTION.md` lines 7-10, 27, 61, and 97.
- Evidence: The proposal correctly says the direction conflicts with `VISION.md` and requires a vision amendment plus ADR supersession before expanded-scope content is published. It also acknowledges that `CONSTITUTION.md` defines GymPrimer as exercise literacy before workout prescription and says the project must not become a workout planner or clinical rehabilitation product. However, the proposal's `Vision fit`, risks, scope budget, and next artifacts only name `VISION.md` amendment and ADR supersession. `CONSTITUTION.md` is the highest-ranked source of truth, requires higher-ranked artifacts to be updated first or in the same change, and currently says health-adjacent content must avoid active-rehab guidance, posture-correction promises, and injury-specific protocols.
- Required outcome: The proposal must explicitly classify the constitution conflict and include a constitution amendment as a same-slice dependency before it can be accepted or used for downstream specification. The amendment path should preserve the project's non-diagnostic, non-prescriptive boundary while updating constitution-level purpose and health-adjacent rules enough to allow static pattern, condition, and program-literacy education.
- Safe resolution path: Revise the proposal's `Vision fit`, `Risks and Mitigations`, `Scope Budget`, `Next Artifacts`, and `Readiness` sections to say acceptance requires both `CONSTITUTION.md` and `VISION.md` amendments before ADR/spec work relies on the expanded scope. Add a decision-log row for revising constitution-level scope boundaries instead of relying on vision/ADR changes alone. Then request proposal-review R3.
- needs-decision rationale: Owner decision is needed on the exact constitution amendment scope: either revise the constitution to permit the proposed static consumer-education surfaces under strict boundaries, or narrow the proposal to avoid constitution-level conflict.

## Review Dimensions

- Problem clarity: pass. The proposal states the user problem as three unmet beginner needs rather than as a tooling preference.
- User value: pass. The value is concrete: beginners can understand common problems, learn from necessary visuals, and understand basic training structure.
- Option diversity: pass. The proposal compares keeping narrow scope, heavy legal/review scaffolding, citation/red-flag expansion, and interactive symptom routing.
- Decision rationale: pass. Option C follows from the stated non-commercial, Markdown-first, citation-based project shape and rejects heavier or riskier alternatives with reasons.
- Scope control: pass with finding. Non-goals, program boundaries, pattern/condition page contracts, higher PR bar, and review cadence are strong. PR-RB-1 remains because constitution-level scope control is not yet represented in the acceptance path.
- Architecture awareness: pass with finding. Markdown source, derived mdBook, no CMS/API/runtime, and separate `patterns/` and `conditions/` paths are clear. PR-RB-1 remains because the architecture path starts too low in the source-of-truth order.
- Testability: pass. Citation quality, safety routing, source-index validity, scope-boundary proof, media checks, and comprehension proof are reviewable or automatable.
- Risk honesty: pass with finding. The proposal names content, diagnostic, pain-pushing, burnout, source-rot, visual-workload, program-prescription, and governance risks. PR-RB-1 requires naming the constitution conflict inside that governance risk.
- Rollout realism: concern. Page-by-page rollout and first-slice proof are realistic, but downstream sequencing must start with constitution and vision amendments before ADR/spec reliance.
- Readiness for spec: concern. The proposal is close, but PR-RB-1 blocks acceptance and therefore blocks clean spec handoff.

## Scope Preservation Review

- Scope-preservation result: pass. The proposal classifies each initial user goal with allowed treatment values and records broad-scope tradeoffs in a scope budget. No initial user goal disappeared. Deferred and out-of-scope items have rationales and follow-up routing.

## Recommended Proposal Edits

- Recommended edits:
  - In `Vision fit`, state that the direction proposes both a constitution revision and a vision revision, while retaining the exact required vision-fit enum `proposes a vision revision`.
  - Add `Constitution amendment` to the scope budget as a `same-slice dependency`.
  - Update the governance-conflict risk mitigation from "Amend `VISION.md` and supersede the active ADR" to "Amend `CONSTITUTION.md`, amend `VISION.md`, then supersede the active ADR."
  - Add `CONSTITUTION.md` amendment as the first downstream artifact in `Next Artifacts`.
  - Add a decision-log row explaining that constitution-level health-adjacent and workout-planner boundaries must be revised before expanded-scope content can publish.
  - Update readiness to say the proposal is not ready for acceptance until PR-RB-1 is resolved.

## Recommendation

- Recommendation: changes-requested. The direction is strategically sound and the R1 concerns were largely resolved, but the proposal cannot be accepted while it omits the highest-ranked governance artifact from the required amendment path.
- Vision conflict outcome: revise vision, plus revise constitution first or in the same change. This is not an explicit exception request.
- No automatic downstream handoff. This direct proposal-review request remains isolated; the next action is proposal revision for PR-RB-1, then proposal-review R3.
