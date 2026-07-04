# Test Spec: Exercise Method Guidance

## Status

active

## Related spec and plan

- Spec: `specs/exercise-method-guidance.md`
- Spec review: `docs/changes/exercise-method-guidance/reviews/spec-review-r1.md`
- Plan: `docs/plans/2026-07-04-exercise-method-guidance.md`
- Plan review: `docs/changes/exercise-method-guidance/reviews/plan-review-r1.md`
- Architecture: `docs/architecture/system/architecture.md`
- Architecture review: `docs/changes/exercise-method-guidance/reviews/architecture-review-r1.md`
- Review log: `docs/changes/exercise-method-guidance/review-log.md`

## Testing strategy

Unit coverage extends the Markdown-first checker and template tests with
fixture-driven method-section parsing, allowed method types, required labels,
hidden-only metadata rejection, deferred method-type rejection, and forbidden
adaptive-programming language.

Integration coverage runs `tools/checks/check_markdown_first.py` against real
repository Markdown surfaces after each owning milestone. Real-page tests prove
the six proof-slice exercise pages exist, declare the required method types,
keep existing exercise-page sections, link the principle page where useful, and
do not contradict promoted pattern previews.

End-to-end coverage proves that a reader can move from an exercise page to the
shared principle page and still read the method guidance directly in Markdown
without generated HTML, a server, hidden metadata, or generated data.

Smoke coverage runs focused local commands after each milestone and the full
local command set during Lifecycle Closeout.

Manual coverage records source-audit samples and beginner-comprehension
evidence for requirements that cannot be proven by static parsing: source
support for concrete method claims, non-prescriptive tone, and reader
understanding that starter ranges are not a personal program.

Contract coverage treats the visible `## How much to do` heading and
`Method type:` line as the public Markdown contract. Checker output must use
file paths and stable failure categories for method-section, method-type,
label, metadata, forbidden-language, and preview-alignment failures.

