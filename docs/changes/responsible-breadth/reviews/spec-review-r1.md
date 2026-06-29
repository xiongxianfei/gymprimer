# Spec Review R1: Responsible Breadth Content Expansion

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: SR-RB-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/responsible-breadth/reviews/spec-review-r1.md`
- Review log: `docs/changes/responsible-breadth/review-log.md`
- Review resolution: `docs/changes/responsible-breadth/review-resolution.md`
- Open blockers: SR-RB-1
- Immediate next stage: spec revision
- Eventual test-spec readiness: not-ready
- Stop condition: spec must resolve same-rank compatibility with `specs/markdown-first-primer.md`

## Findings

## Finding SR-RB-1

- Finding ID: SR-RB-1
- Severity: blocking
- Location: `specs/responsible-breadth.md` lines 25-27 and 313-320; `specs/markdown-first-primer.md` lines 94-100, 134-136, 255-263, and 271-288.
- Evidence: The Responsible Breadth spec says the approved Markdown-first v0.1 spec remains active for the original five-page slice and that the expansion adds a new governed surface after constitution and vision amendment. The existing approved Markdown-first spec still has broad v0.1 requirements that the first slice must include exactly five pages before broader content expansion, that v0.1 content must stay within beginner principles, machines, low-risk bodyweight, dumbbell patterns, and basic cardio, and that v0.1 content must not include injury-specific advice, posture-correction protocols, pain treatment, diagnosis, or rehabilitation pathways. Because both specs would sit at the same source-of-truth rank once approved, downstream architecture, validation, and implementation would have to guess whether Responsible Breadth amends, supersedes, or versions the old R21/R22 and related promotion boundaries.
- Required outcome: The spec set must explicitly settle same-rank compatibility before approval. Downstream readers must be able to tell which requirements govern the original Markdown-first five-page slice, which requirements govern Responsible Breadth pages, and whether any old v0.1 exclusions are amended or superseded for the expanded surface.
- Safe resolution path: Revise `specs/responsible-breadth.md` to include a clear compatibility rule such as "For Responsible Breadth pages, this spec supersedes `specs/markdown-first-primer.md` R21/R22 only for the accepted expanded content types; all Markdown source-of-truth, citation, media, privacy, and promotion requirements from the Markdown-first spec continue to apply unless this spec gives a stricter rule." Also update `specs/markdown-first-primer.md` with a brief compatibility note pointing to `specs/responsible-breadth.md` as the governing spec for expanded pattern, condition, principle, and program-example pages. Preserve the original five-page v0.1 contract.
- needs-decision rationale: none

## Review Dimensions

| Review dimension | Verdict |
| --- | --- |
| requirement clarity | concern |
| normative language | pass |
| completeness | concern |
| testability | concern |
| examples | pass |
| compatibility | block |
| observability | pass |
| security/privacy | pass |
| non-goals | pass |
| acceptance criteria | concern |

Notes:

- Requirement clarity: the Responsible Breadth page contracts, source-quality rules, program boundaries, review cadence, media rules, and proof obligations are mostly clear. SR-RB-1 blocks because the old-spec conflict makes the governing requirement set ambiguous.
- Normative language: requirements use testable `MUST`/`MUST NOT`/`SHOULD` wording and manual-verification paths where automation is not sufficient.
- Completeness: normal, boundary, rollback, privacy, observability, and accessibility behavior are covered. Same-rank migration/compatibility is incomplete.
- Testability: the new spec is broadly testable, but test-spec cannot map requirements safely until it knows how old Markdown-first exclusions interact with Responsible Breadth.
- Examples: examples cover non-diagnostic pattern pages, red-flag routing, static program examples, source quality, necessary visuals, and first-slice scope.
- Compatibility: blocked by SR-RB-1.
- Observability: review records, manual proof records, validation output, and command reporting are specified.
- Security/privacy: private health information, reader-test identification, symptom collection, and personal inference are prohibited.
- Non-goals: excluded product shapes and specialized content are clear.
- Acceptance criteria: AC1-AC10 are useful, but approval cannot stand until compatibility is resolved.

## Recommendation

- Recommendation: changes-requested. Resolve SR-RB-1, then request spec-review R2.
- No automatic downstream handoff. This direct spec-review request remains isolated.
