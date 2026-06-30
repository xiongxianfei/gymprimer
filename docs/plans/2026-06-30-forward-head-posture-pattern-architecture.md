# Plan: Forward Head Posture Pattern Architecture

## Status

- Status: active
- Plan lifecycle state: active
- Terminal disposition: not-applicable

## Purpose / big picture

Implement the approved forward-head-posture proof slice as a repeatable
pattern-page architecture. The implementation should prove that a pattern page
can route red flags first, explain an observable posture pattern without
diagnosis, map likely contributors to bounded exercise options, link detailed
exercise options to complete exercise pages, and keep citations, media, and
validation inside the Markdown-first repository boundary.

This plan sequences implementation only. It does not reopen the accepted
direction, add a runtime product, promote a single pattern page from README, or
turn the exercise menu into a corrective routine.

## Source artifacts

- Proposal: `../proposals/2026-06-30-forward-head-posture-pattern-architecture.md`
- Proposal review:
  - `../changes/forward-head-posture-pattern-architecture/reviews/proposal-review-r2.md`
- Spec: `../../specs/forward-head-posture-pattern-architecture.md`
- Spec review:
  - `../changes/forward-head-posture-pattern-architecture/reviews/spec-review-r1.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review:
  - `../changes/forward-head-posture-pattern-architecture/reviews/architecture-review-r1.md`
- Related ADRs:
  - `../adr/2026-06-27-markdown-first-citation-based-authority.md`
  - `../adr/2026-06-28-ai-generated-raster-media-provenance.md`
  - `../adr/2026-06-29-expanded-raster-media-purposes.md`
  - `../adr/2026-06-29-direct-repository-layout-normalization.md`
  - `../adr/2026-06-29-responsible-breadth-static-content-boundaries.md`
- Governing specs:
  - `../../specs/markdown-first-primer.md`
  - `../../specs/responsible-breadth.md`
- Test spec: `../../specs/forward-head-posture-pattern-architecture.test.md`

## Context and orientation

GymPrimer is a Markdown-first repository. The implementation surface is static
Markdown content, local validation scripts, tests, optional generated raster
media under `media/`, and review evidence under
`docs/changes/forward-head-posture-pattern-architecture/`.

The approved proof slice has six content pages:

- `patterns/forward-head-posture.md`
- `exercises/chin-nod.md`
- `exercises/thoracic-extension.md`
- `exercises/wall-slide.md`
- `exercises/prone-y-t.md`
- `exercises/band-pull-apart.md`

The pattern page owns the observable pattern explanation, red-flag routing,
uncertainty, contributor model, detailed exercise annotations, broader
collected exercise list, next links, sources, and author/review metadata. The
exercise pages own exercise setup, movement instructions, muscles involved,
feel cues, mistakes, progressions, safety notes, and page-local sources.

The optional pattern image is limited to one generated raster comparison image
under `media/patterns/forward-head-posture/`. It must have approved provenance
in `media/PROVENANCE.md`, no in-image text, no exercise thumbnails, no red
injury marks, and no before/after cure implication.

## Non-goals

- Do not diagnose neck pain, shoulder pain, headache, disc issues, nerve
  symptoms, thoracic outlet syndrome, or any medical condition.
- Do not create a treatment plan, rehab protocol, posture-correction routine,
  return-to-training prescription, or personalized program.
- Do not add a symptom checker, decision tree, user-input flow, runtime app,
  hosted site, CMS, database, generated output path, or CI workflow.
- Do not implement rounded shoulders or any other pattern page in this plan.
- Do not promote `patterns/forward-head-posture.md` from README as active
  pattern-set content by itself.
- Do not add exercise thumbnails to the pattern page in this first slice.
- Do not add exercise images unless the later test spec and implementation
  evidence show they are needed and can satisfy the existing media/provenance
  contract.

## Requirements covered

- R1-R7: M2-M3 create the titled pattern page, required sections, red-flags
  ordering, non-diagnostic boundaries, observable definition, beginner
  observations, and observation-only self-checks.
- R8-R11: M3 covers core contributors, page-local source support, uncertainty,
  and the four pattern claim families.
- R12-R19: M2-M3 cover the five detailed exercise options, fix reason, muscles,
  cue/caveat, same-slice exercise links, broader secondary list, and no routine
  or prescription framing.
- R20-R23: M3 covers the optional one-image boundary, media path, provenance,
  no in-image text, and Markdown-as-source-of-truth rule.
- R24-R26: M1 covers deterministic exercise-link, image-existence,
  page-contract, source-section, media-provenance, privacy, and forbidden
  language validation.
- R27: M4 verifies README does not promote the single forward-head page.
- R28: M1-M4 preserve no new page class, runtime, generated output, CI,
  hosted app, CMS, symptom checker, decision tree, or user-input flow.
- R29: M1-M4 preserve separate spec, architecture, and template
  responsibilities.
- R30: M4 records exact local validation commands and no unobserved CI claim.
- R31: M2 keeps exercise pages text-first unless later reviewed evidence
  requires optional images.
- R32: M1 adds focused checker/test assertions for deterministic constraints
  not already covered.
- AC1-AC17: M1-M4 provide acceptance evidence after test-spec review and
  implementation review.

## Current Handoff Summary

- Current milestone: M1
- Current milestone state: review-requested
- Last reviewed milestone: none
- Review status: proposal-review R2 approved; spec-review R1 approved;
  architecture-review R1 approved; plan-review R1 approved; test-spec-review
  R2 approved
- Remaining in-scope implementation milestones: M1 review, M2, M3, M4
- Next stage: code-review
- Final closeout readiness: not ready
- Reason final closeout is or is not ready: M1 implementation has local
  validation evidence and is ready for code-review, but M1 review, M2-M4,
  explain-change, verification, and PR handoff remain downstream gates.

## Milestones

### M1. Validation Contract for the Forward-Head Slice

- Milestone state: review-requested
- Goal: Add or extend deterministic validation for the forward-head proof slice
  before content relies on it.
- Requirements: R2, R14, R20-R26, R28-R30, R32, AC2, AC4, AC7, AC8, AC11-AC15,
  AC17
- Files/components likely touched:
  - `tools/checks/check_markdown_first.py`
  - `tests/test_responsible_breadth_m1.py`
  - `tests/test_markdown_first_templates.py`
  - `tests/fixtures/responsible-breadth/`
  - `docs/templates/pattern-page.md` only if tests expose a template gap
- Dependencies:
  - Plan-review approval.
  - Test-spec and test-spec-review approval.
- Tests to add/update:
  - Pattern page required-section fixtures for the forward-head architecture.
  - Missing detailed exercise-link fixture.
  - Missing same-slice exercise-page fixture.
  - Optional pattern-image missing-asset fixture.
  - One-image/no-thumbnail/no-in-image-text assertion where it can be checked
    deterministically.
  - Forbidden diagnostic, treatment, rehab, posture-correction, routine, and
    personalized-programming fixtures.
- Implementation steps:
  - Map existing Responsible Breadth checker coverage to R24-R26 and R32.
  - Add focused assertions for constraints not already covered.
  - Keep semantic source-quality judgment as review evidence when automation
    cannot verify it reliably.
  - Avoid adding markdownlint-only checks for diff semantics; cosmetic rewrap
    detection is a separate diff-aware checker concern outside this spec.
- Validation commands:
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - `python3 -m unittest tests.test_markdown_first_templates`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`
  - `python3 tools/checks/check_privacy.py tools tests docs/templates docs/changes/forward-head-posture-pattern-architecture`
  - `git diff --check`
