# Explain Change: Top-Five Generated Images for Fewer-Than-Five Exercise Documents

## Status

Reviewed-diff rationale complete after M3 code-review R5.

Next lifecycle stage: verify.

This explanation does not claim final verification, hosted CI, PR readiness, or branch readiness.

## Summary

This change creates a governed named-population exception that lets eighteen listed exercise documents target five total accepted images per page.
Existing accepted images count toward the total, accepted older sequence images are preserved, and new generated or derived raster images fill only the page-local gaps.

The implementation adds validator support, prioritization audit validation, real-page media checks, page-local audit evidence, generated and derived image assets, prompt records, provenance rows, page image references, review records, and validation notes.
`exercises/baduanjin-basics.md` remains excluded because it already had five images.

## Problem

The accepted image-prioritization workflow previously treated fewer-than-five images as an evaluation trigger, not an automatic generation target.
The owner then requested top-five high-quality images for all listed fewer-than-five exercise documents, with five meaning five total images per page including existing accepted images.

That request conflicted with the prior normal exercise-image count behavior.
The project needed a durable policy exception, tests, generated-media records, and rollback evidence before producing a large image batch.

## Decision Trail

| Decision source | Decision | Implementation result |
|---|---|---|
| Proposal option C | Use a governed named-population top-five initiative rather than direct chat generation. | Added proposal/spec/plan/test-spec workflow artifacts and kept all generation under reviewed milestones. |
| Owner decision | Do not require repository-local `human_reviewer`, review-owner, visual-safety-review evidence, or replacement accountability artifacts for this initiative. | Added a path-scoped reviewer exception while retaining prompt records, provenance, page refs, privacy checks, and rollback evidence. |
| Spec R1-R2 | Include exactly eighteen named exercise documents and exclude Baduanjin. | Added named-population validation and did not edit `exercises/baduanjin-basics.md` for this initiative. |
| Spec R3-R14 | Treat fewer-than-five as a generation trigger for the named population, count existing images, and reject forced filler or sixth images. | Added audit validation, page-local top-10 evidence, M2 coverage-limit handling for band pull-apart, and five-image real-page coverage for the rest. |
| Spec R15-R22A | Require accepted exercise image purposes, local media paths, prompt records, provenance rows, and scoped blank reviewer behavior. | Added assets under `media/exercises/`, prompt records under `media/prompts/exercises/`, and rows in `media/PROVENANCE.md`. |
| Spec R23-R26 | Keep Markdown authoritative and preserve acceptable existing images unless a concrete page-local issue exists. | Kept existing images and older sequence images, added support images next to relevant Markdown sections, and used crops only as supplemental derived references. |
| Spec R27-R30 | Cover the population through two or three milestones and avoid runtime/product expansion. | Implemented M1 validation, M2 first batch, and M3 remaining batch with no hosted app, CMS, database, API, video, or coaching behavior. |
| Architecture | Generated exercise images remain repository-local support assets with provenance and prompt records; this initiative gets a named reviewer-field exception. | Kept the change inside Markdown, static media, prompt records, validation tools, tests, and change-local evidence. |
| Plan | Split implementation into validation framework, first batch, and remaining batch closeout. | M1, M2, and M3 are closed by code-review R2, R4, and R5. |

## Diff Rationale By Area

