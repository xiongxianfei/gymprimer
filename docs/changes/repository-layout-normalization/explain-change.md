# Repository Layout Normalization Change Rationale

## Summary

Repository layout normalization makes the physical tree match the approved five-block architecture: project references, content, media, governance, and tooling/operations. The change removes old numbered content paths, moves red flags to root `RED-FLAGS.md`, co-locates promoted raster media by content subject, and removes the superseded structured-platform implementation from the active tree after dependency inventory and validation coverage were in place.

This artifact explains why the implementation changed each area. It does not claim final verification, CI success, branch readiness, or PR readiness.

## Problem

The repository still carried several older layout conventions at once:

- numbered content directories: `01-getting-started/`, `02-machines/`, `03-bodyweight/`;
- nested safety reference path: `about/red-flags.md`;
- image-type media buckets: `media/equipment/`, `media/movements/`, `media/supplemental/`, and SVG examples;
- historical structured-platform artifacts: `content/`, `schemas/`, `generated/`, and `tools/validation/`;
- active tests and references that kept old paths looking valid.

That conflicted with the accepted architecture direction: one canonical content location per content type, root project references, subject-co-located media with provenance, governance under `docs/`, and tooling/operations clearly separated from product content.

## Decision Trail

| Source | Decision or requirement | Implementation effect |
| --- | --- | --- |
| `specs/repository-layout-normalization.md` R1-R2 | Preserve five logical blocks and canonical content directories. | Content paths now use `exercises/`, `patterns/`, `conditions/`, `principles/`, and `programs/`. |
| R3-R7 and R23 | Fold old numbered content paths and red flags into canonical paths with no stubs. | M3 moved first-slice Markdown pages and `RED-FLAGS.md`, then removed old content/red-flags paths directly. |
| R8-R10, R20, R24 | Move promoted media to `media/<content-type>/<slug>/` and update Markdown references plus provenance rows. | M4 moved raster assets under `media/exercises/<slug>/` and `media/patterns/<slug>/`, then updated `media/PROVENANCE.md`. |
| R13-R17 and AC10-AC12 | Inventory dependencies before removal and remove or label historical structured-platform artifacts. | M1 recorded exact old paths; M4 removed inactive structured-platform folders/tools/tests and recorded disposition evidence. |
| R21-R22 | Preserve Markdown-first source authority and safety/content boundaries. | No runtime, CMS, hosted app, generated authority, diagnosis, treatment, or content-scope change was introduced. |
| Architecture building blocks | Project references, content, media, governance, and tooling/operations are separate blocks. | README, architecture docs, media README, and checker behavior now reflect that split. |
| Test spec RLN-T1-RLN-T11 and RLN-CMD1-RLN-CMD8 | Validation ownership is milestone-specific and deterministic. | M1-M4 each produced evidence, tests, or command transcripts according to ownership. |

## Diff Rationale By Area

| Area | Files changed | Reason | Evidence |
| --- | --- | --- | --- |
| Dependency inventory | `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md` | Preserve exact old paths and classify active dependencies before removal, satisfying R15-R17. | M1 inventory command and M3 review-resolution restored exact command/path rows. |
| Checker enforcement | `tools/checks/check_markdown_first.py`, `tests/test_repository_layout_normalization.py` | Add deterministic failure behavior for old numbered paths, stale red-flags links, old media buckets, stale provenance rows, root-level governance folders, and unclassified historical artifacts. | `python3 -m unittest discover -s tests` and real-page checker runs passed. |
| Privacy checker fixtures | `tools/checks/check_privacy.py`, `tests/test_markdown_first_privacy.py` | Keep privacy validation usable after deleting old structured-platform/privacy fixtures that intentionally contained forbidden terms. | Privacy checks passed over the M4 active scope. |
| Content paths | `principles/`, `exercises/`, `patterns/anterior-pelvic-tilt.md`, README/source references/tests | Move old first-slice content into canonical content directories and update active links. | M3 active stale-path scan over README, active content, tests, and tools returned no matches. |
| Red flags | `RED-FLAGS.md`, content links, README, tests | Make root `RED-FLAGS.md` the canonical safety-routing reference and remove `about/red-flags.md` directly. | Markdown checker passed against root `RED-FLAGS.md`. |
| Media paths | `media/exercises/<slug>/...`, `media/patterns/anterior-pelvic-tilt/...`, exercise/pattern Markdown, `CONTRIBUTING.md` | Replace image-type buckets with subject-co-located media paths. | M4 stale media scan returned no active matches; media files exist under target paths. |
| Media provenance | `media/PROVENANCE.md`, media tests | Keep exact `asset_path` and `page_refs` synchronized with moved raster images. | Markdown checker validates raster provenance rows and page refs. |
| Historical artifact cleanup | removed `content/`, `schemas/`, `generated/`, `tools/validation/`, old tests and fixtures | Remove superseded structured-platform artifacts after active dependencies and tests were handled. | `historical-artifact-disposition.md` records final disposition; old-directory check returned no paths. |
| Documentation and architecture references | `README.md`, `media/README.md`, `docs/architecture/system/architecture.md`, ADR media note, templates | Keep contributor-facing and architecture-facing layout descriptions aligned with the normalized tree. | Code-review M4 R3 found no material findings. |
| Workflow records | plan, change metadata, review records, review-resolution, review-log | Maintain lifecycle state, validation evidence, and review traceability through M1-M4 and CR-RLN findings. | M4 is closed; final closeout remains. |
| Learning records | `docs/learn/sessions/2026-06-29-building-block-view-best-practices.md`, `docs/learn/topics/architecture.md` | Capture a separate architecture lesson requested by the maintainer. This is related context, not an implementation requirement for layout normalization. | Committed separately as `f7950bd`. |

