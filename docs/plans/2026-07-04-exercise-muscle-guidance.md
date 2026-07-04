# Plan: Exercise Muscle Guidance

## Status

- Status: reviewed
- Plan lifecycle state: active
- Terminal disposition: not terminal

## Purpose / big picture

Implement the approved exercise-muscle-guidance contract without turning GymPrimer into an anatomy atlas, clinical cueing product, or personalized coaching system. The work standardizes new and migrated exercise pages on `## Muscles involved`, pairs it with `## What you should feel`, adds role-based muscle guidance, keeps source support page-local, and proves the format on a small representative slice before broader migration.

This plan sequences implementation only. It does not reopen the accepted role-based direction, add new exercises, require images on every page, rewrite every exercise page at once, or make generated visuals a source of truth.

## Source artifacts

- Proposal: `../proposals/2026-07-04-exercise-muscle-guidance-standard.md`
- Proposal review: `../changes/exercise-muscle-guidance-standard/reviews/proposal-review-r1.md`
- Spec: `../../specs/exercise-muscle-guidance.md`
- Spec review: `../changes/exercise-muscle-guidance-standard/reviews/spec-review-r1.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review: `../changes/exercise-muscle-guidance-standard/reviews/architecture-review-r1.md`
- Governing specs:
  - `../../specs/markdown-first-primer.md`
  - `../../specs/exercise-image-standard.md`
  - `../../specs/exercise-method-guidance.md`
  - `../../specs/rowing-machine-basics-and-beginner-workouts.md`
- Test spec: `../../specs/exercise-muscle-guidance.test.md`
- Test-spec review: `../changes/exercise-muscle-guidance-standard/reviews/test-spec-review-r1.md`

## Context and orientation

Exercise pages live under `exercises/`. Newer pages already use `## Muscles involved` and `## What you should feel`; several legacy pages still use `## Used muscles`. The exercise template is `docs/templates/exercise-card.md`. Markdown validation is centered in `tools/checks/check_markdown_first.py` with Python `unittest` coverage under `tests/`. Generated raster muscle-attention images are already governed by `specs/exercise-image-standard.md` and `media/PROVENANCE.md`.

The approved contract is visible Markdown only. Muscle names, roles, feel cues, caveats, safety notes, and citations stay in the exercise page. Optional muscle-attention images may support broad-region awareness, but they do not carry labels, exact anatomy, or source-of-truth claims.

The first proof slice should choose representative pages from the spec's allowed set:

- cardio equipment: `exercises/rowing-machine.md`
- machine or resistance: `exercises/chest-press.md` or `exercises/seated-row.md`
- hold or trunk: `exercises/plank.md` or `exercises/dead-bug.md`
- low-load control: `exercises/wall-slide.md` or `exercises/chin-nod.md`
- mobility or stretch: `exercises/thoracic-extension.md` or `exercises/kneeling-hip-flexor-stretch.md`
- band or shoulder control: `exercises/band-pull-apart.md`

## Non-goals

- Do not add exact muscle activation percentages.
- Do not turn EMG findings into routine beginner instruction.
- Do not diagnose, treat, prescribe rehabilitation, promise posture correction, or infer reader dysfunction.
- Do not add individualized cueing, symptom-based substitutions, adaptive coaching, or personal workout logic.
- Do not require every exercise page to use a muscle-attention image.
- Do not add an anatomy atlas or new exercise inventory.
- Do not rewrite every exercise page in the first implementation slice.
- Do not change generated image provenance rules beyond what the exercise-image spec already owns.

## Requirements covered

- R1-R3: M1 and M2 cover `## Muscles involved` adoption and legacy `## Used muscles` compatibility.
- R4-R15: M2 applies role-based and phase-linked muscle guidance across the proof slice.
- R16-R20: M1 and M2 cover `## What you should feel`, feel-cue alignment, and compensation wording.
- R21-R31: M1-M3 cover exact activation, EMG, source-support, technical-name, and clinical-boundary rules.
- R32-R36: M1 and M3 cover optional muscle-attention image alignment through existing image-standard rules and manual review.
- R37: M1 updates the exercise template.
- R38-R40: M2 and M3 cover proof-slice selection and broad rollout gating.
- R41-R42: M1 adds deterministic validation surfaces and stable failure categories where practical.
- R43-R44: M3 records manual source-audit and beginner-comprehension proof.
- AC1-AC5: Plan review, test-spec review, implementation milestones, code review, explain-change, and verify provide acceptance evidence.

