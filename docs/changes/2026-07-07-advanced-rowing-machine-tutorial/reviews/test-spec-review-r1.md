# Test Spec Review R1: Advanced Rowing Machine Tutorial

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR1
- Recording status: recorded
- Recording blocker: none
- Review record: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/test-spec-review-r1.md
- Review log: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md
- Review resolution: not-required
- Open blockers: TSR1
- Immediate next stage: plan revision
- Implementation handoff: not-allowed
- Stop condition: invalid fixture-directory validation command must be narrowed and re-reviewed. [Plan][local-test-spec-review-r1-plan]

## Findings

## Finding TSR1

- Finding ID: TSR1
- Severity: major
- Location: `specs/advanced-rowing-machine-tutorial.test.md` validation command ART-CMD2 and `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md` M1 validation command
- Evidence: `python3 tools/checks/check_markdown_first.py tests/fixtures media/PROVENANCE.md SOURCES.md RED-FLAGS.md` exits nonzero because `tests/fixtures` contains intentionally invalid global Markdown-first fixtures such as missing source IDs, placeholder URLs, uncited safety lines, external images, and missing sources.
- Required outcome: M1 validation must name a dedicated advanced-rowing fixture path or unittest-owned invalid fixtures so the command's pass/fail result proves this change's behavior rather than unrelated historical invalid fixtures.
- Safe resolution path: Revise the plan and test spec to use a dedicated fixture directory such as `tests/fixtures/advanced-rowing-machine-tutorial` for passing checker commands, keep invalid cases under unittest assertions, rerun plan-review after the substantive plan command change, then rerun test-spec-review.
- needs-decision rationale: none

## Review Dimensions

| Dimension | Verdict | Notes |
| --- | --- | --- |
| Governing-contract alignment | pass | The proof map follows the approved spec and architecture. |
| Requirement coverage | pass | All R1-R50 requirements map to automated or manual proof. |
| Example coverage | pass | E1-E7 are covered. |
| Negative and boundary coverage | pass | Invalid scope, media, label, force-overlay, and compatibility cases are represented. |
| Proof-level adequacy | concern | Proof levels are appropriate, but one command is too broad and fails on unrelated fixtures. |
| Milestone mapping | concern | M1 mapping is conceptually correct but uses an invalid fixture command. |
| Command validity | block | ART-CMD2 and the matching plan command are not valid passing commands because `tests/fixtures` includes intentionally failing fixtures. |
| Fixture and data design | concern | Dedicated valid/invalid fixture placement must be made explicit. |
| Manual-proof boundary | pass | Manual proof IDs are justified and bounded. |
| Observability | pass | Test IDs, command IDs, and evidence paths are stable. |
| Determinism and isolation | concern | ART-CMD2 is deterministic but not isolated to this change. |
| Scope and non-goals | pass | The proof map does not add implementation scope. |
| Execution economics | pass | Focused and release-stage commands are separated. |
| Traceability | pass | Requirement, example, edge-case, milestone, and command links are consistent. |
| Implementation handoff | block | Implementation cannot proceed until TSR1 is resolved and re-reviewed. |

## Sources

[local-test-spec-review-r1-test-spec]: ../../../../specs/advanced-rowing-machine-tutorial.test.md
[local-test-spec-review-r1-plan]: ../../../plans/2026-07-07-advanced-rowing-machine-tutorial.md
[local-test-spec-review-r1-command-evidence]: ../../../../tools/checks/check_markdown_first.py