| Area | Files | Why they changed | Requirements and evidence |
|---|---|---|---|
| Governing contract | `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`, `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md` | Captures the named population, five-total-image target, reviewer exception, proof map, and validation commands. | Proposal option C, R1-R30, T1-T8, MP1-MP4. |
| Architecture alignment | `docs/architecture/system/architecture.md` | Records this named-population reviewer-field exception and keeps generated media under the existing Markdown-first repository-local media architecture. | Architecture-review R1, code-review R5. |
| Execution plan and lifecycle | `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`, `docs/plan.md`, `docs/changes/.../change.yaml`, `review-log.md`, `reviews/*.md` | Records milestone sequencing, validation notes, review outcomes, and current handoff state. | Plan-review R1, test-spec-review R1, code-review R2/R4/R5. |
| Audit validation | `tools/checks/exercise_document_image_prioritization.py`, `tests/test_exercise_document_image_prioritization.py`, `docs/changes/.../m1-audit-framework.md` | Adds deterministic validation for included/excluded population, score fields, dispositions, rank 1-5 behavior, and coverage-limit audit shape. | R1-R14, R25-R30, T1-T4, CR-T5IMG-M1-1, CR-T5IMG-M1-2. |
| Exercise media validation | `tools/checks/check_markdown_first.py`, `tests/test_exercise_image_standard.py` | Adds named top-five image-count exception, path-scoped blank reviewer behavior, prompt-record/provenance checks, duplicate muscle-attention protection, and real-page M2/M3 regression checks. | R15-R22A, EC8-EC9A, T4-T6. |
| M2 first batch pages | `exercises/band-pull-apart.md`, `exercises/bird-dog.md` | Adds the first reviewed image batch while preserving existing accepted images; band pull-apart stays at four because the fifth candidate duplicated coverage. | R7-R14, R23-R26, M2 audit, code-review R4. |
| M2 first batch media | `media/exercises/band-pull-apart/*`, `media/exercises/bird-dog/*`, related prompt records, `media/PROVENANCE.md` | Adds setup, movement, shorter-range, posture-control, and muscle-attention support images selected by the first batch audit. | R16-R22A, MP1-MP3, CR-T5IMG-M2-1, CR-T5IMG-M2-2. |
| M3 remaining pages | `exercises/brisk-walking.md`, `exercises/chest-press.md`, `exercises/chin-nod.md`, `exercises/dead-bug.md`, `exercises/glute-bridge.md`, `exercises/hip-hinge.md`, `exercises/incline-push-up.md`, `exercises/kneeling-hip-flexor-stretch.md`, `exercises/lat-pulldown.md`, `exercises/plank.md`, `exercises/prone-y-t.md`, `exercises/rowing-machine.md`, `exercises/seated-row.md`, `exercises/tai-chi-basics.md`, `exercises/thoracic-extension.md`, `exercises/wall-slide.md` | Adds image references next to setup, movement, muscle, easier-option, or important-note sections so images support nearby Markdown rather than replace it. | R3-R6, R11-R15, R23-R28, M3 audit, code-review R5. |
| M3 remaining media | `media/exercises/<exercise-slug>/`, `media/prompts/exercises/<exercise-slug>/`, `media/PROVENANCE.md` | Adds generated support images and deterministic crops from accepted generated source assets, with prompt records and provenance rows for every promoted image. | R16-R22A, MP2-MP4, T5-T8. |
| Audit evidence | `docs/changes/.../evidence/m2-first-batch-audit.md`, `docs/changes/.../evidence/m3-remaining-batch-audit.md` | Records per-page candidate ranking, 1-5 scoring, dispositions, source-support, beginner-comprehension, and rollback proof. | R7-R14, R22A, MP1-MP4. |
| Existing real-page tests | `tests/test_markdown_first_real_pages.py` | Updates older Tai Chi and brisk-walking assertions to preserve their required image checks while accepting the approved top-five count. | Compatibility with R3-R6 and older page-specific media contracts. |

## Tests Added Or Changed

| Test area | What it proves | Why this level is appropriate |
|---|---|---|
| Prioritization unit tests | The named population is exact, Baduanjin is excluded, score fields use `setup_value`, top-five rank dispositions reject `automatic_generation`, and valid named dispositions pass. | Unit tests prove audit-policy behavior before real media promotion. |
| Exercise image standard fixtures | Five-image pages pass only for the named initiative, sixth images fail, second muscle-attention images fail, missing prompt records still fail, and blank reviewers are path-scoped. | Checker-level fixtures protect the repository-wide media contract. |
| M2 real-page regression | Band pull-apart and bird dog page images, prompt records, provenance rows, blank reviewers, score scale, and coverage-limit evidence are wired correctly. | Real-page tests catch drift across Markdown, media, provenance, and evidence. |
| M3 real-page regression | Every remaining M3 page reaches its expected count, each promoted asset exists, each has one provenance row and prompt record, no page has more than one muscle-attention image, and M3 audit scores stay in the 1-5 range. | Integration-level proof is appropriate because the implementation spans pages, media files, prompt records, and audit evidence. |
| Existing Tai Chi and brisk-walking tests | Previously required page-specific images remain present and prompt-backed after those pages move to five total images. | Compatibility tests ensure the top-five initiative does not erase older page contracts. |

