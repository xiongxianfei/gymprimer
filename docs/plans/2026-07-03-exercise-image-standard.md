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
  - `../changes/exercise-image-standard-and-optimization/reviews/spec-review-r3.md`
  - `../changes/exercise-image-standard-and-optimization/reviews/spec-review-r4.md`
- Review resolution:
  - `../changes/exercise-image-standard-and-optimization/review-resolution.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review:
  - `../changes/exercise-image-standard-and-optimization/reviews/architecture-review-r1.md`
  - `../changes/exercise-image-standard-and-optimization/reviews/architecture-review-r2.md`
- ADR:
  - `../adr/2026-07-03-exercise-document-image-purposes.md`
  - `../adr/2026-07-03-generated-raster-prompt-records.md`
- Governing specs:
  - `../../specs/markdown-first-primer.md`
  - `../../specs/responsible-breadth.md`
- Test spec: `../../specs/exercise-image-standard.test.md`; prompt-record
  proof map approved by test-spec-review R5

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

The prompt-record amendment adds a required `prompt_record` field for generated
raster exercise images governed by the amendment. The field points from
`media/PROVENANCE.md` to a repository-local Markdown prompt record under
`media/prompts/exercises/<exercise-slug>/<asset-stem>.md`, and that prompt
record must point back to the same normalized `asset_path`. The current checker
and provenance table do not yet implement that contract, so prompt-record work
must be sequenced before the current M3 image batch returns to code-review.

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
- R15-R20 and R21-R24: M1 validates repository-local image paths,
  `media/exercises/<slug>/` placement for new generated raster exercise
  images, baseline provenance fields, approved review status, page-reference
  matching, and accountable human reviewer behavior where deterministic checks
  are feasible.
- R20A-R20H and AC5A: M3A validates `prompt_record` provenance links,
  repository-local prompt-record path shape, reverse `asset_path` matching,
  exact full prompt text or explicit redaction notes, and no reader-facing
  prompt embedding.
- R25-R27: M1 validates required non-generic alt text and muscle-attention alt
  text boundaries where deterministic checks are feasible.
- R32-R33 and AC6: M1 preserves existing `equipment_identification` and
  `key_movement_illustration` exercise image compatibility without migration.
- R35-R36: M1 provides stable automated failure categories for path, extension,
  alt-text, provenance, purpose, page-reference, image-count, and
  visual-safety-evidence checks.
- R37-R38: M1-M4 and M3A preserve no-secret, no-private-data,
  no-private-health-information, no-runtime, no-CMS, no-user-input, and
  no-personalized-coaching boundaries.
- AC1-AC12: M1-M4 plus M3A provide acceptance evidence after plan review,
  test-spec review, implementation, code review, explain-change, and final
  verification.

## Current Handoff Summary

- Current milestone: Lifecycle Closeout
- Current milestone state: branch-ready
- Last reviewed milestone: M3
- Review status: proposal-review R1 approved; spec-review R2 approved after
  SR-EIS-1 resolution; architecture-review R1 approved; plan-review R1
  approved; test-spec-review R2 approved after TSR-EIS-1 resolution;
  code-review M1 R1 requested changes for CR-EIS-M1-1; owner directed broad
  privacy validation to move to verify-before-PR; test-spec-review R3
  requested changes for TSR-EIS-2; test-spec-review R4 approved the
  validation-path amendment; code-review M1 R2 closed M1; M2 implemented
  authoring guidance and review evidence templates; code-review M2 R1 closed
  M2; M3 added the first generated exercise-image batch and review evidence;
  code-review M3 R1 requested changes for CR-EIS-M3-1 and CR-EIS-M3-2;
  review-resolution locally addressed CR-EIS-M3-1 by replacing the wall-slide
  visual and expanding the batch with clearer movement and muscle-attention
  images; CR-EIS-M3-2 is addressed pending re-review after owner
  reader-prompt evidence, replacement images, exact prompt records, and
  post-replacement clarity confirmation; prompt-preservation spec amendment reset
  `specs/exercise-image-standard.md` to draft for exact full prompt-record
  requirements; spec-review R3 requested changes for SR-EIS-2 because the
  provenance-to-prompt-record link field or deterministic mapping is undefined;
  SR-EIS-2 was addressed by defining `prompt_record` as the required provenance
  field for generated raster exercise image prompt-record links; spec-review R4
  approved the prompt-record amendment; architecture amendment and ADR for
  prompt records were approved by architecture-review R2; architecture status
  was normalized to approved; M3A is now planned for prompt-record checker
  support, test coverage, and M3 prompt-record backfill or replacement
  decisions before M3 returns to code-review; plan-review R2 approved the M3A
  amendment; test-spec-review R5 approved the M3A prompt-record proof map;
  M3A implemented prompt-record validation, provenance table support, and an
  explicit compatibility limitation for in-flight M3 images whose exact prompts
  were not recoverable from durable evidence; code-review M3A R1 requested
  changes for CR-EIS-M3A-1 because the compatibility limitation bypass is not
  scoped to the recorded pre-amendment M3 assets; review-resolution addressed
  CR-EIS-M3A-1 by constraining compatibility to the recorded M3 assets and
  adding regression coverage; after CR-EIS-M3-2 replacements, the
  compatibility path now applies only to the five unreplaced assets;
  code-review M3A R2 resolved CR-EIS-M3A-1 but
  requested changes for CR-EIS-M3A-2 because plan milestone states drifted for
  M3 and M3A; review-resolution addressed CR-EIS-M3A-2 by keeping M3 in
  `resolution-needed` while CR-EIS-M3-2 remains open and returning M3A to
  `review-requested` for code-review re-review; owner reader-prompt evidence
  for CR-EIS-M3-2 was recorded after that state cleanup, unclear or
  inconsistent affected images were replaced with prompt-record-backed assets,
  owner post-replacement feedback confirmed that the pictures are now clear,
  and code-review M3A R3 resolved CR-EIS-M3A-2 and closed M3A; code-review M3
  R2 resolved CR-EIS-M3-1 and CR-EIS-M3-2 and closed M3; M4 audited all
  current exercise pages and recorded keep-existing-image routing; code-review
  M4 R1 closed M4; explain-change was refreshed; final local verification
  passed after neutralizing literal scanner-pattern examples in the superseded
  content-schema plan
- Remaining in-scope implementation milestones: PR handoff
- Next stage: pr
- Final closeout readiness: branch-ready
- Reason final closeout is or is not ready: local branch-ready verification
  passed; PR handoff remains open.

## Milestones

### M1. Exercise Image Validation Contract

- Milestone state: closed
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
  exercise-image validation contract; code-review M1 R2 closed the milestone
  after CR-EIS-M1-1 was resolved through the approved validation-path
  amendment.
- Risks: checker overreach could fail legacy-compatible exercise images or
  non-exercise page classes.
- Rollback: revert M1 checker and test changes; leave existing content and
  media untouched.

### M2. Authoring Guidance and Review Evidence Surfaces

- Milestone state: closed
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
- Result: Implemented optional exercise-image authoring guidance in the
  exercise template plus change-local visual-safety and beginner-comprehension
  evidence templates. Code-review M2 R1 closed the milestone with no material
  findings.
- Risks: guidance could accidentally imply images are required or that they
  replace Markdown citations.
- Rollback: remove the template and evidence-surface additions; keep M1
  validation intact.

### M3. First New Exercise Image Batch

- Milestone state: closed
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
- Result: Implemented clearer movement images and one muscle-attention image
  for each target exercise page, exact provenance rows, refreshed visual-safety
  evidence, and focused regression coverage. CR-EIS-M3-1 is addressed locally
  pending re-review. Owner reader-prompt evidence for CR-EIS-M3-2 is recorded;
  the unclear or inconsistent affected images were replaced with
  prompt-record-backed assets, and owner post-replacement feedback confirms the
  pictures are now clear. Code-review M3 R2 resolved CR-EIS-M3-1 and
  CR-EIS-M3-2 and closed M3.
- Risks: generated images may imply unsupported anatomy, correction, treatment,
  brands, or identifiable people.
- Rollback: remove the Markdown image references, remove unused assets, remove
  or revise provenance rows, retain the text-only exercise pages, and rerun M3
  validation.

### M3A. Prompt Record Validation and M3 Backfill

- Milestone state: closed
- Goal: implement the approved prompt-record contract and bring the in-flight
  M3 generated raster exercise images into compliance before M3 returns to
  code-review.
- Requirements: R20-R20H, R28, R35-R38, AC5, AC5A, AC10-AC12.
- Likely files:
  - `tools/checks/check_markdown_first.py`
  - `tests/test_exercise_image_standard.py`
  - `media/PROVENANCE.md`
  - prompt records under `media/prompts/exercises/<exercise-slug>/`
  - M3 target assets under `media/exercises/<exercise-slug>/` only if exact
    prompts cannot be recovered and replacement images are required
  - change-local visual-safety and beginner-comprehension evidence only if
    any replacement image is generated
- Tests:
  - a generated raster exercise image governed by the amendment passes only
    when its provenance row has non-blank `prompt_record`;
  - a `prompt_record` path outside the repository, outside
    `media/prompts/exercises/<exercise-slug>/<asset-stem>.md`, or with a
    non-Markdown extension fails;
  - a missing prompt-record file fails;
  - a prompt record whose internal `asset_path` does not exactly match the
    provenance row's normalized `asset_path` fails;
  - a prompt record that omits exact full prompt text and lacks an explicit
    redaction note fails;
  - prompt records are not treated as reader-facing exercise Markdown and are
    not embedded into exercise pages;
  - legacy-compatible generated raster exercise images that predate the
    prompt-record amendment remain valid when downstream scope explicitly keeps
    them under the pre-amendment compatibility path.
- Steps:
  - Add focused failing tests for missing `prompt_record`, invalid
    prompt-record path shape, missing prompt record, reverse `asset_path`
    mismatch, missing exact prompt text, and legacy compatibility.
  - Extend provenance parsing and validation to accept the new
    `prompt_record` column while preserving existing required-field behavior.
  - Add repository-local prompt-record resolution and validation helpers.
  - Add exact prompt records for the current M3 generated raster exercise
    images when exact prompts are recoverable.
  - If exact prompts are unavailable for any current M3 image, either record
    the limitation and leave that asset under an explicitly allowed
    pre-amendment compatibility path or replace the image with a newly
    generated asset that has a full prompt record and fresh review evidence.
  - Update `media/PROVENANCE.md` rows for governed M3 images with
    `prompt_record` values.
  - Rerun M3 and prompt-record validation before returning M3 to code-review.
- Validation:
  - `python3 -m unittest tests.test_exercise_image_standard`
  - `python3 -m unittest discover tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  - scoped current-change privacy scan over prompt records and M3 evidence;
    broad EIS-CMD4 privacy validation remains lifecycle closeout / verify
