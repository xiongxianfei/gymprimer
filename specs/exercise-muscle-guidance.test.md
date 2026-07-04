# Test Spec: Exercise Muscle Guidance

## Status

active

## Related spec and plan

- Spec: `specs/exercise-muscle-guidance.md`
- Spec review: `docs/changes/exercise-muscle-guidance-standard/reviews/spec-review-r1.md`
- Plan: `docs/plans/2026-07-04-exercise-muscle-guidance.md`
- Plan review: `docs/changes/exercise-muscle-guidance-standard/reviews/plan-review-r1.md`
- Architecture: `docs/architecture/system/architecture.md`
- Architecture review: `docs/changes/exercise-muscle-guidance-standard/reviews/architecture-review-r1.md`
- Proposal: `docs/proposals/2026-07-04-exercise-muscle-guidance-standard.md`
- Review log: `docs/changes/exercise-muscle-guidance-standard/review-log.md`

## Input artifact identities

| Input | Path | Status / Review state | Identity |
| --- | --- | --- | --- |
| Feature spec | `specs/exercise-muscle-guidance.md` | approved; spec-review R1 approved | `R1-R44`, `AC1-AC5`, and examples `E1-E6` are the governing contract for this test spec. |
| Spec review | `docs/changes/exercise-muscle-guidance-standard/reviews/spec-review-r1.md` | approved; no material findings | Review routed the change to architecture before planning and later test-spec authoring. |
| Architecture | `docs/architecture/system/architecture.md` | approved by architecture-review R1 | Canonical architecture amendment keeps Markdown as source of truth and images support-only. |
| Architecture review | `docs/changes/exercise-muscle-guidance-standard/reviews/architecture-review-r1.md` | approved; no material findings | Review permits planning against the architecture amendment. |
| Execution plan | `docs/plans/2026-07-04-exercise-muscle-guidance.md` | reviewed; active | Milestones M1-M3 define contract/template/checker work, proof-slice pages, and manual proof. |
| Plan review | `docs/changes/exercise-muscle-guidance-standard/reviews/plan-review-r1.md` | approved; no material findings | Review routes to test-spec and blocks implementation until this test spec is reviewed. |
| Change metadata | `docs/changes/exercise-muscle-guidance-standard/change.yaml` | active workflow metadata | Current stage is test-spec authoring at the time this proof map is created. |

## Testing strategy

Unit coverage adds focused exercise-muscle-guidance tests for heading adoption, legacy heading compatibility, role-table and role-bullet parsing, phase-table parsing, feel-section pairing, deterministic forbidden wording, exact activation and EMG wording boundaries, and stable failure categories.

Integration coverage runs the Markdown-first checker against real repository surfaces after each owning milestone. Real-page tests prove the proof-slice pages represent cardio equipment, machine or resistance, hold or trunk, low-load control, mobility or stretch, and band or shoulder-control categories without forcing untouched legacy exercise pages to migrate early.

End-to-end coverage is repository-native: a reader can open each proof-slice exercise Markdown file directly and find broad muscle regions, what they help do, what the reader may feel, what not to overuse, when to stop, and page-local sources without generated HTML, hidden metadata, or an app.

Smoke coverage keeps text-only exercise pages valid and verifies that optional muscle-attention images remain governed by the existing exercise-image standard rather than a second image system.

Manual coverage records semantic source-audit evidence, beginner-comprehension evidence, and optional image-to-Markdown alignment evidence where static validation cannot prove claim support or reader understanding.

Contract coverage treats visible headings and Markdown wording as the public contract. Checker output must include file paths and stable failure categories for missing muscle sections, migrated legacy headings, missing feel sections, deterministic forbidden wording, multiple muscle-attention images, and generic or unsupported muscle-attention alt text.

