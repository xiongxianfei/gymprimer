# Plan Review R1: Repository Layout Normalization

## Result

- Skill: plan-review
- Review status: changes-requested
- Material findings: PR-RLN-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/repository-layout-normalization/reviews/plan-review-r1.md`
- Review log: `docs/changes/repository-layout-normalization/review-log.md`
- Review resolution: `docs/changes/repository-layout-normalization/review-resolution.md`
- Open blockers: PR-RLN-1
- Immediate next stage: plan revision

## Review Dimensions

| Dimension | Verdict |
| --- | --- |
| self-contained context | pass |
| source alignment | pass |
| milestone size | pass |
| sequencing | block |
| scope discipline | pass |
| validation quality | concern |
| TDD readiness | block |
| risk coverage | pass |
| architecture alignment | pass |
| operational readiness | concern |
| plan maintainability | pass |

## Findings

### PR-RLN-1 - Plan assigns test-spec authoring to an implementation milestone

- Finding ID: PR-RLN-1
- Severity: blocker
- Location: `docs/plans/2026-06-29-repository-layout-normalization.md`, M2 "Files/components likely touched" and "Requirements covered"
- Evidence: The plan correctly states that test-spec and test-spec-review are required before implementation, but M2 lists `specs/repository-layout-normalization.test.md` as a file likely touched "after test-spec stage" and assigns AC3 to the implementation milestone. The workflow requires test-spec authoring and review before implementation, so an implementation milestone must not own creation or revision of the test-spec artifact.
- Required outcome: Move test-spec ownership out of implementation milestones. The plan should state that `specs/repository-layout-normalization.test.md` is created in the downstream `test-spec` stage after clean plan-review, and implementation milestones consume that approved test spec.
- Safe resolution path: Remove `specs/repository-layout-normalization.test.md` from M2's implementation file list, remove AC3 from implementation milestone ownership, and add a pre-implementation dependency or handoff note that test-spec maps R1-R25 and EC1-EC9 before M1 starts.
- needs-decision rationale: none

## Additional Notes

- The plan otherwise aligns with the approved spec and architecture: dependency inventory precedes moves, validation tooling precedes broad migration, content path moves are separated from media/historical cleanup, and rollback paths are present.
- Validation commands are appropriately concrete, but the exact scope of historical references versus active references should be refined in test-spec and implementation proof.
