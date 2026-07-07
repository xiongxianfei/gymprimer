# Review Resolution: Top-Five Generated Images for Fewer-Than-Five Exercise Documents

## Status

resolved

## Open Findings

| Finding ID | Status | Required resolution |
|---|---|---|
| PR-T5IMG-1 | resolved | Owner decision recorded: this initiative does not require repository-local `human_reviewer`, review-owner, visual-safety-review evidence, or replacement accountability artifacts. Human review happens through PR merge outside repository validation. |
| CR-T5IMG-M1-1 | resolved | `SCORE_FIELDS`, tests, fixtures, and M1 audit framework now use `setup_value`; regression coverage proves a named top-five audit with `setup_value` passes and a record missing it fails. |
| CR-T5IMG-M1-2 | resolved | Rank 1-5 `automatic_generation` now fails in all contexts; named top-five regression coverage proves `generate_now` and `first_generation_candidate` still pass. |
| CR-T5IMG-M2-1 | resolved | M2 audit scoring now uses the approved 1-5 score range, and regression coverage fails on 0-3 scale text or `0` score cells. |
| CR-T5IMG-M2-2 | resolved | `bird-dog/short-reach.png` was replaced with a visibly smaller-reach image, and the prompt record selected-output notes were updated. |

## Resolution Notes

- 2026-07-06: The owner clarified that this repository should not carry human-reviewer or replacement accountability requirements for this initiative because the PR will be merged after human review.
- Updated the proposal and draft spec to remove repository-local reviewer/accountability requirements for the named top-five image initiative.
- This resolution does not approve implementation by itself; proposal-review R2 and spec review are still required before downstream reliance.
- 2026-07-06: Resolved CR-T5IMG-M1-1 by replacing `safety_setup_value` with `setup_value` in the validator, test fixtures, and M1 audit framework.
- Added regression coverage that a named top-five audit using `setup_value` passes and a candidate missing `setup_value` fails.
- 2026-07-06: Resolved CR-T5IMG-M1-2 by making rank 1-5 `automatic_generation` fail before the named-initiative allowance for `generate_now` and `first_generation_candidate`.
- Added named-initiative regression coverage proving `automatic_generation` fails while `generate_now` and `first_generation_candidate` pass.
- M1 is ready for rerun code-review.
- 2026-07-06: Code-review R3 opened CR-T5IMG-M2-1 and CR-T5IMG-M2-2. M2 is in review-resolution before M3 can start.
- 2026-07-06: Resolved CR-T5IMG-M2-1 by updating the M2 audit evidence to the approved 1-5 scale and adding regression assertions that reject the old 0-3 scale text and any `0` candidate score cells.
- 2026-07-06: Resolved CR-T5IMG-M2-2 by replacing `media/exercises/bird-dog/short-reach.png` with a newly generated shorter-range image and updating the prompt record selected-output notes.
- M2 is ready for rerun code-review.

## Validation

- `python3 -m unittest tests.test_exercise_document_image_prioritization tests.test_exercise_image_standard` passed with 47 tests.
- `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed.
- `python3 tools/checks/check_privacy.py docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents docs/plan.md docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` passed.
- `git diff --check` passed.
- `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed with 68 tests after M2 review-resolution.
- `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed after M2 review-resolution.
- `python3 tools/checks/check_privacy.py exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed after M2 review-resolution.
- `git diff --check` passed after M2 review-resolution.

## Sources

- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/proposal-review-r1.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/code-review-r1.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/code-review-r3.md`