Migration coverage is additive. Existing exercise pages with `## Used muscles` remain valid until selected for the proof slice or another approved migration scope. The broad rollout gate records future batch decisions instead of rewriting all exercise pages in M1 or M2.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | XMG-T1, XMG-T2, XMG-T6 | unit, integration | New or adopted exercise pages require `## Muscles involved`. |
| R2 | XMG-T2, XMG-T6 | unit, integration | Migrated or proof-slice pages fail when they retain `## Used muscles`. |
| R3 | XMG-T3, XMG-T10 | unit, migration | Untouched legacy pages with `## Used muscles` remain compatible. |
| R4 | XMG-T2, XMG-T4, XMG-T6 | unit, integration | Muscle sections must name a broad region and what it helps do. |
| R5 | XMG-T4, XMG-T6, XMG-M1 | unit, integration, manual | More than one meaningful contribution requires role-based guidance. |
| R6 | XMG-T4 | unit | Role guidance may be table or bullets. |
| R7 | XMG-T4, XMG-T6 | unit, integration | Role tables use equivalent Role, Muscle region, and What it helps do columns. |
| R8 | XMG-T5, XMG-T6 | unit, integration | Phase tables use equivalent Phase, Muscle region, and What it helps do columns. |
| R9 | XMG-T4, XMG-T6 | unit, integration | First-version role labels are recognized in fixtures and proof-slice pages. |
| R10 | XMG-T4, XMG-M1 | unit, manual | Equivalent labels require source-audit confirmation and must not create a second taxonomy. |
| R11 | XMG-T6, XMG-M1 | integration, manual | Machine or resistance proof page identifies driver, assistance, posture or shoulder-blade control, and overuse caution. |
| R12 | XMG-T7, XMG-M1 | unit, manual | Low-load control wording is soft unless direct source support is present. |
| R13 | XMG-T6, XMG-M1 | integration, manual | Hold or trunk proof page explains bracing or position control beyond "abs" or "core". |
| R14 | XMG-T6, XMG-M1 | integration, manual | Mobility or stretch proof page distinguishes moved or stretched region from strengthening. |
| R15 | XMG-T5, XMG-T6, XMG-M1 | unit, integration, manual | Cardio-equipment proof page can use phase-linked roles when structure and sources support them. |
| R16 | XMG-T1, XMG-T2, XMG-T6 | unit, integration | Adopted pages require `## What you should feel`. |
| R17 | XMG-T2, XMG-T6, XMG-M2 | unit, integration, manual | Feel section aligns with muscle roles in fixtures, proof-slice pages, and beginner proof. |
| R18 | XMG-T7, XMG-T6 | unit, integration | Feel cues use soft language such as "you may feel" and "pay attention to". |
| R19 | XMG-T7 | unit | "Must feel or wrong" wording fails. |
| R20 | XMG-T7, XMG-M1 | unit, manual | Compensation cues are general movement guidance and not diagnosis. |
| R21 | XMG-T7 | unit | Exact activation percentages fail. |
| R22 | XMG-T7, XMG-M1 | unit, manual | EMG-as-instruction wording fails unless direct support and careful framing are reviewed. |
| R23 | XMG-T7, XMG-M1 | unit, manual | Exact activation claims require direct source support or broad-role softening. |
| R24 | XMG-T8, XMG-M1 | integration, manual | Broad role claims need page-local source support; semantic adequacy is manually audited. |
| R25 | XMG-T8, XMG-M1 | integration, manual | Setup or movement cues inside muscle or feel sections require direct exercise-instruction support. |
| R26 | XMG-T7, XMG-T8, XMG-M1 | unit, integration, manual | Feel and compensation cues need direct support or clearly soft language. |
| R27 | XMG-T8, XMG-M1 | integration, manual | Concrete safety stop conditions require institutional, clinical, or instruction source support. |
| R28 | XMG-T8, XMG-M1 | integration, manual | Global-only source indexing cannot be the only support for specific claims. |
| R29 | XMG-T8, XMG-M1 | integration, manual | Technical muscle names require usefulness and source support. |
| R30 | XMG-T6, XMG-M2 | integration, manual | Common-language regions appear before technical names where both are used. |
| R31 | XMG-T7, XMG-M1 | unit, manual | Posture-correction, treatment, rehab, individualized cueing, and coaching claims fail. |
| R32 | XMG-T9 | integration | Muscle-attention images are optional and delegated to the exercise-image standard. |
| R33 | XMG-T9 | integration | More than one muscle-attention image fails. |
| R34 | XMG-T9, XMG-M3 | integration, manual | Nearby Markdown carries the exact muscle names, broad explanation, cues, caveats, and citations. |
| R35 | XMG-T9, XMG-M3 | integration, manual | Alt text describes broad highlighted region without unsupported exact anatomy. |
| R36 | XMG-T9, XMG-M3 | integration, manual | In-image labels, pain marks, wrong/correct framing, precise anatomy, diagnosis, and treatment claims fail. |
| R37 | XMG-T1 | unit | Exercise template prompts for role-based `## Muscles involved` and `## What you should feel`. |
| R38 | XMG-T6 | integration | Proof slice covers the six required representative categories. |
| R39 | XMG-T6 | integration | Proof slice uses the preferred page list or records equivalent choices. |
| R40 | XMG-T11, XMG-M4 | migration, manual | Broad rollout is gated by a recorded batch plan, not one unreviewed rewrite. |
| R41 | XMG-T2, XMG-T3, XMG-T7, XMG-T9 | unit, integration | Validation checks adopted pages for headings, feel section, deterministic forbidden wording, image purpose, image count, and legacy heading misuse only in migration scope. |
| R42 | XMG-T2, XMG-T7, XMG-T9, XMG-T12 | unit, contract | Validation output includes stable categories and file paths. |
| R43 | XMG-M1, XMG-M3 | manual | Manual audit samples main-driver, support or stabilizer, feel, compensation, safety, and image alignment where relevant. |
| R44 | XMG-M2 | manual | Beginner comprehension proof records region, role, feel, overuse, stop condition, and source verification. |
| AC1 | Upstream spec-review record | contract | Already satisfied by `spec-review-r1`; this test spec does not re-review the spec. |
| AC2 | Upstream architecture-review record | contract | Already satisfied by `architecture-review-r1`; architecture remains an input identity. |
| AC3 | Upstream plan-review record | contract | Already satisfied by `plan-review-r1`; M2 and M3 preserve small-slice rollout. |
| AC4 | XMG-T1-XMG-T12, XMG-M1-XMG-M4 | contract | This proof map gives deterministic, manual, comprehension, and image-alignment proof IDs. |
| AC5 | XMG-MAP1 | contract | Implementation remains blocked until test-spec-review approves this active proof map. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | XMG-T1, XMG-T2, XMG-T4, XMG-T6 | New/adopted exercise pages use role-based `## Muscles involved`. |
| E2 | XMG-T6, XMG-T7, XMG-M2 | Feel cues translate broad roles into soft beginner body awareness. |
| E3 | XMG-T5, XMG-T6, XMG-M1 | Rowing-machine-style phase guidance is covered by phase fixtures and cardio proof page. |
| E4 | XMG-T3, XMG-T10 | Legacy `## Used muscles` pages remain compatible until touched. |
| E5 | XMG-T7, XMG-T8, XMG-M1 | Exact activation claim fixture and source audit require direct support or softening. |
| E6 | XMG-T9, XMG-M3 | Muscle-attention image checks and manual review keep images subordinate to Markdown. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | XMG-T2 | unit | New page with `## Used muscles` fails. |
| EC2 | XMG-T3, XMG-T10 | migration | Untouched legacy page with `## Used muscles` passes outside migration scope. |
| EC3 | XMG-T4 | unit | Migrated page with only `Muscles: back, arms, core.` fails role-guidance checks. |
| EC4 | XMG-T8, XMG-M1 | integration, manual | Directly sourced technical muscle name can pass with beginner-readable context. |
| EC5 | XMG-T7 | unit | "You must feel your glutes or you are doing it wrong" fails. |
| EC6 | XMG-T6, XMG-M1 | integration, manual | Mobility page that frames the target as hard strengthening fails unless source and exercise type support that claim. |
| EC7 | XMG-T9, XMG-M3 | integration, manual | Muscle-attention alt text naming unsupported exact anatomy fails. |
| EC8 | XMG-T8, XMG-M1 | integration, manual | `SOURCES.md` entry without page-local support for a specific muscle claim fails source review. |
| EC9 | XMG-T7 | unit | Diagnosis, treatment, posture-correction, weak-muscle, and personalized cueing language fails deterministic wording checks. |
| EC10 | XMG-T9 | integration | Text-only exercise page with no muscle-attention image remains valid. |
| EC11 | XMG-T9 | integration | Page with two `exercise_muscle_attention_illustration` references fails. |
| EC12 | XMG-T12 | contract | Checker findings lacking file path or stable category fail observability tests. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XMG-CMD1 | `python3 -m unittest tests.test_exercise_muscle_guidance` | planned-for-implementation | tooling maintainer | M1 | M1 | Unexpected nonzero exit blocks M1 closeout and any dependent content migration. | Zero collected tests fail once the file exists; before M1 creates it, absence is expected and not a pre-M1 blocker. | M1 validation notes and code-review record. | Local read-only unit tests; no network, publication, or destructive side effects. |
| XMG-CMD2 | `python3 -m unittest tests.test_markdown_first_templates tests.test_markdown_first_real_pages` | existing/configured | tooling maintainer | M1, M2 | M1 | Unexpected nonzero exit blocks the owning milestone. | Zero collected tests fail because the named modules already exist. | M1 and M2 validation notes and code-review records. | Local read-only unittest execution. |
| XMG-CMD3 | `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | existing/configured | tooling maintainer | M2 | M2 | Unexpected nonzero exit blocks M2 closeout. | Zero collected tests fail because Markdown-first tests already exist. | M2 validation notes and code-review record. | Local read-only unittest discovery. |
| XMG-CMD4 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises` | existing/configured | content/check maintainer | M1 | M1 | Unexpected nonzero exit blocks M1 closeout. | Not applicable; checker validates files, not test collection. | M1 validation notes and code-review record. | Local read-only Markdown checks over template and exercise surfaces. |
| XMG-CMD5 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md` | existing/configured | content/check maintainer | M2, M3 | M2 | Unexpected nonzero exit blocks M2 or M3 closeout. | Not applicable; checker validates files, not test collection. | M2/M3 validation notes and code-review records. | Local read-only Markdown and provenance checks. |
| XMG-CMD6 | `python3 tools/checks/check_privacy.py docs/templates specs tools tests docs/changes/exercise-muscle-guidance-standard` | existing/configured | privacy/check maintainer | M1 | M1 | Any privacy finding or setup error blocks M1 closeout. | Not applicable; privacy checker validates files, not test collection. | M1 validation notes and code-review record. | Local read-only privacy scan over contract and tooling surfaces. |
| XMG-CMD7 | `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises media docs/changes/exercise-muscle-guidance-standard` | existing/configured | privacy/check maintainer | M2, M3 | M2 | Any privacy finding or setup error blocks M2 or M3 closeout. | Not applicable; privacy checker validates files, not test collection. | M2/M3 validation notes and code-review records. | Local read-only privacy scan over content, media metadata, and proof records. |
| XMG-CMD8 | `git diff --check` | existing/configured | release/check maintainer | M3 and lifecycle closeout | M3 | Whitespace errors block M3 closeout and final verification. | Not applicable. | M3 validation notes and final verify report. | Local git whitespace check only. |
| XMG-CMD9 | `python3 -m unittest discover -s tests` | existing/configured | release/check maintainer | lifecycle closeout | verify | Unexpected nonzero exit blocks final verification before PR handoff. | Zero collected tests fail because the repository has existing tests. | Final validation ledger and verify report. | Local read-only unittest discovery. |
| XMG-CMD10 | `python3 tools/checks/check_privacy.py docs/templates specs tools tests SOURCES.md RED-FLAGS.md exercises media docs/changes/exercise-muscle-guidance-standard` | existing/configured | release/check maintainer | lifecycle closeout | verify | Any privacy finding or setup error blocks final verification before PR handoff. | Not applicable; privacy checker validates files, not test collection. | Final validation ledger and verify report. | Local read-only privacy scan over touched and governed surfaces. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| M1. Muscle Guidance Contract Validation and Template | XMG-T1, XMG-T2, XMG-T3, XMG-T4, XMG-T5, XMG-T7, XMG-T8, XMG-T9, XMG-T12 | none | XMG-CMD1, XMG-CMD2, XMG-CMD4, XMG-CMD6 | M1 validation notes and code-review record. | M1 code-review | M1 proves the authoring/checker contract without migrating all exercise pages. |
| M2. Representative Proof-Slice Exercise Pages | XMG-T6, XMG-T10 | XMG-M1, XMG-M2 when enough page text exists for review | XMG-CMD1, XMG-CMD2, XMG-CMD3, XMG-CMD5, XMG-CMD7 | M2 validation notes, source-audit draft evidence, beginner-comprehension draft evidence, and code-review record. | M2 code-review | M2 applies the contract to representative pages and preserves untouched legacy compatibility. |
| M3. Manual Proof and Broad Rollout Gate | XMG-T11 | XMG-M1, XMG-M2, XMG-M3, XMG-M4 | XMG-CMD1, XMG-CMD5, XMG-CMD7, XMG-CMD8 | `docs/changes/exercise-muscle-guidance-standard/manual-proof/source-audit.md`, `beginner-comprehension.md`, `muscle-image-alignment.md`, `broad-rollout-gate.md`, and `validation-ledger.md`. | M3 code-review | M3 finalizes semantic proof and records future migration batching. |
| Lifecycle closeout | XMG-MAP1 | none | XMG-CMD8, XMG-CMD9, XMG-CMD10 | Final validation ledger, explain-change if created, verify report, and PR handoff notes. | verify | Final verification checks artifact-code-test coherence after implementation reviews. |

## Test cases

### XMG-T1. Exercise template prompts for role-based muscle guidance

- Covers: R1, R16, R37, E1, AC4
- Level: unit
- Command IDs: XMG-CMD2
- Fixture/setup: Use `docs/templates/exercise-card.md`.
- Steps: Extend `tests/test_markdown_first_templates.py` to assert the exercise template contains `## Muscles involved`, role-based guidance prompts, and the paired `## What you should feel` section with soft cue language.
- Expected result: The template makes the new contract authorable without requiring a muscle-attention image.
- Failure proves: New exercise pages can be started from stale template guidance.
- Evidence artifact: M1 validation notes and code-review record.
- Automation location: `tests/test_markdown_first_templates.py`
- Required by milestone: M1

