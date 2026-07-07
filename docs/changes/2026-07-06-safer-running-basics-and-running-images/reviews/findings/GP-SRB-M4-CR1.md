## Finding GP-SRB-M4-CR1

- Finding ID: GP-SRB-M4-CR1
- Severity: major
- Location: `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/rollback-proof.md:47`, `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/rollback-proof.md:51`, `tests/test_markdown_first_real_pages.py:815`, temporary rollback page line 25
- Evidence: MP4 requires proof that image rollback leaves the page useful as a text-backed primer. The rollback proof command removes only Markdown image-reference lines. Replaying that command leaves this stale sentence in the temporary text-only page: `Use these images as broad visual references. The Markdown instructions below`. The focused M4 rollback test checks that the proof record exists and names cleanup surfaces, but it does not assert that the temporary text-only page removes this image-only prose.
- Required outcome: The rollback proof and its test must demonstrate a text-only temporary page without image-only instruction prose or image references.
- Safe resolution path: Update the rollback rehearsal to remove the `Use these images as broad visual references` paragraph along with image references, record the updated temporary-root commands and passing results, and add a regression assertion that the rollback proof covers removal of stale image-reference prose or otherwise proves it is absent from the temporary text-only page.
- needs-decision rationale: none

## Sources

- [Safer Running Basics and High-Quality Running Images Test Spec](../../../../../../specs/safer-running-basics-and-running-images.test.md)
