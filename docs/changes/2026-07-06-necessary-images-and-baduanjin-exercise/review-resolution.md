# Review Resolution: Necessary Images and Baduanjin Exercise

## Status

M1 review-resolution complete; code-review R2 closed M1.

## Findings

| Finding | Status | Resolution |
|---|---|---|
| CR-M1-001 | resolved by `reviews/code-review-r2.md` | Added focused Baduanjin forbidden-scope fixtures for treatment protocol, full traditional form / all eight brocades, fall-prevention program, and adaptive coaching wording. |

## CR-M1-001

Source review: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-r1.md`

Required outcome: M1 needs direct BJ-T8 forbidden-scope fixture coverage for treatment, full-form, fall-prevention, and adaptive-coaching wording, or an upstream re-reviewed deferral.

Resolution:

- Added narrow checker patterns for `treatment protocol`, `full traditional form`, `all eight brocades`, `fall-prevention program`, and `adaptive coaching`.
- Added `test_baduanjin_forbidden_scope_wording_fails` to `tests/test_exercise_image_standard.py`.
- The new test runs temporary `exercises/baduanjin-basics.md` fixtures through the existing Markdown checker and asserts the forbidden-scope code `RB006`.

Validation:

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_exercise_image_standard` | pass: 26 tests |
| `python3 -m unittest tests.test_exercise_method_guidance` | pass: 19 tests |
| `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass: 56 tests |
| `python3 -m unittest discover -s tests` | pass: 175 tests |
| `git diff --check` | pass |

## Sources

- [Code review R1](reviews/code-review-r1.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