### XMG-T2. Adopted or migrated pages require the durable muscle heading and feel section

- Covers: R1, R2, R4, R16, R17, R41, R42, E1, EC1
- Level: unit
- Command IDs: XMG-CMD1, XMG-CMD4
- Fixture/setup: Add focused fixtures under a path such as `tests/fixtures/exercise-muscle-guidance/` for new, migrated, and malformed exercise pages.
- Steps: Run checker tests against fixtures for valid adopted page, missing `## Muscles involved`, migrated page retaining `## Used muscles`, missing `## What you should feel`, and bare muscle list.
- Expected result: Valid adopted fixture passes; malformed fixtures fail with file path and stable muscle-guidance categories.
- Failure proves: The visible exercise muscle contract can be omitted or misnamed on adopted pages.
- Evidence artifact: M1 validation notes and code-review record.
- Automation location: `tests/test_exercise_muscle_guidance.py`; `tools/checks/check_markdown_first.py`
- Required by milestone: M1

### XMG-T3. Untouched legacy `## Used muscles` pages remain compatible

- Covers: R3, R41, E4, EC2
- Level: unit
- Command IDs: XMG-CMD1
- Fixture/setup: Add legacy-compatible fixtures or use stable unselected real pages only after confirming they are outside the current migration scope.
- Steps: Run checker tests with an untouched legacy page and a migrated-page fixture that still uses `## Used muscles`.
- Expected result: Untouched legacy fixture passes; migrated-page fixture fails.
- Failure proves: Validation either breaks legacy pages too early or fails to enforce migration when a page is in scope.
- Evidence artifact: M1 validation notes and code-review record.
- Automation location: `tests/test_exercise_muscle_guidance.py`
- Required by milestone: M1

