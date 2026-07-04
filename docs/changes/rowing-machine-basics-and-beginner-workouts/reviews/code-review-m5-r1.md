# Code Review M5 R1: Rowing Machine Basics and Beginner Workout Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m5-r1.md`; `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`; lifecycle routing metadata
- Open blockers: none
- Next stage: explain-change
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Review record: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m5-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Review resolution required: no
- Reviewed milestone: M5
- Milestone closeout: closed
- Remaining implementation milestones: none
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Reviewed diff: `10bcff3..HEAD`
- Reviewed commits: `abf0f89 M5: add rowing media support`; `9509f39 M5: add rowing muscle attention media`
- Governing spec: `specs/rowing-machine-basics-and-beginner-workouts.md`
- Related image standard: `specs/exercise-image-standard.md`
- Active plan: `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
- Test spec: `specs/rowing-machine-basics-and-beginner-workouts.test.md`
- Manual proof: `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/media-decision.md`; `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/visual-safety-review.md`
- Validation evidence: `docs/changes/rowing-machine-basics-and-beginner-workouts/validation-ledger.md`
- Changed test: `tests/test_markdown_first_real_pages.py`

## Diff Summary

M5 adds three local generated raster support images for `exercises/rowing-machine.md`: setup, muscle attention, and movement sequence. The page now references those images with meaningful alt text, `media/PROVENANCE.md` has approved rows with exact prompt-record paths, `media/prompts/exercises/rowing-machine/` contains the prompt records, and the visual-safety review records a pass for all three images.

The milestone also updates the media decision, validation ledger, exercise-image audit inventory, active plan, change metadata, durable rationale, and one real-page regression test that checks local image references, provenance rows, page refs, approved status, and prompt-record files.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | M5 stays within R31-R36 and AC6-AC7: local images only, no borrowed screenshots or identifiable people, support-only media, provenance, prompt records, alt text, page refs, and visual-safety review. |
| Test coverage | pass | `test_rowing_machine_media_is_local_prompt_backed_and_reviewed` checks each rowing asset path, page reference, file presence, provenance row, approved status, page refs, and prompt-record path. |
| Edge cases | pass | Direct visual inspection and `manual-proof/visual-safety-review.md` cover no in-image text, no labels, no correctness marks, no brand marks, no red pain marks, and no clinical framing. |
| Error handling | pass | Markdown-first and image-standard validation fail missing local paths, missing prompt records, missing approved provenance, and unresolved page refs. |
| Architecture boundaries | pass | The change remains Markdown-first content plus local media and proof artifacts; it adds no runtime, app flow, hidden metadata source of truth, or hosted service. |
| Compatibility | pass | Existing exercise-image audit is updated for the new rowing inventory, and the rowing page uses the approved `media/prompts/exercises/rowing-machine/<asset-stem>.md` prompt-record shape. |
| Security/privacy | pass | Privacy validation over content, media metadata, specs, plans, and change evidence passed; no private reader data, training logs, secrets, or identifiable people were introduced. |
| Derived artifact currency | pass | Page refs, asset files, provenance rows, prompt records, visual-safety review, media decision, validation ledger, active plan, and audit inventory are aligned for M5. |
| Unrelated changes | pass | The reviewed diff is scoped to rowing media support, media evidence, lifecycle metadata, and the real-page media regression. |
| Validation evidence | pass | Reviewer reruns passed targeted media regression, Markdown-first checks, image tests, full unit discovery, broad Markdown-first check, privacy scan, and `git diff --check`. |

## Reviewer Validation

- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_rowing_machine_media_is_local_prompt_backed_and_reviewed`: pass, 1 test.
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media`: pass, checked 20 Markdown files.
- `python3 -m unittest discover -s tests -p 'test_*image*.py'`: pass, 14 tests.
- `python3 -m unittest discover -s tests`: pass, 121 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media`: pass, checked 27 Markdown files.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`: pass, checked 84 files.
- `git diff --check`: pass.

## No-Finding Rationale

The implementation directly addresses the follow-up request for readability and muscle-engagement support while keeping exact instruction in Markdown. The muscle-attention image uses broad regional highlights and the page retains the source-supported `## Muscles involved` text as the authoritative wording, so the image does not create a new unsupported exercise contract.

Residual risk remains that static images cannot prove every reader will understand setup, muscle attention, or stroke order perfectly. That risk is acceptable at this stage because the images are support-only, visual-safety reviewed, and backed by existing manual comprehension proof plus downstream final closeout gates.

## Handoff

M5 is closed. No implementation milestones remain. The next lifecycle stage is final closeout beginning with explain-change, followed by final verification and PR handoff. This review does not claim final verification, PR readiness, hosted CI success, or merge readiness.
