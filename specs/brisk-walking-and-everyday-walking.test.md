# Test Spec: Brisk Walking and Everyday Walking Guidance

## Status

active

## Related spec and plan

- Spec: `specs/brisk-walking-and-everyday-walking.md`
- Plan: `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`
- Architecture: `docs/architecture/system/architecture.md`
- Architecture review: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/architecture-review-r2.md`

## Input artifact identities

| Input | Path | Status / Review state | Identity |
| --- | --- | --- | --- |
| Proposal | `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md` | accepted | Proposal-review R3 approved the required brisk-walking movement and muscle-attention image amendment on 2026-07-05. |
| Spec | `specs/brisk-walking-and-everyday-walking.md` | approved | Spec-review R3 approved the amended media contract and closed SR-WALK-IMG-1. |
| Spec review | `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r3.md` | approved | No material findings; eventual test-spec readiness was conditional on downstream architecture and plan updates. |
| Architecture | `docs/architecture/system/architecture.md` | approved | Architecture-review R2 approved the required brisk-walking media amendment. |
| Plan | `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md` | reviewed | Plan-review R2 approved M4 for required brisk-walking images. |
| Plan review | `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/plan-review-r2.md` | approved | No material findings; immediate next stage is test-spec. |

## Testing strategy

Unit tests cover method-type scope, required labels, forbidden wording, template prompts, real-page structure, source-index reuse, muscle/feel sections, and required image behavior.

Integration-style checker runs cover the actual Markdown pages, `SOURCES.md`, `RED-FLAGS.md`, and required media provenance.

Manual proof covers semantic source support, beginner comprehension, M4 required image suitability, and residual risk because deterministic checks cannot prove claim support, reader understanding, or visual instructional value.

No end-to-end browser test is required because the product surface is GitHub-readable Markdown and this change introduces no runtime, UI, generated HTML dependency, tracker, calculator, account, or API.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| BWG-R1 | BWG-T3, BWG-T4, CMD6 | integration | Both page paths must exist and pass focused checker validation. |
| BWG-R2 | BWG-T3, BWG-T5, BWG-MP2 | integration, manual | Brisk walking page must be cardio education without excluded plan/medical framing. |
| BWG-R3 | BWG-T4, BWG-T5, BWG-MP2 | integration, manual | Everyday walking must stay movement-habit guidance. |
| BWG-R4 | BWG-T4, BWG-MP2 | integration, manual | Tests and beginner proof check the brisk/everyday distinction. |
| BWG-R5 | BWG-T3, BWG-MP1, BWG-MP2 | integration, manual | Pace section must cover talk test, effort, and pace reference. |
| BWG-R6 | BWG-T3, BWG-MP1 | integration, manual | Intensity claims need page-local citations and source-audit support. |
| BWG-R7 | BWG-T2, BWG-T3, CMD1, CMD6 | unit, integration | Brisk page must include exact `## How much to do`. |
| BWG-R8 | BWG-T1, BWG-T3, CMD1, CMD6 | unit, integration | Brisk page must declare `Method type: basic_cardio_activity`. |
| BWG-R9 | BWG-T1, CMD1 | unit | Method contract must activate scoped `basic_cardio_activity`. |
| BWG-R10 | BWG-T2, BWG-T3 | unit, integration | Cardio activity uses time, effort, progression, and stop rules. |
| BWG-R11 | BWG-T3, BWG-MP1 | integration, manual | Starter guidance includes 5-10 minutes or approved narrower wording. |
| BWG-R12 | BWG-T3, BWG-MP1 | integration, manual | Progression order is total minutes, brisk minutes, then hills or faster sections. |
| BWG-R13 | BWG-T5, CMD1, CMD6 | unit, integration | Adaptive method wording must fail deterministic checks where practical. |
| BWG-R14 | BWG-T6, CMD3 | unit, integration | Brisk page must include role-based `## Muscles involved`. |
| BWG-R15 | BWG-T6, CMD3 | unit, integration | Brisk page must include aligned `## What you should feel`. |
| BWG-R16 | BWG-T5, BWG-T6, BWG-MP1 | unit, manual | Muscle/feel wording must avoid exact activation and clinical claims. |
| BWG-R17 | BWG-T3, BWG-MP1 | integration, manual | Technique cues need page-local source support. |
| BWG-R18 | BWG-T3, BWG-T4, CMD6 | integration | Both pages must route to `RED-FLAGS.md` when safety context appears. |
| BWG-R19 | BWG-T3, BWG-T4, BWG-MP1 | integration, manual | Stop-rule categories must appear and be source-audited. |
| BWG-R20 | BWG-T5, CMD6 | unit, integration | Disease-specific and return-to-walking plans must be excluded. |
| BWG-R21 | BWG-T3, BWG-T4, CMD6 | integration | Both pages need page-local `## Sources`. |
| BWG-R22 | BWG-T7, CMD6 | integration | Reused source IDs must appear in `SOURCES.md`. |
| BWG-R23 | BWG-MP1 | manual | Source-audit proof covers named claim categories. |
| BWG-R24 | BWG-T8, BWG-T9, BWG-MP3, CMD4, CMD9 | unit, integration, manual | Brisk page must include one movement image and one muscle-attention image. |
| BWG-R25 | BWG-T8, BWG-MP3, CMD4, CMD9 | unit, manual | Movement image must teach brisk-walking form and satisfy image-standard proof. |
| BWG-R25A | BWG-T8, BWG-MP3, CMD4, CMD9 | unit, manual | Muscle-attention image must remain broad and satisfy image-standard proof. |
| BWG-R25B | BWG-T8, BWG-T9, BWG-MP3, CMD4, CMD9 | unit, manual | Required generated raster image metadata, provenance, prompt records, and page refs must be valid. |
| BWG-R26 | BWG-T8, CMD4, CMD9 | integration | Everyday walking remains text-only unless a later spec changes it. |
| BWG-R27 | BWG-T5, CMD1, CMD6, CMD7 | unit, integration | Forbidden calorie, weight-loss, step, tracker, and adaptive behavior is checked where deterministic. |
| BWG-R28 | BWG-T5, CMD6 | unit, integration | Race-walking, running, hiking, rucking, treadmill, incline, and walking-program scope is excluded. |
| BWG-R29 | BWG-T1-BWG-T9, CMD1-CMD11 | unit, integration | Automated validation surfaces are implemented across milestones. |
| BWG-R30 | BWG-MP2 | manual | Beginner proof records the walking-specific comprehension prompts. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | BWG-T3, BWG-MP2 | Brisk walking page behavior and reader understanding. |
| E2 | BWG-T4, BWG-MP2 | Everyday walking habit framing and distinction from brisk cardio. |
| E3 | BWG-T1, BWG-T2, BWG-T3 | Method type and method-shape checks. |
| E4 | BWG-T7, BWG-MP1 | Page-local source and source-index proof. |
| E5 | BWG-T8, BWG-T9, BWG-MP3 | Required movement and muscle-attention image behavior. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 slow errands | BWG-T4, BWG-MP2 | integration, manual | Everyday walking counts as movement, not automatically brisk cardio. |
| EC2 five-minute brisk walk | BWG-T3, BWG-MP1 | integration, manual | Short walks can add up only with source-supported non-prescriptive wording. |
| EC3 10,000 steps | BWG-T5 | unit | Universal step mandates fail forbidden-scope checks where deterministic. |
| EC4 hills | BWG-T3, BWG-MP1 | integration, manual | Hills appear only as later comfortable progression, not a protocol. |
| EC5 source index without page-local source | BWG-T7, CMD6 | integration | Page-local source omission fails. |
| EC6 validator lacks method type | BWG-T1, CMD1 | unit | Method validator must accept scoped `basic_cardio_activity`. |
| EC7 image with labels or pain marks | BWG-T8, CMD4 | unit | Existing exercise-image checks fail unsafe image behavior. |
| EC7A missing required brisk image | BWG-T8, BWG-T9, BWG-MP3, CMD4, CMD9 | integration, manual | Brisk page must include both required support image purposes. |
| EC7B exact anatomy muscle image | BWG-T8, BWG-MP3, CMD4, CMD9 | unit, manual | Muscle-attention image must stay broad and unlabeled. |
| EC8 motivational filler | BWG-T4, BWG-MP2 | integration, manual | Everyday page must contain practical examples and pass comprehension proof. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CMD1 | `python3 -m unittest tests.test_exercise_method_guidance` | planned-for-implementation | implementation agent | M1 | M1 code-review | Nonzero exit blocks M1 closeout. | Zero tests discovered blocks M1 closeout. | M1 validation notes and `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/validation-ledger.md` | Local read/write test fixtures only; no network or publication. |
| CMD2 | `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` | planned-for-implementation | implementation agent | M1 | M1 code-review | Nonzero exit blocks milestone closeout. | Zero tests discovered blocks milestone closeout. | Validation ledger | Local unittest only; no network or publication. |
| CMD3 | `python3 -m unittest tests.test_exercise_muscle_guidance` | planned-for-implementation | implementation agent | M2 | M2 code-review | Nonzero exit blocks M2 closeout. | Zero tests discovered blocks M2 closeout. | Validation ledger | Local unittest only; no network or publication. |
| CMD4 | `python3 -m unittest tests.test_exercise_image_standard` | existing/configured | implementation agent | M3 and M4 | M3 code-review for historical image audit; M4 code-review for required images | Nonzero exit blocks M3 or M4 closeout when required by that milestone. | Zero tests discovered blocks M3 or M4 closeout when required by that milestone. | Validation ledger | Local unittest only; no network or image generation. |
| CMD5 | `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | existing/configured | implementation agent | M2 | M2 code-review | Nonzero exit blocks milestone closeout. | Zero tests discovered blocks milestone closeout. | Validation ledger | Local unittest discovery only; no network or publication. |
| CMD6 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md` | planned-for-implementation | implementation agent | M2 and M4 | M2 code-review for page contract; M4 code-review for required image references | Nonzero exit blocks M2 and later promotion readiness. | Not applicable. | Validation ledger | Local checker only; no network or publication. |
| CMD7 | `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking` | existing/configured | implementation agent | M2 | M2 code-review | Any forbidden finding or setup error blocks closeout. | Not applicable. | Validation ledger | Local privacy scan only; no network or publication. |
| CMD8 | `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media docs/changes/2026-07-05-brisk-walking-and-everyday-walking` | existing/configured | implementation agent | M3 and M4 | M3 code-review for historical media-proof scan; M4 code-review for required images | Any forbidden finding or setup error blocks closeout when required by that milestone. | Not applicable. | Validation ledger | Local privacy scan only; no network or publication. |
| CMD9 | `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | planned-for-implementation | implementation agent | M4 | M4 code-review | Nonzero exit blocks M4 closeout. | Zero tests discovered blocks M4 closeout. | Validation ledger | Local unittest only; no network or image generation. |
| CMD10 | `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | existing/configured | implementation agent | M4 | M4 code-review | Nonzero exit blocks M4 closeout. | Zero tests discovered blocks M4 closeout. | Validation ledger | Local unittest only; no network or publication. |
| CMD11 | `git diff --check` | existing/configured | implementation agent | M4 | M4 code-review | Whitespace errors block M4 closeout. | Not applicable. | Validation ledger | Local diff check only; no network or publication. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | BWG-T1, BWG-T2, BWG-T5 | none | CMD1, CMD2, CMD7 | M1 validation notes; validation ledger | M1 code-review | Proves method type scope and authoring support before page content. |
| M2 | BWG-T3, BWG-T4, BWG-T6, BWG-T7 | none | CMD1, CMD2, CMD3, CMD5, CMD6, CMD7 | M2 validation notes; validation ledger | M2 code-review | Proves page structure, sources, method, and muscle/feel. |
| M3 | none | BWG-MP1, BWG-MP2 | CMD4, CMD5, CMD6, CMD8 | `manual-proof/source-audit.md`; `manual-proof/beginner-comprehension.md`; `manual-proof/optional-image-decision.md`; validation ledger | M3 code-review | Closed under the prior text-only media contract; the historical optional-image decision remains evidence but no longer satisfies the amended required-media contract. |
| M4 | BWG-T8, BWG-T9 | BWG-MP3 | CMD4, CMD5, CMD6, CMD8, CMD9, CMD10, CMD11 | `manual-proof/required-image-decision.md`; `manual-proof/visual-safety.md`; `media/PROVENANCE.md`; prompt records; validation ledger | M4 code-review | Proves the two required brisk-walking images, prompt/provenance/page-ref wiring, visual-safety evidence, and no everyday-walking image before final closeout resumes. |