### XMG-T4. Role tables and role bullets express broad regions and movement roles

- Covers: R4-R7, R9, R10, E1, EC3
- Level: unit
- Command IDs: XMG-CMD1
- Fixture/setup: Add valid role-table, valid role-bullet, equivalent-label, bare-list, and missing-role fixtures.
- Steps: Run focused tests that parse headings, role labels, broad muscle-region text, and "what it helps do" content.
- Expected result: Valid table and bullet fixtures pass; bare-list and missing-role fixtures fail; equivalent labels are flagged for manual source-audit review rather than creating a hidden second taxonomy.
- Failure proves: Role-based guidance can collapse back into anatomy-only lists.
- Evidence artifact: M1 validation notes and code-review record.
- Automation location: `tests/test_exercise_muscle_guidance.py`
- Required by milestone: M1

### XMG-T5. Phase-linked muscle tables are accepted for phase-based movements

- Covers: R8, R15, E3
- Level: unit
- Command IDs: XMG-CMD1
- Fixture/setup: Add valid and invalid phase-table fixtures with columns equivalent to Phase, Muscle region, and What it helps do.
- Steps: Run checker tests for a rowing-style phase table, a missing-phase-column table, and a phase table with no role/action text.
- Expected result: Valid phase table passes; invalid phase tables fail with stable categories.
- Failure proves: Cardio or cyclic movements cannot be represented cleanly without weakening the role contract.
- Evidence artifact: M1 validation notes and code-review record.
- Automation location: `tests/test_exercise_muscle_guidance.py`
- Required by milestone: M1