Migration coverage is additive. Existing exercise pages not selected for this
proof slice remain valid under their prior contract until a later approved
slice selects them. Compatibility notes in related specs are checked only for
the focused-spec pointer and must not duplicate the method guidance contract.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | EMG-T1, EMG-T2, EMG-T6 | unit, integration | Template, fixtures, and proof-slice pages require `## How much to do`. |
| R2 | EMG-T2, EMG-T6 | unit, integration | Visible `Method type:` line is required on adopted exercise pages. |
| R3 | EMG-T2, EMG-T3, EMG-T6 | unit, integration | Active method enum is tested with valid, unknown, and deferred values. |
| R4 | EMG-T3, EMG-T13 | unit, contract | Hidden metadata cannot replace visible Markdown. |
| R5 | EMG-T3, EMG-T13 | unit, contract | If metadata exists, visible Markdown remains authoritative. |
| R6 | EMG-T1, EMG-T2, EMG-T6 | unit, integration | Required visible labels are checked in template, fixtures, and real pages. |
| R7 | EMG-T4, EMG-T7, EMG-M1 | unit, integration, manual | Static education wording is checked by forbidden language and manual tone review. |
| R8 | EMG-T4, EMG-M1 | unit, manual | Adaptive changes based on reader context fail. |
| R9 | EMG-T4, EMG-M1 | unit, manual | Diagnosis, treatment, rehab, correction promises, and guarantees fail. |
| R10 | EMG-T4, EMG-T6, EMG-M1 | unit, integration, manual | Stop language and safety routing are checked structurally and manually. |
| R11 | EMG-T5, EMG-M1 | integration, manual | Page-local source presence is automated; claim support is manually audited. |
| R12 | EMG-T5, EMG-M1 | integration, manual | Page-local source definitions must support sampled method claims. |
| R13 | EMG-T5, EMG-M1 | integration, manual | Global-only support is rejected for safety claims. |
| R14 | EMG-T6, EMG-M1 | integration, manual | Chest press method shape uses sets, reps, form, rest, and progression. |
| R15 | EMG-T6, EMG-M1 | integration, manual | Dynamic-resistance editorial default is checked on the proof page or justified by sources. |
| R16 | EMG-T6, EMG-M1 | integration, manual | Incline push-up shape uses reps or time, variation, and form-quality stop. |
| R17 | EMG-T6, EMG-M1 | integration, manual | Bodyweight-progression starter range is checked on the proof page or justified by sources. |
| R18 | EMG-T6, EMG-M1 | integration, manual | Chin nod shape uses short practice sets, slow reps or holds, and control-first progression. |
| R19 | EMG-T6, EMG-M1 | integration, manual | Low-load control starter range is checked on the proof page or justified by sources. |
| R20 | EMG-T6, EMG-M1 | integration, manual | Plank shape uses hold count, duration, breathing, rest, and form/breathing stop. |
| R21 | EMG-T6, EMG-M1 | integration, manual | Isometric hold starter range is checked on the proof page or justified by sources. |
| R22 | EMG-T6, EMG-M1 | integration, manual | Thoracic extension shape uses slow reps or comfortable holds without forced end range. |
| R23 | EMG-T6, EMG-M1 | integration, manual | Mobility starter range is checked on the proof page or justified by sources. |
| R24 | EMG-T6, EMG-M1 | integration, manual | Hip-flexor stretch shape uses duration, rounds, relaxed effort, no bouncing, and pain backoff. |
| R25 | EMG-T6, EMG-M1 | integration, manual | Stretch starter range is checked on the proof page or justified by sources. |
| R26 | EMG-T3, EMG-T6 | unit, integration | First slice rejects `loaded_carry` and `basic_cardio_equipment`. |
| R27 | EMG-T3, EMG-M3 | unit, manual | Later activation is out of scope and routed to future spec amendment. |
| R28 | EMG-T6 | integration | The six exact proof-slice files must exist and be checked. |
| R29 | EMG-T6 | integration | Each proof-slice page maps to the exact required method type. |
| R30 | EMG-T7 | integration | Principle page must be created or updated. |
| R31 | EMG-T7, EMG-M1 | integration, manual | Principle page covers sets, reps, holds, effort, rest, progression, and non-prescription framing. |
| R32 | EMG-T6, EMG-T7 | integration | Updated exercise pages should link to the principle page where method terms need explanation. |
| R33 | EMG-T8, EMG-M2 | integration, manual | Pattern previews with starter ranges should align with linked exercise pages. |
| R34 | EMG-T8 | integration | Contradictory promoted same-slice previews fail. |
| R35 | EMG-T8, EMG-M2 | integration, manual | Draft-only or incomplete preview behavior is checked when a linked exercise page is not adopted. |
| R36 | EMG-T1 | unit | Exercise template includes the method section before broad rollout. |
| R37 | EMG-T2, EMG-T3, EMG-T4, EMG-T8 | unit, integration | Validation covers section, enum, labels, forbidden phrases, and preview alignment where practical. |
| R38 | EMG-T2, EMG-T3, EMG-T4, EMG-T10 | unit, integration | Failures include file path and stable category. |
| R39 | EMG-M1 | manual | Source audit samples at least one page from each active method type before broad rollout. |
| R40 | EMG-M2 | manual | Beginner comprehension evidence covers starting point, effort, stop condition, and non-prescription understanding. |
| R41 | EMG-T9 | migration | Unselected existing exercise pages remain valid under prior contract. |
| R42 | EMG-T11 | migration | Related specs carry compatibility notes only where needed. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | EMG-T6, EMG-M1 | Chest press real-page check covers dynamic resistance method guidance. |
| E2 | EMG-T6, EMG-M1 | Kneeling hip-flexor stretch real-page check covers hold guidance instead of reps. |
| E3 | EMG-T3, EMG-T13 | Hidden metadata conflict fixture proves visible Markdown is authoritative. |
| E4 | EMG-T8 | Pattern preview alignment fixture and real-page check cover plank contradictions. |
| E5 | EMG-T4 | Adaptive-programming fixture rejects reader-context-based changes. |
| E6 | EMG-T6 | Proof-slice coverage check requires all six active method types. |
| E7 | EMG-T7, EMG-T6 | Principle-page existence and exercise-page links cover shared explanation. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | EMG-M1 | manual | Ambiguous method type requires one primary visible method type and source-supported plain-language context. |
| EC2 | EMG-T5, EMG-M1 | integration, manual | Editorial default without page-local source support fails source review. |
| EC3 | EMG-T4 | unit | Weekly routine wording fails as personal routine language. |
| EC4 | EMG-T4 | unit | Symptom-based substitution fails as injury-related adaptation. |
| EC5 | EMG-T2 | unit | Missing starter range or equivalent method content fails required label/content checks. |
| EC6 | EMG-T3 | unit | Deferred `loaded_carry` fails in first slice. |
| EC7 | EMG-T8 | integration | Plank reps preview contradicting isometric hold fails alignment. |
| EC8 | EMG-T3, EMG-T13 | unit, contract | YAML/front matter without visible `Method type:` fails. |
| EC9 | EMG-T6, EMG-M1 | integration, manual | Stretch page with sourced hold duration may pass if non-prescriptive and safely routed. |
| EC10 | EMG-T9 | migration | Unselected current exercise page remains valid under the previous contract. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Evidence artifact |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EMG-CMD1 | `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` | existing and configured; extended by M1 | tooling maintainer | M1 | M1 | Unexpected nonzero exit blocks M1 closeout. | M1 validation notes and code-review record. |
| EMG-CMD2 | `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | existing and configured; extended by M1 and M3 | tooling maintainer | M1, M3 | M1 | Unexpected nonzero exit blocks the owning milestone. | Milestone validation notes and code-review record. |
| EMG-CMD3 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises patterns principles` | existing and configured; extended by M1 | tooling maintainer | M1 | M1 | Unexpected nonzero exit blocks M1 closeout. | M1 validation notes and code-review record. |
| EMG-CMD4 | `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-method-guidance` | existing and configured | tooling maintainer | M1 | M1 | Any privacy finding or setup error blocks M1 closeout. | M1 validation notes and code-review record. |
| EMG-CMD5 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md principles` | existing and configured; may be extended by M2 | content/check maintainer | M2 | M2 | Unexpected nonzero exit blocks M2 closeout. | M2 validation notes and code-review record. |
| EMG-CMD6 | `python3 -m unittest tests.test_responsible_breadth_m1` | existing and configured; may be extended by M2 | tooling maintainer | M2 | M2 | Unexpected nonzero exit blocks M2 closeout. | M2 validation notes and code-review record. |
| EMG-CMD7 | `python3 tools/checks/check_privacy.py principles SOURCES.md docs/changes/exercise-method-guidance` | existing and configured | content/check maintainer | M2 | M2 | Any privacy finding or setup error blocks M2 closeout. | M2 validation notes and code-review record. |
| EMG-CMD8 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md principles exercises patterns` | existing and configured; extended by M3 | content/check maintainer | M3 | M3 | Unexpected nonzero exit blocks M3 closeout. | M3 validation notes and code-review record. |
| EMG-CMD9 | `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md principles exercises patterns docs/changes/exercise-method-guidance` | existing and configured | content/check maintainer | M3 | M3 | Any privacy finding or setup error blocks M3 closeout. | M3 validation notes and code-review record. |
| EMG-CMD10 | `python3 tools/checks/check_privacy.py docs/changes/exercise-method-guidance` | existing and configured | proof maintainer | M4 | M4 | Any privacy finding or setup error blocks M4 closeout. | M4 validation notes and code-review record. |
| EMG-CMD11 | `python3 -m unittest discover -s tests` | existing and configured | release/check maintainer | M4, Lifecycle Closeout | M4 | Unexpected nonzero exit blocks M4 or Lifecycle Closeout, depending on owning stage. | M4 validation notes, final validation ledger, and verify report. |
| EMG-CMD12 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md principles exercises patterns` | existing and configured | release/check maintainer | Lifecycle Closeout | Lifecycle Closeout | Unexpected nonzero exit blocks final local verification. | Final validation ledger and verify report. |
| EMG-CMD13 | `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md docs specs tools tests principles exercises patterns` | existing and configured | release/check maintainer | Lifecycle Closeout | Lifecycle Closeout | Any privacy finding or setup error blocks final local verification. | Final validation ledger and verify report. |
| EMG-CMD14 | `git diff --check` | existing and configured | release/check maintainer | Lifecycle Closeout | Lifecycle Closeout | Whitespace errors block final local verification. | Final validation ledger and verify report. |

## Milestone proof map

| Milestone | Test and proof IDs | Command IDs | Evidence artifact |
| --- | --- | --- | --- |
| M1 | EMG-T1, EMG-T2, EMG-T3, EMG-T4, EMG-T10, EMG-T11, EMG-T13 | EMG-CMD1, EMG-CMD2, EMG-CMD3, EMG-CMD4 | M1 validation notes and code-review record. |
| M2 | EMG-T7 | EMG-CMD5, EMG-CMD6, EMG-CMD7 | M2 validation notes and code-review record. |
| M3 | EMG-T5, EMG-T6, EMG-T8, EMG-T9 | EMG-CMD2, EMG-CMD8, EMG-CMD9 | M3 validation notes and code-review record. |
| M4 | EMG-M1, EMG-M2, EMG-M3, EMG-T12 | EMG-CMD10, EMG-CMD11 | Manual proof records, M4 validation notes, and code-review record. |
| Lifecycle Closeout | EMG-T12 | EMG-CMD11, EMG-CMD12, EMG-CMD13, EMG-CMD14 | Final validation ledger and verify report. |

## Test cases

### EMG-T1. Exercise template includes method section

- Covers: R1, R6, R36
- Level: unit
- Fixture/setup: Use `docs/templates/exercise-card.md`.
- Steps: Extend `tests/test_markdown_first_templates.py` to assert the template contains `## How much to do`, `Method type:`, `Beginner starting point:`, `Effort:`, `Rest:`, `Progression:`, and `Stop if:`.
- Expected result: The template contains the full visible method section shape.
- Failure proves: Contributors can start new exercise pages without the required method contract.
- Automation location: `tests/test_markdown_first_templates.py`

