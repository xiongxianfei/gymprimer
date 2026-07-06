# Code Review M3 R1: Necessary Images and Tai Chi Exercise

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/code-review-m3-r1.md`, `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-log.md`, `docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md`, `docs/plan.md`, `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/change.yaml`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/code-review-m3-r1.md`
- Review log: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M3
- Milestone closeout: closed
- Remaining implementation milestones: M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `9eb1651` (`M3: add governed Tai Chi support images`).
- Tracked governing branch state: accepted proposal, approved spec, approved architecture, reviewed plan, active test spec, M1-M2 code-review receipts, and M3 implementation commit are tracked on `proposal/necessary-images-and-tai-chi-exercise`.
- Governing artifacts: `specs/necessary-images-and-tai-chi-exercise.md`, `specs/necessary-images-and-tai-chi-exercise.test.md`, `docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md`, `docs/architecture/system/architecture.md`, and `CONSTITUTION.md`.
- Validation evidence: implementation validation notes, M3 commit message validation evidence, visual inspection of generated assets, and reviewer reruns of focused Tai Chi image test, Markdown-first check, privacy check, and unittest discovery.

## Diff Summary

M3 adds exactly three generated raster support images for `exercises/tai-chi-basics.md`: `setup.png`, `weight-shift.png`, and `muscle-attention.png`.
The page references those three assets with meaningful alt text near setup, muscle guidance, and weight-shift Markdown.

Each image has a prompt record under `media/prompts/exercises/tai-chi-basics/`, an approved `media/PROVENANCE.md` row with the expected media purpose, and `exercises/tai-chi-basics.md` in `page_refs`.
The change also adds `visual-safety-review.md` evidence and a real-asset test that checks page references, prompt records, provenance, visual-safety evidence, and the exactly-three image batch.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | pass | M3 satisfies R20-R40 and R43 for the first image batch: exactly three selected images, expected paths and purposes, prompt records, approved provenance rows, page refs, meaningful alt text, and visual-safety evidence. |
| Test coverage | pass | `test_tai_chi_m3_support_batch_has_page_images_prompt_records_and_visual_review` directly covers TC-T6, TC-T7, TC-T9, and TC-T10 real-asset behavior. |
| Edge cases | pass | Existing M1 fixtures still cover fourth-image failure, second muscle-attention failure, missing prompt records, generic alt text, invalid purpose, and visual-safety text failures; reviewer broad unittest discovery passed. |
| Error handling | pass | M3 has no runtime path; rollback remains represented by removing page references, prompt records, provenance rows, and assets while preserving the M2 text page for M4 proof. |
| Architecture boundaries | pass | Assets are repository-local generated rasters, prompt records are repository-local Markdown, provenance stays in `media/PROVENANCE.md`, and Markdown remains source of truth. No hosted app, database, video, or generated public API was introduced. |
| Compatibility | pass | The approved public image paths and prompt-record paths are used. The M2 page-shape test was narrowed so it no longer conflicts with the approved M3 image state. |
| Security/privacy | pass | Privacy checker passed over the Tai Chi page, provenance, prompt records, change-local evidence, and `SOURCES.md`; no private reader data, private reviewer data, secrets, or private health information were observed. |
| Derived artifact currency | pass | Page image references, files, prompt records, provenance rows, and visual-safety evidence are synchronized. Reviewer visual inspection matched the visual-safety record. |
| Unrelated changes | pass | The reviewed commit is scoped to M3 media assets, prompt/provenance/page wiring, visual review evidence, tests, and workflow metadata; the unrelated untracked learning note is outside the review surface. |
| Validation evidence | pass | Reviewer reran the focused M3 image test, Markdown-first validation, privacy validation, and full unittest discovery successfully. The known `pytest` gap is recorded as an environment/tooling gap, not an M3 blocker. |

## No-Finding Rationale

The implementation meets the governed first-batch contract without exceeding the three-image limit or letting images become the source of truth.
Prompt records preserve exact prompts, provenance rows are complete and approved, and the page references only the selected setup, movement, and muscle-attention images.
Manual visual inspection found no in-image text, labels, identifiable faces, brand marks, clinical framing, combat framing, red pain marks, or exact anatomy labels.

## Residual Risks

M4 remains open.
This clean M3 review does not prove beginner comprehension, text-only rollback, final verification, CI status, PR readiness, or final closeout readiness.

## Reviewer Validation

- `python3 -m unittest tests.test_exercise_image_standard.ExerciseImageStandardTest.test_tai_chi_m3_support_batch_has_page_images_prompt_records_and_visual_review` passed.
- `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md` passed.
- `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md media/PROVENANCE.md media/prompts/exercises/tai-chi-basics/ docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/ SOURCES.md` passed.
- `python3 -m unittest discover -s tests` passed.
