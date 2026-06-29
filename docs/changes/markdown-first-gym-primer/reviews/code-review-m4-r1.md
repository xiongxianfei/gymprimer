# Code Review M4 R1: Markdown-First Gym Primer

## Result

- Skill: code-review
- Status: completed
- Artifacts changed:
  - `docs/changes/markdown-first-gym-primer/reviews/code-review-m4-r1.md`
  - `docs/changes/markdown-first-gym-primer/review-log.md`
  - `docs/plans/2026-06-27-markdown-first-gym-primer.md`
  - `docs/plan.md`
  - `docs/workflows.md`
  - `docs/changes/markdown-first-gym-primer/change.yaml`
- Open blockers: none
- Next stage: explain-change
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/code-review-m4-r1.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M4. Optional mdBook and Final Local Quality Gate
- Milestone closeout: closed
- Remaining implementation milestones: none
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: M4 tests, MP4 mdBook deferral proof, MP5 validation
  ledger/source-of-truth drift inspection, manual-proof README, and workflow
  routing updates.
- Tracked governing branch state: working tree on
  `proposal/markdown-first-gym-primer`; artifacts are uncommitted, so this
  review is milestone-local and does not claim branch readiness.
- Governing artifacts: `specs/markdown-first-primer.md` R31-R33 and R36-R40,
  `specs/markdown-first-primer.test.md` T11-T13 and MP4-MP5, and
  `docs/plans/2026-06-27-markdown-first-gym-primer.md` M4.
- Validation evidence rerun during review:
  - `python3 -m unittest tests.test_markdown_first_mdbook tests.test_markdown_first_observability tests.test_markdown_first_compatibility`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight`
  - `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight media docs/changes/markdown-first-gym-primer`
  - `if command -v mdbook >/dev/null 2>&1; then mdbook build; else printf 'mdbook not installed; mdBook deferred\n'; fi`
  - `if rg -n "barbell|deadlift|bench press|Olympic|kettlebell|plyometric|sprint|diagnos|rehab|treat pain|posture correction" 01-getting-started 02-machines 03-bodyweight; then exit 1; else printf "no excluded-scope terms found\n"; fi`
  - `markdownlint --disable MD013 -- docs/changes/markdown-first-gym-primer/manual-proof/MP4-mdbook-build-or-deferral.md docs/changes/markdown-first-gym-primer/manual-proof/MP5-validation-command-ledger.md docs/changes/markdown-first-gym-primer/manual-proof/README.md docs/plans/2026-06-27-markdown-first-gym-primer.md docs/plan.md docs/workflows.md`
  - `git diff --check`

## Diff summary

M4 adds focused tests for mdBook build-or-deferral, final validation
observability, and compatibility/source-of-truth boundaries. Because `mdbook`
is not installed in the local environment, the implementation follows the
approved deferral path instead of adding `book.toml`, `SUMMARY.md`, or generated
`book/` output.

The new MP4 record documents the mdBook deferral and confirms Markdown remains
the source of truth. The new MP5 ledger records the final local command set,
states that CI was not run, and confirms no generated HTML, old generated JSON,
old schema, or old validator surface outranks Markdown.

## Findings

No blocking or required-change findings.

## Checklist coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | R31-R33 allow mdBook only after five pages exist and require deferral when it is unavailable or non-trivial. MP4 records deferral because `mdbook` is unavailable, and no mdBook config or generated output was added. |
| Test coverage | pass | `tests/test_markdown_first_mdbook.py`, `tests/test_markdown_first_observability.py`, and `tests/test_markdown_first_compatibility.py` cover mdBook deferral, command ledger evidence, no CI claim, README-linked Markdown usability, and no generated `book/` output. |
| Edge cases | pass | T11/EC12 is covered by deferral proof and tests that Markdown remains canonical without mdBook. T13 compatibility checks confirm no generated book output is active when mdBook is deferred. |
| Error handling | pass | Missing `mdbook` is handled as an explicit deferral, not an unrecorded failure or a forced dependency. |
| Architecture boundaries | pass | The change does not introduce a hosted app, generated JSON product, custom static-site scope, or derived HTML source-of-truth. |
| Compatibility | pass | README still links the first-slice Markdown pages directly; no full Chinese translation or old-platform route is activated by M4. |
| Security/privacy | pass | The privacy scan passed over first-slice pages, media, provenance records, and change-local proof records. MP5 explicitly avoids claiming CI. |
| Derived artifact currency | pass | No `book.toml`, `SUMMARY.md`, or `book/` output is added or claimed current; MP4 and MP5 record mdBook deferral. |
| Unrelated changes | concern | The working tree contains broad prior milestone artifacts, so this review is milestone-local and does not claim branch-wide cleanliness. |
| Validation evidence | pass | M4 targeted tests, full Markdown-first suite, checker, privacy scan, mdBook deferral command, excluded-scope scan, scoped lint, and diff whitespace check passed during review. |

## No-finding rationale

The implementation satisfies the approved M4 contract by choosing the durable
deferral path for unavailable mdBook, keeping Markdown canonical, adding
targeted tests for T11-T13 behavior, and recording the final local quality gate
without claiming CI, generated HTML currency, final verification, or PR
readiness.

## Residual risks

- mdBook output remains unavailable until a contributor has the `mdbook` binary
  and reruns the optional build path.
- Repository-wide markdownlint still has known broader pre-existing issues and
  is not the M4 gate.
- This review closes implementation milestones only. It does not claim final
  verification, branch readiness, PR readiness, CI success, or final readiness.

## Milestone handoff state

- Reviewed milestone: M4
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining in-scope implementation milestones: none
- Next stage: explain-change
- Final closeout readiness: ready for final closeout sequence, not final
  verification; explain-change, verify, and PR handoff remain.
