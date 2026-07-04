# Explain Change: Rowing Machine Basics and Beginner Workout Guidance

## Status

complete

## Summary

This change adds a beginner-facing `exercises/rowing-machine.md` page, narrowly
activates `basic_cardio_equipment` validation for that page, adds source-backed
rowing technique and safety content, records manual proof, and adds three local
generated raster support images for setup, muscle attention, and stroke
sequence.

The reason for the change is that the rowing machine is common gym equipment
but beginner use depends on technique. The implementation teaches setup,
stroke order, easy beginner effort, broad muscle engagement, stop conditions,
and static examples while keeping GymPrimer Markdown-first, citation-backed,
and outside personalized coaching or clinical advice.

## Problem

GymPrimer did not have a direct place to teach rower setup, damper meaning,
stroke sequence, beginner effort, broad muscles involved, or rower-specific
stop conditions. The approved direction was to treat rowing as skill-based
cardio equipment: technique first, conditioning second.

## Decision Trail

| Stage | Decision | Resulting implementation |
| --- | --- | --- |
| Proposal | Add `exercises/rowing-machine.md` instead of a principle-only page or rowing program. | M2 adds one static Markdown exercise page and avoids a multi-week plan. |
| Spec | Requirements R1-R40 define the page, method type, sources, safety, media, and non-goals. | M1-M5 implement the page, validation, proof, and images within those bounds. |
| Architecture | Keep Markdown as source of truth; allow only necessary local support media with provenance. | No runtime app, database, user flow, hosted service, or hidden metadata source was added. |
| Plan | Implement in M1-M5: method boundary, page/source index, manual proof/media decision, validation ledger, follow-up media. | Each milestone was implemented and closed by code-review. |
| Review findings | PR-RMB-1, TSR-RMB-1, and CR-RMB-M2-1 were resolved. | Prompt-record paths, manual-proof metadata, and safety source support were corrected before closeout. |

Key requirement links:

- R1-R14: page location, Markdown readability, required sections, setup,
  movement sequence, damper, broad muscles, and educational wording.
- R15-R22 and R39-R40: scoped `basic_cardio_equipment` method validation and
  static beginner examples.
- R23-R30: weekly activity, safety routing, page-local source support, and
  source-index discipline.
- R31-R36: local support-only media, generated-raster provenance, prompt
  records, alt text, page refs, and visual-safety review.
- R37-R38: no hosted app, tracker, diagnosis, rehab, medical advice, or
  personalized coaching.

## Diff Rationale By Area

| File or area | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| `exercises/rowing-machine.md` | Adds the rowing-machine page with setup, muscles, movement, beginner method, safety, examples, and sources. | Satisfies the beginner education goal and R1-R30. | Proposal, spec, M2 plan. | `tests/test_markdown_first_real_pages.py`; source audit; beginner comprehension proof. |
| `SOURCES.md` | Adds reused Concept2 rowing sources. | Keeps reused source IDs globally auditable. | R30, source-index discipline. | Markdown-first checks and source audit. |
| `tools/checks/check_markdown_first.py` | Activates `basic_cardio_equipment` only for `exercises/rowing-machine.md`; accepts cardio label aliases; skips `media/prompts/` prompt records during reader-facing scans. | Enables the new cardio-equipment method without broadly changing exercise validation, and prevents support prompt records from being treated as content pages. | R15-R17, R39-R40, M1, M3. | `tests/test_exercise_method_guidance.py`; Markdown-first test discovery. |
| `tests/test_exercise_method_guidance.py` | Adds unit coverage for the scoped cardio method and preserves inactive method behavior. | Proves the validator accepts the rower method only where approved. | R15, R39-R40. | M1 validation and code-review M1. |
| `tests/test_markdown_first_real_pages.py` | Adds real-page checks for rowing sections, stroke sequence, setup, damper, method labels, sources, safety, forbidden scope, and media. | Proves the actual page meets the contract, not only helper behavior. | R1-R38. | M2, review-resolution, and M5 validation. |
| `tests/test_exercise_image_standard.py` | Adds regression coverage for prompt-record scan handling and image-standard expectations. | Keeps generated media support files from breaking Markdown-first page scans while preserving image governance. | R31-R36 and exercise-image standard. | M3 image test run. |
| `media/exercises/rowing-machine/*.png` | Adds setup, muscle-attention, and movement support images. | Responds to the follow-up readability and muscle-engagement request while keeping Markdown authoritative. | R31-R36, M5 plan. | Visual-safety review and code-review M5. |
| `media/PROVENANCE.md` and `media/prompts/exercises/rowing-machine/*.md` | Adds approved provenance rows and exact prompt records for all three generated assets. | Required for generated raster media auditability. | R36 and exercise-image standard. | `test_rowing_machine_media_is_local_prompt_backed_and_reviewed`. |
| `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` | Updates the exercise media inventory for the rowing page. | Keeps the existing image-standard audit current after adding a new exercise page and later rowing images. | Exercise-image standard tests. | `python3 -m unittest discover -s tests -p 'test_*image*.py'`. |
| `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/*` | Records source audit, beginner comprehension, media decision, and visual-safety review. | Captures manual proof for source support, reader comprehension, and image safety that automation cannot fully determine. | AC6-AC7, R27-R36. | Code-review M3 and M5. |
| `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/*`, `review-log.md`, `review-resolution.md`, `validation-ledger.md`, `change.yaml` | Records lifecycle reviews, resolved findings, validation, and current state. | Makes the implementation traceable through workflow gates without relying on chat context. | AGENTS workflow rule and active plan. | Review records M1-M5; closed review-resolution. |
| `docs/proposals/`, `specs/`, `docs/architecture/system/architecture.md`, `docs/plans/`, `docs/plan.md` | Adds and updates governing artifacts for proposal, spec, test spec, architecture, execution plan, and routing. | Durable artifacts were required before substantive content, validation, media, and safety work. | AGENTS source order and standard workflow. | Proposal/spec/architecture/plan/test-spec reviews. |

