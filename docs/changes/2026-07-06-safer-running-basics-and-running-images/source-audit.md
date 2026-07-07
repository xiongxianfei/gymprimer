# Safer Running Source Audit

## Scope

This audit covers the M2 text-only page at
`exercises/safer-running-basics.md`. It checks that the beginner-running
claims are supported by page-local sources and that the page remains general
exercise education rather than individualized coaching.

## Claim Samples

| page_path | claim_type | supporting_source | source_fit | outcome | residual_risk |
|---|---|---|---|---|---|
| `exercises/safer-running-basics.md` | title-alias | approved proposal and spec | Supports `Safer Running Basics` as the H1 while preserving the search phrase only as an alias. | accepted | Readers may still search for a stronger promise, so the disclaimer remains near the top. |
| `exercises/safer-running-basics.md` | run-walk-frequency | `nhs-couch-to-5k` | NHS supports beginner run/walk structure, three running days per week, and rest days between runs. | accepted | This is a static example, not a personal schedule. |
| `exercises/safer-running-basics.md` | warm-up | `mchs-better-runner` | Mayo Clinic Health System supports a short warm-up before running. | accepted | The page keeps the cue general rather than prescribing drills. |
| `exercises/safer-running-basics.md` | progression | `mchs-better-runner` | Mayo Clinic Health System supports gradual mileage progression and the 10% weekly mileage limit. | accepted | Mileage is only one load variable; the page also warns against changing several variables together. |
| `exercises/safer-running-basics.md` | form | `acsm-running-form` | ACSM supports broad form education around reach, loading, and relaxed mechanics. | accepted | The page avoids gait prescription and foot-strike dogma. |
| `exercises/safer-running-basics.md` | muscle | `mchs-better-runner`, `acsm-running-form` | Sources support broad beginner attention to posture, landing, push-off, and relaxed arm swing. | accepted | The muscle table is body-awareness guidance, not exact activation instruction. |
| `exercises/safer-running-basics.md` | strength-evidence-limit | `cdc-adult-activity`, `pubmed-running-injury-exercise-prevention`, `pmc-running-injury-support` | CDC supports including muscle-strengthening activity, while recent running-injury reviews support cautious claims about exercise-only prevention. | accepted | The page presents strength as capacity support and does not promise prevention. |
| `exercises/safer-running-basics.md` | stop-condition [Mayo Clinic][mayo-exercise-chronic-disease] | `mayo-exercise-chronic-disease` | Mayo Clinic supports routing concerning exercise symptoms to appropriate care. | accepted | The page links to `RED-FLAGS.md` and stays non-clinical. |

## Disposition

The M2 page is ready for code review as a text-only exercise page. Shared source
IDs are already registered in `SOURCES.md`, and each cited source used by the
page has a page-local definition.

## Residual Risk

Source support is strongest for general beginner structure, warm-up, activity
guidance, and symptom routing. Form and strength claims remain deliberately
conservative because evidence around running-related injury prevention is
mixed.

## Sources

- [NHS Couch to 5K running plan][nhs-couch-to-5k]
- [Mayo Clinic Health System running guidance][mchs-better-runner]
- [CDC adult activity guidance][cdc-adult-activity]
- [ACSM distance running form guidance][acsm-running-form]
- [Mayo Clinic exercise and chronic disease guidance][mayo-exercise-chronic-disease]
- [PubMed: exercise-based prevention programs and running-related injuries][pubmed-running-injury-exercise-prevention]
- [PMC: running-centred injury prevention support scoping review][pmc-running-injury-support]

[nhs-couch-to-5k]: https://www.nhs.uk/better-health/get-active/get-running-with-couch-to-5k/couch-to-5k-running-plan/
[mchs-better-runner]: https://www.mayoclinichealthsystem.org/hometown-health/speaking-of-health/how-can-i-become-a-better-runner-and-avoid-injury
[cdc-adult-activity]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
[acsm-running-form]: https://acsm.org/distance-running-form-tips/
[mayo-exercise-chronic-disease]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-and-chronic-disease/art-20046049
[pubmed-running-injury-exercise-prevention]: https://pubmed.ncbi.nlm.nih.gov/38261240/
[pmc-running-injury-support]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11986186/
