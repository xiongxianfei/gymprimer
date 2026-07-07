# Review Resolution: Safer Running Basics and High-Quality Running Images

Change ID: `2026-07-06-safer-running-basics-and-running-images`

Current milestone: M2

Status: resolved

## Findings

| Finding ID | Source review | Severity | Status | Required outcome |
|---|---|---|---|---|
| GP-SRB-M1-CR1 | `reviews/code-review-m1-r1.md` | major | resolved | Added active M1 fixture coverage for page heading, alias line, required headings, page-local sources, and shared source registration; accepted by code-review M1 R2. |
| GP-SRB-M2-CR1 | `reviews/code-review-m2-r1.md` | major | resolved | Added explicit persistent-pain routing to the required `What you should feel` route and added a direct real-page test assertion; accepted by code-review M2 R2. |

## Resolution Notes

Fixes applied:

- Added safer-running fixture page-structure tests in `tests/test_markdown_first_page_structure.py`.
- Added checker enforcement for `# Safer Running Basics`, the exact alias line, and required safer-running headings.
- Updated the safer-running image fixture so image exception tests also satisfy the page-shape contract.

Code-review M1 R2 accepted the resolution.

M2 fix applied:

- Added `persistent pain` to the `What you should feel` safety route in `exercises/safer-running-basics.md`.
- Kept the added language concise because `RED-FLAGS.md` remains the central safety route.
- Added a direct `persistent pain` assertion to the M2 real-page feel-guidance test.

Code-review M2 R2 accepted the resolution.

## Validation Evidence

Passed locally:

```bash
python3 -m unittest tests.test_markdown_first_page_structure
python3 -m unittest tests.test_exercise_method_guidance
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
python3 -m unittest discover -s tests
```

## Required Validation After Fix

```bash
python3 -m unittest tests.test_exercise_method_guidance
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
python3 -m unittest discover -s tests
python3 tools/checks/check_markdown_first.py SOURCES.md docs/proposals/2026-07-06-safer-running-basics-and-running-images.md specs/safer-running-basics-and-running-images.md specs/safer-running-basics-and-running-images.test.md docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md docs/changes/2026-07-06-safer-running-basics-and-running-images
python3 tools/checks/check_privacy.py SOURCES.md docs/proposals/2026-07-06-safer-running-basics-and-running-images.md specs/safer-running-basics-and-running-images.md specs/safer-running-basics-and-running-images.test.md docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md docs/changes/2026-07-06-safer-running-basics-and-running-images
git diff --check
```

## Sources

- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/code-review-m1-r1.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- `specs/safer-running-basics-and-running-images.test.md`
