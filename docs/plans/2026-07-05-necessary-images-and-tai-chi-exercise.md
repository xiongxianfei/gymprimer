# Plan: Necessary Images and Tai Chi Exercise

## Status

- Status: reviewed
- Plan lifecycle state: active
- Terminal disposition: none

## Purpose / big picture

This plan sequences the approved Tai Chi Basics direction into reviewable implementation milestones.
The change adds one beginner exercise page, records a ten-candidate image pool for that page, generates exactly three first-batch support images, and proves the media remains subordinate to Markdown.

## Source artifacts

- Proposal: `docs/proposals/2026-07-05-necessary-images-and-tai-chi-exercise.md`
- Spec: `specs/necessary-images-and-tai-chi-exercise.md`
- Architecture: `docs/architecture/system/architecture.md`
- Test spec: `specs/necessary-images-and-tai-chi-exercise.test.md`
- Proposal review: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/proposal-review-r2.md`
- Spec review: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/spec-review-r1.md`
- Architecture review: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/architecture-review-r1.md`

## Context and orientation

The product surface is Markdown-first.
The future implementation must add `exercises/tai-chi-basics.md` without turning Tai Chi into a martial curriculum, clinical program, fall-prevention protocol, adaptive coaching flow, or video-first feature.

The first image batch is capped at exactly three generated raster images:

- `media/exercises/tai-chi-basics/setup.png`
- `media/exercises/tai-chi-basics/weight-shift.png`
- `media/exercises/tai-chi-basics/muscle-attention.png`

Each generated raster image needs a matching prompt record under `media/prompts/exercises/tai-chi-basics/`, an approved `media/PROVENANCE.md` row, meaningful alt text, visual-safety review evidence, and beginner-comprehension proof.
Candidates 4-10 are deferred alternatives or future replacements, not permission to publish a fourth image without downstream approved exception justification.

## Non-goals

- No implementation before plan-review and test-spec-review.
- No full Tai Chi form, martial application, lineage debate, clinical protocol, fall-prevention program, or adaptive balance coaching.
- No borrowed web images, stock photos, screenshots, branded media, identifiable people, remote image references, video, animation, app, database, user account, or generated public JSON.
- No generated image as source-of-truth instruction, safety evidence, anatomy evidence, or programming guidance.

## Requirements covered

| Requirement range | Milestone or evidence surface |
|---|---|
| R1-R8 | M2 page path, title, sections, beginner scope, and non-clinical framing |
| R9-R19 | M2 setup, safety, source support, method guidance, and muscle guidance |
| R20-R29 | M1 proof map and M3 image-count / candidate-pool implementation |
| R30-R35 | M3 provenance and prompt records |
| R36-R40 | M1 validation expectations and M4 visual-safety evidence |
| R41-R42 | M4 beginner comprehension proof and rollback check |
| R43 | M1-M4 scope checks and validation |

## Current Handoff Summary

- Current milestone: M2
- Current milestone state: review-requested
- Last reviewed milestone: M1
- Review status: M1 code-review clean; M2 implemented and awaiting code-review
- Remaining in-scope implementation milestones: M2 review, M3, M4
- Next stage: code-review M2
- Final closeout readiness: not-ready
- Reason final closeout is or is not ready: M2 has not passed code-review, M3-M4 are not implemented, and final verification and PR handoff have not happened.

## Milestones

### M1. Validation and Proof Map

- Milestone state: closed
- Goal: Add or update deterministic tests and proof obligations before content and media are introduced.
- Requirements: R20-R29, R36-R43
- Files/components likely touched:
  - `specs/necessary-images-and-tai-chi-exercise.test.md`
  - `tools/checks/check_markdown_first.py`
  - `tests/` or existing checker fixtures
  - `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/`
- Dependencies:
  - Approved plan-review and test-spec-review.
- Tests to add/update:
  - Page section and title checks for `exercises/tai-chi-basics.md`.
  - Method label checks for `Method type: low_load_control_drill` and required visible labels.
  - Image-count checks for exactly three first-batch images and no second muscle-attention image.
  - Prompt-record and provenance checks for generated raster Tai Chi assets.
  - Privacy and forbidden-scope checks.
- Implementation steps:
  - Add the test spec before production changes.
  - Extend or identify checker coverage for the Tai Chi-specific requirements.
  - Add fixtures for missing prompt record, fourth image, generic alt text, and invalid media purpose when automation is practical.
  - Define manual evidence templates or criteria for visual-safety review and beginner comprehension proof.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md`
  - `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/`
  - `python3 -m pytest`
