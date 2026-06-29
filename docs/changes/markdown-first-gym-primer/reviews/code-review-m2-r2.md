# Code Review M2 R2: Markdown-First Gym Primer

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/markdown-first-gym-primer/reviews/code-review-m2-r2.md`, `docs/changes/markdown-first-gym-primer/review-log.md`, `docs/changes/markdown-first-gym-primer/review-resolution.md`, `docs/plans/2026-06-27-markdown-first-gym-primer.md`, `docs/plan.md`, `docs/workflows.md`, `docs/changes/markdown-first-gym-primer/change.yaml`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/code-review-m2-r2.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Reviewed milestone: M2. Markdown-First Check Tooling and Test Fixtures
- Milestone closeout: closed
- Remaining implementation milestones: M3, M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: CR-M2-1 resolution in `SOURCES.md`, `tools/checks/check_markdown_first.py`, `tests/test_markdown_first_citations.py`, citation fixtures, and workflow metadata.
- Tracked governing branch state: working tree on `proposal/markdown-first-gym-primer`; artifacts are uncommitted, so this review is milestone-local and does not claim branch readiness.
- Governing artifacts: `specs/markdown-first-primer.md`, `specs/markdown-first-primer.test.md`, `docs/plans/2026-06-27-markdown-first-gym-primer.md`, `docs/changes/markdown-first-gym-primer/reviews/code-review-m2-r1.md`, and `docs/changes/markdown-first-gym-primer/review-resolution.md`.
- Validation evidence rerun during review:
  - `python3 -m unittest tests.test_markdown_first_citations`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py tests/fixtures/markdown-first/citations/missing-global-source-id.md; test $? -eq 1`
  - `python3 tools/checks/check_markdown_first.py tests/fixtures/markdown-first/citations/reused-local-a/shared.md tests/fixtures/markdown-first/citations/reused-local-b/shared.md; test $? -eq 1`
  - `python3 tools/checks/check_markdown_first.py tests/fixtures/markdown-first/citations/source-url-mismatch.md; test $? -eq 1`
  - `python3 tools/checks/check_markdown_first.py --help`
  - `python3 tools/checks/check_privacy.py -- README.md CONTRIBUTING.md SOURCES.md CONTENT_LICENSE.md`
  - `if command -v markdownlint >/dev/null 2>&1; then markdownlint "**/*.md"; else printf 'markdownlint not installed\n'; fi`
  - `git diff --check`

## Diff summary

The CR-M2-1 resolution turns `SOURCES.md` into an executable global source index by adding reference-style definitions. `check_markdown_first.py` now loads that index, requires cited IDs to have page-local definitions, requires non-local IDs to exist in `SOURCES.md`, preserves explicit `local-<page-slug>-...` IDs, detects local IDs reused across pages, detects reused non-local IDs missing from `SOURCES.md`, and detects page/global URL mismatches.

The test suite now includes direct fixtures and tests for missing global source IDs, valid global source IDs, valid page-local IDs, reused local IDs, reused non-local IDs missing from `SOURCES.md`, and URL mismatches.

## Findings

No blocking or required-change findings.

## Finding reconciliation

| Finding ID | Prior status | R2 result | Evidence |
| --- | --- | --- | --- |
| CR-M2-1 | open from `code-review-m2-r1` | resolved | The missing-source fixture now exits nonzero with `source_id_missing_from_sources_md`; source-index, reused-local, reused-missing-global, and URL-mismatch tests pass. |

## Checklist coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | T4's global source-index requirement is now implemented and tested without making `SOURCES.md` replace page-local definitions. |
| Test coverage | pass | Citation tests cover missing global ID, valid global ID, valid local ID, reused local ID, reused missing global ID, and URL mismatch. Full Markdown-first suite passed with 29 tests. |
| Edge cases | pass | Direct checks confirmed the adversarial missing global ID, reused local ID, and URL mismatch paths return nonzero with stable rule codes. |
| Error handling | pass | Missing `SOURCES.md` is a setup error; validation findings return exit `1`; help and privacy commands exit successfully. |
| Architecture boundaries | pass | The resolution keeps local standard-library validation and does not revive old structured validators, generated JSON, mdBook, or semantic citation review. |
| Compatibility | pass | Pages still require page-local reference definitions for standalone GitHub rendering; global `SOURCES.md` is an index. |
| Security/privacy | pass | No source text or secret values are echoed by the privacy checker; no private data was introduced in fixtures. |
| Derived artifact currency | pass | No derived artifacts are generated or claimed current. |
| Unrelated changes | pass | The rereview scope is limited to M2 source-index validation, fixtures, and workflow evidence. |
| Validation evidence | pass | Required M2 commands and CR-M2-1 adversarial checks were rerun and passed. `markdownlint` remains unavailable and conditionally deferred. |

## No-finding rationale

CR-M2-1 is resolved because non-local cited source IDs now require `SOURCES.md` membership while page-local IDs remain possible only through the explicit local namespace and single-page usage. The added tests directly cover the prior adversarial hole and adjacent boundary cases.

## Residual risks

- The checker remains a deterministic minimum gate, not semantic citation review. Manual citation review remains assigned to M3.
- `markdownlint` is not installed, so CMD6 remains a documented conditional deferral.
- This review closes M2 only; M3, M4, final verification, CI claims, branch readiness, and PR readiness are not claimed.

## Milestone handoff state

- Reviewed milestone: M2
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining in-scope implementation milestones: M3, M4
- Next stage: implement M3
- Final closeout readiness: not-ready; M3-M4 implementation, code review, explain-change, verify, and PR handoff remain.
