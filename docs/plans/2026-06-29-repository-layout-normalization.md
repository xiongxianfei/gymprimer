## Status

- Status: completed
- Plan lifecycle state: completed
- Terminal disposition: completed-by PR #5

## Purpose / big picture

Normalize GymPrimer's physical repository layout to match the approved five-block architecture: project references, content, media, governance, and tooling/operations. The migration removes old numbered content paths directly, moves red flags to root `RED-FLAGS.md`, co-locates promoted media by content subject, and removes or labels historical structured-platform artifacts only after active dependencies are handled.

## Source artifacts

- Proposal: `docs/proposals/2026-06-29-responsible-breadth.md`
- Spec: `specs/repository-layout-normalization.md`
- Architecture: `docs/architecture/system/architecture.md`
- ADR: `docs/adr/2026-06-29-direct-repository-layout-normalization.md`
- Spec review: `docs/changes/repository-layout-normalization/reviews/spec-review-r2.md`
- Architecture review: `docs/changes/repository-layout-normalization/reviews/architecture-review-r1.md`
- Test spec: `specs/repository-layout-normalization.test.md`

## Context and orientation

Current compatibility paths include `01-getting-started/`, `02-machines/`, `03-bodyweight/`, `about/red-flags.md`, `media/equipment/`, `media/movements/`, `media/supplemental/`, and historical structured-platform folders such as `content/`, `schemas/`, and `generated/`.

Target canonical content paths are `exercises/`, `patterns/`, `conditions/`, `principles/`, and `programs/`. Target project safety reference is root `RED-FLAGS.md`. Target promoted media paths are `media/<content-type>/<slug>/...`. Governance remains under `docs/`.

The migration is dependency-first. Before any old path is removed, active references must be inventoried and updated or removed across Markdown links, README navigation, `SUMMARY.md`, `book.toml`, source references, tests, checkers, evidence records, change metadata, and `media/PROVENANCE.md`.

## Non-goals

- Changing product scope, safety boundaries, citation standards, or Responsible Breadth page contracts.
- Rewriting content quality while moving files.
- Moving governance artifacts out of `docs/`.
- Adding mdBook publication, hosting, CMS, runtime services, search, analytics, or generated HTML authority.
- Leaving compatibility stubs at old paths.
- Removing tests or proof records merely to make deletion easier.

## Requirements covered

- R1-R2: M3, M4
- R3-R7: M3
- R8-R10, R20, R24: M4
- R11-R14: M4
- R15-R17: M1, M3, M4
- R18-R19: M2, M3, M4
- R21-R22: M3, M4
- R23, R25: M1-M4 and closeout
- EC1-EC9: M2-M4
- AC1-AC2: completed by spec-review R2 and architecture-review R1
- AC3: downstream test-spec stage before implementation
- AC4: this plan plus test-spec detail
- AC5-AC12: M2-M4 and implementation closeout

## Current Handoff Summary

- Current milestone: lifecycle closeout
- Current milestone state: completed
- Last reviewed milestone: M4 media and historical-artifact cleanup
- Review status: code-review M4 R3 closed M4 with no material findings
- Remaining in-scope implementation milestones: none
- Next stage: none
- Final closeout readiness: completed
- Reason final closeout is or is not ready: local final verification passed and PR #5 merged the change.

## Milestones

### M1. Dependency inventory and migration manifest

- Milestone state: closed
- Goal: create a deterministic inventory of old paths, active dependencies, and intended dispositions before moving files.
- Requirements: R13-R17, R23, R25, AC4, AC12
- Files/components likely touched:
  - `docs/changes/repository-layout-normalization/evidence/`
  - `docs/changes/repository-layout-normalization/change.yaml`
  - possible migration manifest under `docs/changes/repository-layout-normalization/`
- Dependencies:
  - plan-review approval
  - test-spec-review approval
- Tests to add/update:
  - Dependency inventory evidence
  - Test fixture list for old-path references, if useful for M2
- Implementation steps:
  - Enumerate old numbered content paths and their canonical targets.
  - Enumerate `about/red-flags.md` references and root target.
  - Enumerate media paths referenced by promoted content and provenance rows.
  - Enumerate historical structured-platform folders and active references.
  - Record disposition for each path: move, remove, retain as historical, or archive.
