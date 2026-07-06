# Code Review M3 R1: Necessary Images and Baduanjin Exercise

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-m3-r1.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-log.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/change.yaml`, `docs/plan.md`
- Open blockers: none
- Next stage: implement M4
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-m3-r1.md`
- Review log: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M3
- Milestone closeout: closed
- Remaining implementation milestones: M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `ecf4da7` (`M3: add governed Baduanjin image batch`).
- Tracked governing branch state: `proposal/baduanjin-exercise-images` at `ecf4da7`.
- Governing artifacts: `specs/necessary-images-and-baduanjin-exercise.md`, `specs/necessary-images-and-baduanjin-exercise.test.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`.
- Validation evidence: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md`.
- Relevant implementation files: `exercises/baduanjin-basics.md`, `media/PROVENANCE.md`, `media/exercises/baduanjin-basics/`, `media/prompts/exercises/baduanjin-basics/`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/visual-safety-review.md`, `tests/test_markdown_first_real_pages.py`.

## Diff Summary

M3 adds the five approved Baduanjin first-batch images: setup, two-hands-lift, drawing-bow, alternating-reach, and muscle-attention.
The page references exactly those five local assets with meaningful alt text and keeps the images framed as broad visual references.
Each asset has an exact prompt record under `media/prompts/exercises/baduanjin-basics/` and one approved `media/PROVENANCE.md` row with the expected purpose and `exercises/baduanjin-basics.md` page ref.
The milestone also records manual image review evidence, updates the exercise-image inventory, and adds real-page tests for the actual prompt-backed media surface.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | pass | R22-R29 are satisfied by exactly five first-batch page references and the expected asset names and purposes. R30-R35 are satisfied by approved provenance rows and matching prompt records. R36-R40 are supported by meaningful alt text, direct asset inspection, and the M3 image review record. |
| Test coverage | pass | `tests/test_markdown_first_real_pages.py` adds `test_baduanjin_m3_images_are_local_prompt_backed_and_reviewed`, which checks count, local assets, prompt records, provenance row uniqueness, media purpose, approval status, page refs, and prompt contents. Existing image-standard tests continue to cover sixth-image, second-muscle-attention, prompt-record, and visual-wording failures. |
| Edge cases | pass | EC2-EC9 have direct automated or manual evidence: exactly five images, no second muscle-attention image, no sixth image, prompt-record matching, approved provenance, and visual review for combat framing and exact-anatomy risks. |
| Error handling | pass | This static Markdown slice has no runtime failure path; rollback remains assigned to M4, and the plan records removal of failed references, assets, prompt records, and provenance rows as recovery. |
| Architecture boundaries | pass | Media remains repository-local, Markdown remains authoritative, generated assets are not source-of-truth evidence, and no hosted app, CMS, account, user-input flow, API, or video-first path is introduced. |
| Compatibility | pass | The new public asset and prompt-record paths match the approved compatibility surfaces, and the five-image exception remains scoped to `exercises/baduanjin-basics.md`. |
| Security/privacy | pass | Prompt records, provenance, review evidence, and assets contain no secrets, private health data, user profiles, or identifiable faces; local privacy validation is recorded. |
| Derived artifact currency | pass | Page references, asset files, prompt records, provenance rows, visual review evidence, validation notes, plan state, change metadata, and the image-audit inventory were updated together. |
| Unrelated changes | pass | The diff is limited to the M3 media batch, page media references, real-page media tests, and change-local lifecycle evidence. |
| Validation evidence | pass | Validation notes record the focused failing-before test, focused passing-after test, combined image/real-page test suite, full unittest discovery, Markdown checks, privacy checks, and `git diff --check`. |

## No-Finding Rationale

The implementation satisfies the M3 contract without expanding into M4 proof work.
The real Baduanjin page now references exactly the approved five generated raster assets, and every referenced asset has the expected local prompt record, approved provenance row, page ref, and purpose.
Direct visual inspection found no in-image text, labels, clinical framing, combat framing, identifiable face, weapons, targets, red marks, or exact anatomy labels.
The one residual visual nuance is that the drawing-bow stance is wider than the easiest beginner setup, but it remains a calm side-stance illustration and the Markdown keeps stance depth and range conservative.

## Residual Risks

- M4 must still record beginner comprehension proof and text-only rollback proof.
- Final holistic code review is still required after all implementation milestones are complete.

## Milestone Handoff State

- Reviewed milestone: M3
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining in-scope implementation milestones: M4
- Next stage: implement M4
- Final closeout readiness: not ready because M4 remains unimplemented and downstream review, final verification, and PR handoff have not happened.

## Sources

- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
- [Baduanjin Visual-Safety Review](../visual-safety-review.md)
