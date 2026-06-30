# Code Review M2 R1: Repository Layout Normalization

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/repository-layout-normalization/reviews/code-review-m2-r1.md`, `docs/changes/repository-layout-normalization/review-log.md`, `docs/plans/2026-06-29-repository-layout-normalization.md`, `docs/plan.md`, `docs/changes/repository-layout-normalization/change.yaml`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/repository-layout-normalization/reviews/code-review-m2-r1.md`
- Review log: `docs/changes/repository-layout-normalization/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M2 validation tooling and regression tests
- Milestone closeout: closed
- Remaining implementation milestones: M3 content/reference migration, M4 media and historical-artifact cleanup
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Commit reviewed: `2fd6e17 M2: enforce normalized layout paths`
- Plan: `docs/plans/2026-06-29-repository-layout-normalization.md`
- Spec: `specs/repository-layout-normalization.md`
- Test spec: `specs/repository-layout-normalization.test.md`
- Checker: `tools/checks/check_markdown_first.py`
- Tests: `tests/test_repository_layout_normalization.py`

## Diff Summary

M2 adds repository-layout-normalization checks to the existing Markdown-first checker and adds `tests/test_repository_layout_normalization.py` for target-tree fixtures. The implementation does not move real content or media files. Strict normalized-layout checks activate when root `RED-FLAGS.md` exists in the checked repository, which lets M2 prove target behavior before M3 owns the real red-flags move.

The tests cover canonical content paths, root red-flags links, old numbered paths, stale `about/red-flags.md` links, compatibility stubs, subject-co-located raster media, stale provenance asset paths, root-level governance folders, and historical artifact classification.

## Findings

None.

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | pass | M2 implements the validation portion of R15-R20, R23-R25, AC5-AC8, AC11, and AC12 without moving files before M3/M4. |
| Test coverage | pass | `tests/test_repository_layout_normalization.py` directly covers RLN-T1, RLN-T2, RLN-T4, RLN-T5, RLN-T6, RLN-T7 fixture behavior, and RLN-T10 observability. |
| Edge cases | pass | Direct tests cover EC1, EC2, EC3, EC4, EC5, EC8, and historical classification behavior for EC6/EC7/EC9 before final M4 disposition proof. |
| Error handling | pass | Checker failures include path-specific codes such as `old_content_path_active`, `stale_old_path_reference`, `old_media_bucket_reference`, `stale_media_provenance_path`, and `governance_path_not_under_docs`. |
| Architecture boundaries | pass | Governance remains under `docs/`; M2 adds validation tooling only and does not change content scope, source-of-truth rules, or media policy. |
| Compatibility | pass | Strict checks are gated on the normalized root safety file so the current pre-migration tree is not broken before M3. |
| Security/privacy | pass | Reviewer reran `python3 tools/checks/check_privacy.py tools/checks/check_markdown_first.py tests/test_repository_layout_normalization.py docs/changes/repository-layout-normalization docs/plans/2026-06-29-repository-layout-normalization.md docs/plan.md`; result: checked 17 files, privacy pass. |
| Derived artifact currency | pass | No generated output is introduced or made authoritative. |
| Unrelated changes | pass | Reviewed commit changes the checker, repository-layout tests, and repository-layout lifecycle/rationale files only. Two untracked `docs/learn/` files remain outside this review. |
| Validation evidence | pass | Reviewer reran focused tests, full test discovery, diff check, and privacy check. CI was not observed. |

## No-Finding Rationale

The approved M2 scope was validation tooling and regression tests before real path moves. The implementation adds deterministic fixture tests for the post-migration target and extends the existing checker to reject stale old paths, old media buckets, stale provenance paths, compatibility stubs, misplaced governance folders, and unclassified retained historical artifacts once the normalized layout is active.

The one planned M2 command not run as closeout proof, `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`, is owned by M3 in `specs/repository-layout-normalization.test.md` because M3 creates `RED-FLAGS.md` in the real tree. The M2 fixture tests provide direct proof for that target behavior without prematurely moving files.

## Residual Risk

M2 does not prove the real repository tree has been migrated. M3 must move Markdown content and project references, and M4 must move media/provenance plus historical artifacts. Final verification remains unclaimed.
