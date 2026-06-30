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
  - `../adr/2026-06-30-central-red-flags-disclaimer.md`
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

- Current milestone: M3
- Current milestone state: review-requested
- Last reviewed milestone: M2
- Review status: proposal-review R2 approved; spec-review R1 approved;
  architecture-review R1 approved; plan-review R1 approved; test-spec-review
  R2 approved; code-review M1 R1 changes-requested; spec-review R2 approved
  the central-disclaimer amendment; architecture-review R2 approved the
  central-disclaimer architecture; test-spec-review R3 approved the amended
  proof map; code-review M1 R2 closed M1; code-review M2 R3 closed
  CR-FHP-M2-1; M3 implementation is pending code-review
- Remaining in-scope implementation milestones: M3, M4
- Next stage: code-review M3
- Final closeout readiness: not ready
- Reason final closeout is or is not ready: The central-disclaimer contract
  amendment is spec-approved, architecture-approved, proof-map-approved, M1
  and M2 are closed, and M3 is implemented pending code-review, but M4 remains
  open, and explain-change, verification, and PR handoff remain downstream
  gates.

## Milestones

### M1. Validation Contract for the Forward-Head Slice

- Milestone state: closed
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

- Milestone state: closed
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
  - decision log unchanged
  - validation notes updated
  - validation passed
  - progress updated
  - decision log unchanged
  - validation notes updated
  - milestone committed
  - code-review found CR-FHP-M2-1; R3 closed the finding and milestone
- Risks:
  - Exercise pages can accidentally inherit unsupported clinical claims from
    pattern sources.
  - Creating five pages at once increases citation and review burden.
- Rollback/recovery:
  - Remove or draft-mark the five exercise pages and source additions.
  - Keep validation changes from M1 if they remain generally useful and within
    spec.

### M3. Forward Head Posture Pattern Page and Optional Media

- Milestone state: review-requested
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
- 2026-06-30: Code-review M1 R1 requested changes for missing deterministic
  disclaimer validation on the five forward-head exercise pages.
- 2026-06-30: Owner clarified that the prominent disclaimer belongs only in
  `RED-FLAGS.md`; specs, templates, checker behavior, and tests were amended
  to centralize disclaimer validation and now require spec-review.
- 2026-06-30: Spec-review R2 approved the central-disclaimer amendment with no
  material findings and routed the change to architecture-review.
- 2026-06-30: Canonical architecture and ADR
  `docs/adr/2026-06-30-central-red-flags-disclaimer.md` were updated to assign
  central disclaimer ownership to `RED-FLAGS.md`.
- 2026-06-30: Architecture-review R2 approved the central-disclaimer
  architecture and ADR with no material findings.
- 2026-06-30: Test-spec-review R3 approved the central-disclaimer proof map
  with no material findings.
- 2026-06-30: Code-review M1 R2 closed M1 with no material findings and
  handed off to M2 implementation.
- 2026-06-30: M2 added five same-slice exercise pages:
  `exercises/chin-nod.md`, `exercises/thoracic-extension.md`,
  `exercises/wall-slide.md`, `exercises/prone-y-t.md`, and
  `exercises/band-pull-apart.md`.
- 2026-06-30: M2 added a real-page Responsible Breadth assertion that fails
  until all five forward-head exercise pages exist and pass the exercise-page
  contract.
- 2026-06-30: Code-review M2 R1 requested changes for direct page-local
  source support on sampled exercise-specific setup, technique, muscle,
  feel-cue, common-mistake, and safety claims.
- 2026-06-30: Review-resolution for CR-FHP-M2-1 replaced broad exercise-specific
  source uses with direct page-local support or softened claims on the five
  M2 exercise pages, removed the no-longer-reused ACE exercise-library entry
  from `SOURCES.md`, and added FHP-RO2 evidence in
  `docs/changes/forward-head-posture-pattern-architecture/review-resolution.md`.
- 2026-06-30: Code-review M2 R2 found CR-FHP-M2-1 failed-remediation because
  several sampled setup and technique claims still cite sources that support
  muscle/activity context but not the exact beginner setup details.
- 2026-06-30: Review-resolution for code-review M2 R2 added direct
  exercise-instruction sources for setup and technique claims, kept PubMed/PMC
  sources for muscle/activity claims, replaced the gated thoracic-extension
  source, and updated the FHP-RO2 remediation table.
