# Proposal Review R1: Brisk Walking and Everyday Walking Guidance

## Result

- Skill: proposal-review
- Review status: changes-requested
- Material findings: PR-WALK-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/proposal-review-r1.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-resolution.md`
- Open blockers: PR-WALK-1 must be resolved before this proposal is accepted or used for spec authoring
- Immediate next stage: isolated stop

## Material Findings

## Finding PR-WALK-1

- Finding ID: PR-WALK-1
- Severity: major
- Location: `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md:120`, `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md:164`, `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md:467`, `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md:507`, `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md:531`
- Evidence: The proposal recommends Option C, names `exercises/brisk-walking.md` and `principles/everyday-walking.md`, and records decisions to add two complementary pages and treat brisk walking as `basic_cardio_activity`. Later, `Open questions` and `Readiness` reopen whether `basic_cardio_activity` belongs in the method contract and whether everyday walking is a separate principle page or a section inside brisk walking. Those are not just implementation details; they are the core proposal decisions.
- Required outcome: Make the proposal internally consistent before acceptance or spec authoring. Either commit to the two-page split and `basic_cardio_activity` as the proposal decision, or reclassify one or both as unresolved blocking questions and revise recommendation, decision log, scope budget, rollout, readiness, and next artifacts accordingly.
- Safe resolution path: Preferred path: keep Option C as the decision, keep `exercises/brisk-walking.md`, keep `principles/everyday-walking.md`, keep `basic_cardio_activity`, and revise `Open questions` / `Readiness` so downstream spec decides only contract details such as exact requirement wording, validation timing, source IDs, optional image use, and read-test wording. Alternate path: if the owner still wants the two-page split or method type to be undecided, change the proposal status/readiness to blocked for spec, move the unsettled item into `Open questions`, and remove or soften the conflicting decision-log entries.
- needs-decision rationale: none

## Review Dimensions

| Dimension | Result | Notes |
| --- | --- | --- |
| Problem clarity | pass | The proposal states a real beginner-content gap: walking is accessible, but GymPrimer lacks a clear distinction between everyday movement and deliberate brisk walking. |
| User value | pass | The benefit is concrete: beginners get intensity checks, starter duration, progression framing, technique cues, muscle roles, strength-training context, and stop rules. |
| Option diversity | pass | The proposal compares doing nothing, a broad principle page, two complementary pages, and a walking program. |
| Decision rationale | concern | Option C is well supported, but PR-WALK-1 shows the decision is later reopened in `Open questions` and `Readiness`. |
| Scope control | pass | Non-goals exclude personalized plans, weight-loss prescriptions, step mandates, medical protocols, running, hiking, rucking, tracking, and adaptive flows. |
| Architecture awareness | pass | The proposal names the content pages, source index, exercise template/spec surface, checker surface, and optional provenance surface without inventing a runtime system. |
| Testability | pass | Automated checks, manual source review, and beginner comprehension proof are specific enough for downstream test-spec authoring. |
| Risk honesty | pass | Major risks are named, including weight-loss drift, casual-walking equivalence, medical drift, prescription feel, step-count overconfidence, weak images, broad source support, and fluff. |
| Rollout realism | concern | The rollout is generally realistic, but it should match the resolved core decision after PR-WALK-1. |
| Readiness for spec | block | The proposal should not enter spec until it stops reopening the two-page and method-type decisions or explicitly marks them as blocking. |

## Scope Preservation Review

- Scope-preservation result: pass with one consistency blocker.
- Scope-budget result: pass.
- Vision-fit result: pass.
- Standing-gate result: pass.

The user's initial goals are visible in `Initial intent preservation`: best practices for brisk walking, best practices for everyday walking, proposal generation, project fit, and safety/personalization boundaries are all classified as `in scope`.

The scope budget is appropriate for a multi-workstream proposal. It separates core walking pages, the method-type dependency, technique and intensity guidance, same-slice muscle guidance, optional image work, deferred step-count/program work, separate treadmill work, and out-of-scope medical/running work.

The `Vision fit` section uses the exact allowed value `fits the current vision`, and the direction aligns with `VISION.md` and `CONSTITUTION.md`: static Markdown education, citation-backed content, no hosted app, no diagnosis, no treatment plan, and no personalized coaching.

## Recommended Proposal Edits

- Resolve PR-WALK-1 by aligning `Open questions`, `Decision log`, `Scope budget`, `Next artifacts`, and `Readiness`.
- If the proposal keeps Option C, remove "whether everyday walking should be a principle page or a section inside brisk walking" from downstream open questions and replace it with spec-level details such as exact page contract wording and cross-link wording.
- If the proposal keeps `basic_cardio_activity`, remove "whether `basic_cardio_activity` belongs in the exercise-method contract" as an implementation blocker and instead say the next spec should add or amend the method contract for that accepted direction.
- Consider expanding `Next artifacts` to include the required review gates after spec: spec review, architecture assessment, plan, plan review, test-spec, and test-spec review before content implementation.
- Optional cleanup: after review resolution and owner acceptance, normalize proposal status to `accepted` and add this review record under `Follow-on artifacts`.

## Recommendation

- Recommendation: changes requested.
- Reason: The proposal direction is strong and vision-aligned, but it is not ready for spec while core decisions are both recommended and reopened.
- Next step: revise the proposal to resolve PR-WALK-1, then run proposal-review R2.
- Immediate next stage: isolated stop. This review does not automatically start spec authoring.