- Result: Implemented prompt-record validation for governed generated raster
  exercise images, including missing/invalid `prompt_record` paths, missing
  prompt-record files, reverse `asset_path` mismatch, missing exact prompt or
  redaction evidence, and reader-facing prompt-record embedding checks.
  `media/PROVENANCE.md` now has a `prompt_record` column. Exact prompts for
  the in-flight M3 images were not recoverable from repository-local evidence,
  so M3A records an explicit compatibility limitation in
  `docs/changes/exercise-image-standard-and-optimization/evidence/m3a-prompt-record-backfill.md`
  and the affected provenance rows instead of inventing prompt text.
  Code-review M3A R1 requested changes because the checker accepts the
  compatibility limitation note for any generated raster exercise image instead
  of only the recorded pre-amendment M3 assets. Review-resolution addressed the
  finding by adding a deterministic compatibility asset allowlist and regression
  coverage for non-M3 images that copy the compatibility note. Code-review M3A
  R2 resolved CR-EIS-M3A-1 but requested changes for CR-EIS-M3A-2 because M3
  and M3A milestone states drifted in the plan. Review-resolution addressed the
  lifecycle-state drift by keeping M3 in `resolution-needed` while CR-EIS-M3-2
  remains open and returning M3A to `review-requested` for code-review
  re-review. CR-EIS-M3-2 replacement work later moved five M3 assets off the
  compatibility path by replacing them with exact prompt-record-backed assets;
  the deterministic compatibility allowlist now applies only to the five
  unreplaced M3 compatibility assets. Code-review M3A R3 resolved
  CR-EIS-M3A-2 and closed M3A.
