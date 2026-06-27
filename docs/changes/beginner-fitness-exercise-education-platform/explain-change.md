# Explain Change: Content Schema Foundation M1-M4

## Summary

This change implements the repository-native content foundation for GymPrimer's beginner exercise-literacy platform. It creates structured source areas for reviewed cards, taxonomy, policies, schemas, media, generated output, validation tools, tests, generated evidence, and workflow records.

The implementation exists to prove the approved content contract before any public UI, CMS, AI assistant, personalization, or broad exercise library is built. It turns the approved direction into a local, deterministic validation pipeline and a generated public content package for one reviewed example card.

Current workflow state: all implementation milestones M1-M4 are closed after code review. The next stage is `verify`; branch readiness, PR readiness, CI success, and final verification are not claimed here.

## Problem

The accepted proposal identifies a beginner fitness education gap: users need reliable exercise literacy before workout prescription. Beginners need to understand what an exercise trains, how to set up equipment, how to execute phases, what they should feel, what mistakes to avoid, and when to stop.

Before this change, the repository had governance and planning artifacts but no executable content schema foundation. There was no repository source layout, content schema files, taxonomy fixture, reviewed example card, media examples, validator, privacy scan helper, tests, generated public output, or validation evidence.

## Decision Trail

| Decision source | Decision | How this diff follows it |
| --- | --- | --- |
| Proposal | Build a structured exercise-literacy platform, not an AI-first chatbot, workout generator, rehab tool, or trainer CRM. | The implementation builds repository-native content cards, validation, review gates, and generated public content only. |
| Proposal | Launch English-first while making Chinese a first-class future locale. | The schema and validator require `en-US`, accept `zh-Hans`, and reject bare `en`. |
| Proposal and vision | Treat reviewed text plus SVG step cards as canonical media; video is supplemental only. | The example card references three canonical SVG steps with accessible text; supplemental media is optional and cannot become source of truth. |
| Spec R1-R18 | Define card identity, required localized fields, taxonomy, SVG media, safety notes, no-diagnosis rules, regressions, and progression readiness cues. | M2 validator rules and tests enforce these content-contract fields. |
| Spec R19-R29 | Keep review and publication lifecycle separate, enforce transitions, preserve history, and require digest-scoped review evidence. | M3 validator rules and fixtures validate lifecycle events, approval events, review-sensitive edits, and publication gates. |
| Spec R30-R33, R40 | Produce actionable, privacy-safe validation output; support license and provenance metadata without collecting user PII. | `validate_content.py`, `privacy_scan.py`, generated reports, license/provenance checks, and privacy tests cover this. |
| Spec R34-R36, R38-R39 | Support discovery fields, relationships/prompts, schema versioning, migration checks, and generated output boundaries. | M4 emits deterministic public content with discovery, relationships, comprehension placeholders, and schema version. |
| Architecture and ADR | Use repository-native reviewed content as source of truth; generated output is non-authoritative publication output. | The source lives under `content/`, `media/`, and `schemas/`; generated reports and public package live under `generated/`. |
| Plan | Split work into M1 scaffold, M2 content validation, M3 lifecycle/review validation, and M4 generated output. | The implementation and review records follow those four milestones. |

## Diff Rationale By Area

