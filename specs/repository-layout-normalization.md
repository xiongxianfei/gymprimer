# Spec: Repository Layout Normalization

## Status

draft

## Related proposal

- Upstream direction: `docs/proposals/2026-06-29-responsible-breadth.md`
- Governing architecture: `docs/architecture/system/architecture.md`
- Related specs: `specs/markdown-first-primer.md`,
  `specs/responsible-breadth.md`

## Goal and context

Normalize the repository toward the approved five-block architecture:
project references, content, media, governance, and tooling/operations.

The current tree still contains numbered v0.1 content folders, image-type media
buckets, and historical structured-platform folders. Those paths were preserved
for compatibility while Responsible Breadth was implemented. This spec defines
the migration contract required before files are moved or removed.

This spec does not authorize implementation until spec-review, architecture
review or ADR update, test-spec, plan, and plan-review are complete.

## Glossary

- Canonical content path: the single preferred Markdown location for a content
  type after migration.
- Legacy content path: a previously valid Markdown path retained only for
  compatibility, history, or temporary migration.
- Historical platform artifact: schema-first or generated-output artifact from
  the superseded structured-platform direction.
- Compatibility stub: a short Markdown file left at an old path that points to
  the canonical file without duplicating content.
- Subject-co-located media: media stored under `media/<content-type>/<slug>/`.

## Examples first

Example E1: machine exercise migration
Given `02-machines/lat-pulldown.md` exists
When layout normalization is implemented
Then the canonical page is `exercises/lat-pulldown.md`, links point there, and
the old path is either removed from active navigation or replaced by a
compatibility stub for one migration window.

Example E2: bodyweight exercise migration
Given `03-bodyweight/incline-push-up.md` exists
When layout normalization is implemented
Then the canonical page is `exercises/incline-push-up.md`, equipment or
modality becomes metadata inside the page, and no new bodyweight folder is
created.

Example E3: beginner principle migration
Given `01-getting-started/beginner-training-principles.md` exists
When layout normalization is implemented
Then the canonical page is under `principles/`, unless a reviewed spec chooses
a root orientation file instead.

Example E4: media co-location
Given `media/movements/glute-bridge-sequence.png` supports
`exercises/glute-bridge.md`
When media paths are normalized
Then the canonical media path is under `media/exercises/glute-bridge/`, page
links and `media/PROVENANCE.md` rows are updated together, and the old image
path is no longer referenced by promoted content.

Example E5: governance paths remain under `docs/`
Given `docs/proposals/` and `docs/adr/` exist
When layout normalization is implemented
Then those paths remain unchanged because the workflow guide standardizes
RigorLoop artifact locations under `docs/`.

Example E6: historical structured-platform artifacts
Given `content/`, `schemas/`, and `generated/` are historical artifacts
When layout normalization is implemented
Then they are removed or archived only after tests, specs, and docs that still
reference them are updated or explicitly marked historical.

## Requirements

R1. The repository MUST preserve the approved five logical blocks:
project references, content, media, governance, and tooling/operations.

R2. The canonical content directories MUST be `exercises/`, `patterns/`,
`conditions/`, `principles/`, and `programs/`.

R3. The migration MUST fold `02-machines/` and `03-bodyweight/` exercise pages
into `exercises/`.

R4. Equipment type, bodyweight status, machine status, difficulty, and movement
pattern MUST be represented as page metadata or page content, not top-level
folder identity.

R5. The migration MUST fold `01-getting-started/` into `principles/`, unless
spec-review approves a root orientation file as the only exception.

R6. Pattern, condition, principle, program, and already-canonical exercise
paths MUST remain stable unless a specific file is renamed by the migration
plan.

R7. Media referenced by promoted content SHOULD be moved toward
`media/<content-type>/<slug>/` subject co-location.

R8. Every moved raster media asset MUST have its Markdown references and
`media/PROVENANCE.md` `asset_path` and `page_refs` updated in the same change.

R9. The migration MUST NOT leave promoted Markdown pages pointing at removed or
stale media paths.

R10. `docs/proposals/`, `docs/adr/`, `docs/architecture/`, `docs/changes/`,
`docs/plans/`, and `docs/learn/` MUST remain under `docs/`.

R11. Governance, workflow, proof, plan, and review artifacts MUST NOT be
flattened into the content block.

R12. Historical platform artifacts such as `content/`, `schemas/`, generated
validation reports, and structured-platform tests MAY be removed only when no
active approved spec, test, workflow guide, or validation command relies on
them.

R13. If a historical artifact is retained, it MUST be labeled historical or
archived so contributors do not treat it as active product architecture.

R14. The migration MUST update README, navigation, source references, tests,
checkers, manual proof, and change metadata that reference moved paths.

R15. The migration MUST include automated tests proving that canonical content
paths pass validation and that old active paths are not required for promoted
content.

R16. The migration MUST include link validation or equivalent deterministic
checks for Markdown links and media references touched by the move.

R17. The migration MUST include provenance validation for moved raster media.

R18. The migration MUST preserve Markdown as the source of truth and MUST NOT
introduce a CMS, hosted app dependency, runtime API, search index dependency, or
generated HTML authority.

R19. The migration MUST NOT change health-adjacent content boundaries,
diagnosis/treatment refusals, citation policy, or media source-of-truth rules.

R20. Any compatibility stubs left at old paths MUST be short, non-canonical,
and excluded from duplicate content validation where necessary.

R21. Compatibility stubs MUST NOT contain duplicate exercise, pattern,
condition, principle, or program instructions.

R22. The migration plan MUST define whether old paths are removed immediately
or kept as compatibility stubs for one review window.

R23. The implementation MUST report exact validation commands and whether CI
was observed.

## Inputs and outputs

Inputs:

- Existing Markdown pages under numbered v0.1 folders and canonical content
  folders.
