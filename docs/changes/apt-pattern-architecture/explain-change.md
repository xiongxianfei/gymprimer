# Explain Change: APT Pattern Architecture

## Summary

The APT follow-up turns the anterior pelvic tilt page into the reusable
Responsible Breadth pattern-page proof: it links beginner pain points to an
observable pattern, explains core movement contributors, routes red flags before
exercise options, links only to existing exercise pages, and keeps generated
raster media as support assets with provenance.

After code-review R1 found the reusable pattern template was stale, the
resolution updated `docs/templates/pattern-page.md` and added a focused template
test so future pattern pages start from the same contract the APT page now
demonstrates.

This artifact explains the reviewed diff. It does not claim final verification,
CI success, branch readiness, PR readiness, or Done.

## Problem

The first APT page was structurally compliant but too thin for the intended
pattern-page journey. It explained APT and uncertainty, but it did not yet give
a repository-native path from a beginner's entry question to contributor-level
education and bounded exercise options.

The follow-up implementation solved that, but code-review R1 found a second
problem: the reusable pattern template still pointed authors to
`../about/red-flags.md` and old section names, while the current repository uses
root `RED-FLAGS.md` and the Responsible Breadth pattern architecture headings.

## Decision Trail

| Source | Decision or requirement | Implementation effect |
| --- | --- | --- |
| `docs/proposals/2026-06-29-responsible-breadth.md` | Expand GymPrimer only as static, citation-backed education with red-flag routing. | APT remains education, not diagnosis, treatment, correction promise, or a personal routine. |
| `specs/responsible-breadth.md` R57-R63 | Pattern pages must move from user pain point to observable pattern, core contributors, and exercise options; exercise previews must link to existing exercise pages and include fix reason, used muscles, and important note. | APT was expanded with the required reader journey and linked only to real exercise pages. |
| `specs/responsible-breadth.md` R29-R35f | Generated raster media may support expanded pages only with provenance and support-only framing. | Pattern and exercise images remain subordinate to Markdown text and cited sources, with rows in `media/PROVENANCE.md`. |
| `specs/responsible-breadth.test.md` RB-T21 | The APT page and linked exercise pages are the integration proof for pattern-page architecture. | Tests now inspect the real APT page, linked exercise targets, and exercise image references. |
| `specs/responsible-breadth.test.md` RB-T22 | Expanded raster media-purpose validation must cover pattern alignment, condition anatomy context, and exercise support. | Checker/test coverage was extended for expanded media-purpose behavior. |
| `docs/plans/2026-06-29-responsible-breadth.md` | The APT follow-up does not reopen original M1-M4 scope; it is a follow-up before PR handoff resumes. | The plan now records the follow-up review loop and routes to verify after this explanation. |
| `docs/changes/apt-pattern-architecture/reviews/code-review-r1.md` | CR-APT-1 required the pattern template to match current headings and normalized red-flags path. | The template and focused template test were updated, then accepted by code-review R2. |

## Diff Rationale By Area

| File | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| `patterns/anterior-pelvic-tilt.md` | Expanded the page into the full pattern journey: entry points, definition, observation-not-diagnosis methods, contributors, uncertainty, bounded help menu, and professional routing. | Demonstrate R57-R61 on the real first pattern page. | Responsible Breadth R57-R61, RB-T21. | `test_apt_pattern_page_follows_reader_journey_architecture`; Markdown-first checker. |
| `exercises/dead-bug.md`, `exercises/plank.md`, `exercises/bird-dog.md`, `exercises/glute-bridge.md`, `exercises/hip-hinge.md`, `exercises/kneeling-hip-flexor-stretch.md` | Added standalone exercise pages for every APT support option. | R62 requires pattern exercise previews to link only to existing exercise pages unless draft-only. | Responsible Breadth R61-R62, RB-T21. | `test_anterior_pelvic_tilt_solution_links_have_real_targets`. |
| `media/PROVENANCE.md` and exercise/pattern raster assets | Added provenance rows for generated support images and removed duplicate pattern-page preview copies after review. | Generated raster media must remain support-only and provenance-backed; duplicate preview images were unnecessary when exercise pages own sequence visuals. | Responsible Breadth R29-R35f, RB-T22. | Media-purpose tests and visual-media proof. |
| `tools/checks/check_markdown_first.py` | Added pattern architecture validation and expanded media-purpose validation. | Make missing exercise targets, missing preview annotations, and wrong media-purpose mappings fail deterministically. | RB-T21, RB-T22. | Responsible Breadth tests passed. |
| `tests/test_responsible_breadth_m1.py` | Added integration checks for APT links/images, exercise preview annotations, missing targets, media-purpose failures, and the later CR-APT-1 template regression. | Prove the real page and the reusable template now match the amended contract. | RB-T21, RB-T22, CR-APT-1. | Targeted test and full Responsible Breadth test discovery passed. |
| `docs/templates/pattern-page.md` | Updated the reusable template to use `../RED-FLAGS.md` and the current pattern headings: `Why beginners come to this page`, `Working definition`, `How to notice this in yourself`, `The core reason`, and `What commonly helps`. | Resolve CR-APT-1 so future pages do not start from stale path/heading guidance. | Code-review R1 finding CR-APT-1; Responsible Breadth R57-R61. | Focused template assertion passed; code-review R2 accepted. |
| `docs/changes/apt-pattern-architecture/review-resolution.md` | Recorded SR-APT-SPEC-1 and CR-APT-1 dispositions, validation, and code-review R2 acceptance. | Preserve material-finding traceability before downstream verification. | Code-review R1/R2; spec-review R1/R2. | Privacy check over review artifacts passed. |
| `docs/changes/apt-pattern-architecture/review-log.md`, `change.yaml`, `docs/plan.md`, `docs/plans/2026-06-29-responsible-breadth.md` | Updated lifecycle routing through code-review R1, review-resolution, code-review R2, explain-change, and verify handoff. | Keep the workflow state consistent with the reviewed finding and its closure. | Workflow guide, plan current handoff summary. | State-sync inspection and `git diff --check`. |

