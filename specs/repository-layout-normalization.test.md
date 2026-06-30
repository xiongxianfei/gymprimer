# Test Spec: Repository Layout Normalization

## Status

draft

## Related spec and plan

- Spec: `specs/repository-layout-normalization.md`
- Plan: `docs/plans/2026-06-29-repository-layout-normalization.md`
- Architecture: `docs/architecture/system/architecture.md`
- ADR: `docs/adr/2026-06-29-direct-repository-layout-normalization.md`
- Spec review: `docs/changes/repository-layout-normalization/reviews/spec-review-r2.md`
- Architecture review: `docs/changes/repository-layout-normalization/reviews/architecture-review-r1.md`
- Plan review: `docs/changes/repository-layout-normalization/reviews/plan-review-r2.md`

## Testing strategy

The proof strategy is migration-first: prove dependencies are inventoried, prove the validator catches stale paths before files move, then prove the real normalized tree passes from canonical paths only.

- Unit: checker tests for canonical content directories, old numbered content paths, root `RED-FLAGS.md`, stale media buckets, provenance path updates, compatibility stubs, governance path preservation, historical artifact disposition, and migration evidence records.
- Integration: run the repository Markdown/media/privacy checks against real canonical paths after each migration milestone.
- End-to-end: validate the final repository tree from README/project references through content pages, media assets, provenance rows, and governance artifacts without relying on removed paths.
- Smoke: assert the expected canonical paths exist, old paths are absent, and validation commands are recorded.
- Evidence records: record dependency inventory, path move manifest, historical artifact dispositions, and final validation ledger as deterministic change evidence, not as a separate manual-proof requirement.
- Contract: prove the normalized layout preserves Markdown-first source authority, governance under `docs/`, and unchanged safety/content boundaries.
- Migration: prove old paths are removed directly with no compatibility stubs and that active references are updated before removal.

Existing `unittest` tests remain the preferred automation style. New tests should use temporary directories and fixture trees under `tests/fixtures/repository_layout_normalization/` so stale-path behavior can be asserted without depending on transient working-tree state.

## Test ownership map

| Test ID | Proof area | Owner | Owning milestone | First meaningful execution | Classification | Closeout evidence |
| --- | --- | --- | --- | --- | --- | --- |
| RLN-T1 | Canonical content path validation | tooling maintainer | M2 | M2 | planned-for-milestone | `tests/test_repository_layout_normalization.py` |
| RLN-T2 | Root red-flags reference validation | tooling maintainer | M2 | M2 | planned-for-milestone | red-flags path fixture tests |
| RLN-T3 | Dependency inventory and migration manifest proof | migration maintainer | M1 | M1 | planned-for-milestone | `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md` |
| RLN-T4 | Stale old-path references and compatibility stubs fail | tooling maintainer | M2 | M2 | planned-for-milestone | stale-path and no-stub fixture tests |
| RLN-T5 | Subject-co-located media and provenance validation | tooling maintainer | M2 for fixture behavior; M4 for real migrated media | M2 | planned-for-milestone | media/provenance fixture tests and M4 real-tree validation |
| RLN-T6 | Governance path preservation | tooling maintainer | M2 | M2 | planned-for-milestone | governance path fixture tests |
| RLN-T7 | Historical artifact disposition proof | migration maintainer | M4 | M1 for inventory; M4 for final disposition | planned-for-milestone | `docs/changes/repository-layout-normalization/evidence/historical-artifact-disposition.md` |
| RLN-T8 | End-to-end normalized tree smoke | release/check maintainer | closeout | M3 partial; M4/closeout final | planned-for-milestone | final validation ledger and plan validation command transcripts |
| RLN-T9 | Markdown authority and safety-boundary preservation | release/check maintainer | M3 and M4 | M3 | planned-for-milestone | final validation ledger scope-boundary note |
| RLN-T10 | Observability and validation-output proof | tooling maintainer | M2 | M2 | planned-for-milestone | failing fixture assertions and final validation ledger |
| RLN-T11 | Workflow gate and lifecycle proof | release/check maintainer | closeout | before M1 and at closeout | planned-for-milestone | change metadata, review log, and final validation ledger |

This section assigns implementation proof ownership only. It does not assign test-spec authoring to M1-M4; `specs/repository-layout-normalization.test.md` remains a pre-implementation workflow artifact.

## Planned validation command ownership