### EMG-T2. Method section parser accepts valid visible Markdown and rejects missing fields

- Covers: R1, R2, R3, R6, R37, R38, EC5
- Level: unit
- Fixture/setup: Add valid and invalid exercise fixtures under `tests/fixtures/markdown-first/exercise-method/`.
- Steps: Run focused checker tests with fixtures for a valid method section, missing heading, missing method type, missing required labels, missing starter range text, and unknown method value.
- Expected result: Valid fixture passes; invalid fixtures fail with file path and stable method-specific finding categories.
- Failure proves: Method guidance can be omitted or malformed without deterministic validation.
- Automation location: focused unittest file such as `tests/test_exercise_method_guidance.py`; `tools/checks/check_markdown_first.py`

### EMG-T3. Hidden metadata and deferred method types are rejected

- Covers: R3, R4, R5, R26, R27, R37, R38, E3, EC6, EC8
- Level: unit
- Fixture/setup: Add fixtures with YAML/front matter only, conflicting hidden metadata plus visible text, valid visible text plus non-authoritative metadata, `loaded_carry`, and `basic_cardio_equipment`.
- Steps: Run checker tests against the fixtures.
- Expected result: Hidden-only metadata fails; visible Markdown remains authoritative when both exist; deferred method types fail in the first slice.
- Failure proves: A second source of truth or deferred enum value can become active without spec approval.
- Automation location: `tests/test_exercise_method_guidance.py`; `tools/checks/check_markdown_first.py`

