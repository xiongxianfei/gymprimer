# M2 Source Audit: Advanced Rowing Markdown Content

Date: 2026-07-07
Milestone: M2. Advanced Rowing Markdown Content
Scope: `exercises/rowing-machine-advanced.md`, beginner-page link, and reused source IDs in `SOURCES.md`

## Method

I checked the advanced page's concrete claims against page-local sources before M2 handoff.
This audit is bounded to Markdown content; generated media, prompt records, provenance, visual-safety review, grayscale review, and reader comprehension proof remain in later milestones.

## Audit Results

| Claim area | Page claim checked | Source support | Result |
|---|---|---|---|
| Damper vs drag factor | Damper changes flywheel feel; drag factor is the more comparable measured value across machines. | Concept2 damper setting and drag factor guidance. | Pass |
| Damper 10 boundary | Damper 10 is not proof of strength or better rowing; start around 3-5 while technique is the priority. | Concept2 damper setting and drag factor guidance. | Pass |
| PM5 metrics | PM5 concepts include pace, watts, stroke rate, distance/time, and force curve. | Concept2 PM5 how-to guide and Understanding the PM5. | Pass |
| Split and watts | Pace per 500m is a pace measure; watts represent power output. | Concept2 PM5 how-to guide. | Pass |
| Stroke rate | Stroke rate is strokes per minute; higher rate is not automatically higher intensity or better quality. | Concept2 stroke-rate explanation. | Pass |
| Rhythm and recovery | Drive/recovery rhythm uses a stronger drive and more controlled recovery; British Rowing supports recovery taking about twice the drive phase. | Concept2 PM5 how-to guide and British Rowing technique guide. | Pass |
| Force curve | Force curve is feedback for power application, not a form verdict. | Concept2 PM5 how-to guide. | Pass |
| Workout types | Steady rows, rate ladders, power-per-stroke work, intervals, and benchmark preparation are static examples, not a plan. | Concept2 Workout of the Day, Concept2 2k plan, Concept2 stroke-rate explanation, British Rowing technique guide. | Pass |
| Interval rest | Rest can be very easy rowing in official Concept2 examples. | Concept2 Understanding the PM5 and Concept2 2k plan. | Pass |
| Benchmark boundary | Benchmark preparation links to official Concept2 plan material instead of writing a full schedule. | Concept2 2k plan. | Pass |
| Force-intensity accessibility | Color must not be the only way information is conveyed. | W3C Use of Color guidance. | Pass |
| Safety routing | Chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, worsening symptoms, and painful technique route away from exercise education. | Mayo Clinic heart attack symptoms, Mayo Clinic exercise and arthritis pain guidance, Mayo Clinic weight training technique guidance. | Pass |

## Scope Notes

- The advanced page keeps examples static and does not calculate personal paces, watts, targets, or outcomes.
- The page uses `basic_cardio_equipment` and does not introduce a new method subtype.
- The page does not reference generated media paths yet; M3 owns image assets, prompt packets, provenance, and visual review.
- The beginner page keeps its existing beginner tutorial and adds only the companion-page navigation link.

## Validation Evidence

Initial targeted real-page tests failed before implementation because `exercises/rowing-machine-advanced.md` and the beginner-page link were missing.
After implementation, the targeted real-page tests and scoped Markdown-first check passed.
