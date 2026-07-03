# Spec Review R4: Exercise Image Standard Prompt Records

## Result

- Skill: spec-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r4.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Open blockers: none for spec-review; CR-EIS-M3-2 remains open for M3 code-review resolution
- Immediate next stage: architecture
- Eventual test-spec readiness: conditionally-ready after architecture or ADR assessment confirms or amends prompt-record placement, provenance linking, and generated-raster validation flow.
- Stop condition: none

`Immediate next stage` is the routing field; allowed values exclude `test-spec`.
Use `Eventual test-spec readiness` to assess whether test-spec authoring will
be possible after required routing stages.

## Findings

None.

## Prior Finding Check

| Finding | Status | Review |
|---|---|---|
| SR-EIS-2 | resolved | The revised spec now defines `prompt_record` as a required `media/PROVENANCE.md` field for generated raster exercise images in R20, R20A, E8, E9, State and invariants, Error and boundary behavior, Observability, and EC8A-EC8E. The open question about the prompt-record link field name was removed. |

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | pass | The prompt-record amendment now identifies the required `prompt_record` field, repository-local path semantics, prompt-record location, reverse `asset_path` matching, and failure behavior. |
| normative language | pass | The new `MUST` requirements are testable or manually verifiable, and existing requirement IDs remain stable through additive `R20A`-style IDs. |
| completeness | pass | Normal, missing, out-of-repository, path-shape, reverse-match, redaction, old-data, and migration cases are covered at spec level. |
| testability | pass | Downstream tests can now assert `prompt_record` field presence, repository-local path shape, existing prompt-record file, reverse `asset_path` match, and exact prompt text presence. |
| examples | pass | E8 and E9 demonstrate the `prompt_record` field and missing-field failure. |
| compatibility | pass | Existing image-purpose compatibility and older prompt availability migration limits remain preserved. |
| observability | pass | Prompt-record validation output names affected asset path, `prompt_record` path, failure category, and mismatched or missing field. |
| security/privacy | pass | Prompt records, redaction, private data, and unsafe content boundaries are covered without expanding product scope. |
| non-goals | pass | The amendment does not authorize image generation, broad optimization, runtime systems, hosted media, CMS, or personalized coaching. |
| acceptance criteria | pass | AC5A now maps to observable `prompt_record` behavior. |

## Recommendation

Approve the prompt-record spec amendment. Normalize `specs/exercise-image-standard.md` to `approved` before downstream reliance. The next lifecycle stage is architecture or ADR assessment because the amendment changes the generated-raster provenance contract and validation flow.
