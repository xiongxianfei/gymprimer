# Explain Change: Safer Running Basics and High-Quality Running Images M1

Change ID: `2026-07-06-safer-running-basics-and-running-images`

Milestone: M1 Validation and Contract Fixtures

Status: review-requested

## What Changed

M1 adds validation coverage for the future `Safer Running Basics` page without creating the page, images, prompt records, or provenance rows.

Changed surfaces:

- `tests/test_exercise_method_guidance.py`
- `tests/test_exercise_image_standard.py`
- `tools/checks/check_markdown_first.py`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- `docs/plan.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/change.yaml`

## Why

The approved spec requires `exercises/safer-running-basics.md` to use `Method type: basic_cardio_activity` and authorizes a page-specific first-batch exception for exactly six running images.

Before the running page or images are added, M1 makes those contracts enforceable:

- `basic_cardio_activity` is now active for `exercises/safer-running-basics.md`.
- The running image exception allows up to six images for that page.
- The exception is constrained to the six approved first-batch asset paths.
- A seventh image, a second muscle-attention image, or an unapproved running asset fails validation.

## Tests First

The new tests were added before the checker update.

Observed red state:

- `python3 -m unittest tests.test_exercise_method_guidance` failed with `exercise_method_inactive_type` for `exercises/safer-running-basics.md`.
- `python3 -m unittest tests.test_exercise_image_standard` failed because the running image fixture still used the default three-image limit and had no unapproved-asset finding.

After updating the checker, the targeted suites passed.

## Scope Boundaries

M1 intentionally does not create:

- `exercises/safer-running-basics.md`;
- generated running images;
- prompt records;
- `media/PROVENANCE.md` rows;
- visual-safety review;
- beginner comprehension proof.

Those remain assigned to later milestones in the active plan.

## Validation

Passed locally:

```bash
python3 -m unittest tests.test_exercise_method_guidance
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
python3 -m unittest discover -s tests
```

Final Markdown, privacy, and diff checks are recorded in the implementation handoff.

## Sources

- `specs/safer-running-basics-and-running-images.md`
- `specs/safer-running-basics-and-running-images.test.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
