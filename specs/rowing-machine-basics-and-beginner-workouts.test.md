# Test Spec: Rowing Machine Basics and Beginner Workout Guidance

## Status

active

## Related spec and plan

- Spec: `specs/rowing-machine-basics-and-beginner-workouts.md`
- Spec review: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/spec-review-r1.md`
- Plan: `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
- Plan review: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/plan-review-r2.md`
- Architecture: `docs/architecture/system/architecture.md`
- Architecture review: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/architecture-review-r1.md`
- Related exercise method spec: `specs/exercise-method-guidance.md`
- Related exercise image spec: `specs/exercise-image-standard.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`

## Testing strategy

Unit coverage extends the exercise-method checker with path-scoped
`basic_cardio_equipment` validation. It proves that the rowing-machine page can
use the new method type, unrelated exercise pages cannot, `loaded_carry`
remains deferred, required cardio labels are present, and hidden metadata still
cannot replace visible Markdown.

Integration coverage checks the real rowing-machine page once it exists:
required headings, stroke phases, setup and damper wording, method guidance,
stop conditions, central safety link, source references, source-index behavior,
forbidden-scope wording, and optional media references.

End-to-end coverage remains repository-native. A reader must be able to open
`exercises/rowing-machine.md` directly as Markdown, read the source list,
follow the safety link, and understand that the page is static education rather
than a hosted app, tracker, calculator, video-first product, or personalized
program.

Smoke coverage runs focused local commands for each milestone and a final local
test/check set before code-review or verify handoff. Hosted CI is not part of
this proof unless a run is actually observed later.

Manual coverage records semantic evidence that static parsing cannot prove:
source support for setup, technique, damper, method, weekly activity, and safety
claims; beginner comprehension; text-only versus media necessity; and visual
safety if images are added.

Contract coverage treats visible Markdown as the source of truth. The
`Method type: basic_cardio_equipment` line is authoritative for the rowing page
only, generated raster media remains subordinate to Markdown, and prompt records
for generated raster images use the approved
`media/prompts/exercises/<exercise-slug>/<asset-stem>.md` path shape.

