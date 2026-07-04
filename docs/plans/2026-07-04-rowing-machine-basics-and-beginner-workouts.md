# Plan: Rowing Machine Basics and Beginner Workout Guidance

## Status

- Status: active
- Plan lifecycle state: active
- Terminal disposition: not-applicable

## Purpose / big picture

Implement the approved rowing-machine basics direction as a Markdown-first
exercise page with a narrowly activated `basic_cardio_equipment` method type.
The work adds a beginner-facing rowing-machine page, source-index support,
validation or manual proof for the new method boundary, and evidence that setup,
technique, safety, and beginner comprehension are covered.

This plan sequences implementation only. It does not reopen the accepted
rowing-machine direction, create a workout planner, add a runtime product,
activate `loaded_carry`, or roll out cardio-equipment guidance beyond the
approved rowing-machine scope.

## Source artifacts

- Proposal: `../proposals/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
- Proposal review: `../changes/rowing-machine-basics-and-beginner-workouts/reviews/proposal-review-r1.md`
- Spec: `../../specs/rowing-machine-basics-and-beginner-workouts.md`
- Spec review: `../changes/rowing-machine-basics-and-beginner-workouts/reviews/spec-review-r1.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review: `../changes/rowing-machine-basics-and-beginner-workouts/reviews/architecture-review-r1.md`
- Governing specs:
  - `../../specs/markdown-first-primer.md`
  - `../../specs/exercise-method-guidance.md`
  - `../../specs/exercise-image-standard.md`
- Test spec: `../../specs/rowing-machine-basics-and-beginner-workouts.test.md`

## Context and orientation

GymPrimer is a Markdown-first beginner primer. Exercise pages live under
`exercises/`, shared source records live in `SOURCES.md`, central stop-and-help
language lives in `RED-FLAGS.md`, optional exercise media lives under
`media/exercises/<slug>/`, provenance lives in `media/PROVENANCE.md`, and
prompt records live under `media/prompts/exercises/<exercise-slug>/<asset-stem>.md`
when generated raster media is used.

The approved spec adds exactly one rowing-machine exercise page at
`exercises/rowing-machine.md`. The page must be useful as plain Markdown,
include page-local sources, teach the stroke sequence and setup, and include
`Method type: basic_cardio_equipment` inside `## How much to do`.

The architecture amendment keeps this as visible Markdown content. It creates
no database, user input flow, generated public API, hidden metadata source of
truth, tracker, calculator, hosted app, or new ADR. The `basic_cardio_equipment`
method type is active only for rowing-machine content governed by the approved
spec and later cardio-equipment pages governed by approved downstream artifacts.
`loaded_carry` remains deferred.

The first implementation should be text-first. Images are optional and should
be added only when source audit, comprehension evidence, or reviewer feedback
shows that setup or stroke-sequence comprehension needs visual support.

## Non-goals

- Do not add a personalized rowing plan, race plan, 2k test plan, weight-loss
  promise, heart-rate-zone prescription, adaptive progression, or workout
  tracker.
- Do not add diagnosis, treatment, rehabilitation protocol, return-to-training
  prescription, individualized medical advice, or personalized coaching.
- Do not activate `loaded_carry` or broadly activate cardio-equipment pages.
- Do not add hidden metadata, YAML front matter, generated data packages,
  public APIs, account flows, calculators, or hosted app behavior.
- Do not use remote images, borrowed web images, commercial-machine screenshots,
  branded equipment photos, or identifiable people.
- Do not make images carry essential instructions that are absent from the
  Markdown page.

## Requirements covered

- R1-R3: M2 adds `exercises/rowing-machine.md` with the required top-level
  sections and plain-Markdown readability.
- R4-R7: M2 covers catch, drive, finish, recovery, the required drive and
  recovery sequences, and technique-first framing.
- R8-R14: M2 covers setup, damper, muscles, and broad educational feel wording;
  M3 source-audits the support.
