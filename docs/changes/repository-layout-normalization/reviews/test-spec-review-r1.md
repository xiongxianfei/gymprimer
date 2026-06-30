# Test Spec Review R1: Repository Layout Normalization

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR-RLN-1, TSR-RLN-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/repository-layout-normalization/reviews/test-spec-review-r1.md`
- Review log: `docs/changes/repository-layout-normalization/review-log.md`
- Review resolution: `docs/changes/repository-layout-normalization/review-resolution.md`
- Open blockers: TSR-RLN-1, TSR-RLN-2
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
- Stop condition: implementation must not start until the test spec is revised and approved by test-spec-review.

## Review Dimensions

| Dimension | Verdict |
| --- | --- |
| Governing-contract alignment | pass |
| Requirement coverage | pass |
| Example coverage | pass |
| Negative and boundary coverage | pass |
| Proof-level adequacy | concern |
| Milestone mapping | block |
| Command validity | concern |
| Fixture and data design | pass |
| Manual-proof boundary | block |
| Observability | pass |
| Determinism and isolation | pass |
| Scope and non-goals | pass |
| Execution economics | pass |
| Traceability | concern |
| Implementation handoff | block |

## Findings

## Finding TSR-RLN-1

- Finding ID: TSR-RLN-1
- Severity: material
- Location: `specs/repository-layout-normalization.test.md`, `Test cases`; `Security/privacy verification`; `Performance checks`
- Evidence: Test cases T1-T11 name stable test IDs and automation locations, but they do not assign each test to an owning milestone or owner. The only command-level text is a generic planned privacy command and a final note that proof should include `python3 -m unittest discover -s tests` plus targeted checker commands. The approved plan separates M1 dependency inventory, M2 validation tooling, M3 content/reference migration, and M4 media/historical cleanup, so implementation needs to know which RLN-T tests and commands must exist at each milestone.
- Required outcome: The test spec must add a milestone/ownership map for RLN-T1 through RLN-T11 and the planned validation command set, including classification, owning milestone, first meaningful execution, and failure behavior.
- Safe resolution path: Add a "Test ownership map" and "Planned validation command ownership" section similar to the existing workflow style. Map manual inventory proof to M1, checker/fixture tests to M2, real content/reference migration proof to M3, media/historical cleanup proof to M4, and final lifecycle/validation ledger checks to closeout. Do not move test-spec authoring into implementation milestones.
- needs-decision rationale: none

## Finding TSR-RLN-2

- Finding ID: TSR-RLN-2
- Severity: material
- Location: `specs/repository-layout-normalization.test.md`, `Test cases` T3, T7, T10, T11; `Fixtures and data`; `Manual QA checklist`
- Evidence: The test spec lists three manual proof artifact paths and several manual test cases, but the manual proof records do not have stable proof IDs, owners, owning stages, automation rationale, required environment, required fields, pass conditions, failure conditions, rerun triggers, or privacy statements. The test-spec-review workflow requires manual proof to be exact, justified, owned, evidenced, and bounded to cases where automation is impractical.
- Required outcome: The test spec must define bounded manual proof records with stable IDs and enough required fields that implementation and review can create and assess them without guessing.
- Safe resolution path: Add a "Manual proof ownership" section for dependency inventory, historical artifact disposition, final validation ledger, and optional command-output/observability review. Each proof should name owner role, owning milestone, evidence artifact, automation rationale, required environment, exact steps or required fields, pass condition, failure condition, rerun trigger, and privacy statement.
- needs-decision rationale: none