## Test cases

### BWG-T1. Scoped `basic_cardio_activity` Method Type

- Covers: BWG-R8, BWG-R9, BWG-R13, BWG-R27, BWG-R29, E3, EC6
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Extend `tests.test_exercise_method_guidance` fixtures with `Method type: basic_cardio_activity`.
- Steps: Validate one fixture at `exercises/brisk-walking.md`, one unrelated fixture, and existing `basic_cardio_equipment` rowing fixture.
- Expected result: `basic_cardio_activity` passes only for brisk walking or approved non-equipment cardio activity paths; unrelated paths fail inactive method type; `basic_cardio_equipment` remains scoped; `loaded_carry` remains inactive.
- Failure proves: Method type activation is too broad, too narrow, or regresses existing deferred method boundaries.
- Evidence artifact: M1 validation notes and validation ledger.
- Automation location: `tests/test_exercise_method_guidance.py`
- Required by milestone: M1

### BWG-T2. Cardio Activity Method Shape

- Covers: BWG-R7, BWG-R10, BWG-R11, BWG-R12, BWG-R29, E3
- Level: unit
- Command IDs: CMD1, CMD2
- Fixture/setup: Method-section fixture and template assertions for non-equipment cardio activity.
- Steps: Assert visible `## How much to do`, `Method type: basic_cardio_activity`, beginner starting point, effort, progression, and stop language are required; assert sets/reps are not the primary required method shape.
- Expected result: Valid cardio activity guidance passes with time/effort/progression/stop labels; missing labels or empty labels fail.
- Failure proves: Authors can promote brisk walking without the method information beginners need.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_exercise_method_guidance.py`, `tests/test_markdown_first_templates.py`
- Required by milestone: M1

### BWG-T3. Brisk Walking Page Contract

- Covers: BWG-R1, BWG-R2, BWG-R5-R12, BWG-R17-R22, E1, EC2, EC4
- Level: integration
- Command IDs: CMD2, CMD5, CMD6, CMD7
- Fixture/setup: Real page `exercises/brisk-walking.md`.
- Steps: Assert required sections, brisk pace checks, method type, starter duration, progression order, technique cues, safety notes, `../RED-FLAGS.md` routing, page-local `## Sources`, and source ID references.
- Expected result: The real page satisfies the exercise-page contract and focused checker command passes.
- Failure proves: Brisk walking cannot be promoted as a self-contained Markdown exercise page.
- Evidence artifact: M2 validation notes and validation ledger.
- Automation location: `tests/test_markdown_first_real_pages.py`, checker command CMD6
- Required by milestone: M2