## Validation Evidence Available Before Final Verify

Latest M3 code-review R5 reruns:

| Command | Result |
|---|---|
| `python3 -m unittest discover -s tests` | pass: 207 tests |
| `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` | pass: checked 37 Markdown files |
| `python3 tools/checks/check_privacy.py exercises media media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` | pass: checked 214 files |
| `git diff --check` | pass |

Additional review-only artifact checks after recording code-review R5:

| Command | Result |
|---|---|
| `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` | pass: checked 18 Markdown files |
| `python3 tools/checks/check_privacy.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` | pass: checked 19 files |
| `git diff --check` | pass |

No hosted CI run has been observed for this branch.

## Review Resolution Summary

Five material findings were recorded and resolved:

| Finding | Disposition | Resolution |
|---|---|---|
| PR-T5IMG-1 | resolved before proposal-review R2 | Owner chose no repository-local reviewer or replacement accountability requirements for this initiative; proposal and spec were revised accordingly. |
| CR-T5IMG-M1-1 | closed by code-review R2 | Replaced `safety_setup_value` with `setup_value` in audit validation, fixtures, tests, and M1 audit evidence. |
| CR-T5IMG-M1-2 | closed by code-review R2 | Made rank 1-5 `automatic_generation` fail while keeping `generate_now` and `first_generation_candidate` valid for the named initiative. |
| CR-T5IMG-M2-1 | closed by code-review R4 | Updated M2 audit scoring to the approved 1-5 range and added regression checks for score text and zero scores. |
| CR-T5IMG-M2-2 | closed by code-review R4 | Replaced `bird-dog/short-reach.png` with a visibly smaller-reach image and updated the prompt record notes. |

Details are in `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-resolution.md`.

M3 code-review R5 passed with no material findings.

## Alternatives Rejected

- Keep the prior minimum-needed policy: rejected because it did not satisfy the owner-selected top-five direction.
- Generate all images directly from chat: rejected because it would bypass source-of-truth order, prompt records, provenance, tests, and review.
- Generate five new images per page in addition to existing images: rejected because the approved target is five total accepted images per page.
- Replace older sequence images for style alone: rejected because accepted older sequence images count when page-local audit preserves them.
- Add a sixth image where rank 6 looked useful: rejected because the approved default forbids sixth images without later page-specific authorization.
- Add repository-local human-reviewer replacement artifacts: rejected by owner decision and spec review for this named initiative.

## Scope Control

Preserved non-goals:

- No generated images for `exercises/baduanjin-basics.md` under this initiative.
- No borrowed web images, stock photos, screenshots, remote image references, branded-equipment dependency, or identifiable private-person imagery.
- No second muscle-attention image on any included page.
- No in-image text, labels, citations, warnings, red pain marks, clinical assessment framing, treatment claims, correctness badges, posture-correction promises, or before-and-after framing.
- No hosted app, CMS, database, user account, user-input flow, generated public API, video-first media path, animation, workout planner, clinical product, recovery-care protocol, or personalized coaching behavior.
- No shift of setup, movement, muscles, feel cues, safety notes, or sources from Markdown into images.

## Risks And Follow-Ups

- Visual review was sampled in code-review R5; final verification still needs to decide whether additional visual sampling is required before PR handoff.
- The generated-media diff is large, so PR reviewers should focus on page/media/provenance consistency and whether any image duplicates or weakens nearby Markdown.
- Existing pages now carry more images, so future content edits should keep the five-total-image exception scoped to this named initiative.
- Final verification still needs to run after this explanation.
- PR readiness is not claimed until verify and PR handoff complete.

## Sources

- [Proposal](../../../docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md)
- [Spec](../../../specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md)
- [Test spec](../../../specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md)
- [Plan](../../plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md)
- [Review resolution](review-resolution.md)
- [Code-review R5](reviews/code-review-r5.md)
- [M2 first batch audit](evidence/m2-first-batch-audit.md)
- [M3 remaining batch audit](evidence/m3-remaining-batch-audit.md)
