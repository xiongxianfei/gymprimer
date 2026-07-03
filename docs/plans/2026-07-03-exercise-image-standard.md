# Plan: Exercise Image Standard

## Status

- Status: active
- Plan lifecycle state: active
- Terminal disposition: not-applicable

## Purpose / big picture

Implement the approved Exercise Image Standard as a small-loop content and
validation program. The work should add exercise-specific media-purpose
validation, preserve existing exercise images without migration, create
authoring and review surfaces for future image batches, and then support
reviewable content batches only after the validation contract is in place.

This plan sequences implementation only. It does not reopen the accepted
direction, generate images immediately, optimize all exercise pages in one PR,
or convert GymPrimer into a hosted, visual-first, clinical, or coaching product.

## Source artifacts

- Proposal: `../proposals/2026-07-01-exercise-image-standard-and-optimization.md`
- Proposal review:
  - `../changes/exercise-image-standard-and-optimization/reviews/proposal-review-r1.md`
- Spec: `../../specs/exercise-image-standard.md`
- Spec review:
  - `../changes/exercise-image-standard-and-optimization/reviews/spec-review-r1.md`
  - `../changes/exercise-image-standard-and-optimization/reviews/spec-review-r2.md`
- Review resolution:
  - `../changes/exercise-image-standard-and-optimization/review-resolution.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review:
  - `../changes/exercise-image-standard-and-optimization/reviews/architecture-review-r1.md`
- ADR:
  - `../adr/2026-07-03-exercise-document-image-purposes.md`
- Governing specs:
  - `../../specs/markdown-first-primer.md`
  - `../../specs/responsible-breadth.md`
- Test spec: pending after plan review

## Context and orientation

GymPrimer is a Markdown-first repository. Exercise pages live under
`exercises/`, media assets live under `media/`, generated raster provenance is
centralized in `media/PROVENANCE.md`, and validation currently runs through
local Python checks and unittest coverage.

The current media checker is `tools/checks/check_markdown_first.py`. It already
loads `media/PROVENANCE.md`, validates local image references, classifies
raster extensions before provenance lookup, checks approved provenance rows,
and enforces context-sensitive media-purpose rules for existing Markdown-first
and Responsible Breadth pages.

The current media-purpose compatibility surface already includes
`equipment_identification` and `key_movement_illustration`. This plan must
preserve existing exercise images that use those purposes. Existing exercise
image references, assets, and provenance rows are not migration targets.

The exercise-image standard adds new generated raster purposes only for new
full exercise-document images:

- `exercise_setup_illustration`
- `exercise_movement_illustration`
- `exercise_muscle_attention_illustration`

The first implementation work should prove validation behavior with fixtures
before any generated image batch is added.

## Non-goals

- Do not change existing exercise image assets, Markdown image references, or
  provenance purpose values.
- Do not generate exercise images before validation, test-spec, and review
  gates are complete.
- Do not optimize every exercise page in one implementation loop.
- Do not add new exercise inventory.
- Do not add pattern-page, condition-page, video, animation, stock-photo, or
  hosted visual-delivery standards.
- Do not add a runtime app, CMS, database, user account, user-input flow,
  generated public JSON API, hosted media service, or personalized coaching.
- Do not let images carry diagnosis, treatment, cure, rehabilitation,
  programming, safety, anatomy, or technique claims as source-of-truth evidence.
- Do not promote README navigation from this change.

## Requirements covered

- R1-R6: M1 validates text-only exercise pages, optional image use, the normal
  zero-to-three image range, and one-primary-concept purpose routing.
- R7-R11 and R34: M1 validates the three new exercise-specific purposes, rejects
  pattern, condition, preview, vague, and unknown purposes for full exercise
  documents, and enforces one muscle-attention image per exercise page.
- R12-R14 and R28-R31: M2 defines review evidence and authoring surfaces for
  visual safety, support-only semantics, beginner comprehension checks, and
  manual criteria that cannot be fully automated.
- R15-R24: M1 validates repository-local image paths, `media/exercises/<slug>/`
  placement for new generated raster exercise images, provenance fields,
  approved review status, page-reference matching, and accountable human
  reviewer behavior where deterministic checks are feasible.
- R25-R27: M1 validates required non-generic alt text and muscle-attention alt
  text boundaries where deterministic checks are feasible.
- R32-R33 and AC6: M1 preserves existing `equipment_identification` and
  `key_movement_illustration` exercise image compatibility without migration.
- R35-R36: M1 provides stable automated failure categories for path, extension,
  alt-text, provenance, purpose, page-reference, image-count, and
  visual-safety-evidence checks.
- R37-R38: M1-M4 preserve no-secret, no-private-data, no-private-health-
  information, no-runtime, no-CMS, no-user-input, and no-personalized-coaching
  boundaries.
- AC1-AC12: M1-M4 provide acceptance evidence after plan review, test-spec
  review, implementation, code review, explain-change, and final verification.

## Current Handoff Summary

- Current milestone: M1
- Current milestone state: resolution-needed
- Last reviewed milestone: none
- Review status: proposal-review R1 approved; spec-review R2 approved after
  SR-EIS-1 resolution; architecture-review R1 approved; plan-review R1
  approved; test-spec-review R2 approved after TSR-EIS-1 resolution;
  code-review M1 R1 requested changes for CR-EIS-M1-1; owner directed broad
  privacy validation to move to verify-before-PR; test-spec-review R3
  requested changes for TSR-EIS-2
- Remaining in-scope implementation milestones: M1 resolution, M2-M4, and
  lifecycle closeout
- Next stage: test-spec revision
- Final closeout readiness: not ready
- Reason final closeout is or is not ready: M1 has an unresolved code-review
  finding, and the plan has not completed later milestones, explain-change,
  final verification, or PR handoff.

## Milestones

### M1. Exercise Image Validation Contract

- Milestone state: resolution-needed
- Goal: update automated validation and tests for the exercise-image media
  contract without changing existing exercise images.
- Requirements: R1-R11, R15-R27, R32-R38, AC1-AC8, AC10-AC12.
- Likely files:
  - `tools/checks/check_markdown_first.py`
  - `tests/test_markdown_first_guardrails.py`
  - `tests/test_responsible_breadth_m1.py`
  - optional focused fixture or test file under `tests/`
- Tests:
  - text-only exercise page passes exercise-image-specific media checks;
  - new setup, movement, and muscle-attention purposes pass for generated
    raster images on full exercise pages when provenance is approved;
  - existing `equipment_identification` and `key_movement_illustration`
    exercise images continue to pass without media-purpose migration;
  - pattern, condition, preview, vague, and unknown purposes fail on full
    exercise pages;
  - two muscle-attention images fail;
  - four exercise images fail unless an approved downstream exception is
    explicitly represented;
  - missing, empty, or generic alt text fails;
  - remote image references, paths outside `media/`, unsupported extensions,
    missing local assets, missing provenance, incomplete provenance,
    non-approved provenance, and page-reference mismatches fail;
  - generated raster exercise image reviewer checks reject AI-tool reviewers
    where deterministic reviewer-field validation is implemented.
  - template-aware checker support proves `docs/templates/` can be validated
    without treating placeholder/template language as promoted product content.
- Steps:
  - Add exercise-specific purpose constants and page-context checks.
  - Add image counting and muscle-attention counting for exercise documents.
  - Add generic alt-text rejection for image references.
  - Add new generated raster exercise path checks without requiring migration
    for existing exercise images.
  - Add template path classification or equivalent checker support for
    `docs/templates/`, with tests that accept template placeholders while still
    rejecting real media-contract violations in templates.
  - Preserve existing checker behavior for non-exercise page classes.
  - Add regression tests before or alongside the implementation.
- Validation:
  - `python3 -m unittest tests.test_markdown_first_guardrails tests.test_responsible_breadth_m1`
  - `python3 -m unittest discover tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  - scoped current-change privacy scan as needed for review hygiene; broad
    EIS-CMD4 privacy validation is deferred to lifecycle closeout / verify