- Validation commands:
  - `rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags|media/equipment|media/movements|media/supplemental|content/|schemas/|generated/" .`
  - `python3 tools/checks/check_privacy.py docs/changes/repository-layout-normalization`
  - `git diff --check`
- Expected observable result: a reviewer can see every dependency that must be handled before an old path is removed.
- Implementation result: `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md` records old paths, active dependencies, canonical targets, milestone ownership, and M2 fixture candidates. No files were moved or removed.
- Commit message: `M1: record layout dependency inventory`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - prose references or test fixtures may be missed by simple search.
- Rollback/recovery:
  - restore the prior manifest/proof and rerun the inventory search.

### M2. Validation tooling and regression tests

- Milestone state: closed
- Goal: update checks and tests so canonical paths, root red flags, no compatibility stubs, media co-location, provenance updates, and dependency-first behavior are enforceable.
- Requirements: R15-R20, R23-R25, EC1-EC9, AC5-AC8, AC11-AC12
- Files/components likely touched:
  - `tools/checks/check_markdown_first.py`
  - `tests/`
  - `tests/fixtures/`
- Dependencies:
  - M1 inventory
  - approved test spec
- Tests to add/update:
  - Old numbered path references fail after migration.
  - `about/red-flags.md` references fail after migration.
  - Compatibility stubs fail.
  - Moved raster media requires exact `media/PROVENANCE.md` `asset_path` and `page_refs`.
  - Historical artifact retention requires explicit historical/archive classification when active dependencies remain.
- Implementation steps:
  - Add or update fixtures for each edge case.
  - Extend validation to reject stale old-path references in promoted content and navigation.
  - Extend validation to accept root `RED-FLAGS.md` as canonical.
  - Extend media checks for subject-co-located raster paths and provenance.
  - Keep governance under `docs/` unaffected.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`
  - `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/repository-layout-normalization`
  - `git diff --check`
- Expected observable result: tests fail for stale old paths and pass for the normalized target tree.
- Implementation result: `tests/test_repository_layout_normalization.py` adds regression coverage for canonical content paths, root `RED-FLAGS.md`, old numbered paths, old red-flags links, compatibility stubs, subject-co-located media, stale provenance rows, root-level governance folders, and historical artifact classification. `tools/checks/check_markdown_first.py` enforces those rules once the normalized root `RED-FLAGS.md` exists.
- Commit message: `M2: enforce normalized layout paths`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - path checks may over-match historical review records that intentionally mention old paths.
- Rollback/recovery:
  - scope validation to active content/navigation first, then add explicit historical allowances for change records.

### M3. Content and project-reference migration

- Milestone state: closed
- Goal: move Markdown content and project references to canonical paths, update active links, and remove old numbered and red-flags paths directly.
- Requirements: R1-R7, R10-R12, R15-R19, R21-R23, R25, AC5-AC6, AC8-AC9, AC11-AC12
- Files/components likely touched:
  - `01-getting-started/`
  - `02-machines/`
  - `03-bodyweight/`
  - `about/red-flags.md`
  - `RED-FLAGS.md`
  - `exercises/`
  - `principles/`
  - `README.md`
  - `SOURCES.md`
  - `docs/`
  - tests and checkers touched in M2
- Dependencies:
  - M1 inventory
  - M2 validation tooling
- Tests to add/update:
  - Real-page validation for canonical paths
  - Link validation for moved Markdown pages
  - Regression tests that old numbered paths are not required
- Implementation steps:
  - Move machine and bodyweight exercise pages into `exercises/`.
  - Move beginner principles into `principles/beginner-training-principles.md`.
  - Move `about/red-flags.md` to `RED-FLAGS.md`.
  - Update active Markdown links, README navigation, source references, tests, checkers, and proof records.
  - Remove old numbered content directories and `about/` if empty after migration.
  - Confirm no compatibility stubs remain.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`
  - `rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools`
  - `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises docs/changes/repository-layout-normalization`
  - `git diff --check`
- Expected observable result: canonical Markdown content validates from new paths and old content paths are gone without stubs.
- Implementation result: moved beginner principles to `principles/beginner-training-principles.md`, moved first-slice exercise pages to `exercises/`, moved red flags to `RED-FLAGS.md`, removed old content directories directly, updated active README/content/test/checker/provenance references, and preserved media bucket cleanup for M4.
- Commit message: `M3: migrate content paths`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
  - code-review R1 requested resolution for CR-RLN-M3-1 before closeout
  - CR-RLN-M3-1 resolved and M3 returned to code-review
  - code-review R2 closed M3 with no material findings
