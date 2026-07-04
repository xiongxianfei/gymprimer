# Explain Change: Exercise Muscle Guidance

## Summary

This change adds a durable exercise-muscle-guidance standard and implements the first reviewed proof slice. GymPrimer exercise pages can now adopt `## Muscles involved` with role- or phase-based guidance, pair it with `## What you should feel`, keep specific claims page-local and cited, and preserve untouched legacy `## Used muscles` pages until a planned migration slice touches them.

The implementation deliberately stops short of rewriting every exercise page. It adds the authoring contract, focused checker behavior, proof-slice page migrations, manual semantic proof, and a future rollout gate.

## Problem

The accepted proposal identified inconsistent muscle guidance across exercise pages. Some pages used `## Muscles involved`, older pages used `## Used muscles`, and guidance ranged from bare muscle lists to potentially overconfident activation language. Beginners needed practical role-based guidance: what broad region matters, what it helps do, what they may feel, what not to overuse, and when the cue is only a broad learning aid.

The project also needed to preserve GymPrimer's Markdown-first, citation-backed, non-clinical boundaries. That meant no anatomy atlas, no exact activation percentages, no diagnosis or treatment claims, no personalized cueing, and no one-shot migration of every exercise page.

## Decision Trail

| Decision point | Result | Durable source |
| --- | --- | --- |
| Proposal option | Chose role-based muscle guidance for exercise pages instead of keeping current sections, requiring only lists, or building an anatomy atlas. | `docs/proposals/2026-07-04-exercise-muscle-guidance-standard.md` |
| Proposal review | Approved the direction and routed it to a focused spec. | `docs/changes/exercise-muscle-guidance-standard/reviews/proposal-review-r1.md` |
| Feature requirements | Defined R1-R44 for section names, role/phase guidance, feel cues, wording boundaries, source support, image alignment, proof slice, rollout gating, validation, and manual proof. | `specs/exercise-muscle-guidance.md` |
| Architecture decision | Kept muscle guidance as visible Markdown; optional muscle-attention images stay support-only under the existing image standard; page-local source support remains required. | `docs/architecture/system/architecture.md` |
| Test strategy | Mapped deterministic checks to XMG-T1-XMG-T12 and manual proof to XMG-M1-XMG-M4. | `specs/exercise-muscle-guidance.test.md` |
| Execution plan | Split work into M1 contract/checker/template, M2 representative proof-slice pages, and M3 manual proof plus broad rollout gate. | `docs/plans/2026-07-04-exercise-muscle-guidance.md` |
| Code review | M1 R1 found missing XMG-T8 source-surface proof; M1 R2 accepted the resolution; M2 and M3 reviews were clean-with-notes. | `docs/changes/exercise-muscle-guidance-standard/review-log.md` |

## Diff Rationale By Area