- Result: Implemented checker and focused regression coverage for the
  exercise-image validation contract; code-review M1 R1 requested
  review-resolution for CR-EIS-M1-1.
- Risks: checker overreach could fail legacy-compatible exercise images or
  non-exercise page classes.
- Rollback: revert M1 checker and test changes; leave existing content and
  media untouched.

### M2. Authoring Guidance and Review Evidence Surfaces

- Milestone state: planned
- Goal: add the durable Markdown guidance needed before generated exercise
  images can be reviewed consistently.
- Requirements: R2-R6, R12-R14, R25-R31, R37-R38, AC9-AC12.
- Likely files:
  - `docs/templates/exercise-card.md`
  - `docs/changes/exercise-image-standard-and-optimization/`
  - optional `media/PROVENANCE.md` guidance-only notes if an existing local
    convention requires them
- Tests:
  - static checks continue to pass for template and review-evidence text after
    M1 template-aware checker support is in place;
  - privacy checks pass over the new review evidence surfaces;
  - no generated images or exercise-page media references are added in this
    milestone.
- Steps:
  - Add optional exercise-image block guidance to the exercise template.
  - Add a change-local visual-safety review checklist template or evidence
    stub for later image batches.
  - Add beginner comprehension evidence prompts for material image batches.
  - Keep all guidance Markdown-first, citation-aware, non-clinical, and
    support-only.