- Expected observable result: Missing required sections, broken detailed
  exercise links, missing image assets, invalid media provenance, and forbidden
  language fail locally before page promotion can be claimed.
- Commit message: `M1: add forward-head pattern validation`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
  - code-review pending
- Risks:
  - Existing generic pattern checks may be too broad or too APT-specific.
  - No reliable automation can prove all source-support semantics.
- Rollback/recovery:
  - Revert focused checker/test additions and keep content unimplemented.
  - Route back to spec if validation needs a requirement the approved spec does
    not authorize.

### M2. Same-Slice Exercise Pages

- Milestone state: planned
- Goal: Create the five exercise pages required for the pattern complete loop,
  each with page-local source support and no rehab or treatment framing.
- Requirements: R12, R14-R17, R19, R28, R30-R31, AC7-AC9, AC14-AC15, AC17
- Files/components likely touched:
  - `exercises/chin-nod.md`
  - `exercises/thoracic-extension.md`
  - `exercises/wall-slide.md`
  - `exercises/prone-y-t.md`
  - `exercises/band-pull-apart.md`
  - `SOURCES.md` only when sources are reused across pages
  - `docs/changes/forward-head-posture-pattern-architecture/`
- Dependencies:
  - M1 validation coverage or approved test-spec coverage for exercise-page
    contracts.
  - Exercise instruction and safety sources selected during test-spec or
    implementation.
