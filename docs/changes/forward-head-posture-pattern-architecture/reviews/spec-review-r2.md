# Spec Review R2: Central Disclaimer Amendment

## Result

- Skill: spec-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/forward-head-posture-pattern-architecture/reviews/spec-review-r2.md`
- Review log: `docs/changes/forward-head-posture-pattern-architecture/review-log.md`
- Review resolution: `docs/changes/forward-head-posture-pattern-architecture/review-resolution.md`
- Open blockers: none
- Immediate next stage: architecture
- Eventual test-spec readiness: conditionally-ready
- Stop condition: direct spec-review request is isolated; no automatic downstream handoff. Architecture-review should assess the amended central-disclaimer boundary before M1 re-review or M2 implementation.

`Immediate next stage` is the routing field; allowed values exclude `test-spec`.
Use `Eventual test-spec readiness` to assess whether test-spec authoring will
be possible after required routing stages.

## Findings

None.

## Review Scope

- Primary spec: `specs/forward-head-posture-pattern-architecture.md`
- Governing shared spec amended by this change: `specs/markdown-first-primer.md`
- Proof map checked for alignment: `specs/forward-head-posture-pattern-architecture.test.md`
- Template contract checked for alignment: `docs/templates/exercise-card.md`, `docs/templates/principle-page.md`, `docs/templates/pattern-page.md`, `docs/templates/condition-page.md`
- Review trigger: owner clarification that the prominent disclaimer should be centralized in `RED-FLAGS.md`, not repeated on every page.

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | pass | R7 and R8 in `specs/markdown-first-primer.md` now identify `RED-FLAGS.md` as the central disclaimer surface, and R16 in the forward-head spec removes per-exercise disclaimer language while retaining safety-routing requirements. |
| normative language | pass | The amended requirements use testable `MUST` language for the central disclaimer and conditional safety routing, while templates remain authoring prompts rather than governance-only policy. |
| completeness | pass | The amendment covers the shared Markdown-first spec, forward-head proof-slice spec, test-spec expectations, template prompts, checker behavior, review-resolution disposition, and lifecycle routing. |
| testability | pass | The proof surface includes a unit test requiring the central disclaimer on `RED-FLAGS.md`, tests proving page-local disclaimers are not required, template tests preventing repeated disclaimer scaffolding, and active Markdown checker coverage. |
| examples | pass | Existing forward-head examples remain valid because the amendment changes safety framing location, not the page/link/media behavior those examples cover. |
| compatibility | pass | Existing pages may retain old page-local disclaimers without becoming invalid, while new templates stop requiring repeated boilerplate. The central `RED-FLAGS.md` path is stable and already active. |
| observability | pass | The checker emits `MF001` against `RED-FLAGS.md` when the central disclaimer is missing or too low, and validation evidence records the central-disclaimer and stale-template-path checks. |
| security/privacy | pass | Centralizing the disclaimer does not add user input, symptom intake, private health data, runtime behavior, or generated advice. The existing no-diagnosis and privacy requirements remain unchanged. |
| non-goals | pass | The amendment aligns with the Responsible Breadth non-goal against per-card legal disclaimer scaffolding and does not reopen diagnosis, treatment, rehab, personalization, app, or media-policy scope. |
| acceptance criteria | pass | AC3 in the shared spec now observes `RED-FLAGS.md` directly; AC8 in the forward-head spec remains observable through the exercise-page contract without requiring repeated disclaimers. |

## No-Finding Rationale

The amended contract is precise enough for downstream review and testing: it identifies the sole required disclaimer surface, preserves conditional safety routing from page templates to `RED-FLAGS.md`, removes the conflicting per-page disclaimer requirement from the forward-head exercise contract, and keeps red-flag routing before exercise/self-management content. No implementation or content author needs to guess whether to repeat the full disclaimer on every page.

## Eventual Test-Spec Readiness

Conditionally ready. The proof map already reflects the central-disclaimer amendment, but it should be re-reviewed or status-normalized after architecture-review confirms the amended boundary.