### BWG-T4. Everyday Walking Principle Contract

- Covers: BWG-R1, BWG-R3, BWG-R4, BWG-R18-R22, E2, EC1, EC8
- Level: integration
- Command IDs: CMD2, CMD5, CMD6, CMD7
- Fixture/setup: Real page `principles/everyday-walking.md`.
- Steps: Assert required principle sections, practical walking examples, brisk/everyday distinction, safety notes, `../RED-FLAGS.md` routing when safety context appears, and page-local sources.
- Expected result: The real page teaches movement habit-building without equating all walking with formal brisk cardio.
- Failure proves: Everyday walking content is missing, unstructured, unsafe, or indistinguishable from the exercise page.
- Evidence artifact: M2 validation notes and validation ledger.
- Automation location: `tests/test_markdown_first_real_pages.py`, checker command CMD6
- Required by milestone: M2

### BWG-T5. Walking Forbidden Scope Guardrails

- Covers: BWG-R2, BWG-R13, BWG-R16, BWG-R20, BWG-R27, BWG-R28, EC3, EC7
- Level: unit
- Command IDs: CMD1, CMD6, CMD7
- Fixture/setup: Method fixtures and real-page scans for deterministic forbidden wording.
- Steps: Check for adaptive programming, rehab/treatment/diagnosis, weight-loss prescription, calorie target, step-count mandate, heart-rate zones, tracker/app wording, running progression, hiking, rucking, treadmill protocol, incline protocol, and walking-program framing where deterministic.
- Expected result: Fixtures with forbidden wording fail, and real pages do not contain excluded-scope wording.
- Failure proves: The walking slice can drift into out-of-scope medical, weight-loss, tracking, or program content.
- Evidence artifact: M1 and M2 validation notes.
- Automation location: `tests/test_exercise_method_guidance.py`, checker command CMD6
- Required by milestone: M1 and M2