## Current Handoff Summary

- Current milestone: M3
- Current milestone state: review-requested
- Last reviewed milestone: M2
- Review status: proposal-review R1 approved; spec-review R1 approved; architecture-review R1 approved; plan-review R1 approved; test-spec-review R1 approved; code-review M1 R1 changes-requested; code-review M1 R2 clean-with-notes; code-review M2 R1 clean-with-notes
- Remaining in-scope implementation milestones: M3
- Next stage: code-review M3
- Final closeout readiness: not ready
- Reason final closeout is or is not ready: M1 and M2 are closed and M3 is awaiting code-review, but final verification and PR handoff have not started.

## Milestones

### M1. Muscle Guidance Contract Validation and Template

- Milestone state: closed
- Goal: make the exercise muscle guidance contract authorable and checkable before proof-slice content changes.
- Requirements: R1-R3, R16-R20, R21-R31, R32-R37, R41-R42, AC1, AC4-AC5.
- Files/components likely touched:
  - `docs/templates/exercise-card.md`
  - `tools/checks/check_markdown_first.py`
  - `tests/test_markdown_first_templates.py`
  - focused tests such as `tests/test_exercise_muscle_guidance.py`
  - `tests/test_markdown_first_real_pages.py`
- Dependencies:
  - plan-review and test-spec-review must approve the proof map before implementation.
- Tests to add/update:
  - template includes role-based `## Muscles involved` guidance and pairing with `## What you should feel`;
  - adopted/new exercise fixtures require `## Muscles involved`;
  - migrated fixtures fail if they retain `## Used muscles`;
  - untouched legacy fixtures remain compatible;
  - deterministic forbidden wording fails where practical;
  - existing muscle-attention image count and alt-text checks remain aligned with the image spec.
- Implementation steps:
  - Update the exercise template prompt for role-based muscle guidance.
  - Add or extend checker behavior for new/adopted exercise pages without forcing all legacy pages to migrate.
  - Add stable failure categories for missing muscle heading, migrated legacy heading, missing feel section, and deterministic forbidden wording.
  - Keep image-specific checks delegated to the existing exercise-image standard where possible.
- Validation commands:
  - `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages`
  - `python3 -m unittest tests.test_exercise_muscle_guidance`
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises`
  - `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-muscle-guidance-standard`
- Expected observable result: contributors have a template and deterministic validation path for role-based muscle guidance without breaking untouched legacy exercise pages.
- Commit message: `M1: add exercise muscle guidance contract checks`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - A broad checker rule could accidentally fail untouched `## Used muscles` pages before migration.
- Rollback/recovery:
  - Scope validation to new/adopted fixtures and proof-slice pages; keep legacy compatibility until the page is explicitly migrated.

### M2. Representative Proof-Slice Exercise Pages

- Milestone state: closed
- Goal: apply the muscle guidance contract to a representative set of exercise pages without broad all-page migration.
- Requirements: R1-R31, R38-R40, AC2-AC5.
- Files/components likely touched:
  - `exercises/rowing-machine.md`
  - one of `exercises/chest-press.md` or `exercises/seated-row.md`
  - one of `exercises/plank.md` or `exercises/dead-bug.md`
  - one of `exercises/wall-slide.md` or `exercises/chin-nod.md`
  - one of `exercises/thoracic-extension.md` or `exercises/kneeling-hip-flexor-stretch.md`
  - `exercises/band-pull-apart.md`
  - `SOURCES.md` only when sources are reused across pages
- Dependencies:
  - M1 should be closed.
- Tests to add/update:
  - real-page tests assert proof-slice pages use `## Muscles involved` and `## What you should feel`;
  - tests check proof-slice category coverage;
  - checker tests prove legacy pages outside the slice remain compatible.
