# Learn Session: Back, Running, and Injury-Avoidance Learning Paths

## Frame

- Trigger: explicit `$learn` invocation asking for best practices for users to learn how to train their back, run effectively, and avoid injury through GymPrimer.
- Trigger type: explicit maintainer/user request.
- Scope: user-facing learning-path direction for back training, running education, and injury-avoidance behavior within the current GymPrimer product boundaries.
- Evidence in scope:
  - `VISION.md`
  - `docs/proposals/2026-06-26-beginner-fitness-exercise-education-platform.md`
  - `specs/content-schema.md`
  - `docs/plans/2026-06-26-content-schema-foundation.md`
  - `content/cards/examples/ex-lat-pulldown.json`
  - Prior learn session `docs/learn/sessions/2026-06-26-project-map-next-stage.md`
  - External reference points: CDC adult activity guidance, ACSM distance-running guidance, Mayo Clinic strength-training technique guidance, AAOS injury-prevention guidance.
- Explicit exclusions:
  - No workout prescription.
  - No rehab, diagnosis, pain-treatment, or injury-specific programming.
  - No authoritative topic file update.
  - No content-schema/spec/architecture change.
  - No new exercise card content.
- Prior learnings reviewed:
  - `2026-06-26-project-map-next-stage.md` captured a routing correction only; it does not already cover user learning-path direction.
- Session record path: `docs/learn/sessions/2026-06-27-back-running-injury-learning-paths.md`

## Observe

- OBS-001: GymPrimer's vision says the project teaches exercise literacy before workout prescription. A user should be able to explain what an exercise trains, setup, first movement phase, what to feel, one common mistake, and when to stop.
- OBS-002: The accepted proposal includes back-relevant exercises in the first content priorities, including lat pulldown, seated cable row, face pull, assisted pull-up, dumbbell row, and rowing-machine basics. It also includes treadmill basics and weekly aerobic/strength literacy.
- OBS-003: The current implementation contains one public example card, `ex-lat-pulldown`, which teaches a vertical pulling pattern and says it is for learning how to train the upper back. This can support back-exercise literacy, but not a complete back-training plan.
- OBS-004: The content schema already supports the fields needed for safe learning: equipment setup, start position, movement phases, breathing/bracing, what to feel, what not to feel, common mistakes, regressions, progressions, safety notes, stop signs, review metadata, and taxonomy fields for `pull_vertical`, `pull_horizontal`, `cardio_running`, `cardio_rowing`, and `cardio_cycling`.
- OBS-005: External guidance aligns with GymPrimer's current boundaries:
  - CDC adult guidance combines aerobic activity with at least two days of muscle-strengthening activity each week.
  - Mayo Clinic strength-training guidance emphasizes correct form, breathing, controlled movement, and avoiding excessive load.
  - ACSM distance-running guidance emphasizes gradual introduction of running habits and supporting running with strengthening, neuromotor exercise, foot strengthening, and mobility.
  - AAOS injury-prevention guidance emphasizes warm-up, appropriate equipment, hydration, and recovery.
- OBS-006: A safe GymPrimer learning path should teach users how to understand and self-check reviewed cards, not tell them exactly how much to train, diagnose pain, or promise injury prevention.

## External References Checked

- CDC, "Adult Activity: An Overview": https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
- Mayo Clinic, "Weight training: Do's and don'ts of proper technique": https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842
- ACSM, "Healthy Habits for Distance Running": https://acsm.org/distance-running-form-tips/
- AAOS OrthoInfo, "Safe Exercise": https://orthoinfo.aaos.org/en/staying-healthy/safe-exercise/

## Classify

| Observation | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
| --- | --- | --- | --- | --- | --- |
| OBS-001 to OBS-006 | direction | direction | future proposal/spec for beginner learning paths covering back basics, running basics, and safety literacy | Explicit user request for best practices; no request to alter authoritative artifacts yet | The observations identify a future product/content direction, not a repeated internal workflow failure or contributor-confirmed durable policy lesson. The right owner would be a proposal/spec before implementation. |

## Route

- No topic file was created. The evidence supports product/content direction, not a contributor-confirmed durable lesson.
- No proposal, spec, architecture, or content card was changed in this session.
- Recommended follow-up when the maintainer wants to act: create a proposal or spec for "Beginner Learning Paths" with at least three paths:
  - Back basics: vertical pull, horizontal pull, upper-back/scapular control, and common setup mistakes.
  - Running basics: walking/run-walk progression literacy, treadmill basics, effort language, warm-up/cool-down, cadence/form cues only at a beginner-safe level.
  - Safety literacy: stop signs, pain distinction language, warm-up, conservative progression, recovery, equipment/shoe fit, and professional-help prompts.

## Best-Practice Direction For The Project

Users should learn through GymPrimer in this order:

1. Learn the movement pattern before choosing volume or intensity.
2. Read the card's purpose, equipment setup, start position, and movement phases.
3. Use "what you should feel" and "what you should not feel" as self-checks.
4. Start with the easiest controlled version and low load or low running volume.
5. Progress only after the readiness cue is satisfied.
6. Stop and seek qualified help for sharp, radiating, worsening, unusual, chest-pain, dizziness, fainting, new numbness, or unusual shortness-of-breath symptoms.
7. Treat GymPrimer as education, not a medical, rehab, or personalized programming product.

## No Durable Lesson Rationale

This session captures a product/content direction from a maintainer prompt plus supporting evidence. It does not show repeated review findings, recurring incidents, failed validation patterns, or an accepted authoritative policy change. Therefore it should not update `docs/learn/topics/` or become workflow policy by itself.

## Validation

- Session file created by direct inspection and evidence review.
- No code, schema, validator, generated output, or content card changed.
