# Review Resolution: Necessary Images and Baduanjin Exercise

## Status

M4 review-resolution implemented for CR-M4-001; code-review rereview pending.

## Findings

| Finding | Status | Resolution |
|---|---|---|
| CR-M1-001 | resolved by `reviews/code-review-r2.md` | Added focused Baduanjin forbidden-scope fixtures for treatment protocol, full traditional form / all eight brocades, fall-prevention program, and adaptive coaching wording. |
| CR-M4-001 | resolved pending code-review rereview | Updated rollback proof, validation notes, plan evidence, and change metadata with concrete temporary-root commands and reran focused rollback checks. |

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

## CR-M4-001

Source review: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-m4-r1.md`

Required outcome: M4 rollback evidence must record a reproducible temporary-root command sequence that matches the command actually exercised, and the focused rollback Markdown-first and privacy checks must pass from that recorded sequence.

Resolution:

- Replaced the wildcard `GYMPRIMER_ROOT=/tmp/gymprimer-baduanjin-rollback.*` evidence with a concrete temporary root: `/tmp/gymprimer-baduanjin-rollback.cr-m4-001`.
- Updated the rollback proof to record the setup commands that create the temporary text-only page and remove Baduanjin provenance rows.
- Updated validation notes, plan evidence, and change metadata to use the concrete temporary-root command record.

Validation:

| Command | Result |
|---|---|
| `tmp=/tmp/gymprimer-baduanjin-rollback.cr-m4-001; GYMPRIMER_ROOT="$tmp" python3 tools/checks/check_markdown_first.py "$tmp/exercises/baduanjin-basics.md" "$tmp/media/PROVENANCE.md" "$tmp/SOURCES.md" "$tmp/RED-FLAGS.md"` | pass: checked 4 Markdown files |
| `tmp=/tmp/gymprimer-baduanjin-rollback.cr-m4-001; GYMPRIMER_ROOT="$tmp" python3 tools/checks/check_privacy.py "$tmp/exercises/baduanjin-basics.md" "$tmp/media/PROVENANCE.md" "$tmp/SOURCES.md" "$tmp/RED-FLAGS.md"` | pass: checked 4 files |
| `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_rollback_proof_records_text_only_cleanup` | pass: 2 tests |
| `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass: 84 tests |
| `python3 -m unittest discover -s tests` | pass: 184 tests |
| `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | pass: checked 25 Markdown files |
| `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/plan.md docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | pass: checked 29 files |
| `git diff --check` | pass |

## Sources

- [Code review R1](reviews/code-review-r1.md)
- [Code review M4 R1](reviews/code-review-m4-r1.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
