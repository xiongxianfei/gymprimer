# Advanced Rowing Machine Tutorial Plan

## Status

- Status: reviewed
- Plan lifecycle state: active
- Terminal disposition: not-terminal

## Purpose / big picture

This plan sequences the approved advanced rowing-machine tutorial into reviewable implementation milestones.
The implementation adds a static advanced companion page, a scoped image-rich media batch, image-instruction packets, provenance, validation, and manual proof without turning GymPrimer into coaching software or a workout planner.

## Source artifacts

- Proposal: `../proposals/2026-07-07-advanced-rowing-machine-tutorial.md`
- Spec: `../../specs/advanced-rowing-machine-tutorial.md`
- Spec review: `../changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/spec-review-r1.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review: `../changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/architecture-review-r1.md`
- Test spec: `../../specs/advanced-rowing-machine-tutorial.test.md`

## Context and orientation

The beginner rowing page remains `exercises/rowing-machine.md`.
The advanced companion page will be `exercises/rowing-machine-advanced.md`.
Generated rowing media, if accepted during implementation, lives under `media/exercises/rowing-machine-advanced/`.
Prompt records function as image-instruction packets under `media/prompts/exercises/rowing-machine-advanced/`.
Generated raster assets need approved rows in `media/PROVENANCE.md`.

Markdown remains the source of truth.
Images, force-intensity overlays, technical diagrams, prompt records, provenance, and review evidence support the Markdown but do not replace page-local citations or safety boundaries.

## Non-goals

- No personalized rowing plan, adaptive programming, race strategy, or performance guarantee.
- No clinical care, injury-specific return-to-rowing protocol, treatment plan, or medical judgment.
- No hosted app, PM5 data-analysis app, tracker, calculator, wearable integration, video product, runtime API, generated public JSON, or coaching engine.
- No borrowed PM5 screenshots, copied UI, third-party photos, brand marks, or identifiable people.
- No global increase to the normal exercise-image limit for unrelated exercise pages.
- No new method type named `advanced_basic_cardio_equipment`.

## Requirements covered

| Requirement group | Milestone or evidence surface |
| --- | --- |
| R1-R9, R47-R48 | M2 page content and scope wording |
| R10-R21 | M2 source-backed advanced rowing Markdown and `SOURCES.md` updates when required |
| R22-R32, R39-R46 | M1 validator/test support and M3 media packet/provenance implementation |
| R33-R38, R42-R44 | M3 force-intensity packet, Markdown legend, alt text, and grayscale review |
| R49 | M4 advanced-reader comprehension proof |
| R50 | M1-M4 validation notes and final verification evidence |
| AC1-AC10 | Plan-review, test-spec, implementation, code-review, explain-change, verify, and PR handoff gates |

## Current Handoff Summary

- Current milestone: M4. Manual Proof, Review Evidence, and Closeout Preparation
- Current milestone state: closed
- Last reviewed milestone: M3. Governed Media, Prompt Packets, and Provenance
- Review status: code-review R5 clean-with-notes; M4 closed
- Remaining in-scope open milestones: none
- Next stage: pr
- Final closeout readiness: ready for PR handoff
- Reason final closeout is or is not ready: PR #18 is open; hosted CI was pending at handoff, and review/merge/closeout remain.

## Milestones

### M1. Validation and Test Scaffolding

- Milestone state: closed
- Goal: Add focused validation and tests for the advanced rowing page contract, image-rich exception, image-instruction packets, force-intensity overlays, and forbidden-scope wording.
- Requirements: R1-R9, R18-R32, R39-R46, R50
- Files/components likely touched:
  - `tools/checks/check_markdown_first.py`
  - `tests/`
  - `tests/fixtures/advanced-rowing-machine-tutorial/`
  - `specs/advanced-rowing-machine-tutorial.md` only if a reviewed downstream correction is required
- Dependencies:
  - approved spec and architecture
  - plan-review and test-spec-review before implementation
- Tests to add/update:
  - section-presence checks for `exercises/rowing-machine-advanced.md`
  - scoped image-count exception tests
  - prompt-record image-instruction packet tests
  - force-intensity overlay legend, phase-map, alt-text, and provenance-note tests where automatable
  - forbidden personalized, clinical, copied-UI, and race-coaching wording tests
- Implementation steps:
  - add fixtures for valid and invalid advanced rowing pages
  - add fixtures for prompt packets and provenance rows
  - update checker logic only for the scoped advanced rowing page and generated rowing assets
  - keep unrelated exercise pages under the existing default image-count rules
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/checks/check_markdown_first.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md`
  - `python3 tools/checks/check_privacy.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`
  - `git diff --check`