Migration coverage is additive. Existing exercise pages, active method types,
source IDs, templates, and media remain valid unless selected by this approved
slice. `loaded_carry` remains deferred. Future cardio-equipment pages require
their own approved downstream scope.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | RMB-T2 | integration | Real-page test requires `exercises/rowing-machine.md`. |
| R2 | RMB-T2, RMB-T11 | integration, contract | Page is Markdown-only and has no runtime, video, account, tracking, or server dependency. |
| R3 | RMB-T2 | integration | Required top-level section list is exact. |
| R4 | RMB-T3 | integration | Movement breakdown contains catch, drive, finish, and recovery. |
| R5 | RMB-T3, RMB-M2 | integration, manual | Drive sequence is checked in Markdown and beginner comprehension. |
| R6 | RMB-T3, RMB-M2 | integration, manual | Recovery sequence is checked in Markdown and beginner comprehension. |
| R7 | RMB-T4, RMB-M1 | integration, manual | Technique-first framing and not-pull-hard framing are checked. |
| R8 | RMB-T4, RMB-M1 | integration, manual | Setup terms and source support are checked. |
| R9 | RMB-T4, RMB-M1 | integration, manual | Foot strap wording is automated for presence and manually audited for source support. |
| R10 | RMB-T4 | integration | Comfortable catch range and no forced vertical-shin wording are checked. |
| R11 | RMB-T4 | integration | Damper feel and no high-damper superiority wording are checked. |
| R12 | RMB-T4 | integration | Stroke effort, not blindly high damper, is checked. |
| R13 | RMB-T5 | integration | Broad legs/glutes, trunk, upper-back/lats, and arms wording is checked. |
| R14 | RMB-T5, RMB-T11 | integration, contract | Precise activation, diagnosis, treatment, and correction wording are rejected. |
| R15 | RMB-T1 | unit | `basic_cardio_equipment` is allowed only for rowing-machine governed scope. |
| R16 | RMB-T1, RMB-T6 | unit, integration | Rowing method section includes `Method type: basic_cardio_equipment`. |
| R17 | RMB-T1, RMB-T6 | unit, integration | Required cardio labels or equivalent lines are checked. |
| R18 | RMB-T6 | integration | Short easy exposure and reset break are checked. |
| R19 | RMB-T6, RMB-T11 | integration, contract | Easy/moderate start is checked; all-out, maximal damper, and sprint-first wording is rejected. |
| R20 | RMB-T6 | integration | Technique before time before moderate effort is checked. |
| R21 | RMB-T6, RMB-M1 | integration, manual | Static examples are allowed only when framed as examples. |
| R22 | RMB-T6, RMB-T11 | integration, contract | Race plans, 2k tests, multi-week plans, weight-loss promises, HR-zone prescriptions, and personalization are rejected. |
| R23 | RMB-T10 | integration | Rowing contributes to aerobic work and does not replace strength training. |
| R24 | RMB-T10, RMB-M1 | integration, manual | Adult aerobic plus two-days muscle-strengthening guidance has citation support. |
| R25 | RMB-T9 | integration | Safety notes link to `../RED-FLAGS.md` or correct relative path. |
| R26 | RMB-T9 | integration | Stop conditions cover specified symptoms and technique breakdown. |
| R27 | RMB-T9, RMB-M1 | integration, manual | Concrete safety and stop-condition claims have source support. |
| R28 | RMB-T4, RMB-T6, RMB-T8, RMB-T10, RMB-M1 | integration, manual | Technique, setup, damper, method, weekly activity, and example claims are source-audited. |
| R29 | RMB-T8 | integration | Used claim sources appear in page-local `## Sources`. |
| R30 | RMB-T8, RMB-M1 | integration, manual | Reused sources use `SOURCES.md` according to source-index rules. |
| R31 | RMB-T12 | integration | Remote images, borrowed images, screenshots, branded photos, and identifiable people fail media review. |
| R32 | RMB-M3 | manual | Text-only decision is recorded when comprehension is sufficient. |
| R33 | RMB-T12, RMB-M4 | integration, manual | Setup image, if added, is limited to setup-relevant information. |
| R34 | RMB-T12, RMB-M4 | integration, manual | Stroke image, if added, is limited to rowing movement sequence or key positions. |
| R35 | RMB-T12, RMB-M4 | integration, manual | In-image instructions, citations, safety notes, red pain marks, diagnostic symbols, and wrong/correct labels fail review. |
| R36 | RMB-T12, RMB-M4 | integration, manual | Generated raster images must satisfy provenance, prompt-record, alt-text, page-ref, and visual-safety requirements. |
| R37 | RMB-T11 | contract | No hosted app, calculator, tracker, user input, public API, or hidden metadata source is introduced. |
| R38 | RMB-T11 | contract | Diagnosis, treatment, rehab, return-to-training, individualized medical advice, and coaching are rejected. |
| R39 | RMB-T1 | unit | Existing active method types remain valid and `loaded_carry` remains inactive. |
| R40 | RMB-T1, RMB-M1 | unit, manual | Validation or manual proof distinguishes `basic_cardio_equipment` from existing method types. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | RMB-T3, RMB-M2 | Stroke phases and drive/recovery sequences are checked in Markdown and comprehension evidence. |
| E2 | RMB-T4, RMB-T8, RMB-M1 | Foot strap claim must have nearby citation and page-local source support. |
| E3 | RMB-T1, RMB-T6 | Method section must use `basic_cardio_equipment` and include cardio guidance labels. |
| E4 | RMB-T6, RMB-T11, RMB-M1 | Static workout examples are checked for non-prescriptive framing and forbidden plan language. |
| E5 | RMB-T12, RMB-M4 | Optional media must be local, alt-texted, provenance-backed when generated, and Markdown-consistent. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | RMB-T4, RMB-M1 | integration, manual | Foot-strap wording remains general enough and source-supported. |
| EC2 | RMB-T4 | integration | Catch wording allows comfortable range rather than forcing vertical shins. |
| EC3 | RMB-T6 | integration | Harder version prioritizes smoother technique and more time before harder effort. |
| EC4 | RMB-T4 | integration | Damper wording distinguishes flywheel feel from work and effort. |
| EC5 | RMB-T6, RMB-T11 | integration, contract | Examples remain short and do not become schedule, challenge, or plan. |
| EC6 | RMB-M3 | manual | Text-only guidance can pass when comprehension evidence is sufficient. |
| EC7 | RMB-T12, RMB-M4 | integration, manual | Unsupported media technique requires revision or removal before promotion. |
| EC8 | RMB-M1 | manual | Sport-rowing sources require claim narrowing or more direct gym-beginner sources. |
| EC9 | RMB-T1 | unit | Deferred checker behavior is updated or manual proof blocks promotion. |
| EC10 | RMB-T8, RMB-M1 | integration, manual | Existing compatible `SOURCES.md` IDs are reused unless audit justifies a new ID. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Evidence artifact |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RMB-CMD1 | `python3 -m unittest tests.test_exercise_method_guidance` | existing and extended | tooling maintainer | M1 | M1 | Unexpected nonzero exit blocks M1 closeout. | M1 validation notes and code-review record. |
| RMB-CMD2 | `python3 -m unittest tests.test_markdown_first_real_pages` | existing and extended | tooling maintainer | M1, M2 | M1 | Unexpected nonzero exit blocks owning milestone. | Milestone validation notes and code-review record. |
| RMB-CMD3 | `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | existing smoke | tooling maintainer | M1 | M1 | Unexpected nonzero exit blocks M1 closeout. | M1 validation notes and code-review record. |
| RMB-CMD4 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises patterns principles` | existing and extended | content/check maintainer | M1 | M1 | Unexpected nonzero exit blocks M1 closeout. | M1 validation notes and code-review record. |
| RMB-CMD5 | `python3 tools/checks/check_privacy.py tools tests docs/templates specs docs/changes/rowing-machine-basics-and-beginner-workouts` | existing | tooling maintainer | M1 | M1 | Any privacy finding or setup error blocks M1 closeout. | M1 validation notes and code-review record. |
| RMB-CMD6 | `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages` | existing and extended | content/check maintainer | M2 | M2 | Unexpected nonzero exit blocks M2 closeout. | M2 validation notes and code-review record. |
| RMB-CMD7 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises principles patterns` | existing and extended | content/check maintainer | M2 | M2 | Unexpected nonzero exit blocks M2 closeout. | M2 validation notes and code-review record. |
| RMB-CMD8 | `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises docs/changes/rowing-machine-basics-and-beginner-workouts` | existing | content/check maintainer | M2 | M2 | Any privacy finding or setup error blocks M2 closeout. | M2 validation notes and code-review record. |
| RMB-CMD9 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media` | existing and extended when media is added | content/check maintainer | M3 | M3 | Unexpected nonzero exit blocks M3 closeout. | M3 validation notes and code-review record. |
| RMB-CMD10 | `python3 tools/checks/check_privacy.py exercises media docs/changes/rowing-machine-basics-and-beginner-workouts` | existing | proof maintainer | M3 | M3 | Any privacy finding or setup error blocks M3 closeout. | M3 validation notes and code-review record. |
| RMB-CMD11 | `python3 -m unittest discover -s tests -p 'test_*image*.py'` | existing and conditional | media/check maintainer | M3 | M3 if media is added | Unexpected nonzero exit blocks media promotion. | M3 validation notes, media decision, and code-review record. |
| RMB-CMD12 | `git diff --check` | existing | implementer | M2-M4 | M2 | Whitespace errors block owning milestone closeout. | Milestone validation notes. |
| RMB-CMD13 | `python3 -m unittest discover -s tests` | existing smoke | release/check maintainer | M4 | M4 | Unexpected nonzero exit blocks M4 closeout. | M4 validation ledger and code-review record. |
| RMB-CMD14 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media` | existing and extended | release/check maintainer | M4 | M4 | Unexpected nonzero exit blocks M4 closeout. | M4 validation ledger and verify report. |
| RMB-CMD15 | `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md specs/rowing-machine-basics-and-beginner-workouts.test.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md` | existing | release/check maintainer | M4 | M4 | Any privacy finding or setup error blocks M4 closeout. | M4 validation ledger and verify report. |

## Milestone proof map

| Milestone | Test and proof IDs | Command IDs | Evidence artifact |
| --- | --- | --- | --- |
| M1 | RMB-T1, RMB-T11 | RMB-CMD1, RMB-CMD2, RMB-CMD3, RMB-CMD4, RMB-CMD5 | M1 validation notes and code-review record. |
| M2 | RMB-T2, RMB-T3, RMB-T4, RMB-T5, RMB-T6, RMB-T7, RMB-T8, RMB-T9, RMB-T10, RMB-T11 | RMB-CMD6, RMB-CMD7, RMB-CMD8, RMB-CMD12 | M2 validation notes and code-review record. |
| M3 | RMB-T12, RMB-M1, RMB-M2, RMB-M3, RMB-M4 | RMB-CMD9, RMB-CMD10, RMB-CMD11, RMB-CMD12 | Manual proof records, media decision, visual-safety evidence if needed, and code-review record. |
| M4 | RMB-T11, RMB-M5 | RMB-CMD12, RMB-CMD13, RMB-CMD14, RMB-CMD15 | Validation ledger, lifecycle metadata, and code-review record. |

## Test cases

### RMB-T1. Scoped basic cardio method validation

- Covers: R15, R16, R17, R39, R40, E3, EC9
- Level: unit
- Fixture/setup: Extend `tests/test_exercise_method_guidance.py` with fixture Markdown for `exercises/rowing-machine.md`, an unrelated exercise page, all previously active method types, `loaded_carry`, and hidden-only method metadata.
- Steps: Run `validate_exercise_method_guidance` against the fixtures.
- Expected result: `Method type: basic_cardio_equipment` passes for `exercises/rowing-machine.md` when required labels or equivalent lines are present; the same method type fails for unrelated pages; existing active method types still pass; `loaded_carry` still fails; hidden-only metadata still fails.
- Failure proves: The new method type is either still deferred for rowing, activated too broadly, or weakens the visible-Markdown method contract.
- Automation location: `tests/test_exercise_method_guidance.py`; `tools/checks/check_markdown_first.py`.

### RMB-T2. Rowing page exists and has the required Markdown shape

- Covers: R1, R2, R3
- Level: integration
- Fixture/setup: Use real repository file `exercises/rowing-machine.md`.
- Steps: Assert the file exists, contains the required top-level headings, and does not require generated HTML, JavaScript, video, account, tracking flow, local server, database, or user input.
- Expected result: The page is direct Markdown with the required section contract and no runtime dependency language.
- Failure proves: The page is missing, structurally incomplete, or outside the Markdown-first boundary.
- Automation location: `tests/test_markdown_first_real_pages.py` or focused rowing test module.

### RMB-T3. Stroke phases and sequence are visible

- Covers: R4, R5, R6, E1
- Level: integration
- Fixture/setup: Use `exercises/rowing-machine.md`.
- Steps: Parse or inspect `## Movement breakdown` for catch, drive, finish, recovery, drive sequence legs then body then arms, and recovery sequence arms then body then legs.
- Expected result: The phase list and both sequences are present and not reversed or obscured.
- Failure proves: A beginner cannot learn the core stroke model from the page.
- Automation location: `tests/test_markdown_first_real_pages.py` or focused rowing test module; reinforced by RMB-M2.

