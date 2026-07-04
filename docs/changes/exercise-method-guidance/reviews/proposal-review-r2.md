# Proposal Review R2: Exercise Method Guidance by Training Type

## Result

- Skill: proposal-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-method-guidance/reviews/proposal-review-r2.md`
- Review log: `docs/changes/exercise-method-guidance/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Immediate next stage: isolated stop; `spec` is the next lifecycle stage only after an explicit workflow or user request

## Material Findings

None.

## Review Dimensions

| Dimension | Result | Notes |
| --- | --- | --- |
| Problem clarity | pass | The proposal states the beginner problem as a missing page-local answer to "How much of this should I do?" rather than starting from a tooling solution. |
| User value | pass | The user value is concrete: exercise pages become more usable at the point where beginners need starter amount, effort, rest, and progression guidance. |
| Option diversity | pass | The proposal compares doing nothing, one universal sets-and-reps line, method guidance by training type, and principle-page-only guidance. |
| Decision rationale | pass | The recommended training-type approach follows from the exercise variety and preserves non-prescriptive boundaries. |
| Scope control | pass | Non-goals clearly exclude individualized programming, rehab, diagnosis, symptom-based substitutions, advanced optimization, calculators, and broad unreviewed rewrites. |
| Architecture awareness | pass | The proposal names `specs/exercise-method-guidance.md` as the focused normative artifact and limits architecture review to future metadata, taxonomy, generated index, or cross-page data-model choices. |
| Testability | pass | The proposal identifies section-presence checks, forbidden-language checks, source support, pattern-preview alignment, source-audit sampling, and beginner comprehension proof. |
| Risk honesty | pass | The proposal names prescription drift, inconsistent classification, under-sourcing, broad rewrites, principle-page conflicts, safety-routing weight, and page length. |
| Rollout realism | pass | The proposal uses a focused spec, template/check updates, a six-page proof slice, same-slice principle support, and a separate broad rollout. |
| Readiness for spec | pass | Proposal-level decisions are resolved; remaining detail is appropriate for `specs/exercise-method-guidance.md`. |

## Scope Preservation Review

- Scope-preservation result: pass

The user's initial goals are preserved and classified in `Initial Intent Preservation`:

| Initial user goal | Review result |
| --- | --- |
| Provide specific exercise instructions for each exercise, including repetitions per set and sets per exercise. | in scope |
| Provide appropriate methods for different types of training. | in scope |
| Improve exercises in the repository. | in scope |
| Avoid drifting into personalized workout planning. | in scope |

The scope budget is appropriate for a multi-workstream proposal. It separates the core exercise-method contract and training-type menu from same-slice dependencies, first-slice proof pages, broad exercise rollout, and out-of-scope program examples.

## Recommended Proposal Edits

- Recommended edits: remove or revise the stale sentence in `Recommended Direction` that says the section "should be called something like `How much to do` or `Beginner method`, with final naming left to the spec." The later resolved decision correctly chooses `How much to do`; this cleanup is non-blocking because the proposal's `Resolved Decisions for First Implementation` and `Decision Log` settle the heading.

## Recommendation

- Recommendation: approve the proposal direction for downstream spec authoring.

The proposal is ready to normalize to `accepted` before downstream stages rely on it. The next lifecycle artifact should be `specs/exercise-method-guidance.md`, but this direct proposal-review request remains isolated and does not automatically hand off to spec authoring.
