## Finding GP-SRB-M3-CR1

- Finding ID: GP-SRB-M3-CR1
- Severity: major
- Location: `specs/safer-running-basics-and-running-images.test.md:238`, `specs/safer-running-basics-and-running-images.test.md:240`, `tests/test_markdown_first_real_pages.py:730`, `tests/test_markdown_first_real_pages.py:754`, `docs/plans/2026-07-06-safer-running-basics-and-running-images.md:163`, `docs/changes/2026-07-06-safer-running-basics-and-running-images/visual-safety-review.md:1`
- Evidence: The approved test spec names `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/visual-safety-review.md` as the expected M3 visual-review evidence path. The implementation instead creates `docs/changes/2026-07-06-safer-running-basics-and-running-images/visual-safety-review.md`, and the M3 tests assert that change-root path. This makes the production evidence and automated proof diverge from the approved proof map. [Test spec][local-GP-SRB-M3-CR1-test-spec]
- Required outcome: The visual-review evidence path and the automated tests must match the approved proof map, or the proof map must be amended through the proper upstream review before M3 can close.
- Safe resolution path: Prefer moving the visual-review artifact under `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/visual-safety-review.md`, updating the M3 tests and plan references to that path, and rerunning the M3 validation commands. If the change-root path is intentional, amend the approved test spec first and route that amendment through the required review gate before rereviewing M3.
- needs-decision rationale: none

## Sources

- [Safer Running Basics and High-Quality Running Images Test Spec][local-GP-SRB-M3-CR1-test-spec]

[local-GP-SRB-M3-CR1-test-spec]: ../../../../../../specs/safer-running-basics-and-running-images.test.md