- 2026-06-30: Code-review M2 R3 closed CR-FHP-M2-1 with no material findings
  after sampling direct exercise-instruction and muscle/activity source
  support separately.
- 2026-06-30: M3 added `patterns/forward-head-posture.md`, one generated
  raster comparison image at
  `media/patterns/forward-head-posture/forward-head-posture-comparison.png`,
  the matching `media/PROVENANCE.md` row, and a focused real-page Responsible
  Breadth assertion.
- 2026-06-30: M3 keeps the pattern page unpromoted from README; M4 still owns
  README promotion-gate evidence and lifecycle closeout.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-30 | Sequence validation before content pages. | The spec requires deterministic checks for links, image assets, media provenance, privacy, and forbidden language before promotion claims. | Implement pages first and backfill checker coverage later. |
| 2026-06-30 | Put the five exercise pages before the pattern page. | The pattern page's detailed exercise annotations must link to same-slice pages, so the dependency should exist before final pattern integration. | Create the pattern page first with placeholder links. |
| 2026-06-30 | Keep the optional image in the pattern-page milestone. | The image is support-only and optional; it should not block exercise-page implementation. | Generate media before content structure and source claims are stable. |
| 2026-06-30 | Leave README promotion to lifecycle evidence, not content implementation. | The approved spec gates README promotion on the full pattern set, not this single page. | Promote the forward-head page immediately after local validation. |
| 2026-06-30 | Scope the M1 exercise-page contract to the five forward-head exercise paths. | Current exercise pages outside this slice use older headings, while the approved proof-map requires the complete-loop contract for the five selected forward-head pages. | Apply the new exercise-page heading contract globally in M1. |
| 2026-06-30 | Centralize the prominent disclaimer in `RED-FLAGS.md` instead of page templates. | Repeating the same disclaimer on every page adds boilerplate and can drift; pages should route safety context to the canonical red-flags reference when needed. | Require every exercise, pattern, and principle page template to repeat the full disclaimer. |
| 2026-06-30 | Use one generated raster comparison image for M3. | The approved slice allows one support-only image when provenance, purpose, path, and no embedded writing checks pass. | Add exercise thumbnails, make the page text-only despite the approved media slice, or add more than one pattern image. |
| 2026-06-30 | Keep NICE and the 2024 posture-pattern review page-local on the pattern page. | They support this page's red-flag routing and uncertainty claims and are not yet reused across pages; AAOS and ACSM already have global source IDs. | Add one-off page sources to `SOURCES.md` prematurely. |

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
- The M1 code-review finding exposed a stale assumption from the older
  Markdown-first v0.1 contract. Responsible Breadth already treats per-card
  disclaimer scaffolding as a non-goal, so the repository now centralizes the
  disclaimer in `RED-FLAGS.md`.
- M2 uses the expanded forward-head exercise contract headings (`What this
  exercise is for`, `Equipment setup`, `Muscles involved`, `Movement
  breakdown`, and related sections), because that is the active validation
  surface for the five same-slice pages.
- M2 source IDs were added to `SOURCES.md` only when reused across more than
  one exercise page; each exercise page still carries page-local reference
  definitions.
- M2 review-resolution keeps direct exercise-specific sources page-local when
  they are used by only one page, which avoids promoting one-off exercise
  sources into the reusable global source index.
- M2 R3 review-resolution separates source roles explicitly: direct
  exercise-instruction sources carry setup, movement, feel, and common-mistake
  wording, while PubMed/PMC research sources carry muscle/activity context.
- M3 needed a focused real-page assertion because existing forward-head tests
  covered fixtures and the real exercise pages but not the actual pattern page.
- M3 source support separates pattern claim families from exercise
  instruction support: NICE covers red-flag routing, the 2024 BMC/PMC review
  covers posture-pattern uncertainty, AAOS covers shoulder/scapular context,
  and ACSM covers general strength-training framing.

## Validation notes

- 2026-06-30: Plan authoring validation ran privacy and whitespace checks over
  the plan, index, and touched lifecycle artifacts before handoff.
- 2026-06-30: Test spec authoring validation ran privacy, whitespace, coverage
  token, and routing checks over the test spec, plan, index, and change-local
  lifecycle artifacts.