- Validation:
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates media/PROVENANCE.md`
  - `python3 tools/checks/check_privacy.py -- docs/templates docs/changes/exercise-image-standard-and-optimization`
- Result: pending
- Risks: guidance could accidentally imply images are required or that they
  replace Markdown citations.
- Rollback: remove the template and evidence-surface additions; keep M1
  validation intact.

### M3. First New Exercise Image Batch

- Milestone state: planned
- Goal: add a small reviewed batch for the five forward-head support exercises
  only after M1 and M2 are closed.
- Requirements: R1-R31, R35-R38, AC1-AC12.
- Target exercise pages:
  - `exercises/chin-nod.md`
  - `exercises/thoracic-extension.md`
  - `exercises/wall-slide.md`
  - `exercises/prone-y-t.md`
  - `exercises/band-pull-apart.md`
- Likely files:
  - target exercise pages listed above;
  - new assets under `media/exercises/<exercise-slug>/`;
  - `media/PROVENANCE.md`;
  - visual-safety and beginner comprehension evidence under
    `docs/changes/exercise-image-standard-and-optimization/`.
- Tests:
  - validation accepts every new asset path and provenance row;
  - each generated raster row has approved status, exact `asset_path`,
    permitted exercise purpose, accountable human reviewer, and referencing
    `page_refs`;
  - pages stay readable as Markdown and keep claims in text;
  - visual-safety evidence covers every image;
  - beginner comprehension evidence is recorded for the batch.
- Steps:
  - Choose the minimum needed images for each target page.
  - Generate or add only approved images that pass visual-safety review.
  - Add Markdown references, alt text, and nearby explanatory text without
    unsupported new claims.
  - Add exact provenance rows.
  - Record visual-safety and beginner comprehension evidence.
- Validation:
  - `python3 -m unittest discover tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  - `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md docs/changes/exercise-image-standard-and-optimization exercises media/PROVENANCE.md`
- Result: pending
- Risks: generated images may imply unsupported anatomy, correction, treatment,
  brands, or identifiable people.
- Rollback: remove the Markdown image references, remove unused assets, remove
  or revise provenance rows, retain the text-only exercise pages, and rerun M3
  validation.

### M4. Remaining Exercise Audit and Follow-up Routing

- Milestone state: planned
- Goal: audit all current `exercises/*.md` pages under the accepted standard
  without forcing existing image migration or a broad all-pages media rewrite.
