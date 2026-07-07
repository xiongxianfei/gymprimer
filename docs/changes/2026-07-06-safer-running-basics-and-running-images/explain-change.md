# Explain Change: Safer Running Basics and High-Quality Running Images M1-M4

Change ID: `2026-07-06-safer-running-basics-and-running-images`

Milestone: M1 Validation and Contract Fixtures; M2 Markdown Page and Source Contract; M3 Governed Image Batch; M4 Comprehension Proof and Final Readiness; final holistic code review

Status: ready-for-verify

## Summary

This change adds `exercises/safer-running-basics.md` as a beginner-facing running education page, keeps `injury-free running` as search alias language rather than a promise, and publishes a governed six-image first batch with prompt records, provenance rows, visual-safety review, beginner comprehension proof, and local validation evidence.

The implementation stays Markdown-first: the page text remains authoritative for effort, progression, muscle roles, form cues, and safety routing, while generated images serve as broad visual references.

## Current Closeout State

All implementation milestones are closed.
Material code-review findings were resolved, accepted, or withdrawn through recorded review rounds.
Final holistic code-review R1 found no blocking or required-change findings and routed the change to final closeout and verification.

CI has not been observed and is not claimed.

## M4 What Changed

M4 records final milestone proof for the safer-running page and image batch before code-review.

Changed surfaces:

- `tests/test_markdown_first_real_pages.py`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/beginner-comprehension-proof.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/rollback-proof.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/validation-ledger.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- `docs/plan.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/change.yaml`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/explain-change.md`

## M4 Why

The approved spec requires beginner comprehension proof for the final published page and image set. The proof confirms that a beginner can answer what the page helps with, whether it guarantees injury-free running, how to start, what run/walk means, what effort should feel like, what the posture and landing images teach, and the required safety-route prompt. [Spec](../../../specs/safer-running-basics-and-running-images.md)

The test spec also requires rollback proof. M4 records a text-only rollback rehearsal that removes image references and safer-running provenance rows in a temporary root, then reruns Markdown-first and privacy checks without destructively editing the live page.

The validation ledger records the exact local commands and states that CI was not observed.

## M4 Tests First

The M4 proof tests were added before proof records were created.

Observed red state:

- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_rollback_proof_records_text_only_cleanup tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_validation_ledger_records_final_handoff_commands` failed because the beginner-comprehension proof, rollback proof, and validation ledger did not exist.

After adding the proof records and validation ledger, the targeted proof tests passed.

## M4 Scope Boundaries

M4 does not change the page text, generated images, prompt records, or provenance rows.

Those surfaces were implemented and reviewed in M2 and M3. M4 only records final proof and local validation evidence for the already approved page and image set.

## M4 Validation

Passed locally:

```bash
python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_rollback_proof_records_text_only_cleanup tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_validation_ledger_records_final_handoff_commands
python3 -m unittest tests.test_exercise_method_guidance
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
python3 tools/checks/check_markdown_first.py exercises/safer-running-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md
python3 tools/checks/check_privacy.py exercises/safer-running-basics.md media/PROVENANCE.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md
python3 -m unittest discover -s tests
git diff --check
```

## Final Code Review

Final holistic code-review R1 reviewed the complete branch diff from merge base `66370f1af687ca30e444b4c13376393a51239758` to `HEAD`.
It inspected the page, tests, prompt records, provenance rows, review evidence, local validation, and the six generated images.

Result: `clean-with-notes`.

No blocking or required-change findings were recorded.

The review record is `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/code-review-final-r1.md`.

## M3 What Changed

M3 adds the approved six-image first batch for `exercises/safer-running-basics.md`.

Changed surfaces:

- `exercises/safer-running-basics.md`
- `tests/test_markdown_first_real_pages.py`
- `media/exercises/safer-running-basics/`
- `media/prompts/exercises/safer-running-basics/`
- `media/PROVENANCE.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/visual-safety-review.md`
- `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- `docs/plan.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/change.yaml`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/explain-change.md`

## M3 Why

The approved spec authorizes exactly six first-batch generated images for the running page because running is dynamic, whole-body, and commonly misunderstood by beginners.

The six images cover the approved top-six concepts: posture, landing, run/walk structure, warm-up, broad muscle attention, and neutral overstride comparison.

Each generated asset has a matching prompt record and an approved provenance row, and the page references only local relative paths with meaningful alt text. The images remain broad visual references; Markdown remains the source of truth for effort, progression, form cues, muscle roles, and safety routing.

## M3 Tests First

The M3 real-page tests were added before image implementation.

Observed red state:

- `python3 -m unittest tests.test_markdown_first_real_pages` failed because the page had zero safer-running image references and no visual-safety review artifact.

After adding the image batch, prompt records, provenance rows, page references, and review evidence, the targeted suite passed. One stale M2 text-only assertion was removed because M3 replaces it with exact six-image assertions.

## M3 Scope Boundaries

M3 intentionally does not create beginner comprehension proof.

That remains assigned to M4 in the active plan.

## M3 Validation

Passed locally:

```bash
python3 -m unittest tests.test_markdown_first_real_pages
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
python3 tools/checks/check_markdown_first.py exercises/safer-running-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images
python3 tools/checks/check_privacy.py exercises/safer-running-basics.md media/PROVENANCE.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images
git diff --check
```

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