- R15-R17, R39-R40: M1 adds or proves the scoped `basic_cardio_equipment`
  validation boundary and keeps `loaded_carry` deferred.
- R18-R24: M2 adds static beginner method and weekly-activity guidance; M3
  audits that examples remain educational rather than prescriptive.
- R25-R28: M2 adds safety routing and source-backed stop conditions; M3 audits
  source support for safety, setup, technique, damper, method, and weekly
  activity claims.
- R29-R30: M2 updates page-local sources and `SOURCES.md` where source-index
  rules require it.
- R31-R36: M3 decides whether text-only is sufficient or implements approved
  optional local media with provenance, prompt records, alt text, and visual
  review.
- R37-R38: M1-M4 preserve the no-runtime and no-medical-advice boundaries.
- AC1-AC9: Upstream reviews, M1-M4 validation, downstream plan-review,
  test-spec-review, code-review, manual proof, and final verification provide
  acceptance evidence.

## Current Handoff Summary

- Current milestone: M4
- Current milestone state: review-requested
- Last reviewed milestone: M3
- Review status: proposal-review R1 approved; spec-review R1 approved;
  architecture-review R1 approved; plan-review R1 requested PR-RMB-1; PR-RMB-1
  revision approved by plan-review R2; test-spec-review R2 approved the proof
  map; code-review M2 R1 requested CR-RMB-M2-1; CR-RMB-M2-1 resolved pending
  M2 code-review rerun; code-review M2 R2 closed M2; code-review M3 R1 closed M3
- Remaining in-scope implementation milestones: M4
- Remaining lifecycle milestones: code-review, explain-change, verify, PR
  handoff
- Next stage: code-review M4
- Final closeout readiness: not-ready
- Reason final closeout is or is not ready: M1 and M2 are closed by code-review;
  M3 is closed by code-review; M4 is implemented pending code-review; durable
  rationale, final verification, and PR handoff remain before closeout.

## Milestones

### M1. Cardio Method Boundary and Validation

- Milestone state: closed
- Goal: make the scoped `basic_cardio_equipment` boundary checkable before the
  rowing page relies on it.
- Requirements: R15-R17, R37-R40, AC2, AC4-AC5, AC8-AC9.
- Files/components likely touched:
  - `tools/checks/check_markdown_first.py`
  - `tests/test_exercise_method_guidance.py`
  - `tests/test_markdown_first_real_pages.py`
  - focused fixtures under `tests/fixtures/markdown-first/`, if needed
  - `docs/templates/exercise-card.md`, only if the existing template needs a
    cardio-equipment note
- Dependencies:
  - plan-review and test-spec-review must approve the proof map before
    implementation.
- Tests to add/update:
  - `basic_cardio_equipment` passes only for `exercises/rowing-machine.md` or
    another path explicitly governed by later approved artifacts.
  - `basic_cardio_equipment` still fails on unrelated exercise pages.
  - `loaded_carry` remains deferred.
  - required cardio labels or equivalent lines are detected for beginner
    starting point, effort, rest/reset, progression, and stop condition.
  - hidden metadata still cannot replace visible `Method type:` text.
- Implementation steps:
  - Inspect current exercise-method checker behavior and fixtures.
  - Add fail-before-implementation tests for scoped
    `basic_cardio_equipment`.
  - Implement the narrow checker/template update or record why current
    validation plus manual proof is sufficient.
  - Keep the rule path-aware so existing exercise pages do not fail solely for
    missing rowing-specific method guidance.
