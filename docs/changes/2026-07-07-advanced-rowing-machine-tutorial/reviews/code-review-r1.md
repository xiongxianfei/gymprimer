# Code Review R1: Advanced Rowing Machine Tutorial M1

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/code-review-r1.md`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md`, `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`, `docs/plan.md`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/change.yaml`
- Open blockers: CR1, CR2
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR1, CR2
- Recording status: recorded
- Recording blocker: none
- Review record: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/code-review-r1.md
- Review log: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md
- Review resolution: required
- Reviewed milestone: M1. Validation and Test Scaffolding
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M1 review-resolution, M2, M3, M4
- Required review-resolution: yes
- Finding IDs: CR1, CR2
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: commit `d0ae6b8` (`M1: add advanced rowing validation scaffolding`) against `HEAD~1`.
- Tracked governing branch state: branch `2026-07-07-advanced-rowing-machine-tutorial`, clean before review recording.
- Governing artifacts: `specs/advanced-rowing-machine-tutorial.md`, `specs/advanced-rowing-machine-tutorial.test.md`, `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`.
- Validation evidence: M1 validation notes in the plan and `change.yaml`, plus reviewer-owned temporary negative fixture reproductions.
- Relevant implementation files: `tools/checks/check_markdown_first.py`, `tests/test_advanced_rowing_machine_tutorial.py`, `tests/fixtures/advanced-rowing-machine-tutorial/README.md`.

## Diff summary

M1 adds advanced-rowing-specific Markdown-first checker constants, page-section validation, scoped eight-image exception, prompt packet checks, force-intensity overlay boundaries, and selected forbidden-scope wording checks.
It adds a focused unittest module using temporary repository roots and a narrow passing fixture directory for ART-CMD2.
It also updates workflow metadata to route M1 to code-review.

## Findings

## Finding CR1

- Finding ID: CR1
- Severity: major
- Location: `tools/checks/check_markdown_first.py:848` and `tests/test_advanced_rowing_machine_tutorial.py:335`
- Evidence: ART-T11 requires invalid fixtures to reject screenshots, copied PM5 UI, brand marks, identifiable people, badges, red pain marks, race-win framing, and unsupported promises. The implemented prompt-packet validator checks force-overlay claims and in-image labels, but it does not reject copied UI, logos, identifiable people, screenshots, race framing, or unsupported promises outside the narrow force-overlay regex. A reviewer-owned temporary fixture appended `review_notes: copied PM5 UI with logo and identifiable person` to `media/prompts/exercises/rowing-machine-advanced/monitor-metrics.md`; `python3 tools/checks/check_markdown_first.py` returned `0` and reported `checked 1 Markdown file(s): pass`.
- Required outcome: Advanced rowing media validation must reject the explicitly excluded image semantics that are automatable from alt text, prompt packets, provenance notes, or prompt creation notes.
- Safe resolution path: Add an advanced-rowing media/text forbidden-pattern check covering copied PM5 UI, screenshots, logos or brand marks, identifiable people, correct/wrong badges, red pain marks, elite/race-win framing, and unsupported promises. Add failing temporary-root tests for representative ART-T11 cases, then rerun M1 validation commands.
- needs-decision rationale: none

## Finding CR2

- Finding ID: CR2
- Severity: major
- Location: `tools/checks/check_markdown_first.py:368` and `tests/test_advanced_rowing_machine_tutorial.py:387`
- Evidence: ART-T12 requires invalid fixtures for personal paces, calculated targets, adaptive intervals, full benchmark plans, return-to-rowing guidance, competition programming, and runtime product features. The implemented tests only cover a personalized pace target, race strategy, a tracker, and `advanced_basic_cardio_equipment`. Reviewer-owned temporary fixtures showed that `This page gives competition programming for a 2k race.`, `This page writes a full benchmark plan for the reader.`, and `This page calculates personal watts and paces.` each passed validation with return code `0`.
- Required outcome: Advanced rowing scope validation must reject the named forbidden-scope cases required by ART-T12 and the relevant spec boundaries.
- Safe resolution path: Extend `ADVANCED_ROWING_FORBIDDEN_SCOPE_PATTERNS` or equivalent validation to cover calculated personal targets, personal watts/paces, full benchmark plans, competition programming, active recovery protocols, and other named ART-T12/R48 cases. Add negative tests for the missing cases and rerun M1 validation commands.
- needs-decision rationale: none

## Checklist coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | block | CR1 conflicts with R41 and ART-T11; CR2 conflicts with R13, R17, R48, and ART-T12. |
| Test coverage | block | `tests/test_advanced_rowing_machine_tutorial.py` lacks negative tests for copied UI/logo/identifiable-person semantics and several named forbidden-scope cases. |
| Edge cases | block | Named edge cases in ART-T11 and ART-T12 are not directly proven and reviewer reproductions show false negatives. |
| Error handling | pass | Existing failures return checker findings rather than exceptions for covered invalid states. |
| Architecture boundaries | pass | The checker changes remain scoped to Markdown-first validation and do not add runtime products or new data models. |
| Compatibility | pass | The eight-image exception is path-scoped, and tests cover unrelated pages retaining the default image limit. |
| Security/privacy | concern | CR1 leaves identifiable-person prompt semantics accepted by automated validation, though privacy scan evidence itself passed. |
| Derived artifact currency | pass | Plan, plan index, and change metadata were updated for M1 handoff before review. |
| Unrelated changes | pass | The diff is limited to M1 checker/tests/fixture and workflow handoff metadata. |
| Validation evidence | concern | The recorded commands passed, but the selected tests did not cover all named M1 proof-map cases. |

## No-finding rationale

Not applicable.
This review has material findings.

## Residual risks

Static checks still cannot prove visual semantics, grayscale distinguishability, source adequacy, or reader comprehension.
Those remain assigned to later manual proof IDs in the approved test spec.

## Milestone handoff

- Reviewed milestone: M1. Validation and Test Scaffolding
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining implementation milestones: M1 review-resolution, M2, M3, M4
- Next stage: review-resolution
- Final closeout readiness: not-ready; M1 has unresolved code-review findings and M2-M4 remain unimplemented.

## Sources

[local-code-review-r1-spec]: ../../../../specs/advanced-rowing-machine-tutorial.md
[local-code-review-r1-test-spec]: ../../../../specs/advanced-rowing-machine-tutorial.test.md
[local-code-review-r1-plan]: ../../../plans/2026-07-07-advanced-rowing-machine-tutorial.md
[local-code-review-r1-checker]: ../../../../tools/checks/check_markdown_first.py
[local-code-review-r1-tests]: ../../../../tests/test_advanced_rowing_machine_tutorial.py