### RMB-T4. Setup, catch, damper, and technique-first guidance are source-auditable

- Covers: R7, R8, R9, R10, R11, R12, R28, E2, EC1, EC2, EC4
- Level: integration
- Fixture/setup: Use `exercises/rowing-machine.md`.
- Steps: Assert setup guidance mentions foot strap, catch range, grip, shoulders, posture, handle path, and damper meaning; check foot strap wording, comfortable catch range, damper-as-feel wording, and effort-creates-work wording; require nearby citation markers for setup and damper claims.
- Expected result: Required setup and damper concepts are present with page-local citation markers and no high-damper superiority or forced-range wording.
- Failure proves: The page under-teaches setup, misstates the damper, or lacks audit hooks for source review.
- Automation location: focused rowing real-page test; semantic support verified by RMB-M1.

### RMB-T5. Muscles and feel language stays broad and non-clinical

- Covers: R13, R14
- Level: integration
- Fixture/setup: Use `exercises/rowing-machine.md`.
- Steps: Assert `## Muscles involved` mentions legs/glutes, trunk, upper back/lats, and arms in broad educational language; scan page for precise activation, diagnosis, treatment, cure, rehab, or correction claims.
- Expected result: Muscle literacy is present without individualized activation or clinical claims.
- Failure proves: The page either fails basic muscle literacy or drifts into unsupported clinical/anatomy precision.
- Automation location: focused rowing real-page test and checker forbidden-scope scans.

