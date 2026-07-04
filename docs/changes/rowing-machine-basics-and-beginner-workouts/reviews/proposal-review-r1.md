# Proposal Review R1: Rowing Machine Basics and Beginner Workout Guidance

## Result

- Skill: proposal-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/proposal-review-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Immediate next stage: isolated stop; `spec` is the next lifecycle stage only after proposal status normalization and an explicit workflow or user request

## Material Findings

None.

## Review Dimensions

| Dimension | Result | Notes |
| --- | --- | --- |
| Problem clarity | pass | The proposal states the beginner problem directly: rowing machines are common, but the movement is technical and GymPrimer lacks a dedicated setup/technique/method page. |
| User value | pass | The benefit is concrete for a beginner standing in front of a rower: foot setup, stroke sequence, damper meaning, effort framing, workout examples, and stop conditions. |
| Option diversity | pass | The proposal compares doing nothing, a general cardio-equipment principle page, a dedicated rowing-machine page, and a rowing program. |
| Decision rationale | pass | The recommended dedicated page follows from the specificity of rowing setup and the drive/recovery sequence, while deferring broader programs. |
| Scope control | pass | Non-goals clearly exclude personalized plans, race training, sport performance, beginner sprint protocols, heart-rate prescription, weight-loss claims, rehab, hosted tools, and borrowed commercial media. |
| Architecture awareness | pass | The proposal names the expected Markdown page, source index, template, method spec, optional media, provenance, checker, and red-flag surfaces without inventing runtime architecture. |
| Testability | pass | The proposal identifies automated checks, source-support review, media/provenance checks when relevant, and beginner read-test questions. |
| Risk honesty | pass | The major risks are named: plan drift, hard-effort drift, under-sourced setup, damper misunderstanding, rowing replacing strength work, page length, visual miscue risk, and medical-advice drift. |
| Rollout realism | pass | Rollout starts with proposal review and a focused method-spec amendment before drafting the page; rollback is narrow because the change is Markdown-first. |
| Readiness for spec | pass | The remaining open questions are appropriate for spec or implementation planning. The known blocker, `basic_cardio_equipment`, is correctly routed to a focused downstream spec amendment. |

## Scope Preservation Review

- Scope-preservation result: pass

The user's initial goals are visibly classified in `Initial intent preservation`:

| Initial user goal | Review result |
| --- | --- |
| Explain best practices for using a rowing machine | in scope |
| Generate a proposal for GymPrimer | in scope |
| Fit the current project shape | in scope |
| Keep guidance beginner-safe | in scope |
| Include workout guidance | in scope |
| Avoid overbroad programming | in scope |
| Use best practices and sources | in scope |

The scope budget is appropriate for a multi-workstream proposal. It separates the core rowing page from the same-slice method/spec dependency, optional media, generated-image provenance, source-index work, beginner read-test evidence, deferred cardio-equipment pages, and out-of-scope sport/rehab content.

## Recommended Proposal Edits

- Recommended edits: none required for approval.

Non-blocking note: before downstream reliance, normalize the proposal status from `draft` to `accepted` and add this review record under `Follow-on artifacts` or equivalent closeout text. The proposal is otherwise ready for acceptance.

## Recommendation

- Recommendation: approve the proposal direction for downstream spec authoring.

The proposal is ready to normalize to `accepted` before downstream stages rely on it. The next lifecycle artifact should be a focused spec amendment for `basic_cardio_equipment` and the rowing-machine exercise-page contract. This direct proposal-review request remains isolated and does not automatically hand off to spec authoring.