- Existing media under `media/`.
- `media/PROVENANCE.md`.
- README, specs, tests, checkers, docs, manual proof, and change metadata that
  reference moved paths.

Outputs:

- Normalized file tree matching the approved content and media blocks.
- Updated Markdown links and media references.
- Updated provenance rows.
- Updated tests and validation commands.
- Optional compatibility stubs or removal records for old paths.

## State and invariants

- Markdown remains canonical.
- Source citations remain page-local with reusable sources in `SOURCES.md`.
- `media/PROVENANCE.md` remains the provenance index for AI-generated raster
  assets.
- Governance remains under `docs/`.
- Historical structured-platform artifacts are inactive unless a later accepted
  proposal reactivates them.

## Error and boundary behavior

- If a moved Markdown file leaves a broken link, validation fails.
- If a moved raster image lacks an updated provenance row, validation fails.
- If an old path remains active navigation after its canonical replacement is
  promoted, validation fails unless the path is an approved compatibility stub.
- If a historical artifact is still referenced by active tests or specs, it
  must not be deleted without updating those active references.
- If deleting historical generated output would remove required validation
  evidence for an active change, deletion must wait for a reviewed archival or
  replacement plan.

## Compatibility and migration

The migration must happen in an explicit migration plan after spec-review and
architecture/ADR review. The plan must enumerate each path move, each path
removal, each compatibility stub, and each validation command.

Recommended migration order:

1. Add tests for canonical path validation and old-path behavior.
2. Move exercise and principle Markdown pages.
3. Update all internal links and navigation.
4. Move media into subject-co-located paths where feasible.
5. Update `media/PROVENANCE.md`.
6. Remove or archive historical structured-platform artifacts that have no
   active references.
7. Run full targeted validation and record evidence.

Rollback:

- Restore old paths or compatibility stubs.
- Revert link and provenance updates.
- Re-run Markdown, media, privacy, and unit validation.

## Observability

Validation output should identify:

- broken Markdown link path;
- stale old-path reference;
- missing canonical target;
- missing media asset;
- stale `media/PROVENANCE.md` `asset_path`;
- stale `page_refs`;
- historical artifact that is still actively referenced.

Manual proof should record files moved, files removed, compatibility stubs
created, and validation commands run.

## Security and privacy

The migration must not introduce secrets, private data, private machine paths,
reader health details, or unlicensed media. Privacy checks must include moved
Markdown, moved media provenance rows, migration proof, and updated validation
fixtures.

## Accessibility and UX

Markdown pages and media references must remain usable directly in GitHub.
Images must retain alt text or nearby explanatory text after path migration.
Compatibility stubs, if used, must provide a clear link to the canonical page.

## Performance expectations

Repository-local validation for the normalized tree should remain practical for
local development. The migration should not require network access for core
validation.

## Edge cases

EC1. A pattern page links to `../media/movements/dead-bug-preview.png` after the
asset moved to `media/patterns/anterior-pelvic-tilt/`: fails until the link is
updated.

EC2. `media/PROVENANCE.md` still lists the old `asset_path` after an image
move: fails provenance validation.

EC3. `README.md` links `02-machines/lat-pulldown.md` after the canonical page
is `exercises/lat-pulldown.md`: fails navigation validation unless the old path
is an approved compatibility stub.

EC4. A compatibility stub duplicates full exercise instructions: fails because
old paths must not become duplicate source content.

EC5. `docs/proposals/` is moved to root-level `proposals/`: fails because
workflow artifact locations remain under `docs/`.

EC6. `content/` is deleted while an active test still expects fixture data
there: fails until the active test is removed, archived, or updated under a
reviewed migration.

EC7. A generated report under `generated/` is deleted but still cited as
current validation evidence: fails until replacement evidence is recorded.

## Non-goals

- Changing the product scope, safety boundaries, citation standards, or
  Responsible Breadth page contracts.
- Rewriting content quality while moving files.
- Moving governance artifacts out of `docs/`.
- Introducing mdBook publication, hosting, CMS, search, runtime services, or
  analytics.
- Recreating generated historical output.
- Removing tests merely to make deletion easier.

## Acceptance criteria

AC1. Spec-review approves this migration spec before implementation relies on
it.

AC2. Architecture review or ADR update approves the physical directory
migration boundary before planning.

AC3. A test spec maps R1-R23 and EC1-EC7 to automated tests or manual proof.

AC4. A migration plan enumerates every moved path, removed path, retained
compatibility stub, validation command, and rollback step.

AC5. After implementation, promoted Markdown pages pass validation from
canonical paths.

AC6. After implementation, no promoted Markdown page links to removed media or
removed old content paths.

AC7. After implementation, every moved raster asset has an updated approved
provenance row.

AC8. After implementation, governance artifacts still live under `docs/`.

AC9. After implementation, historical structured-platform artifacts are either
removed safely or clearly labeled/archived as historical.

AC10. The implementation reports exact local validation commands and does not
claim CI unless observed.

## Open questions

1. Should old numbered Markdown paths be removed immediately or retained as
   compatibility stubs for one review window?
2. Should `about/red-flags.md` remain in `about/`, move to root
   `RED-FLAGS.md`, or keep both with one canonical path?
3. Should historical structured-platform specs and tests be deleted, moved to
   an archive, or retained with explicit historical labels?

## Next artifacts

1. Spec-review for this migration spec.
2. Architecture review or ADR amendment for the physical migration boundary.
3. Test-spec mapping layout and media migration proof.
4. Migration execution plan.

## Follow-on artifacts

None yet

## Readiness

Ready for spec-review. Not architecture-ready, plan-ready,
implementation-ready, code-review-ready, verification-ready, branch-ready, or
PR-ready until the downstream workflow gates complete.