- Validation commands:
  - `python3 -m unittest tests.test_exercise_method_guidance`
  - `python3 -m unittest tests.test_markdown_first_real_pages`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises patterns principles`
  - `python3 tools/checks/check_privacy.py tools tests docs/templates specs docs/changes/rowing-machine-basics-and-beginner-workouts`
- Expected observable result: the repository can distinguish the approved
  rowing-machine cardio method type from deferred or unrelated method types.
- Commit message: `M1: scope cardio equipment method validation`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - A broad enum change could accidentally allow `basic_cardio_equipment`
    everywhere.
  - A strict checker could break existing exercise pages outside the approved
    slice.
- Rollback/recovery:
  - Revert to the previous deferred enum behavior and document manual proof as
    a temporary blocker until the test spec is revised.

### M2. Rowing Page and Source Index

- Milestone state: closed
- Goal: draft the text-first rowing-machine page with page-local citations,
  global source-index support where required, and no optional media yet.
- Requirements: R1-R14, R18-R30, R37-R38, AC3-AC9.
- Files/components likely touched:
  - `exercises/rowing-machine.md`
  - `SOURCES.md`
  - `RED-FLAGS.md`, only if an existing anchor or wording gap blocks the
    required link
  - `tests/test_markdown_first_real_pages.py`
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/`
- Dependencies:
  - M1 should provide the method boundary validation or a documented manual
    validation substitute.
- Tests to add/update:
  - rowing page has all required sections.
  - movement breakdown includes catch, drive, finish, recovery, and the required
    drive and recovery sequences.
  - `## How much to do` includes `Method type: basic_cardio_equipment`.
  - page links to the central safety reference.
  - forbidden prescription, diagnosis, rehab, sprint-first, maximal-damper, and
    race-plan wording is absent.
  - page-local sources and `SOURCES.md` entries are present where required.
- Implementation steps:
  - Draft `exercises/rowing-machine.md` using the approved page structure.
  - Add setup, technique, damper, muscles, feel, mistakes, beginner method,
    easier/harder versions, and safety notes with nearby citations.
  - Add page-local `## Sources` entries.
  - Add or reuse `SOURCES.md` entries for reused source IDs according to
    existing source-index rules.
  - Keep workout examples static and visibly non-personalized.
- Validation commands:
  - `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages`
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises principles patterns`
  - `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises docs/changes/rowing-machine-basics-and-beginner-workouts`
  - `git diff --check`
- Expected observable result: `exercises/rowing-machine.md` exists as a
  citation-backed, text-first beginner page that satisfies the approved spec.
- Commit message: `M2: add rowing machine beginner page`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Technique wording could outrun source support.
  - Workout examples could read like a personalized plan.
- Rollback/recovery:
  - Narrow unsupported claims, remove over-specific examples, or hold the page
    as unlinked draft content until source support and review pass.

### M3. Manual Proof, Comprehension, and Optional Media Decision

- Milestone state: closed
- Goal: record bounded manual evidence and decide whether text-only guidance is
  sufficient or whether setup or stroke-sequence images are needed.
- Requirements: R28-R36, AC5-AC7.
- Files/components likely touched:
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/source-audit.md`
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/beginner-comprehension.md`
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/media-decision.md`
  - `media/exercises/rowing-machine/`, only if media is added
  - `media/PROVENANCE.md`, only if generated raster media is added
  - `media/prompts/exercises/rowing-machine/<asset-stem>.md`, only if generated
    raster media requires prompt records
  - `exercises/rowing-machine.md`, only if media references or wording fixes are
    needed
- Dependencies:
  - M2 page draft must exist before manual source audit and comprehension
    review.
- Tests to add/update:
  - media/provenance checker coverage if images are added.
  - alt-text and local-path validation if images are referenced.
  - manual source-audit record for foot setup, stroke sequence, damper, beginner
    method, weekly activity, and stop conditions.
  - non-identifying beginner comprehension record for rower purpose, foot strap,
    drive sequence, recovery sequence, beginner first step, stop condition, and
    source verification.
- Implementation steps:
  - Perform a source-support audit against the page claims.
  - Record non-identifying beginner comprehension evidence.
  - Record a media decision: text-only accepted, or image work required.
  - If images are required, add only local setup or stroke-sequence media,
    provenance, prompt records where required, meaningful alt text, and visual
    safety review.
  - Remove or revise any image that introduces unsupported technique or
    instructions absent from Markdown.
