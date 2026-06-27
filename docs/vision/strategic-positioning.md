# Strategic positioning

This document records the strategic-positioning pass that produced `VISION.md`. It supports the vision as rationale and is not independently authoritative. If this document and `VISION.md` ever conflict, either update this rationale or revise the vision through a substantive update.

## Category

Open-source educational reference for gym beginners — a reviewed, community-maintained exercise primer. Not a workout app, not a coaching platform, not a personalization engine, not a clinical product.

## Primary user

Adults in their first ninety days of regular gym training, or returning after a year or more away from training. Launch content is English-first, with Chinese treated as a first-class future locale in the content model.

## Primary pain

Existing resources do not teach in the order a beginner needs. Videos show movement but skip equipment setup and beginner cues. Databases list muscles without explaining how to use the machine. Workout apps prescribe sets and reps before the user understands the exercises being prescribed. AI assistants generate confident but unreliable safety guidance. Personal trainers are excellent but scarce and expensive.

## Primary promise

For every common machine and movement, give the beginner a reviewed, plain-language card that explains what it trains, how to set it up, how to perform it phase by phase, what to feel, what to avoid, and when to stop.

## Core mechanism

A locale-aware, schema-driven content repository of reviewed exercise cards, version-controlled in Git and licensed Apache 2.0, with no AI-generated content in the source of truth. Reviewer name and review date are visible in every entry. Review is tiered by content risk: trainers or strength coaches clear cards, physical therapists review safety and pain-language policy, and sports medicine clinicians advise on disclaimers, emergency criteria, and elevated-risk cards. Illustrated SVG step cards are the canonical movement media. Equipment-anchored discovery lets a beginner find a card by the machine they are standing in front of.

## Alternatives

- YouTube and short-form video fitness content
- Exercise databases such as ExRx and Muscle&Strength
- Workout-tracking and prescription apps such as Fitbod, Strong, Hevy
- AI-coaching apps such as Future and Caliber
- General-purpose AI chatbots used as ad-hoc fitness advisors
- In-person personal trainers

## Tradeoff

Comprehension over prescription. Correctness on forty to sixty reviewed exercises over shallow coverage of hundreds. English launch velocity plus locale-aware structure over a bilingual launch that doubles review burden before the schema stabilizes. Tiered review over a flat review board. SVG illustrations as canonical source over expensive or hard-to-license launch video. Open shared content over AI-personalized content.

## Compatibility surfaces

GitHub hosting, Apache 2.0 license, Markdown-and-YAML content schema, locale-keyed fields, CMS workflow, SVG illustration style guide, web frontend, and a possible future constrained AI-assistance layer that retrieves only from reviewed content. These are implementation choices, not the project category — the project would still be GymPrimer on a different stack.

## Refusals

Workout prescription, AI-generated advice as source of truth, community video as source of truth, launch-required bilingual cards, injury diagnosis, active rehabilitation content, sport-specific programming, personalized workout plans, advanced programming for athletes.

## Falsifiability

A beginner who reads a card but cannot correctly explain what the exercise trains, how to set up the equipment, what the first movement phase is, what to feel, one common mistake, and when to stop — that indicates a failed card. A pattern of such failures across the library, a stale review queue, a schema that cannot add Chinese without migration, SVG steps that fail beginner comprehension, or contributor drift toward prescription indicates project failure.
