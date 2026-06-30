# Code Review R1: APT Pattern Architecture

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/apt-pattern-architecture/reviews/code-review-r1.md`, `docs/changes/apt-pattern-architecture/review-log.md`, `docs/changes/apt-pattern-architecture/review-resolution.md`, `docs/changes/apt-pattern-architecture/change.yaml`, `docs/plan.md`, `docs/plans/2026-06-29-responsible-breadth.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-APT-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/apt-pattern-architecture/reviews/code-review-r1.md`
- Review log: `docs/changes/apt-pattern-architecture/review-log.md`
- Review resolution: `docs/changes/apt-pattern-architecture/review-resolution.md`
- Reviewed milestone: APT follow-up implementation for RB-T21/RB-T22
- Milestone closeout: resolution-needed
- Remaining implementation milestones: APT follow-up review resolution
- Required review-resolution: yes
- Finding IDs: CR-APT-1
- Verify readiness: not-claimed

## Review Surface

- Branch: `refine/apt-pattern-architecture`
- Scoped commits inspected:
  - `d85c308 feat: refine anterior pelvic tilt pattern`
  - `1608592 APT: implement pattern architecture proof`
  - `1905b25 APT: remove duplicate preview images`
- Current files inspected:
  - `patterns/anterior-pelvic-tilt.md`
  - `docs/templates/pattern-page.md`
  - `tools/checks/check_markdown_first.py`
  - `tests/test_responsible_breadth_m1.py`
  - `media/PROVENANCE.md`
  - `docs/changes/apt-pattern-architecture/manual-proof/pattern-source-scope.md`
  - `docs/changes/apt-pattern-architecture/manual-proof/visual-media-review.md`
  - linked exercise pages under `exercises/`
- Governing artifacts inspected:
  - `CONSTITUTION.md`
  - `VISION.md`
  - `specs/responsible-breadth.md`
  - `specs/responsible-breadth.test.md`
  - `docs/plans/2026-06-29-responsible-breadth.md`
  - `docs/changes/apt-pattern-architecture/change.yaml`

## Validation Evidence

- `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
  - Result: pass
  - Output summary: Ran 20 tests, OK
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`
  - Result: pass
  - Output summary: checked 18 Markdown files
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises docs/templates docs/changes/apt-pattern-architecture docs/changes/responsible-breadth docs/plans/2026-06-29-responsible-breadth.md docs/plan.md media tools/checks/check_markdown_first.py tests/test_responsible_breadth_m1.py`
  - Result: pass
  - Output summary: checked 82 files
- `git diff --check c2e0dc7..HEAD`
  - Result: pass

CI was not observed.

## Finding CR-APT-1

- Finding ID: CR-APT-1
- Severity: major
- Location: `docs/templates/pattern-page.md:22`
- Evidence: The reusable pattern template still directs authors to link `../about/red-flags.md` and uses the older `Plain-language overview`, `What mainstream sources generally agree on`, and `Commonly recommended self-management themes` headings. The amended Responsible Breadth contract requires the pattern-page architecture headings `Why beginners come to this page`, `Working definition`, `How to notice this in yourself`, `The core reason`, and `What commonly helps` in R57-R61. The current checker enforces `RED-FLAGS.md` after layout normalization and validates pattern architecture against `What commonly helps`.
- Required outcome: Update the pattern-page template so a contributor following it produces a page that satisfies the current Responsible Breadth pattern architecture and normalized red-flags path.
- Safe resolution path: Revise only `docs/templates/pattern-page.md` and any directly affected template tests or validation notes. Preserve the APT page content unless the template fix exposes a concrete page inconsistency. Re-run the targeted Responsible Breadth tests and Markdown-first checker over templates or add a focused template assertion if the existing validation surface does not cover the corrected template.
- needs-decision rationale: none

## Checklist

| Area | Result | Evidence |
| --- | --- | --- |
| Spec alignment | concern | APT page follows R57-R61, but the reusable template does not. |
| Test coverage | concern | RB-T21/RB-T22 tests cover the real page and checker failures, but do not catch the stale pattern template contract. |
| Edge cases | pass | Missing exercise target, missing preview annotations, wrong pattern media purpose, and condition anatomy diagnosis text are covered. |
| Error handling | pass | Checker emits stable RB004/RB007/media finding codes for invalid states. |
| Architecture boundaries | pass | Pattern page remains Markdown source, linked exercises are separate pages, and raster media has provenance. |
| Compatibility | concern | Template references the removed nested red-flags path and old pattern section names. |
| Security/privacy | pass | Privacy scan passed over reviewed surfaces; no secrets or private health details observed. |
| Derived artifact currency | pass | No generated canonical artifacts are introduced; media provenance rows match current referenced raster assets. |
| Unrelated changes | concern | The branch contains later repository-layout commits, so this review scoped only the APT follow-up commits and current APT surfaces. |
| Validation evidence | pass | Targeted local commands passed; CI was not observed. |

## Handoff

Review-resolution is required for CR-APT-1. Do not resume PR handoff for the APT follow-up until the template contract is corrected, validation is refreshed, and the finding is re-reviewed or otherwise closed.
