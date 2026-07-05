# Source Audit

## Scope

- Change ID: `exercise-muscle-guidance-standard`
- Milestone: M3
- Proof ID: XMG-M1
- Pages checked: `exercises/rowing-machine.md`, `exercises/chest-press.md`, `exercises/plank.md`, `exercises/chin-nod.md`, `exercises/thoracic-extension.md`, and `exercises/band-pull-apart.md`
- Criteria: sample at least one main-driver claim, one support-stabilizer claim, one feel-cue, one compensation-cue, and one safety-cue from the proof slice.
- Check date: 2026-07-04
- Auditor role: implementation reviewer using checked-in Markdown, page-local source definitions, and public source pages where reachable.
- Privacy statement: no reader identity, health history, symptoms, training logs, contact details, or private reviewer notes were collected.

## Result

Pass for M3 implementation handoff.

The sampled proof-slice claims use page-local source definitions and stay within broad beginner exercise literacy. No sampled claim relies only on `SOURCES.md`, exact activation percentages, EMG-as-instruction, diagnosis, treatment, individualized cueing, or posture-correction promises.

## Claim Samples

| page_path | claim_type | sampled claim | supporting_source | disposition | residual_risk |
| --- | --- | --- | --- | --- | --- |
| `exercises/rowing-machine.md` | main-driver | Drive: legs and glutes start the work by pushing through the footplates. | `local-rowing-machine-muscles`; `concept2-rowing-technique` | supported. Concept2 describes rowing as coordinated large-muscle action and describes the drive as starting with the legs. | low; source is rowing-specific and phase-specific. |
| `exercises/band-pull-apart.md` | support-stabilizer | Shoulder-girdle and arms help keep the band path near chest height. | `local-band-pull-apart-instruction` | supported as broad movement-control wording. The page keeps the claim practical and does not make an exact activation claim. | medium-low; source is an exercise-instruction page rather than a formal anatomy review. |
| `exercises/chin-nod.md` | feel-cue | You may feel light effort near the front of the neck or a mild stretch around the neck. | `local-chin-nod-instruction` | supported and softened. CUH describes chin retraction with a straight-backed setup, pulling the chin in, and feeling a neck stretch. | low; cue uses "may feel" and does not require an exact sensation. |
| `exercises/thoracic-extension.md` | compensation-cue | Pay attention to gentle upper-back motion rather than forcing the neck backward or arching the low back. | `local-thoracic-extension-instruction`; `mayo-weight-training` | supported as practical control wording. The page frames this as a mobility cue and not as strengthening or posture correction. | medium; Physitrack source was not fully retrievable through static tooling during this audit, so later human source review should re-check the source page before broad rollout. |
| `exercises/rowing-machine.md` | safety-cue | Stop for chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, worsening symptoms, numbness, or painful/jerky technique. | `local-rowing-machine-safety`; `local-rowing-machine-exercise-pain`; `nhs-back-pain`; `mayo-weight-training` | supported and conservatively routed to `RED-FLAGS.md`. Mayo and NHS sources support the symptom escalation and pain-stop boundary. | low; this is safety routing, not exercise substitution or diagnosis. |

## Disposition

- `main-driver`: pass.
- `support-stabilizer`: pass with residual source-specificity caution for future batches.
- `feel-cue`: pass.
- `compensation-cue`: pass with future re-check noted.
- `safety-cue`: pass.

## Source Support Notes

- Concept2 rowing sources were checked for the drive/recovery sequence and broad muscles used during the rowing stroke.
- CUH neck exercise guidance was checked for chin retraction setup, straight neck/back wording, stretch wording, and professional-care routing if exercises are painful.
- Mayo Clinic weight-training guidance was checked for controlled movement, form quality, breathing, balanced major muscle work, and stopping exercise that causes pain.
- `media/PROVENANCE.md` and page-local source definitions were checked for source-surface consistency where muscle-attention images are present.

## Post-PR Follow-Up: Seated Row Image Addition

| page_path | claim_type | sampled claim | supporting_source | disposition | residual_risk |
| --- | --- | --- | --- | --- | --- |
| `exercises/chest-press.md` | image-to-Markdown alignment | The muscle-attention image highlights broad chest, front-shoulder/triceps, and upper-back support regions while nearby Markdown keeps exact role guidance in a source-backed table. | `mayo-weight-training`; `local-chest-press-setup`; `media/PROVENANCE.md`; `media/prompts/exercises/chest-press/muscle-attention.md` | supported as broad image alignment and source-surface proof. The page keeps the image support-only and says the role cue is not a precise activation test. | low; page was already in the proof slice and the follow-up adds only support media plus prompt/provenance evidence. |
| `exercises/plank.md` | image-to-Markdown alignment | The muscle-attention image highlights broad abdomen/side-trunk, glute/hip, shoulder/upper-back, and leg support regions while nearby Markdown keeps exact role guidance in a source-backed table. | `mayo-weight-training`; `media/PROVENANCE.md`; `media/prompts/exercises/plank/muscle-attention.md` | supported as broad image alignment and source-surface proof. The page keeps the image support-only and says the regions are not an exact activation test. | low; page was already in the proof slice and the follow-up adds only support media plus prompt/provenance evidence. |
| `exercises/seated-row.md` | image-to-Markdown alignment | The muscle-attention image highlights broad upper-back, arm/grip, and trunk-posture regions while nearby Markdown keeps exact guidance in a role table. | `local-seated-row-instruction`; `media/PROVENANCE.md`; `media/prompts/exercises/seated-row/muscle-attention.md` | supported as broad image alignment and source-surface proof. The page cites a seated-row instruction page for the pull, arm support, and still-torso cue. | medium; this is a post-PR follow-up outside the original proof slice and needs code review before renewed branch-ready claims. |

## Residual Risk

This is a bounded source audit, not a clinical review or a remote-source archival snapshot. It is sufficient for the approved M3 manual evidence gate because every sampled claim is either directly exercise-specific, broadly institutionally supported, or softened to practical beginner language. Any later changes to proof-slice muscle roles, feel cues, compensation cues, safety cues, or source IDs must rerun this audit.
