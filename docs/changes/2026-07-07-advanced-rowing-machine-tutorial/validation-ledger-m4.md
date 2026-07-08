# M4 Validation Ledger

Date: 2026-07-07
Milestone: M4. Manual Proof, Review Evidence, and Closeout Preparation

## Scope

This ledger records final M4 validation for the advanced rowing-machine tutorial implementation before code-review.
It covers automated checks, manual proof artifacts, and known validation limits.

## Manual Proof Artifacts

| Proof ID | Requirement coverage | Artifact | Result |
| --- | --- | --- | --- |
| ART-MP1 | Source audit for damper, drag factor, monitor metrics, stroke rate, force curve, workout examples, benchmark boundaries, and safety wording. | `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/manual-proof/source-audit-m4.md` | Pass |
| ART-MP2 | Visual-safety review for generated images. | `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/manual-proof/visual-safety-review-m3.md` | Pass |
| ART-MP3 | Grayscale and force-overlay review. | `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/manual-proof/grayscale-review-m3.md` | Pass |
| ART-MP4 | Advanced-reader comprehension proof. | `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/manual-proof/advanced-reader-comprehension-m4.md` | Pass |

## Validation Commands

| Command ID | Command | Result | Evidence |
| --- | --- | --- | --- |
| ART-CMD1 | `python3 -m unittest discover -s tests` | pass | Ran 237 tests. |
| ART-CMD8 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | pass | Checked 44 Markdown file(s). |
| ART-CMD9 | `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md RED-FLAGS.md exercises media docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | pass | Checked 249 file(s): privacy pass. |
| ART-CMD10 | `git diff --check` | pass | No whitespace errors reported. |

## Known Limits

- Static checks cannot prove every visual semantic; this is why ART-MP2 and ART-MP3 are recorded.
- Static checks cannot prove source adequacy by themselves; this is why ART-MP1 is recorded.
- Static checks cannot prove reader comprehension by themselves; this is why ART-MP4 is recorded.
- Hosted CI is not claimed unless a later stage observes a CI run.

## Disposition

M4 validation passed locally.
Hosted CI was not observed and is not claimed.

## Sources

[local-advanced-rowing-test-spec]: ../../../specs/advanced-rowing-machine-tutorial.test.md
[local-advanced-rowing-plan]: ../../../docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md
[local-source-audit-m4]: manual-proof/source-audit-m4.md
[local-visual-safety-review-m3]: manual-proof/visual-safety-review-m3.md
[local-grayscale-review-m3]: manual-proof/grayscale-review-m3.md
[local-comprehension-proof-m4]: manual-proof/advanced-reader-comprehension-m4.md
