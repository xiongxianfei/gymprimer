# Explain Change: Safer Running Basics and High-Quality Running Images M1-M2

Change ID: `2026-07-06-safer-running-basics-and-running-images`

Milestone: M1 Validation and Contract Fixtures; M2 Markdown Page and Source Contract

Status: review-requested

## M2 What Changed

M2 adds the text-only safer-running exercise page and its source-support proof before generated images are introduced.

Changed surfaces:

- `exercises/safer-running-basics.md`
- `tests/test_markdown_first_real_pages.py`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/source-audit.md`
- `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- `docs/plan.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/change.yaml`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/explain-change.md`

## M2 Why

The approved spec requires a beginner-facing page at `exercises/safer-running-basics.md` with the approved H1, alias line, required headings, `basic_cardio_activity` method guidance, page-local sources, and `RED-FLAGS.md` routing.

The page keeps the original search intent by using `injury-free running` only in the alias line, then states that no page can guarantee injury-free running. It teaches run/walk intervals, easy effort, rest days, warm-up, gradual loading, simple form cues, broad muscle attention, common mistakes, easier and harder variants, and non-clinical safety routing.

M2 also updates the existing exercise-image M4 audit with a zero-image row for the new page because that audit is tested as an inventory of all current `exercises/*.md` pages. The row keeps image generation deferred to M3.

## M2 Tests First

The new real-page tests were added before the page and audit artifact.

Observed red state:

- `python3 -m unittest tests.test_markdown_first_real_pages` failed because `exercises/safer-running-basics.md` and `docs/changes/2026-07-06-safer-running-basics-and-running-images/source-audit.md` did not exist.

After adding the page, source audit, and exercise-image audit inventory row, the targeted and full suites passed.

## M2 Scope Boundaries

M2 intentionally does not create:

- generated running images;
- prompt records;
- `media/PROVENANCE.md` rows;
- visual-safety review;
- beginner comprehension proof.

Those remain assigned to M3 and M4 in the active plan.

## M2 Validation

Passed locally:

```bash
python3 -m unittest tests.test_markdown_first_real_pages
python3 tools/checks/check_markdown_first.py exercises/safer-running-basics.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-safer-running-basics-and-running-images
python3 tools/checks/check_privacy.py exercises/safer-running-basics.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-safer-running-basics-and-running-images
python3 -m unittest discover -s tests
```

## M1 What Changed

M1 adds validation coverage for the future `Safer Running Basics` page without creating the page, images, prompt records, or provenance rows.

Changed surfaces:

- `tests/test_exercise_method_guidance.py`
- `tests/test_exercise_image_standard.py`
- `tools/checks/check_markdown_first.py`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- `docs/plan.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/change.yaml`

## M1 Why

The approved spec requires `exercises/safer-running-basics.md` to use `Method type: basic_cardio_activity` and authorizes a page-specific first-batch exception for exactly six running images.

Before the running page or images are added, M1 makes those contracts enforceable:

- `basic_cardio_activity` is now active for `exercises/safer-running-basics.md`.
- The running image exception allows up to six images for that page.
- The exception is constrained to the six approved first-batch asset paths.
- A seventh image, a second muscle-attention image, or an unapproved running asset fails validation.

## M1 Tests First

The new tests were added before the checker update.

Observed red state:

- `python3 -m unittest tests.test_exercise_method_guidance` failed with `exercise_method_inactive_type` for `exercises/safer-running-basics.md`.
- `python3 -m unittest tests.test_exercise_image_standard` failed because the running image fixture still used the default three-image limit and had no unapproved-asset finding.

After updating the checker, the targeted suites passed.

## M1 Scope Boundaries

M1 intentionally does not create:

- `exercises/safer-running-basics.md`;
- generated running images;
- prompt records;
- `media/PROVENANCE.md` rows;
- visual-safety review;
- beginner comprehension proof.

Those remain assigned to later milestones in the active plan.

## M1 Validation

Passed locally:

```bash
python3 -m unittest tests.test_exercise_method_guidance
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
python3 -m unittest discover -s tests
```

Final Markdown, privacy, and diff checks are recorded in the implementation handoff.

## Review Resolution

Code-review M1 R1 recorded GP-SRB-M1-CR1 for missing M1 coverage of the approved page shape, alias boundary, and source-registration proof.

Resolution added:

- safer-running page-shape fixture tests for the approved H1, alias line, required headings, and page-local sources;
- source-registration proof through the shared `SOURCES.md` fixture;
- checker enforcement for the safer-running title, alias line, and required sections;
- a safer-running image fixture update so image-exception tests still exercise a valid page contract.

## Sources

- `specs/safer-running-basics-and-running-images.md`
- `specs/safer-running-basics-and-running-images.test.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