- Risks:
  - broad documentation references to old paths may be historical rather than active.
- Rollback/recovery:
  - restore old Markdown paths, revert link updates, and rerun validation.

### M4. Media and historical-artifact cleanup

- Milestone state: closed
- Goal: move promoted media to subject-co-located paths, update provenance, and remove or label historical structured-platform artifacts according to dependency inventory.
- Requirements: R8-R10, R13-R20, R22-R25, AC6-AC12
- Files/components likely touched:
  - `media/`
  - `media/PROVENANCE.md`
  - content pages referencing media
  - `content/`
  - `schemas/`
  - `generated/`
  - tests, checkers, fixtures, and proof records
- Dependencies:
  - M1 inventory
  - M2 validation tooling
  - M3 content/reference migration
- Tests to add/update:
  - Media path and provenance validation for moved raster assets
  - Missing old media-bucket reference regression
  - Historical artifact disposition evidence
- Implementation steps:
  - Move promoted media from image-type buckets to `media/<content-type>/<slug>/`.
  - Update Markdown image references and alt text as needed.
  - Update `media/PROVENANCE.md` exact `asset_path` and `page_refs`.
  - Remove old media-bucket paths after references and provenance are updated.
  - Remove historical structured-platform artifacts with no active dependencies.
  - Label or archive retained historical artifacts when active dependencies still require them.
  - Record final dependency and validation evidence.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`
  - `rg -n "media/equipment|media/movements|media/supplemental|content/|schemas/|generated/|tools/validation" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools media/PROVENANCE.md`
  - `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/repository-layout-normalization tests tools`
  - `git diff --check`
- Expected observable result: promoted media is subject-co-located with exact provenance rows, old media buckets are not referenced by promoted content, and historical artifacts are removed or explicitly historical.
- Implementation result: promoted raster media moved to `media/exercises/<slug>/` and `media/patterns/<slug>/`, Markdown and contributor image links updated, provenance rows updated to exact new paths, old media buckets and SVG examples removed, and superseded structured-platform folders, tools, tests, and fixtures removed from the active tree with M4 disposition evidence recorded.
- Commit message: `M4: migrate media and historical artifacts`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - code-review R1 requested resolution for CR-RLN-M4-1 before closeout
  - CR-RLN-M4-1 resolved and M4 returned to code-review
  - code-review R3 closed M4 with no material findings
  - milestone committed
- Risks:
  - privacy scan over broad historical fixtures may fail on intentional test data.
  - removing generated evidence may conflict with historical review records.
- Rollback/recovery:
  - restore old media paths or historical folders, revert provenance and link changes, and rerun validation.

## Validation plan

- `python3 -m unittest discover -s tests`: unit and regression tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`: real-page Markdown, source, media, and layout validation after migration.
- `python3 tools/checks/check_privacy.py ...`: scoped privacy checks over changed content, media provenance, tests, tools, and evidence records.
- `rg -n "...old paths..." ...`: deterministic old-path dependency audit.
- `git diff --check`: whitespace and patch hygiene.

## Risks and recovery

- Risk: direct removal breaks stale active links.
  - Recovery: use M1 dependency inventory plus M2 stale-path regression tests before removing paths.
- Risk: historical references are confused with active dependencies.
  - Recovery: record each retained historical reference as historical/archive disposition in M1 and M4 proof.
- Risk: provenance paths drift from moved media.
  - Recovery: keep media moves and `media/PROVENANCE.md` updates in the same milestone and validate exact paths.
- Risk: broad privacy checks fail on intentional historical fixtures.
  - Recovery: scope privacy validation to changed active surfaces and document any fixture exception.

## Dependencies

- Spec-review R2 is complete.
- Architecture-review R1 is complete.
- Architecture status is normalized to approved.
- ADR status is normalized to accepted.
- Plan-review is required before test-spec.
- Test-spec must map R1-R25 and EC1-EC9 before M1 starts.
- Test-spec and test-spec-review are required before implementation.

## Progress