| Area | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| `content/` | Added example card, v1 taxonomy, review-routing policy, and README files. | Establish the repository-native source model chosen by the ADR and needed by the validator. | Architecture building block view; spec R1-R8, R19-R24, R32-R33. | `generated/validation-report.json`; M2/M3 tests. |
| `content/cards/examples/ex-lat-pulldown.json` | Added one reviewed example exercise card. | Provide a minimal valid card that exercises locale, taxonomy, safety, SVG, review, license, and generated-output behavior without creating a broad library. | Proposal first-release direction; plan M2/M4. | `tests/test_content_contract_m2.py`; `generated/public-content.json`. |
| `content/taxonomy/v1.json` | Added v1 controlled enums and seed muscle/equipment/movement values. | Make validation deterministic and prevent unknown locale/taxonomy drift. | Spec R6-R8, R20-R21, controlled enum requirements. | Unknown enum/taxonomy tests; validation report. |
| `content/policies/review-routing-v1.json` | Added executable review-routing policy data. | Keep review routing as repository-native policy data rather than duplicated hard-coded logic. | M3 code-review CR-M3-1; spec review-routing matrix. | `tests/test_review_routing_m3.py`; `generated/review-routing-validation-report.json`. |
| `media/svg/examples/` | Added three SVG step cards for lat pulldown. | Prove canonical SVG step references and accessible media text for source-of-truth movement instruction. | Spec R9-R11; architecture media boundary. | SVG step count and accessible text tests. |
| `schemas/` | Added schema summary files for cards, taxonomy, media, review events, audit events, and validation reports. | Create machine-readable contract surfaces without adding external schema tooling. | Plan M1; architecture schema area. | Validator reads schema version; tests assert report shape. |
| `tools/validation/validate_content.py` | Added the local validator CLI covering source discovery, schema versioning, card validation, taxonomy/media checks, safety blockers, license/provenance gates, lifecycle/review/audit checks, review-routing policy loading, and public package emission. | This is the architecture's validation and publication gate. It proves publication is a validation result, not an author assertion. | Spec R1-R40; architecture validation and publication gate. | Full test suite; generated validation reports; public output diff. |
| `tools/validation/privacy_scan.py` | Added a local negative-match privacy scanner with explicit exit codes. | Plain `rg` has unsuitable no-match semantics for privacy checks. The wrapper makes "no forbidden patterns found" a passing result. | Plan-review PR1; spec R31/R40. | `tests/test_privacy_scan.py`; `generated/privacy-scan-report.json`. |
| `tests/` | Added unit and integration tests for M1-M4. | Convert the content contract and review findings into executable proof. | `specs/content-schema.test.md`; code-review findings CR-M2-1/2, CR-M3-1/2, CR-M4-1. | `generated/test-results.txt` records 60 passing tests. |
| `generated/` | Added validation reports, public content package, privacy report, and manual proof records MP1-MP5. | Provide durable local evidence for validation, source boundaries, privacy, scope, and command documentation. | Test spec milestone proof expectations. | Generated reports and manual proof files. |
| `README.md`, `generated/README.md`, `tools/validation/README.md` | Documented local validation commands, generated output, and no-CI status. | Make the developer workflow executable without implying CI exists. | Plan M4; test spec command ownership. | MP5 and validation commands. |
| `docs/changes/...` | Added review log, review-resolution history, code-review records, change metadata, and this explanation. | Preserve workflow traceability from proposal through implementation and review closeout. | Workflow guide; stage skills. | Review log through `code-review-m4-r2`. |
| `docs/plans/...`, `docs/plan.md`, `docs/workflows.md` | Updated milestone states and routing through M1-M4 closeout. | Keep the active plan and workflow state synchronized with reviewed implementation status. | Plan closeout rules. | State-sync `rg` command. |

## Tests Added Or Changed

| Test file | Coverage | Why this level is appropriate |
| --- | --- | --- |
| `tests/test_validator_cli.py` | M1 CLI behavior, deterministic report shape, missing/no-card handling, and privacy-safe reporting. | Unit/smoke level is enough for scaffold and command contract. |
| `tests/test_privacy_scan.py` | Negative-match scanner exit codes for clean output, forbidden terms, missing path, and invalid regex. | Direct unit tests prove the wrapper contract that replaced raw `rg`. |
| `tests/test_content_contract_m2.py` | Valid `en-US` and `zh-Hans` card shape; invalid locale, enum, taxonomy, SVG, safety, licensing, provenance, supplemental-media, and review metadata cases. | Integration tests run the validator against fixture directories, matching the repository-native architecture boundary. |
| `tests/test_lifecycle_m3.py` | Review/publication status separation, invalid transitions, review-sensitive edits, approval/audit events, direct mutation rejection, and review-completion evidence. | Integration tests are required because lifecycle behavior spans card state, events, digests, and reports. |
| `tests/test_review_routing_m3.py` | Loaded review-routing policy, fixture-only route enforcement, policy metadata, cumulative review tiers, and policy shape errors. | These tests prove policy data is the executable source of truth. |
| `tests/test_generated_output_m4.py` | Public package determinism, discovery fields, source-boundary exclusions, 60-card performance smoke, and the CR-M4-1 boundary matrix. | End-to-end validation is appropriate because generated output is the publication boundary consumed by future UI/search. |

The CR-M4-1 resolution specifically added `test_public_output_excludes_all_publication_boundary_failures`, which proves the public package excludes isolated unpublished, hidden, superseded, internal-only license, review-expired, and blocked-rehab records while including a valid control card.

## Validation Evidence Before Final Verify

Local validation evidence recorded in the plan and generated files:

