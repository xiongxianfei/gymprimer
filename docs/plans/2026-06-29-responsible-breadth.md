# Plan: Responsible Breadth Content Expansion

## Status

- Status: active
- Plan lifecycle state: active
- Terminal disposition: not-applicable

## Purpose / big picture

Implement the approved Responsible Breadth direction as a narrow
Markdown-first proof slice. The work should expand GymPrimer from the original
five-page exercise-literacy slice into static, citation-backed education for
one red-flags reference, one pattern page, one condition page, one programming
principle, and one static program example.

This plan sequences implementation only. It does not reopen the accepted
direction, broaden the first slice, introduce symptom checking, create a
personalized coach, or publish expanded pages before proof and review exist.

## Source artifacts

- Proposal: `../proposals/2026-06-29-responsible-breadth.md`
- Proposal review:
  - `../changes/responsible-breadth/reviews/proposal-review-r3.md`
- Spec: `../../specs/responsible-breadth.md`
- Spec review:
  - `../changes/responsible-breadth/reviews/spec-review-r2.md`
- Compatibility spec: `../../specs/markdown-first-primer.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review:
  - `../changes/responsible-breadth/reviews/architecture-review-r1.md`
- ADR: `../adr/2026-06-29-responsible-breadth-static-content-boundaries.md`
- Existing Markdown-first ADRs:
  - `../adr/2026-06-27-markdown-first-citation-based-authority.md`
  - `../adr/2026-06-28-ai-generated-raster-media-provenance.md`
- Test spec: `../../specs/responsible-breadth.test.md`

## Context and orientation

The original Markdown-first v0.1 plan remains a separate active track for the
first five beginner pages. Responsible Breadth must not invalidate that slice.
This plan targets only the expanded static-content surface defined by
`specs/responsible-breadth.md`.

Architecture has fixed these implementation boundaries:

- Expanded pages are Markdown source files under `patterns/`, `conditions/`,
  `principles/`, `programs/`, and `exercises/`.
- `about/` owns red flags and shared project-level references.
- `SOURCES.md` remains the reusable source index.
- `media/PROVENANCE.md` remains the AI-raster provenance contract.
- `docs/changes/responsible-breadth/manual-proof/` owns semantic proof records.
- README, SUMMARY, or other active navigation must not promote expanded pages
  until the slice passes the reviewed workflow.

The first expanded proof slice is intentionally smaller than the proposal's
full first content slice:

- `about/red-flags.md`
- `patterns/anterior-pelvic-tilt.md`
- `conditions/non-specific-chronic-low-back-pain.md`
- `principles/how-many-days-a-week.md`
- `programs/generic-3-day-full-body-example.md`

Implementation must wait for test-spec-review approval before code or content
changes begin.

## Non-goals

- Do not implement a symptom checker, diagnostic decision tree, user-input
  router, account system, CMS, API, hosted app, analytics, or search index.
- Do not publish diagnosis, individualized medical advice, treatment plans,
  return-to-training prescriptions, active rehabilitation protocols,
  posture-correction promises, injury-specific protocols, or personalized
  programming.
- Do not add acute injury, post-surgical, pediatric, pregnancy,
  oncology-related, mental-health-treatment, sport-specific, or specialized
  population content.
- Do not scale beyond the five-page expanded proof slice in this plan.
- Do not add exercise visual-standard pages in this slice except for validation
  compatibility and templates needed to keep the architecture coherent.
- Do not add AI-generated content as source of truth.
- Do not claim CI passed unless a real CI run is observed.

## Requirements covered

- R1-R4: M1-M4 establish expanded Markdown source paths and the exact first
  proof slice.
- R5-R10: M1-M3 cover pattern/condition page contracts, non-diagnostic framing,
  red-flag routing, and condition/pattern scope.
- R11-R14: M1-M3 cover programming-principle and program-example boundaries.
- R15-R22: M1-M3 cover source count, source quality, source-index validity,
  safety citations, and uncertainty language.
- R23-R28: M1 and M4 cover review metadata, cadence, and triggered review proof.
- R29-R35: M1 and M4 cover visual necessity and inherited media provenance
  behavior; no media may bypass the Markdown-first provenance contract.
- R36-R37: M1 and M4 cover higher-bar review checks.
- R38-R40: M1-M4 preserve excluded-scope and no-runtime-product guardrails.
- R41-R46: M1-M4 cover promotion gating, manual comprehension proof, and
  semantic manual proof.
- R47-R49: M2-M3 cover red-flags reference behavior and reusable sources.
- R50: M4 covers navigation promotion only after evidence exists.
- R51-R56: M1-M4 cover page-class classification, Markdown-first inheritance,
  and original v0.1 preservation.
- AC1-AC10 and AC-COMP-1 through AC-COMP-10: M1-M4 plus the pending test-spec
  and reviews provide acceptance evidence.

## Current Handoff Summary

- Current milestone: lifecycle closeout
- Current milestone state: verified
- Last reviewed milestone: final holistic code-review
- Review status: plan-review R1 approved; test-spec-review R1 blocked on
  TSR-RB-1, TSR-RB-1 was resolved by lifecycle/status normalization, and
  test-spec-review R2 approved the proof map
- Remaining in-scope implementation milestones: none
- Next stage: pr
- Final closeout readiness: branch-ready for PR handoff
- Reason final closeout is or is not ready: The execution plan is approved and
  the test spec is approved, M1 is closed after code-review M1 R1, M2 is
  closed after code-review M2 R1, M3 is closed after code-review M3 R1, M4 is
  closed after code-review M4 R1, final holistic code-review R1 is clean,
  explain-change is complete, and verify passed with fresh local evidence in
  `../changes/responsible-breadth/verify-report.md`. The auto-through profile
  stops before PR, so PR preparation requires separate authorization.

## Milestones

### M1. Responsible Breadth Validation and Proof Scaffold

- Milestone state: closed
- Goal: Extend the local Markdown-first validation and proof structure so
  expanded pages can be classified, checked, and manually reviewed before
  content is promoted.
- Requirements: R1-R2, R5-R8, R15-R23, R29-R37, R41-R46, R51-R56,
  AC5-AC8, AC-COMP-8 through AC-COMP-10
- Files/components likely touched:
  - `tools/checks/check_markdown_first.py`
  - `tests/test_responsible_breadth_*.py`
  - `tests/fixtures/responsible-breadth/`
  - `docs/changes/responsible-breadth/manual-proof/README.md`
  - `docs/templates/`
- Dependencies:
  - Clean plan-review.
  - Responsible Breadth test-spec and test-spec-review.
- Tests to add/update:
  - Page-class path classification fixtures.
  - Missing required section fixtures.
  - Missing red-flag link fixtures.
  - Missing metadata and review-cadence fixtures.
  - Source-count/source-index fixtures for expanded pages.
  - Excluded diagnosis, treatment, rehab, and personalized-programming fixtures.
- Implementation steps:
  - Add or extend checker rules for Responsible Breadth page classification.
  - Add structural checks for required pattern/condition sections.
  - Add metadata checks for author, created date, last reviewed, next review,
    and review scope.
  - Add red-flags ordering checks for safety-relevant expanded pages.
  - Add source-count and source-index checks for expanded page classes.
  - Add proof-record scaffolding for source quality, scope boundary, visual
    necessity, review cadence, and comprehension outcomes.
- Validation commands:
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py --help`
  - `python3 tools/checks/check_privacy.py docs/changes/responsible-breadth specs/responsible-breadth.md specs/markdown-first-primer.md`