### BWG-T6. Brisk Walking Muscle and Feel Guidance

- Covers: BWG-R14, BWG-R15, BWG-R16
- Level: integration
- Command IDs: CMD3, CMD6
- Fixture/setup: Real page `exercises/brisk-walking.md`.
- Steps: Assert `## Muscles involved` uses role-based broad regions and `## What you should feel` aligns with intensity and body-awareness guidance without exact activation or clinical claims.
- Expected result: Muscle and feel sections pass existing muscle-guidance expectations for new exercise pages.
- Failure proves: The brisk page violates the accepted muscle guidance contract or becomes too anatomical/clinical.
- Evidence artifact: M2 validation notes.
- Automation location: `tests/test_exercise_muscle_guidance.py`, `tests/test_markdown_first_real_pages.py`
- Required by milestone: M2

### BWG-T7. Source Index and Page-Local Source Support Structure

- Covers: BWG-R6, BWG-R21, BWG-R22, E4, EC5
- Level: integration
- Command IDs: CMD6
- Fixture/setup: `SOURCES.md`, `exercises/brisk-walking.md`, and `principles/everyday-walking.md`.
- Steps: Assert each page has `## Sources`; reused source IDs appear in `SOURCES.md`; page text does not rely only on `SOURCES.md` for walking claims.
- Expected result: The focused checker and tests identify source-section and source-index gaps.
- Failure proves: Walking claims are not traceable at the page level.
- Evidence artifact: M2 validation notes and M3 source-audit proof.
- Automation location: `tests/test_markdown_first_real_pages.py`, checker command CMD6
- Required by milestone: M2