### XMG-T6. Proof-slice pages satisfy category and content contracts

- Covers: R1-R20, R29-R30, R38-R39, E1-E3, EC6
- Level: integration
- Command IDs: XMG-CMD1, XMG-CMD2, XMG-CMD3, XMG-CMD5
- Fixture/setup: Use the selected proof-slice pages from the approved representative set after M2 implementation.
- Steps: Run real-page tests that require one page in each category, `## Muscles involved`, `## What you should feel`, role or phase guidance, category-appropriate wording, and common-language regions before technical names where both appear.
- Expected result: The proof slice covers cardio equipment, machine or resistance, hold or trunk, low-load control, mobility or stretch, and band or shoulder-control pages with aligned muscle and feel guidance.
- Failure proves: The first implementation slice does not represent the approved exercise categories or the migrated pages still lack the new contract.
- Evidence artifact: M2 validation notes and code-review record.
- Automation location: `tests/test_exercise_muscle_guidance.py`; `tests/test_markdown_first_real_pages.py`
- Required by milestone: M2

### XMG-T7. Deterministic forbidden wording fails

- Covers: R12, R18-R23, R26, R31, R41-R42, E2, E5, EC5, EC9
- Level: unit
- Command IDs: XMG-CMD1, XMG-CMD4
- Fixture/setup: Add fixtures containing exact activation percentages, EMG-as-instruction wording, "must feel or wrong" claims, diagnosis, treatment, rehab, posture-correction promises, weak-muscle claims, individualized cueing, and neutral soft-language controls.
- Steps: Run checker tests against the wording fixtures.
- Expected result: Forbidden fixtures fail with stable categories; neutral soft-language fixtures pass.
- Failure proves: Muscle and feel guidance can drift into overconfident, clinical, or personalized advice.
- Evidence artifact: M1 validation notes and code-review record.
- Automation location: `tests/test_exercise_muscle_guidance.py`; `tools/checks/check_markdown_first.py`
- Required by milestone: M1

