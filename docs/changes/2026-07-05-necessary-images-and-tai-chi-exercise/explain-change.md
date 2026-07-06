# Explain Change: Necessary Images and Tai Chi Exercise

## M1 validation proof-map implementation

M1 adds Tai Chi-specific validation coverage before page content or image assets are introduced.
The implementation updates `tests/test_exercise_image_standard.py` with fixtures for the Tai Chi candidate-pool contract, the exact first-batch image paths and purposes, fourth-image rejection, second muscle-attention rejection, prompt-record failure, generic alt-text failure, and deterministic visual-safety text failure.

The implementation also updates `tests/test_exercise_method_guidance.py` with Tai Chi-specific `low_load_control_drill` method fixtures.
Those fixtures confirm that static low-load control wording passes and adaptive or rehab/treatment wording fails.

No checker code changed in M1.
The new tests passed against the existing method, media-purpose, image-count, prompt-record, provenance, alt-text, and visual-safety validation paths.
That keeps M1 scoped to proof coverage and avoids adding page-specific checker branches before a failing test demonstrates a gap.

## Validation evidence

- `python3 -m unittest tests.test_exercise_image_standard tests.test_exercise_method_guidance` passed after correcting an overly literal contract assertion.
- `python3 -m unittest tests.test_exercise_method_guidance` passed.
- `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed.
- `python3 -m unittest discover -s tests` passed.
- `git diff --check` passed.
- `python3 tools/checks/check_privacy.py tests/test_exercise_image_standard.py tests/test_exercise_method_guidance.py specs/necessary-images-and-tai-chi-exercise.test.md docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/` passed.

`python3 -m pytest` was attempted because the draft plan had named it, but it could not run in this environment because `pytest` is not installed.
The reviewed test spec command ledger uses unittest commands for M1.
