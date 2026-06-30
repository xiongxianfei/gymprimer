# Verify Report: APT Pattern Architecture

Date: 2026-06-29
Branch: `refine/apt-pattern-architecture`
Scope: direct follow-up verification for PR handoff

## Result

- Status: pass
- Open blockers: none
- Next stage: pull request
- CI status: not observed

## Traceability

| Area | Files / evidence | Status |
| --- | --- | --- |
| APT page reader journey | `patterns/anterior-pelvic-tilt.md` | pass |
| Reusable pattern architecture | `docs/templates/pattern-page.md` | pass |
| Linked exercise pages | `exercises/dead-bug.md`, `exercises/plank.md`, `exercises/bird-dog.md`, `exercises/glute-bridge.md`, `exercises/hip-hinge.md`, `exercises/kneeling-hip-flexor-stretch.md` | pass |
| Raster image replacement | `media/movements/*.png`, `media/PROVENANCE.md` | pass |
| Link regression | `tests/test_responsible_breadth_m1.py` | pass |
| Durable rationale | `docs/changes/apt-pattern-architecture/explain-change.md` | pass |
| Manual proof | `docs/changes/apt-pattern-architecture/manual-proof/` | pass |

## Validation Evidence

- `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - Result: pass
  - Output summary: 16 tests OK
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - Result: pass
  - Output summary: 51 tests OK
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md about patterns conditions principles programs exercises`
  - Result: pass
  - Output summary: checked 13 Markdown files
- `python3 tools/checks/check_privacy.py README.md SOURCES.md about patterns conditions principles programs exercises docs/templates docs/changes/apt-pattern-architecture docs/changes/responsible-breadth docs/learn media`
  - Result: pass
  - Output summary: checked 77 files
- `git diff --check`
  - Result: pass

## Media Review

The generated raster images were visually inspected locally. Each referenced PNG exists under `media/movements/`, has Markdown alt text, and has an approved provenance row in `media/PROVENANCE.md`.

## Risks

- AI-generated exercise images can still contain anatomical imperfections. Mitigation: no in-image text, no source-of-truth claims in the images, Markdown remains canonical, and future reviewer feedback can replace individual assets.
- CI was not observed; only local validation is claimed.