### XMG-T8. Source-support surfaces are structurally checkable

- Covers: R24-R29, E5, EC4, EC8
- Level: integration
- Command IDs: XMG-CMD1, XMG-CMD4, XMG-CMD5
- Fixture/setup: Add fixtures with page-local source definitions, global-only source references, missing sources, technical muscle names with citation, and concrete safety stop conditions.
- Steps: Run checker tests for source-section presence and source-surface failures, then route semantic claim support to XMG-M1.
- Expected result: Page-local source structure passes; missing or global-only support for specific claims fails where deterministic; semantic adequacy is manually audited.
- Failure proves: Specific muscle, feel, compensation, setup, movement, or safety claims can be promoted without even structural source support.
- Evidence artifact: M1/M2 validation notes and source-audit evidence.
- Automation location: `tests/test_exercise_muscle_guidance.py`; `tools/checks/check_markdown_first.py`; XMG-M1
- Required by milestone: M1

### XMG-T9. Muscle-attention image rules remain delegated and aligned

- Covers: R32-R36, R41-R42, E6, EC7, EC10, EC11
- Level: integration
- Command IDs: XMG-CMD1, XMG-CMD5
- Fixture/setup: Reuse or extend exercise-image fixtures for text-only page, one valid muscle-attention image, two muscle-attention images, missing or generic alt text, and unsupported exact anatomy in alt text.
- Steps: Run checker tests and integration checks that confirm optional use, one-image limit, broad-region alt text, and existing image-standard provenance behavior.
- Expected result: Text-only pages pass; valid one-image pages pass; multiple or unsupported muscle-attention image cases fail and semantic image alignment routes to XMG-M3.
- Failure proves: The muscle-guidance contract has forked image governance or allows image claims unsupported by Markdown.
- Evidence artifact: M1/M3 validation notes and optional image-alignment evidence.
- Automation location: `tests/test_exercise_muscle_guidance.py`; `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`; XMG-M3
- Required by milestone: M1

### XMG-T10. Legacy compatibility survives proof-slice migration

- Covers: R3, R40-R41, E4, EC2
- Level: integration
- Command IDs: XMG-CMD1, XMG-CMD5
- Fixture/setup: Use proof-slice selection records plus unselected current exercise pages.
- Steps: Assert selected proof-slice pages use `## Muscles involved` and unselected legacy pages with `## Used muscles` are not failed solely for the legacy heading.
- Expected result: Migration is scoped to selected/adopted pages and does not become a repository-wide rewrite.
- Failure proves: The checker or content slice violates the approved incremental migration strategy.
- Evidence artifact: M2 validation notes and code-review record.
- Automation location: `tests/test_exercise_muscle_guidance.py`; `tests/test_markdown_first_real_pages.py`
- Required by milestone: M2

### XMG-T11. Broad rollout gate records remaining exercise-page decisions

- Covers: R40
- Level: integration
- Command IDs: XMG-CMD1, XMG-CMD8
- Fixture/setup: Use `docs/changes/exercise-muscle-guidance-standard/manual-proof/broad-rollout-gate.md` after M3.
- Steps: Add a test or proof-record check that the gate lists remaining exercise pages and assigns each to keep, rename only, rewrite roles, revise feel cues, future image candidate, or a documented equivalent batch category.
- Expected result: Future migration has a recorded batch surface and no hidden all-page rewrite is implied.
- Failure proves: Broad rollout can proceed without a reviewed migration inventory.
- Evidence artifact: Broad-rollout gate and M3 validation notes.
- Automation location: `tests/test_exercise_muscle_guidance.py`; XMG-M4
- Required by milestone: M3