### RMB-T6. Basic cardio method guidance is static and beginner-safe

- Covers: R16, R17, R18, R19, R20, R21, R22, E3, E4, EC3, EC5
- Level: integration
- Fixture/setup: Use `exercises/rowing-machine.md`.
- Steps: Inspect `## How much to do` for `Method type: basic_cardio_equipment`, beginner starting point, effort, rest/reset, progression, stop condition, short easy exposure such as 3-5 minutes, break/reset language, easy or moderate effort, technique-before-time-before-effort progression, and static example framing.
- Expected result: The method section provides beginner-safe static examples and rejects all-out effort, maximal damper, sprint-first work, race tests, 2k plans, multi-week schedules, weight-loss guarantees, HR-zone prescription, or personalization.
- Failure proves: The page turns cardio equipment guidance into unsafe or personalized programming.
- Automation location: focused rowing real-page test and checker forbidden-scope scans; semantic source support verified by RMB-M1.

### RMB-T7. Forbidden personalized, clinical, and product boundaries fail

- Covers: R22, R37, R38, EC5
- Level: contract
- Fixture/setup: Add checker fixtures or focused scans containing schedule/challenge/plan, symptom adaptation, diagnosis, treatment, rehab, return-to-training, coaching, hosted app, calculator, tracker, user-input flow, generated public API, or hidden metadata source-of-truth language.
- Steps: Run checker or focused tests against invalid fixtures and the real page.
- Expected result: Invalid fixtures fail with stable forbidden-scope categories; the real page avoids the forbidden boundaries.
- Failure proves: The implementation can drift into app/product, clinical, or personalized-plan behavior.
- Automation location: `tools/checks/check_markdown_first.py`, focused unittest fixtures, and `tests/test_exercise_method_guidance.py` where method-section language is involved.