- Tests to add/update:
  - Real-page checker coverage for all five exercise pages.
  - Source-section and source-index reuse checks where applicable.
  - Privacy checks over all new exercise pages.
- Implementation steps:
  - Draft each page from `docs/templates/exercise-card.md`.
  - Keep each page general exercise education, not neck-pain treatment or rehab.
  - Add setup, muscles involved, movement breakdown, feel cues, common
    mistakes, easier version, harder version, safety notes, and sources.
  - Cite setup, technique, muscle, feel-cue, common-mistake, and safety claims
    from page-local sources.
  - Avoid exercise images unless later evidence shows they are necessary.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - `python3 tools/checks/check_privacy.py exercises docs/changes/forward-head-posture-pattern-architecture SOURCES.md`
  - `git diff --check`
- Expected observable result: All five exercise pages exist, satisfy the
  exercise-page contract, have page-local sources, and avoid treatment,
  diagnosis, rehab, and personalized programming.
- Commit message: `M2: add forward-head support exercises`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Exercise pages can accidentally inherit unsupported clinical claims from
    pattern sources.
  - Creating five pages at once increases citation and review burden.
- Rollback/recovery:
  - Remove or draft-mark the five exercise pages and source additions.
  - Keep validation changes from M1 if they remain generally useful and within
    spec.

### M3. Forward Head Posture Pattern Page and Optional Media

- Milestone state: planned
- Goal: Create `patterns/forward-head-posture.md` with the approved pattern
  architecture and optional support image/provenance.
- Requirements: R1-R14, R18-R30, R32, AC2-AC7, AC10-AC17
- Files/components likely touched:
  - `patterns/forward-head-posture.md`
  - `media/patterns/forward-head-posture/`
  - `media/PROVENANCE.md`
  - `SOURCES.md`
  - `docs/changes/forward-head-posture-pattern-architecture/`
- Dependencies:
  - M1 validation coverage.
  - M2 same-slice exercise pages.
  - Four pattern source families: red flags/professional routing,
    posture-pattern evidence and uncertainty, shoulder/scapular context, and
    general resistance-training framing.
  - Final generated raster asset only if it can satisfy provenance and visual
    safety rules.
- Tests to add/update:
  - Real-page pattern architecture assertions.
  - Detailed exercise annotation and link checks.
  - Optional image path/provenance/media-purpose checks.
  - README non-promotion assertion if not already covered elsewhere.
- Implementation steps:
  - Draft the page from `docs/templates/pattern-page.md`.
  - Put red flags before exercise options and link `../RED-FLAGS.md`.
  - Define forward head posture as an observable head, neck, upper-back, and
    rib-cage position.
  - Add beginner observations, observation-only self-checks, core contributors,
    uncertainty, detailed exercise annotations, broader secondary exercise
    list, avoidances, professional routing, sources, and review metadata.
  - If using a generated raster image, place one approved asset under
    `media/patterns/forward-head-posture/` and add an exact provenance row.
  - Keep all labels, safety claims, anatomical explanations, and exercise
    instructions in Markdown text with citations, not in the image.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns exercises media/PROVENANCE.md`
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_privacy.py patterns exercises media docs/changes/forward-head-posture-pattern-architecture SOURCES.md`
  - `git diff --check`
