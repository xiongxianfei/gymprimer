# Validation Ledger: Rowing Machine Basics and Beginner Workout Guidance

## Status

M4 review-requested

## Scope

- Change ID: `rowing-machine-basics-and-beginner-workouts`
- Milestone: M4
- Ledger date: 2026-07-04
- Environment: local repository checkout on branch `proposal/rowing-machine-basics`
- CI observation status: hosted CI was not observed

## Preconditions

- M1 scoped `basic_cardio_equipment` validation is closed by code-review.
- M2 rowing-machine page and source-index work is closed by code-review after
  CR-RMB-M2-1 review-resolution.
- M3 manual source audit, beginner comprehension proof, and text-only media
  decision are closed by code-review.
- No rowing-machine media is referenced, so no rowing `media/PROVENANCE.md`
  row, prompt record, or visual-safety review is required for this state.

## Commands

| Command | Result | Evidence summary |
| --- | --- | --- |
| `python3 -m unittest discover -s tests` | pass | Ran 120 tests; result `OK`. |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media` | pass | Checked 27 Markdown files; result `pass`. |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md` | pass | Checked 75 files; result `privacy pass`. |
| `git diff --check` | pass | No whitespace errors reported. |

## Promotion and Navigation Decision

No README or navigation edit is included in M4. The approved plan lists
`README.md` as conditional: update it only if the approved promotion path
requires navigation. The rowing-machine page, manual proof, and validation
evidence are ready for M4 code-review without adding a repository entry-point
link in this slice.

## Residual Risk

- Hosted CI was not observed.
- M4 code-review, durable cross-milestone review, final verification, and PR
  handoff remain downstream gates.
- The page remains text-only; adding rowing-machine media later would re-run
  the media decision, provenance, prompt-record, and visual-safety obligations.

## No Premature Claims

This ledger records local validation only. It does not claim CI passed, branch
readiness, PR readiness, final verification, final closeout, or merge readiness.

## Re-Run Trigger

Re-run this ledger after any implementation, test, source, media, proof,
navigation, or validation-command change.