### BWG-T8. Required Brisk Walking Images

- Covers: BWG-R24, BWG-R25, BWG-R25A, BWG-R25B, BWG-R26, E5, EC7, EC7A, EC7B
- Level: integration
- Command IDs: CMD4, CMD6, CMD8, CMD9
- Fixture/setup: Real walking pages, generated raster image artifacts, prompt records, and `media/PROVENANCE.md`.
- Steps: Assert `exercises/brisk-walking.md` references exactly one `exercise_movement_illustration` and exactly one `exercise_muscle_attention_illustration`; assert both image paths are local, have meaningful alt text, approved provenance, prompt records, page refs, supported media purpose, no in-image labels, and no red pain marks; assert `principles/everyday-walking.md` has no image.
- Expected result: Brisk walking image-bearing page passes only with both required support images under the exercise-image standard, and everyday walking remains text-only.
- Failure proves: Required media is missing, unsupported, unsafe, incorrectly purposed, or out of scope.
- Evidence artifact: M4 required-image decision, provenance rows, prompt records, visual-safety evidence, and validation ledger.
- Automation location: `tests/test_exercise_image_standard.py`, `tests/test_markdown_first_real_pages.py`
- Required by milestone: M4

### BWG-T9. Required Image Prompt and Provenance Wiring