- Validation commands:
  - `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media`
  - `python3 tools/checks/check_privacy.py exercises media docs/changes/rowing-machine-basics-and-beginner-workouts`
  - `python3 -m unittest discover -s tests -p 'test_*image*.py'`
  - `git diff --check`
- Expected observable result: promotion evidence states whether text-only
  guidance is sufficient; any added media is local, subordinate, reviewed, and
  provenance-backed.
- Commit message: `M3: record rowing proof and media decision`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Comprehension evidence could reveal that text-only guidance is not enough.
  - Generated images could encode unsupported setup or technique.
- Rollback/recovery:
  - Keep the page text-only and unpromoted until wording is fixed or approved
    media is added; remove any failed media references, assets, provenance rows,
    and prompt records.

### M4. Integration, Promotion Gate, and Lifecycle Evidence

- Milestone state: review-requested
- Goal: complete integration checks, update lifecycle evidence, and promote only
  when validation and manual proof satisfy the approved spec.
- Requirements: R1-R40, AC1-AC9.
- Files/components likely touched:
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml`
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/validation-ledger.md`
  - `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
  - `docs/plan.md`
  - `README.md`, only if the approved promotion path requires navigation
  - `SOURCES.md`
  - `exercises/rowing-machine.md`
- Dependencies:
  - M1-M3 must be implemented, reviewed, and closed.
- Tests to add/update:
  - broad Markdown-first checks over content, sources, safety, and media.
  - privacy scan over changed lifecycle evidence and content.
  - validation ledger records exact local commands and outcomes.
  - README or navigation checks only if navigation is added.
- Implementation steps:
  - Run the approved local validation suite.
  - Record a validation ledger with command, result, and evidence summary.
  - Update change metadata and plan progress to the next downstream gate.
  - Add README or other navigation only if manual proof supports promotion and
    the approved workflow permits it.
  - Prepare for code-review and final verify without claiming CI or branch
    readiness.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media`
  - `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
  - `git diff --check`
- Expected observable result: the rowing-machine slice has implementation,
  validation, manual proof, and lifecycle evidence ready for code-review and
  later final verification.
- Commit message: `M4: finalize rowing validation evidence`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Broad validation could expose unrelated historical content issues.
  - Promotion navigation could get ahead of manual proof.
- Rollback/recovery:
  - Keep the page as unlinked draft content, remove premature navigation, and
    record the blocking validation or proof gap before re-planning.

## Validation plan

- `python3 -m unittest tests.test_exercise_method_guidance`: prove the scoped
  method-type behavior and method-section requirements.
- `python3 -m unittest tests.test_markdown_first_real_pages`: prove real-page
  structural expectations where the repository already centralizes them.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`: smoke
  Markdown-first validation tests after checker changes.
- `python3 -m unittest discover -s tests -p 'test_*image*.py'`: run image and
  provenance tests if optional media is added.
- `python3 -m unittest discover -s tests`: final local repository test suite
  before implementation handoff or final verify.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media`: final Markdown-first content, link, source, method, media, and safety check surface, adjusted only if the checker documents a narrower supported path.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`: privacy scan over changed content and evidence.
- `git diff --check`: whitespace and patch hygiene.
- Manual source audit: confirm foot setup, stroke sequence, damper, beginner
  method, weekly activity, and stop-condition claims have cited support.
- Manual beginner comprehension proof: record non-identifying answers for rower
  purpose, foot strap position, drive sequence, recovery sequence, beginner
  first step, stop condition, and source verification.
- Manual visual-safety review: required only if setup or stroke-sequence media is
  added.

## Risks and recovery

- Risk: `basic_cardio_equipment` is accidentally activated for all exercise
  pages.
  - Recovery: restore path-scoped validation and keep unrelated cardio pages
    blocked pending their own approved artifacts.
- Risk: the rowing page becomes a rowing program instead of a beginner
  education page.
  - Recovery: remove schedules, race tests, all-out intervals, adaptive
    language, and goal-based prescription wording.