- Expected observable result: The pattern page passes the required page
  contract, links the five same-slice exercise pages, uses source-supported
  uncertainty and contributor claims, and either remains text-only or references
  exactly one approved support image.
- Commit message: `M3: add forward-head posture pattern page`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - The page can drift into posture-correction promises or pain-treatment
    language.
  - Generated imagery can imply cure, injury, or diagnosis even if provenance
    is present.
- Rollback/recovery:
  - Remove or draft-mark the pattern page and optional media/provenance row.
  - Keep exercise pages only if they remain valid standalone exercise education.

### M4. Lifecycle Closeout and Promotion Gate Evidence

- Milestone state: planned
- Goal: Close the implementation loop after content/code review by recording
  rationale, final verification, and PR handoff evidence without promoting the
  page prematurely.
- Requirements: R27, R30, AC15-AC17
- Files/components likely touched:
  - `README.md` only if validation requires an explicit non-promotion guard
  - `docs/changes/forward-head-posture-pattern-architecture/explain-change.md`
  - `docs/changes/forward-head-posture-pattern-architecture/verify-report.md`
  - `docs/changes/forward-head-posture-pattern-architecture/change.yaml`
  - `docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md`
  - `docs/plan.md`
- Dependencies:
  - M1-M3 closed after code review and any required review resolution.
  - Explain-change and verify stages invoked after implementation review.
- Tests to add/update:
  - README or active-navigation non-promotion assertion if not already covered.
  - Final full-scope local validation ledger.
- Implementation steps:
  - Confirm README does not promote the forward-head page alone.
  - Record change rationale after implementation and code review.
  - Run final verification over content, media, tests, privacy, and whitespace.
  - Record whether hosted CI was observed.
  - Update plan lifecycle state only after downstream gates actually complete.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`
  - `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/forward-head-posture-pattern-architecture`
  - `rg -n "patterns/forward-head-posture.md" README.md`
  - `git diff --check`
- Expected observable result: The full local suite and checks pass, README
  promotion remains gated, final verification records exact commands, and no CI
  pass is claimed unless observed.
- Commit message: `M4: verify forward-head pattern slice`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - README may accidentally expose a single-page pattern set before broader
    pattern-set promotion is approved.
  - Plan closeout can be confused with final verification or PR readiness.
- Rollback/recovery:
  - Remove premature README/SUMMARY links.
  - Keep the plan active until explain-change, verify, and PR handoff evidence
    exist.

## Validation plan

- `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`:
  Responsible Breadth pattern, media, and page-contract tests.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`:
  Markdown-first contract, template, media, and real-page regressions.
- `python3 -m unittest discover -s tests`: final full local unittest suite.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`:
  active Markdown content contract, citation, source-index, media, and scope
  validation.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/forward-head-posture-pattern-architecture`:
  privacy scan over product surfaces, media provenance, and change-local
  evidence.
- `rg -n "patterns/forward-head-posture.md" README.md`: README promotion-gate
  check; any match must be reviewed as either forbidden promotion or explicitly
  non-promotional evidence.
- `git diff --check`: whitespace and patch hygiene.

## Risks and recovery

- Risk: The validation layer cannot express a required deterministic
  constraint.
  - Recovery: Add a focused assertion under M1 or route back to spec if the
    needed behavior is outside R1-R32.
- Risk: Exercise pages inherit unsupported treatment or rehab claims.
  - Recovery: Remove unsupported claims, replace with general exercise
    education, or draft-mark/remove the page.
- Risk: The pattern page becomes a routine or correction promise.
  - Recovery: Reframe exercise options as an educational menu and rerun
    forbidden-language checks.
- Risk: The optional image cannot be made safe enough.
  - Recovery: Ship the pattern page text-only; images are optional.
- Risk: Source burden grows beyond the slice.
  - Recovery: Use `SOURCES.md` only for reused sources and keep page-local
    source definitions for page-specific claims.

