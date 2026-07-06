# Spec Review R1: Brisk Walking and Everyday Walking Guidance

## Result

- Skill: spec-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r1.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Immediate next stage: architecture
- Eventual test-spec readiness: conditionally-ready; ready after architecture assessment records whether the walking content contract requires architecture updates or no architecture changes, then planning and plan review are complete
- Stop condition: none

`Immediate next stage` is the routing field; allowed values exclude `test-spec`.
Use `Eventual test-spec readiness` to assess whether test-spec authoring will
be possible after required routing stages.

## Automated Review Invocation Manifest

- Invocation mode: workflow-managed automated review
- User request: `$workflow auto: test-spec-review`
- Profile: `bounded-review-fix`
- Review target: `specs/brisk-walking-and-everyday-walking.md`
- Governing artifacts: `CONSTITUTION.md`, `VISION.md`, `docs/workflows.md`, accepted proposal, related method, Markdown-first, muscle-guidance, and exercise-image specs
- Excluded context: author hidden reasoning, desired review outcome, implementation notes, and validation-result summaries beyond recorded lifecycle facts
- Manifest status: recorded inside this review record

## Findings

None.

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | pass | BWG-R1 through BWG-R30 define the two page paths, required page roles, `basic_cardio_activity`, source support, safety routing, image behavior, validation expectations, and beginner proof. |
| normative language | pass | The spec uses testable `MUST`, `MUST NOT`, `SHOULD`, and `MAY` language for observable Markdown content, source review, validation, media, safety, and privacy behavior. |
| completeness | pass | The spec covers the exercise page, principle page, method type, intensity checks, method guidance, role-based muscle guidance, technique, stop rules, source indexing, optional media, rollout boundaries, rollback, privacy, accessibility, and edge cases. |
| testability | pass | Required headings, visible method type, page-local sources, source-index reuse, red-flag routing, deterministic forbidden wording, image constraints, and privacy are automatable or structurally reviewable; semantic source support and beginner comprehension are assigned to manual proof. |
| examples | pass | Examples E1-E5 cover brisk walking, everyday walking, method type, source support, and optional image behavior. |
| compatibility | pass | The change is additive, does not require broad migration, and keeps `basic_cardio_activity` distinct from deferred `basic_cardio_equipment` and `loaded_carry` activation. |
| observability | pass | The spec names file-level validation outputs, manual source-audit evidence, beginner read-test evidence, visual-safety evidence when needed, and exact-command reporting constraints. |
| security/privacy | pass | The spec introduces no user input, tracker, account, database, wearable integration, or private health data and bars private data in pages, prompts, provenance, review records, and proof notes. |
| non-goals | pass | Non-goals preserve GymPrimer boundaries against personalized plans, weight-loss prescriptions, calories, step mandates, heart-rate zones, medical programs, rehab, running, hiking, rucking, treadmill protocols, trackers, and generated source-of-truth content. |
| acceptance criteria | pass | AC1 through AC10 are observable and correctly gate Option C, page contracts, method-contract behavior, source obligations, safety boundaries, image-optional behavior, validation planning, and implementation blocking. |

## Routing Assessment

The spec affects the visible exercise-page content contract, a new method type, validation behavior, source-support review, optional media provenance, and manual proof. Under `CONSTITUTION.md`, architecture assessment is required before planning or implementation because the change touches content contracts, validation tooling, and source-of-truth boundaries.

The approved immediate routing is `architecture`. The architecture stage should record whether a canonical architecture update is required for `basic_cardio_activity`, checker behavior, optional media, and manual proof, or whether the approved spec is sufficient without architecture changes.

## Recommended Spec Edits

No blocking edits.

Lifecycle cleanup performed for downstream reliance:

- `specs/brisk-walking-and-everyday-walking.md` status was normalized from `draft` to `approved`.
- `Follow-on artifacts` now points to this review record.

## Recommendation

Approve the spec for downstream architecture assessment. In the active workflow-managed `auto: test-spec-review` request, continue to recorded architecture assessment before planning or test-spec authoring.
