# Spec Review R3: Exercise Image Standard Prompt Records

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: SR-EIS-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r3.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Open blockers: SR-EIS-2
- Immediate next stage: spec revision
- Eventual test-spec readiness: not-ready
- Stop condition: prompt-record link field is not specified enough for architecture, tests, or implementation

`Immediate next stage` is the routing field; allowed values exclude `test-spec`.
Use `Eventual test-spec readiness` to assess whether test-spec authoring will
be possible after required routing stages.

## Findings

## Finding SR-EIS-2

- Finding ID: SR-EIS-2
- Severity: blocking
- Location: `specs/exercise-image-standard.md` R20A, R20C, R35, Open questions
- Evidence: R20A says a generated raster exercise image provenance row "MUST link to a repository-local prompt record," and R35 says validation fails for "missing prompt records" and "prompt-record asset-path mismatches." However, Open questions still leaves the "exact prompt-record link field name in `media/PROVENANCE.md`" to downstream artifacts. R20C defines fields inside the prompt record, but no requirement defines the observable provenance field, table column, or deterministic mapping that satisfies the row-to-record link.
- Required outcome: The spec must define the observable link contract between each generated raster provenance row and its prompt record well enough that architecture, tests, and checker implementation do not choose a field name or mapping by guesswork.
- Safe resolution path: Add a requirement-level contract such as `prompt_record` as a required `media/PROVENANCE.md` field for generated raster exercise images, with repository-local path semantics and an exact reverse `asset_path` match inside the prompt record. Alternatively, if the project does not want a new provenance column, define a deterministic path derivation rule from `asset_path` to prompt record and remove the open question that delegates the link field decision downstream. Then update Examples E8/E9, Inputs and outputs, State and invariants, Error and boundary behavior, Observability, Edge cases, and Acceptance criteria as needed.
- needs-decision rationale: none

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | block | Prompt preservation is clear in intent, but the provenance-to-prompt-record link is not observable. |
| normative language | concern | The new `MUST link` language is normative but lacks the field or deterministic mapping that makes it testable. |
| completeness | concern | Prompt record content, location, privacy, and migration are covered; the linking mechanism is incomplete. |
| testability | block | Tests cannot know whether to expect a `prompt_record` column, a derived path, or another link representation. |
| examples | concern | E8/E9 show the desired behavior but do not specify how the row links to the prompt record. |
| compatibility | pass | Existing image-purpose compatibility remains preserved, and older prompt availability is called out as a migration concern. |
| observability | concern | Prompt-record failures are named, but the observable link field or mapping is missing. |
| security/privacy | pass | Prompt records, redaction, private data, and unsafe content boundaries are covered. |
| non-goals | pass | The amendment does not expand runtime, hosted, CMS, new inventory, or image-generation scope. |
| acceptance criteria | concern | AC5A covers prompt preservation generally but cannot be mapped to an exact row-link test until SR-EIS-2 is fixed. |

## Recommendation

Request a focused spec revision for SR-EIS-2. Do not proceed to architecture, test-spec, plan revision, prompt-record backfill, or checker implementation until the spec names the provenance-to-prompt-record link contract.
