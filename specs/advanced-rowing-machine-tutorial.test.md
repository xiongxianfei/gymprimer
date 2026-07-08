# Test Spec: Advanced Rowing Machine Tutorial

## Status

active

## Related spec and plan

- Spec: `specs/advanced-rowing-machine-tutorial.md`
- Spec review: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/spec-review-r1.md`
- Plan: `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`
- Plan review: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/plan-review-r1.md`
- Architecture: `docs/architecture/system/architecture.md`
- Architecture review: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/architecture-review-r1.md`

## Input artifact identities

| Input | Path | Status / Review state | Identity |
| --- | --- | --- | --- |
| Proposal | `docs/proposals/2026-07-07-advanced-rowing-machine-tutorial.md` | accepted | Proposal status normalized after proposal-review R1. |
| Spec | `specs/advanced-rowing-machine-tutorial.md` | approved | Spec-review R1 approved with no material findings. |
| Architecture | `docs/architecture/system/architecture.md` | approved | Architecture-review R1 approved the canonical amendment. |
| Plan | `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md` | reviewed | Plan-review R2 approved the TSR1 fixture-command correction. |
| Review log | `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md` | current | Proposal, spec, architecture, and plan reviews are recorded. |

## Testing strategy

Unit coverage extends checker fixtures before production content exists.
M1 tests prove the advanced rowing page contract, scoped image exception, prompt-packet shape, force-intensity overlay metadata, and forbidden wording with fixtures and existing media/provenance checks.

Integration coverage checks real repository artifacts as they appear.
M2 checks the Markdown page, source support, beginner-page link, method type, required sections, static examples, and forbidden scope.
M3 checks media references, prompt records, provenance rows, technical diagram label duplication, and force-intensity Markdown integration.

End-to-end coverage remains repository-native.
Readers must be able to open `exercises/rowing-machine-advanced.md` as Markdown, follow the beginner-page link, inspect sources, and understand that the page is static education.

Manual coverage is required for source adequacy, visual semantics, grayscale distinguishability, and advanced-reader comprehension because static checks cannot prove those judgments.

Migration coverage is additive.
The beginner page remains valid, unrelated exercise image limits remain unchanged, and no new method type is activated.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1-R4 | ART-T1, ART-T2 | integration | Beginner page preservation, advanced path, Markdown-only use, and downstream link behavior. |
| R5-R7 | ART-T2 | integration | Required headings and prerequisite editorial boundary. |
| R8-R9, R47-R48 | ART-T3, ART-T12 | contract | Advanced literacy, no coaching, no runtime product, no clinical or competition-programming scope. |
| R10-R15 | ART-T4, ART-MP1 | integration, manual | Damper, drag factor, monitor metrics, stroke rate, and force curve claims. |
| R16-R19 | ART-T5, ART-T12 | integration, contract | Static workout examples, benchmark boundary, method type, and no new subtype. |
| R20-R21 | ART-T6, ART-MP1 | integration, manual | Page-local citations and `SOURCES.md` reuse. |
| R22-R24 | ART-T7, ART-T8 | unit, integration | Scoped eight-image exception and one teaching purpose per image. |
| R25-R29 | ART-T8, ART-T9 | integration | Provenance rows, prompt records, image-instruction packet fields, and force maps. |
| R30-R32 | ART-T10 | integration | Which images may or must not use force-intensity overlays. |
| R33-R38 | ART-T10, ART-MP3 | integration, manual | 0-3 relative scale, non-measurement wording, non-color cues, grayscale review, and palette boundary. |
| R39-R44 | ART-T11, ART-MP2 | integration, manual | Label restrictions, technical diagram exception, image exclusions, alt text, legend, and phase explanation. |
| R45-R46 | ART-MP2, ART-MP3 | manual | Visual-safety review and force-overlay grayscale review. |
| R49 | ART-MP4 | manual | Advanced-reader comprehension proof. |
| R50 | ART-T13 | smoke | Exact validation commands and outcomes before completion claims. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | ART-T1, ART-T2 | Beginner page stays focused and only links to the advanced page after approval. |
| E2 | ART-T2 | Prerequisite text is present and framed as editorial scope. |
| E3 | ART-T4, ART-T12 | Monitor concepts stay static and do not calculate personal targets. |
| E4 | ART-T10, ART-MP3 | Force-intensity overlay has relative-scale wording and no measurement claim. |
| E5 | ART-T8, ART-T9 | Generated image reference requires matching prompt packet and force map when applicable. |
| E6 | ART-T11 | Technical diagram labels are minimal and duplicated in Markdown and alt text. |
| E7 | ART-T5, ART-T12 | Workout examples remain static and benchmark prep links official plans or stays conceptual. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | ART-T2 | integration | Advanced page prerequisites route expectations back to beginner stroke sequence. |
| EC2 | ART-T11 | integration | Technical labels may be allowed only with Markdown and alt-text duplication. |
| EC3 | ART-T11 | integration | Body and muscle images remain label-free. |
| EC4 | ART-MP3 | manual | Grayscale failure blocks force-overlay promotion. |
| EC5 | ART-MP1, ART-MP3 | manual | Force map must narrow or revise when source audit or visual review finds mismatch. |
| EC6 | ART-T10 | integration | `stroke-rate-ladder.png` force overlay requires recorded downstream rationale. |
| EC7 | ART-T9 | integration | Missing force map in a force-overlay packet blocks asset promotion. |
| EC8 | ART-T5, ART-T12 | contract | Benchmark prep cannot become a full plan. |
| EC9 | ART-T5, ART-T12 | contract | Interval examples remain static, not adaptive. |
| EC10 | ART-MP2 | manual | Image may be deferred when text is sufficient. |
| EC11 | ART-T7 | unit | Other exercise pages still need their own approved image-count exception. |
| EC12 | ART-MP1 | manual | Source audit narrows claims when a source does not support the exact indoor-rowing claim. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ART-CMD1 | `python3 -m unittest discover -s tests` | existing/configured | implementer | M1-M4 | M1 | Nonzero exit blocks milestone closeout. | Zero discovered tests fail the command purpose and block closeout. | Milestone validation notes and code-review record. | Local read/write test execution only. |
| ART-CMD2 | `python3 tools/checks/check_markdown_first.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md` | planned-for-implementation | checker maintainer | M1 | M1 | Nonzero exit blocks M1 except when unittest intentionally asserts invalid fixture failure behavior. | Not applicable. | M1 validation notes and code-review record. | Local static scan over this change's fixture directory only. |
| ART-CMD3 | `python3 tools/checks/check_privacy.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | existing/configured | implementer | M1 | M1 | Any privacy finding blocks M1 closeout. | Not applicable. | M1 validation notes. | Local static scan over this change's fixture directory only. |
| ART-CMD4 | `python3 tools/checks/check_markdown_first.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md` | planned-for-implementation | content/checker maintainer | M2 | M2 | Nonzero exit blocks M2 closeout. | Not applicable. | M2 validation notes and code-review record. | Local static scan only. |
| ART-CMD5 | `python3 tools/checks/check_privacy.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | existing/configured | implementer | M2 | M2 | Any privacy finding blocks M2 closeout. | Not applicable. | M2 validation notes. | Local static scan only. |
| ART-CMD6 | `python3 tools/checks/check_markdown_first.py exercises/rowing-machine-advanced.md media/PROVENANCE.md media/prompts/exercises/rowing-machine-advanced` | planned-for-implementation | media/checker maintainer | M3 | M3 | Nonzero exit blocks generated media promotion. | Not applicable. | M3 validation notes and code-review record. | Local static scan only. |
| ART-CMD7 | `python3 tools/checks/check_privacy.py exercises/rowing-machine-advanced.md media/prompts/exercises/rowing-machine-advanced media/PROVENANCE.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | existing/configured | implementer | M3 | M3 | Any privacy finding blocks M3 closeout. | Not applicable. | M3 validation notes. | Local static scan only. |
| ART-CMD8 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | planned-for-implementation | release/checker maintainer | M4 | M4 | Nonzero exit blocks M4 unless recorded as unrelated pre-existing validation gap and accepted by code-review. | Not applicable. | M4 validation ledger and code-review record. | Local static scan only. |
| ART-CMD9 | `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md RED-FLAGS.md exercises media docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | existing/configured | implementer | M4 | M4 | Any privacy finding blocks M4 closeout. | Not applicable. | M4 validation ledger. | Local static scan only. |
| ART-CMD10 | `git diff --check` | existing/configured | implementer | M1-M4 | M1 | Whitespace errors block milestone closeout. | Not applicable. | Milestone validation notes. | Local git working-tree check only. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | ART-T7, ART-T8, ART-T9, ART-T10, ART-T11, ART-T12 | none | ART-CMD1, ART-CMD2, ART-CMD3, ART-CMD10 | M1 validation notes and code-review record | M1 code-review | Fixture tests prove validation before production page and media exist. |
| M2 | ART-T1, ART-T2, ART-T3, ART-T4, ART-T5, ART-T6, ART-T12 | ART-MP1 | ART-CMD1, ART-CMD4, ART-CMD5, ART-CMD10 | M2 validation notes, source-audit evidence, code-review record | M2 code-review | Real page and beginner-page link become testable here. |
| M3 | ART-T7, ART-T8, ART-T9, ART-T10, ART-T11 | ART-MP2, ART-MP3 | ART-CMD1, ART-CMD6, ART-CMD7, ART-CMD10 | prompt packets, provenance rows, visual-safety evidence, grayscale review | M3 code-review | Only images selected by implementation are required; deferred images need no asset proof. |
| M4 | ART-T13 | ART-MP1, ART-MP2, ART-MP3, ART-MP4 | ART-CMD1, ART-CMD8, ART-CMD9, ART-CMD10 | final validation ledger, manual proof records, code-review record | M4 code-review | M4 closes manual and validation evidence before downstream explain-change and verify. |

## Test cases

### ART-T1. Beginner page remains the entry point

- Covers: R1, R4, E1
- Level: integration
- Command IDs: ART-CMD4
- Fixture/setup: Real `exercises/rowing-machine.md` and `exercises/rowing-machine-advanced.md`.
- Steps: Check that the beginner page remains present, keeps beginner-focused content, and links to `rowing-machine-advanced.md` only after the advanced page exists and validates.
- Expected result: Beginner page is preserved and advanced navigation is a bottom-page companion link.
- Failure proves: The implementation overloaded or displaced the beginner page.
- Evidence artifact: M2 validation notes.
- Automation location: `tests/test_markdown_first_real_pages.py` or a focused advanced rowing test module.
- Required by milestone: M2.

### ART-T2. Advanced page shape and prerequisite boundary

- Covers: R2, R3, R5, R6, R7, E2, EC1
- Level: integration
- Command IDs: ART-CMD4
- Fixture/setup: Real `exercises/rowing-machine-advanced.md`.
- Steps: Assert the H1, required top-level sections, Markdown-only nature, and prerequisite text including 10-15 minutes and legs -> body -> arms then arms -> body -> legs.
- Expected result: Required sections exist and the prerequisite is editorial, not a medical or performance test.
- Failure proves: The page contract is incomplete or the scope boundary is misleading.
- Evidence artifact: M2 validation notes.
- Automation location: focused advanced rowing real-page test.
- Required by milestone: M2.

### ART-T3. Scope and product boundary rejection

- Covers: R8, R9, R47, R48
- Level: contract
- Command IDs: ART-CMD1, ART-CMD4
- Fixture/setup: Invalid fixture pages plus real advanced page.
- Steps: Run checker tests against wording for personalization, adaptive programming, race strategy, clinical judgment, hosted tools, trackers, calculators, PM5 data analysis, video product, and coaching engine.
- Expected result: Invalid fixtures fail; real page avoids forbidden scope.
- Failure proves: The implementation can become a coach, product surface, or clinical workflow.
- Evidence artifact: M1 and M2 validation notes.
- Automation location: checker fixture tests and real-page scan.
- Required by milestone: M1, M2.

### ART-T4. Advanced rowing concepts are source-backed

- Covers: R10, R11, R12, R13, R14, R15, E3
- Level: integration
- Command IDs: ART-CMD4
- Fixture/setup: Real advanced page and `SOURCES.md`.
- Steps: Check sections for damper versus drag factor, no damper-10 superiority, split, watts, stroke rate, distance/time, force curve, higher rate not automatically better, and force curve as feedback rather than verdict.
- Expected result: Concepts are present with page-local citations and no personal targets.
- Failure proves: The page under-teaches monitor literacy or overstates technique feedback.
- Evidence artifact: M2 validation notes and ART-MP1.
- Automation location: focused advanced rowing real-page test.
- Required by milestone: M2.

### ART-T5. Workout examples stay static

- Covers: R16, R17, R18, R19, E7, EC8, EC9
- Level: integration
- Command IDs: ART-CMD4
- Fixture/setup: Real advanced page and invalid fixtures.
- Steps: Check steady rows, rate ladders, power-per-stroke, intervals, and benchmark prep wording; reject adaptive progression, full benchmark plans, race strategy, and `advanced_basic_cardio_equipment`.
- Expected result: Examples are static literacy and use `basic_cardio_equipment` when method-style labels appear.
- Failure proves: The page has become a training plan or unsupported method subtype.
- Evidence artifact: M2 validation notes.
- Automation location: focused advanced rowing real-page test and checker fixtures.
- Required by milestone: M2.

### ART-T6. Sources and source-index reuse

- Covers: R20, R21
- Level: integration
- Command IDs: ART-CMD4
- Fixture/setup: Real advanced page and `SOURCES.md`.
- Steps: Verify page-local source definitions for concrete advanced claims and global source-index entries where current rules require reused IDs.
- Expected result: Concrete claims are auditable locally and reused source IDs are globally consistent.
- Failure proves: Claims cannot be reviewed or source IDs drift from repository rules.
- Evidence artifact: M2 validation notes and ART-MP1.
- Automation location: Markdown-first checker and focused source tests.
- Required by milestone: M2.

### ART-T7. Scoped image-rich exception

- Covers: R22, R23, R24, EC10, EC11
- Level: unit
- Command IDs: ART-CMD1, ART-CMD2, ART-CMD6
- Fixture/setup: Valid and invalid advanced rowing fixtures plus unrelated exercise fixtures.
- Steps: Confirm only `exercises/rowing-machine-advanced.md` may use up to eight first-batch asset paths and unrelated exercise pages still fail without their own exception.
- Expected result: The exception is exact, page-scoped, and image paths are limited to the approved list.
- Failure proves: Image limits are raised too broadly or the approved batch is not enforced.
- Evidence artifact: M1 and M3 validation notes.
- Automation location: checker unit tests.
- Required by milestone: M1, M3.

### ART-T8. Media provenance and one-purpose image checks

- Covers: R24, R25, R26, R27, R28
- Level: integration
- Command IDs: ART-CMD6
- Fixture/setup: Referenced image assets, prompt packet files, and `media/PROVENANCE.md`.
- Steps: Match each page image reference to a local asset, prompt packet, approved provenance row, page reference, media purpose, instructional layer, teaching goal, visual rules, exact prompt, and review notes.
- Expected result: Every promoted generated image has one teaching purpose and complete packet/provenance evidence.
- Failure proves: Media promotion is undocumented, unreviewable, or disconnected from Markdown.
- Evidence artifact: M3 validation notes, prompt packets, provenance rows.
- Automation location: checker tests and media/provenance validation.
- Required by milestone: M1, M3.

### ART-T9. Force map packet requirement

- Covers: R29, E5, EC7
- Level: integration
- Command IDs: ART-CMD6
- Fixture/setup: Force-overlay and non-force-overlay prompt packet fixtures.
- Steps: Confirm force-overlay packets include a force-intensity map and non-force images either omit the map or state why no map applies.
- Expected result: Force-overlay assets cannot be promoted without a reviewable broad phase map.
- Failure proves: The visual layer can become unsupported or unauditable.
- Evidence artifact: M3 validation notes and prompt packets.
- Automation location: checker tests.
- Required by milestone: M1, M3.

### ART-T10. Force-intensity overlay boundaries

- Covers: R30, R31, R32, R33, R34, R35, R36, R37, R38, E4, EC4, EC5, EC6
- Level: integration
- Command IDs: ART-CMD6
- Fixture/setup: Advanced page image references, nearby Markdown, prompt packets, and provenance notes.
- Steps: Check which image stems may use overlays, enforce no overlays on monitor, damper, and interval images, require 0-3 relative scale wording, non-measurement text, non-color cues, grayscale-review evidence, no red pain-map styling, and rationale for any stroke-rate-ladder overlay.
- Expected result: Force overlays are explicitly relative, accessible, and limited to accepted images.
- Failure proves: The implementation implies exact force, uses color-only meaning, or applies overlays outside the approved scope.
- Evidence artifact: M3 validation notes and ART-MP3.
- Automation location: checker tests plus manual grayscale review.
- Required by milestone: M1, M3.

### ART-T11. Label, alt-text, and excluded-image checks

- Covers: R39, R40, R41, R42, R43, R44, E6, EC2, EC3
- Level: integration
- Command IDs: ART-CMD6
- Fixture/setup: Advanced page Markdown, image references, alt text, prompt packets, and invalid fixtures.
- Steps: Reject in-image labels for body/movement/muscle/force images, allow minimal technical diagram labels only when duplicated in Markdown and alt text, and reject screenshots, copied PM5 UI, brand marks, identifiable people, badges, red pain marks, race-win framing, and unsupported promises.
- Expected result: Images remain support assets with meaningful alt text and nearby explanations.
- Failure proves: Media semantics are inaccessible, copied, branded, misleading, or unsupported.
- Evidence artifact: M3 validation notes and ART-MP2.
- Automation location: checker tests plus manual visual review.
- Required by milestone: M1, M3.

### ART-T12. Forbidden-scope fixtures

- Covers: R8, R9, R13, R15, R16, R17, R47, R48, E3, E7, EC8, EC9
- Level: contract
- Command IDs: ART-CMD1, ART-CMD4
- Fixture/setup: Invalid Markdown fixtures for personal paces, calculated targets, adaptive intervals, full benchmark plans, return-to-rowing guidance, competition programming, and runtime product features.
- Steps: Run checker tests and scan the real advanced page for the same forbidden patterns.
- Expected result: Invalid fixtures fail and the real page stays static.
- Failure proves: The advanced tutorial can drift into personalization, race coaching, or product behavior.
- Evidence artifact: M1 and M2 validation notes.
- Automation location: checker fixture tests.
- Required by milestone: M1, M2.

### ART-T13. Completion evidence ledger

- Covers: R50
- Level: smoke
- Command IDs: ART-CMD1, ART-CMD8, ART-CMD9, ART-CMD10
- Fixture/setup: Change-local validation notes and review handoff evidence.
- Steps: Confirm implementation handoff records exact commands, pass/fail outcomes, known unrelated gaps, manual proof paths, and no CI claim unless observed.
- Expected result: Completion claims are backed by exact local evidence.
- Failure proves: The handoff overclaims readiness or hides validation gaps.
- Evidence artifact: M4 validation ledger and later code-review record.
- Automation location: checklist or focused metadata test if added.
- Required by milestone: M4.

## Fixtures and data

- Valid fixture for a minimal advanced rowing page with required sections and no images under `tests/fixtures/advanced-rowing-machine-tutorial`.
- Invalid fixtures for missing sections, wrong path, personalized targets, adaptive plan wording, race-programming wording, and runtime product features under the same focused fixture directory or unittest-managed temporary directories.
- Valid and invalid prompt packet fixtures under `tests/fixtures/advanced-rowing-machine-tutorial`.
- Valid and invalid provenance rows for advanced rowing images under `tests/fixtures/advanced-rowing-machine-tutorial` or unittest-managed temporary files.
- Optional generated media fixtures should be tiny placeholder files only when a test needs path existence; real generated images are implementation artifacts, not test fixtures.

## Mocking/stubbing policy

Use filesystem fixtures and temporary repository roots for checker tests.
Do not mock source parsing, provenance matching, or prompt-record path resolution when an integration fixture can exercise the real checker logic.
Do not generate images during automated tests.

## Migration or compatibility tests

Compatibility coverage is additive.
Tests must confirm `exercises/rowing-machine.md` remains valid, unrelated exercise pages do not inherit the eight-image exception, existing exercise media purposes remain compatible, and `advanced_basic_cardio_equipment` remains inactive.

## Observability verification

No logs, metrics, traces, or runtime audit events apply.
Repository observability is validation evidence: command outputs, review records, prompt packets, provenance rows, source-audit notes, visual-safety notes, grayscale review, and comprehension proof.

## Security/privacy verification

Privacy checks must scan implementation content, prompt records, provenance rows, and change-local proof artifacts.
Manual proof must not include private reader data, private health data, private local paths, screenshots of private PM5 data, secrets, credentials, or identifiable people.

## Performance checks

No runtime performance checks apply.
Local validation should remain practical for normal repository checks; full unittest and focused Markdown/privacy checks are sufficient.

## Manual QA checklist

- ART-MP1 Source audit: damper, drag factor, PM5 metrics, stroke rate, force curve, workout examples, benchmark boundaries, and safety wording are supported at the level claimed.
- ART-MP2 Visual-safety review: each generated image has one teaching purpose, no copied UI, no brand marks, no identifying person, no unsupported promise, no inappropriate labels, and alt text matching the image.
- ART-MP3 Grayscale and force-overlay review: force-intensity levels remain distinguishable without color and do not imply exact force, EMG, injury risk, or form correctness.
- ART-MP4 Advanced-reader comprehension proof: a non-identifying reader can answer the spec's questions about split, stroke rate, drag factor, damper, force curve, rate changes, non-personalized scope, and helpful images.

## What not to test and why

- Do not test personalized pace calculators, PM5 data imports, wearable integrations, hosted apps, or trackers because they are out of scope.
- Do not test actual user performance outcomes because the page makes no performance guarantee.
- Do not test exact biomechanical force output or EMG data because force-intensity overlays are relative teaching aids.
- Do not run network link checking as part of this proof map; page-local source syntax and manual source audit are sufficient for this slice.
- Do not require all eight images if implementation defers some approved candidates; only referenced images require packet, provenance, and visual proof.

## Uncovered gaps

None blocking test-spec review.
Static checks cannot fully verify visual semantics, source adequacy, or reader comprehension, so ART-MP1 through ART-MP4 are required manual proof.

## Next artifacts

- Test-spec review.
- Implementation only after clean test-spec-review.

## Follow-on artifacts

- Test-spec review R2: `../docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/test-spec-review-r2.md`

## Readiness

This test spec has completed test-spec-review and is the active proof map for implementation.

## Sources

[local-advanced-rowing-machine-tutorial-test-spec]: advanced-rowing-machine-tutorial.md
[local-advanced-rowing-machine-tutorial-test-plan]: ../docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md
[local-advanced-rowing-machine-tutorial-test-plan-review]: ../docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/plan-review-r1.md
[local-advanced-rowing-machine-tutorial-test-architecture]: ../docs/architecture/system/architecture.md
