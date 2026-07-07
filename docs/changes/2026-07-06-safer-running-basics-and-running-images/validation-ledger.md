# Safer Running M4 Validation Ledger

## Scope

- Change ID: `2026-07-06-safer-running-basics-and-running-images`
- Milestone: M4 Comprehension Proof and Final Readiness
- Reviewed page: `exercises/safer-running-basics.md`
- Manual proof: `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/beginner-comprehension-proof.md`
- Rollback proof: `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/rollback-proof.md`
- Visual review proof: `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/visual-safety-review.md`

## Validation Commands

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_rollback_proof_records_text_only_cleanup tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_validation_ledger_records_final_handoff_commands` | pass |
| `python3 -m unittest tests.test_exercise_method_guidance` | pass |
| `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass |
| `python3 -m unittest discover -s tests` | pass |
| `python3 tools/checks/check_markdown_first.py exercises/safer-running-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md` | pass |
| `python3 tools/checks/check_privacy.py exercises/safer-running-basics.md media/PROVENANCE.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md` | pass |
| `git diff --check` | pass |

## Rollback Rehearsal

| Command | Result |
|---|---|
| `GYMPRIMER_ROOT=/tmp/gymprimer-safer-running-rollback.m4 python3 tools/checks/check_markdown_first.py /tmp/gymprimer-safer-running-rollback.m4/exercises/safer-running-basics.md /tmp/gymprimer-safer-running-rollback.m4/media/PROVENANCE.md /tmp/gymprimer-safer-running-rollback.m4/SOURCES.md /tmp/gymprimer-safer-running-rollback.m4/RED-FLAGS.md` | pass |
| `GYMPRIMER_ROOT=/tmp/gymprimer-safer-running-rollback.m4 python3 tools/checks/check_privacy.py /tmp/gymprimer-safer-running-rollback.m4/exercises/safer-running-basics.md /tmp/gymprimer-safer-running-rollback.m4/media/PROVENANCE.md /tmp/gymprimer-safer-running-rollback.m4/SOURCES.md /tmp/gymprimer-safer-running-rollback.m4/RED-FLAGS.md` | pass |

## CI

CI was not observed.

No hosted CI pass is claimed by this ledger.

## Residual Risk

M4 records static proof and local validation only.
It does not replace downstream code-review, final verification, PR review, or any hosted CI that may run later.

## Sources

- `specs/safer-running-basics-and-running-images.md`
- `specs/safer-running-basics-and-running-images.test.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/beginner-comprehension-proof.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/rollback-proof.md`