## Tests Added Or Changed

| Test or proof | What it proves | Why this level is appropriate |
| --- | --- | --- |
| `test_apt_pattern_page_follows_reader_journey_architecture` | The real APT page contains the required pattern journey headings and passes the checker with linked exercises. | Integration is needed because RB-T21 names the real APT page as proof. |
| `test_anterior_pelvic_tilt_solution_links_have_real_targets` | Every APT exercise option links to an existing exercise page and each linked exercise page has a raster example. | Directly covers R62 and the exercise-image support path. |
| `test_pattern_exercise_preview_requires_annotation_and_existing_target` | Missing `Used muscles` and missing exercise targets fail. | Negative fixture coverage prevents structural compliance without useful previews. |
| `test_pattern_alignment_media_requires_pattern_alignment_purpose` | Pattern alignment images cannot use the old generic media purpose. | Directly covers RB-T22 and R35c-R35d. |
| `test_condition_anatomy_media_must_not_imply_diagnosis` | Condition anatomy media cannot imply diagnosis, pathology, or treatment. | Covers the expanded media-purpose safety boundary. |
| Focused template assertions in `test_responsible_breadth_templates_exist_and_carry_contract` | The pattern template requires `../RED-FLAGS.md` and current headings, and rejects stale path/headings. | This is the smallest direct regression proof for CR-APT-1. |

## Validation Evidence Available Before Final Verify

Latest validation recorded during CR-APT-1 resolution and code-review R2:

- `python3 -m unittest tests.test_responsible_breadth_m1.ResponsibleBreadthM2Test.test_responsible_breadth_templates_exist_and_carry_contract`
  - Result: passed.
- `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - Result: passed, 20 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`
  - Result: passed, checked 18 Markdown files.
- `python3 tools/checks/check_privacy.py docs/templates/pattern-page.md tests/test_responsible_breadth_m1.py docs/changes/apt-pattern-architecture/review-resolution.md`
  - Result: passed, checked 3 files.
- `python3 tools/checks/check_privacy.py docs/changes/apt-pattern-architecture docs/plan.md docs/plans/2026-06-29-responsible-breadth.md docs/templates/pattern-page.md tests/test_responsible_breadth_m1.py`
  - Result: passed, checked 18 files.
- `git diff --check`
  - Result: passed.

Validation limitation: checking all `docs/templates` with
`check_markdown_first.py` still fails on unrelated template placeholders and
old template debt. The CR-APT-1 fix uses a focused template assertion instead.

CI was not observed.

## Review Resolution Summary

Material findings are closed:

- `SR-APT-SPEC-1`: resolved by spec-review R2 after adding deterministic
  expanded-page `media_purpose` values and boundaries.
- `CR-APT-1`: resolved by code-review R2 after the pattern template and focused
  template test were updated.

See `docs/changes/apt-pattern-architecture/review-resolution.md` for the full
dispositions. `docs/changes/apt-pattern-architecture/reviews/code-review-r2.md`
accepted the CR-APT-1 resolution with no material findings.

## Alternatives Rejected

- Leaving the old `../about/red-flags.md` template path was rejected because
  repository layout normalization made root `RED-FLAGS.md` canonical.
- Updating the APT page during CR-APT-1 resolution was rejected because the
  template fix did not reveal a concrete APT page inconsistency.
- Adding duplicate preview images back to the pattern page was rejected because
  exercise pages own sequence visuals and the pattern page can link to those
  exercise pages textually.
- Treating all `docs/templates` checker failures as in-scope was rejected
  because unrelated templates still contain placeholders and older template debt.

## Scope Control

The follow-up preserves the project refusals:

- no diagnosis;
- no individualized medical advice;
- no treatment plan;
- no rehabilitation protocol;
- no posture-correction promise;
- no personalized program;
- no runtime symptom checker, app, account system, or generated source of truth.

Markdown remains the source of truth. Generated raster media remains a support
asset with provenance and cannot become evidence for anatomy, technique, safety,
diagnosis, treatment, or programming claims.

## Risks And Follow-Ups

- CI has not been observed.
- Final verification must be refreshed because the prior verify report predates
  the CR-APT-1 template/test/review-resolution diff.
- Other templates still have unrelated placeholder/template-debt issues when run
  through the broad Markdown checker; those are not part of CR-APT-1 but should
  be handled in a separate scoped change before broad template validation is
  required.

## Readiness

Ready for `verify`. Not branch-ready, PR-ready, or Done until the verify stage
updates validation evidence and reports residual risk.
