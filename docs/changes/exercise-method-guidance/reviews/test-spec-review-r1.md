# Test Spec Review R1: Exercise Method Guidance

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR-EMG-1, TSR-EMG-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-method-guidance/reviews/test-spec-review-r1.md`
- Review log: `docs/changes/exercise-method-guidance/review-log.md`
- Review resolution: `docs/changes/exercise-method-guidance/review-resolution.md`
- Open blockers: none
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
- Stop condition: none

## Findings

## Finding TSR-EMG-1

- Finding ID: TSR-EMG-1
- Severity: major
- Location: `specs/exercise-method-guidance.test.md`, `Test cases`, `Validation plan`, and command references in EMG-T5 through EMG-T12
- Evidence: The proof map names many commands, for example `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises` at EMG-T5, real-page checker commands at EMG-T6 through EMG-T9, and the final command set at EMG-T12. It also says commands run after each owning milestone in `Testing strategy`. However, the test spec does not classify those commands as existing/configured, planned-for-implementation, manual-only, or release-owned, and it does not name the command owner and owning milestone in a command ledger. The review rule requires planned commands to be classified and to name owner and milestone.
- Required outcome: Add a command/validation ledger that classifies every named command, assigns owner/stage or milestone, names the first milestone where the command is required, and states failure behavior and evidence location.
- Safe resolution path: Add a `Validation commands` or equivalent table to `specs/exercise-method-guidance.test.md` with columns for command ID, command, classification, owner, owning milestone, first required milestone, failure behavior, and evidence artifact. Then reference those command IDs from EMG-T5 through EMG-T12 and the milestone proof map.
- needs-decision rationale: none

## Finding TSR-EMG-2

- Finding ID: TSR-EMG-2
- Severity: major
- Location: `specs/exercise-method-guidance.test.md`, EMG-M1 through EMG-M3 and `Manual QA checklist`
- Evidence: EMG-M1, EMG-M2, and EMG-M3 name manual proof records, steps, expected result, failure proof, and broad automation location. They do not explicitly name automation rationale, required environment, evidence artifact as a separate field, pass condition, failure condition, owning stage, and re-run trigger. The review rule requires manual proof to name a stable ID, automation rationale, exact steps, required environment, evidence artifact, pass condition, failure condition, and owning stage.
- Required outcome: Expand each manual proof case into an auditable manual-proof contract with all required metadata.
- Safe resolution path: Update EMG-M1, EMG-M2, and EMG-M3 to include explicit fields for automation rationale, required environment, evidence artifact, pass condition, failure condition, owning stage, and re-run trigger. Keep the existing proof record paths, but make the pass/fail and ownership criteria precise enough that implementation and code-review can execute them without guessing.
- needs-decision rationale: none

## Review Dimensions

| Dimension | Result | Notes |
| --- | --- | --- |
| Governing-contract alignment | pass | The proof map follows the approved visible-Markdown source-of-truth contract, proof slice, deferred method types, safety boundaries, and no-runtime architecture. |
| Requirement coverage | pass | R1-R42 are mapped to automated test IDs or manual proof IDs. |
| Example coverage | pass | E1-E7 are mapped to stable test or manual proof IDs. |
| Negative and boundary coverage | pass | Missing method sections, inactive method types, hidden-only metadata, adaptive programming, treatment language, source gaps, preview contradictions, and unselected-page compatibility are covered. |
| Proof-level adequacy | concern | The selected proof levels are mostly appropriate, but manual-proof cases lack required metadata. See TSR-EMG-2. |
| Milestone mapping | concern | Test IDs align to plan milestones at a high level, but command ownership and milestone classification are implicit. See TSR-EMG-1. |
| Command validity | concern | Commands are plausible and repository-native, but are not classified with owner, owning milestone, first required milestone, failure behavior, and evidence artifact. See TSR-EMG-1. |
| Fixture and data design | pass | Fixture names and temporary-root allowance are deterministic, local, and privacy-safe. |
| Manual-proof boundary | concern | Manual checks are justified by source-support and comprehension limits, but the cases lack required proof metadata. See TSR-EMG-2. |
| Observability | pass | Stable checker categories and evidence fields are required for automated and manual failures. |
| Determinism and isolation | pass | Automated tests avoid network access, use local files or synthetic fixtures, and reserve public-source checking for manual audit. |
| Scope and non-goals | pass | The proof map avoids personalized programming, medical/rehab behavior, hidden metadata source of truth, valid deferred method types, and broad rollout. |
| Execution economics | pass | Focused tests, real-page checks, smoke validation, and manual proof are separated by risk and milestone. |
| Traceability | pass | Requirement, example, edge-case, test, fixture, and manual proof IDs are linked consistently. |
| Implementation handoff | block | Implementation cannot proceed until TSR-EMG-1 and TSR-EMG-2 are resolved and re-reviewed. |

## Recommendation

Revise `specs/exercise-method-guidance.test.md` to add a command ledger and complete manual-proof metadata, then rerun test-spec-review. No automatic downstream handoff is allowed.
