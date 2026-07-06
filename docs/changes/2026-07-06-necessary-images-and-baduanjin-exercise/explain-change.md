# Explain Change: Necessary Images and Baduanjin Exercise

## Status

Final reviewed-diff rationale complete after final holistic code-review R1.

Next lifecycle stage: verify.

This explanation does not claim final verification, hosted CI, PR readiness, or branch readiness.

## Summary

This change adds a static beginner-facing `Baduanjin Basics` exercise page with exactly five governed generated support images.
It also adds the spec, test spec, architecture amendment, execution plan, tests, prompt records, provenance rows, manual visual-safety proof, beginner-comprehension proof, rollback proof, review records, and validation evidence needed to keep the page Markdown-first and non-clinical.

The main product decision is the path-scoped five-image exception for `exercises/baduanjin-basics.md`.
Baduanjin is a sequence-based gentle-movement page, so the first image batch covers setup, upward reach, drawing-bow side stance, alternating reach, and broad muscle attention while keeping candidates 6-10 deferred.

## Problem

Baduanjin is not one static exercise setup.
Beginners need visual help for ready stance, soft knees, arm path, weight shift, side stance, upward reach, alternating reach, and broad body regions to notice.

The risk was that adding many images could turn a static primer page into a martial curriculum, medical qigong treatment page, fall-prevention program, adaptive coaching feature, or image-led source of truth.
The implementation therefore makes Markdown authoritative, uses generated images only as support assets, and requires prompt records, provenance rows, manual visual review, beginner-comprehension proof, and rollback proof.

## Decision Trail

| Decision source | Decision | Implementation result |
|---|---|---|
| Proposal | Add Baduanjin Basics and evaluate top-10 image candidates before generation. | Added `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/image-candidate-pool.md` and selected exactly five first-batch images. |
| Spec R1-R20 | Add a static beginner page with source-backed setup, safety, method, movement, muscle, and feel guidance. | Added `exercises/baduanjin-basics.md` and Baduanjin real-page tests. |
| Spec R21-R29 | Allow exactly five selected first-batch images for this page only. | Added a path-scoped five-image exception and tests that preserve the three-image default elsewhere. |
| Spec R30-R39 | Require prompt records, approved provenance rows, meaningful alt text, and safe image semantics. | Added five generated assets, five exact prompt records, five provenance rows, alt text, visual-safety proof, and real-page media tests. |
| Spec R40-R43 | Require manual visual-safety proof, beginner-comprehension proof, rollback proof, and no runtime or coaching behavior. | Added `visual-safety-review.md`, `beginner-comprehension-proof.md`, `rollback-proof.md`, scope tests, and final review evidence. |
| Architecture | Keep generated media repository-local and subordinate to Markdown. | Updated architecture and kept assets under `media/exercises/`, prompt records under `media/prompts/`, and provenance in `media/PROVENANCE.md`. |
| Plan | Implement in M1-M4 with tests/proof before promotion. | M1-M4 are closed by code review; final holistic code-review R1 passed. |

## Diff Rationale By Area

