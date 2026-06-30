# Code Review M4 R1: Repository Layout Normalization

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/repository-layout-normalization/reviews/code-review-m4-r1.md`, `docs/changes/repository-layout-normalization/review-log.md`, `docs/changes/repository-layout-normalization/review-resolution.md`, `docs/plans/2026-06-29-repository-layout-normalization.md`, `docs/plan.md`, `docs/changes/repository-layout-normalization/change.yaml`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-RLN-M4-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/repository-layout-normalization/reviews/code-review-m4-r1.md`
- Review log: `docs/changes/repository-layout-normalization/review-log.md`
- Review resolution: `docs/changes/repository-layout-normalization/review-resolution.md`
- Reviewed milestone: M4 media and historical-artifact cleanup
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M4 media and historical-artifact cleanup
- Required review-resolution: yes
- Finding IDs: CR-RLN-M4-1
- Verify readiness: not-claimed

## Review Inputs

- Commit reviewed: `57438c6 M4: migrate media and historical artifacts`
- Plan: `docs/plans/2026-06-29-repository-layout-normalization.md`
- Spec: `specs/repository-layout-normalization.md`
- Test spec: `specs/repository-layout-normalization.test.md`
- Architecture: `docs/architecture/system/architecture.md`
- Checker: `tools/checks/check_markdown_first.py`, `tools/checks/check_privacy.py`
- Tests: `tests/test_repository_layout_normalization.py`, `tests/test_markdown_first_guardrails.py`, `tests/test_responsible_breadth_m1.py`, `tests/test_markdown_first_privacy.py`
- Evidence reviewed: `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md`, `docs/changes/repository-layout-normalization/evidence/m4-media-and-historical-disposition.md`, `docs/changes/repository-layout-normalization/change.yaml`

## Diff Summary

M4 moves promoted raster media from old image-type buckets into subject-co-located paths under `media/exercises/<slug>/` and `media/patterns/<slug>/`, updates Markdown image references and `media/PROVENANCE.md`, removes old media buckets and SVG examples, and removes superseded structured-platform folders, tools, tests, and fixtures from the active tree.

The implementation also updates checker fixtures and privacy fixtures so active validation no longer depends on removed structured-platform or old media-bucket paths.

## Findings

### CR-RLN-M4-1 — M4 historical-disposition evidence uses a different path than the approved proof map

- Severity: major
- Location: `specs/repository-layout-normalization.test.md:41`, `docs/changes/repository-layout-normalization/evidence/m4-media-and-historical-disposition.md:1`
- Evidence: the approved test-spec ownership map names `docs/changes/repository-layout-normalization/evidence/historical-artifact-disposition.md` as RLN-T7 closeout evidence. The M4 implementation records historical disposition inside `docs/changes/repository-layout-normalization/evidence/m4-media-and-historical-disposition.md`, and `find docs/changes/repository-layout-normalization/evidence -maxdepth 1 -type f` shows no `historical-artifact-disposition.md` file. The content appears substantively present, but not at the contract path the proof map names.
- Required outcome: align the M4 disposition evidence with the approved RLN-T7 evidence path, or explicitly revise the approved test-spec/plan evidence mapping before relying on the alternate filename.
- Safe resolution path: add or rename the M4 disposition evidence to `docs/changes/repository-layout-normalization/evidence/historical-artifact-disposition.md`, update references in plan/change metadata if needed, rerun the M4 validation set plus `git diff --check`, and request M4 re-review. If the team prefers the current combined filename, update `specs/repository-layout-normalization.test.md` and the plan first so RLN-T7 names the chosen path, then rerun validation and re-review.
- needs-decision rationale: none

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | concern | The file moves, active stale-path removal, and provenance updates match R8-R10, R13-R20, and R24. CR-RLN-M4-1 prevents clean proof-map alignment for RLN-T7 historical disposition evidence. |
| Test coverage | concern | Reviewer reran the full suite and M4-focused tests passed, but tests do not assert the exact RLN-T7 evidence filename named by the test spec. |
| Edge cases | concern | Active stale-path scans distinguish active surfaces from historical records, but the named evidence-record edge case is not at the expected path. |
| Error handling | pass | Checker failures remain deterministic for stale media buckets, missing provenance, unsupported media, and privacy violations. |
| Architecture boundaries | pass | Media now lives under `media/<content-type>/<slug>/...`; governance remains under `docs/`; old structured-platform implementation folders are removed from the active tree. |
| Compatibility | concern | Active content, tests, tools, and provenance no longer rely on removed paths, but downstream reviewers following the approved RLN-T7 closeout path will not find the expected file. |
| Security/privacy | pass | Reviewer reran the M4 privacy command; it checked 103 files and passed. No secrets or private data were observed in the reviewed outputs. |
| Derived artifact currency | pass | Removed generated structured-platform artifacts are not treated as active derived output; no mdBook or generated publication output is introduced. |
| Unrelated changes | pass | The reviewed diff is scoped to M4 media relocation, historical structured-platform cleanup, checker/test updates, and lifecycle/evidence records. Two untracked `docs/learn/` files remain outside this review. |
| Validation evidence | concern | Reviewer reran the M4 validation commands successfully, but validation evidence does not compensate for the mismatched RLN-T7 evidence path. |

## Direct Proof

Reviewer reran these commands locally:

- `python3 -m unittest discover -s tests` — passed, ran 79 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` — passed, checked 18 Markdown files.
- `rg -n "media/equipment|media/movements|media/supplemental|content/|schemas/|generated/|tools/validation" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools media/PROVENANCE.md` — no matches, exit 1 expected for `rg` no-match.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/repository-layout-normalization tests tools` — passed, checked 103 files.
- `find media/equipment media/movements media/supplemental media/svg content schemas generated tools/validation -maxdepth 0 -print 2>/dev/null || true` — returned no paths.
- `git diff --check` — passed.

Additional reviewer inspections:

- `find media -type f | sort` shows only `media/README.md`, `media/PROVENANCE.md`, subject-co-located exercise images, and the APT pattern image.
- `rg -n '!\[[^]]*\]\(([^)]*media/[^)]*)\)' README.md CONTRIBUTING.md docs/templates exercises patterns conditions principles programs media/PROVENANCE.md` shows active media references using the new subject-co-located paths, except for the template placeholder under `docs/templates/pattern-page.md`.
- `find docs/changes/repository-layout-normalization/evidence -maxdepth 1 -type f -printf '%f\n' | sort` shows `dependency-inventory.md` and `m4-media-and-historical-disposition.md`, not the RLN-T7 path named in the test spec.

CI was not observed.

## Milestone Handoff

M4 is not closed. The next stage is review-resolution for CR-RLN-M4-1, followed by M4 re-review. No automatic downstream handoff is made from this isolated code-review request.