### EMG-T4. Forbidden adaptive programming and treatment language fails

- Covers: R7, R8, R9, R10, R37, R38, E5, EC3, EC4
- Level: unit
- Fixture/setup: Add fixtures containing reader-context adaptation, weekly routine commands, symptom-based substitutions, diagnosis/treatment/rehab wording, posture-correction promises, return-to-training guidance, and guarantee/fix wording.
- Steps: Run checker tests against the fixtures.
- Expected result: Forbidden fixtures fail with stable categories; neutral static education fixtures pass.
- Failure proves: Method guidance can drift into personalized programming or health advice.
- Automation location: `tests/test_exercise_method_guidance.py`; `tools/checks/check_markdown_first.py`

### EMG-T5. Page-local method source support surface is checkable

- Covers: R11, R12, R13, EC2
- Level: integration
- Fixture/setup: Add fixtures with page-local source definitions, global-only safety support, missing source definitions, and concrete method claims without nearby citations where detectable.
- Steps: Run checker tests under EMG-CMD3 where the fixture is available in M1 and EMG-CMD8 for real-page source checks after M3.
- Expected result: Page-local sources pass structurally; missing or global-only safety support fails; semantic claim support is routed to EMG-M1.
- Failure proves: Concrete method claims can be promoted without even structural source support.
- Automation location: `tests/test_exercise_method_guidance.py`; `tools/checks/check_markdown_first.py`; EMG-M1

