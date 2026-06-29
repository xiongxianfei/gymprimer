# Test Spec Review R3: M3A Media Proof Map

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR-M3A-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/test-spec-review-r3.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Open blockers: TSR-M3A-1
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
- Stop condition: none

## Findings

### TSR-M3A-1 - Stale edge-case IDs in test-case traceability

- Finding ID: TSR-M3A-1
- Severity: major
- Location: `specs/markdown-first-primer.test.md`, Test cases section.
- Evidence: The M3A update renumbered and expanded edge cases so EC6-EC11 now
  describe media-provenance behavior, and EC12-EC16 describe mdBook, reader
  confusion, broken source, old generated JSON, and soreness-vs-pain behavior.
  The edge-case coverage table maps those IDs correctly, but several
  individual test cases still cite old edge-case numbers:
  - T4 lists `EC8` and `EC10`, but those now mean non-approved media
    provenance and `page_refs` mismatch, not broken source or soreness wording.
  - T7 lists `EC9`, but that now means out-of-scope `media_purpose`, not old
    generated JSON conflict.
  - T10 lists `EC7`, `EC8`, and `EC10`, but those now mean media provenance
    failures, not reader confusion, broken source, or soreness wording.
  - T11 lists `EC6`, but that now means missing AI raster provenance, not
    mdBook replacing Markdown navigation.
- Required outcome: Every test case `Covers:` line must use the revised
  EC1-EC16 meanings consistently with the edge-case coverage table.
- Safe resolution path: Revise only the stale `Covers:` lines:
  - T4 should cover `EC1`, `EC2`, `EC14`, and `EC16`.
  - T7 should cover `EC15`.
  - T10 should cover `EC13`, `EC14`, and `EC16`.
  - T11 should cover `EC12`.
  Then rerun the structural scans for T/CMD/MP ownership, R1-R53, E1-E8,
  EC1-EC16, and route to test-spec-review R4.

## Review Dimensions

| Dimension | Verdict | Notes |
| --- | --- | --- |
| Governing-contract alignment | pass | The M3A proof map follows the approved spec, extension-based architecture, media ADR, and plan-review R3 sequence. |
| Requirement coverage | pass | R1-R53 appear in the requirement coverage map, and R41-R53 map to T14/T15 with appropriate unit/manual split. |
| Example coverage | pass | E1-E8 appear in the example coverage map, including AI raster, text-only, and missing-provenance cases. |
| Negative and boundary coverage | pass | Media failure behavior covers remote images, outside-media paths, unsupported extensions, missing assets, missing/incomplete/non-approved provenance, out-of-scope purpose, and `page_refs` mismatch. |
| Proof-level adequacy | pass | Deterministic media behavior is assigned to automated unit/checker tests; visual safety remains manual. |
| Milestone mapping | pass | M3A is owned separately from M3 and does not depend on MP3 beginner read-test evidence. |
| Command validity | pass | CMD10-CMD12 have owners, milestones, required-starting points, pre-milestone allowance, failure behavior, and evidence. |
| Fixture and data design | pass | Planned fixtures are deterministic and cover text-only, SVG, raster extensions, provenance variants, and invalid media paths. |
| Manual-proof boundary | pass | MP6 is bounded to human visual-safety judgment and explicit no-raster evidence. |
| Observability | pass | The test spec requires media failures to identify page path, media path, normalized `asset_path`, classification, provenance path, and stable code. |
| Determinism and isolation | pass | Unit fixtures avoid network calls and classify media by local path/extension before provenance lookup. |
| Scope and non-goals | pass | The proof map does not add hosted app, broader media taxonomy, external asset workflow, or AI coaching scope. |
| Execution economics | pass | Focused M3A checks are separated from M3 read-test and M4 mdBook/final-gate work. |
| Traceability | block | TSR-M3A-1 leaves stale EC IDs in individual test-case `Covers:` lines. |
| Implementation handoff | block | Implementation cannot rely on the proof map until TSR-M3A-1 is corrected and re-reviewed. |

## Readiness

The test spec is not approved for implementation handoff. The next stage is
test-spec revision for TSR-M3A-1.