- Expected observable result: validation rejects out-of-contract advanced rowing pages and accepts the approved scoped contract.
- Commit message: `M1: add advanced rowing validation scaffolding`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed after this handoff update
- Risks:
  - checker logic may accidentally raise image limits globally
  - prompt packet validation may become too rigid for future media workflows
- Rollback/recovery:
  - revert the scoped checker/test additions and keep the approved spec as future implementation guidance

### M2. Advanced Rowing Markdown Content

- Milestone state: closed
- Goal: Create the advanced companion page and link it from the beginner rowing page after validation support exists.
- Requirements: R1-R21, R47-R50
- Files/components likely touched:
  - `exercises/rowing-machine.md`
  - `exercises/rowing-machine-advanced.md`
  - `SOURCES.md`
  - `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/`
- Dependencies:
  - M1 validation support
  - page-local source audit
- Tests to add/update:
  - real-page checker coverage for the advanced rowing page
  - source-index reuse checks when sources are reused globally
- Implementation steps:
  - draft required advanced page sections
  - add prerequisite and scope boundary text
  - explain damper, drag factor, monitor metrics, rhythm, force curve, stroke-rate control, workout types, muscles, feel cues, common mistakes, and safety notes
  - keep examples static and cite concrete claims page-locally
  - add the beginner-page link only after the advanced page validates
  - update `SOURCES.md` when current source-index rules require reused source IDs
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md`
  - `python3 tools/checks/check_privacy.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`
  - `git diff --check`
- Expected observable result: readers can open a static Markdown advanced rowing tutorial without personalized programming, clinical claims, runtime tools, or media dependency.
- Commit message: `M2: add advanced rowing companion page`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - content can drift from literacy into coaching or benchmark programming
  - numeric examples can become under-sourced
- Rollback/recovery:
  - remove the beginner-page link and archive or revert the advanced page while preserving the beginner page

### M3. Governed Media, Prompt Packets, and Provenance

- Milestone state: closed
- Goal: Prepare and integrate the approved first-batch advanced rowing images only through governed prompt records, provenance rows, alt text, and visual review.
- Requirements: R22-R46, R50
- Files/components likely touched:
  - `media/exercises/rowing-machine-advanced/`
  - `media/prompts/exercises/rowing-machine-advanced/`
  - `media/PROVENANCE.md`
  - `exercises/rowing-machine-advanced.md`
  - `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/`
- Dependencies:
  - M1 validation support
  - M2 page sections and image guide
  - governed image-generation workflow
- Tests to add/update:
  - exact asset-path validation for the eight first-batch paths
  - prompt packet reverse `asset_path` tests
  - provenance `prompt_record`, `page_refs`, purpose, and review-status tests
  - technical diagram label duplication tests where automatable
- Implementation steps:
  - write image-instruction packets before generation
  - generate only images accepted by the reviewed implementation slice
  - add approved provenance rows after human visual review
  - integrate image references, alt text, legends, and phase explanations in Markdown
  - record grayscale review for force-intensity images
  - defer any image that does not clearly teach one distinct concept
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py exercises/rowing-machine-advanced.md media/PROVENANCE.md media/prompts/exercises/rowing-machine-advanced`
  - `python3 tools/checks/check_privacy.py exercises/rowing-machine-advanced.md media/prompts/exercises/rowing-machine-advanced media/PROVENANCE.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`
  - `git diff --check`
- Expected observable result: every promoted generated asset has a matching packet, approved provenance, local page reference, meaningful alt text, and visual-safety evidence.
- Commit message: `M3: add advanced rowing governed media assets`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - generated images may include text, brand-like UI, copied monitor layout, identifying people, or misleading force emphasis
  - eight images may be too noisy for the final page
- Rollback/recovery:
  - remove failed image references first, then remove unused prompt records, media files, and provenance rows

### M4. Manual Proof, Review Evidence, and Closeout Preparation

