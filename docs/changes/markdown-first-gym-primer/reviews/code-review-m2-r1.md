# Code Review M2 R1: Markdown-First Gym Primer

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/markdown-first-gym-primer/reviews/code-review-m2-r1.md`, `docs/changes/markdown-first-gym-primer/review-log.md`, `docs/changes/markdown-first-gym-primer/review-resolution.md`, `docs/plans/2026-06-27-markdown-first-gym-primer.md`, `docs/plan.md`, `docs/workflows.md`, `docs/changes/markdown-first-gym-primer/change.yaml`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-M2-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/code-review-m2-r1.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Reviewed milestone: M2. Markdown-First Check Tooling and Test Fixtures
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M2, M3, M4
- Required review-resolution: yes
- Finding IDs: CR-M2-1
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: M2 working-tree changes under `tools/checks/`, `tests/fixtures/markdown-first/`, M2 `tests/test_markdown_first_*.py`, and workflow handoff metadata.
- Tracked governing branch state: working tree on `proposal/markdown-first-gym-primer`; implementation artifacts are uncommitted, so this review is milestone-local and does not claim branch readiness.
- Governing artifacts: `specs/markdown-first-primer.md`, `specs/markdown-first-primer.test.md`, `docs/plans/2026-06-27-markdown-first-gym-primer.md`, `CONSTITUTION.md`.
- Validation evidence inspected or rerun:
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py --help`
  - `python3 tools/checks/check_privacy.py -- README.md CONTRIBUTING.md SOURCES.md CONTENT_LICENSE.md`
  - adversarial temporary-page check for a cited source ID absent from `SOURCES.md`

## Diff summary

M2 adds `tools/checks/check_markdown_first.py` for Markdown page structure, claim-level citation, language/scope, and media checks. It adds `tools/checks/check_privacy.py` for negative-match privacy scanning. It adds deterministic fixtures and subprocess-based unittest coverage for page structure, citation failures, guardrails, and privacy semantics.

## Findings

### Finding CR-M2-1

- Finding ID: CR-M2-1
- Severity: major
- Location: `tools/checks/check_markdown_first.py:115`; `specs/markdown-first-primer.test.md:222`
- Evidence: T4 requires the citation checker to assert that reused source IDs appear in `SOURCES.md`. The checker skips support files including `SOURCES.md` and validates only page-local reference definitions. An adversarial page with a safety claim citing `[Unknown][unknown-source]`, a local reference definition for `unknown-source`, and no `SOURCES.md` entry exited `0` with `checked 1 Markdown file(s): pass`.
- Required outcome: The M2 checker and fixture tests must fail when a page uses a source ID that is expected to be reusable/global but is missing from `SOURCES.md`, while still allowing page-local citations that satisfy the approved source model.
- Safe resolution path: Add a fixture where a page uses a missing global/reused source ID and prove it fails; add a valid fixture for a source ID present in `SOURCES.md`; update `check_markdown_first.py` to load/check the repository `SOURCES.md` index for cited source IDs in the M2 scope; rerun the M2 targeted tests and required CLI checks.
- needs-decision rationale: none

## Checklist coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | block | T4 explicitly requires reused source IDs to appear in `SOURCES.md`; the implementation has no effective global source-index check. |
| Test coverage | block | The 23-test suite passes, but no test covers a page-local source ID missing from `SOURCES.md`. The adversarial check demonstrates the gap. |
| Edge cases | block | EC2/T4 source coverage is incomplete for the reused-source/global-index boundary. |
| Error handling | pass | Missing paths return setup errors, invalid pages return nonzero, and privacy findings use nonzero status. |
| Architecture boundaries | pass | The new tooling is standard-library local validation and does not revive the old structured validator. |
| Compatibility | concern | CLI shape is usable, but source-index behavior must be corrected before M2 can close. |
| Security/privacy | pass | Privacy output reports file/rule/line without echoing matched sensitive text; false positive policy prose was narrowed before handoff. |
| Derived artifact currency | pass | No derived artifacts are generated or claimed current. |
| Unrelated changes | pass | M2 changes are limited to checker tooling, fixtures/tests, and workflow metadata. |
| Validation evidence | concern | Required commands pass, but the required command set is insufficient without the missing T4 fixture/check. |

## Residual risks

The checker remains a heuristic minimum gate; semantic citation adequacy is intentionally left to M3 manual citation review. CR-M2-1 is narrower: it concerns a deterministic T4 requirement that belongs in M2.

## Milestone handoff state

- Reviewed milestone: M2
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M2, M3, M4
- Next stage: review-resolution
- Final closeout readiness: not-ready; M2 has an open material finding and M3-M4 remain unimplemented.
