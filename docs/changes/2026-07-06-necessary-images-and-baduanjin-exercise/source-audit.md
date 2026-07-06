# Baduanjin Source Audit

## Scope

Milestone: M2 Baduanjin Markdown Page

Checked page: `exercises/baduanjin-basics.md`

This audit samples setup, safety, method, movement, muscle, feel, and stop-condition claims for page-local source support. It does not approve generated images; those remain downstream M3/M4 work. [VA][va-tai-chi-qigong]

## Claim Samples

| page_path | claim_type | sampled_claim | supporting_source | source_fit | outcome | residual_risk |
|---|---|---|---|---|---|---|
| exercises/baduanjin-basics.md | setup | Practice on a clear, flat surface with comfortable clothing, non-slip foot contact, small first movements, and wall or stable-chair support when balance is uncertain. | `va-tai-chi-qigong` | VA describes Tai Chi and Qigong as gentle practices using slow movements, breathing, and focus, and notes qigong combines breathing, posture, focus, and slow movement. | supported | Surface, clothing, and support wording are conservative beginner setup guidance. |
| exercises/baduanjin-basics.md | safety | Ask a qualified instructor or clinician when medical condition, medication, injury history, dizziness, or balance concern makes practice uncertain. | `va-tai-chi-qigong` | VA directs readers toward professional guidance and trained instruction for complementary practices. | supported | Static page cannot assess an individual reader. |
| exercises/baduanjin-basics.md | method | Beginner starting point uses 3-5 minutes, low effort, pauses, and smoothness before longer practice. | `nccih-qigong`, `va-tai-chi-qigong` | NCCIH supports qigong as body movement/posture, breath regulation, and attention; VA supports slow movement, breathing, and focus. | supported | Duration is an editorial starter range and remains static general education. |
| exercises/baduanjin-basics.md | movement | Beginner breakdown stays to ready stance, two hands lift upward, drawing the bow, alternating reach, and return to standing. | `nccih-qigong`, `baduanjin-review` | NCCIH identifies Baduanjin as qigong; the review describes Baduanjin as eight simple movements with lower physical and cognitive demands than more complex practices. | supported | The page intentionally avoids form-correctness authority. |
| exercises/baduanjin-basics.md | muscle | Broad muscle roles include legs/glutes, trunk, shoulders/upper back, and feet/ankles. | `va-tai-chi-qigong` | VA supports posture, focus, slow movement, and standing or seated practice; the page uses broad movement-attention regions only. | supported | No exact activation claim is made. |
| exercises/baduanjin-basics.md | feel | Reader may notice quiet leg/glute work, tall trunk, relaxed shoulders, steady feet, and normal breathing. | `nccih-qigong`, `va-tai-chi-qigong` | Sources support posture, breath regulation, attention, slow movement, and focus. | supported | Feel cues are broad attention cues, not a correctness test. |
| exercises/baduanjin-basics.md | stop-condition | Stop for dizziness, chest pain, fainting, unusual shortness of breath, sharp pain, numbness, weakness, worsening symptoms, loss of balance control, or uncertainty from medical condition, medication, injury history, or balance concerns. | `local-baduanjin-basics-red-flags`, `va-tai-chi-qigong` | Mayo supports urgent symptom routing for chest pain, fainting, shortness of breath, and concerning symptoms; VA supports professional guidance and trained instruction for uncertainty. | supported | RED-FLAGS.md remains the central routing page for symptoms beyond static exercise education. [VA][va-tai-chi-qigong] |

## Disposition

M2 source support is accepted for the text-only Baduanjin page. Unsupported clinical, disease, cure, individualized-programming, and martial-form claims were not included.

## Residual Risk

The page remains static education and cannot check posture, balance, medical context, or reader understanding. Generated image semantic review and beginner comprehension proof remain downstream M3/M4 obligations.

## Sources

- [Baduanjin Basics page](../../../exercises/baduanjin-basics.md)
- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)

[va-tai-chi-qigong]: https://www.va.gov/WHOLEHEALTH/cih/Tai_Chi_and_Qigong.asp