### EMG-T6. Six proof-slice exercise pages satisfy method contracts

- Covers: R1-R29, R32, R41, E1, E2, E6, E7, EC9
- Level: integration
- Fixture/setup: Use real pages `exercises/chest-press.md`, `exercises/incline-push-up.md`, `exercises/chin-nod.md`, `exercises/plank.md`, `exercises/thoracic-extension.md`, and `exercises/kneeling-hip-flexor-stretch.md` after M3.
- Steps: Run real-page tests and EMG-CMD8.
- Expected result: All six pages exist, keep the exercise-page contract, include `## How much to do`, declare the exact required method type, use the required method-shape labels, and avoid deferred method types.
- Failure proves: The first proof slice does not cover the active method menu or has broken exercise-page contracts.
- Automation location: `tests/test_markdown_first_real_pages.py`; `tests/test_exercise_method_guidance.py`; `tools/checks/check_markdown_first.py`

### EMG-T7. Principle page exists and explains shared method concepts

- Covers: R30, R31, R32, E7
- Level: integration
- Fixture/setup: Use `principles/sets-reps-holds-rest-and-progression.md` after M2.
- Steps: Run EMG-CMD5 and tests asserting the page contains sets, repetitions, timed holds, effort scale, rest, one-variable progression, and non-prescription framing.
- Expected result: Principle page exists, passes the principle-page contract, has page-local sources, and is linkable from updated exercise pages.
- Failure proves: Exercise pages must repeat long explanations or link to a missing/insufficient principle page.
- Automation location: `tests/test_responsible_breadth_m1.py`; `tests/test_exercise_method_guidance.py`; `tools/checks/check_markdown_first.py`

### EMG-T8. Pattern previews do not contradict linked exercise method guidance

- Covers: R33, R34, R35, R37, E4, EC7
- Level: integration
- Fixture/setup: Add fixtures for aligned preview, contradictory plank reps preview, preview linking to a missing or not-yet-adopted exercise page, and draft-only/incomplete preview wording.
- Steps: Run checker tests and EMG-CMD8 real-page checks against `patterns` and `exercises`.
- Expected result: Contradictory promoted previews fail; aligned previews pass; non-adopted exercise previews are draft-only or avoid complete exercise-instruction framing.
- Failure proves: Pattern pages can teach a starter range that conflicts with the full exercise page.
- Automation location: `tests/test_exercise_method_guidance.py`; `tools/checks/check_markdown_first.py`; EMG-M2 for semantic review

### EMG-T9. Unselected exercise pages remain compatible

- Covers: R41, EC10
- Level: integration
- Fixture/setup: Use current exercise pages not selected for the first proof slice.
- Steps: Run EMG-CMD3 after M1 and EMG-CMD8 after M3.
- Expected result: Unselected exercise pages do not fail solely because they lack `## How much to do`; if they voluntarily include the section, the section must satisfy the method contract.
- Failure proves: The additive migration breaks existing exercise pages before they are selected for rollout.
- Automation location: `tests/test_markdown_first_real_pages.py`; `tools/checks/check_markdown_first.py`

### EMG-T10. Checker reports stable method-finding categories

- Covers: R38
- Level: unit
- Fixture/setup: Reuse invalid fixtures from EMG-T2, EMG-T3, EMG-T4, and EMG-T8.
- Steps: Under EMG-CMD2, assert stderr/stdout or checker result objects include file paths and stable categories for missing section, missing method type, inactive method type, missing labels, hidden-only metadata, forbidden adaptive programming, and preview contradiction.
- Expected result: Each failure is identifiable by file path and stable category.
- Failure proves: Authors and reviewers cannot triage method guidance failures reliably.
- Automation location: `tests/test_exercise_method_guidance.py`; `tools/checks/check_markdown_first.py`

