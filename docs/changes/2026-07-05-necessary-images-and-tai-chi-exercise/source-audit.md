# Tai Chi Source Audit

## Scope

Milestone: M2 Tai Chi Markdown Page

Checked page: `exercises/tai-chi-basics.md`

This audit samples setup, safety, method, movement, muscle, feel, and stop-condition claims for page-local source support. It does not approve generated images; those remain downstream M3/M4 work.

## Claim Samples

| page_path | claim_type | sampled_claim | supporting_source | source_fit | outcome | residual_risk |
|---|---|---|---|---|---|---|
| exercises/tai-chi-basics.md | setup | Practice on a clear, flat surface with non-slip footwear or stable foot contact, small slow movements, and wall or stable-chair support when balance is uncertain. | `harvard-tai-chi`, `nhs-balance-exercises` | Harvard supports comfortable clothing and non-slip supportive shoes; NHS supports building up slowly and practicing near a wall or stable chair. | supported | The exact stance width is editorial beginner guidance, not a cited clinical rule. |
| exercises/tai-chi-basics.md | safety | Ask a qualified instructor or clinician when medical condition, medication, injury history, dizziness, or balance concern makes practice uncertain. | `harvard-tai-chi`, `va-tai-chi-qigong` | Harvard recommends checking with a medical care team for limiting conditions or medications that can cause dizziness/lightheadedness; VA points readers to providers and trained instructors. | supported | Static page cannot assess an individual reader. |
| exercises/tai-chi-basics.md | method | Beginner starting point uses 3-5 minutes, low effort, pauses, and smoothness before larger or more complex movement. | `nccih-tai-chi`, `harvard-tai-chi`, `nhs-balance-exercises` | Sources support slow gentle movement, smaller/slower beginner forms, and gradual buildup. | supported | Duration is an editorial starter range and remains static general education. |
| exercises/tai-chi-basics.md | movement | Beginner breakdown stays to ready stance, small weight shift, opening movement, and return to standing. | `nccih-tai-chi`, `harvard-tai-chi`, `va-tai-chi-qigong` | Sources support slow flowing movement, breathing/focus, smaller beginner forms, and shifting weight as a simple motion. | supported | The page intentionally avoids named form correctness. |
| exercises/tai-chi-basics.md | muscle | Broad muscle roles include legs/glutes, trunk, shoulders/upper back, and feet/ankles. | `harvard-tai-chi`, `nhs-balance-exercises` | Harvard supports lower-body, upper-body, and core involvement; NHS balance movements support ground contact and balance adjustment framing. | supported | No exact activation claim is made. |
| exercises/tai-chi-basics.md | feel | Reader may notice quiet leg/glute work, tall trunk, relaxed shoulders, steady feet, and normal breathing. | `nccih-tai-chi`, `harvard-tai-chi`, `va-tai-chi-qigong` | Sources support controlled breathing, relaxed muscles, balance/posture, and slow flowing practice. | supported | Feel cues are broad attention cues, not a correctness test. |
| exercises/tai-chi-basics.md | stop-condition | Stop for dizziness, chest pain, fainting, unusual shortness of breath, sharp pain, worsening symptoms, loss of balance control, or uncertainty from medical condition, medication, injury history, or balance concerns. | `local-tai-chi-basics-red-flags`, `harvard-tai-chi`, `nhs-balance-exercises` | Mayo supports urgent symptom routing for chest pain, fainting, shortness of breath, and concerning symptoms; Harvard supports medical-team checks for conditions and dizziness-related medication; NHS supports wall/chair support when balance may be lost. | supported | RED-FLAGS.md remains the central routing page for symptoms beyond static exercise education. |

## Disposition

M2 source support is accepted for the text-only Tai Chi page. Unsupported clinical, disease, cure, fall-prevention, rehab, and individualized-programming claims were not included.

## Residual Risk

The page remains static education and cannot check posture, balance, medical context, or reader understanding. Generated image semantic review and beginner comprehension proof remain downstream M3/M4 obligations.
