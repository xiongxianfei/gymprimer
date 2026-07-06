# Code Review M1 R1: Safer Running Basics and High-Quality Running Images

Review date: 2026-07-06

Reviewed milestone: M1 Validation and Contract Fixtures

Review target: `cf1add2 M1: add safer running validation contract`

Review status: changes-requested

## Review Inputs

- Diff/review surface: `git diff HEAD^..HEAD -- tools/checks/check_markdown_first.py tests/test_exercise_method_guidance.py tests/test_exercise_image_standard.py docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/changes/2026-07-06-safer-running-basics-and-running-images`
- Governing spec: `specs/safer-running-basics-and-running-images.md`
- Test spec: `specs/safer-running-basics-and-running-images.test.md`
- Plan: `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- Validation evidence reviewed: plan M1 validation notes and rerun targeted commands listed below.

## Diff Summary

The implementation adds `basic_cardio_activity` scope for `exercises/safer-running-basics.md`, adds a six-image exception for that page, restricts the exception to the six approved first-batch image paths, and adds fixture tests for the method and image exception behavior.

It also commits the accepted proposal/spec/plan/test-spec workflow artifacts and marks M1 as `review-requested`.

## Findings

### Finding GP-SRB-M1-CR1

- Finding ID: GP-SRB-M1-CR1
- Severity: major
- Location: `tests/test_exercise_method_guidance.py:178`, `tests/test_exercise_image_standard.py:343`, `docs/plans/2026-07-06-safer-running-basics-and-running-images.md:45`, `docs/plans/2026-07-06-safer-running-basics-and-running-images.md:48`, `specs/safer-running-basics-and-running-images.test.md:34`
- Evidence: M1 requires tests for method coverage, the image exception, exact image paths, required page headings, alias treatment, image alt text, and source registration. The implementation adds the method test at `tests/test_exercise_method_guidance.py:178` and image exception tests at `tests/test_exercise_image_standard.py:343`, but `rg "safer-running|Safer Running|injury-free|Also searched|source registration" tests tools/checks` finds no implementation-side test or checker assertion for the required H1, alias line, alias boundary, required sections, or source registration. The test spec explicitly assigns T1 and T2 to M1/M2 and requires automated coverage for `# Safer Running Basics`, the alias line, required headings, `## Sources`, and the `# Injury-Free Running` title rejection.
- Required outcome: M1 must include active automated coverage for the required safer-running page shape and alias boundary, or the approved plan/test-spec must be revised through the proper upstream workflow to defer those proof obligations out of M1.
- Safe resolution path: Add focused M1 tests that validate a fixture or helper-rendered safer-running page contract for the approved H1, alias line, required headings, page-local sources, and rejection of `# Injury-Free Running`; include source-registration proof if it is not already covered by the checker fixture. Keep production page creation deferred to M2 unless the plan is revised. Rerun the M1 targeted validation commands and return M1 to `review-requested`.
- needs-decision rationale: none

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | concern | Method and image-exception parts align with R3, R7, and R8, but M1 does not cover test-spec T1/T2 page shape and alias proof. |
| Test coverage | concern | Added method and image tests pass, but required page heading, alias, required-section, and source-registration tests are absent. |
| Edge cases | concern | Seventh image, second muscle-attention image, and unapproved asset are covered; invalid page title/alias boundary is not covered. |
| Error handling | pass | Checker emits deterministic `exercise_image_count_exceeded`, `exercise_muscle_attention_limit`, and `exercise_image_unapproved_exception_asset` findings for tested invalid image states. |
| Architecture boundaries | pass | The change stays within the existing Markdown-first checker and tests; architecture assessment recorded `architecture-not-required`. |
| Compatibility | pass | Existing Baduanjin/Tai Chi exception behavior remains covered by existing tests, and broad page tests pass. |
| Security/privacy | pass | No secrets or private data observed in the diff; privacy checker passed for reviewed artifacts. |
| Derived artifact currency | pass | No generated public artifacts are introduced by M1. |
| Unrelated changes | pass | The implementation and workflow artifacts are scoped to the safer-running change. |
| Validation evidence | pass | Reviewer reran targeted M1 commands successfully; validation does not remove the coverage finding. |

## Validation Rerun

Reviewer reran:

```bash
python3 -m unittest tests.test_exercise_method_guidance
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
```

Both commands passed locally during review.

## Residual Risks

The current implementation could advance to M2 without automated proof that the future page uses the approved title, alias framing, required headings, and source-registration behavior. That is exactly the gap captured by GP-SRB-M1-CR1.

## Milestone Handoff

M1 should move to `resolution-needed`. Required next stage is review-resolution for GP-SRB-M1-CR1.

This review does not claim branch readiness, PR readiness, final verification, or CI success.