- Expected observable result: Invalid expanded-page fixtures fail with stable
  messages, valid fixtures pass, and manual proof scaffolding exists before
  content pages rely on it.
- Commit message: `M1: add Responsible Breadth validation scaffold`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Overloading the Markdown-first checker could make original v0.1 pages fail
    expanded rules.
  - Structural checks cannot prove semantic source quality.
- Rollback/recovery:
  - Keep Responsible Breadth checks path-scoped to expanded directories.
  - Revert or disable only expanded-scope checks while preserving existing
    Markdown-first validation.

### M2. Project-Level References, Templates, and Source Seed

- Milestone state: closed
- Goal: Create the reusable references and authoring templates needed before
  expanded content pages can be drafted.
- Requirements: R3-R4, R5-R14, R15-R23, R36-R37, R47-R49, R51-R56,
  AC4-AC7, AC-COMP-1 through AC-COMP-10
- Files/components likely touched:
  - `about/red-flags.md`
  - `about/sources.md` or equivalent shared source guidance if selected by
    implementation
  - `docs/templates/pattern-page.md`
  - `docs/templates/condition-page.md`
  - `docs/templates/programming-principle-page.md`
  - `docs/templates/program-example-page.md`
  - `SOURCES.md`
  - `CONTRIBUTING.md`
