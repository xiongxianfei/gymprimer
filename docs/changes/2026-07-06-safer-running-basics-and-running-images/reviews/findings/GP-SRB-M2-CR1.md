## Finding GP-SRB-M2-CR1

- Finding ID: GP-SRB-M2-CR1
- Severity: major
- Location: `specs/safer-running-basics-and-running-images.md:120`, `exercises/safer-running-basics.md:94`, `exercises/safer-running-basics.md:114`, `exercises/safer-running-basics.md:150`, `tests/test_markdown_first_real_pages.py:578`
- Evidence: Spec R5.4 requires the `What you should feel` section to route chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, weakness, worsening symptoms, or persistent pain to the project safety path and appropriate professional help. The page routes chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, weakness, symptoms that worsen, and symptoms that do not settle, but it never names persistent pain. The M2 real-page test asserts the other required symptom terms and the `RED-FLAGS.md` route, but it also omits persistent pain, so the requirement gap is not protected. [Spec][local-GP-SRB-M2-CR1-spec]
- Required outcome: The M2 page and tests must explicitly cover persistent pain routing in the safety-facing text required by R5.4.
- Safe resolution path: Add persistent pain to the `What you should feel` safety sentence and the related `Stop if` or `Safety notes` route as appropriate, keeping the Mayo citation and `RED-FLAGS.md` link on the safety line. Add a direct assertion for `persistent pain` in `test_safer_running_broad_muscle_feel_and_stop_guidance` or an equivalent M2 real-page test. Rerun `python3 -m unittest tests.test_markdown_first_real_pages`, the scoped Markdown/privacy checks for the page and change directory, and the full unittest suite before returning M2 to `review-requested`. [Spec][local-GP-SRB-M2-CR1-spec]
- needs-decision rationale: none

## Sources

- [Safer Running Basics and High-Quality Running Images Spec][local-GP-SRB-M2-CR1-spec]

[local-GP-SRB-M2-CR1-spec]: ../../../../../../specs/safer-running-basics-and-running-images.md