- Milestone state: closed
- Goal: Record source audit, visual-safety review, grayscale review, advanced-reader comprehension proof, and final local validation evidence before code-review and later verification.
- Requirements: R20-R21, R45-R50, AC1-AC10
- Files/components likely touched:
  - `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/`
  - `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/`
  - plan progress and validation notes
- Dependencies:
  - M1-M3 complete or explicitly narrowed
  - non-identifying manual proof inputs
- Tests to add/update:
  - no new automated tests unless manual proof reveals a checker gap
- Implementation steps:
  - record source audit for damper, drag factor, monitor metrics, stroke rate, force curve, workout examples, and safety boundaries
  - record visual-safety review for each generated image
  - record grayscale review for force-intensity images
  - record advanced-reader comprehension proof without private reader data
  - update validation notes with exact commands and outcomes
  - hand off to code-review after milestone implementation evidence is complete
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-07-advanced-rowing-machine-tutorial`
  - `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md RED-FLAGS.md exercises media docs/changes/2026-07-07-advanced-rowing-machine-tutorial`
  - `git diff --check`
- Expected observable result: implementation has automated validation plus recorded manual evidence for claims and visuals that static checks cannot fully verify.
- Commit message: `M4: record advanced rowing proof evidence`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - manual proof may reveal that one or more images should be removed or deferred
  - broad final Markdown checks may expose unrelated pre-existing checker incompatibilities in governance artifacts
- Rollback/recovery:
  - narrow or remove unsupported claims, remove weak images, and document any unrelated validation gap rather than claiming it passed

## Validation plan

- `python3 -m unittest discover -s tests`: run the full local unittest suite after implementation milestones.
- `python3 tools/checks/check_markdown_first.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md media/PROVENANCE.md media/prompts/exercises/rowing-machine-advanced docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: validate the focused page, source, media, packet, provenance, and evidence surface.
- `python3 tools/checks/check_privacy.py exercises media/prompts media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: scan implementation and evidence surfaces for private data.
- `git diff --check`: catch whitespace errors.
- Manual source audit: verify cited support for advanced rowing claims that static checks cannot prove.
- Manual visual-safety review: verify image purpose, privacy, label, brand, clinical, and unsupported-claim boundaries.
- Manual grayscale review: verify force-intensity overlays remain understandable without color.
- Advanced-reader comprehension proof: verify the reader can answer the spec's monitor, drag-factor, force-curve, rate, scope, and image-helpfulness questions.

## Risks and recovery

- Risk: the advanced page becomes coaching or race planning.
  - Recovery: remove or narrow workout examples and link official external plans rather than writing a full plan.
- Risk: force-intensity overlays imply exact measurement.
  - Recovery: revise legends, alt text, packets, and images; remove overlays that fail grayscale or visual-safety review.
- Risk: the image-rich exception becomes a global precedent.
  - Recovery: keep checker and plan wording scoped to `exercises/rowing-machine-advanced.md`.
- Risk: generated images fail visual review.
  - Recovery: remove image references and preserve a valid text-only page.
- Risk: final validation exposes unrelated architecture-checker findings.
  - Recovery: report the validation gap separately and avoid claiming those unrelated checks passed.

## Dependencies

- Plan-review must approve this plan before test-spec authoring.
- Test-spec and test-spec-review must define proof ownership before implementation.
- Image generation must wait until the governed image-instruction packets and implementation milestone authorize it.
- Manual proof must avoid private reader data and private machine paths.

## Progress

- 2026-07-07: Proposal accepted after clean proposal-review.
- 2026-07-07: Spec approved after clean spec-review.
- 2026-07-07: Canonical architecture amendment approved after clean architecture-review.
- 2026-07-07: Draft plan created and routed to plan-review.
- 2026-07-07: Plan-review R1 approved the plan and routed to test-spec.
- 2026-07-07: TSR1 required a plan command revision; M1 fixture validation now uses `tests/fixtures/advanced-rowing-machine-tutorial`.
- 2026-07-07: Plan-review R2 approved the TSR1 plan-command revision.
- 2026-07-07: Test-spec-review R2 approved the proof map and resolved TSR1.
- 2026-07-07: M1 implemented scoped advanced rowing checker validation, focused unittest coverage, and the passing fixture directory required by ART-CMD2.
- 2026-07-07: Code-review R1 requested changes for CR1 and CR2.
- 2026-07-07: Review-resolution implemented fixes for CR1 and CR2 and routed M1 back to code-review.
- 2026-07-07: Code-review R2 accepted the CR1 and CR2 fixes and closed M1.
- 2026-07-07: M2 added `exercises/rowing-machine-advanced.md`, the beginner-page companion link, reused source-index entries, real-page regression tests, M2 source-audit evidence, and an aligned text-only row in the exercise-image audit.
- 2026-07-07: Code-review R3 accepted the M2 implementation and closed M2.
- 2026-07-07: M3 implemented eight governed advanced-rowing image assets, image-instruction prompt packets, provenance rows, page image integration, visual-safety proof, grayscale proof, and real-page media regression tests.
- 2026-07-07: Code-review R4 accepted the M3 implementation and closed M3.
- 2026-07-07: M4 recorded final source-audit proof, advanced-reader comprehension proof, validation ledger, broad local validation evidence, and routed the milestone to code-review.
- 2026-07-07: Code-review R5 accepted the M4 implementation and closed M4.
- 2026-07-07: Explain-change recorded the reviewed-diff rationale in `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/explain-change.md` and routed the change to verify.
- 2026-07-07: Final local verification passed, recorded `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/verify-report.md`, and routed the change to PR handoff. Hosted CI was not observed.
- 2026-07-07: PR #18 opened from `2026-07-07-advanced-rowing-machine-tutorial` to `main`; GitHub Actions `Validation checks` was pending at handoff.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-07 | Use four implementation milestones. | Validation, Markdown, media assets, and manual proof have different risk profiles and review evidence. | One large implementation milestone. |
| 2026-07-07 | Keep image-instruction packets inside prompt records. | This reuses the accepted prompt-record architecture while adding the advanced rowing fields needed by the spec. | New sidecar metadata format. |
| 2026-07-07 | Keep the image-rich exception scoped to the advanced rowing page. | The spec and architecture do not globally raise exercise image limits. | Global image-count policy change. |
| 2026-07-07 | Validate M1 through fixtures before the real advanced page exists. | The real page is created in M2, so M1 should prove checker behavior with tests and fixtures. | Running real-page validation before the page exists. |
| 2026-07-07 | Scope M1 checker fixture commands to `tests/fixtures/advanced-rowing-machine-tutorial`. | The broader `tests/fixtures` tree intentionally contains invalid fixtures for other checker tests. | Scanning all fixture directories as one passing command. |
| 2026-07-07 | Keep M2 media-free. | M2 proves the static advanced Markdown contract; M3 owns generated images, prompt records, provenance, visual-safety review, and grayscale review. | Referencing future generated image paths before media governance exists. |
| 2026-07-07 | Use no readable in-image labels for all M3 advanced rowing assets. | Markdown and alt text can carry the labels while preserving the stricter body-image and technical-diagram accessibility boundary. | Minimal diagram labels in the generated images. |
| 2026-07-07 | Retain all eight first-batch images after visual review. | Each asset passed the one-purpose, privacy, label, brand, clinical, and unsupported-claim checks and maps to a distinct page concept. | Deferring the monitor, damper, interval, or rate visuals. |

## Surprises and discoveries

- The canonical architecture package has pre-existing Markdown-first checker incompatibilities when scanned directly; the architecture-review record treats that as a validation gap rather than an amendment blocker.
- Adding `exercises/rowing-machine-advanced.md` required updating the existing exercise-image audit row set because current tests enumerate every `exercises/*.md` page.
- M3 full-suite validation caught that using the exact forbidden phrase in rule text can trip the media-forbidden checker; the page and prompt packets now use `unsupported outcome claims` for the instructional boundary.
- M4 broad Markdown-first validation requires change-local proof documents to include `## Sources` and to reuse global source IDs exactly for non-local links.

## Validation notes

- `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/spec-review-r1.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/architecture-review-r1.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md specs/advanced-rowing-machine-tutorial.md`: pass, checked 4 Markdown file(s).
- `python3 tools/checks/check_privacy.py docs/changes/2026-07-07-advanced-rowing-machine-tutorial specs/advanced-rowing-machine-tutorial.md docs/architecture/system/architecture.md`: pass, checked 7 file(s).
- `git diff --check`: pass, no whitespace errors reported.
- `python3 tools/checks/check_markdown_first.py docs/architecture/system/architecture.md specs/advanced-rowing-machine-tutorial.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/spec-review-r1.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md`: fail on pre-existing canonical architecture checker incompatibilities.
- `python3 -m unittest tests.test_advanced_rowing_machine_tutorial`: pass, 5 tests.
- `python3 -m unittest discover -s tests`: pass, 229 tests.
- `python3 tools/checks/check_markdown_first.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md`: pass, checked 4 Markdown file(s).
- `python3 tools/checks/check_privacy.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: pass, checked 13 file(s).
- `git diff --check`: pass, no whitespace errors reported.
- `python3 -m unittest tests.test_advanced_rowing_machine_tutorial`: pass, 6 tests.
- `python3 -m unittest discover -s tests`: pass, 230 tests.
- `python3 tools/checks/check_markdown_first.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md`: pass, checked 4 Markdown file(s).
- `python3 tools/checks/check_privacy.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: pass, checked 14 file(s).
- `git diff --check`: pass, no whitespace errors reported.
- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_rowing_machine_links_to_advanced_page tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_page_shape_and_prerequisites tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_concepts_are_static_and_source_backed tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_workout_types_force_system_and_sources`: initial fail before implementation because `exercises/rowing-machine-advanced.md` and the beginner-page link were missing.
- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_rowing_machine_links_to_advanced_page tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_page_shape_and_prerequisites tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_concepts_are_static_and_source_backed tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_workout_types_force_system_and_sources`: pass, 4 tests.
- `python3 -m unittest discover -s tests`: pass, 234 tests.
- `python3 tools/checks/check_markdown_first.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md`: pass, checked 4 Markdown file(s).
- `python3 tools/checks/check_privacy.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: pass, checked 17 file(s).
- `git diff --check`: pass, no whitespace errors reported.
- Code-review R3 reviewer-ran `python3 -m unittest discover -s tests`: pass, 234 tests.
- Code-review R3 reviewer-ran `python3 tools/checks/check_markdown_first.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md`: pass, checked 4 Markdown file(s).
- Code-review R3 reviewer-ran `python3 tools/checks/check_privacy.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: pass, checked 17 file(s).
- Code-review R3 reviewer-ran `git diff --check`: pass, no whitespace errors reported.
- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_media_batch_is_local_prompt_backed_and_reviewed tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_prompt_packets_record_force_and_label_boundaries tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_media_markdown_has_legends_and_label_duplication`: initial M3 fail before page integration because image guide sections and assets were not complete.
- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_media_batch_is_local_prompt_backed_and_reviewed tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_prompt_packets_record_force_and_label_boundaries tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_advanced_rowing_media_markdown_has_legends_and_label_duplication`: pass, 3 tests.
- `python3 -m unittest discover -s tests`: initial M3 fail because the media-forbidden checker caught the exact phrase `performance promise` in prompt constraints and `unsupported promises` in rule text.
- `python3 -m unittest discover -s tests`: pass, 237 tests.
- `python3 tools/checks/check_markdown_first.py exercises/rowing-machine-advanced.md media/PROVENANCE.md media/prompts/exercises/rowing-machine-advanced`: pass, checked 2 Markdown file(s).
- `python3 tools/checks/check_privacy.py exercises/rowing-machine-advanced.md media/prompts/exercises/rowing-machine-advanced media/PROVENANCE.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: pass, checked 26 file(s).
- `git diff --check`: pass, no whitespace errors reported.
- Code-review R4 reviewer-ran `python3 -m unittest discover -s tests`: pass, 237 tests.
- Code-review R4 reviewer-ran `python3 tools/checks/check_markdown_first.py exercises/rowing-machine-advanced.md media/PROVENANCE.md media/prompts/exercises/rowing-machine-advanced`: pass, checked 2 Markdown file(s).
- Code-review R4 reviewer-ran `python3 tools/checks/check_privacy.py exercises/rowing-machine-advanced.md media/prompts/exercises/rowing-machine-advanced media/PROVENANCE.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: pass, checked 26 file(s).
- Code-review R4 reviewer-ran `git diff --check`: pass, no whitespace errors reported.
- `python3 -m unittest discover -s tests`: pass, 237 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: initial M4 fail because proof documents needed `## Sources`, source-linked safety rows, and existing global source IDs for non-local source references.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: pass, checked 44 Markdown file(s).
- `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md RED-FLAGS.md exercises media docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: pass, checked 249 file(s).
- `git diff --check`: pass, no whitespace errors reported.
- Code-review R5 reviewer-ran `python3 -m unittest discover -s tests`: pass, 237 tests.
- Code-review R5 reviewer-ran `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: pass, checked 44 Markdown file(s).
- Code-review R5 reviewer-ran `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md RED-FLAGS.md exercises media docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: pass, checked 249 file(s).
- Code-review R5 reviewer-ran `git diff --check`: pass, no whitespace errors reported.
- Explain-change validation passed with `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-07-advanced-rowing-machine-tutorial/explain-change.md docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md docs/plan.md`: checked 3 Markdown file(s).
- Explain-change validation passed with `python3 tools/checks/check_privacy.py docs/changes/2026-07-07-advanced-rowing-machine-tutorial/explain-change.md docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md docs/plan.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/change.yaml`: checked 4 file(s).
- Explain-change state-sync inspection passed with `rg -n 'Current stage: verify|Next stage: verify|current_stage: verify|next_stage: verify|Explain-change recorded|Ready for verify|open_findings: \[\]|review_resolution_status: closed|Final verification has not run yet|Hosted CI has not been observed' docs/plan.md docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/change.yaml docs/changes/2026-07-07-advanced-rowing-machine-tutorial/explain-change.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-resolution.md`.
- Explain-change validation passed with `git diff --check`: no whitespace errors reported.
- Final verify passed with `python3 -m unittest discover -s tests`: 237 tests.
- Final verify passed with `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md principles exercises patterns`: checked 30 Markdown file(s).
- Final verify passed with `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md docs specs tools tests principles exercises patterns`: checked 594 file(s).
- Final verify passed with `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: checked 46 Markdown file(s).
- Final verify passed with `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md RED-FLAGS.md exercises media docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: checked 251 file(s).
- Final verify passed with `python3 tools/checks/check_markdown_first.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md`: checked 4 Markdown file(s).
- Final verify passed with `python3 tools/checks/check_markdown_first.py exercises/rowing-machine-advanced.md media/PROVENANCE.md media/prompts/exercises/rowing-machine-advanced`: checked 2 Markdown file(s).
- Final verify passed with `python3 tools/checks/check_privacy.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial`: checked 26 file(s).
- Final verify passed with `git diff --check`: no whitespace errors reported.
- Verify-report validation passed with `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-07-advanced-rowing-machine-tutorial/verify-report.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/explain-change.md docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md docs/plan.md`: checked 4 Markdown file(s).
- Verify-report validation passed with `python3 tools/checks/check_privacy.py docs/changes/2026-07-07-advanced-rowing-machine-tutorial/verify-report.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/explain-change.md docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md docs/plan.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/change.yaml`: checked 5 file(s).
- Verify-report state-sync inspection passed with `rg -n 'Current stage: pr|Next stage: pr|current_stage: pr|next_stage: pr|current_verification_status: branch-ready|Ready for PR handoff|branch-ready|open_findings: \[\]|review_resolution_status: closed|Hosted CI was not observed|PR body/open readiness is not claimed' docs/plan.md docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/change.yaml docs/changes/2026-07-07-advanced-rowing-machine-tutorial/verify-report.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-resolution.md`.
- Verify-report validation passed with `git diff --check`: no whitespace errors reported.

## Outcome and retrospective

- M1 implementation and review-resolution are closed.
- M2 implementation is closed after clean code-review R3.
- M3 implementation is closed after clean code-review R4.
- M4 implementation is closed after clean code-review R5.
- Explain-change is complete.
- Final local verification is complete and branch-ready is recorded in `verify-report.md`.
- PR #18 is open; hosted CI was pending at handoff.

## Readiness

- See `Current Handoff Summary`.
- Ready for PR review after hosted CI reports.

## Sources

[local-2026-07-07-advanced-rowing-machine-tutorial-proposal]: ../proposals/2026-07-07-advanced-rowing-machine-tutorial.md
[local-2026-07-07-advanced-rowing-machine-tutorial-spec]: ../../specs/advanced-rowing-machine-tutorial.md
[local-2026-07-07-advanced-rowing-machine-tutorial-spec-review]: ../changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/spec-review-r1.md
[local-2026-07-07-advanced-rowing-machine-tutorial-architecture]: ../architecture/system/architecture.md
[local-2026-07-07-advanced-rowing-machine-tutorial-architecture-review]: ../changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/architecture-review-r1.md