No unrelated implementation changes were found in code-review M5.

## Tests Added Or Changed

| Test | What it proves | Why this level is appropriate |
| --- | --- | --- |
| `tests/test_exercise_method_guidance.py` cardio method tests | `basic_cardio_equipment` is accepted for governed rowing content and not broadly activated elsewhere. | Unit-level checker behavior is the risk surface. |
| `tests/test_markdown_first_real_pages.py` rowing content tests | The actual rowing page includes required sections, setup, damper, sequence, method labels, source IDs, safety terms, central red-flags link, and forbidden-scope exclusions. | Integration-level real-page tests catch content drift. |
| `test_rowing_machine_media_is_local_prompt_backed_and_reviewed` | The three media assets are referenced locally, exist, have approved provenance rows, page refs, and exact prompt records. | Media governance depends on page/provenance/prompt alignment. |
| `tests/test_exercise_image_standard.py` prompt-record and audit checks | Prompt records do not become reader-facing Markdown pages, and the image audit stays current. | Existing image-standard contracts are shared across exercise pages. |

## Validation Evidence Available Before Final Verify

Local validation recorded through M5:

- `python3 -m unittest tests.test_exercise_method_guidance`
- `python3 -m unittest tests.test_markdown_first_real_pages`
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
- `python3 -m unittest discover -s tests -p 'test_*image*.py'`
- `python3 -m unittest discover -s tests`
- `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media`
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media`
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
- `git diff --check`

Manual evidence recorded:

- `manual-proof/source-audit.md`
- `manual-proof/beginner-comprehension.md`
- `manual-proof/media-decision.md`
- `manual-proof/visual-safety-review.md`
- `validation-ledger.md`

Hosted CI was not observed. Final `verify` has not run yet.

## Review Resolution Summary

`docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md`
is closed.

Resolved findings:

- `PR-RMB-1`: plan prompt-record references were corrected to
  `media/prompts/exercises/rowing-machine/<asset-stem>.md`.
- `TSR-RMB-1`: manual proof cases `RMB-M1` through `RMB-M5` gained explicit
  automation rationale, required environment, evidence artifact, pass
  condition, failure condition, owning stage, and re-run trigger.
- `CR-RMB-M2-1`: safety notes were split into source-supported groups with
  page-local source support for non-cardiopulmonary stop conditions.

Code-review M5 R1 closed the final implementation milestone with no findings.

## Alternatives Rejected

- Principle-only cardio-equipment page: rejected because it would not teach the
  rower-specific setup and stroke sequence a beginner needs.
- Full rowing program or 2k/race plan: rejected because it would move GymPrimer
  into personalized or sport-programming scope.
- Broad global activation of `basic_cardio_equipment`: rejected in favor of a
  path-scoped validator rule for the governed rowing page.
- Text-only after the follow-up media request: rejected because setup,
  sequence, and muscle attention became concrete readability needs.
- In-image labels or instructions: rejected because images must remain support
  assets and Markdown remains the source of truth.
- README navigation in this slice: not added because promotion/navigation
  remains conditional and downstream-gated.

## Scope Control

The change preserves these non-goals:

- No hosted app, database, calculator, workout tracker, user account, or
  generated public API.
- No personalized conditioning plan, race plan, heart-rate-zone prescription,
  2k training plan, or weight-loss guarantee.
- No diagnosis, treatment, rehabilitation protocol, return-to-training
  prescription, individualized medical advice, or symptom collection.
- No borrowed web images, commercial-machine screenshots, branded equipment
  photos, identifiable people, or remote image references.
- No broad migration of existing exercise pages or method types.

## Risks And Follow-Ups

Remaining risks before downstream gates:

- Static images cannot prove every reader will understand setup, muscle
  attention, or stroke sequence perfectly.
- Hosted CI has not been observed.
- Final `verify` and PR handoff remain.

The active plan state after this explanation: M1-M5 are closed by code-review,
no implementation milestones remain, and the next lifecycle stage is `verify`.
This artifact does not claim final verification, PR readiness, hosted CI
success, or merge readiness.
