# Code Review M1 R1: Exercise Image Standard

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m1-r1.md`, `docs/changes/exercise-image-standard-and-optimization/review-log.md`, `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`, `docs/changes/exercise-image-standard-and-optimization/change.yaml`, `docs/plans/2026-07-03-exercise-image-standard.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-EIS-M1-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m1-r1.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Reviewed milestone: M1
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M1 resolution, M2, M3, M4, lifecycle closeout
- Required review-resolution: yes
- Finding IDs: CR-EIS-M1-1
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: commit `6bfacf3` (`M1: implement exercise image validation contract`), especially `tools/checks/check_markdown_first.py`, `tests/test_exercise_image_standard.py`, and M1 lifecycle artifacts.
- Tracked governing branch state: proposal, approved spec, approved test spec, approved architecture/ADR, active plan, and prior review records are present in tracked branch state as of `6bfacf3`.
- Governing artifacts: `specs/exercise-image-standard.md`, `specs/exercise-image-standard.test.md`, `docs/adr/2026-07-03-exercise-document-image-purposes.md`, `docs/architecture/system/architecture.md`, and `docs/plans/2026-07-03-exercise-image-standard.md`.
- Validation evidence inspected: M1 validation notes in `docs/changes/exercise-image-standard-and-optimization/change.yaml` and `docs/plans/2026-07-03-exercise-image-standard.md`; reviewer reran focused tests and EIS-CMD5 and ran targeted duplicate-provenance and three-image probes.

## Diff summary

M1 adds the accepted exercise image purposes to `tools/checks/check_markdown_first.py`, keeps legacy exercise media purposes valid, adds exercise image count and muscle-attention limits, rejects generic alt text, adds deterministic unsafe exercise-image text checks, rejects AI-tool reviewer values for expanded exercise pages, and adds a template path boundary for `docs/templates/`. It adds focused temporary-repository tests in `tests/test_exercise_image_standard.py` for text-only pages, allowed and disallowed purposes, provenance failures, image count and muscle-attention limits, path and alt-text boundaries, legacy compatibility, and template validation. It also records the proposal/spec/architecture/plan/test-spec lifecycle artifacts and routes M1 to code-review.

## Findings

### Finding CR-EIS-M1-1

- Finding ID: CR-EIS-M1-1
- Severity: major
- Location: `specs/exercise-image-standard.test.md` EIS-CMD4; `docs/plans/2026-07-03-exercise-image-standard.md` M1 validation; `docs/changes/exercise-image-standard-and-optimization/change.yaml` validation
- Evidence: EIS-CMD4 is the required M1 privacy command and says any forbidden findings fail the active milestone. The implementation evidence records that `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/exercise-image-standard-and-optimization docs/plans media exercises tools tests` failed. The reviewer rerun observed the same failure on pre-existing forbidden-pattern command examples in `docs/plans/2026-06-26-content-schema-foundation.md`. The scoped current-change privacy command passed, but that is not the approved EIS-CMD4 command.
- Required outcome: M1 closeout evidence must include a passing approved privacy validation path, or the governing test spec/plan must be revised and re-reviewed to make the scoped command the approved M1 validation path.
- Safe resolution path: Either make the approved EIS-CMD4 command pass without weakening privacy policy, or route a focused test-spec/plan revision through the required review gates to replace EIS-CMD4 with the scoped current-change command. Then rerun M1 validation and request code-review re-review.
- needs-decision rationale: none

## Checklist coverage

- Spec alignment: pass. The checker implements M1-scope requirements for optional images, new exercise purposes, one muscle-attention image, generated-raster provenance, alt-text placeholders, legacy purpose compatibility, and no runtime/product expansion.
- Test coverage: concern. The focused tests cover the main M1 behavior, and reviewer probes directly confirmed duplicate provenance rows fail and a valid three-image exercise page passes. The validation-command failure remains open.
- Edge cases: pass. Temporary fixtures and existing guardrail tests cover text-only pages, disallowed purposes, missing/incomplete/unapproved provenance, page-reference mismatch, AI-tool reviewer values, four-image failure, two muscle-attention failure, wrong media bucket, generic alt text, deterministic unsafe wording, legacy purposes, template placeholder language, and remote template media.
- Error handling: pass. The checker preserves stable failure categories for media path, remote media, extension, missing asset, provenance, page refs, purpose, image-count, muscle-attention, generic alt text, AI reviewer, and deterministic unsafe wording.
- Architecture boundaries: pass. The implementation extends static Markdown/media validation and the centralized `media/PROVENANCE.md` contract without adding runtime services, CMS, user input, generated JSON, video, or coaching behavior.
- Compatibility: pass. No existing exercise image references, assets, or provenance purpose values changed; real existing exercise images still use the legacy-compatible purposes under `media/exercises/<slug>/`.
- Security/privacy: concern. The scoped current-change privacy scan passed, but the approved broad EIS-CMD4 command failed and must be resolved before M1 can close.
- Derived artifact currency: pass. No generated public artifacts are introduced by M1; lifecycle artifacts are present and routed to review-resolution after this review.
- Unrelated changes: pass. The commit includes upstream lifecycle artifacts and the M1 checker/test implementation for the same active change; no unrelated product, runtime, content, or media edits were found.
- Validation evidence: block. Required EIS-CMD4 evidence is failing. Focused tests, repository unittest discovery, checker commands, EIS-CMD5, scoped privacy, and diff whitespace checks otherwise provide credible evidence for the implemented behavior.

## No-finding rationale

Not applicable; this review has one material finding.

## Direct-proof gaps

- Required EIS-CMD4 privacy validation has failed evidence and must be resolved.
- No direct-proof gap remains for duplicate provenance rows or a valid three-image exercise page; reviewer probes confirmed duplicate rows fail with `media_provenance_incomplete` and three valid exercise images pass.

## Milestone handoff state

- Reviewed milestone: M1
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M1 resolution, M2, M3, M4, lifecycle closeout
- Next stage: review-resolution
- Final closeout readiness: not ready because M1 has an unresolved material finding and M2-M4 remain open.
