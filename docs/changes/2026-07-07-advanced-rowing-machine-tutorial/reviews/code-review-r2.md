# Code Review R2: Advanced Rowing Machine Tutorial M1

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/code-review-r2.md`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-resolution.md`, `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`, `docs/plan.md`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/change.yaml`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/code-review-r2.md
- Review log: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md
- Review resolution: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-resolution.md
- Reviewed milestone: M1. Validation and Test Scaffolding
- Milestone closeout: closed
- Remaining implementation milestones: M2, M3, M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: commit `5ad3974` (`Resolve M1 code review findings`) plus existing M1 implementation commits.
- Tracked governing branch state: branch `2026-07-07-advanced-rowing-machine-tutorial`, clean before review recording.
- Governing artifacts: `specs/advanced-rowing-machine-tutorial.md`, `specs/advanced-rowing-machine-tutorial.test.md`, `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`.
- Review-resolution evidence: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-resolution.md`.
- Relevant implementation files: `tools/checks/check_markdown_first.py`, `tests/test_advanced_rowing_machine_tutorial.py`, `tests/fixtures/advanced-rowing-machine-tutorial/README.md`.

## Diff summary

The review-resolution commit adds `ADVANCED_ROWING_FORBIDDEN_MEDIA_TEXT_RE` and wires it into advanced rowing prompt/provenance validation.
It adds temporary-root tests for copied PM5 UI, screenshots, brand marks, identifiable people, correct/wrong badges, red pain marks, elite/race framing, and unsupported promises.

It also extends advanced rowing forbidden-scope checks for calculated personal watts or paces, full benchmark plans, competition programming, active recovery protocols, medical judgment, treatment plans, and injury-specific protocols.
The focused tests now include those previously missing ART-T12 cases.

## Findings

No blocking or required-change findings.

Prior findings:

| Finding | R2 disposition | Evidence |
| --- | --- | --- |
| CR1 | resolved | The checker now rejects excluded media text through `advanced_rowing_media_text_forbidden`, and `test_advanced_prompt_packet_excluded_media_text_fails` covers representative ART-T11 cases. |
| CR2 | resolved | `ADVANCED_ROWING_FORBIDDEN_SCOPE_PATTERNS` now covers the missing scope cases, and `test_advanced_rowing_page_sections_and_forbidden_scope_fail` includes calculated personal watts/paces, full benchmark plan, competition programming, active recovery protocols, and clinical-protocol wording. |

## Checklist coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | pass | CR1/CR2 fixes align with R13, R17, R41, R48, ART-T11, and ART-T12. |
| Test coverage | pass | Focused tests now include representative excluded media semantics and missing forbidden-scope cases. |
| Edge cases | pass | Named CR1 and CR2 edge cases have direct temporary-root test coverage. |
| Error handling | pass | Invalid cases fail through checker findings, not exceptions. |
| Architecture boundaries | pass | Changes remain inside Markdown-first validation and tests. |
| Compatibility | pass | The advanced checks remain scoped to `media/exercises/rowing-machine-advanced/` and `exercises/rowing-machine-advanced.md`; existing focused and full test suites pass. |
| Security/privacy | pass | Identifiable-person media wording is now rejected, and privacy validation passed. |
| Derived artifact currency | pass | Review-resolution, plan, plan index, and change metadata are updated with the M1 re-review state. |
| Unrelated changes | pass | The diff is limited to CR1/CR2 resolution and lifecycle metadata. |
| Validation evidence | pass | Reviewer reran focused tests, full unittest, focused Markdown check, focused privacy check, and whitespace check. |

## No-finding rationale

The R1 false negatives are now covered by explicit checker patterns and targeted temporary-root tests.
The added checks are scoped to the advanced rowing page or advanced rowing media packet surface, preserving unrelated exercise behavior.
The focused and full validation commands passed under reviewer execution.

## Residual risks

Static validation still cannot prove actual generated-image visual semantics, grayscale distinguishability, source adequacy, or reader comprehension.
Those remain assigned to later M3/M4 manual proof surfaces and do not block M1 validation scaffolding closeout.

## Validation evidence

Reviewer-ran commands:

```bash
python3 -m unittest tests.test_advanced_rowing_machine_tutorial
python3 -m unittest discover -s tests
python3 tools/checks/check_markdown_first.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md
python3 tools/checks/check_privacy.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial
git diff --check
```

Results:

- Focused advanced rowing tests: pass, 6 tests.
- Full unittest suite: pass, 230 tests.
- Focused Markdown-first check: pass, checked 4 Markdown file(s).
- Focused privacy check: pass, checked 15 file(s).
- Whitespace check: pass.

## Milestone handoff

- Reviewed milestone: M1. Validation and Test Scaffolding
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining implementation milestones: M2, M3, M4
- Next stage: implement M2. Advanced Rowing Markdown Content
- Final closeout readiness: not-ready; M2-M4 remain unimplemented and later review, explain-change, verify, and PR handoff remain.

## Sources

[local-code-review-r2-spec]: ../../../../specs/advanced-rowing-machine-tutorial.md
[local-code-review-r2-test-spec]: ../../../../specs/advanced-rowing-machine-tutorial.test.md
[local-code-review-r2-plan]: ../../../plans/2026-07-07-advanced-rowing-machine-tutorial.md
[local-code-review-r2-resolution]: ../review-resolution.md
[local-code-review-r2-checker]: ../../../../tools/checks/check_markdown_first.py
[local-code-review-r2-tests]: ../../../../tests/test_advanced_rowing_machine_tutorial.py