- Risks: exact prompts for already-generated M3 images may be unavailable;
  replacement images could reopen visual clarity, provenance, visual-safety,
  and beginner-comprehension review work.
- Rollback: remove M3A checker changes, tests, prompt-record files, and
  `prompt_record` provenance fields; keep the approved spec and architecture
  amendments as unimplemented until a new plan slice is approved.

### M4. Remaining Exercise Audit and Follow-up Routing

- Milestone state: closed
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
- Result: Implemented M4 audit evidence in
  `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md`.
  The audit covers all current `exercises/*.md` pages, records
  `keep existing image` for each page, preserves legacy-compatible image
  purposes without migration-only edits, and routes future image work to small
  reviewed follow-up loops only when a concrete comprehension gap is named.
  `tests/test_exercise_image_standard.py` now checks that every current
  exercise page appears in the audit.
  Code-review M4 R1 closed the milestone with no material findings.
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

- `python3 -m unittest tests.test_exercise_image_standard`
- `python3 -m unittest tests.test_markdown_first_guardrails tests.test_responsible_breadth_m1`
- `python3 -m unittest discover tests`
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`

Prompt-record validation must be added to the test spec before M3A
implementation. M3A validation should include missing `prompt_record`, invalid
path shape, missing prompt-record file, reverse `asset_path` mismatch, missing
exact prompt text or redaction note, and legacy compatibility fixtures.

Milestone-level privacy validation may use scoped current-change scans when
review hygiene needs it. The broad EIS-CMD4 privacy sweep is owned by lifecycle
closeout / verify and must pass before PR handoff, not during M1-M4
or M3A implementation closeout.

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
- Prompt-record drift: validate `prompt_record` path shape, file existence,
  reverse `asset_path` matching, and exact prompt text or explicit redaction
  notes.
- Missing exact prompts: replace affected generated raster images or record an
  explicit compatibility limitation before promotion; do not invent prompts.
- Large content PR risk: keep generated image batches small and reviewable.
- Source-support drift near images: keep claims in Markdown and use page-local
  sources; images cannot introduce new claims.

## Dependencies

- Plan-review must approve this plan before test-spec authoring.
- Test-spec and test-spec-review must complete before implementation.
- M3 depends on M1 and M2 closure.
- M3A depends on prompt-record architecture-review R2 approval, this plan
  amendment, plan-review, and a prompt-record test-spec amendment with
  test-spec-review approval.
- M3 cannot return to code-review until M3A is implemented and reviewed, or
  plan-review/test-spec-review explicitly choose a different safe sequencing
  path.
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
- 2026-07-03: Test-spec revision aligned the plan's general validation section
  with the amended EIS-CMD4 lifecycle closeout / verify ownership.
- 2026-07-03: Test-spec-review R4 approved the TSR-EIS-2 revision; M1
  code-review re-review is next.
- 2026-07-03: Code-review M1 R2 resolved CR-EIS-M1-1 and closed M1; M2
  implementation is next.
- 2026-07-03: M2 implemented optional exercise-image authoring guidance,
  visual-safety review evidence, and beginner-comprehension evidence; code-review
  M2 is next.
- 2026-07-03: Code-review M2 R1 closed M2 with no material findings; M3
  implementation is next.
- 2026-07-03: M3 implemented one movement image each for `chin-nod`,
  `thoracic-extension`, `wall-slide`, `prone-y-t`, and `band-pull-apart`,
  with provenance rows and review evidence; code-review M3 is next.
- 2026-07-03: Code-review M3 R1 requested changes because the wall-slide image
  does not match the forearms-on-wall variation and the beginner-comprehension
  evidence is a maintainer checklist rather than reader-prompt evidence.
- 2026-07-03: Owner feedback said the first M3 images were not clear enough to
  show movement or muscle use. Review-resolution replaced the movement assets,
  added one muscle-attention asset per target page, updated provenance and
  visual-safety evidence, and left reader-prompt beginner-comprehension evidence
  as the remaining blocker.
- 2026-07-03: Exact full prompt preservation was requested as a repository best
  practice. The exercise-image spec was amended back to draft with prompt-record
  requirements; spec-review is next before architecture, test-spec, plan, or
  implementation updates.
- 2026-07-03: Spec-review R3 requested changes for SR-EIS-2 because the
  prompt-record amendment requires a link from provenance rows to prompt records
  but leaves the exact link field or deterministic mapping to downstream
  artifacts.
- 2026-07-03: SR-EIS-2 was addressed by defining `prompt_record` as the required
  generated raster exercise image provenance field for prompt-record links,
  with repository-local path semantics and reverse `asset_path` matching.
- 2026-07-03: Spec-review R4 approved the prompt-record amendment after
  SR-EIS-2 resolution; architecture or ADR assessment is next.
- 2026-07-03: Architecture amendment added prompt-record validation flow,
  `prompt_record` provenance linking, prompt-record packaging, and ADR
  2026-07-03 generated raster prompt records; architecture-review R2 followed.
- 2026-07-03: Architecture-review R2 approved the prompt-record canonical
  architecture amendment and ADR with no material findings.
- 2026-07-03: Architecture status was normalized to approved after
  architecture-review R2. The plan was revised to add M3A for prompt-record
  checker support, tests, and M3 image prompt-record backfill or replacement
  decisions; plan-review is next.
- 2026-07-03: Plan-review R2 approved the M3A prompt-record validation and M3
  backfill plan amendment; test-spec amendment is next.
- 2026-07-03: Test spec was amended with M3A prompt-record requirements,
  examples, edge cases, commands, fixtures, observability, migration, and
  readiness; test-spec-review R5 followed.
- 2026-07-03: Test-spec-review R5 approved the M3A prompt-record proof map;
  M3A implementation is next.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-03 | Put validation before generated image batches. | The spec changes media-purpose and provenance behavior, so fixtures should prove the contract before content changes. | Generate images first; mix checker changes and image batch in one PR. |
| 2026-07-03 | Preserve existing exercise images without migration. | The approved spec says existing `equipment_identification` and `key_movement_illustration` exercise images remain valid. | Rename old purposes opportunistically; require migration when pages are touched. |
| 2026-07-03 | Use one plan with small implementation milestones. | The accepted proposal keeps one coherent product decision while avoiding broad implementation PRs. | One large all-exercise optimization PR; separate proposals for small batches. |
| 2026-07-03 | Add M3A for prompt-record validation and M3 backfill before M3 re-review. | The prompt-record amendment changes generated-raster provenance validation after M3 was already in review-resolution, so the new contract needs its own testable slice before the image batch can be accepted. | Hide prompt-record work inside M3 re-review; postpone prompt records to M4; treat chat or tool history as durable prompt evidence. |

## Surprises and discoveries

- The existing checker already centralizes raster provenance and
  context-sensitive media-purpose validation, so M1 can extend current
  behavior rather than adding a new validator.
- `docs/templates/exercise-card.md` exists and is the likely authoring surface
  for optional image guidance.
- Template validation needed a path-context boundary: template files should not
  be treated as promoted product pages, but their image references still need
  normal media-contract validation.
- M2 can use an inline path placeholder in the exercise template instead of a
  Markdown image reference, so the template remains concrete without implying a
  real asset that needs provenance.
- M3 initially selected one `exercise_movement_illustration` per target page,
  but owner feedback showed the batch did not make movement or muscle use clear
  enough. Review-resolution revised M3 to use one movement image and one
  `exercise_muscle_attention_illustration` per target page.
- The M3 wall-slide and band pull-apart images remain simplified support
  illustrations; nearby Markdown remains authoritative for forearm contact,
  band choice, muscle wording, and range.
- The prompt-record amendment happened after M3 image generation began, and
  current `media/PROVENANCE.md` rows do not have a `prompt_record` column.
  M3A must backfill exact prompts only when they are recoverable; otherwise it
  must replace affected images or record an explicit compatibility limitation.
- M3A searched repository-local evidence for exact full M3 prompts and found
  only concise prompt summaries and review notes. The implementation therefore
  used the approved explicit compatibility-limitation path for the in-flight M3
  assets and did not generate replacement images.

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
- Before M2 documentation changes, `python3 -m unittest tests.test_markdown_first_templates`
  failed with the expected missing optional exercise-image guidance and evidence
  templates.
- After M2 implementation, `python3 -m unittest tests.test_markdown_first_templates`
  passed with 4 tests.
- After M2 implementation,
  `python3 -m unittest tests.test_markdown_first_templates tests.test_exercise_image_standard`
  passed with 11 tests.
- After M2 implementation,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates media/PROVENANCE.md`
  passed, checking 10 Markdown files.