### RMB-T8. Sources and source index are complete

- Covers: R24, R27, R28, R29, R30, E2, EC10
- Level: integration
- Fixture/setup: Use `exercises/rowing-machine.md` and `SOURCES.md`.
- Steps: Check that cited source IDs used in page claims appear in the page-local `## Sources`; check reused IDs against `SOURCES.md` when existing source-index rules require it; sample citations near foot setup, damper, technique, method, weekly activity, and safety claims.
- Expected result: Page-local sources exist for every used claim source and reused source IDs are globally auditable.
- Failure proves: Source support is missing, global source discipline regressed, or cited claims cannot be audited.
- Automation location: Markdown-first checker/source tests plus RMB-M1 semantic audit.

### RMB-T9. Safety routing and stop conditions are complete

- Covers: R25, R26, R27
- Level: integration
- Fixture/setup: Use `exercises/rowing-machine.md` and `RED-FLAGS.md`.
- Steps: Assert `## Safety notes` links to `../RED-FLAGS.md` or the correct relative path and includes chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, symptoms that worsen, painful technique, and jerky or uncontrolled technique breakdown.
- Expected result: The page routes to the central safety reference and names the required stop conditions.
- Failure proves: Safety routing is missing or concrete stop guidance is incomplete.
- Automation location: focused rowing real-page test; source support verified by RMB-M1.

### RMB-T10. Weekly activity guidance does not replace strength work

- Covers: R23, R24
- Level: integration
- Fixture/setup: Use `exercises/rowing-machine.md`.
- Steps: Assert the page says rowing contributes to aerobic activity, does not replace all strength training, and states that adult guidance includes aerobic activity and muscle-strengthening activity on at least two days per week with citation support.
- Expected result: Weekly activity framing preserves the aerobic-plus-strength boundary.
- Failure proves: The page could mislead beginners into treating rowing as a complete replacement for strength work.
- Automation location: focused rowing real-page test; source support verified by RMB-M1.

### RMB-T11. Runtime, hidden metadata, and clinical boundaries remain absent

- Covers: R2, R14, R19, R22, R37, R38
- Level: contract
- Fixture/setup: Use real page plus invalid fixtures if checker coverage is added.
- Steps: Scan for generated HTML requirements, JavaScript, video-first framing, database, user account, tracker, calculator, user input, hidden metadata source-of-truth, diagnosis, treatment, rehab, return-to-training, individualized medical advice, all-out effort, sprint-first work, maximal damper, and personalized coaching.
- Expected result: Real page passes; invalid fixtures fail where checker support exists.
- Failure proves: The implementation violates core product, safety, or exercise-method boundaries.
- Automation location: Markdown-first checker and focused unittest fixtures.

### RMB-T12. Optional media is either absent with evidence or fully compliant