## Dependencies

- Plan-review must approve this plan before test-spec authoring.
- Test-spec and test-spec-review must map R1-R32, AC1-AC17, and the milestone
  validation commands before implementation starts.
- Exercise instruction and safety sources must be selected during test-spec or
  implementation with page-local citation support.
- Optional final image generation requires provenance, review, and media checks
  before promotion.
- No hosted CI exists; local validation evidence remains the required proof.

## Progress

- 2026-06-30: Proposal review R2 approved the forward-head-posture pattern
  architecture direction.
- 2026-06-30: Spec review R1 approved the focused spec with no material
  findings.
- 2026-06-30: Architecture review R1 approved the canonical architecture update
  with no material findings.
- 2026-06-30: Execution plan created and indexed for plan-review.
- 2026-06-30: Plan-review R1 approved the execution plan with no material
  findings.
- 2026-06-30: Test spec drafted and routed to test-spec-review.
- 2026-06-30: Test-spec-review R1 requested changes for review-only semantic
  evidence metadata and validation command ownership.
- 2026-06-30: Test spec revised to use review-only code-review evidence and
  validation command ownership metadata.
- 2026-06-30: Test-spec-review R2 approved the active test spec for
  implementation.
- 2026-06-30: M1 implemented focused forward-head validation tests and checker
  rules, passed targeted local validation, and is ready for code-review.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-30 | Sequence validation before content pages. | The spec requires deterministic checks for links, image assets, media provenance, privacy, and forbidden language before promotion claims. | Implement pages first and backfill checker coverage later. |
| 2026-06-30 | Put the five exercise pages before the pattern page. | The pattern page's detailed exercise annotations must link to same-slice pages, so the dependency should exist before final pattern integration. | Create the pattern page first with placeholder links. |
| 2026-06-30 | Keep the optional image in the pattern-page milestone. | The image is support-only and optional; it should not block exercise-page implementation. | Generate media before content structure and source claims are stable. |
| 2026-06-30 | Leave README promotion to lifecycle evidence, not content implementation. | The approved spec gates README promotion on the full pattern set, not this single page. | Promote the forward-head page immediately after local validation. |
| 2026-06-30 | Scope the M1 exercise-page contract to the five forward-head exercise paths. | Current exercise pages outside this slice use older headings, while the approved proof-map requires the complete-loop contract for the five selected forward-head pages. | Apply the new exercise-page heading contract globally in M1. |

## Surprises and discoveries

- `docs/workflows.md` still has stale current-change routing for an older
  Markdown-first track. This plan uses `docs/plan.md` and the
  forward-head-posture review records as the active routing surface instead of
  rewriting the workflow guide in this slice.
- Existing Responsible Breadth tests already cover much of the pattern-page
  architecture and media-purpose behavior; M1 should prefer focused extensions
  over a duplicate checker.
- Current APT support exercise pages use an older exercise-page shape, so M1
  applies the new complete-loop exercise contract only to the five
  forward-head exercise paths.

## Validation notes

- 2026-06-30: Plan authoring validation ran privacy and whitespace checks over
  the plan, index, and touched lifecycle artifacts before handoff.
- 2026-06-30: Test spec authoring validation ran privacy, whitespace, coverage
  token, and routing checks over the test spec, plan, index, and change-local
  lifecycle artifacts.
- 2026-06-30: M1 tests-first run of `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'` failed before implementation with expected missing forward-head title/link, exercise-page contract, and image-contract assertions.
- 2026-06-30: M1 validation passed with `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`, `python3 -m unittest tests.test_markdown_first_templates`, `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`, `python3 tools/checks/check_privacy.py tools tests docs/templates docs/changes/forward-head-posture-pattern-architecture`, and `git diff --check`.

## Outcome and retrospective

- Pending. Fill only after implementation, review, verification, and PR handoff
  complete.

## Readiness

- See `Current Handoff Summary`.
- Ready for code-review of M1. Readiness is not Done; M1 review, M2-M4,
  explain-change, verification, and PR handoff remain open.