- 2026-06-29: Created plan after spec-review R2 and architecture-review R1 approved the repository layout normalization contract and architecture.
- 2026-06-29: Revised plan after plan-review R1 to remove test-spec authoring from implementation milestones.
- 2026-06-29: Authored `specs/repository-layout-normalization.test.md` to map R1-R25 and EC1-EC9 before M1 starts.
- 2026-06-29: Test-spec-review R1 requested revision for TSR-RLN-1 and TSR-RLN-2.
- 2026-06-29: Test-spec-review R2 approved the revised proof map and allowed implementation handoff.
- 2026-06-29: M1 implemented dependency inventory evidence without moving or removing files.
- 2026-06-29: Code-review M1 R1 closed M1 with no material findings and routed the change to M2 implementation.
- 2026-06-29: M2 implemented repository layout normalization regression tests and checker enforcement without moving real content or media files.
- 2026-06-29: Code-review M2 R1 closed M2 with no material findings and routed the change to M3 implementation.
- 2026-06-30: M3 moved canonical Markdown content paths and root red flags, updated active references, and left media bucket cleanup to M4.
- 2026-06-30: Code-review M3 R1 requested resolution for CR-RLN-M3-1 because the M1 dependency inventory and validation metadata were rewritten from exact old paths to placeholders during M3 cleanup.
- 2026-06-30: Review-resolution restored exact M1 inventory proof and narrowed the M3 stale-path scan to active content, tests, and tools so historical proof records can retain exact old paths.
- 2026-06-30: Code-review M3 R2 closed M3 with no material findings and routed the change to M4 implementation.
- 2026-06-30: M4 moved promoted media into subject-co-located paths, removed old media buckets and SVG examples, removed the superseded structured-platform folders/tools/tests, and recorded M4 disposition evidence.
- 2026-06-30: Code-review M4 R1 requested resolution for CR-RLN-M4-1 because the historical-disposition evidence exists under a different filename than the approved RLN-T7 proof-map path.
- 2026-06-30: Code-review M4 R2 found CR-RLN-M4-1 still present because no resolution diff added the approved RLN-T7 evidence path or amended the proof map.
- 2026-06-30: Review-resolution renamed the M4 disposition evidence to the approved RLN-T7 path and routed M4 back to code-review.
- 2026-06-30: Code-review M4 R3 closed M4 with no material findings and routed the change to final closeout.
- 2026-06-30: Updated `docs/changes/repository-layout-normalization/explain-change.md` for the final reviewed implementation and routed the change to verify.
- 2026-06-30: Final local verification passed and routed the change to PR handoff.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-29 | Sequence dependency inventory before validation and file moves | The spec requires dependencies to be identified and updated before old paths are removed. | Moving files first and fixing broken references reactively |
| 2026-06-29 | Put validation tooling before content/media moves | Stale-path and provenance checks should catch migration mistakes as files move. | Manual-only validation during a broad file migration |
| 2026-06-29 | Split content/reference migration from media/historical cleanup | Markdown path moves and media/provenance moves have different failure modes and rollback paths. | One large migration milestone |
| 2026-06-29 | Keep test-spec ownership outside implementation milestones | The workflow requires test-spec and test-spec-review before implementation starts. | Letting M2 create or revise `specs/repository-layout-normalization.test.md` |

## Surprises and discoveries

- M2 validation must not require the real `RED-FLAGS.md` checker command yet because M3 owns the actual red-flags move. The checker therefore activates strict normalized-layout checks when `RED-FLAGS.md` exists in the checked repository, which lets fixture tests prove the target behavior before the real tree migrates.

## Validation notes

