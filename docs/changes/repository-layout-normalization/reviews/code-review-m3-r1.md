# Code Review M3 R1: Repository Layout Normalization

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/repository-layout-normalization/reviews/code-review-m3-r1.md`, `docs/changes/repository-layout-normalization/review-log.md`, `docs/changes/repository-layout-normalization/review-resolution.md`, `docs/plans/2026-06-29-repository-layout-normalization.md`, `docs/plan.md`, `docs/changes/repository-layout-normalization/change.yaml`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-RLN-M3-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/repository-layout-normalization/reviews/code-review-m3-r1.md`
- Review log: `docs/changes/repository-layout-normalization/review-log.md`
- Review resolution: `docs/changes/repository-layout-normalization/review-resolution.md`
- Reviewed milestone: M3 content and project-reference migration
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M3 content/reference migration, M4 media and historical-artifact cleanup
- Required review-resolution: yes
- Finding IDs: CR-RLN-M3-1
- Verify readiness: not-claimed

## Review Inputs

- Commit reviewed: `715366d M3: migrate content paths`
- Plan: `docs/plans/2026-06-29-repository-layout-normalization.md`
- Spec: `specs/repository-layout-normalization.md`
- Test spec: `specs/repository-layout-normalization.test.md`
- Checker: `tools/checks/check_markdown_first.py`
- Tests: `tests/test_repository_layout_normalization.py`, `tests/test_markdown_first_real_pages.py`, `tests/test_markdown_first_mdbook.py`, `tests/test_markdown_first_contract.py`, `tests/test_responsible_breadth_m1.py`
- Evidence reviewed: `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md`, `docs/changes/repository-layout-normalization/change.yaml`

## Diff Summary

M3 moves root red flags to `RED-FLAGS.md`, moves the old first-slice Markdown pages into canonical `principles/` and `exercises/` paths, removes the old content directories, updates promoted content links and tests, and leaves media bucket cleanup to M4. The checker now gates media-bucket enforcement separately from Markdown-path enforcement so M3 can close content migration before M4 moves media.

The implementation also rewrites repository-layout change records and the M1 dependency inventory to remove literal old content-path strings from `docs/changes/repository-layout-normalization`.

## Findings

### CR-RLN-M3-1 — M3 rewrote exact dependency-inventory proof into placeholders

- Severity: major
- Location: `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md:16`, `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md:25`, `docs/changes/repository-layout-normalization/change.yaml:41`
- Evidence: the current M1 dependency inventory records an inventory command over placeholder text such as `the former getting-started directory` instead of the literal old paths that existed before migration. The same file now lists placeholder paths such as `the former getting-started directory/beginner-training-principles.md`. `change.yaml` also records that placeholder command as the M1 validation command. The previous committed version of the same evidence recorded the actual command `rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags|media/equipment|media/movements|media/supplemental|content/|schemas/|generated/" .` and exact rows for `01-getting-started/beginner-training-principles.md`, `02-machines/*.md`, `03-bodyweight/incline-push-up.md`, and `about/red-flags.md`.
- Required outcome: restore or re-establish exact migration proof without making the active stale-path scan depend on erasing historical evidence. M1 inventory and validation metadata must report the actual paths and commands used for the dependency inventory, or a clearly reviewed historical-path allowlist/exclusion must preserve exact historical proof while keeping the M3 stale active-path check deterministic.
- Safe resolution path: restore exact M1 inventory command/path rows and exact M1 validation metadata, then adjust the M3 stale-path validation evidence so it distinguishes active content/reference scans from intentional historical proof records. If the validation command scope changes materially, update the plan/test-spec evidence first; otherwise record the narrowed historical-proof handling in `review-resolution.md`, rerun M3 validation, and request M3 code-review again.

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | block | M3 satisfies the file-move direction, but CR-RLN-M3-1 conflicts with R15/R17 and AC12 because the dependency inventory no longer records exact pre-removal paths. |
| Test coverage | concern | Unit tests pass, but they do not cover preservation of exact historical inventory evidence after the stale-path scan is introduced. |
| Edge cases | concern | The planned risk that historical records may intentionally mention old paths was handled by rewriting evidence rather than by explicit allowlist/exclusion handling. |
| Error handling | pass | Checker behavior for active paths still emits deterministic validation errors; no runtime error path is introduced. |
| Architecture boundaries | pass | Canonical content paths, root red flags, and governance under `docs/` match the approved architecture boundary. |
| Compatibility | concern | The migration leaves the active tree in the intended canonical shape, but audit compatibility for M1/M3 evidence is not reliable until CR-RLN-M3-1 is resolved. |
| Security/privacy | pass | Reviewer reran the privacy check over active content and repository-layout change records; checked 32 files, privacy pass. |
| Derived artifact currency | pass | No generated HTML or derived publication output is introduced as authoritative. |
| Unrelated changes | concern | The broad rewrite of historical review/evidence wording is related to stale-path validation, but it crosses from active reference cleanup into audit-evidence mutation. |
| Validation evidence | block | The recorded M1 inventory command in `change.yaml` is no longer the exact command previously run, and the M3 stale-path no-match proof passes partly because exact historical evidence was rewritten. |

## Direct Proof

Reviewer reran these commands locally:

- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` — passed, checked 18 Markdown files.
- `python3 -m unittest discover -s tests` — passed, ran 141 tests.
- `git diff --check` — passed.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises docs/changes/repository-layout-normalization` — passed, checked 32 files.

CI was not observed.

## Milestone Handoff

M3 is not closed. The next stage is review-resolution for CR-RLN-M3-1, followed by M3 re-review. No automatic downstream handoff is made from this isolated code-review request.