- Covers: R31, R32, R33, R34, R35, R36, E5, EC6, EC7
- Level: integration
- Fixture/setup: Use `exercises/rowing-machine.md`, `media/PROVENANCE.md`, optional media under `media/exercises/rowing-machine/`, optional prompt records under `media/prompts/exercises/rowing-machine/`, and manual evidence.
- Steps: If no images are referenced, require a media-decision record explaining text-only sufficiency. If images are referenced, run media validation for local paths, no remote or borrowed media, meaningful alt text, subject-co-located assets, approved provenance, prompt records, page refs, visual-safety evidence, and no in-image text/safety/diagnostic/wrong-correct labels.
- Expected result: The page is valid text-only, or every image is local, subordinate, provenance-backed when generated, prompt-record-backed, and visually reviewed.
- Failure proves: Media is unsupported, unlicensed, non-local, source-of-truth-bearing, or visually unsafe.
- Automation location: `tests/test_exercise_image_standard.py`, `tools/checks/check_markdown_first.py`, and RMB-M3/RMB-M4.

### RMB-M1. Manual source-support audit

- Covers: R7, R8, R9, R13, R21, R24, R27, R28, R30, R40, E2, E4, EC1, EC8, EC10
- Level: manual
- Fixture/setup: Use final draft `exercises/rowing-machine.md`, page-local sources, `SOURCES.md`, and external source pages.
- Automation rationale: Static checks can prove citation markers and source-list presence, but they cannot prove that cited rowing, damper, activity-guideline, and safety sources semantically support the exact page claims.
- Required environment: Local repository checkout with the final draft page, `SOURCES.md`, and browser or documented source access for the cited public sources.
- Evidence artifact: `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/source-audit.md`.
- Steps: Record whether foot setup, catch range, stroke sequence, damper, beginner method, weekly activity, stop conditions, muscle wording, and static example framing are supported by the cited sources.
- Pass condition: Every audited claim category is marked supported by a cited source, narrowed to match source support, or blocked from promotion with a specific unresolved source gap.
- Failure condition: Any audited claim category is unsupported, relies only on a global source without page-local support, uses a sport-rowing source for an unsupported gym-beginner setup claim, or lacks a recorded disposition.
- Owning stage: M3 manual proof before promotion and before M4 lifecycle evidence.
- Re-run trigger: Re-run after any edit to setup, stroke sequence, damper, method examples, weekly activity, stop conditions, muscle wording, source IDs, or cited source entries.
- Expected result: Every audited claim category is supported, narrowed, or explicitly blocked before promotion.
- Failure proves: Citation markers exist but semantic source support is inadequate.
- Automation location: `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/source-audit.md`.

### RMB-M2. Beginner comprehension proof

- Covers: R5, R6, E1
- Level: manual
- Fixture/setup: Use a non-identifying beginner read test of `exercises/rowing-machine.md`.
- Automation rationale: Automated text checks can prove required words are present, but they cannot prove a target beginner can understand rower purpose, setup, sequence, stop conditions, or source verification.
- Required environment: Local repository checkout with the final draft page and a non-identifying reader or reviewer simulation that records no private health, contact, or training-log data.
- Evidence artifact: `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/beginner-comprehension.md`.
- Steps: Record whether the reader can state what the rower is for, foot strap position, drive sequence, recovery sequence, beginner first step, stop condition, and which source to click for technique.
- Pass condition: Evidence records pass or short non-identifying notes for every required question, plus any confusion found and revision/recheck outcome.
- Failure condition: Any required question is unanswered, wrong, recorded with identifying/private information, or reveals confusion that is not revised and rechecked before promotion.
- Owning stage: M3 manual proof before promotion and before M4 lifecycle evidence.
- Re-run trigger: Re-run after substantive edits to setup, movement breakdown, how-much-to-do, safety notes, sources, or media that affects beginner comprehension.
- Expected result: Evidence records pass/fail or short non-identifying notes for each question and any required revisions.
- Failure proves: The page may be source-backed but not understandable to the target reader.
- Automation location: `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/beginner-comprehension.md`.

### RMB-M3. Text-only versus media decision