- Implementation steps:
  - Select exact proof-slice pages from the approved representative set.
  - Rewrite each selected `## Muscles involved` section around roles or phases.
  - Align `## What you should feel` with the muscle roles using soft beginner language.
  - Add or adjust page-local citations for specific muscle, feel, compensation, setup, movement, and safety claims.
  - Keep optional images unchanged unless existing image-adjacent wording needs alignment.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`
  - `python3 -m unittest tests.test_exercise_muscle_guidance tests.test_markdown_first_real_pages`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises media docs/changes/exercise-muscle-guidance-standard`
- Expected observable result: the proof-slice pages explain broad muscle roles, feel cues, and overuse cautions in source-backed beginner language.
- Commit message: `M2: add muscle guidance proof slice`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Muscle claims may be under-sourced or become too anatomical.
- Rollback/recovery:
  - Soften unsupported claims to broad roles, remove exact activation wording, or narrow the proof slice before code review.

### M3. Manual Proof and Broad Rollout Gate

- Milestone state: review-requested
- Goal: record semantic source-support proof, beginner comprehension outcomes, optional image alignment evidence, and a broad-rollout gate before future batches.
- Requirements: R24-R28, R32-R36, R38-R44, AC3-AC5.
- Files/components likely touched:
  - `docs/changes/exercise-muscle-guidance-standard/manual-proof/source-audit.md`
  - `docs/changes/exercise-muscle-guidance-standard/manual-proof/beginner-comprehension.md`
  - `docs/changes/exercise-muscle-guidance-standard/manual-proof/muscle-image-alignment.md`
  - `docs/changes/exercise-muscle-guidance-standard/manual-proof/broad-rollout-gate.md`
  - `docs/changes/exercise-muscle-guidance-standard/validation-ledger.md`
- Dependencies:
  - M2 should be closed or ready for final review.
- Tests to add/update:
  - evidence files exist and include required proof criteria;
  - broad-rollout gate records remaining pages and batching decision categories.
- Implementation steps:
  - Sample one main-driver claim, one support/stabilizer claim, one feel cue, one compensation cue, and one safety cue per proof category or representative page.
  - Record source-support disposition and residual risk.
  - Record non-identifying beginner comprehension answers for region, role, feel, overuse avoidance, stop condition, and source verification.
  - Record image-to-Markdown alignment for any proof-slice muscle-attention image.
  - Create a broad-rollout gate that lists remaining exercise pages and classifies each as keep, rename only, rewrite roles, revise feel cues, or future image candidate.
- Validation commands:
  - `python3 tools/checks/check_privacy.py docs/changes/exercise-muscle-guidance-standard`
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`
  - `python3 -m unittest tests.test_exercise_muscle_guidance`
  - `git diff --check`
- Expected observable result: semantic evidence supports the proof slice and future all-exercise migration is gated by a recorded batch plan.
- Commit message: `M3: record muscle guidance proof evidence`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Manual proof may show that a page's muscle guidance is not source-supported enough.
- Rollback/recovery:
  - Revise or remove unsupported page wording and rerun the source audit before requesting code review.

## Validation plan

- `python3 -m unittest tests.test_exercise_muscle_guidance`: focused checker and proof-slice contract tests.
- `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages`: template and real-page integration coverage.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`: broader Markdown-first regression coverage.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises media/PROVENANCE.md`: content, source, template, media, and checker integration.
- `python3 tools/checks/check_privacy.py docs/templates specs tools tests SOURCES.md RED-FLAGS.md exercises media docs/changes/exercise-muscle-guidance-standard`: privacy scan over touched surfaces.
- `git diff --check`: whitespace and patch hygiene.
- Manual source audit: semantic source support for sampled muscle, feel, compensation, safety, and optional image-alignment claims.
- Beginner comprehension proof: non-identifying read-test evidence for the proof slice.

## Risks and recovery

- Risk: role tables make pages too long or anatomical.
  - Recovery: use short role bullets, common-language regions first, and technical names only where source-supported.
- Risk: source support is too weak for a specific muscle claim.
  - Recovery: soften the wording, add a direct page-local source, or remove the claim.
- Risk: internal muscle focus crowds out task/form cues.
  - Recovery: keep `## What you should feel` paired with movement cues and avoid making every cue a muscle cue.
- Risk: checker enforcement migrates legacy pages too early.
  - Recovery: keep validation scoped to new/adopted/proof-slice pages and touched-page migration.
- Risk: muscle-attention images imply precise anatomy.
  - Recovery: remove or replace the image, keep Markdown authoritative, and update provenance/evidence only after review.

