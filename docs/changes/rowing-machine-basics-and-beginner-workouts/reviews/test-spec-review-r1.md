# Test Spec Review R1: Rowing Machine Basics and Beginner Workout Guidance

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR-RMB-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/test-spec-review-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Review resolution: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md`
- Open blockers: TSR-RMB-1
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
- Stop condition: none

## Findings

## Finding TSR-RMB-1

- Finding ID: TSR-RMB-1
- Severity: major
- Location: `specs/rowing-machine-basics-and-beginner-workouts.test.md`, manual proof cases `RMB-M1` through `RMB-M5`
- Evidence: `RMB-M1` through `RMB-M5` define stable IDs, level, fixture/setup, steps, expected result, failure proof, and automation location. They do not explicitly name automation rationale, required environment, evidence artifact as a separate field, pass condition, failure condition, owning stage, or re-run trigger. The test-spec-review rule requires manual proof to name a stable ID, automation rationale, exact steps, required environment, evidence artifact, pass condition, failure condition, and owning stage.
- Required outcome: Expand every manual proof case into an auditable manual-proof contract with the required metadata.
- Safe resolution path: Update `RMB-M1` through `RMB-M5` to include explicit fields for automation rationale, required environment, evidence artifact, pass condition, failure condition, owning stage, and re-run trigger. Preserve the existing proof record paths, but make the pass/fail and ownership criteria precise enough that implementation and code-review can execute them without guessing. Then rerun test-spec authoring checks and request test-spec-review R2.
- needs-decision rationale: none

## Review Dimensions

| Dimension | Verdict | Notes |
| --- | --- | --- |
| Governing-contract alignment | pass | The proof map follows the approved rowing-machine spec, plan-review R2, method-type boundary, optional-media boundary, and no-runtime architecture. |
| Requirement coverage | pass | R1-R40 are mapped to automated tests, manual proof, or both. |
| Example coverage | pass | E1-E5 are mapped to stable automated or manual proof IDs. |
| Negative and boundary coverage | pass | The proof map covers missing page/sections, deferred and broad method activation, forbidden personalized/clinical/product language, unsafe effort, source gaps, media violations, and compatibility boundaries. |
| Proof-level adequacy | concern | Automated and manual levels are generally appropriate, but the manual proof cases need required metadata. See TSR-RMB-1. |
| Milestone mapping | pass | M1-M4 map to test/proof IDs, command IDs, and evidence artifacts. |
| Command validity | pass | RMB-CMD1 through RMB-CMD15 are classified, owned, milestone-scoped, and include first-required milestone, failure behavior, and evidence artifact. |
| Fixture and data design | pass | Fixtures are local, deterministic, synthetic, and privacy-safe; media fixtures follow existing temporary-root patterns. |
| Manual-proof boundary | concern | Manual checks are justified by semantic source support, comprehension, text-only/media decisions, and visual safety, but lack required manual-proof metadata. See TSR-RMB-1. |
| Observability | pass | The proof map requires stable failure categories, evidence records, validation ledgers, and non-identifying comprehension outcomes. |
| Determinism and isolation | pass | Automated checks are local and network-free; source support is explicitly manual. |
| Scope and non-goals | pass | The proof map avoids performance rowing, personalization, diagnosis, rehab, hosted apps, calculators, trackers, and required images when text-only evidence is sufficient. |
| Execution economics | pass | Focused milestone checks, optional media checks, full-suite smoke, and manual proof are separated by risk and milestone. |
| Traceability | pass | Requirement, example, edge-case, command, milestone, and test/proof IDs are linked consistently. |
| Implementation handoff | block | Implementation cannot proceed until TSR-RMB-1 is resolved and re-reviewed. |

## Reviewed Surfaces

- `specs/rowing-machine-basics-and-beginner-workouts.test.md`
- `specs/rowing-machine-basics-and-beginner-workouts.md`
- `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/spec-review-r1.md`
- `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
- `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/plan-review-r2.md`
- `docs/architecture/system/architecture.md`
- `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/architecture-review-r1.md`
- `docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml`
- `AGENTS.md`
- `CONSTITUTION.md`

## Recommendation

Revise the test spec to add complete manual-proof metadata for `RMB-M1` through
`RMB-M5`, then rerun test-spec-review. No implementation handoff is allowed.
