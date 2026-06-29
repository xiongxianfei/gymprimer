# Explain Change: Markdown-First Gym Primer

## Summary

This change turns GymPrimer from the prior structured reviewed-content
platform into a Markdown-first, citation-based beginner primer.

Markdown files are now the primary product. The first slice contains five
GitHub-readable pages, citation and disclaimer rules, narrow media provenance
rules, lightweight validation tools, manual proof records, and reviewed
workflow evidence through M4. Optional mdBook output was evaluated in M4 and
deferred because `mdbook` is not installed locally; Markdown remains the source
of truth.

## Problem

The accepted proposal found that the earlier direction had accumulated schema,
review lifecycle, reviewer-tier, generated JSON, and future hosted-site
machinery before the project had proven that beginners could use the exercise
content. The project also did not have a real expert-review board, so claiming
expert-reviewed content would have overstated the trust model.

The implemented solution narrows v0.1 to a repository-native Markdown primer:
beginner pages with disclaimers, page-local sources, reusable source indexing,
scope exclusions, optional provenance-controlled images, and local checks.

## Decision Trail

| Stage | Decision | Durable source |
| --- | --- | --- |
| Proposal | Adopt Markdown-first repository content with optional mdBook, citation-based authority, English-first v0.1, and five initial pages. | `docs/proposals/2026-06-27-markdown-first-gym-primer.md`; `proposal-review-r2` |
| Vision/governance | Update project identity from structured platform to Markdown-first beginner exercise-literacy primer. | `VISION.md`, `CONSTITUTION.md`, `AGENTS.md` |
| Spec | Define R1-R53 for Markdown source of truth, page structure, citations, scope, licensing, media, privacy, beginner proof, and mdBook deferral. | `specs/markdown-first-primer.md`; `spec-review-r3` |
| Architecture/ADR | Make Markdown the canonical source, old platform artifacts historical, mdBook derived, and raster media classified before provenance lookup. | `docs/architecture/system/architecture.md`; ADRs dated 2026-06-27 and 2026-06-28 |
| Plan | Execute M1, M2, M3A, M3, and M4 in order, with M3A enabling media validation and M3 blocked until beginner proof existed. | `docs/plans/2026-06-27-markdown-first-gym-primer.md`; `plan-review-r3` |
| Test spec | Map T1-T15, CMD, and MP proof records to milestones and closeout evidence. | `specs/markdown-first-primer.test.md`; `test-spec-review-r4` |
| Review | Close M1, M2, M3A, M3, and M4 through code review. | `review-log.md`; `code-review-m4-r1` |

## Diff Rationale By Area

| Area | Files | Change | Reason | Evidence |
| --- | --- | --- | --- | --- |
| Product route and governance | `README.md`, `VISION.md`, `CONSTITUTION.md`, `AGENTS.md`, `docs/vision/strategic-positioning.md` | Reframed GymPrimer as a Markdown-first beginner primer and removed active old-platform assumptions. | Supports R1-R4 and the accepted proposal's trust/source-of-truth change. | M1 tests and `code-review-m1-r1`. |
| Contributor and license contract | `CONTRIBUTING.md`, `CONTENT_LICENSE.md`, `SOURCES.md` | Added citation, disclaimer, media, privacy, Apache-2.0, CC BY 4.0, right-to-submit, and reusable source-index guidance. | Supports R7-R16 and R26-R28; replaces unavailable expert review with source discipline. | M1/M2 tests and CR-M2-1 resolution. |
| Templates | `docs/templates/exercise-card.md`, `docs/templates/principle-page.md` | Added reusable Markdown page shapes with disclaimer, required sections, safety notes, and sources. | Supports R5-R8 and gives contributors a consistent first-slice structure. | `tests/test_markdown_first_templates.py`. |
| Legacy boundary | `content/README.md`, `schemas/README.md`, `generated/README.md`, `tools/validation/README.md`, old plan and ADR | Marked old structured-platform surfaces as superseded historical context. | Supports R34-R35 without deleting traceability. | `tests/test_markdown_first_legacy_boundary.py`. |
| Checker tooling | `tools/checks/check_markdown_first.py`, `tools/checks/check_privacy.py` | Added local Markdown-first validation, source-index validation, media classification/provenance checks, and negative-match privacy scanning. | Supports T3-T6, T14, R36-R37, R41-R53. | M2 and M3A tests; `code-review-m2-r2`; `code-review-m3a-r1`. |
| Test fixtures | `tests/fixtures/markdown-first/**` | Added valid and invalid fixtures for page structure, citations, scope/language/media guardrails, and privacy. | Proves invalid contract cases fail before real page promotion. | 51 Markdown-first tests passed in M4 review. |
| First-slice content | `01-getting-started/`, `02-machines/`, `03-bodyweight/` | Added the required principle page, three machine pages, and incline push-up page with disclaimers, citations, scope limits, use cases, and beginner-readable structure. | Supports R2, R5-R22, AC1-AC7, and T8-T10. | Checker, privacy scan, excluded-scope scan, MP1-MP3, `code-review-m3-r3`. |
| Media examples and provenance | `media/PROVENANCE.md`, `media/equipment/`, `media/movements/`, `media/svg/`, `media/supplemental/` | Added approved AI-generated raster examples for equipment/key movement support, SVG examples, provenance rows, and media guidance. | Supports R23-R25 and R41-R53 while keeping images optional and provenance-controlled. | M3A media tests, MP6, MP7, media provenance checks. |
| Manual proof | `docs/changes/markdown-first-gym-primer/manual-proof/` | Added render, citation, beginner read-test, media review, mdBook deferral, and final validation ledger records. | Covers manual-only and conditional proof obligations that automation cannot fully prove. | MP1-MP7 and code reviews. |
| M4 mdBook/final gate | `MP4-mdbook-build-or-deferral.md`, `MP5-validation-command-ledger.md`, `tests/test_markdown_first_mdbook.py`, `tests/test_markdown_first_observability.py`, `tests/test_markdown_first_compatibility.py` | Recorded mdBook deferral, command ledger, no CI claim, and compatibility tests. | Supports R31-R33, R36-R40, T11-T13, and AC10-AC13. | `code-review-m4-r1` clean-with-notes. |
| Workflow evidence | `docs/workflows.md`, `docs/plan.md`, plan body, `change.yaml`, reviews, review log, review resolution | Kept lifecycle routing, findings, milestone state, and validation history current. | Required by the project workflow and source-order rules. | Review log shows all material findings resolved. |

