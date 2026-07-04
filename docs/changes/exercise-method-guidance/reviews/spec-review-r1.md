# Spec Review R1: Exercise Method Guidance

## Result

- Skill: spec-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-method-guidance/reviews/spec-review-r1.md`
- Review log: `docs/changes/exercise-method-guidance/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Immediate next stage: architecture
- Eventual test-spec readiness: conditionally-ready; ready after the architecture stage records whether the visible-Markdown method contract and validation changes require architecture updates or no architecture changes
- Stop condition: none

`Immediate next stage` is the routing field; allowed values exclude `test-spec`.
Use `Eventual test-spec readiness` to assess whether test-spec authoring will
be possible after required routing stages.

## Findings

None.

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | pass | Requirements R1-R42 define the section heading, visible method-type line, active enum, first proof slice, source rules, forbidden behavior, compatibility, and validation expectations. |
| normative language | pass | `MUST`, `MUST NOT`, `SHOULD`, and `MAY` are used for observable content, validation, and review contracts rather than hidden implementation choices. |
| completeness | pass | The spec covers normal flow, proof-slice pages, deferred method types, pattern-preview alignment, source support, migration, rollback, security/privacy, accessibility, and edge cases. |
| testability | pass | Section presence, method type enum, hidden-only metadata rejection, forbidden language, proof-slice coverage, and required labels are automatable; source adequacy and beginner comprehension are assigned to manual proof. |
| examples | pass | Examples E1-E7 cover dynamic resistance, stretching, visible source of truth, pattern alignment, adaptive-programming rejection, proof-slice coverage, and principle-page linkage. |
| compatibility | pass | The spec is additive, preserves prior exercise-page sections, avoids retroactive v0.1 adoption before selected implementation slices, and scopes compatibility notes to related specs. |
| observability | pass | Automated findings and manual validation records are named, including stable file-level failures and residual-risk recording for semantic proof gaps. |
| security/privacy | pass | The spec introduces no user input, accounts, analytics, private health data, or runtime storage, and it forbids inviting readers to submit sensitive personal training or health details. |
| non-goals | pass | The non-goals preserve GymPrimer's boundary against personalized plans, adaptive programming, diagnosis, treatment, rehab, advanced performance programming, and hidden metadata as source of truth. |
| acceptance criteria | pass | AC1-AC10 are observable enough for review, planning, architecture assessment, validation planning, and scope-boundary checks. |

## Routing Assessment

The spec itself avoids hidden metadata, generated indexes, shared taxonomy files,
runtime APIs, and databases. However, the change still affects Markdown content
contracts, validation tooling, template behavior, and cross-page pattern-preview
alignment. Under `CONSTITUTION.md`, architecture assessment should occur before
planning or implementation when validation tooling or source-of-truth boundaries
are affected.

Therefore, the approved routing is `architecture`. The architecture stage can
record either that no architecture changes are required beyond the visible
Markdown contract, or that architecture/ADR updates are needed for validation
tooling and cross-page contract boundaries.

## Recommended Spec Edits

No blocking edits.

Non-blocking cleanup: after this review is accepted for downstream reliance,
normalize `specs/exercise-method-guidance.md` from `draft` to `approved` and
consider updating `Next artifacts` so it names architecture assessment as the
next recorded lifecycle stage for this change.

## Recommendation

Approve the spec for downstream architecture assessment. No automatic downstream
handoff is performed by this direct review request.
