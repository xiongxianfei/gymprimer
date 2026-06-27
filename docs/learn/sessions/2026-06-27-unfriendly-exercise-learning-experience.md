# Learn Session: Unfriendly Exercise Learning Experience

## Frame

- Trigger: explicit `$learn` invocation stating that users cannot easily learn how to exercise from GymPrimer and that the experience is unfriendly.
- Trigger type: explicit maintainer/user request.
- Scope: product and UX learning direction for making GymPrimer easier for beginners to use for exercise literacy.
- Evidence in scope:
  - `VISION.md`
  - `README.md`
  - `docs/proposals/2026-06-26-beginner-fitness-exercise-education-platform.md`
  - `specs/content-schema.md`
  - `docs/architecture/system/architecture.md`
  - `docs/plans/2026-06-26-content-schema-foundation.md`
  - `docs/learn/sessions/2026-06-27-back-running-injury-learning-paths.md`
  - External reference points: CDC plain-language guidance, W3C WCAG 2.2, Nielsen Norman Group usability heuristics, and beginner exercise-safety references already used by the proposal and prior learn session.
- Explicit exclusions:
  - No frontend implementation.
  - No content-schema change.
  - No new exercise cards.
  - No workout prescription, personalization, diagnosis, rehab, or AI coaching.
  - No authoritative topic file update.
- Prior learnings reviewed:
  - `2026-06-27-back-running-injury-learning-paths.md` already records that back, running, and safety learning should become future beginner learning paths rather than immediate source-of-truth content changes.
- Session record path: `docs/learn/sessions/2026-06-27-unfriendly-exercise-learning-experience.md`

## Observe

- OBS-001: The current README says the repository contains the vision, content-schema artifacts, validation tools, and generated-output evidence. It also says the project does not yet contain a frontend, CMS, public exercise library, or public runtime API.
- OBS-002: The generated public package currently contains one reviewed example card and is explicitly described as evidence for the schema and validation workflow, not a launch library.
- OBS-003: The vision defines GymPrimer's user-facing success by beginner comprehension: after reading a card, a beginner should be able to explain what the exercise trains, setup, first movement phase, what they should feel, one common mistake, and when to stop.
- OBS-004: The accepted proposal already rejects a passive static encyclopedia as the full product direction because it is weak for beginner uncertainty, equipment setup, and comprehension checks.
- OBS-005: The accepted proposal recommends a guided comprehension layer: search, equipment lookup, "what should I feel?" checks, short quizzes, and beginner-readable readiness cues.
- OBS-006: The approved content schema includes discovery and learning hooks: cards must be discoverable by equipment, exercise name, aliases, movement pattern, muscle, and difficulty; it should support card relationships and comprehension-check prompts.
- OBS-007: The content-schema spec explicitly does not define frontend page layout, search UI, quizzes, learning paths, or analytics UI. It lists a UX/search spec as a follow-on artifact.
- OBS-008: The active implementation plan intentionally excludes frontend, search UI, glossary UI, quizzes, analytics, CMS integration, hosting, and AI. This means an unfriendly current experience is expected for the current foundation stage, but it is not acceptable for a future user-facing release.
- OBS-009: External UX and health-literacy guidance aligns with a future GymPrimer UX direction: use plain language, meet accessibility requirements, give users clear system status and recognition-based navigation, and test whether real beginners can complete the core learning tasks.

## External References Checked

- CDC, "Plain Language Materials & Resources": https://www.cdc.gov/health-literacy/php/develop-materials/plain-language.html
- W3C, "Web Content Accessibility Guidelines (WCAG) 2.2": https://www.w3.org/TR/WCAG22/
- Nielsen Norman Group, "10 Usability Heuristics for User Interface Design": https://www.nngroup.com/articles/ten-usability-heuristics/
- Mayo Clinic, "Weight training: Do's and don'ts of proper technique": https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842

## Classify

| Observation | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
| --- | --- | --- | --- | --- | --- |
| OBS-001 to OBS-009 | direction | direction | future proposal/spec for beginner-facing UX, search, equipment lookup, learning paths, comprehension checks, and usability testing | Explicit user request; existing proposal/spec/architecture already identify UX/search as a follow-on artifact | The evidence supports a product direction and future artifact, not an implementation-ready task or durable internal workflow lesson. Current unfriendly experience follows from the deliberate foundation-only scope, but a future user-facing release needs a dedicated UX/search spec. |

## Route

- No topic file was created. This is direction for a future product artifact, not a contributor-confirmed durable lesson.
- No proposal, spec, architecture, content card, schema, validator, or UI code was changed.
- Recommended follow-up: create a proposal or spec for "Beginner Exercise Learning Experience" before implementation.

## Best-Practice Direction For The Project

The future user-facing experience should be designed around the beginner's jobs to be done:

1. Identify the machine, movement, or body area they are trying to understand.
2. Quickly learn what the exercise is for and whether it is appropriate for a beginner.
3. Set up the equipment without guessing.
4. Follow the movement in a small number of visible phases.
5. Self-check what they should feel and what they should not feel.
6. Notice common mistakes and choose an easier version when needed.
7. Know when to stop and seek qualified help.
8. Confirm comprehension before progressing.

Recommended UX principles:

- Lead with task-based entry points: search by machine name, equipment photo label, muscle/body area, movement pattern, and beginner goal.
- Render cards as guided learning flows, not raw encyclopedia pages: purpose, setup, start position, step cards, feel cues, mistakes, regression, safety, and a short check.
- Use progressive disclosure: show the next action first, with deeper anatomy, review metadata, and glossary details available but not blocking the first read.
- Make setup visually dominant for machine cards, because equipment uncertainty is one of the core beginner problems.
- Treat "what should I feel?", "what should I not feel?", and "when should I stop?" as first-class UI sections, not footnotes.
- Add beginner pathways such as first gym machines, back basics, push basics, leg machines, treadmill basics, and safety literacy.
- Add comprehension checks that map directly to the vision's falsifiability questions.
- Keep all safety language plain, conservative, and non-diagnostic.
- Make canonical SVG step cards accessible with localized text alternatives and keyboard/screen-reader support.
- Test with people in their first ninety days of regular gym training, using realistic prompts such as "find how to use this machine" and "tell me when you would stop."

## No Durable Lesson Rationale

This session captures a maintainer-stated product concern plus supporting project evidence. It does not show repeated production incidents, recurring failed reviews, or an accepted UX decision artifact. Therefore it should not update `docs/learn/topics/` or become policy by itself.

## Validation

- Session file created by direct inspection and evidence review.
- No code, schema, validator, generated output, or content card changed.