- Requirements: R1-R6, R32-R38, AC2-AC6, AC10-AC12.
- Likely files:
  - `docs/changes/exercise-image-standard-and-optimization/`
  - possible focused follow-up notes in the plan body
- Tests:
  - audit evidence records each current exercise page as `no image needed`,
    `keep existing image`, `candidate setup image`, `candidate movement image`,
    `candidate muscle-attention image`, or `needs future batch`;
  - existing images using legacy-compatible purposes remain untouched;
  - no page is modified solely for media-purpose migration.
- Steps:
  - Inventory current exercise pages and current image references.
  - Record the minimum necessary image category per page.
  - Split any future image work into small implementation loops under this
    proposal and plan rather than creating new proposals for small batches.
  - Update the plan if the audit reveals a new scope class that exceeds full
    exercise-document images.
- Validation:
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`
  - `python3 tools/checks/check_privacy.py -- docs/changes/exercise-image-standard-and-optimization exercises media/PROVENANCE.md`
- Result: pending
- Risks: audit notes could become a hidden backlog without reviewable
  milestones.
- Rollback: remove or revise audit evidence; keep implemented validation and
  reviewed image batches intact.

### Lifecycle Closeout

- Milestone state: planned
- Goal: close the plan only after all in-scope implementation milestones are
  closed and downstream rationale, verification, and PR handoff are complete.
- Requirements: AC1-AC12.
- Likely files:
  - `docs/plans/2026-07-03-exercise-image-standard.md`
  - `docs/plan.md`
  - `docs/changes/exercise-image-standard-and-optimization/`
- Tests:
  - final validation commands match the implemented milestone set;
  - review logs and plan status agree.
- Steps:
  - Run explain-change after implementation reviews are clean.
  - Run verify before PR handoff.
  - Update plan status only after downstream evidence supports the transition.
- Validation:
  - final validation commands approved by the test spec and verify stage
- Result: pending
- Risks: marking readiness as Done before review, verification, or PR handoff.
- Rollback: restore active lifecycle state and name the remaining gate.

## Validation plan

Before implementation, create and review a test spec that maps spec
requirements and acceptance criteria to exact automated tests, manual
visual-safety evidence, beginner comprehension evidence, and validation
commands.

Expected local command set after implementation begins:

- `python3 -m unittest tests.test_markdown_first_guardrails tests.test_responsible_breadth_m1`
- `python3 -m unittest discover tests`
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
- `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/exercise-image-standard-and-optimization docs/plans media exercises tools tests`

Manual evidence is required for visual semantics and beginner comprehension
when generated image batches are added.

## Risks and recovery

- Legacy image migration churn: M1 and M4 explicitly preserve existing
  `equipment_identification` and `key_movement_illustration` exercise images.
- Checker false positives: add fixture coverage for old and new media-purpose
  behavior before broad content edits.
- Visual-safety gaps: require manual image evidence before promotion because
  static checks cannot prove all visual semantics.
- Provenance drift: validate exact `asset_path`, required fields,
  `review_status`, and `page_refs`.
- Large content PR risk: keep generated image batches small and reviewable.
- Source-support drift near images: keep claims in Markdown and use page-local
  sources; images cannot introduce new claims.

## Dependencies

- Plan-review must approve this plan before test-spec authoring.
- Test-spec and test-spec-review must complete before implementation.
- M3 depends on M1 and M2 closure.
- M4 depends on M1 closure and should run after at least one validated image
  batch unless owner direction changes.
- Generated image batches require an accountable human reviewer identity for
  provenance and review evidence.

## Progress

- 2026-07-02: Proposal review R1 approved the Exercise Image Standard proposal.
- 2026-07-03: Spec review R2 approved the spec after SR-EIS-1 resolution.
- 2026-07-03: Architecture review R1 approved the canonical architecture
  amendment and ADR.
- 2026-07-03: Architecture status was normalized to approved and the ADR was
  normalized to accepted before planning.
- 2026-07-03: Execution plan drafted for plan review.
- 2026-07-03: Plan review R1 approved the execution plan.
- 2026-07-03: Test spec drafted for test-spec review.
- 2026-07-03: Test-spec review R1 requested changes for template-aware checker
  command ownership; the test spec and plan were revised to make that support
  an explicit M1/M2 implementation obligation.
- 2026-07-03: Test-spec review R2 approved the revised proof map for M1
  implementation handoff.
- 2026-07-03: M1 implemented exercise-image media-purpose validation,
  generated-raster provenance checks, image count and muscle-attention limits,
  generic and unsafe alt-text rejection, legacy-purpose compatibility, and
  template-aware checker support; code-review is next.
- 2026-07-03: Code-review M1 R1 requested review-resolution for CR-EIS-M1-1
  because the required broad EIS-CMD4 privacy command fails on pre-existing
  superseded-plan examples.
- 2026-07-03: Owner directed broad privacy validation to happen during verify
  before PR rather than blocking M1. The test spec and plan were revised to
  move EIS-CMD4 to lifecycle closeout / verify and need test-spec-review before
  M1 code-review re-review.
- 2026-07-03: Test-spec-review R3 requested test-spec revision for TSR-EIS-2
  because the plan still lists broad EIS-CMD4 as an implementation-start
  command.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-03 | Put validation before generated image batches. | The spec changes media-purpose and provenance behavior, so fixtures should prove the contract before content changes. | Generate images first; mix checker changes and image batch in one PR. |
| 2026-07-03 | Preserve existing exercise images without migration. | The approved spec says existing `equipment_identification` and `key_movement_illustration` exercise images remain valid. | Rename old purposes opportunistically; require migration when pages are touched. |
| 2026-07-03 | Use one plan with small implementation milestones. | The accepted proposal keeps one coherent product decision while avoiding broad implementation PRs. | One large all-exercise optimization PR; separate proposals for small batches. |

## Surprises and discoveries

- The existing checker already centralizes raster provenance and
  context-sensitive media-purpose validation, so M1 can extend current
  behavior rather than adding a new validator.
- `docs/templates/exercise-card.md` exists and is the likely authoring surface
  for optional image guidance.
- Template validation needed a path-context boundary: template files should not
  be treated as promoted product pages, but their image references still need
  normal media-contract validation.

## Validation notes

- Before checker changes, `python3 -m unittest tests.test_exercise_image_standard`
  failed with the expected missing M1 behavior for new exercise purposes,
  image-count limits, generic and unsafe alt text, and template placeholder
  handling.
- After implementation, `python3 -m unittest tests.test_exercise_image_standard`
  passed with 7 focused M1 tests.
- After implementation,
  `python3 -m unittest tests.test_markdown_first_guardrails tests.test_responsible_breadth_m1 tests.test_exercise_image_standard`
  passed with 51 tests.
- After implementation,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed, checking 25 Markdown files.
- After implementation,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates media/PROVENANCE.md`
  passed, checking 10 Markdown files.
- After implementation, `python3 -m unittest discover tests` passed with 95
  tests.
- After implementation, `git diff --check` passed.
- Before the validation-path amendment, the broad planned privacy command
  `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/exercise-image-standard-and-optimization docs/plans media exercises tools tests`
  failed on pre-existing forbidden-pattern examples in the superseded
  `docs/plans/2026-06-26-content-schema-foundation.md` plan.
- Owner subsequently directed this broad privacy sweep to move to final verify
  before PR instead of M1 closeout.
- The scoped current-change privacy command
  `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/exercise-image-standard-and-optimization docs/plans/2026-07-03-exercise-image-standard.md media exercises tools tests`
  passed, checking 113 files.

## Outcome and retrospective

Pending. This plan is not complete until all in-scope milestones, reviews,
explain-change, verification, and PR handoff are complete.

## Readiness

See Current Handoff Summary for the live next stage. This plan is ready for
test-spec revision, not final closeout.
