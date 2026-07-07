# Code Review R4: Advanced Rowing Machine Tutorial M3

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/code-review-r4.md`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md`, `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`, `docs/plan.md`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/change.yaml`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/code-review-r4.md
- Review log: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md
- Review resolution: not-required
- Reviewed milestone: M3. Governed Media, Prompt Packets, and Provenance
- Milestone closeout: closed
- Remaining implementation milestones: M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: commit `8959ddf` (`M3: add advanced rowing governed media assets`).
- Tracked governing branch state: branch `2026-07-07-advanced-rowing-machine-tutorial`, clean before review recording.
- Governing artifacts: `specs/advanced-rowing-machine-tutorial.md`, `specs/advanced-rowing-machine-tutorial.test.md`, `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`.
- Relevant implementation files: `exercises/rowing-machine-advanced.md`, `media/PROVENANCE.md`, `media/exercises/rowing-machine-advanced/`, `media/prompts/exercises/rowing-machine-advanced/`, `tests/test_markdown_first_real_pages.py`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/manual-proof/visual-safety-review-m3.md`, and `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/manual-proof/grayscale-review-m3.md`.

## Diff summary

M3 adds the eight approved advanced-rowing generated raster assets under `media/exercises/rowing-machine-advanced/`.
It adds matching image-instruction prompt packets under `media/prompts/exercises/rowing-machine-advanced/`.
It adds approved provenance rows for the eight assets in `media/PROVENANCE.md`.

The advanced rowing page now references each asset with meaningful alt text, nearby Markdown explanation, force-intensity legends where applicable, and technical-diagram label duplication text where applicable.
The real-page tests now assert exact local assets, prompt packets, provenance rows, instructional layers, force-map boundaries, and page integration.
M3 also records visual-safety and grayscale manual proof for the generated assets.

## Findings

No blocking or required-change findings.

## Checklist coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | pass | R22-R46 are represented by the exact eight paths in `media/exercises/rowing-machine-advanced/`, prompt packet fields in `media/prompts/exercises/rowing-machine-advanced/*.md`, provenance rows in `media/PROVENANCE.md`, and page image integration in `exercises/rowing-machine-advanced.md`. |
| Test coverage | pass | `tests/test_markdown_first_real_pages.py` adds M3 real-page checks for local image references, asset existence, provenance status, prompt-record fields, force-overlay packet terms, non-force image maps, force legends, and technical-diagram Markdown/alt label handling. |
| Edge cases | pass | ART-T7 through ART-T11 have direct proof: exact stem set and prompt/provenance matching in tests, force-overlay/non-overlay stem separation in prompt packets, no `stroke-rate-ladder` force overlay, visual-safety proof in `manual-proof/visual-safety-review-m3.md`, and grayscale proof in `manual-proof/grayscale-review-m3.md`. |
| Error handling | pass | No runtime code or permission-sensitive behavior is introduced. Static failure paths are handled through the existing Markdown-first checker categories for missing packets, mismatched page references, disallowed force overlays, label duplication, forbidden media text, and missing provenance. |
| Architecture boundaries | pass | The diff remains Markdown-first and repository-local: images support the page, prompt packets record generation instructions, and provenance records approval. It does not add a hosted app, runtime API, calculator, tracker, video product, or coaching engine. |
| Compatibility | pass | The image-rich exception stays scoped to `exercises/rowing-machine-advanced.md`; the existing checker constants still limit the approved advanced-rowing asset set and do not globally raise unrelated exercise image limits. |
| Security/privacy | pass | Prompt packets and proof artifacts avoid private data, private source material, screenshots of personal monitor data, and identifiable people. Reviewer-ran privacy validation passed over the M3 surfaces. |
| Derived artifact currency | pass | Page image references, prompt packet `asset_path` fields, provenance `prompt_record` fields, proof notes, plan state, and change metadata are synchronized for M3. |
| Unrelated changes | pass | Commit `8959ddf` is limited to M3 media assets, prompt packets, provenance, advanced page image integration, M3 tests, manual proof, and lifecycle metadata. |
| Validation evidence | pass | Reviewer reran full unittest discovery, focused Markdown-first validation, focused privacy validation, and whitespace validation; all passed. |

## No-finding rationale

The implementation satisfies the M3 media-governance contract without widening scope beyond the approved advanced-rowing page.
Every promoted asset has a local file, prompt packet, approved provenance row, page reference, media purpose, instructional layer, teaching goal, visual rules, exact prompt, and review notes.

The force-intensity images are limited to the approved four stems and have 0-3 relative-scale packet wording, non-measurement boundaries, non-color cue language, page legends, and grayscale proof.
The monitor, damper/drag-factor, interval, and stroke-rate ladder assets do not use force-intensity overlays.
Independent visual inspection during review did not show copied PM5 UI, readable in-image labels, logos, identifiable people, red warning marks, correct/wrong badges, or race-win framing.

## Residual risks

- Static tests cannot prove all visual semantics; M3 mitigates this with manual visual-safety and grayscale proof, and final broader proof remains assigned to M4.
- M4 remains open for final manual proof and broad validation ledger, including reader comprehension.
- CI was not observed; only local validation is cited.

## Validation evidence

Reviewer-ran commands:

```bash
python3 -m unittest discover -s tests
python3 tools/checks/check_markdown_first.py exercises/rowing-machine-advanced.md media/PROVENANCE.md media/prompts/exercises/rowing-machine-advanced
python3 tools/checks/check_privacy.py exercises/rowing-machine-advanced.md media/prompts/exercises/rowing-machine-advanced media/PROVENANCE.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial
git diff --check
```

Results:

- Full unittest suite: pass, 237 tests.
- Focused Markdown-first check: pass, checked 2 Markdown file(s).
- Focused privacy check: pass, checked 26 file(s).
- Whitespace check: pass.

## Milestone handoff

- Reviewed milestone: M3. Governed Media, Prompt Packets, and Provenance
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining implementation milestones: M4
- Next stage: implement M4. Manual Proof, Review Evidence, and Closeout Preparation
- Final closeout readiness: not-ready; M4 implementation, later review, explain-change, verify, and PR handoff remain.

## Sources

[local-code-review-r4-spec]: ../../../../specs/advanced-rowing-machine-tutorial.md
[local-code-review-r4-test-spec]: ../../../../specs/advanced-rowing-machine-tutorial.test.md
[local-code-review-r4-plan]: ../../../plans/2026-07-07-advanced-rowing-machine-tutorial.md
[local-code-review-r4-advanced-page]: ../../../../exercises/rowing-machine-advanced.md
[local-code-review-r4-provenance]: ../../../../media/PROVENANCE.md
[local-code-review-r4-prompts]: ../../../../media/prompts/exercises/rowing-machine-advanced/
[local-code-review-r4-tests]: ../../../../tests/test_markdown_first_real_pages.py
[local-code-review-r4-visual-proof]: ../manual-proof/visual-safety-review-m3.md
[local-code-review-r4-grayscale-proof]: ../manual-proof/grayscale-review-m3.md
