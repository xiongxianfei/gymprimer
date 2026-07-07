# Safer Running Beginner Comprehension Proof

## Status

pass

## Scope

- Change ID: `2026-07-06-safer-running-basics-and-running-images`
- Milestone: M4
- Proof ID: MP3
- Audited page: `exercises/safer-running-basics.md`
- Audited images:
  - `media/exercises/safer-running-basics/posture.png`
  - `media/exercises/safer-running-basics/landing.png`
  - `media/exercises/safer-running-basics/run-walk.png`
  - `media/exercises/safer-running-basics/warm-up.png`
  - `media/exercises/safer-running-basics/muscle-attention.png`
  - `media/exercises/safer-running-basics/overstride-comparison.png`
- Audit date: 2026-07-07
- Method: non-identifying reviewer simulation of a beginner read test
- Privacy: no private reader, health, contact, location, route, pace, or training-log data recorded

## Method

Reader profile: beginner-oriented content read-through using the MP3 prompts from `specs/safer-running-basics-and-running-images.test.md`.

Result scale:

- `clear`: the page and image set give enough direct wording or visual support to answer the prompt.
- `partial`: the page and image set give some answer but need a wording or image fix.
- `unclear`: the page and image set do not answer the prompt.

## Prompt Results

| prompt | result | evidence | residual confusion |
|---|---|---|---|
| what the page can help them do | clear | The `## What this is for` section says the page helps beginners understand run/walk intervals, easy effort, rest days, gradual loading, and relaxed running form. | None identified. |
| whether the page can guarantee injury-free running | clear | The `## What this page cannot promise` section says no page can guarantee injury-free running. | None identified. |
| how to start a first running session | clear | The `## Warm up` and `## How much to do` sections describe 3-5 minutes of brisk walking or easy jogging, then 10-20 minutes total using short easy running with walking recovery. | None identified. |
| what run/walk means | clear | The `## How much to do` section says to alternate short easy running with walking recovery, and `media/exercises/safer-running-basics/run-walk.png` makes the alternation visible. | None identified. |
| what effort should feel like | clear | The `## What you should feel` section says effort should feel warm and slightly out of breath, not panicked or strained, with short-sentence speech still possible. | None identified. |
| what the posture image teaches | clear | `media/exercises/safer-running-basics/posture.png` shows tall posture and relaxed arm swing, while Markdown keeps exact form cues as the source of truth. | None identified. |
| what the landing image teaches | clear | `media/exercises/safer-running-basics/landing.png` shows the foot close to the body and a short quiet stride without prescribing one required foot strike. | None identified. |
| what would make them stop or seek help | clear | The safety-facing text routes chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, weakness, worsening symptoms, persistent pain, or symptoms that do not settle to the central `RED-FLAGS.md` path and appropriate professional guidance. [Mayo Clinic][mayo-exercise-chronic-disease] | None identified. |
| images helped more than text alone | clear | The six images make posture, landing, run/walk structure, warm-up sequence, broad body-region attention, and overstride contrast visible while Markdown remains authoritative for effort, progression, muscles, and safety wording. | None identified. |

## Disposition

The safer-running page and six first-batch images pass the M4 beginner-comprehension prompt check.

No wording or image replacement is required from this read-through.

## Residual Risk

This proof avoids private reader details and records only prompt outcomes.
It is a static reviewer simulation, not live usability research, and it does not replace future public-reader feedback after publication.

## Sources

- [Safer Running Basics and High-Quality Running Images spec](../../../../specs/safer-running-basics-and-running-images.md)
- [Safer Running Basics and High-Quality Running Images test spec](../../../../specs/safer-running-basics-and-running-images.test.md)
- [Safer Running Basics page](../../../../exercises/safer-running-basics.md)
- [Mayo Clinic exercise and chronic disease guidance][mayo-exercise-chronic-disease]

[mayo-exercise-chronic-disease]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-and-chronic-disease/art-20046049
