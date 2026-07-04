# Change Rationale: Exercise Method Guidance

## Summary

This change implements the approved exercise-method guidance workflow in
milestones. M1 adds the authoring template and deterministic validation surface
for the visible `## How much to do` contract before proof-slice exercise content
is edited in later milestones.

## Current Scope

M1 is limited to:

- `docs/templates/exercise-card.md`
- method-guidance checks in `tools/checks/check_markdown_first.py`
- focused Markdown-first tests and fixtures
- compatibility notes in `specs/markdown-first-primer.md` and
  `specs/responsible-breadth.md` only where needed
- workflow records under `docs/changes/exercise-method-guidance/`

M1 does not update the six proof-slice exercise pages, create the principle
page, record manual source audit, record beginner-comprehension evidence, or
claim broad rollout.

## Status

M1 implementation is review-requested. Code-review has not happened yet.

## M1 Rationale

The checker now validates method guidance only when an exercise page contains
`## How much to do`, or when a page tries to use hidden-only `method_type`
metadata. This keeps M1 additive and avoids forcing unselected exercise pages to
adopt the new section before M3.

The template now shows the required visible labels: `Method type:`, `Beginner
starting point:`, `Effort:`, `Rest:`, `Progression:`, and `Stop if:`. The
wording keeps starter guidance static and educational, and routes broader
safety concerns to `RED-FLAGS.md`.

The related specs received pointer-only compatibility notes to
`specs/exercise-method-guidance.md`. They do not duplicate the active method
type menu or starter-range tables, so the focused spec remains the normative
home for the method contract.

## M1 Validation

- `python3 -m unittest tests.test_exercise_method_guidance` failed before
  implementation for the expected missing checker function, then passed with 7
  tests after implementation.
- `python3 -m unittest tests.test_markdown_first_templates` failed before the
  template method section existed, then passed after implementation.
- `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` passed with 7 tests.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed with 52 tests.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises patterns principles` passed and checked 21 Markdown files.
- `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-method-guidance` passed and checked 89 files.
- `python3 -m unittest discover -s tests` passed with 109 tests as additional smoke.
- `git diff --check` passed.
