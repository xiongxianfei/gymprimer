# Review Resolution: Repository Layout Normalization

## Spec-review R1 Resolution

### SR-RLN-1 — Old-path compatibility policy

Status: resolved

Required outcome: choose whether old numbered v0.1 paths are removed immediately or retained as compatibility stubs, and make that choice deterministic in the spec before test-spec, plan, or implementation.

Disposition: the spec now chooses direct removal. Old numbered content paths must be removed directly, promoted content must link to canonical paths, and compatibility stubs are not allowed.

Spec changes:

- Updated E1 and E3 to require direct removal of old numbered paths.
- Replaced the compatibility-stub requirements with direct-removal requirements.
- Updated error behavior, migration behavior, observability, edge cases, and acceptance criteria to fail lingering old-path stubs.

### SR-RLN-2 — Root red-flags and orientation-path policy

Status: resolved

Required outcome: define canonical treatment for `the former nested red-flags path.md` and `the former getting-started directory/beginner-training-principles.md` inside this migration.

Disposition: the spec now chooses root `RED-FLAGS.md` as canonical and `principles/beginner-training-principles.md` as the canonical beginner-principles path.

Spec changes:

- Added E5 for direct red-flags migration.
- Added R6 requiring `the former nested red-flags path.md` to move to root `RED-FLAGS.md`.
- Updated state, accessibility, edge cases, and acceptance criteria for the root red-flags path.

### SR-RLN-3 — Media migration determinism

Status: resolved

Required outcome: make media co-location testable by requiring touched promoted media to move to `media/<content-type>/<slug>/`, or explicitly defer media co-location.

Disposition: the spec now requires media referenced by promoted content to move directly to subject-co-located paths under `media/<content-type>/<slug>/`.

Spec changes:

- Replaced the non-deterministic media SHOULD with a MUST.
- Updated migration ordering to move media into subject-co-located paths.
- Updated EC1 and acceptance criteria to validate direct media-path migration.

## Additional Decision

Historical structured-platform artifacts must be removed directly when no active approved spec, test, workflow guide, or validation command relies on them. If an active dependency still requires retention, the artifact must be labeled historical or archived.

## Plan-review R1 Resolution

### PR-RLN-1 — Test-spec ownership in implementation milestone

Status: resolved

Required outcome: remove test-spec authoring ownership from implementation milestones. The plan should state that `specs/repository-layout-normalization.test.md` is created during the downstream `test-spec` stage after clean plan-review, and implementation consumes that approved test spec.

Recommended disposition: remove `specs/repository-layout-normalization.test.md` from M2 "Files/components likely touched", remove AC3 from implementation milestone ownership, and add a pre-implementation dependency that test-spec maps R1-R25 and EC1-EC9 before M1 starts.

Resolution:

- Removed `specs/repository-layout-normalization.test.md` from M2 implementation file ownership.
- Reassigned AC3 to the downstream test-spec stage before implementation.
- Added a pre-implementation dependency that test-spec maps R1-R25 and EC1-EC9 before M1 starts.
- Added a decision-log row explaining that test-spec ownership stays outside implementation milestones.

## Test-spec-review R1 Findings

### TSR-RLN-1 — Missing test and command milestone ownership

Status: resolved

Required outcome: the test spec must add a milestone/ownership map for RLN-T1 through RLN-T11 and the planned validation command set, including classification, owning milestone, first meaningful execution, and failure behavior.

Safe resolution path: add a "Test ownership map" and "Planned validation command ownership" section. Keep AC3/test-spec ownership outside implementation milestones while assigning the proof artifacts and validation commands to M1-M4 or closeout.

Resolution:

- Added `Test ownership map` to `specs/repository-layout-normalization.test.md`, assigning RLN-T1 through RLN-T11 to owners, milestones, first meaningful execution points, classifications, and closeout evidence.
- Added `Planned validation command ownership`, assigning RLN-CMD1 through RLN-CMD8 to owners, milestones, required-starting points, expected failure behavior, and closeout evidence.
- Preserved the pre-implementation role of `specs/repository-layout-normalization.test.md`; test-spec authoring is not assigned to M1-M4.

### TSR-RLN-2 — Manual proof records are under-specified

Status: resolved

Required outcome: the test spec must define bounded manual proof records with stable IDs, owners, owning stages, automation rationale, exact required fields or steps, pass/fail conditions, rerun triggers, and privacy statements.

Safe resolution path: add a "Manual proof ownership" section for dependency inventory, historical artifact disposition, final validation ledger, and observability/command-output review where needed.

Resolution:

- Superseded the manual-proof requirement by removing manual-only proof ownership from `specs/repository-layout-normalization.test.md`.
- Replaced manual-proof artifact paths with deterministic evidence records under `docs/changes/repository-layout-normalization/evidence/`.
- Updated test levels and coverage maps so R1-R25 and EC1-EC9 are covered by automated tests, migration checks, smoke checks, contract checks, and evidence records rather than manual proof.
- Updated the plan to refer to evidence records instead of manual proof.

## Code-review M3 R1 Findings

### CR-RLN-M3-1 — M3 rewrote exact dependency-inventory proof into placeholders

Status: resolved

Finding source: `docs/changes/repository-layout-normalization/reviews/code-review-m3-r1.md`

Required outcome: restore or re-establish exact migration proof without making the active stale-path scan depend on erasing historical evidence. M1 inventory and validation metadata must report the actual paths and commands used for the dependency inventory, or a clearly reviewed historical-path allowlist/exclusion must preserve exact historical proof while keeping the M3 stale active-path check deterministic.

Safe resolution path: restore exact M1 inventory command/path rows and exact M1 validation metadata, then adjust the M3 stale-path validation evidence so it distinguishes active content/reference scans from intentional historical proof records. If the validation command scope changes materially, update the plan/test-spec evidence first; otherwise record the narrowed historical-proof handling here, rerun M3 validation, and request M3 code-review again.

Resolution:

- Restored the exact M1 inventory command in `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md`.
- Restored exact M1 path rows for the old numbered content directories and `about/red-flags.md`.
- Restored exact M1 validation metadata in `docs/changes/repository-layout-normalization/change.yaml`.
- Updated RLN-CMD4 in `specs/repository-layout-normalization.test.md` to scan active surfaces only: `README.md`, `SOURCES.md`, `RED-FLAGS.md`, promoted content directories, `tests`, and `tools`.
- Updated the M3 plan validation command and validation notes to distinguish active stale-reference validation from intentional historical proof records.
- Reran M3 validation and routed M3 back to code-review.