- Dependencies:
  - M1 scaffold complete.
- Tests to add/update:
  - Template structure tests.
  - Red-flags reference structural checks.
  - Source-index reuse checks.
- Implementation steps:
  - Write `about/red-flags.md` with emergency, prompt medical care, and
    professional assessment routing in plain language.
  - Add expanded page templates with required sections and metadata fields.
  - Seed `SOURCES.md` with reusable institutional/public-health sources used by
    the first expanded slice.
  - Update contributor guidance for higher-bar pattern, condition, and program
    review.
  - Record manual proof that red-flags language does not diagnose or triage the
    reader.
- Validation commands:
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - `python3 tools/checks/check_markdown_first.py SOURCES.md about`
  - `python3 tools/checks/check_privacy.py SOURCES.md CONTRIBUTING.md about docs/templates docs/changes/responsible-breadth`
- Expected observable result: The red-flags reference, source seed, contributor
  guidance, and templates pass structural/privacy checks and can be used by the
  first expanded pages.
- Commit message: `M2: add Responsible Breadth references and templates`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Red-flags language may drift into triage or diagnosis.
  - Templates may become too verbose for beginners.
- Rollback/recovery:
  - Remove active navigation to the references.
  - Keep templates draft-only until revised.

### M3. First Expanded Proof Slice Content

- Milestone state: closed
- Goal: Draft and validate the four expanded content pages that depend on the
  red-flags reference: one pattern, one condition, one principle, and one static
  program example.
- Requirements: R1-R28, R36-R49, R51-R56, AC4-AC10, AC-COMP-1 through
  AC-COMP-10
- Files/components likely touched:
  - `patterns/anterior-pelvic-tilt.md`
  - `conditions/non-specific-chronic-low-back-pain.md`
  - `principles/how-many-days-a-week.md`
  - `programs/generic-3-day-full-body-example.md`
  - `SOURCES.md`
  - `docs/changes/responsible-breadth/manual-proof/`
- Dependencies:
  - M1 scaffold complete.
  - M2 red-flags reference, source seed, and templates complete.
- Tests to add/update:
  - Real-page integration tests over the first expanded proof slice.
  - Source-index and page-local source tests over real expanded pages.
  - Excluded-scope negative scans over real expanded pages.
- Implementation steps:
  - Draft the pattern page with non-diagnostic framing, red-flag routing,
    source-quality minimums, uncertainty language, and professional routing.
  - Draft the condition page with consumer-education framing, red-flag routing,
    source-quality minimums, uncertainty language, and no treatment plan.
  - Draft the programming-principle page with cited general ranges and no
    individualized recommendation.
  - Draft the program-example page as a static worked example with no user input
    or symptom adaptation.
  - Record manual source-quality, scope-boundary, and comprehension proof.
