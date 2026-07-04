# Learn Session: Test Spec Skill Proof Contracts

## Frame

- Trigger: explicit `$learn` maintainer request after exercise-method-guidance test-spec review and revision.
- Trigger type: maintainer request plus review finding observation.
- Scope: best practices for improving the `test-spec` skill so future test specs get validation ownership and manual proof contracts right the first time.
- Session record path: `docs/learn/sessions/2026-07-04-test-spec-skill-proof-contracts.md`
- Evidence in scope:
  - `docs/changes/exercise-method-guidance/reviews/test-spec-review-r1.md`
  - `docs/changes/exercise-method-guidance/review-resolution.md`
  - `specs/exercise-method-guidance.test.md`
  - `.agents/skills/test-spec/SKILL.md`
  - `.agents/skills/test-spec/assets/test-spec-skeleton.md`
- Explicit exclusions:
  - This session does not edit the `test-spec` skill.
  - This session does not make new workflow policy authoritative.
  - This session does not claim exercise-method-guidance implementation readiness.
  - This session does not update `docs/learn/topics/` because the evidence is a focused skill-improvement direction, not an accumulated durable lesson.
- Prior learnings reviewed:
  - `docs/learn/topics/content-quality.md`
  - `docs/learn/topics/architecture.md`
  - `docs/learn/sessions/2026-06-30-review-finding-summary-titles.md`

## Observe

| Observation ID | Observation | Evidence | Best practice for `test-spec` improvement |
| --- | --- | --- | --- |
| OBS-001 | Named validation commands need an explicit command ledger before test-spec-review. | `TSR-EMG-1` found that commands named in EMG-T5 through EMG-T12 were not classified with owner, milestone, first required milestone, failure behavior, and evidence artifact. The revision added command IDs EMG-CMD1 through EMG-CMD14. | When a test spec names validation commands, require a `Validation commands` table with command ID, command, classification, owner, owning milestone, first required milestone, failure behavior, and evidence artifact. Test cases and proof maps should reference command IDs rather than relying only on raw command strings. |
| OBS-002 | Manual proof cases need a complete audit contract, not only steps and expected results. | `TSR-EMG-2` found that EMG-M1 through EMG-M3 lacked automation rationale, required environment, evidence artifact, pass condition, failure condition, owning stage, and re-run trigger. The revision added those fields. | The `test-spec` skill should require every manual proof ID to include automation rationale, exact steps, required environment, evidence artifact, pass condition, failure condition, owning stage, and re-run trigger. |
| OBS-003 | Milestone proof maps should tie tests, manual proofs, command IDs, and evidence artifacts together. | The review resolution says the revised test spec added a milestone proof map for M1, M2, M3, M4, and Lifecycle Closeout that links test/proof IDs, command IDs, and evidence artifacts. | Test specs for milestone-based work should include a milestone proof map when validation is staged across milestones, so implementation and code-review can execute without inferring ownership or timing. |
| OBS-004 | The current `test-spec` skill and skeleton mention commands and manual QA broadly but do not require the fields that review needed. | `.agents/skills/test-spec/SKILL.md` requires manual QA and fixtures/commands in expected output. `.agents/skills/test-spec/assets/test-spec-skeleton.md` has no validation-command ledger section or manual-proof metadata template. | The skill and skeleton should be amended together so authors start from the same proof contract that reviewers enforce. |

## Classify

| Observation ID | Proposed primary classification | Final primary classification | Secondary routes | Confirmed by | Rationale |
| --- | --- | --- | --- | --- | --- |
| OBS-001 | process-follow-up | process-follow-up | future `test-spec` skill/template update | Maintainer request in chat plus `TSR-EMG-1` | This is a concrete process gap in the test-spec authoring surface. It should be routed to the owning skill/template, not encoded as a learn-topic policy. |
| OBS-002 | process-follow-up | process-follow-up | future `test-spec` skill/template update | Maintainer request in chat plus `TSR-EMG-2` | The manual-proof fields are reusable for future test specs, but the authoritative change belongs in the skill assets. |
| OBS-003 | process-follow-up | process-follow-up | future `test-spec` skill/template update | Maintainer request in chat plus review-resolution evidence | The milestone proof map is a best-practice addition for staged implementation plans and should be captured in the authoring template. |
| OBS-004 | process-follow-up | process-follow-up | future `test-spec` skill/template update | Maintainer request in chat and direct skill/skeleton inspection | The current skill surface is missing the exact structures that avoided re-review findings after revision. |

## Route

- Topic updates: none.
- Durable lesson captured: no. The evidence is focused and sufficient for a process follow-up, but not yet accumulated enough to create durable topic guidance.
- Follow-up created: `docs/follow-ups.md`, "Improve test-spec skill proof-contract authoring".
- Recommended owner surface: `.agents/skills/test-spec/SKILL.md` and `.agents/skills/test-spec/assets/test-spec-skeleton.md`.

## Best Practices

For a future `test-spec` skill improvement, update the skill and skeleton so authors must do the following before test-spec-review:

1. Add a validation-command ledger whenever the test spec names commands.
2. Assign every command a stable command ID and reference those IDs from test cases, milestone maps, and readiness evidence.
3. Classify each command as existing/configured, planned-for-implementation, manual-only, release-owned, or another explicit local category.
4. Record command owner, owning milestone, first required milestone, failure behavior, and evidence artifact.
5. Treat every manual proof as an auditable contract with automation rationale, exact steps, required environment, evidence artifact, pass condition, failure condition, owning stage, and re-run trigger.
6. Add a milestone proof map for staged work so each milestone names its required tests, manual proofs, command IDs, and evidence artifacts.
7. Keep the skill instructions and skeleton assets aligned, because reviewers enforce the artifact shape that authors start from.

## Outcome

- Result: process follow-up recorded.
- No topic file update was made.
- No `test-spec` skill behavior was changed in this session.
- Next recommended action: run a dedicated skill-maintenance update for `test-spec`, then review the updated skill and skeleton against `test-spec-review` expectations.
