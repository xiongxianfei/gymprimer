# Validation Ledger: Rowing Machine Basics and Beginner Workout Guidance

## Status

M5 media enhancement closed by code-review

## Scope

- Change ID: `rowing-machine-basics-and-beginner-workouts`
- Milestone: M5 follow-up media enhancement
- Ledger date: 2026-07-04
- Environment: local repository checkout on branch `proposal/rowing-machine-basics`
- CI observation status: hosted CI was not observed

## Preconditions

- M1 scoped `basic_cardio_equipment` validation is closed by code-review.
- M2 rowing-machine page and source-index work is closed by code-review after
  CR-RMB-M2-1 review-resolution.
- M3 manual source audit and beginner comprehension proof are closed by
  code-review.
- The M3 media decision was re-run after the user requested necessary images
  for readability.
- Rowing-machine setup, muscle-attention, and movement images now have local
  page references, `media/PROVENANCE.md` rows, exact prompt records, and
  visual-safety review.
- Code-review M5 R1 closed the media enhancement with no implementation
  findings.

## Commands

| Command | Result | Evidence summary |
| --- | --- | --- |
| `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_rowing_machine_media_is_local_prompt_backed_and_reviewed` | pass | Failed first before media wiring; passed after page references, provenance, and prompt records were added. |
| `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media` | pass | Checked 20 Markdown files; result `pass`. |
| `python3 -m unittest discover -s tests -p 'test_*image*.py'` | pass | Ran 14 tests; result `OK`. |
| `python3 -m unittest discover -s tests` | pass | Ran 121 tests; result `OK`. |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media` | pass | Checked 27 Markdown files; result `pass`. |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md` | pass | Checked 84 files; result `privacy pass`. |
| `git diff --check` | pass | No whitespace errors reported. |

## Reviewer Reruns

| Command | Result | Evidence summary |
| --- | --- | --- |
| `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_rowing_machine_media_is_local_prompt_backed_and_reviewed` | pass | Code-review M5 R1 reran the targeted rowing media regression; result `OK`. |
| `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media` | pass | Code-review M5 R1 checked 20 Markdown files; result `pass`. |
| `python3 -m unittest discover -s tests -p 'test_*image*.py'` | pass | Code-review M5 R1 ran 14 image-standard tests; result `OK`. |
| `python3 -m unittest discover -s tests` | pass | Code-review M5 R1 ran 121 tests; result `OK`. |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media` | pass | Code-review M5 R1 checked 27 Markdown files; result `pass`. |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md` | pass | Code-review M5 R1 checked 84 files; result `privacy pass`. |
| `git diff --check` | pass | Code-review M5 R1 found no whitespace errors. |
| `python3 tools/checks/check_privacy.py docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m5-r1.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/plan.md docs/changes/rowing-machine-basics-and-beginner-workouts/validation-ledger.md` | pass | Post-review recording check covered six lifecycle files; result `privacy pass`. |
| `git diff --check` | pass | Post-review recording check found no whitespace errors. |
| `state-sync check for docs/plan.md, docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md, docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml, review-log.md, and validation-ledger.md` | pass | Lifecycle metadata points to explain-change after M5 closeout. |

## Promotion and Navigation Decision

No README or navigation edit is included in M5. The approved plan lists
`README.md` as conditional: update it only if the approved promotion path
requires navigation. The rowing-machine page now has local setup,
muscle-attention, and movement images, but promotion/navigation remains gated
by code-review and later final verification.

## Residual Risk

- Hosted CI was not observed.
- Durable cross-milestone rationale, final verification, and PR handoff remain
  downstream gates.
- The generated images are static support assets; Markdown remains the source
  of truth for setup, muscle engagement, sequence, safety, and method guidance.

## No Premature Claims

This ledger records local validation only. It does not claim CI passed, branch
readiness, PR readiness, final verification, final closeout, or merge readiness.

## Re-Run Trigger

Re-run this ledger after any implementation, test, source, media, proof,
navigation, or validation-command change.
