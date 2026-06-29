# Test Spec Review R1: Markdown-First Gym Primer

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/test-spec-review-r1.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Open blockers: TSR1
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
- Stop condition: proof-map defect inside the active test spec; implementation must wait for revised test spec and re-review

## Findings

## Finding TSR1

- Finding ID: TSR1
- Severity: major
- Location: `specs/markdown-first-primer.test.md` requirement coverage map and test cases
- Evidence: The test spec maps requirements to T1-T13 and names automation locations, but it does not assign each test, planned command, and manual proof record to an implementation milestone or owner. For example, T1-T13 list coverage and automation locations in `specs/markdown-first-primer.test.md`, while the approved plan sequences M1 active route/docs, M2 check tooling, M3 five-page content/read-test, and M4 mdBook/final gate. The current proof map leaves implementers to infer which tests must be created or activated in each milestone and when commands such as `tools/checks/check_markdown_first.py`, `tools/checks/check_privacy.py`, manual proof records, and `mdbook build` become required evidence.
- Required outcome: The test spec must explicitly map T1-T13, planned validation commands, and manual proof records to M1-M4, including which milestone owns implementation, first meaningful execution, and closeout evidence for each proof. Planned commands must be classified as existing, planned-for-milestone, manual-only, or conditional/external, with the owning milestone named.
- Safe resolution path: Revise `specs/markdown-first-primer.test.md` by adding a milestone/proof ownership section or equivalent per-test fields. A safe mapping would put contributor/docs/template/legacy contract checks in M1, checker CLI and fixture tests in M2, real first-slice page integration plus beginner proof in M3, and mdBook build-or-deferral plus final local quality gate in M4. Re-run test-spec structural and coverage scans, then request `test-spec-review` R2.
- needs-decision rationale: none

## Review Dimensions

| Dimension | Verdict | Notes |
| --- | --- | --- |
| Governing-contract alignment | pass | The proof map follows the approved Markdown-first spec, architecture, and plan boundaries without adding hosted app, CMS, AI, formal expert-review, generated JSON product, or broad content scope. |
| Requirement coverage | pass | R1-R40 all map to T1-T13, with manual proof where semantic review or beginner comprehension cannot be automated. |
| Example coverage | pass | E1-E5 map to stable tests and manual proof where appropriate. |
| Negative and boundary coverage | pass | The proof map covers global-only safety citation failure, missing page-local sources, excluded scope, full Chinese translation, third-party media, privacy failures, old generated JSON conflicts, and mdBook source-of-truth drift. |
| Proof-level adequacy | pass | Unit, integration, smoke, contract, migration, and manual levels are appropriate to the risks. |
| Milestone mapping | block | TSR1: tests and commands are not explicitly assigned to M1-M4 ownership and activation points. |
| Command validity | concern | Commands are plausible and many are planned for future implementation, but command classification and milestone ownership are incomplete under TSR1. |
| Fixture and data design | pass | Planned fixtures are deterministic repository files, temporary-test friendly, and privacy-safe. |
| Manual-proof boundary | pass | Manual proof is limited to render inspection, semantic citation review, beginner comprehension, and mdBook build-or-deferral evidence. |
| Observability | pass | The test spec requires failures to identify file path, rule/check name, failing section/source/media/scope/privacy category, and pass/fail/error status. |
| Determinism and isolation | pass | Unit fixtures avoid network calls; link health is manual or optional-tool evidence; mdBook success cannot be mocked. |
| Scope and non-goals | pass | The proof map explicitly excludes hosted site, CMS, AI, formal reviewer lifecycle, broad translation, external media workflows, clinical flows, and unobserved CI claims. |
| Execution economics | pass | The proof map separates focused unit checks from integration, manual semantic review, optional mdBook, and network-dependent link checking. |
| Traceability | concern | Requirement, example, edge-case, and test IDs are linked; milestone traceability is the missing part captured by TSR1. |
| Implementation handoff | block | Implementation would require guessing when each proof becomes mandatory, so handoff is not allowed until TSR1 is resolved and re-reviewed. |

## Recommendation

Request a focused test-spec revision for TSR1. Do not start implementation until the revised proof map passes test-spec-review.
