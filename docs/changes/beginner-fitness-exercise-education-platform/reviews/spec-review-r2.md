# Spec Review: Content Schema and Review Contract R2

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: SR4
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/beginner-fitness-exercise-education-platform/reviews/spec-review-r2.md`
- Review log: `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`
- Review resolution: `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`
- Open blockers: SR4
- Immediate next stage: spec revision
- Eventual test-spec readiness: not-ready
- Stop condition: locale key requirements conflict with the controlled locale enum, so validators and fixtures would have to guess whether English content uses `en` or `en-US`

## Findings

## Finding SR4

- Finding ID: SR4
- Severity: major
- Location: `specs/content-schema.md` glossary, examples E1-E2, requirements R2-R3, minimum v1 controlled enums, and AC25
- Evidence: The glossary says a locale key may be `en` or `zh-Hans`; E1 requires `en` locale fields; E2 starts from an approved English card with locale key `en`; R2 requires every publishable exercise card to have an English locale branch keyed as `en`; and R3 says additional locales use the same field structure as `en`. The controlled enum later defines v1 locale keys as only `en-US` and `zh-Hans`, and AC25 validates `locale = en-US` and `locale = zh-Hans`. Because AC23 rejects unknown locale values, `en` is simultaneously required by R2 and rejected by the enum contract.
- Required outcome: The spec must use one normative English locale key consistently across glossary, examples, requirements, enums, acceptance criteria, validation behavior, and migration notes.
- Safe resolution path: Replace `en` with `en-US` in the glossary examples, E1, E2, R2, and R3, or explicitly add `en` to the controlled locale enum with clear semantics and compatibility behavior. The safer path for the current BCP-47 v1 contract is to standardize on `en-US` everywhere and leave additional English variants to reviewed taxonomy extension.
- needs-decision rationale: none

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | block | SR4 creates contradictory requirements for the required English locale key. |
| normative language | concern | The R2 revision strengthened lifecycle and review routing, but locale requirements still conflict with the normative enum. |
| completeness | pass | The revised spec now defines lifecycle semantics, review routing, controlled enums, audit fields, and relevant edge cases. |
| testability | block | Locale validation fixtures cannot pass both R2 and AC23/AC25 as written. |
| examples | concern | E1 and E2 still use `en`, contradicting the v1 locale enum. |
| compatibility | concern | Locale key choice is a migration-sensitive contract and must be stable before architecture relies on it. |
| observability | pass | Audit and validation output requirements are concrete and preserve separate review/publication state. |
| security/privacy | pass | The spec avoids PII, secrets, private reviewer contact details, PHI, and unconstrained AI source-of-truth content. |
| non-goals | pass | Implementation, UX, legal, AI, rehab, and exact exercise-list scope remain appropriately out of scope. |
| acceptance criteria | block | AC25 requires `en-US` while R2 requires `en`; acceptance criteria cannot be implemented against both. |

## Resolved Prior Findings

- SR1 is resolved by separate `review_status` and `publication_status` fields, allowed transition tables, publication eligibility invariants, review-sensitive edit behavior, and separate audit fields.
- SR2 is resolved by the review-routing matrix, reviewer-tier semantics, cumulative review obligations, and elevated-risk default-deny behavior.
- SR3 is resolved by the minimum v1 controlled enums and reviewed taxonomy-extension behavior.

## Exact Suggested Changes

- Change the glossary locale example from `en` to `en-US`.
- Change E1 from required `en` locale fields to required `en-US` locale fields.
- Change E2 from locale key `en` to locale key `en-US`.
- Change R2 to require at least one English locale branch keyed as `en-US`.
- Change R3 to say additional locale branches use the same field structure as `en-US`.

## Routing

Immediate next stage is `spec revision`. This is a narrow revision: once the English locale key is normalized, the spec should be ready for another spec review focused on confirming the locale contract and preserving the R2 lifecycle/review-routing fixes.
