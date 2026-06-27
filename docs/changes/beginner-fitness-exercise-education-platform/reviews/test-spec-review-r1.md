# Test Spec Review: Content Schema Foundation R1

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR1, TSR2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/beginner-fitness-exercise-education-platform/reviews/test-spec-review-r1.md`
- Review log: `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`
- Review resolution: `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`
- Open blockers: none
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
- Stop condition: none

## Findings

## Finding TSR1

- Finding ID: TSR1
- Severity: major
- Location: `specs/content-schema.test.md:28`, `specs/content-schema.test.md:118`
- Evidence: The test spec lists primary validation commands at lines 28-37 and test cases T1-T16 at lines 118-276, but it does not classify each command as existing/configured, planned for implementation, manual-only, or release-owned; it does not name a command owner; and it does not map test cases or commands to M1-M4 where they first become meaningful. The plan is milestone-based, and this review skill requires planned commands to name an owner and milestone.
- Required outcome: The test spec must add an explicit milestone and command ownership map before implementation handoff. Each validation command must state classification, owner, owning milestone, expected failure behavior, and whether it is allowed to run before the related tool or fixture exists. Each test case or test group must map to M1, M2, M3, or M4.
- Safe resolution path: Add a "Milestone and command ownership" section mapping T1-T2 to M1, T3-T9 to M2, T10-T13 to M3, and T14-T16 to M4 unless the author chooses a different justified mapping. Add a command table for the `unittest`, `validate_content.py`, `privacy_scan.py`, `diff`, and lifecycle `rg` commands with owner `implementation milestone maintainer`, status `planned until implemented`, expected nonzero behavior, and first milestone where the command must pass.
- needs-decision rationale: none

## Finding TSR2

- Finding ID: TSR2
- Severity: major
- Location: `specs/content-schema.test.md:360`
- Evidence: The manual QA checklist at lines 360-366 uses free-form bullets. It does not provide stable manual proof IDs, automation rationale, exact steps, required environment, evidence artifact, pass condition, failure condition, or owning stage. The review skill requires manual proof to be exact, justified, owned, evidenced, and bounded to cases where automation is impractical.
- Required outcome: Manual checks must be converted into explicit manual proof records before implementation handoff.
- Safe resolution path: Replace or supplement the checklist with records such as MP1 lifecycle-state sync, MP2 generated-output source-boundary inspection, MP3 fixture privacy spot-check, MP4 scope/non-goal inspection, and MP5 developer-command documentation check. Each record should include automation rationale, exact steps, required environment, evidence artifact, pass condition, failure condition, and owning stage or milestone.
- needs-decision rationale: none

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| Governing-contract alignment | pass | The proof map follows the approved content schema, repository-native architecture, and reviewed plan without changing scope. |
| Requirement coverage | pass | R1-R40 have mapped tests or migration/manual-oriented checks. |
| Example coverage | pass | E1-E5 and E3a-E3d are represented by stable test IDs. |
| Negative and boundary coverage | pass | Locale, taxonomy, media, safety, lifecycle, review-routing, licensing, privacy, migration, and generated-output failure paths are covered. |
| Proof-level adequacy | pass | Unit, integration, e2e, smoke, contract, migration, and manual levels are generally appropriate for the planned repository-native validator. |
| Milestone mapping | block | TSR1: T1-T16 and validation commands are not explicitly mapped to M1-M4. |
| Command validity | block | TSR1: planned commands are listed, but classification, owner, milestone, and pre-existence behavior are missing. |
| Fixture and data design | pass | Fixture groups are deterministic, local, privacy-safe, and representative. |
| Manual-proof boundary | block | TSR2: manual checks lack stable IDs, evidence artifacts, exact pass/fail conditions, and ownership. |
| Observability | pass | Report fields, audit fields, error identifiers, and privacy-safe output are explicitly tested. |
| Determinism and isolation | pass | Tests avoid network and external services; generated output determinism is covered. |
| Scope and non-goals | pass | The proof map avoids UI, CMS, AI, legal-policy, account, and rehab scope. |
| Execution economics | concern | Coverage is well scoped, but the 60-card performance fixture and e2e generated-output test need milestone ownership per TSR1 to avoid landing too early. |
| Traceability | concern | Requirement, example, and edge-case traceability are strong; milestone traceability is incomplete. |
| Implementation handoff | block | Implementation cannot proceed until TSR1 and TSR2 are resolved and the revised test spec is re-reviewed. |

## Readiness

The test spec is reviewable but not approved. Revise `specs/content-schema.test.md` to resolve TSR1 and TSR2, update `review-resolution.md`, and run a second `test-spec-review` before implementation starts.
