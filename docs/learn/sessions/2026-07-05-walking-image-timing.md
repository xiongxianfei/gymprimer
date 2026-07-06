# Learn Session: Walking Image Timing

## Result

- Skill: learn
- Status: recorded
- Artifacts changed: `docs/learn/sessions/2026-07-05-walking-image-timing.md`
- Open blockers: none for this learn record
- Next stage: none from learn
- Session path: `docs/learn/sessions/2026-07-05-walking-image-timing.md`
- Lessons captured: none
- Follow-ups: none created

## Frame

- Trigger: explicit `$learn` maintainer question asking why GymPrimer did not generate exercise images at the first time for the walking exercise document.
- Trigger type: explicit maintainer request and contributor observation.
- Scope: the brisk-walking and everyday-walking image/no-image decision in the active walking guidance change.
- Evidence in scope:
  - `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md`
  - `specs/brisk-walking-and-everyday-walking.md`
  - `specs/brisk-walking-and-everyday-walking.test.md`
  - `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/optional-image-decision.md`
  - `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m3-r1.md`
  - `AGENTS.md`
- Explicit exclusions:
  - No generated image asset is created in this learn session.
  - No media provenance, prompt record, exercise page, proposal, spec, architecture, plan, workflow, or skill behavior is changed.
  - No claim is made that future walking images are forbidden.
  - No claim is made that every future exercise page should start text-only.
  - No verification readiness, PR readiness, CI status, or branch readiness is claimed.
- Prior learnings reviewed:
  - `docs/learn/topics/content-quality.md`
  - `docs/learn/sessions/2026-07-04-muscle-guidance-best-practices.md`
  - `docs/learn/sessions/2026-07-04-test-spec-skill-proof-contracts.md`
  - `docs/learn/README.md` was checked but does not exist.

## Observe

| Observation ID | Observation | Evidence |
| --- | --- | --- |
| OBS-001 | Walking images were not generated in the first slice because the approved change made media optional, not required. | The accepted proposal says walking pages do not require images by default and says not to add multiple walking images unless a beginner read test shows text alone is unclear. The approved spec says `exercises/brisk-walking.md` may include no image and must remain valid as text-only, while `principles/everyday-walking.md` must not include an image in the first implementation slice unless a later approved amendment records why. |
| OBS-002 | The plan intentionally defaulted to text-only unless implementation evidence found a concrete comprehension issue. | The active plan states that the approved first slice does not require a walking image, that text-only brisk walking remains valid, and that no image should be generated unless implementation evidence shows text alone is not enough and the image can satisfy the exercise-image standard. |
| OBS-003 | M3 manual proof found no concrete image need. | `optional-image-decision.md` records `decision: text-only`, says no image was added, states that the Markdown explains posture, arm swing, heel-to-toe walking, start/finish, talk-test effort, and progression without needing an image, and says the beginner-comprehension proof records no comprehension gap requiring an image. |
| OBS-004 | Generated exercise images carry governance cost and risk, so the project treats them as support artifacts rather than default content. | The plan and optional image record require local asset paths, meaningful alt text, prompt records, approved provenance rows, no in-image labels, no red pain marks, no wrong/correct framing, page references, and visual-safety evidence when an image is added. `AGENTS.md` also says generated output and media-source changes must not be implemented from chat alone. |
| OBS-005 | The maintainer question may indicate a future product direction: default exercise images might be desirable for some exercise documents, but that direction is broader than the walking change. | The current walking change already has a text-only decision. Changing default image timing across exercise pages would affect media policy, specs, validation, provenance, review effort, and possibly templates. |

## Classify

| Observation ID | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
| --- | --- | --- | --- | --- | --- |
| OBS-001 to OBS-004 | observation | observation | session record only | Current accepted proposal, approved spec, active plan, manual proof, and M3 code review | The evidence explains why images were not generated in this slice, but it does not show a recurring failure or systemic gap. The decision is already captured in authoritative walking artifacts. |
| OBS-005 | direction | direction-candidate | future proposal if the maintainer wants default image generation for exercise pages | Maintainer question only; no confirmation to change default policy | A broader "generate images at the first time" rule would change media policy and workflow behavior. It needs an owning proposal/spec or workflow artifact, not a learn-topic entry. |
| OBS-001 to OBS-005 | no-durable-lesson | no-durable-lesson | none | Learn skill evidence standard | This is a single workflow observation with an already-recorded rationale. There is not enough accumulated evidence to add durable topic guidance or change default agent behavior from learn alone. |

## Route

- Topic updates: none.
- Authoritative artifact updates: none.
- Follow-ups created: none.
- Scheduled follow-up: none.
- Routing note: if the maintainer wants exercise images to be generated by default in future first slices, open a proposal for exercise-media timing and governance. That proposal should decide which exercise types need images by default, which image purposes are required or optional, when beginner proof can skip media, and how prompt records, provenance, visual review, and tests scale.

## Answer to the Maintainer Question

We did not generate images the first time for walking because the source-of-truth artifacts deliberately made the first walking slice text-only unless evidence showed an image was needed.

That choice had four practical reasons:

1. The walking Markdown already explained the key visual cues: upright posture, natural arm swing, relaxed hands, heel-to-toe walking, easy start, easy finish, talk-test effort, and progression.
2. The beginner-comprehension proof found no setup or movement-comprehension gap that required an image.
3. Generated exercise images are not free in this project: each one needs a local asset, prompt record, provenance row, alt text, visual-safety review, page reference, tests, and maintenance.
4. GymPrimer is Markdown-first. Images should support the text when they solve a real beginner comprehension problem, not become the source of truth or automatic decoration.

The current decision does not forbid a future brisk-walking image. It says a later proof can add one `exercise_movement_illustration` if a concrete setup or movement-comprehension gap appears.

## No-Learn Rationale

No durable lesson was added to `docs/learn/topics/`.

This session records an evidence-bound explanation, but the evidence is a single feature-slice decision that is already captured in the proposal, spec, plan, manual proof, and code-review record. A broader default-image rule would need proposal/spec/workflow work before it becomes project guidance.

## Validation

- Session record only; no product content, media, spec, plan, workflow, skill, provenance, or topic file changed.