### EMG-T11. Compatibility notes point to the focused spec without duplicating rules

- Covers: R42
- Level: manual
- Fixture/setup: Use `specs/markdown-first-primer.md` and `specs/responsible-breadth.md` after M1.
- Steps: Inspect or, when assertions are added, run under EMG-CMD2 to verify that any added compatibility note names `specs/exercise-method-guidance.md` as the normative home and does not duplicate active method enum or starter-range tables.
- Expected result: Related specs route readers to the focused spec only where needed.
- Failure proves: The method guidance contract can split across multiple normative sources.
- Automation location: manual inspection in code review or focused text assertions if compatibility notes are added

### EMG-T12. Final local validation command set passes

- Covers: AC1-AC10
- Level: smoke
- Fixture/setup: Full repository after M4 and before Lifecycle Closeout.
- Steps: Run EMG-CMD11, EMG-CMD12, EMG-CMD13, and EMG-CMD14.
- Expected result: All commands pass locally, or any unavailable command is recorded as a validation gap with residual risk.
- Failure proves: The reviewed implementation cannot be handed to final verification.
- Automation location: Lifecycle Closeout validation notes and verify report

### EMG-T13. Visible Markdown source of truth remains authoritative

- Covers: R4, R5, E3, EC8
- Level: unit
- Fixture/setup: Fixtures with visible method type only, hidden metadata only, and visible/hidden conflict.
- Steps: Run parser-level tests that read only visible Markdown for the authoritative method type.
- Expected result: Visible-only passes; hidden-only fails; visible/hidden conflict uses visible value for method-type classification and fails only if the visible value is invalid.
- Failure proves: The architecture boundary can silently move from Markdown source to hidden metadata.
- Automation location: `tests/test_exercise_method_guidance.py`; `tools/checks/check_markdown_first.py`

### EMG-M1. Manual source and non-prescription audit

- Covers: R7-R25, R39, EC1, EC2, EC9
- Level: manual
- Fixture/setup: Use the final six proof-slice exercise pages and their page-local source lists after M3.
- Automation rationale: Static checks can verify headings, labels, source sections, and citations, but cannot prove each public source supports a concrete amount, effort, rest, progression, or safety claim at the level made.
- Required environment: Local repository checkout after M3 with the six proof-slice exercise pages, `SOURCES.md`, page-local source links, and public source URLs available for reviewer inspection.
- Evidence artifact: `docs/changes/exercise-method-guidance/manual-proof/method-source-audit.md`
- Steps: Record the evidence artifact; sample at least one page from each active method type; verify concrete amount, effort, rest, progression, and safety claims against page-local sources; record whether wording is static education rather than personal prescription.
- Pass condition: Every active method type has a sampled source-support result; sampled concrete claims are supported by page-local sources or removed; wording is recorded as static education rather than a personal prescription; residual risk is named.
- Failure condition: Any active method type lacks a sampled page, a sampled concrete claim is unsupported, a method claim relies only on `SOURCES.md`, or wording reads as an instruction adapted to the reader.
- Owning stage: M4 implementation and M4 code-review.
- Re-run trigger: Any edit to proof-slice method guidance, method sources, source citations, starter ranges, stop guidance, or method type assignment.
- Expected result: Every active method type has a sampled source-support result, unsupported claims are removed or recited, and residual risk is recorded.
- Failure proves: Method guidance can be structurally valid but semantically unsupported or prescriptive.
- Automation location: manual proof record; code-review must cite the EMG-M1 outcome

### EMG-M2. Manual beginner comprehension proof

