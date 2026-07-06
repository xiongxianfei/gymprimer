# Explain Change: Necessary Images and Tai Chi Exercise

## Summary

This change adds a Markdown-first `exercises/tai-chi-basics.md` page, a Tai Chi-specific top-10 image candidate record, exactly three generated support images, prompt records, approved provenance rows, and manual proof that the images remain support material.

The work exists because Tai Chi is difficult to explain with text alone, but GymPrimer still requires citations, safety routing, Markdown source-of-truth, generated-media provenance, and bounded review before images become project assets.

Current handoff state: M1-M4 are closed by code-review, no implementation milestones remain, explain-change is refreshed, and `verify` is next.
This artifact does not claim final verification, branch readiness, PR readiness, or CI success.

## Problem

The accepted proposal identified two problems.
First, image generation needed prioritization so the project would not generate images randomly or for every possible cue.
Second, Tai Chi needed visuals because beginner posture, weight shift, relaxed movement, and broad muscle attention are hard to understand from text alone.

The owner clarified that the top-10 list is for one specific exercise, not a cross-project image backlog, and that the user-facing name and path must be Tai Chi and `exercises/tai-chi-basics.md`.

## Decision Trail

| Stage | Decision | Evidence |
|---|---|---|
| Proposal | Choose Option C: evaluate ten Tai Chi image candidates, generate the top three first, and add the Tai Chi page. | `docs/proposals/2026-07-05-necessary-images-and-tai-chi-exercise.md` |
| Proposal review | Treat candidates 4-10 as deferred alternatives subject to the three-image limit; add approved low-load labels in the method sample. | `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/proposal-review-r2.md` |
| Spec | Define R1-R43 for page scope, method labels, image count, prompt records, provenance, alt text, visual safety, comprehension proof, rollback, privacy, and product boundaries. | `specs/necessary-images-and-tai-chi-exercise.md` |
| Architecture | Keep Markdown canonical; store generated rasters under `media/exercises/`, prompts under `media/prompts/`, and provenance in `media/PROVENANCE.md`. | `docs/architecture/system/architecture.md` |
| Plan | Split implementation into M1 validation proof map, M2 text page, M3 governed image batch, and M4 review evidence. | `docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md` |
| Test spec | Map R1-R43 to TC-T1 through TC-T11, CMD1-CMD6, and manual proofs MP1-MP4. | `specs/necessary-images-and-tai-chi-exercise.test.md` |
| Code review | M1, M2, M3, and M4 passed with no material implementation findings. | `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-log.md` |

## Diff Rationale By Area

