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

## M2 Review Resolution. Safety Source Support

Code-review M2 R1 found that the safety note cited one heart-attack symptoms
source for the full stop-condition list. The resolution splits the safety note
into narrower groups:

- cardiopulmonary red flags: chest pain, dizziness, fainting, and unusual
  shortness of breath;
- pain and symptom escalation: sharp pain, symptoms that worsen, and numbness;
- technique breakdown: painful, jerky, or uncontrolled movement.

The page now cites the heart-attack symptoms source only for cardiopulmonary
warnings, reuses `nhs-back-pain` and `mayo-weight-training` for existing
safety/technique support, and adds `local-rowing-machine-exercise-pain` as a
page-local source for sharp or worsening exercise pain.

### Validation

- `python3 -m unittest tests.test_markdown_first_real_pages` failed after the
  test update and before the content fix because the new safety source IDs were
  absent.
- `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages` passed.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises principles patterns` passed.
- `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises docs/changes/rowing-machine-basics-and-beginner-workouts` passed.
- `git diff --check` passed.

## M3. Manual Proof and Media Decision

M3 records the semantic proof that static checks cannot provide and decides
whether rowing needs images before promotion.

### What changed

- `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/source-audit.md`
  records source support for setup, stroke sequence, damper, muscles, method
  examples, weekly activity, stop conditions, and source-index discipline.
- `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/beginner-comprehension.md`
  records a non-identifying reviewer simulation for the required beginner read
  questions.
- `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/media-decision.md`
  accepts text-only guidance and records that no rowing media, provenance row,
  prompt record, or visual-safety review is required in M3.
- `exercises/rowing-machine.md` now cites a page-local Concept2 muscles-used
  source for the broad muscles section.
- `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md`
  now lists `exercises/rowing-machine.md` as a current text-only exercise page.
- `tools/checks/check_markdown_first.py` skips `media/prompts/` Markdown prompt
  records during reader-facing page scans; `tests/test_exercise_image_standard.py`
  has regression coverage for that behavior.

### Why it changed

The approved M3 plan requires manual source audit, beginner comprehension proof,
and a media decision before promotion. During validation, the image-standard
audit and prompt-record scan behavior also needed same-slice alignment because
the new rowing page changed the exercise inventory and the M3 validation command
scans `media`.

### Validation

- Initial `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media`
  failed before the checker update because existing `media/prompts/...` prompt
  records were treated as reader-facing content pages.
- Initial `python3 -m unittest discover -s tests -p 'test_*image*.py'` failed
  before the audit update because `exercises/rowing-machine.md` was missing
  from the exercise-image M4 audit inventory.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media` passed.
- `python3 tools/checks/check_privacy.py exercises media docs/changes/rowing-machine-basics-and-beginner-workouts` passed.
- `python3 -m unittest discover -s tests -p 'test_*image*.py'` passed.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed.
- `git diff --check` passed.

## M4. Integration and Validation Ledger

M4 records the integration validation evidence and routes the change to
code-review without claiming downstream readiness.

### What changed

- `docs/changes/rowing-machine-basics-and-beginner-workouts/validation-ledger.md`
  records the exact M4 validation commands, outcomes, CI observation status,
  residual risks, and navigation decision.
- The active plan and change metadata now route M4 to code-review.
- README navigation is unchanged because the approved plan makes README edits
  conditional, and no required navigation change exists for this milestone.

### Why it changed

The approved test spec requires a durable M4 ledger that ties exact local
commands, outcomes, residual risks, and promotion/navigation decisions to the
implementation state before code-review handoff.

### Validation

- `python3 -m unittest discover -s tests` passed.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media` passed.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md` passed.
- `git diff --check` passed.
