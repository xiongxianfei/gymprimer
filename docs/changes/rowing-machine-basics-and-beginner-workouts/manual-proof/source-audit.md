# Source Audit: Rowing Machine Basics and Beginner Workout Guidance

## Status

pass

## Scope

- Change ID: `rowing-machine-basics-and-beginner-workouts`
- Milestone: M3
- Proof ID: RMB-M1
- Audited page: `exercises/rowing-machine.md`
- Audit date: 2026-07-04
- Auditor: implementation agent
- Privacy: no private reader, health, contact, or training-log data recorded

## Method

Checked the final M2 page against page-local source references, `SOURCES.md`,
and the cited public source pages. This audit verifies semantic source support;
it does not replace the automated Markdown-first source and privacy checks.

## Claim Audit

| Claim category | Page claim location | Cited support | Disposition |
| --- | --- | --- | --- |
| Technique-first framing | `## Before you start`; `## What this is for` | Concept2 indoor rowing technique says beginners should not pull too hard until comfortable with technique fundamentals. | supported |
| Foot setup | `## Equipment setup` | Concept2 RowErg foot-position guidance supports the strap crossing the ball or widest part of the foot. | supported |
| Catch range and posture | `## Equipment setup`; `### 1. Catch` | Concept2 indoor rowing technique supports arms long, neutral head, relaxed shoulders, long spine, and shins vertical or as close as comfortable. | supported |
| Stroke sequence | `## Movement breakdown`; `### 2. Drive`; `### 4. Recovery` | Concept2 indoor rowing technique supports drive as legs, body, arms and recovery as arms, body, legs. | supported |
| Damper meaning | `## Before you start`; `## Common mistakes` | Concept2 damper guidance supports damper as flywheel feel, not a proof of work; the rower creates work through stroke effort. | supported |
| Muscles involved | `## Muscles involved` | Concept2 muscles-used guidance supports broad leg, glute, trunk/core, back, and arm involvement through the rowing stroke. | supported after M3 page-local citation was added |
| Beginner method | `## How much to do` | Concept2 getting-started workouts supports short beginner rows, breaks, easy starts, and repeat rounds when the beginner feels good. | supported |
| Static examples | `## How much to do` | Concept2 getting-started workouts supports short easy rows and simple intervals as examples. The page frames them as examples, not a schedule or plan. | supported |
| Weekly activity | `## How much to do` | CDC and WHO adult activity guidance support aerobic activity plus muscle-strengthening activity on at least two days per week. | supported |
| Cardiopulmonary stop conditions | `## Safety notes` | Mayo Clinic heart-attack symptoms reference supports chest pain, shortness of breath, dizziness/lightheadedness, and feeling like passing out. | supported |
| Pain, worsening symptoms, and numbness | `## Safety notes` | Mayo Clinic exercise-pain guidance supports taking a break for pain and caution for sharp or worsening pain. NHS back-pain guidance supports urgent routing for quickly worsening severe pain and numbness-related red flags. | supported |
| Painful or uncontrolled technique | `## Safety notes`; `Stop condition` | Mayo Clinic weight-training guidance supports proper form, controlled movement, lowering intensity when form cannot be kept, and stopping exercise that causes pain. | supported |
| Source index discipline | `## Sources`; `SOURCES.md` | Reused source IDs `nhs-back-pain` and `mayo-weight-training` appear in `SOURCES.md`; page-local `local-rowing-machine-*` IDs remain page-local. | supported |

## Result

Every audited claim category is supported by a page-local citation, narrowed to
the cited source, or covered by existing global source-index rules. No source
gap blocks promotion from M3 to M4.

## Re-Run Trigger

Re-run this audit after any edit to setup, stroke sequence, damper, method
examples, weekly activity, stop conditions, muscle wording, source IDs, or cited
source entries.