- 2026-06-30: M1 tests-first run of `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'` failed before implementation with expected missing forward-head title/link, exercise-page contract, and image-contract assertions.
- 2026-06-30: M1 validation passed with `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`, `python3 -m unittest tests.test_markdown_first_templates`, `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`, `python3 tools/checks/check_privacy.py tools tests docs/templates docs/changes/forward-head-posture-pattern-architecture`, and `git diff --check`.
- 2026-06-30: Code-review M1 R1 used a temporary fixture that removed the
  disclaimer from `exercises/wall-slide.md` while keeping checked sections; the
  checker unexpectedly passed, producing finding CR-FHP-M1-1.
- 2026-06-30: Central-disclaimer amendment validation passed with
  `python3 -m unittest tests.test_markdown_first_page_structure tests.test_markdown_first_templates`,
  `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`,
  `rg -n "about/red-flags.md|Disclaimer:" docs/templates specs/forward-head-posture-pattern-architecture.md specs/forward-head-posture-pattern-architecture.test.md specs/markdown-first-primer.md specs/markdown-first-primer.test.md`,
  `python3 tools/checks/check_privacy.py docs/templates specs/markdown-first-primer.md specs/markdown-first-primer.test.md specs/forward-head-posture-pattern-architecture.md specs/forward-head-posture-pattern-architecture.test.md docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md tests/test_markdown_first_page_structure.py tests/test_markdown_first_templates.py tools/checks/check_markdown_first.py docs/architecture/system/architecture.md`,
  and `git diff --check`.
- 2026-06-30: Architecture authoring validation for the central-disclaimer
  amendment ran privacy, architecture-routing, active Markdown, template, and
  whitespace checks before architecture-review handoff.
- 2026-06-30: Architecture authoring validation passed with
  `python3 -m unittest tests.test_markdown_first_page_structure tests.test_markdown_first_templates`,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`,
  `python3 tools/checks/check_privacy.py docs/architecture/system/architecture.md docs/architecture/system/diagrams/container.mmd docs/adr/2026-06-30-central-red-flags-disclaimer.md docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  `rg -n "2026-06-30-central-red-flags-disclaimer|current_stage: architecture-review|current_architecture_status: draft|Central red-flags disclaimer|central disclaimer|RED-FLAGS.md owns" docs/architecture/system/architecture.md docs/architecture/system/diagrams/container.mmd docs/adr/2026-06-30-central-red-flags-disclaimer.md docs/changes/forward-head-posture-pattern-architecture/change.yaml docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  and `git diff --check`.
- 2026-06-30: Architecture-review R2 lifecycle validation passed with
  `python3 tools/checks/check_privacy.py docs/architecture/system/architecture.md docs/architecture/system/diagrams/container.mmd docs/adr/2026-06-30-central-red-flags-disclaimer.md docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  `rg -n "AR-R2|architecture-review-r2|current_stage: test-spec-review|current_architecture_status: approved|Next stage: test-spec-review|Architecture-review R2 approved" docs/architecture/system/architecture.md docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  and `git diff --check`.
- 2026-06-30: Test-spec-review R3 lifecycle validation passed with
  `python3 tools/checks/check_privacy.py specs/forward-head-posture-pattern-architecture.test.md docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  `python3 -c "from pathlib import Path; text = Path('specs/forward-head-posture-pattern-architecture.test.md').read_text(encoding='utf-8'); missing = [f'{prefix}{i}' for prefix, count in [('R', 32), ('E', 5), ('EC', 10), ('AC', 17), ('FHP-CMD', 13), ('FHP-RO', 3)] for i in range(1, count + 1) if f'{prefix}{i}' not in text]; assert not missing, 'missing coverage tokens: ' + ', '.join(missing); print('coverage token check passed')"`,
  `rg -n "TSR-R3|test-spec-review-r3|current_stage: code-review|current_test_spec_status: approved|next_stage: code-review|Implementation handoff: allowed|Review status: approved" specs/forward-head-posture-pattern-architecture.test.md docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  and `git diff --check`.
- 2026-06-30: Code-review M1 R2 validation passed with
  `python3 -m unittest tests.test_markdown_first_page_structure tests.test_markdown_first_templates`,
  `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`,
  `python3 tools/checks/check_privacy.py tools tests docs/templates docs/changes/forward-head-posture-pattern-architecture specs/forward-head-posture-pattern-architecture.md specs/forward-head-posture-pattern-architecture.test.md specs/markdown-first-primer.md specs/markdown-first-primer.test.md docs/architecture/system/architecture.md docs/adr/2026-06-30-central-red-flags-disclaimer.md docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  and `git diff --check`.