| Area / files | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| Workflow artifacts under `docs/changes/exercise-muscle-guidance-standard/` | Added change metadata, review log, reviews, review-resolution, validation ledger, manual-proof files, and this explanation. | The standard workflow requires durable proposal/spec/architecture/plan/test/review/validation rationale before final verify and PR handoff. | `AGENTS.md`, `docs/plans/2026-07-04-exercise-muscle-guidance.md` | Code-review M1 R2, M2 R1, and M3 R1; M3 validation ledger. |
| `docs/proposals/2026-07-04-exercise-muscle-guidance-standard.md` | Recorded accepted product direction and scoped rollout. | The change affects content contract, source support, and safety boundaries, so it needed a proposal before implementation. | Proposal review R1 | Proposal accepted; no material proposal-review findings. |
| `specs/exercise-muscle-guidance.md` | Added normative requirements R1-R44 and acceptance criteria AC1-AC5. | Implementation needed explicit rules for headings, legacy compatibility, role vocabulary, feel-cue pairing, page-local source support, optional images, and proof evidence. | Proposal option C | Spec-review R1 approved. |
| `docs/architecture/system/architecture.md` | Added exercise muscle guidance to the Markdown source-of-truth architecture, authoring flow, source-support rules, validation observability, and acceptance scenarios. | The change touches template, checker, exercise content, media alignment, and manual proof boundaries; those are long-lived content-system decisions. | Architecture-review R1 | Architecture-review R1 approved. |
| `docs/plans/2026-07-04-exercise-muscle-guidance.md` and `docs/plan.md` | Added and maintained the active plan, milestones, validation notes, progress, and current handoff. | The work needed small implementation slices instead of broad repository churn. | Plan-review R1 | Current handoff now moves from explain-change to verify after this artifact. |
| `specs/exercise-muscle-guidance.test.md` | Added the proof map for unit, integration, manual, migration, image-alignment, and closeout validation. | The checker cannot prove semantic source truth, so the test spec separates deterministic validation from manual evidence. | Test-spec-review R1 | Test-spec-review R1 approved. |
| `docs/templates/exercise-card.md` | Replaced a simple muscle prompt with role-based guidance, broad-region-first wording, source-support reminder, and paired soft feel-cue instructions. | Supports R1, R16-R18, R29-R30, and R37 for future exercise authors. | Spec R1, R16-R18, R29-R30, R37 | `tests/test_markdown_first_templates.py`. |
| `tools/checks/check_markdown_first.py` | Added `validate_exercise_muscle_guidance()` and helper parsing for exact headings, adopted-page scope, role/phase table shape, role bullets, bare lists, source-surface citations, and deterministic forbidden wording. | Supports deterministic parts of R1-R3, R4-R8, R16, R18-R23, R28, R31, and R41-R42 without attempting semantic source truth. | Spec R41-R42; test spec XMG-T1-XMG-T8, XMG-T12 | `tests/test_exercise_muscle_guidance.py`; code-review M1 R2. |
| `tests/test_exercise_muscle_guidance.py` | Added focused unit coverage for adopted headings, legacy compatibility, role tables, bullets, phase tables, source-surface failures, forbidden wording, stable finding categories, and M3 proof artifacts. | Proves the checker contract and required manual-proof files from XMG-T1-XMG-T8, XMG-T11, and XMG-T12. | Test spec XMG-T1-XMG-T12, XMG-M1-XMG-M4 | `python3 -m unittest tests.test_exercise_muscle_guidance`. |
| `tests/test_markdown_first_real_pages.py` | Added proof-slice category coverage and legacy compatibility tests for real exercise pages. | Proves M2 selected one page per required category and did not force nonselected legacy pages to migrate. | Spec R3, R38-R40; test spec XMG-T6, XMG-T10 | M2 validation and code-review M2 R1. |
| `tests/test_markdown_first_templates.py` | Added assertions for role-based template prompt text and soft feel-cue language. | Keeps the template from drifting behind the approved exercise-page contract. | Spec R37; XMG-T1 | M1 validation and code-review M1 R2. |
| `exercises/rowing-machine.md` | Converted muscle guidance to a phase table for drive, transfer, finish, and recovery. | Cardio equipment benefits from phase-linked broad muscle roles. | Spec R8, R15, R38-R39 | M2 real-page tests; source audit. |
| `exercises/chest-press.md` | Added role-table guidance for main driver, support, and stabilizer regions plus aligned feel cues. | Covers the machine/resistance proof category and demonstrates driver/support/stabilizer wording. | Spec R5-R7, R11, R16-R18 | M2 real-page tests; source audit sample. |
| `exercises/plank.md` | Migrated from `## Used muscles` to `## Muscles involved` and added paired feel cues around trunk control. | Covers hold/trunk guidance and proves touched legacy pages migrate while untouched legacy pages remain compatible. | Spec R2-R3, R13, R16-R18 | M2 real-page tests. |
| `exercises/chin-nod.md` | Added soft role bullets for control focus and posture support. | Covers low-load control wording without posture-correction or exact activation claims. | Spec R12, R18-R20, R31 | M2 real-page tests; source audit sample. |
| `exercises/thoracic-extension.md` | Added mobility-focus and support bullets that distinguish movement from strengthening. | Covers mobility/stretch pages and avoids turning the drill into a hard contraction or correction promise. | Spec R14, R18-R20, R31 | M2 real-page tests; source audit sample. |
| `exercises/band-pull-apart.md` | Added role-table guidance for upper-back/rear-shoulder work, arm/grip support, and posture/control. | Covers the band or shoulder-control proof category. | Spec R5-R7, R11, R16-R18 | M2 real-page tests; source audit sample. |
| `manual-proof/source-audit.md` | Recorded sampled main-driver, support/stabilizer, feel, compensation, and safety source-support review. | Static parsing cannot prove source adequacy; R43 requires manual evidence. | Spec R24-R28, R43 | M3 tests and code-review M3 R1. |
| `manual-proof/beginner-comprehension.md` | Recorded non-identifying proof-slice comprehension outcomes. | R44 requires evidence that a beginner can identify the region, role, feel, overuse caution, stop condition, and source to verify. | Spec R44 | M3 tests and code-review M3 R1. |
| `manual-proof/muscle-image-alignment.md` | Recorded alignment for all proof-slice muscle-attention images and noted text-only proof pages. | Optional images must remain broad, unlabeled, support-only, and subordinate to Markdown. | Spec R32-R36, R43 | M3 tests and code-review M3 R1. |
| `manual-proof/broad-rollout-gate.md` | Classified remaining exercise pages for future batches. | Prevents a silent all-page migration and preserves small-loop rollout. | Spec R40 | M3 tests and code-review M3 R1. |

No unrelated file changes were identified in the reviewed diff.

## Tests Added Or Changed

