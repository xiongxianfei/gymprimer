# Proposal Review R1: Top-Five Generated Images for Fewer-Than-Five Exercise Documents

## Result

- Skill: proposal-review
- Review status: changes-requested
- Material findings: PR-T5IMG-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/proposal-review-r1.md`
- Review log: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-log.md`
- Review resolution: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-resolution.md`
- Open blockers: PR-T5IMG-1 must be resolved before spec relies on this proposal. [Source][local-proposal-review-r1-exercise-image-standard]
- Immediate next stage: isolated stop; proposal revision is next. [Source][local-proposal-review-r1-proposal]

## Material Findings

## Finding PR-T5IMG-1

- Finding ID: PR-T5IMG-1
- Severity: major
- Location: `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`, `Vision fit`, `Goals`, `Recommended Direction`, `Expected Behavior Changes`, `Risks and Mitigations`, and `Readiness`
- Evidence: The proposal asks to "Revise the generated-image reviewer contract so this initiative does not require a separate accountable human reviewer field beyond repository PR review" and says downstream spec should remove the separate generated-image human-reviewer requirement for this initiative only. It also says the proposal fits only if generated images have "clear provenance and human review" and keeps visual-safety evidence, beginner-comprehension proof, and promotion gates. The approved exercise-image standard currently requires `human_reviewer` in provenance rows and defines visual-safety review as human review, so the proposal removes a concrete accountability field without defining the replacement accountability surface.
- Required outcome: Revise the proposal to specify the replacement accountability model for generated image promotion. The revision must say whether repository PR author review, PR approval, change-local visual-safety evidence owner, provenance `notes`, prompt-record review owner, or another durable artifact becomes the accountability surface. It must also update risks, mitigation, rollout, testing strategy, and readiness so downstream specs can implement the reviewer-field exception without weakening visual-safety, provenance, privacy, source-support, and rollback proof.
- Safe resolution path: Keep the user's direction that a separate per-image `human_reviewer` field is not required, but add a named replacement such as "review accountability is recorded at the milestone/change level through PR author acceptance and change-local visual-safety evidence." Then route the exact field-level behavior to spec review. If the owner instead wants no accountable human review at all, the proposal must explicitly classify that as a source-order conflict with `CONSTITUTION.md`, `VISION.md`, and `specs/exercise-image-standard.md`, and require a higher-ranked governance or media-policy revision before implementation.
- needs-decision rationale: Owner decision is needed at the proposal/spec boundary because this changes the media trust model for AI-generated exercise images and determines whether downstream validation may accept blank `human_reviewer` rows.

## Review Dimensions

| Dimension | Result | Notes |
|---|---|---|
| Problem clarity | pass | The proposal states the real conflict: the user wants top-five image generation for fewer-than-five exercise documents, while the current accepted workflow treats the threshold as evaluation only. |
| User value | pass | The proposal names concrete beginner value: more setup, movement, and broad attention visuals for pages that currently have low image coverage. |
| Option diversity | pass | It compares preserving the current policy, direct chat generation, a governed named-population revision, and a smaller pilot batch. |
| Decision rationale | pass | The recommended named-population exception follows from the user's selected direction while preserving source-order review before implementation. |
| Scope control | pass | Non-goals exclude direct generation, Baduanjin, borrowed media, hosted systems, clinical framing, and personalized coaching. |
| Architecture awareness | concern | The media/provenance surfaces are named, but PR-T5IMG-1 leaves the replacement accountability surface underdefined after removing `human_reviewer`. |
| Testability | concern | Image-count, prompt-record, provenance, path, alt-text, and privacy checks are testable; reviewer-field exception tests are not yet spec-ready because the replacement accountability source is undefined. |
| Risk honesty | concern | The proposal names review capacity risk, but it does not yet name the trust/accountability risk introduced by removing per-image reviewer attribution. |
| Rollout realism | concern | Two or three milestones are realistic, but rollout must state how each milestone proves visual-safety accountability if per-image `human_reviewer` is blank. |
| Readiness for spec | block | The direction is close, but PR-T5IMG-1 must be resolved before a spec can safely rely on the proposal. |

## Scope Preservation Review

- Scope-preservation result: pass.
- The proposal visibly classifies the user's goals: top-five images for the listed documents, fewer-than-five included population, Baduanjin exclusion, existing accepted image counting, older sequence image counting, no separate human-reviewer requirement, and two-or-three milestone implementation.
- The one deferred goal, implementation across two or three milestones, is routed through rollout and scope budget.

## Scope Budget Review

- Scope-budget result: pass with one material accountability caveat covered by PR-T5IMG-1.
- The proposal uses allowed treatment values and separates policy revision, spec amendments, architecture assessment, per-page audits, milestone implementation, generated assets, and template follow-up.

## Vision Fit Review

- Result: concern.
- The first non-empty line under `Vision fit` is the exact allowed value `fits the current vision`.
- Root `VISION.md` exists, and the proposal does not use `no vision exists yet`.
- The image-count direction fits the current vision when Markdown remains the source of truth.
- The reviewer-field exception needs PR-T5IMG-1 resolution because the proposal currently says human review remains part of the fit while removing the concrete reviewer field.

## Standing Artifact Gate Review

- Result: pass.
- `VISION.md` and `CONSTITUTION.md` exist.
- The proposal explicitly identifies that accepted proposals/specs need revision before implementation, rather than silently bypassing source order.

## Evidence Reviewed

- `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `CONSTITUTION.md`
- `VISION.md`
- `specs/exercise-image-standard.md`
- User direction in this thread:
  - five means five total images per page;
  - existing accepted images count;
  - accepted older sequence images count;
  - no separate human reviewer;
  - all documents should be implemented across two or three milestones;
  - related spec should be updated.

## Recommended Proposal Edits

- Add a risk row for "reviewer-field removal weakens generated-media accountability" and a mitigation that names the replacement accountability artifact.
- Replace generic "beyond repository PR review" wording with a precise rule, for example: "per-image `human_reviewer` may be blank only when the milestone has change-local visual-safety evidence and PR author acceptance that names the accountable owner for the batch."
- Update `Testing and Verification Strategy` to require checks for the replacement accountability artifact when `human_reviewer` is blank.
- Update `Rollout and Rollback` so each milestone cannot close unless the replacement accountability evidence exists.
- Update `Readiness` to say the proposal is ready for spec only after PR-T5IMG-1 is resolved and the proposal status is normalized to `accepted`.

## Recommendation

- Recommendation: changes requested.
- Reason: The top-five image-count direction is reviewable and aligned enough to proceed after revision, but the reviewer-field exception changes the generated-media trust model and currently lacks a concrete replacement accountability surface.
- Next step: revise the proposal to resolve PR-T5IMG-1, then rerun proposal-review.
- Immediate next stage: isolated stop; no automatic downstream handoff. [Source][local-proposal-review-r1-proposal]

## Sources

- `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `CONSTITUTION.md`
- `VISION.md`
- `specs/exercise-image-standard.md`

[local-proposal-review-r1-proposal]: ../../../proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md
[local-proposal-review-r1-exercise-image-standard]: ../../../../specs/exercise-image-standard.md