- `git diff --check` passed during plan authoring.
- `python3 tools/checks/check_privacy.py docs/plans/2026-06-29-repository-layout-normalization.md docs/plan.md docs/changes/repository-layout-normalization/change.yaml docs/architecture/system/architecture.md docs/adr/2026-06-29-direct-repository-layout-normalization.md specs/repository-layout-normalization.md` passed, checked 6 files.
- Plan revision for PR-RLN-1 removed test-spec ownership from M2 and made R1-R25 / EC1-EC9 test-spec mapping a pre-implementation dependency.
- `git diff --check` passed after test-spec authoring.
- `python3 tools/checks/check_privacy.py specs/repository-layout-normalization.test.md docs/plans/2026-06-29-repository-layout-normalization.md docs/plan.md docs/changes/repository-layout-normalization/change.yaml` passed, checked 4 files.
- Test spec authored at `specs/repository-layout-normalization.test.md` and maps R1-R25 plus EC1-EC9 before M1 starts.
- Test-spec-review R1 recorded changes-requested for missing proof/command milestone ownership and under-specified manual proof records.
- Manual-proof requirements were removed by replacing manual-proof artifacts with deterministic evidence records in the test spec and plan.
- Test-spec-review R2 approved the revised proof map.
- M1 inventory command passed: `rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags|media/equipment|media/movements|media/supplemental|content/|schemas/|generated/" .` returned matches and those dependencies are categorized in `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md`.
- M1 privacy check passed: `python3 tools/checks/check_privacy.py docs/changes/repository-layout-normalization` checked 12 files.
- M1 diff check passed: `git diff --check`.
- Code-review M1 R1 reviewer reran `git diff --check`; passed.
- Code-review M1 R1 reviewer reran `python3 tools/checks/check_privacy.py docs/changes/repository-layout-normalization docs/plans/2026-06-29-repository-layout-normalization.md docs/plan.md`; checked 14 files, privacy pass.
- M2 focused regression test passed: `python3 -m unittest tests.test_repository_layout_normalization` ran 10 tests.
- M2 full unit suite passed: `python3 -m unittest discover -s tests` ran 141 tests.
- M2 diff check passed: `git diff --check`.
- M2 privacy check passed: `python3 tools/checks/check_privacy.py tools/checks/check_markdown_first.py tests/test_repository_layout_normalization.py docs/changes/repository-layout-normalization docs/plans/2026-06-29-repository-layout-normalization.md docs/plan.md` checked 17 files.
- M2 did not run `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` as closeout proof because `specs/repository-layout-normalization.test.md` assigns RLN-CMD3 to M3 and the real `RED-FLAGS.md` move is not in M2 scope.
- Code-review M2 R1 reviewer reran `python3 -m unittest tests.test_repository_layout_normalization`; passed, 10 tests.
- Code-review M2 R1 reviewer reran `python3 -m unittest discover -s tests`; passed, 141 tests.
- Code-review M2 R1 reviewer reran `git diff --check`; passed.
- Code-review M2 R1 reviewer reran `python3 tools/checks/check_privacy.py tools/checks/check_markdown_first.py tests/test_repository_layout_normalization.py docs/changes/repository-layout-normalization docs/plans/2026-06-29-repository-layout-normalization.md docs/plan.md`; checked 17 files, privacy pass.
- M3 checker validation passed: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` checked 18 Markdown files.
- M3 stale content/red-flags scan was superseded during CR-RLN-M3-1 resolution because it incorrectly scanned change-history records that must preserve exact old paths.
- M3 active-surface stale content/red-flags scan passed with no matches: `rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools` returned exit 1 because no stale active paths were found.
- M3 full unit suite passed: `python3 -m unittest discover -s tests` ran 141 tests.
- M3 privacy check passed: `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises docs/changes/repository-layout-normalization` checked 32 files.
- M3 diff check passed: `git diff --check`.
- M3 old directory check passed: `find 01-getting-started 02-machines 03-bodyweight about -maxdepth 0 -type d -print 2>/dev/null || true` returned no paths.
- Code-review M3 R1 reviewer reran `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`; passed, checked 18 Markdown files.
- Code-review M3 R1 reviewer reran `python3 -m unittest discover -s tests`; passed, ran 141 tests.
- Code-review M3 R1 reviewer reran `git diff --check`; passed.
- Code-review M3 R1 reviewer reran `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises docs/changes/repository-layout-normalization`; checked 32 files, privacy pass.
- CR-RLN-M3-1 resolution active-surface stale-path scan passed with no matches: `rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools` returned exit 1 because no stale active paths were found.
- CR-RLN-M3-1 resolution checker validation passed: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` checked 18 Markdown files.
- CR-RLN-M3-1 resolution full unit suite passed: `python3 -m unittest discover -s tests` ran 141 tests.
- CR-RLN-M3-1 resolution diff check passed: `git diff --check`.
- CR-RLN-M3-1 resolution privacy check passed: `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises docs/changes/repository-layout-normalization specs/repository-layout-normalization.test.md docs/plans/2026-06-29-repository-layout-normalization.md docs/plan.md` checked 36 files.
- Code-review M3 R2 reviewer reran `rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools`; no matches, exit 1 expected for `rg` no-match.
- Code-review M3 R2 reviewer reran `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`; passed, checked 18 Markdown files.
- Code-review M3 R2 reviewer reran `python3 -m unittest discover -s tests`; passed, ran 141 tests.
- Code-review M3 R2 reviewer reran `git diff --check`; passed.
- Code-review M3 R2 reviewer reran `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises docs/changes/repository-layout-normalization specs/repository-layout-normalization.test.md docs/plans/2026-06-29-repository-layout-normalization.md docs/plan.md`; checked 36 files, privacy pass.
- Code-review M3 R2 reviewer reran `find 01-getting-started 02-machines 03-bodyweight about -maxdepth 0 -type d -print 2>/dev/null || true`; returned no paths.
- M4 full unit suite passed: `python3 -m unittest discover -s tests` ran 79 tests.
- M4 checker validation passed: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` checked 18 Markdown files.
- M4 active stale media/historical scan passed with no matches: `rg -n "media/equipment|media/movements|media/supplemental|content/|schemas/|generated/|tools/validation" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools media/PROVENANCE.md` returned exit 1 because no stale active paths were found.
- M4 privacy check passed: `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/repository-layout-normalization tests tools` checked 103 files.
- M4 diff check passed: `git diff --check`.
- M4 old directory check passed: `find media/equipment media/movements media/supplemental media/svg content schemas generated tools/validation -maxdepth 0 -print 2>/dev/null || true` returned no paths.
- M4 focused regression tests passed: `python3 -m unittest tests.test_repository_layout_normalization tests.test_markdown_first_guardrails tests.test_responsible_breadth_m1 tests.test_markdown_first_privacy` ran 50 tests.
- CR-RLN-M4-1 resolution full unit suite passed: `python3 -m unittest discover -s tests` ran 79 tests.
- CR-RLN-M4-1 resolution checker validation passed: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` checked 18 Markdown files.
- CR-RLN-M4-1 resolution active stale media/historical scan passed with no matches: `rg -n "media/equipment|media/movements|media/supplemental|content/|schemas/|generated/|tools/validation" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools media/PROVENANCE.md` returned exit 1 because no stale active paths were found.
- CR-RLN-M4-1 resolution privacy check passed: `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/repository-layout-normalization tests tools` checked 105 files.
- CR-RLN-M4-1 resolution diff check passed: `git diff --check`.
- Code-review M4 R3 reviewer reran `python3 -m unittest discover -s tests`; passed, ran 79 tests.
- Code-review M4 R3 reviewer reran `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`; passed, checked 18 Markdown files.
- Code-review M4 R3 reviewer reran `rg -n "media/equipment|media/movements|media/supplemental|content/|schemas/|generated/|tools/validation" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools media/PROVENANCE.md`; no matches, exit 1 expected for `rg` no-match.
- Code-review M4 R3 reviewer reran `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/repository-layout-normalization tests tools`; checked 105 files, privacy pass.
- Code-review M4 R3 reviewer reran `git diff --check`; passed.
- Explain-change privacy check passed: `python3 tools/checks/check_privacy.py docs/changes/repository-layout-normalization/explain-change.md docs/plans/2026-06-29-repository-layout-normalization.md docs/plan.md docs/changes/repository-layout-normalization/change.yaml` checked 4 files.
- Explain-change diff check passed: `git diff --check`.
- Verify full unit suite passed: `python3 -m unittest discover -s tests` ran 79 tests.
- Verify checker validation passed: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` checked 18 Markdown files.
- Verify active old content/red-flags scan passed with no matches: `rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools` returned exit 1 because no stale active paths were found.
- Verify active stale media/historical scan passed with no matches: `rg -n "media/equipment|media/movements|media/supplemental|content/|schemas/|generated/|tools/validation" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools media/PROVENANCE.md` returned exit 1 because no stale active paths were found.
- Verify privacy check passed: `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/repository-layout-normalization tests tools` checked 106 files.
- Verify old-directory check passed: `find 01-getting-started 02-machines 03-bodyweight about media/equipment media/movements media/supplemental media/svg content schemas generated tools/validation -maxdepth 0 -print 2>/dev/null || true` returned no paths.
- Verify diff check passed: `git diff --check`.

## Outcome and retrospective

- Completed by PR #5 after final local verification and PR handoff.

## Readiness

- See `Current Handoff Summary`.
- Complete. No downstream lifecycle gate remains for this plan.