- Covers: BWG-R24, BWG-R25B, BWG-R29, E5, EC7A
- Level: integration
- Command IDs: CMD4, CMD6, CMD8, CMD9, CMD10
- Fixture/setup: `media/exercises/brisk-walking/movement.png`, `media/exercises/brisk-walking/muscle-attention.png`, prompt records under `media/prompts/exercises/brisk-walking/`, `media/PROVENANCE.md`, and `exercises/brisk-walking.md`.
- Steps: Assert each required image has exactly one approved provenance row with `asset_type = ai_generated_raster`, the expected media purpose, a repository-local prompt record, a prompt-record asset path matching the provenance asset path, non-blank exact prompt text, page refs containing `exercises/brisk-walking.md`, and no unsupported source input or privacy data.
- Expected result: Each required generated raster asset is traceable from Markdown reference to provenance row to exact prompt record and back to the same normalized asset path.
- Failure proves: The image is not auditable, the prompt/provenance contract is incomplete, or the wrong asset is being promoted.
- Evidence artifact: `media/PROVENANCE.md`, prompt records, and validation ledger.
- Automation location: `tests/test_exercise_image_standard.py`, checker command CMD6
- Required by milestone: M4

### BWG-MP1. Manual Source Audit

- Covers: BWG-R6, BWG-R11, BWG-R12, BWG-R17, BWG-R19, BWG-R23, E4
- Level: manual
- Command IDs: none
- Fixture/setup: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/source-audit.md`.
- Steps: Record claim samples for intensity, talk test, weekly activity guidance where used, less-sitting framing, technique, starter duration or progression, and stop rules.
- Expected result: Each sampled claim has page, claim, source ID, source fit, outcome, and residual risk.
- Failure proves: Semantic source support was not reviewed before promotion.
- Evidence artifact: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/source-audit.md`
- Automation location: manual
- Required by milestone: M3

### BWG-MP2. Beginner Comprehension Proof

- Covers: BWG-R2-R5, BWG-R30, E1, E2, EC1, EC8
- Level: manual
- Command IDs: none
- Fixture/setup: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/beginner-comprehension.md`.
- Steps: Record non-identifying results for the walking-specific prompts: difference between everyday and brisk walking, brisk pace check, starting duration, expected body feel, stop conditions, and source for intensity.
- Expected result: Evidence records whether the reader can answer each prompt and what must be fixed if they cannot.
- Failure proves: Page approval relies on generic reader approval instead of the approved comprehension proof.
- Evidence artifact: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/beginner-comprehension.md`
- Automation location: manual
- Required by milestone: M3

### BWG-MP3. Required Image Decision and Visual-Safety Proof