- Risk: setup, damper, technique, or weekly-activity claims are under-sourced.
  - Recovery: narrow the claim to what the source supports or replace it with a
    better page-local source before promotion.
- Risk: text-only guidance fails the beginner comprehension proof.
  - Recovery: revise wording first; add setup or movement media only when the
    comprehension gap is visual.
- Risk: optional media introduces unsupported or source-of-truth instructions.
  - Recovery: remove the image reference and asset, then revise or regenerate
    only under the exercise-image standard.
- Risk: broad validation exposes unrelated historical failures.
  - Recovery: record the unrelated failure, run targeted approved checks for the
    rowing slice, and do not claim broad validation until the unrelated issue is
    resolved or explicitly scoped out.

## Dependencies

- Accepted rowing-machine proposal and approved proposal-review record.
- Approved rowing-machine spec and approved spec-review record.
- Approved architecture amendment and approved architecture-review record.
- Approved plan-review before test-spec or implementation.
- Implement M1 with the approved test spec before code-review.
- Existing Markdown-first, exercise-method, and exercise-image validation tools.
- Public source pages for rowing technique, damper, beginner workouts, adult
  activity guidance, and central safety routing.
- Optional image-generation and provenance workflow only if M3 determines media
  is needed.

## Progress

- 2026-07-04: Proposal created and accepted after clean proposal-review R1.
- 2026-07-04: Spec created and approved after clean spec-review R1.
- 2026-07-04: Architecture amendment created and approved after clean
  architecture-review R1.
- 2026-07-04: Architecture lifecycle metadata normalized to approved before
  planning relied on the amendment.
- 2026-07-04: Execution plan created; plan-review is the next lifecycle stage.
- 2026-07-04: Plan-review R2 approved the plan after PR-RMB-1 resolution.
- 2026-07-04: Test spec drafted and approved by test-spec-review R2;
  implementation M1 is the next lifecycle stage.
- 2026-07-04: M1 implementation added tests first, then scoped
  `basic_cardio_equipment` validation to `exercises/rowing-machine.md`.
- 2026-07-04: M1 moved to review-requested for code-review.
- 2026-07-04: Code-review M1 R1 returned clean-with-notes and closed M1.
- 2026-07-04: M2 implementation added real-page tests first, drafted
  `exercises/rowing-machine.md`, updated `SOURCES.md`, and moved M2 to
  review-requested for code-review.
- 2026-07-04: Code-review M2 R1 requested CR-RMB-M2-1 for incomplete
  page-local source support on the safety stop-condition sentence.
- 2026-07-04: Review-resolution split `## Safety notes` into source-supported
  groups and moved M2 back to review-requested for code-review.
- 2026-07-04: Code-review M2 R2 returned clean-with-notes and closed M2.
- 2026-07-04: M3 implementation recorded the source audit, beginner
  comprehension proof, and text-only media decision; added a page-local muscles
  source; updated image audit inventory for the new text-only rowing page; and
  moved M3 to review-requested for code-review.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-04 | Make method-boundary validation M1 before page drafting. | The rowing page depends on `basic_cardio_equipment`, and the existing exercise-method spec previously deferred that value. | Draft the page first and discover checker/source-index failures late. |
| 2026-07-04 | Start text-first and make media evidence-triggered. | The spec allows text-only when comprehension is sufficient, while generated media adds provenance, prompt-record, and visual-safety obligations. | Add images by default; prohibit images even if comprehension evidence shows a visual gap. |
| 2026-07-04 | Gate promotion/navigation behind manual proof. | The page should not be surfaced as ready until source audit and beginner comprehension evidence pass. | Add README navigation immediately after drafting; defer all promotion decisions to chat. |

## Surprises and discoveries

- `basic_cardio_equipment` was explicitly deferred by the earlier
  exercise-method guidance slice, so this change needs a scoped activation
  guardrail rather than a broad enum expansion.
- The existing `## How much to do` checker could support cardio guidance with
  label aliases, so `docs/templates/exercise-card.md` was unaffected for M1.
