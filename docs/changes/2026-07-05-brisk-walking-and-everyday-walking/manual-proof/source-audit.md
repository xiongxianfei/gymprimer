# Walking Source Audit

## Scope

This source audit samples semantic support for the M2 walking pages before promotion.

Pages reviewed:

- `exercises/brisk-walking.md`
- `principles/everyday-walking.md`

No external websites were fetched during this audit. The audit checks that the
page claims are traceable to the approved page-local source IDs and identifies
where residual source-fit judgment remains manual.

## Claim Samples

| page_path | claim_type | sampled_claim | supporting_source | source_fit | outcome | residual_risk |
| --- | --- | --- | --- | --- | --- | --- |
| `exercises/brisk-walking.md` | intensity | Brisk walking is deliberate moderate-intensity cardio when effort is high enough. | `cdc-physical-activity-intensity`; `nhs-walking-for-health` | Direct for moderate intensity examples and walking-for-health framing. | accepted | Manual review still needed before broad promotion for exact wording tone. |
| `exercises/brisk-walking.md` | talk-test | The reader can talk, but not comfortably sing. | `cdc-physical-activity-intensity`; `nhs-walking-for-health` | Direct for talk-test framing. | accepted | None beyond normal source-staleness review. |
| `exercises/brisk-walking.md` | weekly-activity-guidance | Walking can contribute to aerobic activity while strength work remains separate. | `cdc-adult-activity`; `aha-physical-activity-recommendations` | Direct for adult aerobic and strengthening guidance. | accepted | Page intentionally avoids turning weekly targets into a personal plan. |
| `principles/everyday-walking.md` | less-sitting-framing | Everyday walking helps move more and sit less. | `aha-physical-activity-recommendations`; `cdc-adult-activity` | Direct for move-more and less-sitting guidance. | accepted | Everyday walking intensity is still distinguished from brisk cardio in page text. |
| `exercises/brisk-walking.md` | walking-technique | Look forward, relax neck and shoulders, swing arms naturally, keep relaxed hands, stay tall, and roll heel to toe. | `mayo-walking` | Direct for walking posture, arm swing, trunk engagement, and heel-to-toe routine cues. | accepted | Exact beginner phrasing remains editorial, not a clinical technique protocol. |
| `exercises/brisk-walking.md` | starter-duration-or-progression | Start with 5-10 minutes; progress by total minutes, then brisk minutes, then hills or faster sections if comfortable. | `nhs-walking-for-health`; `aha-physical-activity-recommendations`; `mayo-walking` | Supported by short-walk accumulation and gradual build-up guidance. | accepted | Hill/faster-section wording is deliberately conservative and not an incline protocol. |
| `exercises/brisk-walking.md` | stop-rules | Stop for chest pain, fainting, severe dizziness, unusual shortness of breath, new severe pain, numbness, weakness, neurological symptoms, symptoms that worsen, or symptoms that do not settle. | `local-brisk-walking-red-flags`; `../RED-FLAGS.md` | Direct safety routing for serious symptoms plus central safety reference. | accepted | This remains safety-routing education, not symptom triage. |
| `principles/everyday-walking.md` | stop-rules | Stop and seek appropriate help for the same walking red flags; change route if the route feels unsafe. | `local-everyday-walking-red-flags`; `mayo-walking`; `../RED-FLAGS.md` | Direct enough for conservative safety routing and route-selection advice. | accepted | Route safety examples are practical guidance rather than medical claims. |

## Disposition

M3 source audit accepts the sampled claims for this implementation slice.

The pages keep page-local source definitions and reuse indexed global source
IDs where the same public sources appear across pages.

## Residual Risk

Automated checks cannot prove full semantic source adequacy, tone, or future
source freshness.

Before final publication, reviewers should re-check the sampled source support
if walking wording changes, if source URLs change, or if an optional image is
added later.