- After M2 implementation,
  `python3 tools/checks/check_privacy.py -- docs/templates docs/changes/exercise-image-standard-and-optimization`
  passed, checking 23 files.
- After M2 implementation, `git diff --check` passed.
- Before M3A implementation, `python3 -m unittest tests.test_exercise_image_standard`
  failed with expected missing `prompt_record` validation behavior and missing
  M3A prompt-record/backfill evidence.
- After M3A implementation, `python3 -m unittest tests.test_exercise_image_standard`
  passed with 11 focused exercise-image tests.
- After M3A implementation, `python3 -m unittest discover tests` passed with
  100 tests.
- After M3A implementation,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed, checking 25 Markdown files.
- After M3A implementation,
  `python3 tools/checks/check_privacy.py -- docs/plan.md docs/plans/2026-07-03-exercise-image-standard.md docs/changes/exercise-image-standard-and-optimization/change.yaml docs/changes/exercise-image-standard-and-optimization/evidence/m3a-prompt-record-backfill.md media/PROVENANCE.md tests/test_exercise_image_standard.py tools/checks/check_markdown_first.py`
  passed, checking 7 files.
- After M3A implementation, `git diff --check` passed.
- During M2 code-review,
  `python3 -m unittest tests.test_markdown_first_templates tests.test_exercise_image_standard`
  passed with 11 tests.
