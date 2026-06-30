# Repository Layout Normalization M4 Media and Historical Disposition

Change ID: repository-layout-normalization
Milestone: M4 media and historical-artifact cleanup
Date: 2026-06-30

## Purpose

This evidence record documents the M4 disposition for promoted media and superseded structured-platform artifacts after M3 closed the Markdown content-path migration.

## Media disposition

| Old path | New path | References updated |
| --- | --- | --- |
| `media/equipment/lat-pulldown-machine-example.png` | `media/exercises/lat-pulldown/lat-pulldown-machine-example.png` | `exercises/lat-pulldown.md`, `CONTRIBUTING.md`, `media/PROVENANCE.md` |
| `media/movements/front-lat-pulldown-example.png` | `media/exercises/lat-pulldown/front-lat-pulldown-example.png` | `exercises/lat-pulldown.md`, `media/PROVENANCE.md` |
| `media/equipment/seated-row-machine-example.png` | `media/exercises/seated-row/seated-row-machine-example.png` | `exercises/seated-row.md`, `media/PROVENANCE.md` |
| `media/equipment/chest-press-machine-example.png` | `media/exercises/chest-press/chest-press-machine-example.png` | `exercises/chest-press.md`, `media/PROVENANCE.md` |
| `media/movements/incline-push-up-phases-example.png` | `media/exercises/incline-push-up/incline-push-up-phases-example.png` | `exercises/incline-push-up.md`, `CONTRIBUTING.md`, `media/PROVENANCE.md` |
| `media/movements/anterior-pelvic-tilt-comparison.png` | `media/patterns/anterior-pelvic-tilt/anterior-pelvic-tilt-comparison.png` | `patterns/anterior-pelvic-tilt.md`, `media/PROVENANCE.md` |
| `media/movements/dead-bug-sequence.png` | `media/exercises/dead-bug/dead-bug-sequence.png` | `exercises/dead-bug.md`, `media/PROVENANCE.md` |
| `media/movements/plank-sequence.png` | `media/exercises/plank/plank-sequence.png` | `exercises/plank.md`, `media/PROVENANCE.md` |
| `media/movements/bird-dog-sequence.png` | `media/exercises/bird-dog/bird-dog-sequence.png` | `exercises/bird-dog.md`, `media/PROVENANCE.md` |
| `media/movements/glute-bridge-sequence.png` | `media/exercises/glute-bridge/glute-bridge-sequence.png` | `exercises/glute-bridge.md`, `media/PROVENANCE.md` |
| `media/movements/hip-hinge-sequence.png` | `media/exercises/hip-hinge/hip-hinge-sequence.png` | `exercises/hip-hinge.md`, `media/PROVENANCE.md` |
| `media/movements/kneeling-hip-flexor-stretch-sequence.png` | `media/exercises/kneeling-hip-flexor-stretch/kneeling-hip-flexor-stretch-sequence.png` | `exercises/kneeling-hip-flexor-stretch.md`, `media/PROVENANCE.md` |

After the moves, `media/equipment/`, `media/movements/`, `media/supplemental/`, and `media/svg/` were removed directly.

## Historical structured-platform disposition

The following superseded structured-platform artifacts were removed from the active tree because M4 also removed their active tests and validation tooling dependencies:

- `content/`
- `schemas/`
- `generated/`
- `tools/validation/`
- content-schema-era tests and fixtures under `tests/`

Historical records that mention those paths remain in governance and change-history documents for traceability. They are not active product paths or active validation tooling.

## Active validation boundary

M4 active stale-path validation scans active project surfaces rather than change-history records:

```bash
rg -n "media/equipment|media/movements|media/supplemental|content/|schemas/|generated/|tools/validation" README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises tests tools media/PROVENANCE.md
```

Expected result: no matches. Exact historical path strings may remain in `docs/changes/`, superseded specs, and historical review records as traceability evidence.
