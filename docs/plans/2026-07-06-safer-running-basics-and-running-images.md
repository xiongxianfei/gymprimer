# Plan: Safer Running Basics and High-Quality Running Images

Status: active

Plan lifecycle state: active

Change ID: `2026-07-06-safer-running-basics-and-running-images`

Proposal: `docs/proposals/2026-07-06-safer-running-basics-and-running-images.md`

Spec: `specs/safer-running-basics-and-running-images.md`

Architecture assessment: `docs/changes/2026-07-06-safer-running-basics-and-running-images/architecture-assessment.md`

Review log: `docs/changes/2026-07-06-safer-running-basics-and-running-images/review-log.md`

## Current Handoff Summary

Current milestone: M2

Current state: review-requested

Review status: proposal-review R1 approved; spec-review R1 approved; architecture assessment recorded `architecture-not-required`; plan-review R1 approved; test-spec-review R1 approved; code-review M1 R1 changes-requested; GP-SRB-M1-CR1 resolved; code-review M1 R2 clean-with-notes; code-review M2 R1 changes-requested for GP-SRB-M2-CR1; GP-SRB-M2-CR1 resolved pending rereview.

Next required gate: code-review M2 rereview.

Implementation status: M1 closed; M2 review-resolution applied; M3 not started.

Final closeout status: not ready.

## Scope

This plan implements the approved spec for a static beginner running page and its governed six-image first batch.

The implementation MUST NOT add a hosted app, adaptive coaching, video, animation, race plan, individualized program, or condition-specific pain-care page.

## Milestones

### M1. Validation and Contract Fixtures

Goal: make the existing validation surface able to enforce the approved page and media contract before adding production content.

Tasks:

- Add or update tests for `basic_cardio_activity` coverage on the safer-running page.
- Add or update tests for the page-specific six-image exception.
- Add or update tests for the exact six required asset paths, prompt-record paths, and provenance rows.
- Add or update tests for required page headings, alias treatment, image alt text, and source registration.
- Add fixtures only when needed to prove the checker behavior before the real page exists.

Acceptance evidence:

- Failing tests demonstrate the missing safer-running page and media contract before production content is added.
- The tests trace to R1 through R12 in the approved spec.

Progress:

- State: closed.
- Added a `basic_cardio_activity` path-scope test for `exercises/safer-running-basics.md`.
- Added fixture tests proving the six approved running image paths pass with the page-specific exception.
- Added fixture tests proving a seventh running image, a second muscle-attention image, and an unapproved running asset fail.
- Activated `basic_cardio_activity` validation for `exercises/safer-running-basics.md`.
- Added the page-specific six-image exception and allowed first-batch asset set to the Markdown-first checker.
- Code-review M1 R1 recorded GP-SRB-M1-CR1: M1 still needs required page heading, alias-boundary, required-section, and source-registration test coverage or an upstream plan/test-spec revision.
- Review-resolution added fixture-backed page contract tests for the approved H1, alias line, required headings, page-local source definitions, and shared source registration.
- Review-resolution added checker enforcement for the safer-running title, alias line, and required sections.
- Review-resolution updated the safer-running image fixture so image-exception tests continue to exercise a valid page shape.
- Code-review M1 R2 accepted the review-resolution and closed M1.

Tests-first evidence:

- `python3 -m unittest tests.test_exercise_method_guidance` failed before the checker update with `exercise_method_inactive_type` for `exercises/safer-running-basics.md`.
- `python3 -m unittest tests.test_exercise_image_standard` failed before the checker update because the running fixture still used the default three-image limit and lacked the new unapproved-asset finding.

Validation notes:

