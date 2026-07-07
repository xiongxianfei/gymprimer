# Code Review M2 R1: Safer Running Basics and High-Quality Running Images

Review date: 2026-07-06

Reviewed milestone: M2 Markdown Page and Source Contract

Review target: `31ca499 M2: add safer running Markdown page`

Review status: changes-requested

## Review Inputs

- Diff/review surface: `git show 31ca499 -- exercises/safer-running-basics.md tests/test_markdown_first_real_pages.py docs/changes/2026-07-06-safer-running-basics-and-running-images/source-audit.md docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md docs/changes/2026-07-06-safer-running-basics-and-running-images`
- Governing spec: `specs/safer-running-basics-and-running-images.md`
- Test spec: `specs/safer-running-basics-and-running-images.test.md`
- Plan: `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- Validation evidence reviewed: plan M2 validation notes and reviewer reruns listed below.

## Diff Summary

The implementation adds `exercises/safer-running-basics.md` as a text-only beginner running page with the approved H1, alias line, required sections, `Method type: basic_cardio_activity`, page-local running sources, run/walk progression, warm-up, form cues, muscle guidance, common mistakes, variants, and safety routing.

It also adds M2 real-page tests, records `source-audit.md`, updates the current exercise-image audit inventory with the new zero-image page, and moves workflow metadata to `code-review` / `M2 review-requested`.

## Findings

### Finding GP-SRB-M2-CR1

- Finding ID: GP-SRB-M2-CR1
- Severity: major
- Location: `specs/safer-running-basics-and-running-images.md:120`, `exercises/safer-running-basics.md:94`, `exercises/safer-running-basics.md:114`, `exercises/safer-running-basics.md:150`, `tests/test_markdown_first_real_pages.py:578`
- Evidence: Spec R5.4 requires the `What you should feel` section to route chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, weakness, worsening symptoms, or persistent pain to the project safety path and appropriate professional help. The page routes chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, weakness, symptoms that worsen, and symptoms that do not settle, but it never names persistent pain. The M2 real-page test asserts the other required symptom terms and the `RED-FLAGS.md` route, but it also omits persistent pain, so the requirement gap is not protected. [Spec][local-code-review-m2-r1-spec]
- Required outcome: The M2 page and tests must explicitly cover persistent pain routing in the safety-facing text required by R5.4. [Spec][local-code-review-m2-r1-spec]
- Safe resolution path: Add persistent pain to the `What you should feel` safety sentence and the related `Stop if` or `Safety notes` route as appropriate, keeping the Mayo citation and `RED-FLAGS.md` link on the safety line. Add a direct assertion for `persistent pain` in `test_safer_running_broad_muscle_feel_and_stop_guidance` or an equivalent M2 real-page test. Rerun `python3 -m unittest tests.test_markdown_first_real_pages`, the scoped Markdown/privacy checks for the page and change directory, and the full unittest suite before returning M2 to `review-requested`. [Spec][local-code-review-m2-r1-spec]
- needs-decision rationale: none

Detailed finding record: `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/findings/GP-SRB-M2-CR1.md`

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | concern | The page satisfies R1, R2, R3, R4, most of R5, R6, and R11 for M2, but R5.4's named persistent-pain route is missing from the page text. |
| Test coverage | concern | Real-page tests cover title, alias, required headings, method, broad muscle guidance, most symptom-route terms, and source registration, but omit persistent pain from the R5.4 term list. |
| Edge cases | concern | The test directly rejects `# Injury-Free Running` and confirms no image references in M2; the persistent-pain route edge case is not covered. |
| Error handling | pass | No runtime error handling changed; checker validation still covers invalid method/muscle/source states and the M2 page passes the checker. |
| Architecture boundaries | pass | The change stays within Markdown content, tests, source audit, and workflow artifacts; architecture assessment remains `architecture-not-required`. |
| Compatibility | pass | The implementation keeps generated images, prompt records, and provenance deferred to M3 and records the current exercise-image audit row needed by existing inventory tests. |
| Security/privacy | pass | No secrets, private data, user-submitted media, hosted app, auth, or logging changes were observed. |
| Derived artifact currency | pass | The source audit and exercise-image audit inventory were updated for the new current page; no generated raster assets or provenance rows are introduced in M2. |
| Unrelated changes | pass | The diff is scoped to the safer-running M2 page, tests, audit evidence, current image-audit inventory, and workflow handoff artifacts. |
| Validation evidence | concern | Reviewer reruns passed, but they also demonstrate that current validation does not catch the missing persistent-pain requirement. |

## Validation Rerun

Reviewer reran:

```bash
python3 -m unittest tests.test_markdown_first_real_pages
python3 tools/checks/check_markdown_first.py exercises/safer-running-basics.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-safer-running-basics-and-running-images
```

Both commands passed locally during review. The passing result does not resolve GP-SRB-M2-CR1 because the missing `persistent pain` term is a spec-fidelity gap not currently asserted.

## Residual Risks

If this advances without resolution, the page would omit one symptom category explicitly named by the approved safety-routing requirement, and the regression tests would not prevent that omission from recurring.

## Milestone Handoff

M2 should move to `resolution-needed`.

Required next stage is review-resolution for GP-SRB-M2-CR1.

This review does not claim branch readiness, PR readiness, final verification, or CI success.

## Sources

- `specs/safer-running-basics-and-running-images.md`
- `specs/safer-running-basics-and-running-images.test.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/findings/GP-SRB-M2-CR1.md`

[local-code-review-m2-r1-spec]: ../../../specs/safer-running-basics-and-running-images.md