- During M2 code-review,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates media/PROVENANCE.md`
  passed, checking 10 Markdown files.
- During M2 code-review,
  `python3 tools/checks/check_privacy.py -- docs/templates docs/changes/exercise-image-standard-and-optimization`
  passed, checking 23 files.
- During M2 code-review, `git diff --check` passed.
- Before M3 content changes, `python3 -m unittest tests.test_exercise_image_standard`
  failed with the expected missing target page image references, asset files,
  provenance rows, and evidence files.
- After M3 implementation, `python3 -m unittest tests.test_exercise_image_standard`
  passed with 8 tests.
- After M3 implementation, `python3 -m unittest discover tests` passed with 97
  tests.
- After M3 implementation,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed, checking 25 Markdown files.
- After M3 implementation,
  `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md docs/changes/exercise-image-standard-and-optimization exercises media/PROVENANCE.md`
  passed, checking 39 files.
- After M3 implementation, `git diff --check` passed.
- During M3 code-review, `python3 -m unittest tests.test_exercise_image_standard`
  passed with 8 tests.
- During M3 code-review, `python3 -m unittest discover tests` passed with 97
  tests.
- During M3 code-review,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed, checking 25 Markdown files.
- During M3 code-review,
  `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md docs/changes/exercise-image-standard-and-optimization exercises media/PROVENANCE.md`
  passed, checking 39 files.
- During M3 code-review, `git diff --check` passed.
- After M3 review-resolution asset, page, provenance, and evidence updates,
  `python3 -m unittest tests.test_exercise_image_standard` passed with 8 tests.
- After M3 review-resolution updates, `python3 -m unittest discover tests`
  passed with 97 tests.
- After M3 review-resolution updates,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed, checking 25 Markdown files.
- After M3 review-resolution updates,
  `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md docs/changes/exercise-image-standard-and-optimization exercises media/PROVENANCE.md`
  passed, checking 40 files.
- After M3 review-resolution updates, `git diff --check` passed.
- During prompt-record architecture review,
  `python3 tools/checks/check_privacy.py -- docs/changes/exercise-image-standard-and-optimization/reviews/architecture-review-r2.md docs/changes/exercise-image-standard-and-optimization/review-log.md docs/changes/exercise-image-standard-and-optimization/change.yaml`
  passed, checking 3 files.
- During prompt-record plan amendment,
  `python3 tools/checks/check_privacy.py -- docs/architecture/system/architecture.md docs/plan.md docs/plans/2026-07-03-exercise-image-standard.md docs/changes/exercise-image-standard-and-optimization/change.yaml`
  passed, checking 4 files.
- During prompt-record plan amendment, `git diff --check` passed.
- After CR-EIS-M3-2 reader-prompt evidence, replacement assets, prompt
  records, provenance rows, and compatibility-scope updates,
  `python3 -m unittest tests.test_exercise_image_standard` passed with 12
  focused exercise-image tests.
- After CR-EIS-M3-2 replacement updates, `python3 -m unittest discover tests`
  passed with 101 tests.
- After CR-EIS-M3-2 replacement updates,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed, checking 25 Markdown files.
- After CR-EIS-M3-2 replacement updates,
  `python3 tools/checks/check_privacy.py -- docs/plan.md docs/plans/2026-07-03-exercise-image-standard.md docs/changes/exercise-image-standard-and-optimization media/PROVENANCE.md media/prompts tools/checks/check_markdown_first.py tests/test_exercise_image_standard.py exercises`
  passed, checking 54 files.
- After CR-EIS-M3-2 replacement updates, `git diff --check` passed.
- After CR-EIS-M3-2 post-replacement owner clarity confirmation,
  `python3 -m unittest tests.test_exercise_image_standard` passed with 12
  focused exercise-image tests.
- After CR-EIS-M3-2 post-replacement owner clarity confirmation,
  `python3 -m unittest discover tests` passed with 101 tests.
- After CR-EIS-M3-2 post-replacement owner clarity confirmation,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed, checking 25 Markdown files.
- After CR-EIS-M3-2 post-replacement owner clarity confirmation,
  `python3 tools/checks/check_privacy.py -- docs/plan.md docs/plans/2026-07-03-exercise-image-standard.md docs/changes/exercise-image-standard-and-optimization`
  passed, checking 31 files.
- After CR-EIS-M3-2 post-replacement owner clarity confirmation,
  `git diff --check` passed.
- During M3A R3 code-review, `python3 -m unittest tests.test_exercise_image_standard`
  passed with 12 tests.
- During M3A R3 code-review,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed, checking 25 Markdown files.
- During M3A R3 code-review,
  `python3 tools/checks/check_privacy.py -- docs/plan.md docs/plans/2026-07-03-exercise-image-standard.md docs/changes/exercise-image-standard-and-optimization media/PROVENANCE.md media/prompts tools/checks/check_markdown_first.py tests/test_exercise_image_standard.py exercises`
  passed, checking 54 files.
- During M3A R3 code-review, `git diff --check HEAD` passed.
- During M3 R2 code-review, `python3 -m unittest tests.test_exercise_image_standard`
  passed with 12 tests.
- During M3 R2 code-review, `python3 -m unittest discover tests` passed with
  101 tests.
- During M3 R2 code-review,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed, checking 25 Markdown files.
- During M3 R2 code-review,
  `python3 tools/checks/check_privacy.py -- docs/changes/exercise-image-standard-and-optimization/evidence exercises media/PROVENANCE.md media/prompts`
  passed, checking 26 files.
- During M3 R2 code-review, `git diff --check HEAD` passed.
- After M4 audit implementation, `python3 -m unittest tests.test_exercise_image_standard`
  passed with 13 tests.
- After M4 audit implementation, `python3 -m unittest discover tests` passed
  with 102 tests.
- After M4 audit implementation,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`
  passed, checking 19 Markdown files.
