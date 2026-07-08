# Code Review R3: Advanced Rowing Machine Tutorial M2

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/code-review-r3.md`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md`, `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`, `docs/plan.md`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/change.yaml`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/code-review-r3.md
- Review log: docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md
- Review resolution: not-required
- Reviewed milestone: M2. Advanced Rowing Markdown Content
- Milestone closeout: closed
- Remaining implementation milestones: M3, M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: commit `fc7bc17` (`M2: add advanced rowing companion page`).
- Tracked governing branch state: branch `2026-07-07-advanced-rowing-machine-tutorial`, clean before review recording.
- Governing artifacts: `specs/advanced-rowing-machine-tutorial.md`, `specs/advanced-rowing-machine-tutorial.test.md`, `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`.
- Relevant implementation files: `exercises/rowing-machine-advanced.md`, `exercises/rowing-machine.md`, `SOURCES.md`, `tests/test_markdown_first_real_pages.py`, `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/source-audit-m2.md`, `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md`.

## Diff summary

M2 adds the static advanced rowing companion page at `exercises/rowing-machine-advanced.md`.
The page includes the required sections, prerequisite boundary, damper and drag factor explanation, monitor metric literacy, rhythm and force-curve guidance, stroke-rate control, static workout-type examples, broad muscle guidance, force-intensity visual-system text, safety notes, and page-local sources.

The beginner rowing page keeps its existing tutorial and adds a bottom companion link.
`SOURCES.md` now includes the reused Concept2, British Rowing, W3C, and Mayo source IDs.
Real-page tests cover the advanced page shape, prerequisites, concepts, forbidden scope, source IDs, workout examples, and force-intensity system.
The M2 source audit records bounded manual support for the concrete advanced-rowing claims.
The exercise-image audit adds the new advanced page as text-only, deferring generated media to M3.

## Findings

No blocking or required-change findings.

## Checklist coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | pass | R1-R21 and R47-R50 are represented by the page content and link: the beginner page remains intact with only a companion link at `exercises/rowing-machine.md:185`, the advanced page exists at `exercises/rowing-machine-advanced.md:1`, and the page keeps static literacy/non-plan boundaries at `exercises/rowing-machine-advanced.md:23-30` and `exercises/rowing-machine-advanced.md:111-126`. |
| Test coverage | pass | `tests/test_markdown_first_real_pages.py:1501-1644` adds real-page coverage for the beginner link, advanced page shape, prerequisites, runtime exclusions, advanced rowing concepts, source IDs, static workout types, method type, and force-intensity terms. |
| Edge cases | pass | ART-T1 through ART-T6 and ART-T12 have direct M2 evidence: prerequisite/editorial boundary at `exercises/rowing-machine-advanced.md:32-43`, no personal targets at `exercises/rowing-machine-advanced.md:74` and `exercises/rowing-machine-advanced.md:115`, benchmark boundary at `exercises/rowing-machine-advanced.md:123-126`, and source audit rows at `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/source-audit-m2.md:16-27`. |
| Error handling | pass | No runtime or failure-handling code is introduced. The relevant invalid-state handling is static checker coverage from M1 plus M2 real-page tests and Markdown-first validation. |
| Architecture boundaries | pass | The diff remains Markdown-first and asset-free for M2. Generated media, prompt packets, provenance, visual-safety review, and grayscale review remain deferred to M3/M4, documented at `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/source-audit-m2.md:9-10` and `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md:38`. |
| Compatibility | pass | `SOURCES.md:55-62` and `SOURCES.md:106-113` add the reused advanced-rowing source IDs; `tests/test_markdown_first_real_pages.py:1636-1644` checks the new source-index entries. The exercise-image audit row keeps existing audit enumeration current. |
| Security/privacy | pass | The page asks for no user data, accounts, logs, wearable data, or uploads, and reviewer-ran privacy validation passed over the M2 surfaces. |
| Derived artifact currency | pass | Plan, change metadata, review log, source audit, source index, and the exercise-image audit are updated for the new advanced page. No generated assets or provenance rows are introduced in this milestone. |
| Unrelated changes | pass | The diff is limited to the M2 page/link, source index, tests, source audit, lifecycle metadata, and required exercise-image audit row. |
| Validation evidence | pass | Reviewer reran full unittest discovery, focused Markdown-first validation, focused privacy validation, and whitespace validation; all passed. |

## No-finding rationale

The implementation satisfies the M2 contract without adding media, runtime behavior, generated assets, personalized programming, clinical protocols, or race coaching.
Concrete advanced-rowing claims have page-local citations and a bounded M2 source-audit record.
The added tests cover the named real-page behavior and source-index obligations that become observable in M2.
The remaining visual, prompt, provenance, grayscale, and reader-comprehension proof obligations are explicitly assigned to M3/M4 and are not required for this text-only milestone.

## Residual risks

- The advanced page has no generated media yet; that is intentional for M2 and remains assigned to M3.
- Static review cannot prove final visual semantics, grayscale distinguishability, or reader comprehension; those remain assigned to later proof surfaces.
- CI was not observed; only local validation is cited.

## Validation evidence

Reviewer-ran commands:

```bash
python3 -m unittest discover -s tests
python3 tools/checks/check_markdown_first.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md
python3 tools/checks/check_privacy.py exercises/rowing-machine.md exercises/rowing-machine-advanced.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial
git diff --check
```

Results:

- Full unittest suite: pass, 234 tests.
- Focused Markdown-first check: pass, checked 4 Markdown file(s).
- Focused privacy check: pass, checked 17 file(s).
- Whitespace check: pass.

## Milestone handoff

- Reviewed milestone: M2. Advanced Rowing Markdown Content
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining implementation milestones: M3, M4
- Next stage: implement M3. Governed Media, Prompt Packets, and Provenance
- Final closeout readiness: not-ready; M3-M4 implementation, later review, explain-change, verify, and PR handoff remain.

## Sources

[local-code-review-r3-spec]: ../../../../specs/advanced-rowing-machine-tutorial.md
[local-code-review-r3-test-spec]: ../../../../specs/advanced-rowing-machine-tutorial.test.md
[local-code-review-r3-plan]: ../../../plans/2026-07-07-advanced-rowing-machine-tutorial.md
[local-code-review-r3-advanced-page]: ../../../../exercises/rowing-machine-advanced.md
[local-code-review-r3-beginner-page]: ../../../../exercises/rowing-machine.md
[local-code-review-r3-sources]: ../../../../SOURCES.md
[local-code-review-r3-tests]: ../../../../tests/test_markdown_first_real_pages.py
[local-code-review-r3-source-audit]: ../source-audit-m2.md
