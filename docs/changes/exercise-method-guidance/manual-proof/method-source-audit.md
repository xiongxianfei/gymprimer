# M4 Method Source Audit

## Scope

- Change ID: `exercise-method-guidance`
- Milestone: M4
- Proof ID: EMG-M1
- Pages checked: the six proof-slice exercise pages from R28 and R29.
- Criteria: each active method type has source-supported amount, effort, rest, progression, stop, and non-prescription wording.
- Audit date: 2026-07-04
- Auditor role: implementation reviewer using the approved spec and test spec.
- Source access: page-local source links and current public source pages were checked where available; no private or reader-specific data was used.

## Result

Pass for M4 implementation handoff.

All six active method types have one sampled page in the proof slice. The sampled concrete method claims use page-local sources, and the wording is static educational guidance rather than personalized programming.

## Checks

| Method type | Page | Method claims sampled | Page-local source support | Non-prescription result | Result |
| --- | --- | --- | --- | --- | --- |
| `dynamic_resistance` | `exercises/chest-press.md` | 1-3 easy sets of 8-15 controlled reps; stop with controlled reps still available; 60-120 seconds rest; add reps before small load increases; stop when control breaks. | `mayo-weight-training` supports comfortable 12-15 starting reps, proper form, controlled movement, stopping for pain, and reducing load/reps when form fails; `acsm-resistance-training` supports consistency, simple resistance training, and variable progression. | Uses "try" and controlled-form boundaries; does not adapt to reader symptoms, goals, or training response. | pass |
| `bodyweight_progression` | `exercises/incline-push-up.md` | 1-3 easy sets of 5-12 controlled reps; choose a surface high enough for a steady body line; about 60 seconds rest; lower the hand surface only after repeatable control; stop when setup or form fails. | `mayo-weight-training` supports proper form, controlled movement, comfortable starting load, and lowering difficulty when form cannot be kept; `acsm-resistance-training` supports bodyweight exercise as effective resistance training and simple progression. | Frames incline height as a general control cue, not an individualized plan. | pass |
| `low_load_control_drill` | `exercises/chin-nod.md` | 1-3 short practice sets of 6-10 slow reps; low effort; rest as needed; progress by smoother control; stop for head tipping, jaw tension, shoulder shrugging, or unsafe symptoms. | `local-chin-nod-instruction` supports small chin retraction, straight neck/back, no head tipping, repeatable reps, and seeking advice if painful; `acsm-resistance-training` supports consistency over complex progression; `nhs-neck-pain` supports safety routing for neck symptoms. | Keeps the drill as low-load practice and avoids posture-correction promises or treatment language. | pass |
| `isometric_hold` | `exercises/plank.md` | 2-3 holds of 10-30 seconds; use a knee plank or shorter hold if shape changes; breathe normally; rest 45-60 seconds; add seconds before harder variation; stop when bracing, posture, or breathing fails. | `mayo-weight-training` supports proper form, breathing while lifting/holding effort, controlled difficulty, and reducing reps/load when form cannot be kept. The timed hold range follows the approved editorial default shape for isometric holds and remains conservative. | Uses starter language and form-quality stop cues; does not prescribe a personal routine. | pass |
| `mobility_drill` | `exercises/thoracic-extension.md` | 1-2 sets of 6-10 slow reps; easy controlled range; rest until gentle reps are possible; progress by smoother control or a brief comfortable pause; stop for forced neck movement, unstable chair, or unsafe symptoms. | `local-thoracic-extension-instruction` supports sitting upright, extending over a chair, holding briefly, and returning upright; `acsm-resistance-training` supports simple gradual progression; `nhs-neck-pain` supports safety routing for neck symptoms. | Presents a mobility option and explicitly avoids forcing end range or treating posture. | pass |
| `stretch_hold` | `exercises/kneeling-hip-flexor-stretch.md` | 1-2 holds of about 20-30 seconds per side; mild stretch; relaxed effort and normal breathing; no bouncing; back off for pain, sharpness, worsening, or low-back movement. | `mayo-stretching` supports gentle stretching, no bouncing, holding stretches for about 30 seconds, and avoiding pain; page-local `mayo-weight-training` supports controlled technique and stop/back-off framing for unsafe symptoms. | Uses "try" and mild effort language; does not claim treatment or correction. | pass |

## Source Support Notes

- Mayo Clinic weight-training guidance was checked for beginner starting load, controlled form, breathing, rest, and stop/reduce-difficulty guidance.
- Mayo Clinic stretching guidance was checked for gentle effort, no bouncing, about-30-second holds, and avoiding pain.
- ACSM resistance-training guidance was checked for the broad consistency-over-complexity framing and support for simple resistance training using bodyweight, bands, machines, or free weights.
- CUH neck exercise guidance was checked for chin retraction setup, small controlled motion, repeat wording, and seeking professional advice if exercises are painful.
- Physitrack thoracic-extension guidance was checked for seated chair setup, upper-back extension over the chair, brief hold, and return to upright.
- NHS neck-pain guidance was checked for symptom safety routing and professional-care boundaries.

## Residual Risk

This is a bounded manual source audit, not a full clinical review. It checks whether the proof-slice method guidance is reasonably supported by page-local public sources and stays within the approved beginner-education scope. Any later edit to proof-slice method wording, source citations, starter ranges, stop guidance, or method type assignment must rerun EMG-M1.