- `python3 -m unittest tests.test_exercise_method_guidance` passed: 20 tests.
- `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed: 67 tests.
- `python3 -m unittest discover -s tests` passed: 201 tests.
- Review-resolution validation passed: `python3 -m unittest tests.test_markdown_first_page_structure`, `python3 -m unittest tests.test_exercise_method_guidance`, `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages`, and `python3 -m unittest discover -s tests`.
- Artifact Markdown, privacy, and diff checks are recorded in the M1 handoff.

Decisions and discoveries:

- M1 stays validation-only. It does not create `exercises/safer-running-basics.md`, generated images, prompt records, provenance rows, visual review, or beginner comprehension proof.
- The image exception is path-scoped to `exercises/safer-running-basics.md` and stricter than the generic exception: it allows only the six approved first-batch asset paths.
- Existing Baduanjin and Tai Chi image tests remain unchanged and continue to pass.

### M2. Markdown Page and Source Contract

Goal: add `exercises/safer-running-basics.md` as a source-backed beginner cardio page before image generation is treated as accepted.

Tasks:

- Create the page with the approved H1, alias line, method type, and required sections.
- Write beginner-facing text for run/walk, easy effort, rest days, warm-up, gradual loading, form cues, muscle roles, common mistakes, variants, and safety routing.
- Keep `injury-free running` as alias/search language only.
- Keep strength guidance as general capacity support, not guaranteed injury prevention.
- Add page-local sources and any required `SOURCES.md` registrations.
- Link to `RED-FLAGS.md` from safety-facing text.

Acceptance evidence:

- Page-level checker passes for section structure, source coverage, privacy, and safety boundaries.
- Tests from M1 that can pass without final images now pass.

Progress:

- State: review-requested.
- Added `exercises/safer-running-basics.md` with the approved H1, alias line, required sections, and `Method type: basic_cardio_activity`.
- Added beginner-facing run/walk, easy-effort, rest-day, warm-up, progression, form-cue, muscle-role, common-mistake, variant, and safety-routing guidance.
- Kept `injury-free running` as alias/search language and stated that no page can guarantee injury-free running.
- Added page-local source definitions for all cited running sources already registered in `SOURCES.md`.
- Added `docs/changes/2026-07-06-safer-running-basics-and-running-images/source-audit.md`.
- Added real-page M2 tests for the page shape, method contract, muscle/feel route guidance, source IDs, and source audit.
- Updated the exercise-image M4 inventory audit with the new text-only running page because its test covers every current exercise page.
- Code-review M2 R1 recorded GP-SRB-M2-CR1: M2 omits the R5.4 persistent-pain safety-routing term from the page and real-page tests.
- Review-resolution added concise persistent-pain routing to `What you should feel` and a direct real-page test assertion.

Tests-first evidence:

- `python3 -m unittest tests.test_markdown_first_real_pages` failed before production content with missing `exercises/safer-running-basics.md` and missing source-audit artifact.

Validation notes:

- `python3 -m unittest tests.test_markdown_first_real_pages` passed: 44 tests.
- `python3 tools/checks/check_markdown_first.py exercises/safer-running-basics.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-safer-running-basics-and-running-images` passed.
- `python3 tools/checks/check_privacy.py exercises/safer-running-basics.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-safer-running-basics-and-running-images` passed.
- `python3 -m unittest discover -s tests` passed: 209 tests.

Decisions and discoveries:

- M2 remains text-only. It does not create generated images, prompt records, provenance rows, visual review, or beginner comprehension proof.
- The full test suite required the existing exercise-image audit to list the new current exercise page; the added row records zero current images and defers the six-image batch to M3.

### M3. Governed Image Batch

Goal: add the six approved generated images with prompt records, provenance, page references, and visual-safety evidence.

Tasks:

- Prepare exact prompts for the six approved assets.
- Generate or add only the approved six raster files under `media/exercises/safer-running-basics/`.
- Add prompt records under `media/prompts/exercises/safer-running-basics/`.
- Add approved provenance rows in `media/PROVENANCE.md`.
- Reference the images from the page using local relative paths and meaningful alt text.
- Record manual visual-safety review evidence under the change directory.

Acceptance evidence:

- Every referenced image has a prompt record and provenance row.
- Visual-safety review confirms no in-image text, labels, badges, red pain marks, medical framing, logos, identifiable people, or correct/wrong framing.
- The page publishes no first-batch image beyond the six approved paths.

### M4. Comprehension Proof and Final Readiness

Goal: prove that the page and image set meet the beginner education goal and are ready for review.

Tasks:

- Record beginner comprehension proof under the change directory.
- Confirm the proof covers the questions required by R12.3.
- Run the full validation command set.
- Update the plan handoff summary, review log, and any change evidence.
- Hand off to code-review with exact command outputs summarized.

Acceptance evidence:

- Beginner proof shows the reader understands what the page can and cannot promise, how to start, what run/walk means, what effort should feel like, what the posture and landing images teach, and what would make them stop or seek help. [Mayo Clinic][mayo-exercise-chronic-disease]
- All local validation commands pass or any gap is explicitly recorded.

## Validation Commands

Run these during implementation as the relevant files come into existence:

```bash
python3 -m unittest tests.test_exercise_method_guidance
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
python3 -m unittest discover -s tests
python3 tools/checks/check_markdown_first.py exercises/safer-running-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images
python3 tools/checks/check_privacy.py exercises/safer-running-basics.md media/PROVENANCE.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images
git diff --check
```

For workflow-artifact-only validation before implementation, run the scoped checks listed in the test spec.

## M1 Handoff

State: closed

Implemented surfaces:

- `tools/checks/check_markdown_first.py`
- `tests/test_exercise_method_guidance.py`
- `tests/test_exercise_image_standard.py`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/explain-change.md`

