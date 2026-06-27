# Learn Session: Project Map Next Stage Correction

## Frame

- Trigger: contributor observation that the project-map invocation reported `Next stage: architecture` when it should have reported `proposal`.
- Trigger type: contributor observation and explicit learn invocation.
- Scope: `docs/project-map.md` downstream recommendation and the evidence used to classify the next stage.
- Evidence in scope: `docs/project-map.md`, `CONSTITUTION.md`, `AGENTS.md`, user correction in chat.
- Explicit exclusions: no architecture design review, no workflow policy change, no topic-file durable lesson, no CI or implementation validation.
- Prior learnings reviewed: none observed; no `docs/learn/` records existed before this session.
- Session record path: `docs/learn/sessions/2026-06-26-project-map-next-stage.md`

## Observe

- OBS-001: The project map recorded no source tree, specs, architecture docs, schema, tests, package config, CI, deployment config, or release process. It also listed open questions about implementation stack, content storage, locale-aware card schema, validation tooling, ownership, and README status. That evidence indicates unresolved direction and scope, not readiness for architecture.
- OBS-002: `CONSTITUTION.md` says the standard workflow creates or updates a proposal when direction or scope needs a decision, then creates or updates a spec for observable requirements, then creates architecture for cross-component or hard-to-reverse decisions.
- OBS-003: The prior project-map response reported `Next stage: architecture`, which skipped the proposal decision point implied by the map's own open questions.

## Classify

| Observation | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
| --- | --- | --- | --- | --- | --- |
| OBS-001 to OBS-003 | artifact-update | artifact-update | update `docs/project-map.md` downstream recommendation | User correction: "it should be proposal" | The affected output was the map's downstream recommendation. This is a concrete artifact correction, not a broad workflow-policy lesson. |

## Route

- Updated `docs/project-map.md` with a `Downstream recommendation` section setting `Next stage: proposal`.
- No topic file was created. A single routing mistake does not establish a durable lesson or reusable policy beyond the corrected artifact.
- No proposal was opened by this learn session. The corrected map now routes future direction work to proposal.

## No Durable Lesson Rationale

This session captured one confirmed routing correction. It does not show repeated review findings, recurring incidents, failed validation patterns, or accepted authoritative policy changes. The durable record is the session plus the corrected project-map recommendation.

## Validation

- Edited files were reviewed by direct inspection after update.
