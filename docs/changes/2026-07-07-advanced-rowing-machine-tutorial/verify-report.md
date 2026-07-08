# Verify Report: Advanced Rowing Machine Tutorial

## Result

- Skill: verify
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/verify-report.md`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/change.yaml`, `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`, `docs/plan.md`
- Open blockers: none
- Next stage: pr
- Validation: local final verification passed
- Readiness: branch-ready; PR body/open readiness is not claimed

## Verdict

The final advanced rowing-machine change pack is coherent across the accepted proposal, approved spec, architecture amendment, reviewed plan, active test spec, implementation files, generated media, prompt packets, provenance rows, manual proof records, code-review records, review-resolution, explain-change, and fresh local validation.

The branch is ready for PR handoff.
Hosted CI has not been observed.

## Traceability

| Requirement group | Test IDs and proof | Files changed | Evidence | Status |
| --- | --- | --- | --- | --- |
| R1-R9, R47-R48 | ART-T1, ART-T2, ART-T3, ART-T12 | `exercises/rowing-machine.md`, `exercises/rowing-machine-advanced.md`, `tools/checks/check_markdown_first.py`, tests | Real-page tests, forbidden-scope fixture tests, broad Markdown-first validation | pass |
| R10-R19 | ART-T4, ART-T5, ART-T12, ART-MP1 | `exercises/rowing-machine-advanced.md`, `SOURCES.md`, source-audit proof | Real-page tests and source audits confirm static damper, monitor, rhythm, force-curve, workout, benchmark, and method boundaries | pass |
| R20-R21 | ART-T6, ART-MP1 | `exercises/rowing-machine-advanced.md`, `SOURCES.md`, source-audit proof | Page-local source checks and broad Markdown-first validation passed | pass |
| R22-R32 | ART-T7, ART-T8, ART-T9, ART-T10 | `media/exercises/rowing-machine-advanced/*.png`, `media/prompts/exercises/rowing-machine-advanced/*.md`, `media/PROVENANCE.md`, checker/tests | Scoped eight-image exception, prompt packet, provenance, and force-overlay allow/deny tests passed | pass |
| R33-R44 | ART-T10, ART-T11, ART-MP2, ART-MP3 | advanced page, prompt packets, generated images, manual visual proof | Force-intensity, label, alt-text, legend, excluded-media, visual-safety, and grayscale checks passed | pass |
| R45-R46 | ART-MP2, ART-MP3 | `manual-proof/visual-safety-review-m3.md`, `manual-proof/grayscale-review-m3.md` | Manual proof records and code-review R5 accepted the visual-safety/grayscale evidence | pass |
| R49 | ART-MP4 | `manual-proof/advanced-reader-comprehension-m4.md` | Non-identifying reader comprehension proof covers required advanced-rowing questions | pass |
| R50 | ART-T13, ART-CMD1, ART-CMD8, ART-CMD9, ART-CMD10 | `validation-ledger-m4.md`, plan, change metadata, verify report | Exact commands and outcomes are recorded before branch-ready claim | pass |

## Verification Dimensions

| Dimension | Verdict | Evidence |
| --- | --- | --- |
| Spec coverage | pass | Implemented behavior maps to R1-R50 or the upstream general-audience governance update. |
| Requirement satisfaction | pass | Automated tests, manual proof, code reviews, and final validation cover all `MUST` requirements. |
| Test coverage | pass | ART-T1 through ART-T13 and ART-MP1 through ART-MP4 have automated or manual evidence. |
| Test validity | pass | Temporary-root negative tests cover forbidden assets, force-overlay misuse, missing prompt fields, copied UI, personal targets, competition programming, and clinical protocol drift. |
| Architecture coherence | pass | The implementation stays Markdown-first and uses prompt records, provenance, source audits, and static validation rather than runtime software. |
| Artifact lifecycle state | pass | `docs/plan.md`, active plan, `change.yaml`, review records, review-resolution, explain-change, and this report agree on PR handoff after verification. |
| Plan completion | pass | M1-M4 are closed, review-resolution is closed, code-review R5 is clean-with-notes, and explain-change is complete. |
| Validation evidence | pass | Fresh local commands listed below passed. Hosted CI was not observed. |
| Drift detection | pass | The final diff matches the accepted proposal, approved spec, architecture amendment, plan milestones, and explain-change rationale. |
| Risk closure | pass | Scope, privacy, licensing/provenance, source support, visual safety, grayscale accessibility, and rollback/manual proof risks are addressed. |
| Release readiness | pass | Working tree validation passed locally; branch-ready is supported. PR body/open readiness belongs to the PR stage. |

## Fresh Validation

Commands run from the repository root:

| Command | Result |
| --- | --- |
| `python3 -m unittest discover -s tests` | pass, 237 tests |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md principles exercises patterns` | pass, checked 30 Markdown file(s) |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md docs specs tools tests principles exercises patterns` | pass, checked 594 file(s) |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | pass, checked 46 Markdown file(s) |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md RED-FLAGS.md exercises media docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | pass, checked 251 file(s) |
| `python3 tools/checks/check_markdown_first.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md` | pass, checked 4 Markdown file(s) |
| `python3 tools/checks/check_markdown_first.py exercises/rowing-machine-advanced.md media/PROVENANCE.md media/prompts/exercises/rowing-machine-advanced` | pass, checked 2 Markdown file(s) |
| `python3 tools/checks/check_privacy.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | pass, checked 26 file(s) |
| `git diff --check` | pass |

The local CI-equivalent commands from `.github/workflows/ci.yml` passed.
No hosted GitHub Actions run was observed during verify.

## Manual Proof

| Proof ID | Record | Verification result |
| --- | --- | --- |
| ART-MP1 | `source-audit-m2.md`, `manual-proof/source-audit-m4.md` | pass |
| ART-MP2 | `manual-proof/visual-safety-review-m3.md` | pass |
| ART-MP3 | `manual-proof/grayscale-review-m3.md` | pass |
| ART-MP4 | `manual-proof/advanced-reader-comprehension-m4.md` | pass |

These checks are manual by design because static text checks cannot fully prove visual semantics, source adequacy, grayscale distinction, or reader comprehension.

## CI Status

CI workflow configuration exists at `.github/workflows/ci.yml`.
The configured local equivalents passed during this verify run.
Hosted CI was not observed, so this report does not claim hosted CI passed.

## Artifact Drift

No blocking drift found.

Verified lifecycle surfaces:

- `docs/plan.md`
- `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/change.yaml`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-resolution.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/explain-change.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/verify-report.md`

## Remaining Risks

- Hosted CI has not been observed before PR handoff.
- Generated images may still benefit from broader human visual review after PR feedback, but prompt packets, provenance, visual-safety proof, grayscale proof, and rollback path are present.
- PR body and PR open readiness are not claimed here.

## Handoff

Branch-ready is supported by tracked artifacts and fresh local validation.
The next lifecycle stage is `pr`.

## Sources

- `docs/proposals/2026-07-07-advanced-rowing-machine-tutorial.md`
- `specs/advanced-rowing-machine-tutorial.md`
- `specs/advanced-rowing-machine-tutorial.test.md`
- `docs/architecture/system/architecture.md`
- `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/explain-change.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-resolution.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md`
- `.github/workflows/ci.yml`