- Covers: R32, EC6
- Level: manual
- Fixture/setup: Use final text draft, source audit, and beginner comprehension evidence.
- Automation rationale: Whether media is necessary depends on comprehension evidence and reviewer judgment; static checks can only validate media after a decision is made.
- Required environment: Local repository checkout with the final text draft, source-audit record, beginner-comprehension record, and any proposed media references if media is under consideration.
- Evidence artifact: `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/media-decision.md`.
- Steps: Record whether text-only guidance is sufficient or whether setup or stroke-sequence media is required to fix a comprehension gap.
- Pass condition: The record states either that text-only guidance is sufficient with supporting comprehension evidence, or that setup/stroke-sequence media is required with a specific scope and reason.
- Failure condition: Media is added without a recorded need, text-only promotion proceeds despite an unresolved visual comprehension gap, or the decision lacks a link to source-audit and comprehension evidence.
- Owning stage: M3 manual proof before optional media work is promoted.
- Re-run trigger: Re-run after substantive text changes that affect comprehension, after beginner-comprehension evidence changes, or before adding/removing rowing-machine media.
- Expected result: Text-only is accepted with evidence, or image work is explicitly triggered and scoped.
- Failure proves: Media could be omitted despite a comprehension gap or added without a need.
- Automation location: `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/media-decision.md`.

### RMB-M4. Visual-safety review for rowing media

- Covers: R33, R34, R35, R36, E5, EC7
- Level: manual
- Fixture/setup: Required only if media is added; use referenced images, nearby Markdown, provenance rows, prompt records, and alt text.
- Automation rationale: Media validators can check paths, provenance fields, prompt records, and alt-text presence, but human review is required to judge whether an image teaches one approved concept, matches Markdown, and avoids unsupported visual technique or safety meaning.
- Required environment: Local repository checkout with final referenced media files, `exercises/rowing-machine.md`, `media/PROVENANCE.md`, prompt records under `media/prompts/exercises/rowing-machine/` when generated raster media is used, and rendered or viewable image files.
- Evidence artifact: `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/visual-safety-review.md`, only if media is added.
- Steps: Review whether each image teaches one approved concept, matches Markdown, has no in-image text/citations/safety notes/red pain marks/diagnostic symbols/wrong-correct labels, avoids identifying people and misleading brands, and remains color-accessible.
- Pass condition: Each referenced image is approved with per-image evidence for concept, Markdown consistency, no prohibited visual elements, no identifying person or misleading brand, color accessibility, provenance/prompt-record support when required, and residual risk.
- Failure condition: Any image introduces unsupported technique, source-of-truth instructions, prohibited labels/marks/safety symbols, identifiable people, misleading brands, missing provenance or prompt records, or lacks a per-image decision.
- Owning stage: M3 optional media proof before media promotion and before M4 lifecycle evidence.
- Re-run trigger: Re-run after any media asset, alt text, nearby Markdown, provenance row, prompt record, or image purpose changes.
- Expected result: Each image is approved, revised, or removed before promotion.
- Failure proves: Media may introduce unsupported technique or safety meaning.
- Automation location: `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/visual-safety-review.md`, only if media is added.

### RMB-M5. Validation ledger and lifecycle handoff

- Covers: R37, R38
- Level: manual
- Fixture/setup: Use final M4 implementation state.
- Automation rationale: Individual commands can pass or fail automatically, but the lifecycle needs a durable human-readable ledger tying exact commands, outcomes, residual risks, and promotion/navigation decisions to the implementation state.
- Required environment: Local repository checkout at the M4 review-requested state with completed M1-M3 evidence, final content/media/source files, and local command output available for recording.
- Evidence artifact: `docs/changes/rowing-machine-basics-and-beginner-workouts/validation-ledger.md` plus plan and change metadata.
- Steps: Record exact commands, outcomes, residual risks, and whether README/navigation promotion is gated by proof evidence.
- Pass condition: Ledger names every command run, result, evidence summary, residual risk, CI observation status, promotion/navigation decision, and confirms no branch, PR, final verification, or CI-pass claim is made without evidence.
- Failure condition: Ledger omits required commands, records ambiguous outcomes, claims unobserved CI or branch/PR/final readiness, or promotes navigation before required proof passes.
- Owning stage: M4 lifecycle evidence before code-review handoff and later verify.
- Re-run trigger: Re-run after any implementation, test, source, media, proof, navigation, or validation-command change after the ledger is recorded.
- Expected result: Validation evidence is durable and does not claim CI, branch readiness, PR readiness, or final verification prematurely.
- Failure proves: The branch could be handed off with unverifiable readiness claims.
- Automation location: `docs/changes/rowing-machine-basics-and-beginner-workouts/validation-ledger.md` and plan/change metadata.

## Fixtures and data

