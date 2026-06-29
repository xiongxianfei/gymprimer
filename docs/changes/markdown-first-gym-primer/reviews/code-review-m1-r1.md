# Code Review M1 R1: Markdown-First Gym Primer

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/markdown-first-gym-primer/reviews/code-review-m1-r1.md`, `docs/changes/markdown-first-gym-primer/review-log.md`, `docs/plans/2026-06-27-markdown-first-gym-primer.md`, `docs/plan.md`, `docs/workflows.md`, `docs/changes/markdown-first-gym-primer/change.yaml`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/code-review-m1-r1.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M1. Active Route, Contributor Contract, and Legacy Supersession
- Milestone closeout: closed
- Remaining implementation milestones: M2, M3, M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: M1 working-tree changes to `README.md`, `CONTRIBUTING.md`, `SOURCES.md`, `CONTENT_LICENSE.md`, `docs/templates/`, old structured-platform README notices, M1 tests, plan/workflow/change metadata.
- Tracked governing branch state: working tree on `proposal/markdown-first-gym-primer`; implementation artifacts are uncommitted, so this review is milestone-local and does not claim branch readiness.
- Governing artifacts: `specs/markdown-first-primer.md`, `specs/markdown-first-primer.test.md`, `docs/plans/2026-06-27-markdown-first-gym-primer.md`, `CONSTITUTION.md`, `docs/adr/2026-06-27-markdown-first-citation-based-authority.md`.
- Validation evidence rerun during review:
  - `python3 -m unittest tests.test_markdown_first_contract tests.test_markdown_first_templates tests.test_markdown_first_legacy_boundary`
  - `rg -n "Markdown-first|source of truth|01-getting-started|02-machines|03-bodyweight|SOURCES.md" README.md`
  - `rg -n "Apache-2.0|CC BY 4.0|right to submit|third-party media|claim-level|not medical advice" CONTRIBUTING.md CONTENT_LICENSE.md`
  - `test -f SOURCES.md && test -f CONTENT_LICENSE.md && test -f docs/templates/exercise-card.md && test -f docs/templates/principle-page.md`
  - `rg -n "superseded|Markdown-first" docs/plans/2026-06-26-content-schema-foundation.md content/README.md schemas/README.md generated/README.md tools/validation/README.md`
  - `git diff --check`

## Diff summary

M1 replaces active README guidance that previously routed readers toward the old generated-output path with Markdown-first source-of-truth guidance, planned first-slice paths, M1 validation, and clear legacy boundaries.

It adds the M1 contract surfaces required by the plan: `SOURCES.md`, `CONTENT_LICENSE.md`, `docs/templates/exercise-card.md`, and `docs/templates/principle-page.md`.

It expands `CONTRIBUTING.md` with scope, citation, disclaimer, media, privacy, and inbound license terms. It marks `content/`, `schemas/`, `generated/`, and `tools/validation/` README files as superseded historical structured-platform artifacts.

It adds M1 contract tests for T1, T2, and T7.

## Findings

No blocking or required-change findings.

## Checklist coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | `README.md` identifies the Markdown corpus as source of truth and keeps first-slice pages planned until M3; `CONTRIBUTING.md` covers R7-R16, R23-R30, and R26-R28; old platform files are marked historical for R34-R35. |
| Test coverage | pass | `tests/test_markdown_first_contract.py`, `tests/test_markdown_first_templates.py`, and `tests/test_markdown_first_legacy_boundary.py` directly cover T1, T2, and T7. The targeted unittest command passed with 7 tests. |
| Edge cases | pass | M1 covers the named M1 boundary edge: old generated JSON and structured-platform surfaces no longer outrank Markdown-first guidance. First-slice content, claim semantics, privacy tooling, and mdBook edge cases are assigned to later milestones. |
| Error handling | pass | M1 is documentation/template work. The safe fallback is explicit: planned pages are not active until M3, old tools are historical, and no CI is claimed. |
| Architecture boundaries | pass | The change preserves Markdown as canonical, treats generated output as historical/derived, and keeps mdBook out of M1. |
| Compatibility | pass | Old artifacts remain traceable in place instead of being deleted or moved. README labels planned paths without creating stable promoted page links before M3. |
| Security/privacy | pass | Contributor guidance and README prohibit secrets, private health information, local private paths, and identifying reader-test notes. No private data or media assets were added. |
| Derived artifact currency | pass | No derived artifact is updated or claimed current. Generated JSON is explicitly historical, not source of truth. |
| Unrelated changes | pass | The M1 review surface is aligned with the plan’s listed files. Earlier upstream governance/spec/architecture edits remain outside this M1 closeout conclusion. |
| Validation evidence | pass | Required M1 commands were rerun during review and passed; `git diff --check` passed. |

## No-finding rationale

The implementation satisfies the M1 contract without expanding product scope. The active reader/contributor surfaces now point to Markdown-first guidance, required license and citation terms exist, page templates contain the required sections and disclaimers, and old structured-platform directories carry clear supersession notices.

The tests are appropriately narrow for M1. They do not attempt to validate first-slice content, semantic citation quality, privacy scanner behavior, mdBook, or real Markdown page integration because those are assigned to M2-M4 by the approved test spec.

## Residual risks

- M1 does not prove the five content pages, Markdown-first checker tooling, privacy checker, beginner read test, or mdBook behavior. Those remain open in M2-M4.
- This review is milestone-local and does not claim branch readiness, PR readiness, CI success, or final verification.

## Milestone handoff state

- Reviewed milestone: M1
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining in-scope implementation milestones: M2, M3, M4
- Next stage: implement M2
- Final closeout readiness: not-ready; M2-M4 implementation and review, final explain-change/verification, and PR handoff remain.
