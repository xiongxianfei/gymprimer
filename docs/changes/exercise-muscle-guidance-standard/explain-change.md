# Explain Change: Exercise Muscle Guidance

## M1 scope

M1 implements the authoring and deterministic validation surface for the approved exercise muscle guidance standard. It does not migrate proof-slice pages, rewrite all exercise pages, add images, or perform semantic source audits.

## M1 changes

- `docs/templates/exercise-card.md` now prompts authors to write role-based `## Muscles involved` guidance, keep broad regions first, use technical names only when useful and source-supported, and pair the section with soft `## What you should feel` cues.
- `tools/checks/check_markdown_first.py` now has `validate_exercise_muscle_guidance()` for adopted exercise pages. It checks the durable heading, legacy heading misuse when a page has adopted the feel-cue pairing, missing feel sections, role or phase table columns, bare muscle lists, exact activation wording, EMG-as-instruction wording, "must feel or wrong" cues, and deterministic diagnosis/treatment/correction/personalized-coaching wording.
- `tests/test_exercise_muscle_guidance.py` adds focused unit coverage for the M1 proof map: adopted-page structure, legacy compatibility, role tables, role bullets, phase tables, forbidden wording, and observable failure categories.
- `tests/test_markdown_first_templates.py` now checks that the exercise template exposes the new authoring guidance.

## M1 compatibility decision

The checker intentionally preserves untouched legacy `## Used muscles` pages. A page becomes stricter M1 validation scope when it adopts visible `## Muscles involved` or `## What you should feel` guidance. This keeps M1 from becoming the broad migration that the proposal, spec, and plan explicitly deferred to later slices.

## M1 validation

- `python3 -m unittest tests.test_exercise_muscle_guidance` passed.
- `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` passed.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises` passed.
- `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-muscle-guidance-standard` passed.
- `git diff --check` passed.

## M2 scope

M2 applies the approved contract to one representative exercise page per required proof-slice category. It does not migrate the remaining legacy `## Used muscles` pages, add new sources to `SOURCES.md`, change checker semantics, or alter exercise images.

## M2 changes

- `tests/test_markdown_first_real_pages.py` now records the selected proof slice and asserts category coverage, `## Muscles involved`, `## What you should feel`, role or phase structure, soft feel language, source-surface citations, and untouched legacy compatibility outside M2.
- `exercises/rowing-machine.md` now uses a phase table for drive, transfer, finish, and recovery muscle roles.
- `exercises/chest-press.md` now uses a role table for chest, triceps/front shoulders, and upper-back/shoulder-blade control.
- `exercises/plank.md` migrated from `## Used muscles` to `## Muscles involved` and adds a paired `## What you should feel` section for trunk-control awareness.
- `exercises/chin-nod.md` now uses soft role bullets for control focus and posture support.
- `exercises/thoracic-extension.md` now distinguishes mobility focus from support, keeping the drill framed as gentle movement rather than strengthening or posture correction.
- `exercises/band-pull-apart.md` now uses a role table for upper-back/rear-shoulder work, band-path support, and neck/rib/trunk control.

## M2 compatibility decision

M2 leaves nonselected legacy pages with `## Used muscles` untouched and explicitly tests that they remain checker-compatible. Existing muscle-attention images and provenance rows are unchanged because the page text already keeps images support-only and locally cited.

## M2 validation

- `python3 -m unittest tests.test_markdown_first_real_pages` failed before content migration with six expected proof-slice failures.
- `python3 -m unittest tests.test_exercise_muscle_guidance tests.test_markdown_first_real_pages` passed.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md` passed.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed.
- `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises media docs/changes/exercise-muscle-guidance-standard` passed.
- `git diff --check` passed.

## M3 scope

M3 records the manual proof and future rollout gate required after the proof-slice page migration. It does not rewrite additional exercise pages, escalate checker enforcement, add or regenerate images, or claim final verification.

## M3 changes

- `tests/test_exercise_muscle_guidance.py` now asserts that M3 manual proof files exist and contain the required source-audit claim types, beginner-comprehension prompts, muscle-image alignment checks, remaining-page rollout classifications, and validation-ledger commands.
- `docs/changes/exercise-muscle-guidance-standard/manual-proof/source-audit.md` records sampled main-driver, support/stabilizer, feel-cue, compensation-cue, and safety-cue source support.
- `docs/changes/exercise-muscle-guidance-standard/manual-proof/beginner-comprehension.md` records non-identifying proof-slice comprehension outcomes for the required prompts.
- `docs/changes/exercise-muscle-guidance-standard/manual-proof/muscle-image-alignment.md` records support-only alignment for the proof-slice muscle-attention images.
- `docs/changes/exercise-muscle-guidance-standard/manual-proof/broad-rollout-gate.md` classifies remaining exercise pages for future batches without authorizing broad migration.
- `docs/changes/exercise-muscle-guidance-standard/validation-ledger.md` records the M3 validation commands and outcomes.

## M3 compatibility decision

M3 leaves exercise Markdown, media assets, media prompt records, provenance rows, and `SOURCES.md` unchanged. The manual proof records residual risk and future-batch decisions instead of making broad content edits inside the proof milestone.

## M3 validation

- `python3 -m unittest tests.test_exercise_muscle_guidance` failed before evidence creation with five expected missing-file failures.
- `python3 -m unittest tests.test_exercise_muscle_guidance` passed.
- `python3 tools/checks/check_privacy.py docs/changes/exercise-muscle-guidance-standard` passed.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md` passed.
- `git diff --check` passed.

## Next stage

M3 is ready for code-review. Final verification and PR handoff remain blocked until M3 review closes.