- M2 did not need a `RED-FLAGS.md` change because `../RED-FLAGS.md` resolves
  from `exercises/rowing-machine.md`.
- M2 did not add media or README navigation; both remain gated by later manual
  proof and promotion decisions.
- Review-resolution for CR-RMB-M2-1 reused already indexed `nhs-back-pain` and
  `mayo-weight-training` sources, and added a page-local
  `local-rowing-machine-exercise-pain` source for sharp or worsening pain.
- M3 source audit found that the muscles section needed a nearby page-local
  source for glutes and lats, so `local-rowing-machine-muscles` was added from
  Concept2's rowing muscles-used article.
- M3 accepted text-only rowing guidance because the beginner comprehension proof
  passed without a visual comprehension gap.
- `media/prompts/` Markdown prompt records are data/support artifacts, not
  reader-facing content pages. The Markdown-first checker now skips them during
  directory scans while the exercise-image prompt-record tests continue to
  validate their own contract.
- The exercise-image M4 audit is a current exercise inventory checked by
  `tests/test_exercise_image_standard.py`; adding `exercises/rowing-machine.md`
  required a text-only row there even though no rowing image was added.
- M4 did not change README navigation because the approved plan makes README
  edits conditional and no required navigation update exists before code-review.

## Validation notes

- 2026-07-04: `python tools/checks/check_privacy.py docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/architecture-review-r1.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md docs/architecture/system/architecture.md` passed before plan creation.
- 2026-07-04: `python tools/checks/check_markdown_first.py` was not used as a
  lifecycle-artifact validator because it is content-page oriented and flags
  proposal/spec wording outside its supported scope.
- 2026-07-04: `python3 tools/checks/check_privacy.py docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/plan.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/architecture/system/architecture.md` passed after plan creation.
- 2026-07-04: `git diff --check` passed after plan creation.
- 2026-07-04: `rg -n "^- draft amendment|is pending architecture review|is ready for architecture review" docs/architecture/system/architecture.md docs/plan.md` returned no matches after architecture status settlement.
- 2026-07-04: PR-RMB-1 was addressed by replacing the incorrect prompt-record
  directory references with the approved
  `media/prompts/exercises/rowing-machine/<asset-stem>.md` prompt-record path
  shape and updating the M3 privacy command.
- 2026-07-04: `python3 tools/checks/check_privacy.py docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plan.md` passed after PR-RMB-1 revision.
- 2026-07-04: `git diff --check` passed after PR-RMB-1 revision.
- 2026-07-04: Test-spec authoring added
  `specs/rowing-machine-basics-and-beginner-workouts.test.md`.
- 2026-07-04: `python3 tools/checks/check_privacy.py specs/rowing-machine-basics-and-beginner-workouts.test.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plan.md` passed after test-spec authoring.
- 2026-07-04: `git diff --check` passed after test-spec authoring.
- 2026-07-04: Coverage scan confirmed R1-R40, E1-E5, and EC1-EC10 appear in
  `specs/rowing-machine-basics-and-beginner-workouts.test.md`.
- 2026-07-04: TSR-RMB-1 was addressed by adding manual-proof metadata to
  `RMB-M1` through `RMB-M5`.
- 2026-07-04: `python3 tools/checks/check_privacy.py specs/rowing-machine-basics-and-beginner-workouts.test.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plan.md` passed after TSR-RMB-1 revision.
- 2026-07-04: `git diff --check` passed after TSR-RMB-1 revision.
- 2026-07-04: Manual-proof metadata scan confirmed `RMB-M1` through `RMB-M5`
  include automation rationale, required environment, evidence artifact, pass
  condition, failure condition, owning stage, and re-run trigger.
- 2026-07-04: Test-spec-review R2 approved the proof map and allowed
  implementation handoff for M1.