## Tests Added Or Changed

| Test or proof area | What it proves |
| --- | --- |
| `tests/test_repository_layout_normalization.py` | Canonical content paths pass; old numbered paths, old red-flags links, compatibility stubs, old media buckets, stale provenance paths, root governance folders, and unclassified historical artifacts fail. |
| `tests/test_markdown_first_guardrails.py` | Raster media references still require approved provenance after media path normalization; text-only pages and SVG fixtures keep expected behavior. |
| `tests/test_responsible_breadth_m1.py` | Responsible Breadth page checks use normalized media paths for pattern/exercise references. |
| `tests/test_markdown_first_privacy.py` | Privacy checker still has a failing forbidden-term case without keeping forbidden content in tracked fixtures. |
| `docs/changes/repository-layout-normalization/evidence/historical-artifact-disposition.md` | RLN-T7 closeout evidence for removed structured-platform artifacts and moved media disposition. |

## Validation Evidence Before Final Verify

Latest reviewer-owned M4 R3 validation:

- `python3 -m unittest discover -s tests` passed, ran 79 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` passed, checked 18 Markdown files.
- `rg -n "media/equipment|media/movements|media/supplemental|content/|schemas/|generated/|tools/validation" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools media/PROVENANCE.md` returned no matches; exit 1 is expected for `rg` no-match.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/repository-layout-normalization tests tools` passed, checked 105 files.
- `git diff --check` passed.

CI was not observed.

## Review Resolution Summary

Material findings are resolved:

- `CR-RLN-M3-1`: resolved by restoring exact M1 inventory command/path rows and narrowing the M3 stale-path scan to active surfaces while preserving historical proof records.
- `CR-RLN-M4-1`: resolved by renaming the M4 disposition evidence to `docs/changes/repository-layout-normalization/evidence/historical-artifact-disposition.md`, matching RLN-T7.

See `docs/changes/repository-layout-normalization/review-resolution.md` for full dispositions. `docs/changes/repository-layout-normalization/reviews/code-review-m4-r3.md` closed M4 with no material findings.

## Alternatives Rejected

- Compatibility stubs at old content paths were rejected because the spec requires direct removal and no stale active paths.
- Keeping image-type media buckets was rejected because promoted media must be subject-co-located under `media/<content-type>/<slug>/`.
- Keeping structured-platform artifacts as active code was rejected because they are superseded by the Markdown-first route and no active approved dependency remained after M4 cleanup.
- Moving governance to root-level `proposals/` or `adr/` was rejected because this repository keeps RigorLoop governance artifacts under `docs/`.
- Recreating generated structured-platform output was rejected as out of scope.

## Scope Control

The change preserves the project boundaries:

- Markdown remains the source of truth.
- No mdBook publication, hosted app, CMS, runtime service, search, analytics, or generated HTML authority was introduced.
- No content-quality rewrite, diagnosis/treatment expansion, citation-policy change, media source-of-truth change, or Responsible Breadth page-contract change was introduced.
- Governance artifacts remain under `docs/`.

## Risks And Follow-Ups

- Final verification still needs to run after this explanation is committed.
- CI has not been observed.
- The remaining workflow stages are final `verify` and PR handoff if verification passes.
