# Review Resolution: APT Pattern Architecture

Closeout status: closed

## Findings

| Finding ID | Source review | Status | Summary |
| --- | --- | --- | --- |
| SR-APT-SPEC-1 | `docs/changes/apt-pattern-architecture/reviews/spec-review-r1.md` | resolved | Generated raster support for pattern and condition visuals lacked a deterministic `media_purpose` compatibility rule with the inherited Markdown-first provenance enum. |
| CR-APT-1 | `docs/changes/apt-pattern-architecture/reviews/code-review-r1.md` | resolved by `docs/changes/apt-pattern-architecture/reviews/code-review-r2.md` | The reusable pattern-page template still uses the old red-flags path and old pattern section headings instead of the current normalized pattern architecture. |

## Spec-review R1 resolution

### SR-APT-SPEC-1 - Generated pattern and condition visuals need media-purpose compatibility

Status: resolved by `docs/changes/apt-pattern-architecture/reviews/spec-review-r2.md`.

Required outcome: revise `specs/responsible-breadth.md` so generated raster
images used by pattern and condition pages have a deterministic provenance
purpose rule before test-spec, planning, or implementation rely on the amended
media requirements.

Resolution:

- Chose Option B because the project direction is to use high-quality generated
  raster images instead of hard-to-understand SVG diagrams for expanded pattern,
  condition, and exercise visuals.
- Updated `specs/responsible-breadth.md` to add expanded-page
  `media_purpose` values:
  `pattern_alignment_illustration`, `anatomical_region_illustration`, and
  `exercise_preview_illustration`.
- Added purpose-specific requirements so generated raster images remain support
  assets and cannot become diagnostic, treatment, safety, anatomy, or movement
  source of truth.
- Added edge cases for wrong media-purpose mapping and diagnosis-implying
  anatomical images.
- Added acceptance coverage requiring deterministic expanded-page media-purpose
  values.

Spec-review R2 approved the amended spec with no material findings. The next
stage is architecture because the new expanded-page media-purpose enum affects
architecture/ADR validation boundaries before test-spec or implementation can
rely on it.

## Code-review R1 resolution

### CR-APT-1 - Pattern template is stale against current pattern architecture

Status: resolved by `docs/changes/apt-pattern-architecture/reviews/code-review-r2.md`.

Required outcome: update `docs/templates/pattern-page.md` so following the
template produces a page with the current Responsible Breadth pattern
architecture and normalized red-flags path.

Safe resolution path:

- Replace the nested `../about/red-flags.md` guidance with the normalized
  `../RED-FLAGS.md` path.
- Replace the old pattern headings with the current architecture headings:
  `Why beginners come to this page`, `Working definition`,
  `How to notice this in yourself`, `The core reason`, and
  `What commonly helps`.
- Keep the existing non-diagnostic, no-prescription, source, and media
  boundaries intact.
- Refresh or add focused template validation so the stale headings and red-flags
  path cannot recur silently.
- Re-run targeted Responsible Breadth tests and Markdown-first checks, then
  request re-review.

Resolution:

- Updated `docs/templates/pattern-page.md` to use `../RED-FLAGS.md`.
- Replaced the old pattern-template headings with the current Responsible
  Breadth pattern architecture headings: `Why beginners come to this page`,
  `Working definition`, `How to notice this in yourself`, `The core reason`,
  and `What commonly helps`.
- Added a focused template assertion in `tests/test_responsible_breadth_m1.py`
  that requires the normalized red-flags path and current headings, and rejects
  the stale path and old headings.
- Preserved `patterns/anterior-pelvic-tilt.md`; the template fix did not expose
  a concrete APT page inconsistency.

Validation:

- `python3 -m unittest tests.test_responsible_breadth_m1.ResponsibleBreadthM2Test.test_responsible_breadth_templates_exist_and_carry_contract`
  - Before the template fix: failed because `../RED-FLAGS.md` was missing.
  - After the template fix: passed.
- `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - Result: passed, 20 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`
  - Result: passed, checked 18 Markdown files.
- `python3 tools/checks/check_privacy.py docs/templates/pattern-page.md tests/test_responsible_breadth_m1.py docs/changes/apt-pattern-architecture/review-resolution.md`
  - Result: passed, checked 3 files.
- `git diff --check`
  - Result: passed.

Validation limitation: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates patterns conditions principles programs exercises` is not a valid closeout command for this narrow fix because unrelated templates still contain placeholders and old template debt. The focused template assertion covers CR-APT-1 directly.

Code-review R2 accepted this resolution with no material findings. The next
stage is explain-change because the reviewed resolution changed the template,
focused test, and review-resolution evidence after the earlier verify report.

## Closeout Checklist

- Final dispositions recorded for all material findings: yes.
- Same-stage re-review exists for blocking or changes-requested outcomes: yes,
  `docs/changes/apt-pattern-architecture/reviews/spec-review-r2.md` closed
  `SR-APT-SPEC-1`, and
  `docs/changes/apt-pattern-architecture/reviews/code-review-r2.md` closed
  `CR-APT-1`.
- `needs-decision` findings remain: no.
- Review log has no open findings: yes.
- Validation evidence is recorded for accepted fixes: yes.
