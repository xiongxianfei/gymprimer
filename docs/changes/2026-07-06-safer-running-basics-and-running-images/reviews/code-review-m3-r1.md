# Code Review M3 R1: Safer Running Basics and High-Quality Running Images

Review date: 2026-07-07

Reviewed milestone: M3 Governed Image Batch

Review target: `76e34af M3: add safer running image batch`

Review status: changes-requested

## Review Inputs

- Diff/review surface: `git show 76e34af -- exercises/safer-running-basics.md tests/test_markdown_first_real_pages.py media/PROVENANCE.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images/visual-safety-review.md`
- Governing spec: `specs/safer-running-basics-and-running-images.md`
- Test spec: `specs/safer-running-basics-and-running-images.test.md`
- Plan: `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- Direct image inspection: all six safer-running PNG assets.
- Validation evidence reviewed: plan M3 validation notes and reviewer reruns listed below.

## Diff Summary

The implementation adds six safer-running generated raster images, exact prompt records, approved provenance rows, Markdown image references, a visual-review artifact, M3 real-page tests, and an exercise-image audit update.

The image files, prompt records, provenance rows, local relative page references, top-six purposes, one muscle-attention limit, and deferred candidates 7 through 10 align with the approved M3 image contract.

## Findings

### Finding GP-SRB-M3-CR1

- Finding ID: GP-SRB-M3-CR1
- Severity: major
- Location: `specs/safer-running-basics-and-running-images.test.md:238`, `specs/safer-running-basics-and-running-images.test.md:240`, `tests/test_markdown_first_real_pages.py:730`, `tests/test_markdown_first_real_pages.py:754`, `docs/plans/2026-07-06-safer-running-basics-and-running-images.md:163`, `docs/changes/2026-07-06-safer-running-basics-and-running-images/visual-safety-review.md:1`
- Evidence: The approved test spec names `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/visual-safety-review.md` as the expected M3 visual-review evidence path. The implementation instead creates `docs/changes/2026-07-06-safer-running-basics-and-running-images/visual-safety-review.md`, and the M3 tests assert that change-root path. This makes the production evidence and automated proof diverge from the approved proof map. [Test spec][local-code-review-m3-r1-test-spec]
- Required outcome: The visual-review evidence path and the automated tests must match the approved proof map, or the proof map must be amended through the proper upstream review before M3 can close.
- Safe resolution path: Prefer moving the visual-review artifact under `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/visual-safety-review.md`, updating the M3 tests and plan references to that path, and rerunning the M3 validation commands. If the change-root path is intentional, amend the approved test spec first and route that amendment through the required review gate before rereviewing M3.
- needs-decision rationale: none

Detailed finding record: `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/findings/GP-SRB-M3-CR1.md`

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | concern | R7 through R10 are otherwise satisfied by the six exact assets, one muscle-attention image, prompt records, provenance rows, and visual criteria, but the M3 evidence path diverges from the approved test spec. |
| Test coverage | concern | M3 tests cover the six image refs, prompt records, provenance rows, top-10 ranking, and visual criteria, but they assert the unapproved visual-review path. |
| Edge cases | pass | Tests cover no extra first-batch images, candidates 7 through 10 deferred, one muscle-attention image, local refs, and exact provenance mapping. |
| Error handling | pass | No runtime error handling changed; rollback remains document-scoped through page refs, prompt records, and provenance rows. |
| Architecture boundaries | pass | The change stays within Markdown, local media, prompt records, provenance, tests, and change evidence. |
| Compatibility | concern | Workflow evidence placement is inconsistent with the approved proof map, which can mislead later review and final closeout. |
| Security/privacy | pass | No secrets, private data, identifiable people, brand marks, hosted app, auth, or logging changes were observed. |
| Derived artifact currency | concern | Page refs, prompt records, provenance, and audit rows are current, but the visual-review artifact path and tests are not synchronized with the proof map. |
| Unrelated changes | pass | The diff is scoped to M3 image assets, media records, page refs, tests, audit evidence, and workflow handoff artifacts. |
| Validation evidence | concern | Reviewer reruns passed, but the current passing tests encode the path mismatch described in GP-SRB-M3-CR1. |

## Validation Rerun

Reviewer reran:

```bash
python3 -m unittest tests.test_markdown_first_real_pages
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
python3 tools/checks/check_markdown_first.py exercises/safer-running-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md
python3 tools/checks/check_privacy.py exercises/safer-running-basics.md media/PROVENANCE.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md
python3 -m unittest discover -s tests
git diff --check
```

All commands passed locally during review. The passing result does not resolve GP-SRB-M3-CR1 because current tests assert the path that conflicts with the approved proof map.

## Residual Risks

If this advances without resolution, later reviewers may look for the M3 visual-review evidence at the approved proof-map path and miss the artifact that the current tests accepted elsewhere.

## Milestone Handoff

M3 should move to `resolution-needed`.

Required next stage is review-resolution for GP-SRB-M3-CR1.

This review does not claim branch readiness, PR readiness, final verification, or CI success.

## Sources

- `specs/safer-running-basics-and-running-images.md`
- `specs/safer-running-basics-and-running-images.test.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/findings/GP-SRB-M3-CR1.md`

[local-code-review-m3-r1-test-spec]: ../../../specs/safer-running-basics-and-running-images.test.md
