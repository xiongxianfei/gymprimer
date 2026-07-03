# Test Spec Review R5: Prompt Record M3A Proof Map

## Result

- Skill: test-spec-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/test-spec-review-r5.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: not-required
- Open blockers: none for M3A implementation; `CR-EIS-M3-2` remains open for later M3 code-review resolution
- Immediate next stage: implement
- Implementation handoff: allowed
- Stop condition: none

## Findings

None.

## Reviewed Surfaces

- `specs/exercise-image-standard.test.md`
- `specs/exercise-image-standard.md`
- `docs/plans/2026-07-03-exercise-image-standard.md`
- `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r4.md`
- `docs/changes/exercise-image-standard-and-optimization/reviews/architecture-review-r2.md`
- `docs/changes/exercise-image-standard-and-optimization/reviews/plan-review-r2.md`

## Review Dimensions

| Dimension | Verdict | Notes |
| --- | --- | --- |
| Governing-contract alignment | pass | The proof map follows approved spec-review R4, architecture-review R2, and plan-review R2 for `prompt_record` field semantics, repository-local prompt records, reverse `asset_path` matching, exact prompt text or explicit redaction, and no reader-facing prompt embedding. |
| Requirement coverage | pass | R20-R20H, R35-R37, AC5A, and compatibility/migration expectations now map to EIS-T19, EIS-T20, EIS-T21, EIS-CMD7, EIS-CMD9, and scoped privacy evidence. |
| Example coverage | pass | E8 and E9 are mapped to EIS-T19 and EIS-T20. Existing E1-E7 coverage remains intact. |
| Negative and boundary coverage | pass | EC8A-EC8E cover missing `prompt_record`, invalid path shape, mismatched reverse `asset_path`, missing exact prompt text, and unavailable older prompts. |
| Proof-level adequacy | pass | Deterministic checker behavior is mapped to unit/integration tests; real M3 backfill decisions are mapped to migration/code-review evidence where automation cannot know prompt recoverability. |
| Milestone mapping | pass | M3A owns prompt-record checker support, fixture tests, M3 backfill or replacement decisions, and focused commands before M3 returns to code-review. |
| Command validity | pass | EIS-CMD9 is explicitly owned by M3A, while EIS-CMD2, EIS-CMD3, EIS-CMD7, EIS-CMD8, and scoped privacy checks remain tied to active milestone evidence. Broad EIS-CMD4 remains verify-owned. |
| Fixture and data design | pass | Temporary-root fixtures, prompt-record paths under `media/prompts/exercises/<exercise-slug>/<asset-stem>.md`, placeholder image bytes, and repository-relative `asset_path` values are deterministic and local. |
| Manual-proof boundary | pass | EIS-T21 bounds the manual/migration question to exact prompt recoverability and prohibits invented prompts. Existing visual-safety and comprehension manual proof remains separate for M3. |
| Observability | pass | EIS-T19 and EIS-T20 require stable prompt-record failure categories for affected asset path, `prompt_record` path, missing file, reverse-match mismatch, missing prompt text, and redaction-note failures. |
| Determinism and isolation | pass | The proof map avoids network, external image generation, time-sensitive behavior, shared mutable state, and raster pixel inspection. |
| Scope and non-goals | pass | The proof map does not add runtime, CMS, API, user input, video, medical-effectiveness testing, or legacy image migration beyond the approved prompt-record compatibility boundary. |
| Execution economics | pass | Focused M3A commands stay local; broad privacy scanning remains lifecycle closeout / verify rather than an implementation-milestone blocker. |
| Traceability | pass | Prompt-record requirements, examples, edge cases, commands, fixtures, observability, migration, and readiness all link to stable EIS IDs and the M3A milestone. |
| Implementation handoff | pass | Implementation can proceed for M3A without guessing how prompt-record behavior must be proved. |

## No-Finding Rationale

The amended proof map covers the approved prompt-record contract with both happy-path and failure-path tests. It also handles the risky part of the already-generated M3 images by requiring either recoverable exact prompt records, explicit compatibility limitation, or replacement with fresh prompt-backed assets. No upstream ambiguity or unowned command remains for M3A.

## Readiness

The M3A prompt-record proof-map amendment is approved. Implementation handoff is allowed for M3A only; this does not close `CR-EIS-M3-2`, approve M3 code-review re-review, verify the branch, or authorize PR handoff.
