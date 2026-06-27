# Spec Review: Content Schema and Review Contract R1

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: SR1, SR2, SR3
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/beginner-fitness-exercise-education-platform/reviews/spec-review-r1.md`
- Review log: `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`
- Review resolution: `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`
- Open blockers: SR1, SR2, SR3
- Immediate next stage: spec revision
- Eventual test-spec readiness: not-ready
- Stop condition: spec has material contract gaps that would force tests and architecture to guess

## Findings

## Finding SR1

- Finding ID: SR1
- Severity: major
- Location: `specs/content-schema.md` requirements R19-R26 and state/invariant sections
- Evidence: R20 defines statuses `draft`, `in-review`, `approved`, `published`, `hidden`, and `superseded`; R21 says a card is publishable with "approved review status"; R26 says a review-sensitive edit moves a published card "out of publishable state"; outputs list review-state changes as the same statuses. This mixes review lifecycle and publication lifecycle into one enum, leaving unclear whether `approved` means reviewed but not public, whether `published` is allowed without `approved`, and which status a review-sensitive edit moves to.
- Required outcome: The spec must define unambiguous review and publication state semantics that allow tests to assert valid transitions and publication eligibility.
- Safe resolution path: Split review status from publication status, or define a single explicit state machine with allowed transitions. Add requirements and acceptance criteria for draft, in-review, approved, published, hidden, superseded, and review-sensitive edit behavior.
- needs-decision rationale: none

## Finding SR2

- Finding ID: SR2
- Severity: major
- Location: `specs/content-schema.md` requirements R22-R24, R26, examples E3, and acceptance criteria
- Evidence: R22 says trainer or strength-coach review approves every publishable card. R23 says physical therapist review covers safety-language policy before public beta. R24 says sports-medicine clinician review applies to disclaimer policy, emergency criteria, and elevated-risk cards once categories are defined. R26 requires "the relevant review tier" to approve review-sensitive edits, but the spec does not define which fields trigger card-level trainer review versus policy-level PT review versus clinician review, or what happens before elevated-risk categories are defined.
- Required outcome: The spec must make tiered review obligations testable for card publication and review-sensitive edits without requiring implementers to infer credential routing.
- Safe resolution path: Add a review matrix mapping content change categories to required reviewer tier and scope, such as card-level trainer review, policy-level PT review, clinician policy review, and elevated-risk card review once categories exist. Add acceptance criteria for at least one trainer-only change, one policy-sensitive safety-language change, and one elevated-risk blocker or deferral.
- needs-decision rationale: none

## Finding SR3

- Finding ID: SR3
- Severity: major
- Location: `specs/content-schema.md` requirements R6-R8, R18, R20, R23-R24, R32-R33, open questions, and acceptance criteria
- Evidence: The spec requires controlled taxonomy IDs and review statuses, but does not define allowed seed values for required enums such as card type, difficulty, safety category, review tier, locale list beyond examples, contribution provenance, media type, and licensing fields. The "exact allowed taxonomy IDs" remain an open question, yet R8 and AC3 require validation against unknown IDs. Architecture and test-spec cannot build fixtures without a minimal normative seed taxonomy.
- Required outcome: The spec must include enough controlled values to validate the first cards, while allowing future taxonomy extension through reviewed changes.
- Safe resolution path: Define minimum v1 controlled enums for card type, difficulty, review tier, publication/review statuses, media kind, locale keys, license kind, and safety category. Keep full muscle/equipment lists extensible if needed, but require a seed taxonomy fixture or companion taxonomy spec before architecture/test-spec relies on validation.
- needs-decision rationale: none

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | block | SR1 and SR2 leave state and tiered-review behavior ambiguous. |
| normative language | concern | Most MUSTs are testable, but R23-R24 depend on undefined review scopes and elevated-risk categories. |
| completeness | block | SR3 shows missing controlled values required for validation fixtures. |
| testability | block | Tests cannot assert review-state transitions or taxonomy rejection without resolving SR1-SR3. |
| examples | concern | Examples are useful but need coverage for review-state transitions and review-tier routing. |
| compatibility | pass | Versioning, migration, locale extension, and breaking-change handling are addressed. |
| observability | pass | Validation output and review-state audit requirements are concrete enough. |
| security/privacy | pass | PII, secrets, private reviewer data, and AI source-of-truth restrictions are explicit. |
| non-goals | pass | Excluded implementation, UX, legal, AI, rehab, and exact exercise-list scope is clear. |
| acceptance criteria | block | ACs do not cover state-machine semantics, review-tier routing, or minimum controlled enums. |

## Exact Suggested Changes

- Replace R19-R21/R25-R26 with explicit review and publication state requirements, or a single state machine with allowed transitions.
- Add a table mapping field/change category to required review tier and review scope.
- Add minimum v1 enums or a required seed taxonomy fixture for card type, difficulty, safety category, review tier, media kind, locale keys, license kind, and status fields.
- Add acceptance criteria for state transitions, tiered review routing, and minimum taxonomy validation.

## Routing

Immediate next stage is `spec revision`. Architecture should not start until these material findings are resolved and a later spec-review records approval.
