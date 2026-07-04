# Explain Change: Exercise Muscle Guidance M1

## Scope

M1 implements the authoring and deterministic validation surface for the approved exercise muscle guidance standard. It does not migrate proof-slice pages, rewrite all exercise pages, add images, or perform semantic source audits.

## What changed

- `docs/templates/exercise-card.md` now prompts authors to write role-based `## Muscles involved` guidance, keep broad regions first, use technical names only when useful and source-supported, and pair the section with soft `## What you should feel` cues.
- `tools/checks/check_markdown_first.py` now has `validate_exercise_muscle_guidance()` for adopted exercise pages. It checks the durable heading, legacy heading misuse when a page has adopted the feel-cue pairing, missing feel sections, role or phase table columns, bare muscle lists, exact activation wording, EMG-as-instruction wording, "must feel or wrong" cues, and deterministic diagnosis/treatment/correction/personalized-coaching wording.
- `tests/test_exercise_muscle_guidance.py` adds focused unit coverage for the M1 proof map: adopted-page structure, legacy compatibility, role tables, role bullets, phase tables, forbidden wording, and observable failure categories.
- `tests/test_markdown_first_templates.py` now checks that the exercise template exposes the new authoring guidance.

## Compatibility decision

The checker intentionally preserves untouched legacy `## Used muscles` pages. A page becomes stricter M1 validation scope when it adopts visible `## Muscles involved` or `## What you should feel` guidance. This keeps M1 from becoming the broad migration that the proposal, spec, and plan explicitly deferred to later slices.

## Validation

- `python3 -m unittest tests.test_exercise_muscle_guidance` passed.
- `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` passed.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises` passed.
- `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-muscle-guidance-standard` passed.
- `git diff --check` passed.

## Next stage

M1 is ready for code-review. M2 proof-slice page migration remains blocked until M1 review closes.