- Expected observable result: tests or proof obligations fail before the page, media, prompt records, provenance, and review evidence exist, then pass after later milestones.
- Commit message: `M1: add Tai Chi validation proof map`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Overfitting checks to one page could hide broader media regressions.
- Rollback/recovery:
  - Keep Tai Chi-specific checks gated to the approved page path and remove fixtures if the page scope changes upstream.

### M2. Tai Chi Markdown Page

- Milestone state: review-requested
- Goal: Draft the static beginner-facing Tai Chi Basics page without generated images.
- Requirements: R1-R19, R42-R43
- Files/components likely touched:
  - `exercises/tai-chi-basics.md`
  - `SOURCES.md`
  - `RED-FLAGS.md` only if existing routing is insufficient
- Dependencies:
  - M1 proof map exists.
- Tests to add/update:
  - Page structure, source support, source-index, method guidance, forbidden wording, and privacy checks.
- Implementation steps:
  - Create `exercises/tai-chi-basics.md` with the approved sections.
  - Use `# Tai Chi Basics` and page-local sources.
  - Add `## How much to do` with `Method type: low_load_control_drill`, beginner starting point, effort, rest, progression, and stop guidance.
  - Keep movement limited to ready stance, weight shift, simple opening movement, and return to quiet standing.
  - Add or update shared source IDs in `SOURCES.md` when required.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md`
  - `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md SOURCES.md`
  - `python3 -m pytest`
- Expected observable result: the page passes text-only checks and remains valid without image references.
- Implemented result: `exercises/tai-chi-basics.md` exists as a text-only Markdown page with page-local sources, shared source-index entries, low-load control method labels, broad role-based muscle guidance, and MP1 source-audit evidence.
- Commit message: `M2: add Tai Chi Basics markdown page`
- Milestone closeout:
  - validation passed locally with the recorded unittest, Markdown, privacy, and diff checks
  - progress updated
  - decision log updated
  - validation notes updated
  - milestone committed
- Risks:
  - Content could drift into clinical or martial instruction.
- Rollback/recovery:
  - Remove or narrow the page back to ready stance and weight shift while preserving tests for forbidden scope.

### M3. Governed First Image Batch

- Milestone state: planned
- Goal: Generate and promote exactly three Tai Chi support images through the governed media workflow.
- Requirements: R20-R40, R43
- Files/components likely touched:
  - `media/exercises/tai-chi-basics/setup.png`
  - `media/exercises/tai-chi-basics/weight-shift.png`
  - `media/exercises/tai-chi-basics/muscle-attention.png`
  - `media/prompts/exercises/tai-chi-basics/setup.md`
  - `media/prompts/exercises/tai-chi-basics/weight-shift.md`
  - `media/prompts/exercises/tai-chi-basics/muscle-attention.md`
  - `media/PROVENANCE.md`
  - `exercises/tai-chi-basics.md`
- Dependencies:
  - M2 text page exists and passes checks.
  - Exact prompts are ready for review before generation.
- Tests to add/update:
  - Media path, image-count, purpose, prompt-record, provenance, page-reference, review-status, and alt-text checks.
- Implementation steps:
  - Prepare exact prompts for setup, weight shift, and broad muscle attention.
  - Generate images through the approved Codex/imagegen implementation path.
  - Add assets under `media/exercises/tai-chi-basics/`.
  - Add prompt records preserving exact prompt text.
  - Add approved provenance rows with valid purpose values and `page_refs`.
  - Reference the three images near the Markdown sections they support with meaningful alt text.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md media/PROVENANCE.md`
  - `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md media/PROVENANCE.md media/prompts/exercises/tai-chi-basics/`
  - `python3 -m pytest`