| Area | Files | Why they changed | Requirements and evidence |
|---|---|---|---|
| Governing contract | `specs/necessary-images-and-baduanjin-exercise.md`, `specs/necessary-images-and-baduanjin-exercise.test.md` | Captures the Baduanjin page contract, image exception, media governance, tests, proof obligations, non-goals, and validation commands. | Proposal, R1-R43, BJ-T1-BJ-T11, MP1-MP4. |
| Architecture | `docs/architecture/system/architecture.md` | Adds the Baduanjin five-image exception and repository-local media/prompt/provenance flow to the canonical architecture. | Architecture-review R1 and final holistic code-review R1. |
| Page content | `exercises/baduanjin-basics.md`, `SOURCES.md` | Adds the beginner page, aliases, sections, citations, movement breakdown, method labels, safety routing, and shared source IDs. | R1-R20, R42-R43, M2 source audit, real-page tests. |
| Image policy enforcement | `tools/checks/check_markdown_first.py` | Keeps the normal exercise-image limit at three while allowing five images only for `exercises/baduanjin-basics.md`; adds forbidden-scope wording checks needed by review. | R27, R4, R7-R9, R43, CR-M1-001 resolution. |
| Unit and integration tests | `tests/test_exercise_image_standard.py`, `tests/test_exercise_method_guidance.py`, `tests/test_markdown_first_real_pages.py` | Adds Baduanjin fixtures and real-page checks for image limits, prompt/provenance wiring, forbidden wording, method guidance, source support, proof records, and rollback evidence. | BJ-T1-BJ-T11, CMD1-CMD6. |
| Generated media | `media/exercises/baduanjin-basics/*.png` | Adds the five approved generated support images selected from the ranked candidate pool. | R22-R29, M3 visual-safety review. |
| Prompt records | `media/prompts/exercises/baduanjin-basics/*.md` | Preserves exact prompts, generator, date, reviewer, status, and selected-output notes for each generated raster. | R30-R32, R38-R40. |
| Provenance | `media/PROVENANCE.md` | Adds approved rows for the five Baduanjin assets with purpose, prompt record, license assertion, reviewer, status, and page refs. | R30, R33-R35. |
| Manual proof | `source-audit.md`, `visual-safety-review.md`, `beginner-comprehension-proof.md`, `rollback-proof.md` | Records source support, visual-safety review, beginner-comprehension outcomes, and a reproducible text-only rollback rehearsal. | MP1-MP4, R40-R42, CR-M4-001 resolution. |
| Exercise image inventory | `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | Keeps the current exercise-image audit inventory aligned with the new Baduanjin page and images. | Derived artifact currency checked by M2/M3/final reviews. |
| Workflow records | `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`, `docs/plan.md` | Records proposal/spec/architecture/plan/test-spec reviews, milestone reviews, review-resolution, validation notes, and current handoff state. | Standard workflow and final holistic code-review R1. |

## Tests Added Or Changed

| Test area | What it proves | Why this level is appropriate |
|---|---|---|
| Baduanjin image-standard fixtures | Five Baduanjin images pass only under the path-scoped exception; sixth image, second muscle-attention image, missing prompt record, prompt mismatch, invalid purpose, visual-scope wording, and unrelated four-image pages fail. | Checker-level fixtures prove policy before relying on real generated assets. |
| Baduanjin method fixtures | `low_load_control_drill` wording passes when static and general; adaptive, treatment, recovery-care, symptom, and medication-response wording fails. | Unit-level validation protects non-clinical and non-coaching scope. |
| Real Baduanjin page tests | The page exists with required shape, aliases, sections, sources, method guidance, muscle guidance, scope boundaries, and safety routing. | Integration tests validate the actual public Markdown page. |
| Real media tests | The page references exactly five local Baduanjin assets with meaningful alt text; each asset has one approved provenance row and matching prompt record. | Integration tests prevent page/media/provenance drift. |
| Proof-record tests | Beginner-comprehension and rollback proof files include the required prompts, paths, cleanup surfaces, commands, and pass results. | Token-level tests keep manual proof records present while semantic judgment remains manual. |

## Validation Evidence Before Final Verify

Latest final holistic code-review reruns:

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass: 84 tests |
| `python3 -m unittest discover -s tests` | pass: 184 tests |
| `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/ docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | pass: checked 27 Markdown files |
| `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/ docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | pass: checked 31 files |
| `git diff --check` | pass |

No hosted CI run has been observed for this branch.

## Review Resolution Summary

Two material findings were recorded and resolved:

| Finding | Disposition | Resolution |
|---|---|---|
| CR-M1-001 | closed by code-review R2 | Added direct Baduanjin forbidden-scope fixture coverage for treatment protocol, full traditional form / all eight brocades, fall-prevention program, and adaptive coaching wording. |
| CR-M4-001 | closed by code-review M4 R2 | Replaced the wildcard rollback command record with concrete temporary-root commands and reran focused rollback Markdown-first and privacy checks. |

Details are in `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-resolution.md`.

Final holistic code-review R1 passed with no material findings.

## Alternatives Rejected

- Generate all eight movements immediately: rejected because it would increase governance burden and imply a complete traditional form course.
- Add Baduanjin as text-only only: rejected because the sequence is image-dependent for beginners.
- Split content and image proposals: rejected because the central decision is that this page needs a governed first image batch.
- Use borrowed or stock images: rejected because the accepted media workflow requires governed generated assets, prompt records, provenance, and visual review.
- Make images source-of-truth instructions: rejected because Markdown must remain authoritative for setup, cues, muscles, safety, sources, and rollback.

## Scope Control

Preserved non-goals:

- No medical qigong treatment, disease claim, pain cure, posture fix, or replacement for medical care.
- No fall-prevention program, individualized balance program, recovery plan, symptom protocol, or adaptive coaching.
- No martial application, combat framing, lineage debate, or full eight-brocade curriculum.
- No video, animation, hosted app, database, user account, user-input flow, or generated public API.
- No in-image labels, Chinese characters, arrows, citations, safety warnings, pain marks, brand marks, identifiable faces, exact anatomy labels, weapons, targets, or clinical framing.

## Risks And Follow-Ups

- Beginner-comprehension proof is a static non-identifying reviewer simulation, not public-reader research.
- Static images cannot prove exact form quality or individual balance safety.
- External source freshness and link health should be maintained during normal review cycles.
- Final verification still needs to run after this explanation.
- PR readiness is not claimed until verify and PR handoff complete.

## Sources

- [Necessary Images and Baduanjin Exercise proposal](../../../docs/proposals/2026-07-06-necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
- [Final Holistic Code Review R1](reviews/code-review-final-r1.md)
- [Review Resolution](review-resolution.md)