| Test ID | Location | What it proves | Why this level is appropriate |
| --- | --- | --- | --- |
| XMG-T1 | `tests/test_markdown_first_templates.py` | The exercise template exposes role-based muscle guidance and soft feel-cue prompts. | Template drift is deterministic and cheap to test. |
| XMG-T2-XMG-T5 | `tests/test_exercise_muscle_guidance.py` | Adopted pages need `## Muscles involved`, `## What you should feel`, role/bullet or phase structure, and correct table columns. | Unit fixtures isolate checker behavior from real content wording. |
| XMG-T3 / XMG-T10 | `tests/test_exercise_muscle_guidance.py`, `tests/test_markdown_first_real_pages.py` | Untouched legacy `## Used muscles` pages remain compatible outside migration scope. | Prevents accidental broad migration enforcement. |
| XMG-T7 | `tests/test_exercise_muscle_guidance.py` | Exact activation, EMG-as-instruction, "must feel or wrong", diagnosis, treatment, correction, weak-muscle, and personalized cueing language fail where deterministic. | Wording boundaries are stable string-pattern checks. |
| XMG-T8 | `tests/test_exercise_muscle_guidance.py` | Missing citations and global-only or undefined source references fail for adopted role guidance; semantic adequacy remains manual. | This is the minimal structural check requested by code review without pretending to prove source truth. |
| XMG-T6 | `tests/test_markdown_first_real_pages.py` | The proof slice covers the six required exercise categories and each migrated page has valid muscle/feel guidance. | Real-page coverage verifies the actual reader-facing migration. |
| XMG-T11 / XMG-M1-XMG-M4 | `tests/test_exercise_muscle_guidance.py` | Manual proof files exist and include required claim samples, comprehension prompts, image checks, rollout categories, and validation commands. | Manual proof content cannot be semantically automated, but its required evidence surface can be checked. |
| XMG-T12 | `tests/test_exercise_muscle_guidance.py` | Findings include file paths and stable `exercise_muscle_*` categories. | Observability is part of the checker contract. |

## Validation Evidence Available Before Final Verify

Milestone validation and reviewer reruns are recorded in the plan, review records, and validation ledger. Local evidence includes:

- M1 and review-resolution: `python3 -m unittest tests.test_exercise_muscle_guidance`; `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages`; `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises`; `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-muscle-guidance-standard`; `git diff --check`.
- M2: `python3 -m unittest tests.test_exercise_muscle_guidance tests.test_markdown_first_real_pages`; `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`; `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`; `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises media docs/changes/exercise-muscle-guidance-standard`; `git diff --check`.
- M3: `python3 -m unittest tests.test_exercise_muscle_guidance`; `python3 tools/checks/check_privacy.py docs/changes/exercise-muscle-guidance-standard`; `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`; `git diff --check`.
- Code-review M3 R1 reviewer reruns: `python3 tools/checks/check_privacy.py docs/changes/exercise-muscle-guidance-standard`; `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`; `python3 -m unittest tests.test_exercise_muscle_guidance`; `git diff --check`.

Hosted CI has not been observed. Final verify has not run yet.

## Review Resolution Summary

One material finding was opened and closed:

| Finding ID | Disposition | Summary |
| --- | --- | --- |
| CR-XMG-M1-1 | resolved | M1 initially lacked deterministic XMG-T8 source-surface proof. The resolution added focused tests for missing/global-only source support on adopted muscle guidance and minimal checker behavior that requires citations and page-local reference definitions without requiring semantic source truth. |

Durable resolution record: `docs/changes/exercise-muscle-guidance-standard/review-resolution.md`.

M1 R2, M2 R1, and M3 R1 all recorded no open blockers. `review-log.md` has no open findings.

## Alternatives Rejected

- Keep current muscle sections as-is: rejected because it preserves inconsistent, sometimes vague guidance.
- Require only a simple muscle list: rejected because lists do not explain what regions do during movement.
- Build a separate anatomy atlas: deferred because it broadens the product surface and does not solve page-local beginner cueing.
- Rewrite every exercise page in this branch: rejected by proposal, spec, and plan because source support and comprehension evidence need small reviewed batches.
- Require a muscle-attention image on every page: rejected because text-only pages remain valid and images are support assets, not source-of-truth anatomy.
- Make the checker prove semantic source truth: rejected because static validation can check source surfaces, while claim adequacy remains manual review.

## Scope Control

This change preserves the approved non-goals:

- No exact activation percentages or EMG-as-routine beginner instruction.
- No diagnosis, treatment, rehabilitation, posture-correction promise, dysfunction claim, or personalized coaching.
- No new exercise inventory or anatomy atlas.
- No generated images, regenerated media, or changed image provenance in this implementation.
- No immediate migration of all legacy `## Used muscles` pages.
- No hosted app, runtime logic, user-input flow, database, generated JSON, or adaptive workout behavior.

## Risks And Follow-Ups

- Manual source audit is bounded sampling, not exhaustive proof for every future exercise page.
- Beginner comprehension proof is non-identifying proxy evidence, not a formal usability study.
- Existing pages outside the proof slice still need future batched review before migration.
- Future batches should rerun source-audit, comprehension, and image-alignment evidence for their touched pages.
- Final verify still needs to run the lifecycle closeout commands from `specs/exercise-muscle-guidance.test.md`, including broad unittest discovery and the full privacy surface.

## Readiness Statement

All implementation milestones are closed by code review, and the material M1 finding is resolved. This explanation is the pre-verify rationale artifact. The next lifecycle stage is `verify`; this artifact does not claim final verification, branch readiness, PR readiness, or hosted CI success.