- Covers: BWG-R24, BWG-R25, BWG-R25A, BWG-R25B, BWG-R26, E5, EC7, EC7A, EC7B
- Level: manual
- Command IDs: CMD4, CMD9
- Fixture/setup: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/required-image-decision.md` and `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/visual-safety.md`.
- Steps: Record why the media-bearing walking slice uses both required images, asset paths, image purposes, prompt records, provenance rows, alt text, visual-safety outcomes, page references, rejected-asset notes where relevant, and any residual risk. Confirm the movement image teaches brisk-walking form and the muscle-attention image teaches only broad attention regions.
- Expected result: Both required brisk-walking images are justified, local, provenance-backed, visually reviewed, and subordinate to Markdown; everyday walking remains text-only.
- Failure proves: Required media was added without approved purpose, visual-safety proof, or provenance.
- Evidence artifact: `manual-proof/required-image-decision.md`, `manual-proof/visual-safety.md`, image-standard validation output, and validation ledger.
- Automation location: manual plus `tests/test_exercise_image_standard.py`
- Required by milestone: M4

## Fixtures and data

- Method fixtures in `tests/test_exercise_method_guidance.py` for valid and invalid `basic_cardio_activity`.
- Real pages `exercises/brisk-walking.md` and `principles/everyday-walking.md`.
- Existing `SOURCES.md` and `RED-FLAGS.md` files.
- Existing media provenance fixtures from exercise-image tests and required walking image artifacts.
- Required M4 image artifacts at `media/exercises/brisk-walking/movement.png` and `media/exercises/brisk-walking/muscle-attention.png`.
- Required M4 prompt records at `media/prompts/exercises/brisk-walking/movement.md` and `media/prompts/exercises/brisk-walking/muscle-attention.md`.
- Manual proof files under `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/`.

## Mocking/stubbing policy

Use temporary filesystem fixtures for checker unit tests.

Do not mock source-support review, beginner comprehension proof, `SOURCES.md` reuse, or generated raster provenance when those artifacts are the evidence under review.

Do not call external websites, publish pages, or use network-dependent validation in this proof map. Image generation itself is implementation work and must produce local assets, prompt records, provenance rows, and review evidence before promotion.

## Migration or compatibility tests

Compatibility tests must prove `basic_cardio_equipment` remains scoped to rowing-machine or later approved cardio-equipment pages, `loaded_carry` remains inactive, and unrelated text-only exercise pages remain valid.

No old-data, database, API, or path migration tests are required because this change adds new Markdown pages and a method type without moving existing content.

## Observability verification

Validation evidence must identify file paths, stable test or checker failure categories where available, manual proof IDs, command IDs, and residual risk.

No runtime logs, metrics, traces, or audit events apply.

## Security/privacy verification

Privacy scans must cover walking pages and change-local manual proof.

Manual proof must avoid private reader details, private health information, private reviewer data, local machine paths, secrets, credentials, and identifiable private people.

## Performance checks

No runtime performance checks apply.

Local unittest and checker commands should remain suitable for normal repository validation. If a command becomes slow, record the duration and split the command in the validation ledger before expanding scope.

## Manual QA checklist

- Confirm brisk walking and everyday walking remain distinct.
- Confirm brisk walking uses the talk test, moderate effort, and pace reference without defining brisk walking only by speed.
- Confirm brisk walking method guidance is static education and starts with 5-10 minutes or approved narrower wording.
- Confirm everyday walking gives practical examples and does not say every step is formal cardio.
- Confirm both pages route safety concerns to `RED-FLAGS.md`.
- Confirm source-audit rows cover all BWG-R23 categories used by the pages.
- Confirm beginner comprehension proof records each BWG-R30 prompt.
- Confirm required brisk-walking movement and muscle-attention images are fully provenance-backed, visually reviewed, and subordinate to Markdown.
- Confirm the movement image shows upright posture, forward gaze, relaxed neck and shoulders, natural arm swing, relaxed hands, and heel-to-toe walking without race-walking, running, treadmill, hiking, wearable-tracker, wrong/correct, or clinical framing.
- Confirm the muscle-attention image shows only broad attention regions for glutes, thighs, calves, trunk, shoulders or upper back, and feet or ankles without precise anatomy, exposed musculature, labels, diagnosis, treatment, rehabilitation, pain marks, or exact activation claims.

## What not to test and why

- Do not test personalized walking plans, trackers, wearable integrations, calorie calculators, or heart-rate zones because they are out of scope.
- Do not test disease-specific walking programs, pregnancy, post-surgery, injury recovery, cardiopulmonary protocols, or return-to-walking advice because the spec forbids them.
- Do not test race walking, running, hiking, rucking, treadmill, incline walking, or loaded walking because those require later specs.
- Do not test generated HTML rendering because Markdown is the source of truth and no mdBook change is in scope.
- Do not test external link liveness as a required gate unless a later workflow adds network-safe link checking.

## Uncovered gaps

None. Semantic source adequacy and beginner comprehension are manual proof obligations rather than automation gaps.

## Next artifacts

- Test-spec review R2.
- Implementation after test-spec-review R2 approval.

## Follow-on artifacts

- Test-spec review R1: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/test-spec-review-r1.md`
- Test-spec review R2: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/test-spec-review-r2.md`

## Readiness

Active proof map approved by test-spec-review R2. M4 implementation handoff is allowed, but implementation has not started from this review.
