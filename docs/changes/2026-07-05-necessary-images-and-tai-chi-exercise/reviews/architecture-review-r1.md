# Architecture Review R1: Necessary Images and Tai Chi Exercise

## Result

- Review surface: canonical-architecture-update
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/architecture-review-r1.md`
- Review log: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Required canonical updates: none
- Required ADR updates: none
- Next stage: plan

## Findings

None.

## Review Dimensions

| Dimension | Verdict | Notes |
|---|---|---|
| Spec alignment | pass | The architecture maps `exercises/tai-chi-basics.md`, the top-10 candidate pool, first three assets, deferred candidates, provenance, prompt records, visual review, beginner proof, and rollback to the approved spec. |
| Package shape | pass | The change updates the canonical arc42 package in goals, constraints, building blocks, runtime flow, quality requirements, and risks. No new ADR is needed because existing accepted ADRs already govern generated-raster provenance, exercise image purposes, and prompt records. |
| Boundary clarity | pass | Content, media, prompt records, provenance, and review evidence remain separate repository-native blocks. |
| Data ownership | pass | Markdown owns instructions and citations; `media/PROVENANCE.md` owns raster provenance; prompt records own exact prompt text; change-local evidence owns visual and beginner review outcomes. |
| Interface safety | pass | Published Markdown path, asset paths, prompt-record paths, and provenance rows are treated as compatibility surfaces through the existing architecture. |
| Runtime and failure handling | pass | The Tai Chi flow includes generation gating, first-batch image count, deferred-candidate handling, provenance and prompt-record requirements, visual review, beginner proof, and text-only rollback. |
| Deployment and execution boundaries | pass | No hosted app, CMS, database, generated public package, or runtime service is introduced. |
| Security/privacy | pass | The architecture keeps generated media non-identifying and routes prompt/review evidence through existing privacy and no-private-health-information constraints. |
| Quality and operations | pass | Quality requirements include Tai Chi required media and keep images subordinate to Markdown. |
| Testing feasibility | pass | The architecture surfaces page structure, method label, image count, prompt record, provenance, visual review, beginner proof, and rollback cases for plan and test-spec coverage. |
| Complexity discipline | pass | The update applies existing media and prompt-record architecture to one new exercise page instead of creating a new media system. |
| ADR quality | pass | Existing ADRs are sufficient; no durable decision is newly introduced or revised. |
| Plan readiness | pass | No open architecture questions block execution planning. |

## Evidence

- `docs/architecture/system/architecture.md` now records the Tai Chi spec and spec review in related artifacts and adds Tai Chi to goals and constraints.
- The building-block view adds `Tai Chi Basics exercise media` with exactly three first-batch assets under `media/exercises/tai-chi-basics/`.
- The runtime view adds `Tai Chi Basics authoring and media flow`, including candidate-pool evidence, the three generated assets, prompt records, provenance, visual-safety review, beginner-comprehension proof, and rollback.
- Quality requirements now include `Tai Chi required media`, and risks name martial, therapy, fall-prevention, correctness, and fourth-image drift.

## Validation

- `python3 tools/checks/check_privacy.py docs/architecture/system/architecture.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/change.yaml specs/necessary-images-and-tai-chi-exercise.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/spec-review-r1.md` passed.
- `git diff --check -- docs/architecture/system/architecture.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/change.yaml specs/necessary-images-and-tai-chi-exercise.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/spec-review-r1.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-log.md` passed.
