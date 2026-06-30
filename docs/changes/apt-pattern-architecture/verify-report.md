# Verify Report: APT Pattern Architecture

Date: 2026-06-30
Branch: `refine/apt-pattern-architecture`
Scope: workflow-managed final verification after CR-APT-1 resolution

## Result

- Skill: verify
- Status: completed
- Verdict: ready
- Open blockers: none
- Next stage: pr
- Readiness: branch-ready for PR handoff; not PR-body-ready or PR-open-ready
- CI status: not observed; no `.github` workflow files are present locally

## Traceability

| Requirement / proof area | Test IDs | Files changed | Evidence | Status |
| --- | --- | --- | --- | --- |
| Pattern-page architecture: pain point to observable pattern to contributors to exercise options | RB-T21, R57-R63 | `patterns/anterior-pelvic-tilt.md`, `docs/templates/pattern-page.md`, `tests/test_responsible_breadth_m1.py` | `test_apt_pattern_page_follows_reader_journey_architecture`; focused template assertions; Markdown-first checker | pass |
| Existing exercise targets and preview annotations | RB-T21, R61-R62 | APT page, linked `exercises/*.md`, tests | `test_anterior_pelvic_tilt_solution_links_have_real_targets`; `test_pattern_exercise_preview_requires_annotation_and_existing_target` | pass |
| Expanded raster media boundaries and provenance | RB-T22, R29-R35f | `media/PROVENANCE.md`, pattern/exercise media references, checker/tests | media-purpose tests; visual-media proof; Markdown-first checker | pass |
| CR-APT-1 template regression | CR-APT-1 | `docs/templates/pattern-page.md`, `tests/test_responsible_breadth_m1.py`, `review-resolution.md` | focused test requires `../RED-FLAGS.md` and current headings, rejects stale path/headings; code-review R2 clean | pass |
| Review closeout | CR-R1, CR-R2 | `review-log.md`, `review-resolution.md`, review records | `Closeout status: closed`; no `needs-decision`; CR-R2 clean-with-notes | pass |
| Durable rationale | explain-change | `docs/changes/apt-pattern-architecture/explain-change.md` | rationale refreshed after CR-APT-1 and routes to verify | pass |
| Lifecycle state | plan index, plan body, change metadata | `docs/plan.md`, `docs/plans/2026-06-29-responsible-breadth.md`, `change.yaml` | current state synchronized to verified / next stage pr by this report | pass |

## Validation Evidence

Commands were run from the repository root.

| Command | Result | Output summary |
| --- | --- | --- |
| `python3 -m unittest discover -s tests` | pass | Ran 79 tests, OK |
| `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'` | pass | Ran 20 tests, OK |
| `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | pass | Ran 49 tests, OK |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` | pass | checked 18 Markdown files |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises docs/templates docs/changes/apt-pattern-architecture docs/changes/responsible-breadth docs/plans/2026-06-29-responsible-breadth.md docs/plan.md media tools/checks/check_markdown_first.py tests/test_responsible_breadth_m1.py` | pass | checked 84 files |
| `rg -n "about/red-flags.md|\.\./about/red-flags.md|Plain-language overview|What mainstream sources generally agree on|Commonly recommended self-management themes" docs/templates/pattern-page.md tests/test_responsible_breadth_m1.py patterns/anterior-pelvic-tilt.md docs/changes/apt-pattern-architecture` | pass with scoped findings | matches are expected in regression fixtures and historical review/rationale records only; no active `docs/templates/pattern-page.md` or APT page stale usage |
| `rg -n "Current milestone state: follow-up review-closed|Next stage: verify|status: verify-needed|current_stage: verify|\| CR-APT-1 \|" docs/plan.md docs/plans/2026-06-29-responsible-breadth.md docs/changes/apt-pattern-architecture/change.yaml docs/changes/apt-pattern-architecture/review-log.md docs/changes/apt-pattern-architecture/review-resolution.md docs/changes/apt-pattern-architecture/reviews/code-review-r2.md` | pass before final routing update | confirmed pre-verify lifecycle state and CR-APT-1 closure evidence |
| `python3 tools/checks/check_privacy.py docs/changes/apt-pattern-architecture/explain-change.md docs/changes/apt-pattern-architecture/change.yaml docs/plan.md docs/plans/2026-06-29-responsible-breadth.md` | pass | checked 4 files |
| `python3 tools/checks/check_privacy.py docs/changes/apt-pattern-architecture/verify-report.md docs/changes/apt-pattern-architecture/review-resolution.md docs/changes/apt-pattern-architecture/change.yaml docs/plan.md docs/plans/2026-06-29-responsible-breadth.md` | pass | checked 5 files |
| `git diff --check` | pass | no whitespace errors |

## Verification Dimensions

| Dimension | Status | Evidence |
| --- | --- | --- |
| Spec coverage | pass | Changed behavior maps to Responsible Breadth R57-R63, R29-R35f, and CR-APT-1. |
| Requirement satisfaction | pass | Required pattern headings, red-flags path, exercise link behavior, and media-purpose rules have direct test/check evidence. |
| Test coverage | pass | RB-T21/RB-T22 and CR-APT-1 are covered by integration, negative, and focused template assertions. |
| Test validity | pass | The CR-APT-1 focused test failed before the template fix and passed after; negative fixtures cover missing preview data and wrong media purpose. |
| Architecture coherence | pass | Markdown remains canonical; linked exercise pages own exercise details; raster media remains provenance-backed support. |
| Artifact lifecycle state | pass | Review-resolution is closed; code-review R2 is recorded; change metadata and plan surfaces route to `pr` after this verify report. |
| Plan completion | pass | No remaining implementation milestones; APT follow-up review-resolution and explain-change are complete. |
| Validation evidence | pass | Fresh local validation commands are recorded above. |
| Drift detection | pass | Prior stale verify report and missing review-resolution closeout status were updated during verification. |
| Risk closure | pass | CI gap and template-wide checker limitation are recorded; no blocker remains for branch handoff. |
| Release readiness | pass with CI caveat | Branch is locally branch-ready for PR handoff; hosted CI was not observed and no local workflow files exist. |

## Artifact Drift

Resolved during verify:

- Prior verify report was stale and mentioned pre-normalization media paths and pre-CR-APT-1 validation.
- `review-resolution.md` did not explicitly state `Closeout status: closed`.

No remaining blocker was found in the touched lifecycle artifacts.

## CI Status

Hosted CI was not observed. No `.github` workflow files are present in the local
repository, so this report claims local validation only.

## Risks

- AI-generated raster images can contain imperfections. The mitigation remains:
  no in-image text, Markdown and cited sources remain source of truth, media has
  provenance, and images are support assets only.
- Broad Markdown-first checking over all `docs/templates` remains unsuitable
  because unrelated templates contain placeholders and older template debt. The
  CR-APT-1 regression is directly covered by the focused template assertion.
- PR body readiness and PR open readiness are not claimed by this stage.

## Handoff

The APT follow-up is branch-ready for PR handoff based on local verification.
Next stage: `pr`.