| Files | Change | Reason | Source artifact | Test/evidence |
|---|---|---|---|---|
| `docs/proposals/2026-07-05-necessary-images-and-tai-chi-exercise.md` | Records the accepted Tai Chi direction, top-10 single-exercise image list, first three images, and rejected alternatives. | Durable product decision before spec and implementation. | Proposal Option C and proposal-review R2. | Proposal-review R2 approved. |
| `specs/necessary-images-and-tai-chi-exercise.md` | Defines R1-R43 for page content, image limits, provenance, prompt records, visual safety, comprehension proof, rollback, and no-app boundaries. | Turns the accepted direction into testable contract language. | Proposal and spec-review R1. | Spec-review R1 approved. |
| `specs/necessary-images-and-tai-chi-exercise.test.md` | Defines TC-T1 through TC-T11, edge cases, CMD1-CMD6, and MP1-MP4. | Establishes proof obligations before implementation. | Spec R1-R43. | Test-spec-review R1 approved. |
| `docs/architecture/system/architecture.md` | Adds the Tai Chi media path and provenance/prompt-record flow to the canonical architecture. | Generated images affect repository media, prompt, provenance, and review boundaries. | Spec media requirements R20-R40. | Architecture-review R1 approved. |
| `docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md`, `docs/plan.md`, `docs/changes/.../change.yaml` | Track milestone state, validation evidence, and current final-closeout handoff. | Keeps lifecycle state consistent with implementation and code-review outcomes. | Plan and code-review receipts. | Code-review M4 R1 closed M4. |
| `exercises/tai-chi-basics.md` | Adds the static beginner Tai Chi page with required sections, source-backed setup/safety, `low_load_control_drill`, broad muscle guidance, and three image references. | Satisfies R1-R19 and references the approved first image batch after M3. | Spec R1-R19 and R36-R43. | Real-page tests and Markdown-first checks. |
| `SOURCES.md` | Adds shared Tai Chi source IDs for reused public sources. | Global source index must include reused non-local source IDs. | R11 and source-index rules. | `test_tai_chi_setup_safety_sources_and_source_index`. |
| `media/exercises/tai-chi-basics/*.png` | Adds `setup.png`, `weight-shift.png`, and `muscle-attention.png`. | Implements the first three generated support images and no more. | R21-R29. | M3 real-asset tests and visual-safety review. |
| `media/prompts/exercises/tai-chi-basics/*.md` | Adds exact prompt records for each generated raster. | Every generated raster needs a repository-local prompt record. | R31-R32. | Prompt-record tests and provenance checks. |
| `media/PROVENANCE.md` | Adds approved provenance rows for the three Tai Chi images. | Records asset type, media purpose, generator, reviewer, status, prompt record, and page refs before promotion. | R30, R33-R35. | `test_tai_chi_m3_support_batch_has_page_images_prompt_records_and_visual_review`. |
| `docs/changes/.../source-audit.md` | Records MP1 source-support samples for setup, safety, method, movement, muscle, feel, and stop conditions. | Static checks cannot prove claim-level source support by themselves. | MP1 and R11/R15/R19. | `test_tai_chi_m2_source_audit_records_required_claim_samples`. |
| `docs/changes/.../visual-safety-review.md` | Records MP2 review for each selected image. | Static tooling cannot prove generated-image visual semantics. | R38-R40 and MP2. | M3 image test and code-review M3 R1. |
| `docs/changes/.../beginner-comprehension-proof.md` | Records MP3 non-identifying beginner-comprehension prompt outcomes. | The change must show whether a beginner can explain purpose, stance, weight shift, body feel, pause conditions, and image usefulness. | R41 and MP3. | M4 proof test and code-review M4 R1. |
| `docs/changes/.../rollback-proof.md` | Records MP4 text-only rollback steps and temporary review-state validation. | The page must remain valid if images, prompt records, and provenance rows are removed. | R42 and MP4. | M4 rollback proof test and temporary rollback rehearsal. |
| `docs/changes/.../validation-notes.md` | Records M4 local validation and the `pytest` environment gap. | Keeps validation evidence durable before final verify. | Test spec CMD1-CMD6. | Code-review M4 R1 challenged the evidence. |
| `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | Adds Tai Chi to the current exercise-image inventory. | Existing image-standard tests require current exercise pages to be represented in the audit. | Exercise-image standard compatibility. | Full unittest discovery passed after update. |
| `tests/test_exercise_image_standard.py` | Adds candidate-pool, three-image, prompt-record, provenance, alt-text, and visual-safety coverage. | Proves media contract behavior and negative cases before accepting generated images. | TC-T6 through TC-T10. | Focused image tests and broad discovery. |
| `tests/test_exercise_method_guidance.py` | Adds Tai Chi `low_load_control_drill` fixtures. | Proves method labels and rejects adaptive/clinical programming language. | R12-R16 and TC-T4. | `python3 -m unittest tests.test_exercise_method_guidance`. |
| `tests/test_markdown_first_real_pages.py` | Adds real-page tests for Tai Chi structure, scope, sources, method, muscle guidance, M2 source audit, M3 images, and M4 proof records. | Connects the spec to actual Markdown, media, and review-evidence artifacts. | TC-T1 through TC-T5 and TC-T11. | Focused and broad unittest commands passed. |

## Tests Added Or Changed

| Test or proof | What it proves | Why this level is appropriate |
|---|---|---|
| TC-T1 through TC-T5 real-page tests | Page path, title, required sections, beginner scope, source support, method labels, and broad muscle guidance. | These are stable Markdown contracts that can be checked directly. |
| TC-T6 and TC-T7 image candidate/count tests | The Tai Chi candidate pool exists, first batch has exactly three images, and a fourth image or second muscle-attention image fails. | Image-count limits are deterministic and should not rely on manual review. |
| TC-T9 prompt/provenance tests | Image references map to approved provenance rows and prompt records. | Prompt/provenance wiring is structured enough for automation. |
| TC-T10 alt-text and visual-safety text tests | Alt text is meaningful and obvious unsafe visual text patterns fail. | Static text checks catch regressions; MP2 covers visual semantics. |
| TC-T11 rollback proof tests | M4 records text-only rollback cleanup for image references, assets, prompt records, and provenance rows. | The actual rollback is partly manual, so tests require durable proof and commands. |
| MP1 source audit | Sampled Tai Chi claims have page-local source support. | Claim-level support requires manual judgment beyond link presence. |
| MP2 visual-safety review | Images teach one concept and avoid text, labels, identifiable people, brands, clinical/combat framing, unsupported claims, and overprecise anatomy. | Generated-image semantics require human visual inspection. |
| MP3 beginner comprehension proof | Required beginner prompts are answered without private health or reader data. | Reader understanding is not fully automatable. |
| MP4 rollback rehearsal | A text-only temporary copy passes focused checks after image references and Tai Chi provenance rows are removed. | Proves rollback behavior without destructive edits to the working tree. |

## Validation Evidence Available Before Final Verify

Implementation and review recorded these local checks:

- `python3 -m unittest tests.test_exercise_method_guidance`
- `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md`
- `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md media/PROVENANCE.md media/prompts/exercises/tai-chi-basics/ docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/`
- `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`
- `python3 -m unittest discover -s tests`
- `git diff --check`
- Temporary rollback rehearsal using a copied text-only root.

Review-run validation in `reviews/code-review-m4-r1.md` also passed the focused M4 proof tests and repeated the rollback rehearsal.

`python3 -m pytest` is unavailable in this environment because `pytest` is not installed.
The active reviewed test spec uses unittest commands as CMD1, CMD4, and CMD5, so the pytest gap is recorded but is not treated as a blocker for this stage.

Hosted CI has not been observed for this branch.

## Review Resolution Summary

There are no open material implementation review findings.

Proposal-review R1 had two findings:

- `PR-TC-1`: closed by proposal-review R2 after candidates 4-10 were clarified as deferred alternatives subject to the three-image limit.
- `PR-TC-2`: closed by proposal-review R2 after the method sample was aligned with `Effort:`, `Rest:`, and `Stop if:` labels.

`docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-resolution.md` records those closed findings and no open findings.
Code-review M1, M2, M3, and M4 are all clean-with-notes.

## Alternatives Rejected

| Alternative | Why it was rejected |
|---|---|
| Generate Tai Chi images immediately before text/spec review. | It would skip the governed media workflow, prompt records, provenance rows, and review criteria. |
| Add Tai Chi as text-only and stop there. | The proposal judged Tai Chi posture, weight shifting, and continuous movement as image-dependent for beginners. |
| Generate all ten Tai Chi candidate images. | The approved direction limits the first batch to exactly three images; candidates 4-10 are deferred alternatives or future replacements. |
| Publish a fourth image without a downstream exception. | R26-R28 require explicit approved justification before any page version exceeds three exercise images. |
| Teach a full Tai Chi form, martial application, therapy protocol, or fall-prevention program. | The proposal, spec, and constitution keep this page static, beginner-facing, non-clinical, and non-martial. |
| Add runtime app, video, account, database, CMS, or generated public API behavior. | R43 explicitly excludes those product surfaces. |

## Scope Control

The implementation preserves the approved non-goals:

- one page at `exercises/tai-chi-basics.md`;
- exactly three generated support images in the first batch;
- all exact cues, safety notes, muscle names, and citations remain in Markdown;
- images are broad visual support, not source-of-truth instruction;
- no full form, lineage debate, martial application, recovery protocol, treatment claim, fall-prevention program, personalized coaching, or hosted product behavior;
- no borrowed web images, stock photos, identifiable people, brand marks, in-image text, labels, pain marks, or clinical framing.

## Risks And Follow-Ups

Remaining risks before publication:

- Final verification has not run yet.
- Hosted CI has not been observed for this branch.
- The beginner comprehension proof is a non-identifying reviewer simulation, not live public-reader research.
- Generated images remain static aids and cannot prove exact Tai Chi form quality or individual balance safety.
- `pytest` is not installed, so the optional historical `python3 -m pytest` command cannot run unless the project chooses to add that dependency.

Next lifecycle stage: `verify`.
PR handoff should happen only if final verification passes.