### XMG-T12. Validation findings are observable

- Covers: R42, EC12
- Level: unit
- Command IDs: XMG-CMD1
- Fixture/setup: Use invalid fixtures from XMG-T2, XMG-T7, and XMG-T9.
- Steps: Assert checker failures include the affected file path and stable failure categories for missing muscle section, migrated legacy heading, missing feel section, deterministic forbidden wording, multiple muscle-attention images, and generic or unsupported alt text.
- Expected result: Failures are actionable in local output and review evidence.
- Failure proves: Contributors cannot tell which file or rule failed.
- Evidence artifact: M1 validation notes and code-review record.
- Automation location: `tests/test_exercise_muscle_guidance.py`; `tools/checks/check_markdown_first.py`
- Required by milestone: M1

### XMG-MAP1. Implementation remains blocked until test-spec review is approved

- Covers: AC5
- Level: manual
- Command IDs: none
- Fixture/setup: Use `docs/changes/exercise-muscle-guidance-standard/change.yaml`, this test spec, and the recorded test-spec-review.
- Steps: Before implementation begins, confirm change metadata points to this active test spec and a recorded approved test-spec-review with implementation handoff allowed.
- Expected result: Implementation starts only after test-spec-review approval.
- Failure proves: The workflow skipped a required proof-map gate.
- Evidence artifact: `docs/changes/exercise-muscle-guidance-standard/reviews/test-spec-review-r1.md`
- Automation location: workflow review evidence
- Required by milestone: pre-implementation gate

## Fixtures and data

- Focused fixtures should live under a deterministic test fixture path such as `tests/fixtures/exercise-muscle-guidance/`.
- Fixture groups should include adopted valid page, new page with legacy heading, migrated page with legacy heading, untouched legacy page, missing feel section, role table, role bullets, phase table, bare list, forbidden wording, source-support surfaces, text-only image page, and muscle-attention image edge cases.
- Real-page tests use only selected proof-slice pages from the approved representative set and must not silently convert all exercise pages into migration scope.
- Manual proof records live under `docs/changes/exercise-muscle-guidance-standard/manual-proof/`.
- No fixture or manual proof record may include private health information, private reviewer details, secrets, or unpublished source material.

## Mocking/stubbing policy

Tests should use temporary fixture files and repository-local Markdown only. Do not mock source-support semantics as if static parsing proves claim accuracy. Do not use network calls to validate public sources in unit tests. Optional image checks should use existing provenance and Markdown parsing helpers where possible instead of duplicating exercise-image-standard logic.

## Migration or compatibility tests

XMG-T3 and XMG-T10 prove the legacy `## Used muscles` compatibility boundary. XMG-T11 proves broad migration remains gated by batch decisions. These tests must distinguish adoption scope from untouched pages; a checker rule that fails every current legacy heading before migration is a regression.

## Observability verification

XMG-T12 verifies stable categories and file paths for deterministic validation findings. Manual evidence files must identify sampled pages, claim types, image paths when relevant, source references, pass/fail result, and residual risk. Validation ledgers must name exact commands run and outcomes before closeout claims.

## Security/privacy verification

XMG-CMD6, XMG-CMD7, and XMG-CMD10 scan touched contract, tooling, content, media, and manual proof surfaces. Manual beginner-comprehension evidence must record non-identifying outcomes only and must not store health histories, symptoms, names, contact details, or private reviewer data.

## Performance checks

No benchmark is required. The expected performance property is that Markdown-first validation remains suitable for local repository checks. If the focused checker tests or full Markdown checks become slow enough to disrupt local review, implementation should record timing and split expensive checks into release-owned validation without weakening milestone gates.

## Manual QA checklist

### XMG-M1. Manual source audit

- Automation rationale: Static checks can find citations and source sections, but cannot prove that sampled muscle, feel, compensation, setup, movement, and safety claims are semantically supported.
- Required environment: Local checkout with proof-slice pages and public source links available.
- Evidence artifact: `docs/changes/exercise-muscle-guidance-standard/manual-proof/source-audit.md`
- Steps: Sample at least one main-driver claim, one support or stabilizer claim, one feel cue, one compensation cue, and one safety cue across proof-slice pages; record page path, claim text or concise paraphrase, claim type, supporting page-local source, disposition, and residual risk.
- Pass condition: Every sampled claim is supported, softened, or removed before the owning milestone closes.
- Failure condition: Unsupported sampled claims remain, only global sources support specific claims, or the evidence omits required claim types.
- Owning stage: M2 draft evidence and M3 final evidence.
- Re-run trigger: Any proof-slice muscle, feel, compensation, setup, movement, safety, or source wording changes after the audit.