## Tests Added Or Changed

| Test area | Files | What it proves |
| --- | --- | --- |
| M1 contract/template/legacy | `test_markdown_first_contract.py`, `test_markdown_first_templates.py`, `test_markdown_first_legacy_boundary.py` | Active route, contributor/license terms, source index, templates, and superseded old surfaces are present. |
| M2 checker behavior | `test_markdown_first_page_structure.py`, `test_markdown_first_citations.py`, `test_markdown_first_guardrails.py`, `test_markdown_first_privacy.py` | Missing disclaimers/sources, citation/source-index defects, excluded scope, language/media guardrails, and privacy findings are detected. |
| M3 real pages | `test_markdown_first_real_pages.py` | Required first-slice pages exist, README links them, and the checker accepts them. |
| M3A media | Guardrail fixtures and updated checker tests | Text-only pages remain valid, SVGs are allowed, raster images require approved provenance, and invalid media references fail deterministically. |
| M4 final gate | `test_markdown_first_mdbook.py`, `test_markdown_first_observability.py`, `test_markdown_first_compatibility.py` | mdBook is either configured or durably deferred, Markdown remains canonical, command evidence is recorded, CI is not falsely claimed, and generated `book/` output is not active. |

The test levels are intentionally local and lightweight because the product is
a Markdown repository, not a hosted application or generated content service.
Semantic citation adequacy and beginner comprehension are recorded as manual
proof instead of pretending they are fully automatable.

## Validation Evidence Before Final Verify

The latest reviewed M4 evidence includes:

- `python3 -m unittest tests.test_markdown_first_mdbook tests.test_markdown_first_observability tests.test_markdown_first_compatibility`
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight`
- `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight media docs/changes/markdown-first-gym-primer`
- `if command -v mdbook >/dev/null 2>&1; then mdbook build; else printf 'mdbook not installed; mdBook deferred\n'; fi`
- excluded-scope `rg` scan over first-slice content
- scoped `markdownlint --disable MD013 -- ...`
- `git diff --check`

M4 code review reran these checks and recorded a clean-with-notes result. CI
was not run, and this artifact does not claim CI success or final verification.

## Review Resolution Summary

Material findings are closed in
`docs/changes/markdown-first-gym-primer/review-resolution.md`.

| Finding | Disposition |
| --- | --- |
| TSR1 | Resolved by adding milestone/proof ownership to the test spec. |
| CR-M2-1 | Resolved by making `SOURCES.md` an executable source-index input. |
| SR-MEDIA-1 | Resolved by defining centralized AI raster provenance requirements. |
| AR-MEDIA-1 | Resolved by adding deterministic extension-based media classification. |
| PR-MEDIA-1 | Resolved by sequencing M3A before M3 closeout. |
| TSR-M3A-1 | Resolved by correcting stale edge-case traceability. |
| CR-M3-1 | Resolved by adding non-identifying per-page beginner comprehension outcomes to MP3. |

No material findings remain open in the review log.

## Alternatives Rejected

- Continue the structured reviewed-content platform: rejected for v0.1 because
  schema, lifecycle, reviewer, and generated-output machinery exceeded the
  project's current proof needs.
- Hosted Astro/Hugo/Next.js site: rejected because it would move effort away
  from readable content and add deployment/maintenance scope.
- Expert-review claims: rejected until named reviewers exist.
- Global-only sources: rejected because each page must render standalone and
  safety claims need page-local verification.
- Arbitrary local source IDs: rejected after CR-M2-1 because they allowed
  reusable-looking source IDs to bypass `SOURCES.md`.
- Undocumented raster media: rejected because images need deterministic
  provenance and review before promotion.
- Mandatory images or generated HTML: rejected because Markdown text remains
  the product and pages without images remain valid.

## Scope Control

The change preserves the v0.1 non-goals:

- no hosted app, CMS, user accounts, trainer dashboard, AI coach, or progress
  tracking;
- no generated public JSON product or old review-state lifecycle;
- no rehab, diagnosis, pain treatment, posture-correction protocol, advanced
  programming, sprint, plyometric, kettlebell ballistic, Olympic, or barbell
  content;
- no full Chinese translation in v0.1;
- no third-party screenshots, stock photos, borrowed public web images, or
  commercial machine screenshots;
- no claim that CI, final verification, branch readiness, or PR readiness has
  completed.

## Risks And Follow-Ups

- mdBook remains deferred until a contributor installs `mdbook` and chooses to
  exercise the optional build path.
- The current beginner proof is intentionally small: one non-identifying
  beginner reader, not formal usability research.
- Repository-wide `markdownlint "**/*.md"` still has broader pre-existing
  issues outside the current gate; scoped lint was used for milestone evidence.
- Final `verify` still needs to run after this explanation to check artifact,
  code, test, and routing coherence before PR handoff.

## Handoff

Implementation milestones M1, M2, M3A, M3, and M4 are closed after code review.
This explanation completes the durable rationale step and routes the workflow
to `verify`. It does not claim final verification, CI success, branch
readiness, or PR readiness.
