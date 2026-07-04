# M4 Validation Ledger

## Scope

- Change ID: `exercise-method-guidance`
- Milestone: M4
- Proof IDs: EMG-M3 and EMG-T12 partial smoke for M4.
- Evidence date: 2026-07-04
- Criteria: M4 manual proof records exist, privacy and Markdown validation pass, full local unittest suite passes, deferred method types remain inactive, and broad rollout is not authorized by this proof slice.

## Result

Pass for M4 implementation handoff.

M4 records the required manual evidence and does not authorize broad rollout. Final local verification remains assigned to Lifecycle Closeout after M4 code-review.

## Validation Commands

| Command ID | Command | Result | Evidence |
| --- | --- | --- | --- |
| EMG-CMD10 | `python3 tools/checks/check_privacy.py docs/changes/exercise-method-guidance` | pass | Checked 18 files; privacy pass. |
| EMG-CMD8 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md principles exercises patterns` | pass | Checked 22 Markdown files; pass. |
| EMG-CMD11 | `python3 -m unittest discover -s tests` | pass | Ran 114 tests; OK. |
| hygiene | `git diff --check` | pass | No whitespace errors. |

## Manual Proof Records

| Proof ID | Artifact | Result | Re-run trigger |
| --- | --- | --- | --- |
| EMG-M1 | `docs/changes/exercise-method-guidance/manual-proof/method-source-audit.md` | pass | Any edit to proof-slice method guidance, method sources, source citations, starter ranges, stop guidance, or method type assignment. |
| EMG-M2 | `docs/changes/exercise-method-guidance/manual-proof/beginner-comprehension.md` | pass | Any edit to proof-slice method wording, pattern-preview wording, principle-page links, or stop/progression language. |
| EMG-M3 | `docs/changes/exercise-method-guidance/manual-proof/validation-ledger.md` | pass | Any edit to method type lists, templates, fixtures, proof-slice pages, or related specs after this ledger. |

## Deferred Method Type Guardrail

Search command:

```sh
rg -n "loaded_carry|basic_cardio_equipment" specs docs/templates exercises patterns tests docs/changes/exercise-method-guidance
```

Result: pass.

Observed mentions are limited to:

- `tests/test_exercise_method_guidance.py`, where the values are rejected as inactive method types.
- `specs/exercise-method-guidance.md`, where the values are named as deferred or future-scope values.
- `specs/exercise-method-guidance.test.md`, where the values are named as rejected/deferred test cases and manual guardrail criteria.

No promoted exercise page, pattern page, template valid example, or change-local proof record activates `loaded_carry` or `basic_cardio_equipment`.

## Broad-Rollout Gate

Broad exercise-page rollout is not authorized by M4. This change proves only the six-page proof slice and the supporting principle page. A later reviewed plan must select the next batch of exercise pages before any broad update starts.

## Residual Risks

- M4 evidence is bounded to the approved proof slice and does not represent a complete exercise-library audit.
- Source support is manually reviewed rather than mechanically proven at the claim-semantics level.
- Beginner comprehension evidence uses a non-identifying reviewer proxy rather than a formal usability study.
- Hosted CI was not observed; only local commands above were run.