- Fixture Markdown for `basic_cardio_equipment` on `exercises/rowing-machine.md`.
- Fixture Markdown for `basic_cardio_equipment` on an unrelated exercise page.
- Fixture Markdown for `loaded_carry` remaining inactive.
- Fixture Markdown for missing or empty cardio method labels.
- Fixture Markdown for forbidden all-out, sprint-first, maximal-damper, race-plan, schedule, challenge, HR-zone, weight-loss, diagnosis, rehab, coaching, and runtime-product language.
- Real page: `exercises/rowing-machine.md`.
- Source index: `SOURCES.md`.
- Safety reference: `RED-FLAGS.md`.
- Optional media fixtures under temporary test roots, following existing `tests/test_exercise_image_standard.py` patterns.
- Optional generated raster prompt-record fixture path:
  `media/prompts/exercises/rowing-machine/<asset-stem>.md`.

## Mocking/stubbing policy

No network calls are allowed in automated tests. External source pages are not
fetched during test execution; semantic source support is verified by manual
audit against cited sources. File-system fixtures should use temporary
directories for media/provenance prompt-record validation. No user accounts,
trackers, training logs, symptoms, medical history, body measurements, or
private reader data should be mocked because the product must not collect them.

## Migration or compatibility tests

- Existing exercise-method active values remain valid.
- `loaded_carry` remains inactive.
- Existing unselected exercise pages remain valid under their prior contract.
- Existing media and prompt-record contracts remain unchanged.
- Future treadmill, bike, elliptical, or other cardio-equipment pages cannot use
  this spec without approved downstream scope.
- Existing compatible `SOURCES.md` IDs should be reused when source-index rules
  require reuse.

## Observability verification

- Automated checks should report stable finding categories for method type,
  required section, forbidden scope, citation/source, internal-link, media path,
  provenance, prompt-record, page-reference, and privacy failures where those
  checks exist.
- Manual source audit records claim category, source, result, and residual risk.
- Manual beginner comprehension records non-identifying answers and revisions.
- Manual visual-safety review records per-image decisions if media is added.
- Validation ledger records exact commands and outcomes.
- Hosted CI is not reported unless observed later.

## Security/privacy verification

- Run privacy checks over content, media, prompt records, and change evidence.
- Beginner comprehension evidence must be non-identifying.
- Prompt records, provenance rows, and visual-safety evidence must avoid secrets,
  private data, and private health details.
- The page must not ask readers for symptoms, medical history, goals, body
  measurements, location, account details, or training logs.

## Performance checks

No runtime performance check is required because the change is static Markdown.
Validation should remain suitable for local documentation checks. A materially
long-running new command must be justified in the owning milestone before it
becomes a closeout gate.

## Manual QA checklist

- Confirm setup, stroke sequence, damper, beginner method, weekly activity, and
  stop-condition claims are cited and source-supported.
- Confirm the page teaches drive as legs, body, arms and recovery as arms, body,
  legs.
- Confirm beginner guidance starts easy, permits reset breaks, and progresses
  technique before time before effort.
- Confirm workout examples are examples, not a schedule, challenge, race plan,
  weight-loss promise, or personalized progression.
- Confirm central safety routing and stop conditions are complete.
- Confirm rowing is framed as aerobic work that does not replace strength work.
- Confirm text-only comprehension is sufficient or media is justified.
- If media is added, confirm visual-safety evidence, alt text, provenance,
  prompt records, and Markdown consistency.
- Confirm no private reader data, private health data, or identifying evidence
  is recorded.

## What not to test and why

- Do not test rowing performance, split times, 2k outcomes, weight loss, or
  heart-rate-zone accuracy; these are out of scope.
- Do not test personalized programming or adaptive coaching; the page must not
  provide those behaviors.
- Do not test clinical diagnosis, treatment, rehab, or return-to-training
  guidance; those are prohibited.
- Do not test hosted app behavior, calculators, trackers, APIs, accounts, or
  user-input flows; the implementation must not add them.
- Do not require images when manual evidence shows text-only guidance is
  sufficient.
- Do not use web fetching in tests; source support is a manual audit obligation.

## Uncovered gaps

None. All `MUST` requirements, examples, edge cases, compatibility claims,
observability obligations, and security/privacy boundaries have either
automation ownership or explicit manual proof ownership.

## Next artifacts

- Implement M1 method-boundary validation.
- Continue through M2 page/source drafting, M3 manual proof/media decision, and
  M4 validation ledger according to the approved plan.

## Follow-on artifacts

None yet.

## Readiness

This test spec is active after test-spec-review R2 approval.

It authorizes implementation handoff for M1 only. Code-review, explain-change,
verify, and PR handoff remain downstream gates before readiness claims.