- 2026-07-04: `python3 tools/checks/check_privacy.py docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/test-spec-review-r2.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plan.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md specs/rowing-machine-basics-and-beginner-workouts.test.md` passed after test-spec-review R2 recording.
- 2026-07-04: `git diff --check` passed after test-spec-review R2
  recording.
- 2026-07-04: Stale test-spec-review handoff wording scan, excluding recorded
  validation-command lines, found no matches after R2 recording.
- 2026-07-04: Manual-proof metadata scan confirmed `RMB-M1` through `RMB-M5`
  still include automation rationale, required environment, evidence artifact,
  pass condition, failure condition, owning stage, and re-run trigger after R2
  recording.
- 2026-07-04: Added failing M1 tests first. Initial
  `python3 -m unittest tests.test_exercise_method_guidance` failed because
  `basic_cardio_equipment` was still inactive for `exercises/rowing-machine.md`
  and `Rest/reset:` / `Stop condition:` were not accepted label aliases.
- 2026-07-04: `python3 -m unittest tests.test_exercise_method_guidance`
  passed after the scoped checker update.
- 2026-07-04: `python3 -m unittest tests.test_markdown_first_real_pages`
  passed after the scoped checker update.
- 2026-07-04: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  passed after the scoped checker update.
- 2026-07-04: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises patterns principles`
  passed after the scoped checker update.
- 2026-07-04: `python3 tools/checks/check_privacy.py tools tests docs/templates specs docs/changes/rowing-machine-basics-and-beginner-workouts`
  passed after the scoped checker update.
- 2026-07-04: Re-ran M1 validation after handoff metadata updates:
  `python3 -m unittest tests.test_exercise_method_guidance`,
  `python3 -m unittest tests.test_markdown_first_real_pages`,
  `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`,
  `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises patterns principles`,
  `python3 tools/checks/check_privacy.py tools tests docs/templates specs docs/changes/rowing-machine-basics-and-beginner-workouts`,
  and `git diff --check` all passed.
- 2026-07-04: `python3 tools/checks/check_privacy.py tools tests docs/templates specs docs/changes/rowing-machine-basics-and-beginner-workouts docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/plan.md`,
  `git diff --check`, and the plan/change state-sync check passed before M1
  handoff commit.
- 2026-07-04: Code-review M1 R1 independently reran
  `python3 -m unittest tests.test_exercise_method_guidance`, which passed.
- 2026-07-04: `python3 tools/checks/check_privacy.py docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m1-r1.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/plan.md`,
  `git diff --check`, and the plan/change state-sync check passed after
  code-review M1 R1 recording.
- 2026-07-04: Added failing M2 real-page tests first. Initial
  `python3 -m unittest tests.test_markdown_first_real_pages` failed because
  `exercises/rowing-machine.md` did not exist.
- 2026-07-04: `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages`
  passed after adding the rowing page and source-index entries.
- 2026-07-04: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises principles patterns`
  passed after adding the rowing page and source-index entries.
- 2026-07-04: `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises docs/changes/rowing-machine-basics-and-beginner-workouts`
  passed after adding the rowing page and source-index entries.
- 2026-07-04: `git diff --check` passed after adding the rowing page and
  source-index entries.
- 2026-07-04: Re-ran M2 validation after handoff metadata updates:
  `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages`,
  `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises principles patterns`,
  `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises docs/changes/rowing-machine-basics-and-beginner-workouts`,
  `git diff --check`, and the plan/change state-sync check all passed.
- 2026-07-04: Code-review M2 R1 independently reran
  `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages`,
  which passed, but found CR-RMB-M2-1 during semantic source review.
- 2026-07-04: `python3 tools/checks/check_privacy.py docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m2-r1.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/plan.md`,
  `git diff --check`, and state-sync check passed after code-review M2 R1
  recording.
- 2026-07-04: Added failing review-resolution test coverage for missing
  `nhs-back-pain` and `mayo-weight-training` page-local safety sources. Initial
  `python3 -m unittest tests.test_markdown_first_real_pages` failed because
  those source definitions were absent.