- Expected observable result: the page references exactly three generated raster images with matching prompt records, approved provenance, valid purposes, and meaningful alt text.
- Commit message: `M3: add governed Tai Chi support images`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - A generated image may imply therapy, combat, exact correctness, overprecise anatomy, or identifying-person content.
- Rollback/recovery:
  - Remove the failed Markdown reference, unused asset, prompt record, and provenance row; keep the text-only page.

### M4. Review Evidence and Final Local Readiness

- Milestone state: planned
- Goal: Record manual visual-safety review, beginner comprehension proof, rollback proof, and final local validation evidence.
- Requirements: R40-R43
- Files/components likely touched:
  - `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/visual-safety-review.md`
  - `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/beginner-comprehension-proof.md`
  - `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/validation-notes.md`
- Dependencies:
  - M3 image batch exists.
- Tests to add/update:
  - Review-evidence presence checks if existing validation supports them.
  - Manual proof records when semantic criteria cannot be automated.
- Implementation steps:
  - Record visual-safety review for each selected image.
  - Record beginner comprehension proof without private health information.
  - Record text-only rollback proof.
  - Run final local validation and update plan progress.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md`
  - `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md media/PROVENANCE.md media/prompts/exercises/tai-chi-basics/ docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/`
  - `python3 -m pytest`
- Expected observable result: manual evidence and automated checks support promotion of the Tai Chi page and first image batch.
- Commit message: `M4: record Tai Chi image review evidence`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Beginner proof may show residual confusion about weight shift or stop conditions.
- Rollback/recovery:
  - Revise Markdown or replace/remove images, then rerun visual review and beginner proof before closeout.

## Validation plan

- `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md`: page contract, source, method, and media checks.
- `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md media/PROVENANCE.md media/prompts/exercises/tai-chi-basics/ docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/`: privacy and private-health-information check.
- `python3 -m pytest`: regression and checker fixture coverage.
- Manual visual-safety review: generated-image semantic safety and purpose fit.
- Manual beginner comprehension proof: reader can explain Tai Chi purpose, stance, weight shift, body feel, stop conditions, and whether images helped.

## Risks and recovery

- Risk: Images imply therapy, fall-prevention treatment, combat, or exact form correctness.
  - Recovery: reject or replace the image; remove associated Markdown reference, prompt record, and provenance row until review passes.
- Risk: The ten-candidate pool is mistaken for permission to publish more than three images.
  - Recovery: keep checks and review evidence tied to exactly three first-batch assets; require downstream approved exception for a fourth image.
- Risk: Method guidance becomes a personalized practice plan.
  - Recovery: revert to static `low_load_control_drill` wording and rerun forbidden-scope checks.
- Risk: Prompt records or provenance rows drift from asset paths.
  - Recovery: fix the prompt-record reverse link and provenance `asset_path` / `page_refs` together before promotion.

## Dependencies

- Approved plan-review.
- Approved test-spec-review.
- Existing exercise-image standard, prompt-record architecture, exercise-method guidance, and exercise-muscle guidance.
- Generated images must come through the governed Codex/imagegen implementation path.
- Human visual-safety reviewer and non-identifying beginner comprehension proof before promotion.

## Progress

- 2026-07-06: Drafted plan after accepted proposal, approved spec-review, and approved architecture-review.
- 2026-07-06: Plan-review R1 approved the plan with no material findings.
- 2026-07-06: Test-spec-review R1 approved the active test spec with no material findings; workflow auto-run stopped before implementation.
- 2026-07-06: Implemented M1 by adding Tai Chi-specific method and exercise-image validation tests; existing checker behavior already covered the required failures, so no checker code change was needed.
- 2026-07-06: Code-review M1 R1 was clean with no material findings; M1 closed and routed to implementation M2.
- 2026-07-06: Implemented M2 by adding the text-only `exercises/tai-chi-basics.md` page, Tai Chi source IDs in `SOURCES.md`, MP1 source-audit evidence, real-page tests, and the aligned text-only row in the existing exercise-image audit.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-06 | Sequence text page before image generation. | A passing text-only page preserves rollback and keeps Markdown source of truth. | Generate images before page text. |
| 2026-07-06 | Use four implementation milestones. | Validation, content, media, and review evidence have different failure modes and review surfaces. | One large implementation milestone. |
| 2026-07-06 | Leave checker code unchanged for M1. | New Tai Chi-specific fixtures passed against existing method, media-purpose, prompt-record, image-count, alt-text, and visual-safety validation. | Add page-specific checker branches before a failing test demonstrates a gap. |
| 2026-07-06 | Keep M2 text-only and defer all Tai Chi images to M3. | M2 must prove the Markdown page and rollback path before generated assets become page references. | Add placeholder image references or generate images during M2. |
| 2026-07-06 | Update the existing exercise-image audit with a Tai Chi text-only row. | Broad unittest discovery treats that audit as an inventory of current exercise pages. | Leave the audit stale until image generation. |

## Surprises and discoveries

- The approved plan still mentioned `python3 -m pytest`, but the active test spec owns the reviewed command ledger and uses unittest commands. `python3 -m pytest` is unavailable in this environment.
- Broad unittest discovery failed until `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` was updated to include the new text-only Tai Chi page.

## Validation notes

- `python3 tools/checks/check_privacy.py docs/architecture/system/architecture.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/change.yaml specs/necessary-images-and-tai-chi-exercise.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/spec-review-r1.md` passed during architecture authoring.
- `git diff --check -- docs/architecture/system/architecture.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/change.yaml specs/necessary-images-and-tai-chi-exercise.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/spec-review-r1.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-log.md` passed during architecture authoring.
- `python3 -m unittest tests.test_exercise_image_standard tests.test_exercise_method_guidance` initially failed because a candidate-pool contract test asserted exact wording instead of the approved semantic contract; the test was corrected before handoff.
- `python3 -m unittest tests.test_exercise_image_standard tests.test_exercise_method_guidance` passed: 36 tests.
- `python3 -m unittest tests.test_exercise_method_guidance` passed: 17 tests.
- `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed: 41 tests.
- `python3 -m unittest discover -s tests` passed: 158 tests.
- `git diff --check` passed.
- `python3 tools/checks/check_privacy.py tests/test_exercise_image_standard.py tests/test_exercise_method_guidance.py specs/necessary-images-and-tai-chi-exercise.test.md docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/` passed.
- `python3 -m pytest` could not run because `pytest` is not installed: `/usr/bin/python3: No module named pytest`.
- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_page_exists_and_has_required_text_only_shape tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_setup_safety_sources_and_source_index tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_m2_source_audit_records_required_claim_samples` failed before implementation because `exercises/tai-chi-basics.md` and `source-audit.md` did not exist.
- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_page_exists_and_has_required_text_only_shape tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_beginner_scope_and_forbidden_product_language tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_setup_safety_sources_and_source_index tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_low_load_method_guidance tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_broad_muscle_and_feel_guidance tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_m2_source_audit_records_required_claim_samples` passed: 6 tests.
- `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md` passed.
- `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md media/PROVENANCE.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/ SOURCES.md` passed.
- `python3 -m unittest tests.test_exercise_method_guidance` passed: 17 tests.
- `python3 -m unittest discover -s tests` initially failed because the existing exercise-image audit did not list `exercises/tai-chi-basics.md`; after adding the text-only audit row it passed: 164 tests.
- `git diff --check` passed.

## Outcome and retrospective

- M2 implementation is complete and pending code-review.

## Readiness

- See `Current Handoff Summary`.
- M2 is ready for code-review.
