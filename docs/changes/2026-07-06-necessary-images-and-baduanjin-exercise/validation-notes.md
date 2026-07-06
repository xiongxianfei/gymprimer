# Validation Notes: Necessary Images and Baduanjin Exercise

## Status

M1 implementation validation complete; code-review pending.

## 2026-07-06 M1

Scope validated:

- path-scoped five-image exception for `exercises/baduanjin-basics.md`;
- unchanged three-image default for other exercise pages;
- one muscle-attention image limit;
- prompt-record and visual-semantic negative fixtures for Baduanjin images;
- `low_load_control_drill` positive and negative method fixtures;
- ranked top-10 candidate-pool evidence before image generation.

Commands run:

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_exercise_method_guidance` | pass: 19 tests |
| `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass: 55 tests |
| `python3 -m unittest discover -s tests` | pass: 174 tests |
| `git diff --check` | pass |
| `python3 tools/checks/check_markdown_first.py docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/image-candidate-pool.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/explain-change.md` | pass: checked 5 Markdown files |
| `python3 tools/checks/check_privacy.py docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | pass: checked 12 files |

Residual risk:

- M1 does not implement `exercises/baduanjin-basics.md`, generated assets, prompt records, provenance rows, visual-safety review, beginner-comprehension proof, or rollback proof.
- Real-page integration tests for Baduanjin remain assigned to later milestones once those files exist.

## 2026-07-06 M1 Review Resolution

Scope validated:

- CR-M1-001 forbidden-scope fixture coverage for treatment protocol, full traditional form / all eight brocades, fall-prevention program, and adaptive coaching wording.

Commands run:

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_exercise_image_standard` | pass: 26 tests |
| `python3 -m unittest tests.test_exercise_method_guidance` | pass: 19 tests |
| `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass: 56 tests |
| `python3 -m unittest discover -s tests` | pass: 175 tests |
| `git diff --check` | pass |

## Sources

- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