- 2026-07-04: First safety-source content fix failed
  `python3 -m unittest tests.test_markdown_first_real_pages` and
  `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises principles patterns`
  because claim-level safety references were not on the same line and the new
  local source ID did not match the `local-rowing-machine-*` convention.
- 2026-07-04: `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages`
  passed after CR-RMB-M2-1 resolution.
- 2026-07-04: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises principles patterns`
  passed after CR-RMB-M2-1 resolution.
- 2026-07-04: `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises docs/changes/rowing-machine-basics-and-beginner-workouts`,
  `git diff --check`, and state-sync check passed after CR-RMB-M2-1 resolution.
- 2026-07-04: Code-review M2 R2 independently reran
  `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages`,
  `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises principles patterns`,
  `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises docs/changes/rowing-machine-basics-and-beginner-workouts`,
  and `git diff --check`; all passed.
- 2026-07-04: `python3 tools/checks/check_privacy.py docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m2-r2.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/plan.md`,
  `git diff --check`, and state-sync check passed after code-review M2 R2
  recording.
- 2026-07-04: Initial M3 `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media`
  failed because existing `media/prompts/...` prompt records were treated as
  reader-facing content pages. Added regression coverage and skipped
  `media/prompts/` from page checks.
- 2026-07-04: Initial M3 `python3 -m unittest discover -s tests -p 'test_*image*.py'`
  failed because the exercise-image M4 audit did not yet list the new
  `exercises/rowing-machine.md` page. Added a text-only audit row.
- 2026-07-04: `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media`
  passed after M3 proof and checker updates.
- 2026-07-04: `python3 tools/checks/check_privacy.py exercises media docs/changes/rowing-machine-basics-and-beginner-workouts`
  passed after M3 proof and checker updates.
- 2026-07-04: `python3 -m unittest discover -s tests -p 'test_*image*.py'`
  passed after M3 proof and checker updates.
- 2026-07-04: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  passed after the prompt-record scan handling update.
- 2026-07-04: `git diff --check` passed after M3 proof and checker updates.
- 2026-07-04: State-sync check passed for `docs/plan.md`,
  `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`, and
  `docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml` before
  M3 handoff.
- 2026-07-04: Code-review M3 R1 independently reran
  `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media`,
  `python3 tools/checks/check_privacy.py exercises media docs/changes/rowing-machine-basics-and-beginner-workouts`,
  `python3 -m unittest discover -s tests -p 'test_*image*.py'`,
  `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`,
  and `git diff --check`; all passed.
- 2026-07-04: `python3 tools/checks/check_privacy.py docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m3-r1.md docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/plan.md`,
  `git diff --check`, and state-sync check passed after code-review M3 R1
  recording.
- 2026-07-04: M4 `python3 -m unittest discover -s tests` passed with 120 tests.
- 2026-07-04: M4 `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media`
  passed with 27 Markdown files checked.
- 2026-07-04: M4 `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
  passed with 75 files checked.
- 2026-07-04: M4 `git diff --check` passed.
- 2026-07-04: `python3 tools/checks/check_privacy.py docs/changes/rowing-machine-basics-and-beginner-workouts/validation-ledger.md docs/changes/rowing-machine-basics-and-beginner-workouts/explain-change.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/plan.md`,
  `git diff --check`, and state-sync check passed after M4 handoff metadata
  updates.

## Outcome and retrospective

- M1 implemented scoped cardio method validation and closed after clean
  code-review. M2 implemented the rowing page and source index, then closed
  after CR-RMB-M2-1 review-resolution and clean code-review R2. M3 recorded
  manual proof, comprehension evidence, and the text-only media decision, then
  closed after clean code-review R1. M4 recorded integration validation
  evidence and is pending code-review.

## Readiness

- See `Current Handoff Summary`.
- Ready for code-review of M4.
- Not ready for final verification, PR handoff, or Done until the remaining
  lifecycle gates complete.