## Dependencies

- Proposal and proposal review are accepted and recorded.
- Spec and spec review are approved and recorded.
- Canonical architecture amendment and architecture review are approved and recorded.
- Plan review must approve this plan before test-spec authoring proceeds.
- Test spec and test-spec review must be complete before implementation begins.
- Exercise-image standard remains the owner for muscle-attention image media rules.

## Progress

- 2026-07-04: Created plan after accepted proposal, approved spec, and approved architecture amendment.
- 2026-07-04: Plan-review R1 approved the plan and routed to test-spec.
- 2026-07-04: Test-spec-review R1 approved `specs/exercise-muscle-guidance.test.md` and allowed implementation handoff for M1.
- 2026-07-04: Implemented M1 template prompts, focused exercise muscle guidance checker coverage, and unit tests. M1 is ready for code-review.
- 2026-07-04: Code-review M1 R1 requested changes for CR-XMG-M1-1, missing deterministic XMG-T8 source-surface proof.
- 2026-07-04: Resolved CR-XMG-M1-1 with focused XMG-T8 source-surface tests and minimal checker behavior; M1 is ready for code-review rerun.
- 2026-07-04: Code-review M1 R2 accepted the resolution and closed M1. M2 proof-slice implementation is next.
- 2026-07-04: Started M2 implementation for the selected proof slice: rowing machine, chest press, plank, chin nod, thoracic extension, and band pull-apart.
- 2026-07-04: Added M2 real-page tests for proof-slice category coverage, role or phase muscle guidance, soft feel cues, page-local source-surface citations, and untouched legacy compatibility outside the selected slice.
- 2026-07-04: Migrated the selected proof-slice pages to role- or phase-based `## Muscles involved` guidance paired with `## What you should feel`.
- 2026-07-04: M2 validation passed locally; M2 is ready for code-review.
- 2026-07-04: Code-review M2 R1 accepted the proof-slice implementation with no material findings. M2 is closed and M3 manual proof is next.
- 2026-07-04: Started M3 implementation for manual source audit, beginner comprehension proof, muscle-image alignment proof, broad rollout gate, and validation ledger.
- 2026-07-04: Added M3 tests for required manual proof files, source-audit claim types, beginner-comprehension prompts, muscle-attention image alignment records, remaining-page rollout classifications, and validation-ledger commands.
- 2026-07-04: Recorded M3 manual proof artifacts under `docs/changes/exercise-muscle-guidance-standard/manual-proof/` and `validation-ledger.md`.
- 2026-07-04: M3 validation passed locally; M3 is ready for code-review.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-04 | Split implementation into contract, proof-slice content, and manual-proof milestones. | Keeps validation, content, and semantic proof reviewable without broad all-page churn. | One milestone that rewrites every exercise page. |
| 2026-07-04 | Keep all-exercise migration behind a broad-rollout gate. | Existing `## Used muscles` pages remain legacy-compatible until touched, and source review needs batching. | Immediate repository-wide migration. |
| 2026-07-04 | Reuse the exercise-image standard for muscle-attention images. | Avoids duplicating provenance, alt-text, and visual-safety rules. | New image governance inside this plan. |
| 2026-07-04 | Scope M1 checker enforcement to adopted visible muscle guidance while preserving untouched legacy pages. | M1 proves authoring and deterministic validation without converting existing exercise pages before the proof-slice milestone. | Fail every current `## Used muscles` page or rewrite real pages in M1. |
| 2026-07-04 | Select rowing machine, chest press, plank, chin nod, thoracic extension, and band pull-apart for M2. | This covers the six required proof-slice categories while limiting migration to one page per category. | Rewrite every exercise page; select two pages from one category before all required categories are represented. |

## M2 validation notes

