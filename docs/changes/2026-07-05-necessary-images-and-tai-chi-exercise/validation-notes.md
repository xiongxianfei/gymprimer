# Validation Notes: Necessary Images and Tai Chi Exercise

## M4 Local Validation

Date: 2026-07-06

Focused proof tests:

- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_m4_rollback_proof_records_text_only_cleanup`
- Before implementation: failed because `beginner-comprehension-proof.md` and `rollback-proof.md` did not exist.
- After implementation: pass, 2 tests.

Temporary rollback rehearsal:

- Temporary root: `/tmp/gymprimer-tai-chi-rollback.CcCD26`
- `python3 tools/checks/check_markdown_first.py /tmp/gymprimer-tai-chi-rollback.CcCD26/exercises/tai-chi-basics.md /tmp/gymprimer-tai-chi-rollback.CcCD26/media/PROVENANCE.md /tmp/gymprimer-tai-chi-rollback.CcCD26/SOURCES.md /tmp/gymprimer-tai-chi-rollback.CcCD26/RED-FLAGS.md`: pass, checked 4 Markdown files.
- `python3 tools/checks/check_privacy.py /tmp/gymprimer-tai-chi-rollback.CcCD26/exercises/tai-chi-basics.md /tmp/gymprimer-tai-chi-rollback.CcCD26/media/PROVENANCE.md /tmp/gymprimer-tai-chi-rollback.CcCD26/SOURCES.md /tmp/gymprimer-tai-chi-rollback.CcCD26/RED-FLAGS.md`: pass, checked 4 files.

Milestone command ledger:

- `python3 -m unittest tests.test_exercise_method_guidance`: pass, 17 tests.
- `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md`: pass, checked 4 Markdown files.
- `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md media/PROVENANCE.md media/prompts/exercises/tai-chi-basics/ docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/`: pass, checked 23 files.
- `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`: pass, 50 tests.
- `python3 -m unittest discover -s tests`: pass, 167 tests.
- `git diff --check`: pass.

Unavailable command:

- `python3 -m pytest`: unavailable because `pytest` is not installed: `/usr/bin/python3: No module named pytest`.

## Residual Risk

M4 records a non-identifying reviewer simulation for beginner comprehension. It does not replace future public-reader feedback after publication.
