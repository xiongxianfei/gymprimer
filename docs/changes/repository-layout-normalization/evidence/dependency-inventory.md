# Repository Layout Normalization M1 Dependency Inventory

Change ID: repository-layout-normalization
Milestone: M1 dependency inventory and migration manifest
Date: 2026-06-29

## Purpose

This evidence record inventories the old paths, active dependencies, and intended dispositions required before repository layout normalization moves or removes files.

No files are moved or removed in M1. M2 adds validation coverage first. M3 migrates Markdown content and project references. M4 migrates media and historical structured-platform artifacts.

## Inventory command

```bash
rg -n "01-getting-started|02-machines|03-bodyweight|about/red-flags|media/equipment|media/movements|media/supplemental|content/|schemas/|generated/" .
```

Result: matches found and categorized below. Matching is expected in M1 because this milestone records dependencies before migration.

## Existing legacy paths

| Path | Kind | Target disposition | Owning milestone |
| --- | --- | --- | --- |
| `01-getting-started/beginner-training-principles.md` | Markdown content | Move to `principles/beginner-training-principles.md`; remove `01-getting-started/` when empty | M3 |
| `02-machines/lat-pulldown.md` | Markdown content | Move to `exercises/lat-pulldown.md`; remove old path directly | M3 |
| `02-machines/seated-row.md` | Markdown content | Move to `exercises/seated-row.md`; remove old path directly | M3 |
| `02-machines/chest-press.md` | Markdown content | Move to `exercises/chest-press.md`; remove old path directly | M3 |
| `03-bodyweight/incline-push-up.md` | Markdown content | Move to `exercises/incline-push-up.md`; remove old path directly | M3 |
| `about/red-flags.md` | Project safety reference | Move to root `RED-FLAGS.md`; remove `about/` if empty | M3 |
| `media/equipment/*` | Raster media bucket | Move promoted assets under `media/exercises/<slug>/`; update references and provenance rows first | M4 |
| `media/movements/*` | Raster media bucket | Move promoted assets under `media/exercises/<slug>/` or `media/patterns/<slug>/`; update references and provenance rows first | M4 |
| `media/supplemental/README.md` | Historical/supplemental media note | Remove or archive according to active dependency result | M4 |
| `content/` | Historical structured-platform artifact | Remove when active specs/tests/tools no longer rely on it, otherwise label/archive as historical | M4 |
| `schemas/` | Historical structured-platform artifact | Remove when active specs/tests/tools no longer rely on it, otherwise label/archive as historical | M4 |
| `generated/` | Historical generated output | Remove when no active proof or historical reference requires retention, otherwise archive/label | M4 |

## Active Markdown and navigation dependencies

| Dependency | Current references | Required update |
| --- | --- | --- |
| `about/red-flags.md` | `README.md`, `conditions/non-specific-chronic-low-back-pain.md`, `patterns/anterior-pelvic-tilt.md`, Responsible Breadth tests/proof records | Update promoted content and README to `RED-FLAGS.md`; update or retire tests/proof records that still require old path |
| `01-getting-started/beginner-training-principles.md` | `README.md`, `patterns/anterior-pelvic-tilt.md`, Markdown-first specs/plans/proof records | Update promoted content to `principles/beginner-training-principles.md`; preserve old references only in historical artifacts |
| `02-machines/*.md` | `README.md`, `media/PROVENANCE.md`, Markdown-first specs/plans/proof records | Update promoted navigation and provenance page refs to `exercises/*.md`; preserve old references only in historical artifacts |
| `03-bodyweight/incline-push-up.md` | `README.md`, `media/PROVENANCE.md`, Markdown-first specs/plans/proof records | Update promoted navigation and provenance page refs to `exercises/incline-push-up.md`; preserve old references only in historical artifacts |

## Active media dependencies

