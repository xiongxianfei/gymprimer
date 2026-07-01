# Code Review M2 R2: Exercise Source-Support Re-review

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/forward-head-posture-pattern-architecture/reviews/code-review-m2-r2.md`, `docs/changes/forward-head-posture-pattern-architecture/review-log.md`, `docs/changes/forward-head-posture-pattern-architecture/review-resolution.md`, `docs/changes/forward-head-posture-pattern-architecture/change.yaml`, `docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-FHP-M2-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/forward-head-posture-pattern-architecture/reviews/code-review-m2-r2.md`
- Review log: `docs/changes/forward-head-posture-pattern-architecture/review-log.md`
- Review resolution: `docs/changes/forward-head-posture-pattern-architecture/review-resolution.md`
- Reviewed milestone: M2
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M2 resolution, M3, M4
- Required review-resolution: yes
- Finding IDs: CR-FHP-M2-1
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `62d087e` (`M2: resolve exercise source support`), especially the five exercise-page citation changes, `SOURCES.md`, `review-resolution.md`, and M2 lifecycle artifacts.
- Tracked governing branch state: approved forward-head spec, approved test spec, M2 plan state, M2 R1 review record, and CR-FHP-M2-1 review-resolution evidence are tracked in the branch.
- Governing artifacts: `specs/forward-head-posture-pattern-architecture.md` R15-R17 and AC8-AC9; `specs/forward-head-posture-pattern-architecture.test.md` FHP-T7, FHP-T8, and FHP-RO2; `docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md` M2.
- Validation evidence inspected or run: M2 validation ledger in `change.yaml` and the active plan; reviewer reran `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises`, `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`, and `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`.
- Prior finding reconciled: CR-FHP-M2-1 is failed-remediation. The pages no longer rely on the broad ACE exercise-library landing page, but sampled setup and technique claims still cite sources that do not directly support the cited details.

## Diff Summary

The remediation replaces broad source uses with page-local source IDs for the
five same-slice exercise pages, removes the unused ACE exercise-library entry
from `SOURCES.md`, adds an FHP-RO2 evidence table, and routes M2 back to
code-review re-review. The replacement sources are stronger for several muscle
or exercise-identity claims, especially wall-slide serratus anterior activity,
prone arm-raise trapezius activity, and band pull-apart shoulder-girdle muscle
activity.

## Findings

### Finding CR-FHP-M2-1

- Finding ID: CR-FHP-M2-1
- Severity: major
- Location: `exercises/chin-nod.md:29`, `exercises/chin-nod.md:33`, `exercises/thoracic-extension.md:19`, `exercises/wall-slide.md:19`, `exercises/wall-slide.md:29`, `exercises/wall-slide.md:33`, `exercises/prone-y-t.md:29`, `exercises/band-pull-apart.md:19`
- Evidence: R17 and FHP-RO2 require sampled setup, technique, muscle, feel-cue, common-mistake, and safety claims to have suitable page-local support. The remediation cites better sources for several muscle/activity claims, but still attaches research or inaccessible instruction sources to specific beginner setup and technique details they do not directly show. For example, the wall-slide PubMed abstract supports serratus anterior activation during wall slides, but it does not support the page's specific setup details about standing a short step from the wall, keeping the back of the head near the wall, placing forearms or backs of hands near the wall, or using ribs/neck control as the range limiter. The chin-nod PMC source supports deep cervical flexor and craniocervical-flexion training, but the sampled page text extends that support to wall setup and "back of the neck long" technique language. The prone Y/T PubMed abstract supports prone overhead arm raise and trapezius EMG claims, but does not directly support the T-shape/thumbs-up setup wording. The thoracic-extension source URL returned a JavaScript/cookie gate in this review environment, so FHP-RO2 could not compare the cited setup and technique claims to the source text.
- Required outcome: CR-FHP-M2-1 needs a second source-support resolution pass. Each exercise page should cite direct exercise-instruction sources for exact setup and technique details, reserve EMG or anatomy studies for muscle/activity claims, and soften or remove any setup, technique, feel-cue, or common-mistake wording that cannot be matched to a page-local source.
- Safe resolution path: Keep the current stronger sources where they directly support muscle/activity claims. For exact technique claims, add page-local exercise-instruction sources that visibly describe the movement, or rewrite the claims as conservative general cues backed by Mayo/ACSM-style technique sources. Replace or avoid the JS-gated thoracic-extension source unless it can be inspected reliably. Then rerun the M2 validation commands and request M2 code-review R3 with updated FHP-RO2 evidence.
- needs-decision rationale: none

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | concern | R15-R16 page existence and structure remain satisfied, but R17/AC9/FHP-RO2 are still not satisfied for sampled setup and technique claims. |
| Test coverage | concern | Structural tests and checker commands pass, but the approved proof map explicitly assigns semantic source support to code review; that review-only proof still fails. |
| Edge cases | concern | EC4 missing source sections are covered structurally; the remaining edge is semantic source support, which static checks cannot prove. |
| Error handling | pass | No runtime or parser behavior changed; checker commands still produce stable pass/fail outcomes. |
| Architecture boundaries | pass | The diff stays in static Markdown, page-local citations, `SOURCES.md`, and change-local lifecycle artifacts; no runtime app, diagnosis flow, generated output authority, or media source-of-truth change is introduced. |
| Compatibility | pass | The ACE global source entry was removed only after its citations were removed from the reviewed pages; local source IDs remain page-local. |
| Security/privacy | pass | No secrets, private health data, symptom intake, or user-specific information were introduced. |
| Derived artifact currency | pass | No derived artifacts are introduced or relied on. |
| Unrelated changes | pass | The diff is scoped to the five exercise pages, source-index cleanup, and M2 review-resolution/routing records. |
| Validation evidence | concern | Targeted commands pass, but they cannot validate the semantic source-support issue that remains open under FHP-RO2. |

## No-Finding Rationale

Not applicable; CR-FHP-M2-1 remains open as a failed remediation.

## Direct-Proof Gaps

- FHP-RO2 still lacks direct source proof for several sampled setup and technique claims. The current evidence is sufficient for selected muscle/activity claims, but not for the full R17 claim set.

## Milestone Handoff State

- Reviewed milestone: M2
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M2 resolution, M3, M4
- Next stage: review-resolution
- Final closeout readiness: not ready because M2 has an unresolved material finding and M3-M4 remain open.
