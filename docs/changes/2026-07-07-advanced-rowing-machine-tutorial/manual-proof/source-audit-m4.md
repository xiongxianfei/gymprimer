# M4 Source Audit: Advanced Rowing Final Proof

Date: 2026-07-07
Milestone: M4. Manual Proof, Review Evidence, and Closeout Preparation
Scope: `exercises/rowing-machine-advanced.md`, page-local source claims, source-index reuse, and media-adjacent explanatory text

## Method

I rechecked the completed advanced rowing page after M3 media integration.
The audit focused on claims that need source support or safety boundaries:
damper, drag factor, monitor metrics, stroke rate, force curve, rhythm, workout examples, benchmark boundaries, force-intensity accessibility, and safety routing.

This audit does not use generated images as source authority.
Images are treated as support artifacts; Markdown and citations remain the source of truth.

## Audit Results

| Claim area | Final page claim checked | Source support | Result |
| --- | --- | --- | --- |
| Damper and drag factor | Damper changes flywheel feel; drag factor is the more comparable measured flywheel value; damper 10 is not proof of strength or better rowing. | [Concept2 damper setting and drag factor guidance][concept2-advanced-damper-drag-factor]. | Pass |
| Monitor metrics | Split or pace per 500m, watts, stroke rate, distance/time, and force curve are monitor concepts, not personal prescriptions. | [Concept2 PM5 how-to guide][concept2-pm5-how-to-use] and [Understanding the PM5][concept2-understanding-pm5]. | Pass |
| Stroke rate | Stroke rate is strokes per minute; higher rate is not automatically higher quality or intensity. | [Concept2 stroke-rate explanation][concept2-stroke-rate-explained]. | Pass |
| Rhythm and recovery | The page describes a decisive drive with controlled recovery and cites the drive/recovery timing concept. | [Concept2 PM5 how-to guide][concept2-pm5-how-to-use] and [British Rowing technique guide][british-rowing-technique]. | Pass |
| Force curve | Force curve is feedback for power application, not a form verdict or clinical ruling. | [Concept2 PM5 how-to guide][concept2-pm5-how-to-use]. | Pass |
| Workout examples | Steady rows, rate ladders, power-per-stroke work, intervals, and benchmark preparation are static examples, not a plan. | [Concept2 Workout of the Day][concept2-workout-of-day], [Concept2 2k plan][concept2-2k-plan], [Concept2 stroke-rate explanation][concept2-stroke-rate-explained], and [British Rowing technique guide][british-rowing-technique]. | Pass |
| Interval rest | The page uses very easy rowing as a static rest example. | [Concept2 Understanding the PM5][concept2-understanding-pm5] and [Concept2 2k plan][concept2-2k-plan]. | Pass |
| Benchmark boundary | Benchmark preparation points to official Concept2 planning material instead of writing a full schedule. | [Concept2 2k plan][concept2-2k-plan]. | Pass |
| Force-intensity accessibility | Color is not the only meaning channel; overlays use Markdown legend, alt text, outlines, texture, phase explanation, and grayscale review. | [W3C Use of Color guidance][w3c-use-of-color] plus the M3 grayscale proof listed in the validation ledger. | Pass |
| Safety routing | Chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, worsening symptoms, painful technique, and clinician-directed restrictions route away from the tutorial. | [Mayo Clinic heart attack symptoms][mayo-heart-attack-symptoms], [exercise and arthritis pain guidance][mayo-exercise-arthritis-pain], [exercise and chronic disease guidance][mayo-exercise-chronic-disease], and [weight-training technique guidance][mayo-weight-training]. | Pass |

## Source Index Check

The page uses page-local source definitions and the reused advanced-rowing source IDs are present in `SOURCES.md` under the repository's current source-index rules.

## Scope Check

- No personalized paces, watts, weekly schedules, adaptive progression, or benchmark outcome is calculated.
- No race strategy, competition programming, active recovery protocol, treatment plan, injury-specific protocol, or return-to-rowing protocol is introduced.
- No runtime product, hosted app, calculator, tracker, wearable integration, PM5 data-analysis app, video product, or coaching engine is introduced.
- The method label remains `basic_cardio_equipment`; no `advanced_basic_cardio_equipment` subtype is introduced.

## Disposition

The completed advanced rowing page remains source-backed and within the approved static-literacy scope.

## Sources

[concept2-advanced-damper-drag-factor]: https://concept2.com/training/articles/damper-setting
[concept2-pm5-how-to-use]: https://concept2.com/support/monitors/pm5/how-to-use
[concept2-understanding-pm5]: https://concept2.com/training/articles/understanding-pm5
[concept2-stroke-rate-explained]: https://concept2.com/blog/rowing-stroke-rate-explained
[concept2-workout-of-day]: https://concept2.com/training/wod
[concept2-2k-plan]: https://concept2.com/training/plans/2k-erg-test-12-week
[british-rowing-technique]: https://www.britishrowing.org/indoor-rowing/go-row-indoor/how-to-indoor-row/british-rowing-technique/
[w3c-use-of-color]: https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html
[mayo-heart-attack-symptoms]: https://www.mayoclinic.org/diseases-conditions/heart-attack/in-depth/heart-attack-symptoms/art-20047744
[mayo-exercise-arthritis-pain]: https://www.mayoclinic.org/diseases-conditions/arthritis/in-depth/arthritis/art-20047971
[mayo-exercise-chronic-disease]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-and-chronic-disease/art-20046049
[mayo-weight-training]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842