- Validation commands:
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py SOURCES.md about patterns conditions principles programs`
  - `python3 tools/checks/check_privacy.py SOURCES.md about patterns conditions principles programs docs/changes/responsible-breadth`
- Expected observable result: The first expanded content pages pass automated
  checks, include required manual proof, and remain draft-only until M4
  promotion.
- Commit message: `M3: draft Responsible Breadth proof slice`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Pages may sound like diagnosis, treatment, or prescription despite
    structural compliance.
  - Source quality may pass count checks while failing semantic review.
- Rollback/recovery:
  - Mark any failing page draft-only or remove active links.
  - Narrow or remove self-management discussion before re-review.

### M4. Promotion Gate and Final Local Quality Ledger

- Milestone state: closed
- Goal: Promote only the validated first expanded proof slice, record final
  evidence, and keep navigation and generated-output boundaries coherent.
- Requirements: R24-R28, R34-R35, R41-R46, R50-R56, AC1-AC10,
  AC-COMP-1 through AC-COMP-10
- Files/components likely touched:
  - `README.md`
  - `SUMMARY.md` if mdBook is active or selected later
  - `docs/changes/responsible-breadth/manual-proof/`
  - `docs/changes/responsible-breadth/verify-report.md` later during verify,
    not during implementation
  - `docs/plans/2026-06-29-responsible-breadth.md`
- Dependencies:
  - M1-M3 complete and reviewed.
- Tests to add/update:
  - README/navigation promotion tests.
  - Source-of-truth drift checks for expanded pages.
  - Final validation ledger checks.
- Implementation steps:
  - Link the first expanded slice from active navigation only after proof is
    complete.
  - Record a final local validation ledger for all Responsible Breadth commands
    and manual proofs.
  - Record mdBook build or deferral if expanded navigation touches mdBook
    surfaces.
  - Confirm no expanded page is promoted without review metadata, source proof,
    red-flag routing, and comprehension evidence.
- Validation commands:
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md about patterns conditions principles programs`
  - `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md about patterns conditions principles programs docs/changes/responsible-breadth media`
  - `command -v mdbook || true`
  - `mdbook build` if mdBook is configured; otherwise record explicit deferral
- Expected observable result: The expanded proof slice is promoted only after
  complete automated and manual evidence, and final local quality evidence is
  current for code review and later verification.
- Commit message: `M4: promote Responsible Breadth proof slice`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Navigation may promote pages before evidence is complete.
  - mdBook or generated output may look canonical.
- Rollback/recovery:
  - Remove expanded-page links from active navigation.
  - Keep pages as draft Markdown with correction history.

## Validation plan