- `python3 -m unittest discover -s tests`
- `python3 -m unittest tests.test_generated_output_m4`
- `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json`
- `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json --emit-public generated/public-content.json`
- `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out /tmp/gymprimer-validation-report.json --emit-public /tmp/gymprimer-public-content.json`
- `diff -u generated/public-content.json /tmp/gymprimer-public-content.json`
- `python3 tools/validation/validate_content.py --source tests/fixtures/invalid --schemas schemas --media media --out generated/invalid-fixture-report.json --expect-invalid`
- `python3 tools/validation/validate_content.py --source tests/fixtures/lifecycle --schemas schemas --media media --out generated/lifecycle-validation-report.json --expect-mixed`
- `python3 tools/validation/validate_content.py --source tests/fixtures/review-routing --schemas schemas --media media --out generated/review-routing-validation-report.json --expect-mixed`
- `python3 tools/validation/privacy_scan.py --pattern 'private|/home/|secret|PHI|personal health' -- generated/`
- State-sync `rg` command across workflow, plan, architecture, ADR, and spec artifacts.

Latest recorded local test evidence: `generated/test-results.txt` shows 60 tests passing. Latest generated privacy evidence: `generated/privacy-scan-report.json` reports pass with no findings. CI is not configured and no hosted CI run is claimed.

Manual proof records:

- MP1 lifecycle-state synchronization inspection.
- MP2 generated-output source-boundary inspection.
- MP3 fixture privacy spot-check.
- MP4 scope and non-goal inspection.
- MP5 developer-command documentation check.

## Review Resolution Summary

Material findings were resolved through later same-stage review rounds:

| Stage | Findings | Final disposition |
| --- | ---: | --- |
| Spec review | 4 findings across R1-R2 | Resolved by `spec-review-r3`. |
| Plan review | 1 finding | Resolved by `plan-review-r2`. |
| Test-spec review | 2 findings | Resolved by `test-spec-review-r2`. |
| Code review M2 | 2 findings | Resolved by `code-review-m2-r2`. |
| Code review M3 | 2 findings | Resolved by `code-review-m3-r2`. |
| Code review M4 | 1 finding | Resolved by `code-review-m4-r2`. |

Durable record: `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`.

The final implementation review, `code-review-m4-r2`, recorded `clean-with-notes`, closed M4, and left no implementation milestones open.

## Alternatives Rejected

- CMS-first storage was rejected because the schema and review workflow needed to be proven before choosing hosted content infrastructure.
- Application database source-of-truth was rejected because there is no app stack yet and repository reviewability is central to the OSS posture.
- Static Markdown-only pages were rejected because the approved contract requires structured locale branches, taxonomy, lifecycle, review, audit, media, licensing, and validation behavior.
- Video-first or video-as-source-of-truth media was rejected because the vision and spec make SVG step cards plus reviewed text canonical.
- AI-first assistance was rejected for MVP because unconstrained generated exercise guidance is unsafe and harder to audit than reviewed content.
- Broad scanner adoption, such as Semgrep/Gitleaks/Presidio, was deferred because PR1 was an immediate negative-match exit-code problem; the local wrapper solves that without adding dependencies.
- External validation dependencies and package-manager setup were deferred because Python standard-library tooling was enough to prove the first content-contract slice.

## Scope Control

Preserved non-goals:

- No frontend, search UI, glossary UI, quiz UI, analytics UI, or deployment target.
- No CMS, application database, authentication, accounts, payments, or user data collection.
- No AI assistant, retrieval layer, or generated exercise guidance as source of truth.
- No personalized workout generator, medical screening, rehabilitation protocol, diagnosis, or injury-treatment workflow.
- No broad 40-60 card library; only one example card was added to prove the contract.
- No CI success claim; CI remains unconfigured.
- No final legal Terms of Use, Privacy Policy, incident response process, or public beta readiness claim.

## Risks And Follow-Ups

- CI remains absent. A later CI-maintenance slice should run the local validation commands in CI before PR or release automation depends on them.
- The validator is intentionally JSON/Python-standard-library first. If content volume or schema complexity grows, the project may need JSON Schema tooling or a structured parser, but that should be a reviewed follow-up.
- The taxonomy contains v1 seed values, not the complete future muscle/equipment universe.
- The example card is validation-oriented and not a launch library.
- Legal documents, final disclaimer owner, incident-response process, elevated-risk clinical policy, and CC BY 4.0 contribution operations need follow-on specs before public beta.
- A future UI/search layer must consume `generated/public-content.json`, not raw `content/` source files.

## Readiness

This explanation is complete for the reviewed M1-M4 implementation. The change is ready for the next workflow stage: `verify`.

This does not claim final verification, branch readiness, PR readiness, hosted CI success, or public release readiness.