Unchanged with rationale:

- `exercises/safer-running-basics.md`: deferred to M2 by plan.
- `media/exercises/safer-running-basics/`: deferred to M3 by plan.
- `media/prompts/exercises/safer-running-basics/`: deferred to M3 by plan.
- `media/PROVENANCE.md`: deferred to M3 by plan.
- Visual-safety review and beginner comprehension proof: deferred to M3 and M4 by plan.

Ready for: implementation M2.

## M2 Handoff

State: review-requested

Implemented surfaces:

- `exercises/safer-running-basics.md`
- `tests/test_markdown_first_real_pages.py`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/source-audit.md`
- `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/explain-change.md`

Unchanged with rationale:

- `media/exercises/safer-running-basics/`: deferred to M3 by plan.
- `media/prompts/exercises/safer-running-basics/`: deferred to M3 by plan.
- `media/PROVENANCE.md`: deferred to M3 by plan.
- Visual-safety review: deferred to M3 by plan.
- Beginner comprehension proof: deferred to M4 by plan.

Ready for: code-review M2 rereview.

## Recovery

If image generation fails review, remove failed page references, prompt records, and provenance rows for those images before handoff.

If the six-image batch is too dense, keep the highest-priority approved images and record the reduction in review evidence.

If content drifts toward individualized programming or condition-specific pain care, remove that content and return to the approved beginner education contract.

## Risks

| Risk | Mitigation |
|---|---|
| The title implies a guarantee | Use `Safer Running Basics` as H1 and keep `injury-free running` only as alias text. |
| The page becomes a race plan | Keep progression general and avoid performance programming. |
| Images add unsupported claims | Keep Markdown as source of truth and require prompt records, provenance, alt text, and manual review. |
| Six images exceed the normal default | Enforce the page-specific exception and exact six approved paths. |
| Validation cannot enforce the media contract | Add focused tests/checker coverage in M1 before production content. |

## Sources

- `specs/safer-running-basics-and-running-images.md`
- `docs/proposals/2026-07-06-safer-running-basics-and-running-images.md`
- [Mayo Clinic exercise and chronic disease guidance][mayo-exercise-chronic-disease]

[mayo-exercise-chronic-disease]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-and-chronic-disease/art-20046049