- `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`:
  Responsible Breadth fixture and real-page tests after test-spec adds them.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`:
  regression coverage for inherited Markdown-first behavior.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md about patterns conditions principles programs`:
  structural, source, scope, media, and promotion checks once paths exist.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md about patterns conditions principles programs docs/changes/responsible-breadth media`:
  negative-match privacy scan for content and proof records once paths exist.
- `command -v mdbook || true`: determine whether mdBook can be attempted.
- `mdbook build`: run only if mdBook is configured and available; otherwise
  record explicit deferral.
- Manual source-quality review: required for every expanded page before
  promotion.
- Manual scope-boundary review: required for every pattern, condition, and
  program-example page before promotion.
- Manual comprehension proof: required for every page in the first expanded
  proof slice before promotion.
- Manual artifact lifecycle state-sync check: before downstream handoff,
  confirm proposal accepted, spec approved, architecture approved, ADR accepted,
  plan index updated, change metadata current, and no open review-resolution
  findings.

## Risks and recovery

- Risk: Expanded health-adjacent pages drift into diagnosis, treatment, rehab,
  or personalized advice.
  - Recovery: Remove active navigation, mark page draft-only, narrow language,
    and rerun higher-bar review.
- Risk: Source count passes while source quality is weak.
  - Recovery: Block promotion until manual proof confirms institutional,
    guideline, patient-education, public-health, or professional-source mix.
- Risk: Check tooling accidentally applies Responsible Breadth rules to the
  original v0.1 slice.
  - Recovery: Scope expanded checks by path/classification and preserve
    Markdown-first tests as regression coverage.
- Risk: Red-flags reference reads like triage.
  - Recovery: Rewrite to route to professional/emergency care without deciding
    what the reader has.
- Risk: Navigation promotes draft expanded pages.
  - Recovery: Remove links from README/SUMMARY and keep pages draft-only until
    proof and review are complete.
- Risk: Manual proof records expose private health details.
  - Recovery: Redact and replace with non-identifying evidence; rerun privacy
    checks.

## Dependencies

- Clean plan-review before test-spec.
- Responsible Breadth test-spec and test-spec-review before implementation.
- Existing Markdown-first checker and privacy checker remain available.
- Source selection must use public, named, authoritative sources; link-health
  gaps must be recorded when network-dependent checks are unavailable.
- mdBook remains optional and derived; absence of `mdbook` requires a deferral
  record instead of a silent pass.

## Progress

- 2026-06-29: Proposal accepted after proposal-review R3.
- 2026-06-29: Spec approved after spec-review R2.
- 2026-06-29: Architecture and ADR approved by architecture-review R1.
- 2026-06-29: Plan drafted for plan-review.
- 2026-06-29: Plan-review R1 and test-spec-review R2 approved downstream
  implementation handoff for M1.
- 2026-06-29: M1 implemented path-scoped Responsible Breadth checker rules,
  M1 test coverage, and the manual proof scaffold; M1 is ready for
  code-review.
- 2026-06-29: Code-review M1 R1 closed M1 with no material findings.
- 2026-06-29: M2 implemented `about/red-flags.md`, Responsible Breadth page
  templates, reusable source-index seed entries, contributor higher-bar review
  guidance, and RB-MP1 red-flags manual proof; M2 is ready for code-review.
- 2026-06-29: Code-review M2 R1 closed M2 with no material findings.
- 2026-06-29: M3 implemented the first expanded proof-slice pages and
  RB-MP2 through RB-MP7 manual proof records; M3 is ready for code-review.
- 2026-06-29: Code-review M3 R1 closed M3 with no material findings.
- 2026-06-29: M4 promoted the Responsible Breadth proof-slice pages from
  README, recorded the final validation ledger, and recorded mdBook deferral;
  M4 is ready for code-review.
- 2026-06-29: Code-review M4 R1 closed M4 with no material findings.
- 2026-06-29: Final holistic code-review R1 passed with no material findings.
- 2026-06-29: Explain-change refreshed the durable rationale for the final
  reviewed diff.
- 2026-06-29: APT follow-up amendment implemented RB-T21/RB-T22 proof for the
  pattern-page reader journey, exercise preview annotations, existing exercise
  targets, and expanded raster media-purpose validation. The follow-up is ready
  for code-review and does not reopen original M1-M4 scope.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-29 | Sequence validation/proof scaffold before content pages. | Expanded pages need deterministic structural checks and manual proof surfaces before content can be promoted safely. | Draft content first and retrofit checks later. |
| 2026-06-29 | Keep the first implementation slice to one red-flags reference plus four expanded pages. | Matches the approved spec and reduces safety/source-review load before scaling. | Implement the broader proposal first slice with exercises and visuals immediately. |
| 2026-06-29 | Keep expanded pages draft-only until M4 promotion. | Prevents README/SUMMARY from advertising health-adjacent content before proof, review, and validation exist. | Link pages as soon as they are drafted. |

## Aligned surface audit

- `specs/responsible-breadth.md`: unaffected; M1 implements existing R1-R2,
  R5-R8, R15-R23, R29-R37, R41-R46, and R51-R56 proof obligations without
  changing requirements.
- `specs/responsible-breadth.test.md`: unaffected; M1 implements RB-T1 through
  RB-T7 coverage and does not change test mappings.
- `docs/architecture/system/architecture.md`: unaffected; M1 follows the
  existing path-classification and Markdown-first validation boundary.
- `docs/templates/`: unaffected in M1; template creation remains M2 scope.
- M2 touched `about/red-flags.md`, `docs/templates/`, `SOURCES.md`,
  `CONTRIBUTING.md`, and `docs/changes/responsible-breadth/manual-proof/`
  exactly as planned.
- M3 touched `patterns/`, `conditions/`, `principles/`, `programs/`,
  `SOURCES.md`, and M3 manual proof records exactly as planned.
- M4 touched `README.md`, RB-MP8, RB-MP9, tests, and routing metadata exactly
  as planned; no `SUMMARY.md`, `book.toml`, generated HTML, or media files were
  added.
- APT follow-up touched `patterns/anterior-pelvic-tilt.md`,
  `media/PROVENANCE.md`, generated raster preview assets,
  `tools/checks/check_markdown_first.py`, Responsible Breadth tests, and
  change-local proof/rationale. Constitution, vision, proposal, spec,
  architecture, ADR, and original M1-M4 scope are unaffected.

## Surprises and discoveries

- Existing Markdown-first v0.1 excluded-scope terms had to stay active for the
  original slice but be path-scoped away from Responsible Breadth pages, where
  stricter RB guardrails now apply.
- Fixture helpers needed explicit left-aligned Markdown strings; interpolated
  multiline source blocks made `textwrap.dedent` unreliable for this test
  shape.
- `about/red-flags.md` can pass the inherited Markdown-first checker as a
  project-level Markdown page by keeping a prominent disclaimer, page-local
  citations, and wording that avoids v0.1 excluded-scope terms.
- The first expanded proof-slice pages can remain text-only for M3; RB-MP7
  records a no-media note, so media provenance is not required yet.
- `command -v mdbook || true` returned exit 0 with no path output, so M4 uses
  an explicit mdBook deferral rather than claiming a build.

## Validation notes

- 2026-06-29 M1 validation:
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
    passed: 9 tests.
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
    passed: 51 tests.
  - `python3 tools/checks/check_markdown_first.py --help` passed.
  - `python3 tools/checks/check_privacy.py docs/changes/responsible-breadth specs/responsible-breadth.md specs/markdown-first-primer.md`
    passed: checked 15 files.
- 2026-06-29 M2 validation:
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
    passed: 12 tests.
  - `python3 tools/checks/check_markdown_first.py SOURCES.md about` passed:
    checked 2 Markdown files.
  - `python3 tools/checks/check_privacy.py SOURCES.md CONTRIBUTING.md about docs/templates docs/changes/responsible-breadth`
    passed: checked 24 files.
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
    passed: 51 tests.
- 2026-06-29 M3 validation:
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
    passed: 15 tests.
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
    passed: 51 tests.
  - `python3 tools/checks/check_markdown_first.py SOURCES.md about patterns conditions principles programs`
    passed: checked 6 Markdown files.
  - `python3 tools/checks/check_privacy.py SOURCES.md about patterns conditions principles programs docs/changes/responsible-breadth`
    passed: checked 28 files.
- 2026-06-29 M4 validation:
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
    passed: 15 tests.
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
    passed: 51 tests.
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md about patterns conditions principles programs`
    passed: checked 7 Markdown files.
  - `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md about patterns conditions principles programs docs/changes/responsible-breadth media`
    passed: checked 47 files.
  - `command -v mdbook || true` passed with no path output; RB-MP9 records
    explicit deferral.
- 2026-06-29 APT follow-up validation:
  - `python3 -m unittest discover -s tests` passed: 131 tests.
  - `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
    passed: 20 tests.
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
    passed: 51 tests.
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md about patterns conditions principles programs exercises`
    passed: checked 13 Markdown files.
  - `python3 tools/checks/check_privacy.py README.md SOURCES.md about patterns conditions principles programs exercises docs/templates docs/changes/apt-pattern-architecture docs/changes/responsible-breadth docs/plans/2026-06-29-responsible-breadth.md docs/plan.md media tools/checks/check_markdown_first.py tests/test_responsible_breadth_m1.py`
    passed: checked 90 files.
  - `git diff --check` passed.

## Outcome and retrospective

- Pending implementation and final verification.

## Readiness

- See `Current Handoff Summary`.
- Ready for verify only. Not branch-ready, PR-ready, or Done until verify
  completes.
