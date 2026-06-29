# Explain Change: Responsible Breadth

## Summary

This change implements the accepted Responsible Breadth direction end to end:
governance and vision were widened, the scope was specified and designed, local
validation was extended, the first expanded Markdown proof slice was drafted,
manual proof was recorded, and README now promotes only the validated expanded
pages.

## Problem

GymPrimer's old narrow scope taught exercise literacy but left three beginner
needs unresolved: common patterns/conditions, visual and safety routing
standards, and basic programming literacy. The accepted proposal chose static,
citation-backed education with red-flag routing instead of diagnosis,
treatment, personalized programming, or runtime decision support.

## Decision Trail

- Proposal: `docs/proposals/2026-06-29-responsible-breadth.md`
- Proposal review: proposal-review R3 accepted the direction after PR-RB-1
  required constitution-level scope alignment.
- Requirements: `specs/responsible-breadth.md` R1-R56 and AC1-AC10 plus
  AC-COMP-1 through AC-COMP-10.
- Compatibility: `specs/markdown-first-primer.md` now preserves the original
  five-page v0.1 contract while Responsible Breadth governs expanded page
  classes.
- Architecture/ADR: `docs/architecture/system/architecture.md` and
  `docs/adr/2026-06-29-responsible-breadth-static-content-boundaries.md`.
- Plan milestones: M1 validation scaffold, M2 references/templates/source seed,
  M3 first expanded pages, M4 promotion and final ledger.
- Reviews: M1-M4 code reviews and final holistic code-review are clean with no
  material findings.

## Diff Rationale By Area

| Area | Files | Why changed | Evidence |
| --- | --- | --- | --- |
| Governance and vision | `CONSTITUTION.md`, `AGENTS.md`, `VISION.md`, `README.md`, `docs/vision/strategic-positioning.md` | Align top-ranked project scope with accepted static pattern/condition/programming education. | Proposal-review R3; spec-review R2. |
| Specs and compatibility | `specs/responsible-breadth.md`, `specs/markdown-first-primer.md`, `specs/responsible-breadth.test.md` | Define requirements, page classes, compatibility with the original Markdown-first spec, and proof map. | Spec-review R2; test-spec-review R2. |
| Architecture and ADR | `docs/architecture/system/*`, `docs/adr/2026-06-29-responsible-breadth-static-content-boundaries.md` | Record static Markdown boundaries, manual proof ownership, media/provenance inheritance, and no-runtime design. | Architecture-review R1. |
| Workflow records | `docs/changes/responsible-breadth/*`, `docs/plans/2026-06-29-responsible-breadth.md`, `docs/plan.md` | Preserve traceability, review outcomes, manual proof, validation ledger, and autoprogression state. | Plan-review R1; code-review M1-M4; final holistic code-review. |
| Validation tooling | `tools/checks/check_markdown_first.py` | Add path-scoped Responsible Breadth checks without breaking original v0.1 pages. | RB tests and Markdown-first regression suite. |
| Tests | `tests/test_responsible_breadth_m1.py` | Prove page-class routing, contracts, metadata, red-flag order, source count, guardrails, references/templates, real pages, promotion, and proof records. | 15 Responsible Breadth tests passed. |
| Content and templates | `about/`, `patterns/`, `conditions/`, `principles/`, `programs/`, `docs/templates/`, `SOURCES.md`, `CONTRIBUTING.md` | Add the red-flags reference, first expanded proof slice, reusable source seed, page templates, and higher-bar contributor guidance. | M2-M4 validation and manual proof records. |

## PR Feedback Update

The anterior-pelvic-tilt page was expanded after PR feedback identified the
first version as structurally compliant but too thin for beginner use. The
update adds a working definition, observation-not-diagnosis cues, inline
topic-specific red flags, stronger uncertainty language, professional routing
by type, an original SVG alignment comparison, and a "Where to next" block
using existing primer pages. The page-contract split suggestion for a future
mandatory "How to notice this in yourself" section was not folded into this PR
because that would require a spec/template amendment.

## Tests Added Or Changed

- Responsible Breadth tests cover RB-T1 through RB-T20 at the level required by
  each milestone: unit/checker tests, real-page integration, manual-proof
  presence, README promotion, and mdBook deferral proof.
- Existing `test_markdown_first_*.py` tests remain compatibility coverage for
  the original Markdown-first contract.

## Validation Evidence Before Verify

- `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  passed: 15 tests.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  passed: 51 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md about patterns conditions principles programs`
  passed: checked 7 Markdown files.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md about patterns conditions principles programs docs/changes/responsible-breadth media`
  passed: checked 47 files.
- `command -v mdbook || true` exited 0 with no path output; RB-MP9 records
  explicit mdBook deferral.
- CI was not run or observed.

## Review Resolution Summary

Material findings are closed:

- PR-RB-1: resolved by proposal-review R3 after constitution-first scope
  alignment.
- SR-RB-1: resolved by spec-review R2 after adding the same-rank compatibility
  contract.
- TSR-RB-1: resolved by lifecycle/status normalization before test-spec-review
  R2.

No implementation code-review findings were opened.

## Alternatives Rejected

- Runtime symptom checker, diagnostic flow, hosted app, API, CMS, user accounts,
  and generated AI source-of-truth content remained out of scope.
- Per-page commercial disclaimer scaffolding was not added for Responsible
  Breadth pages; the project uses project-level disclaimer, page scope notes,
  red-flag routing, citation discipline, and manual proof.
- mdBook output was not generated because no mdBook binary or configuration is
  available; Markdown remains canonical.

## Scope Control

The change does not add diagnosis, individualized medical advice, treatment
plans, active rehabilitation protocols, return-to-training prescriptions,
personalized programming, acute injury guidance, specialized-population
content, generated HTML, media assets, or a hosted product surface.

## Risks And Follow-Ups

- Link health and source freshness need periodic maintenance.
- External beginner-reader testing remains useful before broader scaling.
- CI is not configured or observed; final verify must report local validation
  only unless a real CI run is available.

## Readiness

Ready for `verify`. Not branch-ready, PR-ready, or Done until verify completes.