- 2026-07-04 M2 expected failing test before content migration: `python3 -m unittest tests.test_markdown_first_real_pages` failed with six proof-slice category failures for missing role or phase structure and the legacy plank heading.
- 2026-07-04 M2 focused validation passed: `python3 -m unittest tests.test_exercise_muscle_guidance tests.test_markdown_first_real_pages`.
- 2026-07-04 M2 content validation passed: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`.
- 2026-07-04 M2 regression validation passed: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`.
- 2026-07-04 M2 privacy validation passed: `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises media docs/changes/exercise-muscle-guidance-standard`.
- 2026-07-04 M2 diff hygiene passed: `git diff --check`.
- 2026-07-04 code-review M2 R1 reviewer validation passed: `python3 -m unittest tests.test_exercise_muscle_guidance tests.test_markdown_first_real_pages`; `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`; `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`; `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises media docs/changes/exercise-muscle-guidance-standard`; `git diff --check`.

## M2 aligned-surface audit

- M2 updated only the selected proof-slice pages, `tests/test_markdown_first_real_pages.py`, the active plan, change metadata, and the durable change explanation.
- `SOURCES.md` is unaffected because the proof-slice pages already had page-local source definitions for the reused citations.
- Media files, prompt records, and provenance are unaffected because M2 did not add, remove, regenerate, or relabel muscle-attention images.

## M3 validation notes

- 2026-07-04 M3 expected failing test before evidence creation: `python3 -m unittest tests.test_exercise_muscle_guidance` failed with five missing-file failures for `source-audit.md`, `beginner-comprehension.md`, `muscle-image-alignment.md`, `broad-rollout-gate.md`, and `validation-ledger.md`.
- 2026-07-04 M3 focused validation passed: `python3 -m unittest tests.test_exercise_muscle_guidance`.
- 2026-07-04 M3 privacy validation passed: `python3 tools/checks/check_privacy.py docs/changes/exercise-muscle-guidance-standard`.
- 2026-07-04 M3 content validation passed: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md`.
- 2026-07-04 M3 diff hygiene passed: `git diff --check`.

## M3 aligned-surface audit

- M3 adds manual proof records for source audit, beginner comprehension, muscle-image alignment, broad rollout gating, and validation evidence.
- Exercise pages, media files, media prompt records, and `SOURCES.md` are unaffected; M3 found no required page or media edits during the bounded proof.
- Broad rollout remains gated for future batches. M3 does not authorize all-page migration or checker escalation.

## Surprises and discoveries

- Initial checker wording was too broad and flagged existing benign phrases such as "Treat this as..." plus non-role paragraph guidance on current pages. M1 narrowed deterministic enforcement to stable adopted-page categories so `docs/templates` and current `exercises/` pass without a proof-slice rewrite.

## Validation notes

- 2026-07-04: Test-spec hygiene checks run during workflow routing: `python3 tools/checks/check_privacy.py specs/exercise-muscle-guidance.test.md docs/changes/exercise-muscle-guidance-standard` passed; `git diff --check` passed; placeholder-marker scan over the test spec and change metadata returned no matches.
- 2026-07-04 M1: `python3 -m unittest tests.test_exercise_muscle_guidance` passed.
- 2026-07-04 M1: `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` passed.
- 2026-07-04 M1: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises` passed with `checked 24 Markdown file(s): pass`.
- 2026-07-04 M1: `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-muscle-guidance-standard` passed with `checked 93 file(s): privacy pass`.
- 2026-07-04 M1: `git diff --check` passed.
- 2026-07-04 M1 code-review: Direct reviewer probe showed adopted muscle guidance with a broad role claim and no citation/source marker returned no muscle-guidance findings. CR-XMG-M1-1 records the required resolution.
- 2026-07-04 M1 review-resolution: `python3 -m unittest tests.test_exercise_muscle_guidance` passed.
- 2026-07-04 M1 review-resolution: `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` passed.
- 2026-07-04 M1 review-resolution: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises` passed with `checked 24 Markdown file(s): pass`.
- 2026-07-04 M1 review-resolution: `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-muscle-guidance-standard` passed with `checked 95 file(s): privacy pass`.
- 2026-07-04 M1 review-resolution: `git diff --check` passed.
- 2026-07-04 M1 code-review R2: Direct reviewer probe returned `exercise_muscle_source_missing` for missing citation, `exercise_muscle_source_missing_definition` for undefined source ID, and no findings for a page-local source definition.

## Outcome and retrospective

- M3 implementation is pending code-review. Final outcome remains pending downstream verification.

## Readiness

- See `Current Handoff Summary`.
- Ready for M3 code-review. Final closeout is not allowed until all implementation milestones, code review, and verification are complete.