| Command ID | Command | Classification | Owner | Owning milestone | Required starting | Allowed before owning milestone? | Expected failure behavior | Closeout evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RLN-CMD1 | `rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags|media/equipment|media/movements|media/supplemental|content/|schemas/|generated/" .` | planned-for-milestone | migration maintainer | M1 | M1 | yes | M1 fails if active references are not recorded with disposition. Historical references may remain only when classified. | dependency inventory evidence |
| RLN-CMD2 | `python3 -m unittest discover -s tests` | planned-for-milestone | tooling maintainer | M2 | M2 | yes | From M2 onward, unexpected nonzero exit fails the milestone. Zero-test discovery for `test_repository_layout_normalization.py` fails M2. | unit test transcript |
| RLN-CMD3 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` | planned-for-milestone | tooling maintainer | M3 | M3 | yes | From M3 onward, nonzero exit fails content/reference migration. Before `RED-FLAGS.md` exists, absence is expected and not closeout proof. | checker transcript |
| RLN-CMD4 | `rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools` | planned-for-milestone | migration maintainer | M3 | M3 | yes | M3 fails if active old content or red-flags references remain in promoted content, tests, or tools. Change-history artifacts may retain exact old paths only as classified historical proof. | M3 validation transcript plus review-resolution disposition when historical proof records retain exact old paths |
| RLN-CMD5 | `rg -n "media/equipment|media/movements|media/supplemental|content/|schemas/|generated/|tools/validation" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools media/PROVENANCE.md` | planned-for-milestone | migration maintainer | M4 | M4 | yes | M4 fails if active old media-bucket, historical structured-platform, or structured validation-tool references remain in active surfaces. Change-history artifacts may retain exact old paths only as classified historical proof. | M4 validation transcript plus disposition evidence when historical proof records retain exact old paths |
| RLN-CMD6 | `python3 tools/checks/check_privacy.py docs/changes/repository-layout-normalization` | existing | migration maintainer | M1 | M1 | yes | Nonzero exit fails M1 proof hygiene. | privacy transcript |
| RLN-CMD7 | `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/repository-layout-normalization tests tools` | planned-for-milestone | release/check maintainer | M4 | M4 | yes | From M4 onward, forbidden finding or setup error fails the milestone. | privacy transcript |
| RLN-CMD8 | `git diff --check` | existing | release/check maintainer | M1-M4 and closeout | M1 | yes | Any whitespace error fails the current milestone or closeout. | command transcript |

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | RLN-T1, RLN-T8 | integration, smoke | Final tree is checked against the five logical blocks. |
| R2 | RLN-T1, RLN-T8 | unit, smoke | Canonical content directories are accepted. |
| R3 | RLN-T1, RLN-T4, RLN-T8 | unit, migration, smoke | Machine/bodyweight pages move into `exercises/`; old folders are rejected after migration. |
| R4 | RLN-T1, RLN-T8 | unit, smoke | Equipment/modality cannot be represented by top-level folder split. |
| R5 | RLN-T1, RLN-T4, RLN-T8 | unit, migration, smoke | Beginner principles move to `principles/` and old path disappears. |
| R6 | RLN-T2, RLN-T4, RLN-T8 | unit, migration, smoke | `RED-FLAGS.md` becomes the root canonical safety reference. |
| R7 | RLN-T1, RLN-T8 | integration, smoke | Already-canonical content paths stay stable unless listed in the manifest. |
| R8 | RLN-T5, RLN-T8 | unit, smoke | Promoted media moves to `media/<content-type>/<slug>/`. |
| R9 | RLN-T5, RLN-T8 | unit, integration | Moved raster assets require updated Markdown references and provenance rows. |
| R10 | RLN-T4, RLN-T5, RLN-T8 | unit, migration, smoke | Promoted Markdown cannot point at removed media paths. |
| R11 | RLN-T6, RLN-T8 | unit, smoke | Governance paths remain under `docs/`. |
| R12 | RLN-T6, RLN-T8 | unit, smoke | Governance/evidence artifacts are not flattened into content directories. |
| R13 | RLN-T7, RLN-T8 | migration, smoke | Historical artifacts are removed only when no active approved dependency remains. |
| R14 | RLN-T7, RLN-T8 | migration, smoke | Retained historical artifacts require explicit historical/archive labeling. |
| R15 | RLN-T3, RLN-T7 | migration | Dependency inventory records active references before any move or removal. |
| R16 | RLN-T3, RLN-T4, RLN-T7 | migration | Active references are updated or removed before the old target disappears. |
| R17 | RLN-T3, RLN-T4, RLN-T8 | migration, smoke | README, navigation, source references, tests, checkers, evidence, and metadata are updated. |
| R18 | RLN-T1, RLN-T4, RLN-T8 | unit, integration, smoke | Automated tests prove canonical paths pass and old active paths are not required. |
| R19 | RLN-T2, RLN-T4, RLN-T5, RLN-T8 | unit, integration, smoke | Deterministic link/media validation covers touched references. |
| R20 | RLN-T5 | unit, integration | Raster media provenance validation covers moved assets. |
| R21 | RLN-T8, RLN-T9 | smoke, contract | Markdown remains source of truth and no runtime/app/search/generated authority appears. |
| R22 | RLN-T8, RLN-T9 | smoke, contract | Safety, diagnosis/treatment refusals, citation policy, and media source rules do not change. |
| R23 | RLN-T4, RLN-T8 | migration, smoke | Old numbered content paths are removed directly with no stubs. |
| R24 | RLN-T4, RLN-T5, RLN-T8 | migration, integration, smoke | Old media buckets are removed after references and provenance rows are updated. |
| R25 | RLN-T10, RLN-T11 | smoke | Exact validation commands are reported and CI is not claimed unless observed. |

## Example coverage map

| Example ID | Covered by | Notes |
| --- | --- | --- |
| E1 | RLN-T1, RLN-T4, RLN-T8 | Machine exercise migration to `exercises/` and direct old-path removal. |
| E2 | RLN-T1, RLN-T8 | Bodyweight exercise migration to `exercises/` without new bodyweight folder. |
| E3 | RLN-T1, RLN-T4, RLN-T8 | Beginner principles migration to `principles/`. |
| E4 | RLN-T5, RLN-T8 | Media co-location plus provenance updates. |
| E5 | RLN-T2, RLN-T4, RLN-T8 | Root `RED-FLAGS.md` migration and old `about/red-flags.md` removal. |
| E6 | RLN-T6, RLN-T8 | Governance paths remain under `docs/`. |
| E7 | RLN-T7, RLN-T8 | Historical artifacts removed or retained as explicitly historical. |

## Edge case coverage

| Edge case ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | RLN-T5 | unit | Old `media/movements/` Markdown link fails after move. |
| EC2 | RLN-T5 | unit | Stale `media/PROVENANCE.md` `asset_path` fails. |
| EC3 | RLN-T4 | unit | README link to old numbered content path fails. |
| EC4 | RLN-T4 | unit | Compatibility stub at an old path fails. |
| EC5 | RLN-T6 | unit | Root-level `proposals/` or `adr/` move fails. |
| EC6 | RLN-T7 | unit, migration | Historical artifact deletion fails while active tests still depend on it. |
| EC7 | RLN-T7 | migration | Generated validation evidence cannot be deleted while cited as current evidence. |
| EC8 | RLN-T2, RLN-T4 | unit | Link to `about/red-flags.md` fails after `RED-FLAGS.md` is canonical. |
| EC9 | RLN-T3, RLN-T4, RLN-T7 | migration | Removal fails while any active checker, test, evidence record, navigation, provenance, or Markdown dependency remains. |

## Test cases

T1. Canonical content path validation
- Covers: R1, R2, R3, R4, R5, R7, R18, E1, E2, E3
- Level: unit
- Fixture/setup: create fixture trees with canonical `exercises/`, `patterns/`, `conditions/`, `principles/`, and `programs/` directories, plus negative fixture trees with active numbered content directories.
- Steps: run the layout validation helper or Markdown-first checker against each fixture.
- Expected result: canonical fixture passes; active `01-getting-started/`, `02-machines/`, or `03-bodyweight/` content fails unless it is a historical fixture explicitly outside promoted content.
- Failure proves: canonical content routing or old numbered path rejection is not enforceable.
- Automation location: `tests/test_repository_layout_normalization.py`

T2. Root red-flags reference validation
- Covers: R6, R17, R19, E5, EC8
- Level: unit
- Fixture/setup: create one fixture with links to `RED-FLAGS.md` and another with links to `about/red-flags.md`.
- Steps: run link validation over the fixtures.
- Expected result: root `RED-FLAGS.md` links pass; `about/red-flags.md` links fail after migration.
- Failure proves: the safety-reference migration can leave stale active links.
- Automation location: `tests/test_repository_layout_normalization.py`

T3. Dependency inventory and migration manifest proof
- Covers: R13, R14, R15, R16, R17, R23, R25, EC6, EC7, EC9
- Level: integration
- Fixture/setup: M1 writes `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md`.
- Steps: run dependency inventory checks and verify that each moved or removed path has canonical target, active references, disposition, update/removal status, and validation command.
- Expected result: no file move or deletion proceeds without a recorded dependency disposition.
- Failure proves: the migration is file-moving before dependencies are understood.
- Automation location: `tests/test_repository_layout_normalization.py` plus dependency inventory evidence.

T4. Stale old-path references and compatibility stubs fail
- Covers: R3, R5, R6, R10, R16, R17, R18, R19, R23, R24, E1, E3, E5, EC3, EC4, EC8, EC9
- Level: unit
- Fixture/setup: fixtures with README/navigation links to old paths and fixtures with compatibility stub files at removed paths.
- Steps: run stale-path validation over README, content, tests, tools, and change-local evidence scopes.
- Expected result: active old-path links and compatibility stubs fail with path-specific messages.
- Failure proves: direct removal and no-stub rules are not enforceable.
- Automation location: `tests/test_repository_layout_normalization.py`

T5. Subject-co-located media and provenance validation
- Covers: R8, R9, R10, R19, R20, R24, E4, EC1, EC2
- Level: unit
- Fixture/setup: fixtures with a moved raster asset under `media/exercises/glute-bridge/`, Markdown image references, and `media/PROVENANCE.md` rows.
- Steps: run media/provenance validation over matching and stale fixtures.
- Expected result: subject-co-located media with matching `asset_path` and `page_refs` passes; stale Markdown paths, stale `asset_path`, stale `page_refs`, or old media buckets fail.
- Failure proves: media moves and provenance updates can drift.
- Automation location: `tests/test_repository_layout_normalization.py`

T6. Governance path preservation
- Covers: R11, R12, E6, EC5
- Level: unit
- Fixture/setup: fixture with `docs/proposals/`, `docs/adr/`, `docs/architecture/`, `docs/changes/`, `docs/plans/`, and `docs/learn/`; negative fixture with root `proposals/` or `adr/`.
- Steps: run layout validation over governance fixture.
- Expected result: governance under `docs/` passes; flattened governance fails.
- Failure proves: workflow artifact locations can be confused with content architecture.
- Automation location: `tests/test_repository_layout_normalization.py`

T7. Historical artifact disposition evidence
- Covers: R13, R14, R15, R16, R17, E7, EC6, EC7, EC9
- Level: integration
- Fixture/setup: M1 inventory plus M4 final historical-artifact disposition evidence.
- Steps: run stale-reference checks and verify each `content/`, `schemas/`, `generated/`, and structured-platform test reference is removed, updated, or retained with historical/archive labeling because an active approved dependency remains.
- Expected result: no active dependency points to a deleted historical artifact; no retained historical artifact appears active product architecture.
- Failure proves: cleanup deleted required evidence or left historical architecture ambiguous.
- Automation location: `tests/test_repository_layout_normalization.py` plus historical artifact disposition evidence.

T8. End-to-end normalized tree smoke
- Covers: R1-R25, E1-E7
- Level: smoke
- Fixture/setup: actual repository after M3 and M4 migrations.
- Steps: run the full targeted validation command set from the plan against `README.md`, `SOURCES.md`, `RED-FLAGS.md`, canonical content directories, `media`, `tests`, `tools`, and change-local proof.
- Expected result: commands pass locally; old content paths, old red-flags path, old media bucket references, unclassified historical artifacts, and stubs are absent from active scopes.
- Failure proves: the final tree does not satisfy the approved migration contract.
- Automation location: plan validation commands and final validation ledger.

T9. Markdown authority and safety-boundary preservation
- Covers: R21, R22
- Level: contract
- Fixture/setup: actual repository diff and privacy/content-boundary checks.
- Steps: inspect that no CMS, hosted app dependency, runtime API, search index dependency, generated HTML authority, diagnosis/treatment boundary change, citation-policy change, or media-source-of-truth change was introduced.
- Expected result: only physical repository layout, references, validation, and proof records change.
- Failure proves: the migration changed product behavior or safety/content policy outside scope.
- Automation location: existing guardrail/privacy tests plus final validation ledger.

T10. Observability and validation-output proof
- Covers: R18, R19, R20, R25
- Level: integration
- Fixture/setup: failing fixtures for stale old path, missing canonical target, missing media asset, stale `asset_path`, stale `page_refs`, compatibility stub, removed-path dependency, and active historical dependency.
- Steps: run checker tests and inspect failure messages.
- Expected result: failure output identifies the concrete bad path or dependency class.
- Failure proves: migration failures cannot be diagnosed reliably.
- Automation location: `tests/test_repository_layout_normalization.py` plus final validation ledger.

T11. Workflow gate and lifecycle proof
- Covers: R25, AC3, plan pre-implementation dependency
- Level: smoke
- Fixture/setup: `specs/repository-layout-normalization.test.md`, plan, change metadata, and review-resolution records.
- Steps: confirm test spec maps R1-R25 and EC1-EC9 before M1 starts; confirm status routes to `test-spec-review`.
- Expected result: implementation remains blocked until this test spec is reviewed and approved.
- Failure proves: implementation can start without the required proof map.
- Automation location: change metadata and plan handoff review.

## Fixtures and data

Planned fixtures:

- `tests/fixtures/repository_layout_normalization/canonical_tree/`: valid canonical content, root red flags, governance under `docs/`, and subject-co-located media.
- `tests/fixtures/repository_layout_normalization/old_numbered_paths/`: active `01-getting-started/`, `02-machines/`, and `03-bodyweight/` references that must fail after migration.
- `tests/fixtures/repository_layout_normalization/old_red_flags_path/`: stale `about/red-flags.md` references.
- `tests/fixtures/repository_layout_normalization/compatibility_stub/`: old-path stubs that must fail.
- `tests/fixtures/repository_layout_normalization/media_provenance/`: matching and stale Markdown/media/provenance combinations.
- `tests/fixtures/repository_layout_normalization/governance_paths/`: valid `docs/` governance and invalid root-level governance alternatives.
- `tests/fixtures/repository_layout_normalization/historical_artifacts/`: active and historical references to `content/`, `schemas/`, and `generated/`.

Evidence artifacts:

- `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md`
- `docs/changes/repository-layout-normalization/evidence/historical-artifact-disposition.md`
- `docs/changes/repository-layout-normalization/evidence/final-validation-ledger.md`

## Mocking/stubbing policy

No network access is required. Tests should use temporary directories or fixtures copied into temporary directories. Compatibility stubs are test inputs only; the real migration must not leave stubs at removed paths. Do not mock the checker output so broadly that stale-path, link, or provenance assertions stop proving real validation behavior.

## Migration or compatibility tests

Migration tests must prove:

- canonical paths pass without old numbered content directories;
- `RED-FLAGS.md` is the only active red-flags target;
- old paths are removed directly and no stubs remain;
- every moved raster image has matching Markdown references and provenance rows;
- old media buckets are not referenced by promoted content;
- historical artifacts are removed only after active dependencies are updated or are retained with explicit historical/archive labeling;
- governance stays under `docs/`;
- rollback notes in the plan remain possible by restoring old paths and reverting reference/provenance updates.

## Observability verification

Validation output should identify the exact broken or stale item for:

- broken Markdown link path;
- stale old-path reference;
- missing canonical target;
- missing media asset;
- stale `media/PROVENANCE.md` `asset_path`;
- stale `page_refs`;
- lingering compatibility stub;
- dependency that still points at a removed path;
- historical artifact that is still actively referenced.

## Security/privacy verification

Run privacy checks over changed Markdown, media provenance, tests, tooling, migration evidence, and change metadata. The migration must not introduce secrets, private machine paths, identifying reader details, private health details, unlicensed media, or any health-adjacent content-boundary change.

Planned command family:

```bash
python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/repository-layout-normalization tests tools
```

## Performance checks

Repository-local validation must remain practical for local development and must not require network access. The final proof should include `python3 -m unittest discover -s tests` plus targeted checker commands; no new long-running build or hosted-service dependency is expected.

## Manual QA checklist

- Confirm `specs/repository-layout-normalization.test.md` maps R1-R25 and EC1-EC9 before M1 starts.
- Confirm the M1 dependency inventory before any old path is moved or removed.
- Review every moved path and removed path against the manifest.
- Confirm `README.md`, navigation, tests, tools, evidence records, and change metadata use canonical paths.
- Confirm `RED-FLAGS.md` exists at root and `about/red-flags.md` is gone with no stub.
- Confirm old numbered content paths are gone with no stubs.
- Confirm promoted media is subject-co-located and `media/PROVENANCE.md` matches exact paths and page references.
- Confirm historical artifacts are removed or clearly labeled/archived because an active dependency remains.
- Record exact local validation commands and whether CI was observed.

## What not to test

- Do not test hosted website publication, search, CMS behavior, runtime APIs, analytics, or generated HTML authority; these are explicitly out of scope.
- Do not test content-quality rewrites; this migration moves and validates files without changing instructional claims.
- Do not test external bookmark preservation; direct old-path removal is the accepted migration strategy.
- Do not test clinical, diagnosis, treatment, or programming behavior beyond proving the migration did not change existing boundaries.

## Uncovered gaps

None. R1-R25 and EC1-EC9 are mapped to automated tests, deterministic evidence records, or both.

## Next artifacts

1. Test-spec-review for this proof map.
2. M1 dependency inventory after test-spec-review approval.

## Follow-on artifacts

None yet

## Readiness

Ready for test-spec-review. Not implementation-ready until test-spec-review approves this proof map and M1 starts under the approved plan.