- 2026-06-30: M2 tests-first proof ran
  `python3 -m unittest tests.test_responsible_breadth_m1.ResponsibleBreadthM1Test.test_forward_head_real_exercise_pages_exist_and_pass_contract`
  before adding pages and failed with the expected missing five exercise pages.
- 2026-06-30: M2 validation passed with
  `python3 -m unittest tests.test_responsible_breadth_m1.ResponsibleBreadthM1Test.test_forward_head_real_exercise_pages_exist_and_pass_contract`,
  `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises`,
  `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`,
  `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`,
  `python3 tools/checks/check_privacy.py exercises docs/changes/forward-head-posture-pattern-architecture SOURCES.md`,
  and `git diff --check`.
- 2026-06-30: Code-review M2 R1 artifact validation passed with
  `python3 tools/checks/check_privacy.py docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  `rg -n "CR-M2-R1|CR-FHP-M2-1|code-review-m2-r1|current_stage: review-resolution|current_milestone_state: resolution-needed|next_stage: review-resolution|Ready for M2 review-resolution|Closeout status: open" docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  and `git diff --check`.
- 2026-06-30: CR-FHP-M2-1 review-resolution validation passed with
  `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises`,
  `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`,
  `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`,
  `python3 tools/checks/check_privacy.py exercises docs/changes/forward-head-posture-pattern-architecture SOURCES.md docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  and `git diff --check`.
- 2026-06-30: Code-review M2 R2 reran
  `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises`,
  `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`,
  and `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`;
  all passed, but FHP-RO2 semantic source review still found unsupported
  setup and technique details.
- 2026-06-30: Code-review M2 R2 artifact validation passed with
  `python3 tools/checks/check_privacy.py docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  `rg -n "CR-M2-R2|failed-remediation|current_stage: review-resolution|current_milestone_state: resolution-needed|next_stage: review-resolution|Closeout status: open" docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  and `git diff --check`.
- 2026-06-30: CR-FHP-M2-1 R3 review-resolution validation passed with
  `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises`,
  `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`,
  `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`,
  `python3 tools/checks/check_privacy.py docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  and `git diff --check`.
- 2026-06-30: Code-review M2 R3 validation passed with
  `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises`,
  `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`,
  `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`,
  `python3 tools/checks/check_privacy.py docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  and `git diff --check`.
- 2026-06-30: Code-review M2 R3 artifact validation passed with
  `python3 tools/checks/check_privacy.py docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  `rg -n "CR-M2-R3|code-review-m2-r3|current_stage: implement|current_milestone: M3|current_milestone_state: planned|last_reviewed_milestone: M2|open_findings: \\[\\]|Closeout status: closed|Ready for M3 implementation|M2 are closed|M3 implementation is next" docs/changes/forward-head-posture-pattern-architecture docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md docs/plan.md`,
  and `git diff --check`.
- 2026-06-30: M3 tests-first proof ran
  `python3 -m unittest tests.test_responsible_breadth_m1.ResponsibleBreadthM1Test.test_forward_head_real_pattern_page_passes_contract`
  before adding the pattern page and failed with the expected missing
  `patterns/forward-head-posture.md`.
- 2026-06-30: M3 validation passed with
  `python3 -m unittest tests.test_responsible_breadth_m1.ResponsibleBreadthM1Test.test_forward_head_real_pattern_page_passes_contract`,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns exercises media/PROVENANCE.md`,
  `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`,
  `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`,
  `python3 tools/checks/check_privacy.py patterns exercises media docs/changes/forward-head-posture-pattern-architecture SOURCES.md`,
  and `git diff --check`.

## Outcome and retrospective

- Pending. Fill only after implementation, review, verification, and PR handoff
  complete.

## Readiness

- See `Current Handoff Summary`.
- Ready for M3 code-review. Readiness is not Done; M3 review, M4,
  explain-change, verification, and PR handoff remain open.
