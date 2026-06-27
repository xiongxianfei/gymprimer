# GymPrimer

## Pitch

GymPrimer is an open-source educational reference for gym beginners. It gives each common machine and movement a reviewed, plain-language card that explains what the exercise trains, how to set up the equipment, how the movement works phase by phase, what the user should feel, what to avoid, and when to stop. It is the primer a beginner reaches for before any program tells them what to lift, maintained in public under Apache 2.0 so the content can be inspected, forked, translated, and improved.

## What makes this different

Existing fitness resources teach in the wrong order. Short-form videos show the movement but skip equipment setup and beginner cues. Exercise databases list muscles but do not teach a beginner how to set up a machine or what to feel. Workout apps prescribe sets and reps to users who do not yet understand the exercises being prescribed. AI assistants generate fluent answers that are often wrong about safety. Personal trainers are excellent but scarce and expensive.

GymPrimer is upstream of all of these. It treats exercise literacy as its own category, before workout prescription. Every card is a reviewable artifact rather than a generated answer. The project chooses depth, correctness, and review history over broad coverage: the first release is expected to cover roughly forty to sixty reviewed exercises, not hundreds. It also chooses illustrations as the canonical movement medium because they are reviewable in Git, accessible, language-neutral, and easier to keep consistent than launch-scale video.

## Who it is for

GymPrimer is for adults in their first ninety days of regular gym training, or returning after a year or more away, who feel lost around machines and free weights and want to understand the equipment before committing to a program. The launch audience is English-first, while the content model keeps Chinese as a first-class future locale. GymPrimer is also for the trainers, physical therapists, clinicians, content authors, illustrators, translators, and engineers who maintain the open content library together.

## Who it is not for

GymPrimer is not for advanced lifters seeking optimized programming, athletes preparing for sport-specific competition, patients in active rehabilitation, or users who want personalized workout plans. It is not a coach replacement or a substitute for medical advice. The first release will not serve these audiences, and the project will decline contributions that try to make it serve them.

## What it commits to

GymPrimer commits to a consistent card shape: equipment setup, movement phases, primary and secondary muscles, breathing and bracing cues, common mistakes, regressions, progressions, and safety notes. It commits to English cards at launch and a locale-aware schema from day one, so Chinese translation can become a contribution path without reworking the content model.

Every published card has expert review, a visible reviewer name, a review date, and public review history. Review is tiered by risk: certified trainers or strength coaches clear each card, physical therapists review safety language and pain guidance at the policy level, and sports medicine clinicians advise on disclaimers, emergency criteria, and elevated-risk cards. This keeps clinical judgment focused on guardrails without turning GymPrimer into a rehabilitation product.

GymPrimer commits to illustrated SVG step cards as canonical media, with three to six steps per card and accessible text alternatives. Community video can later supplement a stable card, but the illustration and reviewed text remain the source of truth. Content and code stay Apache 2.0 licensed. Discovery stays anchored to real gym equipment so a beginner can find guidance from the machine they are standing in front of.

## What it refuses to be

GymPrimer will not prescribe workouts, generate training plans, diagnose injuries, or replace medical advice. It will not publish AI-generated content or community video as a source of truth. It will not double the launch review burden by requiring bilingual cards before the English schema is stable. It will not trade correctness for breadth. It will not add advanced programming, sport-specific prescription, or active-rehab content until the literacy layer is stable, and possibly never. It will decline contributions that drift toward coaching, personalization, clinical guidance, or media production that cannot be reviewed and maintained in public.

## What would prove this wrong

The project has failed if a beginner who reads a card cannot, in their own words, explain what the exercise trains, how to set up the equipment, what the first movement phase is, what they should feel, one common mistake, and when to stop. It has also failed if the locale-aware schema cannot support Chinese without a content migration, if the review tiers blur clinical advice into routine coaching, if SVG cards cannot communicate movement clearly enough for beginner comprehension, if the review workflow cannot keep card content current, or if community contributions drift toward the prescriptive workout content that the refusals above forbid. Beginner comprehension testing, review-currency audits, and schema-localization checks are the checks that surface these failures.