- Covers: R33-R40, E4
- Level: manual
- Fixture/setup: Use the six proof-slice exercise pages and any promoted pattern previews after M3.
- Automation rationale: Static checks can confirm method-section structure, but cannot prove a beginner understands the starting point, effort, stop condition, or non-prescription boundary.
- Required environment: Local repository checkout after M3 with proof-slice exercise pages readable as plain Markdown; a non-identifying beginner reader or equivalent reviewer profile; no collection of private health details.
- Evidence artifact: `docs/changes/exercise-method-guidance/manual-proof/beginner-comprehension.md`
- Steps: Record the evidence artifact; ask a non-identifying beginner reader to identify the starting point, effort, stop condition, and whether the page is a personal program; record preview-alignment confusion if present.
- Pass condition: Evidence records each proof-slice page or sampled page result for starting point, effort, stop condition, and non-prescription understanding; any reader confusion has a recorded content change or residual-risk disposition.
- Failure condition: The reader cannot identify the required concepts, interprets the page as a personal program, or reports preview/full-page contradiction without a recorded fix or disposition.
- Owning stage: M4 implementation and M4 code-review.
- Re-run trigger: Any edit to proof-slice method wording, pattern-preview wording, principle-page links, or stop/progression language after the comprehension record is created.
- Expected result: Evidence shows the reader can explain the required concepts or names page-specific revisions before closeout.
- Failure proves: The method section may pass static checks but still fail the beginner use case.
- Automation location: manual proof record; code-review must cite the EMG-M2 outcome

### EMG-M3. Deferred method type guardrail review

- Covers: R27
- Level: manual
- Fixture/setup: Inspect final diff and proof-slice pages.
- Automation rationale: Automated enum checks can reject deferred values in parsed pages, but final review must ensure templates, docs, fixtures, and source-of-truth text do not accidentally promote deferred method types as active guidance.
- Required environment: Local repository checkout after M4 with final diff, templates, proof-slice pages, test fixtures, and specs available.
- Evidence artifact: `docs/changes/exercise-method-guidance/manual-proof/validation-ledger.md`
- Steps: Confirm no content page, template, test fixture promoted as valid content, or source-of-truth list activates `loaded_carry` or `basic_cardio_equipment`; record any mention as deferred or invalid-test-only.
- Pass condition: Deferred method types appear only as rejected fixture values, deferred examples, or future-scope notes, and no promoted exercise page declares them.
- Failure condition: Any promoted page, template starter example, valid fixture, or normative source-of-truth list treats `loaded_carry` or `basic_cardio_equipment` as active in this slice.
- Owning stage: M4 implementation and M4 code-review.
- Re-run trigger: Any edit to method type lists, templates, fixtures, proof-slice pages, or related specs after the ledger is created.
- Expected result: Deferred method types remain inactive unless a later approved spec amendment exists.
- Failure proves: Future method categories were activated without upstream approval.
- Automation location: code-review note or manual proof record

## Fixtures and data

- `tests/fixtures/markdown-first/exercise-method/valid-dynamic-resistance.md`
- `tests/fixtures/markdown-first/exercise-method/valid-stretch-hold.md`
- `tests/fixtures/markdown-first/exercise-method/missing-how-much.md`
- `tests/fixtures/markdown-first/exercise-method/missing-method-type.md`
- `tests/fixtures/markdown-first/exercise-method/missing-required-labels.md`
- `tests/fixtures/markdown-first/exercise-method/hidden-only-method-type.md`
- `tests/fixtures/markdown-first/exercise-method/conflicting-hidden-visible-method-type.md`
- `tests/fixtures/markdown-first/exercise-method/inactive-method-type.md`
- `tests/fixtures/markdown-first/exercise-method/deferred-loaded-carry.md`
- `tests/fixtures/markdown-first/exercise-method/adaptive-programming.md`
- `tests/fixtures/markdown-first/exercise-method/treatment-or-rehab.md`
- `tests/fixtures/markdown-first/exercise-method/global-only-method-safety.md`
- `tests/fixtures/markdown-first/exercise-method/pattern-preview-aligned.md`
- `tests/fixtures/markdown-first/exercise-method/pattern-preview-contradiction.md`

Fixture names are suggestions; implementation may use temporary-root fixtures
inside unittest if that better matches existing test style. Fixture content must
stay synthetic and contain no private health data.

Real-page data:

- `docs/templates/exercise-card.md`
- `principles/sets-reps-holds-rest-and-progression.md`
- `exercises/chest-press.md`
- `exercises/incline-push-up.md`
- `exercises/chin-nod.md`
- `exercises/plank.md`
- `exercises/thoracic-extension.md`
- `exercises/kneeling-hip-flexor-stretch.md`
- `patterns/*.md` when they preview proof-slice exercises
- `SOURCES.md`
- `RED-FLAGS.md`

Manual proof records:

