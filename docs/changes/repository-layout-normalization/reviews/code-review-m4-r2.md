# Code Review M4 R2: Repository Layout Normalization

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/repository-layout-normalization/reviews/code-review-m4-r2.md`, `docs/changes/repository-layout-normalization/review-log.md`, `docs/plans/2026-06-29-repository-layout-normalization.md`, `docs/changes/repository-layout-normalization/change.yaml`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-RLN-M4-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/repository-layout-normalization/reviews/code-review-m4-r2.md`
- Review log: `docs/changes/repository-layout-normalization/review-log.md`
- Review resolution: `docs/changes/repository-layout-normalization/review-resolution.md`
- Reviewed milestone: M4 media and historical-artifact cleanup
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M4 media and historical-artifact cleanup
- Required review-resolution: yes
- Finding IDs: CR-RLN-M4-1
- Verify readiness: not-claimed

## Review Inputs

- Current HEAD before review record: `403461a Record M4 code review findings`
- Prior review record: `docs/changes/repository-layout-normalization/reviews/code-review-m4-r1.md`
- Prior finding disposition: `docs/changes/repository-layout-normalization/review-resolution.md`
- Plan: `docs/plans/2026-06-29-repository-layout-normalization.md`
- Test spec: `specs/repository-layout-normalization.test.md`
- Evidence directory: `docs/changes/repository-layout-normalization/evidence/`
- Change metadata: `docs/changes/repository-layout-normalization/change.yaml`

## Diff Summary

No implementation resolution for CR-RLN-M4-1 was present before this review. The only existing M4 disposition evidence file remains `docs/changes/repository-layout-normalization/evidence/m4-media-and-historical-disposition.md`.

## Findings

### CR-RLN-M4-1 — Still present

- Severity: major
- Location: `specs/repository-layout-normalization.test.md:41`, `docs/changes/repository-layout-normalization/evidence/`
- Evidence: RLN-T7 still names `docs/changes/repository-layout-normalization/evidence/historical-artifact-disposition.md` as the closeout evidence path. `find docs/changes/repository-layout-normalization/evidence -maxdepth 1 -type f -printf '%f\n' | sort` returns only `dependency-inventory.md` and `m4-media-and-historical-disposition.md`; the approved RLN-T7 path still does not exist. `review-resolution.md` still lists CR-RLN-M4-1 as pending.
- Required outcome: align the M4 disposition evidence with the approved RLN-T7 evidence path, or explicitly revise the approved test-spec/plan evidence mapping before relying on the alternate filename.
- Safe resolution path: add or rename the M4 disposition evidence to `docs/changes/repository-layout-normalization/evidence/historical-artifact-disposition.md`, update references in plan/change metadata if needed, rerun the M4 validation set plus `git diff --check`, and request M4 re-review. If the current combined filename is preferred, update `specs/repository-layout-normalization.test.md` and the plan first so RLN-T7 names the chosen path, then rerun validation and re-review.
- needs-decision rationale: none

## Prior Finding Reconciliation

| Finding | R2 status | Evidence |
| --- | --- | --- |
| CR-RLN-M4-1 | still-present | No resolution diff exists. The evidence directory still lacks `historical-artifact-disposition.md`, while `specs/repository-layout-normalization.test.md` still names that path for RLN-T7 closeout evidence. |

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | block | CR-RLN-M4-1 remains: the approved RLN-T7 evidence path is still missing. |
| Test coverage | concern | No new test or evidence change was present to prove the requested path alignment. |
| Edge cases | concern | The named historical-artifact disposition edge case remains unresolved because downstream readers following the proof map still cannot find the expected evidence file. |
| Error handling | pass | No checker or runtime error-handling change was reviewed in this R2 pass. |
| Architecture boundaries | pass | No new architecture changes were introduced after M4 R1. |
| Compatibility | block | Workflow compatibility remains blocked on the mismatch between the test-spec proof map and the actual evidence filename. |
| Security/privacy | pass | Reviewer ran the privacy checker over the new review/lifecycle artifacts; it passed. |
| Derived artifact currency | pass | No generated or derived publication artifacts are introduced by this review. |
| Unrelated changes | pass | No implementation changes were present beyond the prior review record state; two untracked `docs/learn/` files remain outside this review. |
| Validation evidence | concern | `git diff --check` passed, but no M4 resolution validation was available because the finding was not fixed. |

## Direct Proof

Reviewer inspected:

- `rg -n "Current Handoff Summary|CR-RLN-M4-1|historical-artifact-disposition|m4-media-and-historical-disposition|Milestone state|Review status|Next stage" docs/plans/2026-06-29-repository-layout-normalization.md docs/plan.md docs/changes/repository-layout-normalization/review-resolution.md specs/repository-layout-normalization.test.md docs/changes/repository-layout-normalization/change.yaml`
- `find docs/changes/repository-layout-normalization/evidence -maxdepth 1 -type f -printf '%f\n' | sort`
- `git status --short`

CI was not observed.

## Milestone Handoff

M4 remains resolution-needed. The next stage is still review-resolution for CR-RLN-M4-1, followed by M4 re-review after a resolution diff exists. No automatic downstream handoff is made from this isolated code-review request.