- After M4 audit implementation,
  `python3 tools/checks/check_privacy.py -- docs/changes/exercise-image-standard-and-optimization exercises media/PROVENANCE.md`
  passed, checking 48 files.
- After M4 audit implementation, `git diff --check` passed.
- During M4 code-review, `python3 -m unittest tests.test_exercise_image_standard`
  passed with 13 tests.
- During M4 code-review,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`
  passed, checking 19 Markdown files.
- During M4 code-review,
  `python3 tools/checks/check_privacy.py -- docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md tests/test_exercise_image_standard.py docs/changes/exercise-image-standard-and-optimization/change.yaml docs/plans/2026-07-03-exercise-image-standard.md docs/plan.md`
  passed, checking 5 files.
- During M4 code-review, `git diff --check HEAD` passed.
- After explain-change refresh,
  `python3 tools/checks/check_privacy.py -- docs/changes/exercise-image-standard-and-optimization/explain-change.md docs/changes/exercise-image-standard-and-optimization/change.yaml docs/plans/2026-07-03-exercise-image-standard.md docs/plan.md`
  passed, checking 4 files.
- After explain-change refresh, `git diff --check` passed.
- During final verification, `python3 -m unittest tests.test_exercise_image_standard`
  passed with 13 tests.
- During final verification, `python3 -m unittest discover tests` passed with
  102 tests.
- During final verification,
  `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md`
  passed, checking 25 Markdown files.
- During final verification, the broad privacy command first failed on literal
  scanner-pattern examples in the superseded content-schema plan. After those
  examples were replaced with `<forbidden-pattern-regex>`,
  `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/exercise-image-standard-and-optimization docs/plans media exercises tools tests`
  passed, checking 157 files.
- During final verification, `git diff --check` passed.

## Outcome and retrospective

Pending. This plan is not complete until all in-scope milestones, reviews,
explain-change, verification, and PR handoff are complete.

## Readiness

See Current Handoff Summary for the live next stage. Local branch-ready
verification passed; this plan is awaiting PR handoff and is not final closeout.
