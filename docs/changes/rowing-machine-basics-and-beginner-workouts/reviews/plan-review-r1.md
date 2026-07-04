# Plan Review R1: Rowing Machine Basics and Beginner Workout Guidance

## Result

- Skill: plan-review
- Review status: changes-requested
- Material findings: PR-RMB-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/plan-review-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Review resolution: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md`
- Open blockers: PR-RMB-1
- Immediate next stage: plan revision
- Isolation: direct review request; no automatic downstream handoff.

## Findings

### PR-RMB-1 - Plan uses a prompt-record path that conflicts with the approved image standard

- Finding ID: PR-RMB-1
- Severity: major
- Location:
  `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`,
  Context and orientation, M3 files/components, and M3 validation commands.
- Evidence: The plan says generated raster prompt records live in
  `docs/ai-prompts/`, lists `docs/ai-prompts/` as an M3 touched surface, and
  includes it in the M3 privacy command. The approved exercise-image standard
  requires generated raster exercise image prompt records under
  `media/prompts/exercises/<exercise-slug>/<asset-stem>.md` unless a downstream
  approved spec or architecture amendment defines a more specific location.
  The approved architecture uses the same `media/prompts/exercises/...`
  prompt-record path.
- Required outcome: The plan must use the approved generated-raster
  prompt-record location before test-spec authoring relies on it.
- Safe resolution path: Revise the plan's generated-raster prompt-record
  references from `docs/ai-prompts/` to
  `media/prompts/exercises/rowing-machine/<asset-stem>.md` or the broader
  approved path shape `media/prompts/exercises/<exercise-slug>/<asset-stem>.md`.
  Update the affected M3 file list and M3 privacy command accordingly. Then
  rerun plan-stage privacy and whitespace checks and route back to
  plan-review R2.
- needs-decision rationale: none.

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| Self-contained context | pass | The plan names the accepted proposal, approved spec, approved architecture review, governing method/image specs, current handoff state, and remaining lifecycle gates. |
| Source alignment | block | PR-RMB-1 conflicts with the approved exercise-image prompt-record path. The rest of the plan aligns with the rowing-machine spec and architecture. |
| Milestone size | pass | M1-M4 are reviewable slices: method boundary, page/source drafting, manual proof/media decision, and final integration evidence. |
| Sequencing | pass | The plan puts method-boundary validation before the page, page drafting before manual proof, optional media after comprehension/source review, and promotion after evidence. |
| Scope discipline | pass | Non-goals preserve no planner, no runtime, no `loaded_carry`, no broad cardio rollout, no medical advice, and no borrowed media. |
| Validation quality | concern | Validation commands are concrete and milestone-specific, but M3 includes the wrong prompt-record directory until PR-RMB-1 is fixed. |
| TDD readiness | concern | M1 and M2 are test-spec-ready, but any media/prompt-record proof map would inherit the wrong prompt-record path unless PR-RMB-1 is corrected first. |
| Risk coverage | pass | Risks cover method over-activation, rowing-program drift, under-sourcing, text-only comprehension gaps, optional media risk, and broad validation surprises. |
| Architecture alignment | block | PR-RMB-1 conflicts with the architecture's generated raster prompt-record container and path contract. No other architecture conflict was found. |
| Operational readiness | concern | The plan records validation commands, manual proof, and recovery paths; operational readiness is blocked only for prompt-record path hygiene. |
| Plan maintainability | pass | The plan has lifecycle markers, requirement mapping, current handoff summary, milestone states, validation notes, decisions, and explicit readiness boundaries. |

## Reviewed Surfaces

- `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
- `docs/plan.md`
- `docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml`
- `docs/proposals/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
- `specs/rowing-machine-basics-and-beginner-workouts.md`
- `specs/exercise-image-standard.md`
- `docs/architecture/system/architecture.md`
- `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/spec-review-r1.md`
- `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/architecture-review-r1.md`
- `AGENTS.md`
- `CONSTITUTION.md`

## Automated Review Invocation Manifest

- Review type: direct lifecycle `plan-review`
- Reviewed artifact: `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
- Upstream artifacts checked: accepted proposal, approved rowing-machine spec,
  approved spec-review R1, approved architecture package, approved
  architecture-review R1, approved exercise-image spec, `AGENTS.md`, and
  `CONSTITUTION.md`
- Downstream action taken: review recorded; no test-spec or implementation was
  invoked

## Readiness

The plan is not ready for test-spec handoff until PR-RMB-1 is resolved and a
follow-up plan-review approves the corrected plan.
