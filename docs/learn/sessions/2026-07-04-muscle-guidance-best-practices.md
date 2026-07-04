# Learn Session: Muscle Guidance Best Practices

## Frame

- Trigger: explicit `$learn` invocation from the maintainer stating that
  `Muscles involved` is a very good practice for guiding users to exercise with
  the right muscles, and asking what best practices could improve the project.
- Trigger type: explicit maintainer request and contributor observation.
- Scope: exercise-page muscle guidance, muscle-attention images, and project
  improvement direction after the rowing-machine implementation.
- Evidence in scope:
  - `exercises/rowing-machine.md`
  - `specs/rowing-machine-basics-and-beginner-workouts.md`
  - `specs/rowing-machine-basics-and-beginner-workouts.test.md`
  - `specs/exercise-image-standard.md`
  - `docs/templates/exercise-card.md`
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/verify-report.md`
  - `media/PROVENANCE.md`
  - Existing exercise pages and tests surfaced by bounded `rg` scans for
    `Muscles involved`, `Used muscles`, and muscle-attention media.
- Explicit exclusions:
  - No immediate spec, template, checker, media-standard, or exercise-page
    content change in this learn session.
  - No claim that every exercise page must change from this session alone.
  - No PR readiness, verification readiness, CI status, or merge-readiness claim.
  - No anatomy, diagnosis, treatment, rehab, or individualized coaching rule.
- Prior learnings reviewed:
  - `docs/learn/topics/content-quality.md`
  - `docs/learn/sessions/2026-06-29-responsible-breadth-content-quality.md`
  - `docs/learn/sessions/2026-06-29-building-block-view-best-practices.md`
- Session record path:
  `docs/learn/sessions/2026-07-04-muscle-guidance-best-practices.md`

## Observe

- OBS-001: The rowing-machine page makes muscle guidance more actionable by
  tying muscle groups to movement roles: legs and glutes start the drive, trunk
  transfers posture and force, and upper back/lats/arms finish the pull.
- OBS-002: The rowing spec already contains a strong boundary for this pattern:
  R13 requires broad beginner muscle engagement, while R14 prevents precise
  activation, diagnosis, treatment, or correction claims.
- OBS-003: The exercise-image standard already supports one
  `exercise_muscle_attention_illustration` per exercise when the image remains
  broad, support-only, unlabeled, local, provenance-backed, and subordinate to
  Markdown.
- OBS-004: Existing exercise pages are not fully uniform. Some use
  `## Muscles involved`, older pages use `## Used muscles`, and the amount of
  action-oriented muscle guidance varies by page generation.
- OBS-005: Current evidence supports a promising project direction, but not a
  durable lesson that should be encoded directly into `docs/learn/topics/`.
  The strongest route is a future proposal/spec/template amendment for exercise
  muscle guidance.

## Classify

| Observation | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
| --- | --- | --- | --- | --- | --- |
| OBS-001 to OBS-003 | observation | observation | session record only | Maintainer observation and rowing change evidence | The rowing page shows a useful pattern and existing specs already support it, but this is still one completed feature slice rather than accumulated cross-page evidence. |
| OBS-004 | direction | direction | future proposal/spec/template amendment | Maintainer request asks how to improve the project | Normalizing exercise muscle guidance changes the exercise-page contract and should be proposed, specified, and reviewed rather than added as learn-topic policy. |
| OBS-005 | no-durable-lesson | no-durable-lesson | none | Learn skill evidence standard | The session lacks repeated review findings or broad beginner-reader evidence proving that a new durable rule should be captured now. |

## Route

- No topic file was added or changed.
- No spec, template, architecture, ADR, workflow, checker, media, or exercise
  content artifact was changed.
- Follow-up candidate: create a proposal for an exercise-page muscle guidance
  standard after the current rowing-machine PR is reviewed or merged.

## Best Practices Candidate

These are recommended project improvements to evaluate in a future proposal:

1. Make muscle guidance role-based, not just a muscle list.
   - Name what each muscle group helps do in the movement.
   - Example pattern: driver, posture/transfer, finish/control, stabilizer.

2. Keep muscle guidance beginner-readable.
   - Prefer common wording like legs, glutes, trunk, upper back, lats, and arms.
   - Add technical names only when they genuinely help and are source-supported.

3. Tie muscles to the movement phases.
   - For multi-phase movements, explain which muscle groups matter in setup,
     drive, pull, hold, return, or recovery.
   - This worked well on the rower because the muscle section reinforces the
     stroke sequence instead of sitting apart from it.

4. Pair `## Muscles involved` with `## What you should feel`.
   - `Muscles involved` tells the reader where attention belongs.
   - `What you should feel` turns that into practical body awareness.
   - Keep both broad and non-diagnostic.

5. Name common compensation patterns carefully.
   - Say what beginners often overuse or rush only when it is directly useful.
   - Avoid implying that a reader has a dysfunction or injury.

6. Keep exact instruction in Markdown.
   - Muscle-attention images should support the section, not replace it.
   - Nearby Markdown should carry muscle names, cues, caveats, and citations.

7. Use at most one muscle-attention image per exercise.
   - Use it when muscle targeting or attention is hard to understand from text.
   - Keep the highlight broad, unlabeled, non-clinical, and visually reviewed.

8. Source muscle claims page-locally.
   - Broad muscle roles still need source support when they are exercise claims.
   - Manual source audit should sample muscle wording alongside setup,
     technique, feel cues, common mistakes, and safety.

9. Normalize section naming in a future spec.
   - Prefer `## Muscles involved` for current and future exercise pages.
   - Decide whether older `## Used muscles` pages should migrate in a focused
     compatibility-safe slice.

10. Add validation only after the contract is accepted.
    - A checker could require the section on new exercise pages, reject precise
      activation or clinical wording, and enforce support-only image rules.
    - That should come after a proposal/spec/template update, not from this
      learn session alone.

## Suggested Follow-Up Proposal Shape

Potential proposal title:
`Exercise Muscle Guidance Standard`

Potential scope:

- Define the expected `## Muscles involved` section for exercise pages.
- Require broad, role-based muscle guidance for new or substantially revised
  exercise pages.
- Preserve Markdown as source of truth for muscle guidance.
- Reuse the exercise-image standard for optional muscle-attention images.
- Decide whether and how to migrate older `## Used muscles` pages.
- Add focused tests only after the contract is approved.

Potential non-goals:

- No exact activation percentages.
- No individualized cueing.
- No diagnosis, rehab, corrective-exercise promises, or treatment claims.
- No anatomy-diagram source of truth.
- No blanket requirement that every page must have a muscle image.

## Validation

- `rg` evidence scan over specs, exercises, tests, and `media/PROVENANCE.md`
  found existing muscle sections, existing `Used muscles` legacy sections,
  current image-standard support, and rowing-specific R13/R14 requirements.
- No code, content page, spec, architecture, workflow, media, or policy artifact
  changed.
- This session record was written as a learning artifact only.
