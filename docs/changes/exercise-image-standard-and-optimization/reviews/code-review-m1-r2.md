# Code Review M1 R2: Exercise Image Standard

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m1-r2.md`, `docs/changes/exercise-image-standard-and-optimization/review-log.md`, `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`, `docs/changes/exercise-image-standard-and-optimization/change.yaml`, `docs/plans/2026-07-03-exercise-image-standard.md`, `docs/plan.md`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m1-r2.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Reviewed milestone: M1
- Milestone closeout: closed
- Remaining implementation milestones: M2, M3, M4, lifecycle closeout
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: M1 implementation commit `6bfacf3` plus validation-path amendment commits through `66a4203`, with focus on `tools/checks/check_markdown_first.py`, `tests/test_exercise_image_standard.py`, `specs/exercise-image-standard.test.md`, and M1 lifecycle artifacts.
- Tracked governing branch state: proposal, approved spec, approved architecture/ADR, active plan, approved test-spec amendment, and review-resolution state are present in tracked branch state.
- Governing artifacts: `specs/exercise-image-standard.md`, `specs/exercise-image-standard.test.md`, `docs/adr/2026-07-03-exercise-document-image-purposes.md`, `docs/architecture/system/architecture.md`, and `docs/plans/2026-07-03-exercise-image-standard.md`.
- Prior review evidence: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m1-r1.md` and `docs/changes/exercise-image-standard-and-optimization/reviews/test-spec-review-r4.md`.
- Validation evidence inspected: M1 validation notes in `docs/plans/2026-07-03-exercise-image-standard.md` and `docs/changes/exercise-image-standard-and-optimization/change.yaml`; reviewer reran M1-owned commands during this re-review.

## Diff summary

M1 adds exercise-specific media-purpose validation, generated-raster provenance checks, image count and muscle-attention limits, generic and unsafe alt-text rejection, legacy exercise image purpose compatibility, and template-aware checker support. The later validation-path amendment moves broad EIS-CMD4 privacy validation from M1 closeout to lifecycle closeout / verify before PR handoff, while keeping scoped current-change privacy checks available for milestone review hygiene.

## Findings

No blocking or required-change findings.

## Prior Finding Disposition

| Finding | Verdict | Evidence |
| --- | --- | --- |
| CR-EIS-M1-1 | resolved | Test-spec-review R4 approved the validation-path amendment that makes broad EIS-CMD4 privacy validation a lifecycle closeout / verify gate rather than an M1 gate. The plan and test spec now agree on EIS-CMD4 ownership, and the scoped current-change privacy scan passed during re-review. |

## Checklist coverage

- Spec alignment: pass. The checker implements the M1-scope requirements for optional exercise images, setup/movement/muscle-attention purposes, one muscle-attention image, generated-raster provenance, non-generic alt text, legacy-compatible purposes, and no runtime/product expansion.
- Test coverage: pass. `tests/test_exercise_image_standard.py` covers text-only pages, allowed and disallowed purposes, provenance failures, count limits, muscle-attention limits, path and alt-text boundaries, unsafe wording, legacy compatibility, and template context. Existing guardrail and Responsible Breadth tests also remain green.
- Edge cases: pass. Named edge cases for duplicate provenance rows and valid three-image pages were directly probed in R1; this re-review reran the focused suite and the approved M1 command set.
- Error handling: pass. The checker emits stable categories for remote media, outside-media paths, unsupported extensions, missing assets, missing/incomplete/unapproved provenance, page-reference mismatch, out-of-scope purpose, AI reviewer, image count, muscle-attention limit, generic alt text, and deterministic unsafe wording.
- Architecture boundaries: pass. The implementation extends static Markdown/media validation and the centralized `media/PROVENANCE.md` contract without adding runtime services, CMS, user input, generated JSON, video, or coaching behavior.
- Compatibility: pass. Existing exercise image references, assets, and provenance purpose values are unchanged; legacy `equipment_identification` and `key_movement_illustration` purposes remain valid.
- Security/privacy: pass. M1 no longer owns broad EIS-CMD4 after test-spec-review R4. The scoped current-change privacy command passed for the active exercise-image change surface.
- Derived artifact currency: pass. No generated public artifact is introduced by M1; lifecycle artifacts are updated to reflect the reviewed state.
- Unrelated changes: pass. The reviewed implementation and follow-up validation amendment belong to the same exercise-image standard change and do not include unrelated product/runtime/content edits.
- Validation evidence: pass. Re-review ran the focused M1 tests, combined guardrail suite, real-page checker, template checker, full unittest discovery, scoped current-change privacy scan, and whitespace check.

## No-finding rationale

The only R1 blocker was validation ownership: the broad privacy command failed because it scanned pre-existing superseded-plan examples while the approved proof map treated it as an M1 gate. Owner direction moved that broad sweep to verify before PR, and test-spec-review R4 approved the amended proof map. Under the current approved test spec, M1-owned validation is focused on checker behavior, template support, real-page media validation, scoped privacy hygiene, and whitespace. Those checks passed during this re-review, and no new implementation gap was found.

## Direct-proof gaps

None blocking for M1. Visual-safety review, beginner comprehension evidence, and generated-image batch checks remain intentionally deferred to later milestones.

## Validation run during re-review

- `python3 -m unittest tests.test_exercise_image_standard` passed with 7 tests.
- `python3 -m unittest tests.test_markdown_first_guardrails tests.test_responsible_breadth_m1 tests.test_exercise_image_standard` passed with 51 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md` passed, checking 25 Markdown files.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates media/PROVENANCE.md` passed, checking 10 Markdown files.
- `python3 -m unittest discover tests` passed with 95 tests.
- `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/exercise-image-standard-and-optimization docs/plans/2026-07-03-exercise-image-standard.md media exercises tools tests` passed, checking 116 files.
- `git diff --check` passed.

## Milestone handoff state

- Reviewed milestone: M1
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining in-scope implementation milestones: M2, M3, M4, lifecycle closeout
- Next stage: implement M2
- Final closeout readiness: not ready because M2-M4, explain-change, final verification, and PR handoff remain open.
