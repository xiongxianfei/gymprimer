# Explain Change: Rowing Machine Basics and Beginner Workout Guidance

## Status

in progress

## M1. Cardio Method Boundary and Validation

M1 implements the scoped method-validation boundary required before the
rowing-machine page can rely on `Method type: basic_cardio_equipment`.

### What changed

- `tests/test_exercise_method_guidance.py` now proves that
  `basic_cardio_equipment` passes for `exercises/rowing-machine.md` when the
  visible method section has the required beginner-cardio labels.
- The same test proves that `basic_cardio_equipment` still fails for unrelated
  exercise pages.
- The existing deferred-type test still proves `loaded_carry` remains inactive.
- `tools/checks/check_markdown_first.py` now treats
  `basic_cardio_equipment` as active only for `exercises/rowing-machine.md`.
- The checker accepts `Rest/reset:` as an equivalent rest label and
  `Stop condition:` as an equivalent stop label, while preserving the existing
  `Rest:` and `Stop if:` labels for current exercise pages.

### Why it changed

The approved rowing-machine spec activates `basic_cardio_equipment` only for
rowing-machine content governed by this change. The earlier exercise-method
slice intentionally deferred that method type, so M1 adds a path-aware
activation rule instead of broadening the global active-method enum.

### Scope boundaries

- No rowing-machine content page was added in M1.
- No template change was needed because the existing visible `## How much to do`
  contract can represent the cardio method with label aliases.
- No `loaded_carry` activation was added.
- No runtime behavior, user input, tracker, hosted app, calculator, hidden
  metadata source of truth, diagnosis, treatment, rehab, or personalized
  coaching behavior was added.

### Validation

- `python3 -m unittest tests.test_exercise_method_guidance` passed.
- `python3 -m unittest tests.test_markdown_first_real_pages` passed.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises patterns principles` passed.
- `python3 tools/checks/check_privacy.py tools tests docs/templates specs docs/changes/rowing-machine-basics-and-beginner-workouts` passed.

## M2. Rowing Page and Source Index

M2 adds the text-first rowing-machine page and source-index support required by
the approved spec.

### What changed

- `exercises/rowing-machine.md` now exists as a Markdown page with setup,
  muscles, movement breakdown, beginner method guidance, easier/harder
  versions, safety notes, and page-local sources.
- `SOURCES.md` now includes reusable Concept2 rowing source IDs for technique,
  foot position, damper setting, and getting-started workouts.
- `tests/test_markdown_first_real_pages.py` now checks the rowing page shape,
  stroke sequence, setup and damper wording, `basic_cardio_equipment` labels,
  stop conditions, central safety link, required source IDs, and forbidden
  product/clinical/programming scope.

### Why it changed

The approved spec requires `exercises/rowing-machine.md` to teach rowing as
skill-based cardio equipment, with the drive sequence `legs -> body -> arms`,
the recovery sequence `arms -> body -> legs`, beginner-safe method guidance,
page-local citations, central safety routing, and no runtime product surface.

### Scope boundaries

- No media was added in M2; the page is text-first pending M3 comprehension and
  media-decision evidence.
- No README navigation was added because promotion remains gated by M3 manual
  proof and M4 lifecycle evidence.
- No `RED-FLAGS.md` change was needed because the existing central reference
  path works.
- No hosted app, tracker, calculator, user-input flow, hidden metadata source
  of truth, race plan, or broad cardio-equipment rollout was added.

### Validation

- Initial `python3 -m unittest tests.test_markdown_first_real_pages` failed
  before the page existed.
- `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages` passed.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises principles patterns` passed.
- `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises docs/changes/rowing-machine-basics-and-beginner-workouts` passed.
- `git diff --check` passed.