- `docs/changes/exercise-method-guidance/manual-proof/method-source-audit.md`
- `docs/changes/exercise-method-guidance/manual-proof/beginner-comprehension.md`
- `docs/changes/exercise-method-guidance/manual-proof/validation-ledger.md`

## Mocking/stubbing policy

Do not mock Markdown file reading, source parsing, or checker CLI execution for
integration tests. Unit tests may use temporary directories or synthetic
fixtures to isolate invalid method sections and preview contradictions. Do not
mock public source content for semantic support; source adequacy is a manual
review obligation.

No network access is required for automated tests. Manual source audit may open
public source URLs, but the proof record should summarize the support checked
without copying long source passages.

## Migration or compatibility tests

- EMG-T9 proves unselected exercise pages remain valid under their prior
  contract and are not forced to adopt `## How much to do` in this slice.
- EMG-T11 proves related specs point to the focused method spec without
  creating a second normative contract.
- EMG-T3 and EMG-M3 prove deferred method types remain inactive until later
  approved spec work.
- Rollback is Markdown-only: removing or narrowing a bad method section must
  restore the prior exercise-page contract for that page unless the page remains
  selected in the proof slice.

## Observability verification

Automated checker output must include file paths and stable method-specific
categories for:

- missing `## How much to do`;
- missing `Method type:`;
- inactive or deferred method type;
- missing visible labels;
- hidden-only method metadata;
- forbidden adaptive programming or treatment language;
- deterministic pattern-preview contradiction where practical.

Manual evidence must identify checked files, requirement IDs or test IDs,
result, reviewer role, non-identifying reader type for comprehension evidence,
and residual validation gaps.

## Security/privacy verification

Run privacy scans on content, tests, tools, specs, and proof records as named in
EMG-CMD4, EMG-CMD7, EMG-CMD9, EMG-CMD10, and EMG-CMD13. Fixture and proof data
must not include private health information, reader identities, secrets,
credentials, private machine paths, private contact details, or training logs.

Method guidance must not invite readers to submit symptoms, injuries, goals,
medical history, body measurements, or training response data.

## Performance checks

No runtime performance requirement applies. Local checker and unittest additions
should remain suitable for normal repository validation. Lifecycle Closeout runs
the full local unittest suite and content checker; any meaningful slowdown or
unavailable tool must be recorded in validation notes.

## Manual QA checklist

- Confirm all six active method types are represented once in the proof slice.
- Confirm each proof-slice page has page-local source support for sampled
  concrete method claims.
- Confirm method wording reads as static education, not a personal command.
- Confirm broader safety routing points to `RED-FLAGS.md` when pain, symptoms,
  or professional care are mentioned.
- Confirm pattern previews do not contradict linked exercise pages.
- Confirm beginner-comprehension evidence covers starting point, effort, stop
  condition, and non-prescription understanding.
- Confirm broad rollout is not claimed or started by this proof slice.

## What not to test and why

- Do not test personalized programming outcomes, because personalized plans are
  out of scope.
- Do not test medical diagnosis, treatment, rehab, return-to-training, or
  symptom-substitution behavior, because those are forbidden boundaries rather
  than supported features.
- Do not test `loaded_carry` or `basic_cardio_equipment` as valid active method
  types; test only that they remain rejected or explicitly deferred.
- Do not test generated public data, hidden taxonomy files, YAML front matter as
  source of truth, APIs, databases, analytics, accounts, or hosted behavior,
  because the architecture explicitly excludes them.
- Do not verify semantic source support using static parsing alone; use manual
  source audit for that proof.
- Do not require every existing exercise page to adopt method guidance in this
  first slice.

## Uncovered gaps

None requiring return to spec or architecture. Semantic source support and
beginner comprehension are intentionally manual proof obligations in EMG-M1 and
EMG-M2.

## Next artifacts

- M1 implementation from `docs/plans/2026-07-04-exercise-method-guidance.md`.
- Code-review after each implementation milestone records validation evidence
  against this active proof map.

## Follow-on artifacts

None yet.

## Readiness

Active proof map for implementation. M1 implementation may start from
`docs/plans/2026-07-04-exercise-method-guidance.md`; final closeout still
requires milestone implementation, code-review, explain-change, verify, and PR
handoff.