| Asset or bucket | Current references | Required update |
| --- | --- | --- |
| `media/equipment/lat-pulldown-machine-example.png` | `CONTRIBUTING.md`, `media/PROVENANCE.md` | Move under `media/exercises/lat-pulldown/`; update Markdown image links and provenance row |
| `media/equipment/seated-row-machine-example.png` | `02-machines/seated-row.md`, `media/PROVENANCE.md` | Move under `media/exercises/seated-row/`; update Markdown image links and provenance row |
| `media/equipment/chest-press-machine-example.png` | `02-machines/chest-press.md`, `media/PROVENANCE.md` | Move under `media/exercises/chest-press/`; update Markdown image links and provenance row |
| `media/movements/front-lat-pulldown-example.png` | `02-machines/lat-pulldown.md`, `media/PROVENANCE.md` | Move under `media/exercises/lat-pulldown/`; update Markdown image links and provenance row |
| `media/movements/incline-push-up-phases-example.png` | `CONTRIBUTING.md`, `03-bodyweight/incline-push-up.md`, `media/PROVENANCE.md` | Move under `media/exercises/incline-push-up/`; update Markdown image links and provenance row |
| `media/movements/anterior-pelvic-tilt-comparison.png` | `patterns/anterior-pelvic-tilt.md`, `media/PROVENANCE.md` | Move under `media/patterns/anterior-pelvic-tilt/`; update Markdown image link and provenance row |
| `media/movements/dead-bug-sequence.png` | `exercises/dead-bug.md`, `media/PROVENANCE.md` | Move under `media/exercises/dead-bug/`; update Markdown image link and provenance row |
| `media/movements/plank-sequence.png` | `exercises/plank.md`, `media/PROVENANCE.md` | Move under `media/exercises/plank/`; update Markdown image link and provenance row |
| `media/movements/bird-dog-sequence.png` | `exercises/bird-dog.md`, `media/PROVENANCE.md` | Move under `media/exercises/bird-dog/`; update Markdown image link and provenance row |
| `media/movements/glute-bridge-sequence.png` | `exercises/glute-bridge.md`, `media/PROVENANCE.md` | Move under `media/exercises/glute-bridge/`; update Markdown image link and provenance row |
| `media/movements/hip-hinge-sequence.png` | `exercises/hip-hinge.md`, `media/PROVENANCE.md` | Move under `media/exercises/hip-hinge/`; update Markdown image link and provenance row |
| `media/movements/kneeling-hip-flexor-stretch-sequence.png` | `exercises/kneeling-hip-flexor-stretch.md`, `media/PROVENANCE.md` | Move under `media/exercises/kneeling-hip-flexor-stretch/`; update Markdown image link and provenance row |

## Historical structured-platform dependencies

| Artifact | Active references found | Required disposition |
| --- | --- | --- |
| `content/policies/review-routing-v1.json` | `tools/validation/validate_content.py`, `tests/test_review_routing_m3.py`, generated validation reports, historical structured-platform reviews | M4 must either remove/update the active tool/test dependency or retain the artifact as historical/archived with clear labeling |
| `content/taxonomy/v1.json` | `schemas/taxonomy.schema.json`, generated/manual evidence and historical docs | M4 must remove/update dependency or retain as historical/archived |
| `schemas/*.json` | `tools/validation/README.md`, old content-schema specs/plans/tests, generated reports | M4 must remove/update dependency or retain as historical/archived |
| `generated/*.json` and `generated/manual-proof/*` | Historical reviews, verify reports, old plan validation records | M4 must avoid deleting current validation evidence still cited by active change records; archive/label retained evidence |
| `tools/validation/*` | Historical structured-platform validation commands and tests | M4 must decide whether to remove with structured-platform artifacts or retain as historical tooling |

## M2 fixture candidates

The following dependencies should become regression fixtures or real-tree validation cases in M2:

- README links to old numbered content paths.
- Promoted pages linking to `about/red-flags.md`.
- Promoted pages linking to `../media/movements/*.png`.
- `media/PROVENANCE.md` rows whose `asset_path` or `page_refs` still use old paths.
- Compatibility stubs under old content directories.
- Historical `content/`, `schemas/`, or `generated/` paths referenced by active tests or tools.

## M1 disposition

M1 complete state:

- Dependency inventory recorded.
- No file moves performed.
- No old paths removed.
- M2 remains responsible for validation tooling and fixtures before M3/M4 migration work begins.