### XMG-M2. Beginner comprehension proof

- Automation rationale: Static parsing cannot prove that beginner readers understand what to notice, what the region does, or how to use sources.
- Required environment: Local checkout with proof-slice pages and a non-identifying reader-test process.
- Evidence artifact: `docs/changes/exercise-muscle-guidance-standard/manual-proof/beginner-comprehension.md`
- Steps: For the first proof slice, record non-identifying outcomes for whether a beginner can identify the muscle region to notice, what it helps do, what they may feel, what not to overuse, when to stop, and which source they would click to verify the claim.
- Pass condition: Evidence records page-level outcomes and residual confusion without private health information.
- Failure condition: Evidence is absent, records only general approval, skips required prompts, or stores private health information.
- Owning stage: M2 draft evidence and M3 final evidence.
- Re-run trigger: Any proof-slice page changes that alter muscle roles, feel cues, overuse cues, stop conditions, or source links.

### XMG-M3. Muscle-attention image alignment review

- Automation rationale: Static checks can validate purpose count and alt text shape, but cannot prove a visual highlight is broad, non-clinical, and subordinate to nearby Markdown.
- Required environment: Local checkout with final proof-slice image assets renderable from `media/` when any muscle-attention image is used.
- Evidence artifact: `docs/changes/exercise-muscle-guidance-standard/manual-proof/muscle-image-alignment.md`
- Steps: For every proof-slice muscle-attention image, compare image path, purpose, alt text, nearby `## Muscles involved` and `## What you should feel` text, page-local citations, and provenance; confirm broad region highlight, no in-image labels, no red pain marks, no wrong/correct framing, no precise anatomy as source of truth, and no diagnosis or treatment framing.
- Pass condition: Every reviewed image aligns with nearby Markdown and the exercise-image standard, or the image is removed.
- Failure condition: Any reviewed image is overprecise, labeled, unsupported, clinically framed, missing provenance, or missing meaningful alt text.
- Owning stage: M3.
- Re-run trigger: Any proof-slice muscle-attention image, alt text, nearby muscle guidance, source citation, or provenance row changes.

### XMG-M4. Broad rollout gate review

- Automation rationale: Static checks cannot decide future batch scope or source-audit sequencing for all remaining exercise pages.
- Required environment: Local checkout with final proof-slice pages and current `exercises/` inventory.
- Evidence artifact: `docs/changes/exercise-muscle-guidance-standard/manual-proof/broad-rollout-gate.md`
- Steps: List remaining exercise pages and classify each as keep as-is for now, rename only, rewrite role guidance, revise `## What you should feel`, source-audit needed, or future image candidate; record any pages intentionally deferred.
- Pass condition: Future migration decisions are explicit enough for a later plan or implementation slice.
- Failure condition: The gate is absent, omits remaining pages, implies a broad unreviewed rewrite, or lacks decision categories.
- Owning stage: M3.
- Re-run trigger: New exercise pages are added, proof-slice pages change category, or broad migration starts.

## What not to test and why

- Do not test exact muscle activation percentages as valid output; they are out of scope and should fail deterministic or manual review.
- Do not automate semantic truth of muscle claims beyond structural source-surface checks; that belongs to XMG-M1 manual source audit.
- Do not require every exercise page to have a muscle-attention image; text-only pages are valid.
- Do not require immediate migration of every `## Used muscles` page; migration scope is controlled by M2 and the M3 rollout gate.
- Do not test generated HTML, hosted app flows, user accounts, databases, personalization logic, or AI coaching because the approved contract is Markdown-first repository content.
- Do not use remote source fetching as a unit-test dependency; public-source review is manual and evidence-backed.

## Uncovered gaps

None that block implementation. Semantic source support, beginner comprehension, and image meaning are intentionally manual proof obligations with stable evidence paths and re-run triggers.

## Next artifacts

1. Test-spec review.
2. M1 implementation after test-spec-review approval.
3. M1 code review and validation notes.
4. M2 proof-slice implementation and review.
5. M3 manual proof and broad-rollout gate.

## Follow-on artifacts

- Test-spec review: `docs/changes/exercise-muscle-guidance-standard/reviews/test-spec-review-r1.md`

## Readiness

This test spec is active and has a clean recorded test-spec review. It is ready for M1 implementation use.
