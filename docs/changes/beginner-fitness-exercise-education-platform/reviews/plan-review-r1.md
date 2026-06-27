# Plan Review: Content Schema Foundation R1

## Result

- Skill: plan-review
- Review status: changes-requested
- Material findings: PR1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/beginner-fitness-exercise-education-platform/reviews/plan-review-r1.md`
- Review log: `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`
- Review resolution: `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`
- Open blockers: PR1
- Immediate next stage: plan revision

## Findings

### PR1 - Privacy scan validation commands have inverted success semantics

- Finding ID: PR1
- Severity: major
- Location: `docs/plans/2026-06-26-content-schema-foundation.md` M1 validation commands, M4 validation commands, and Validation plan
- Evidence: M1 lists `rg -n "private|/home/|secret|PHI" generated/validation-report.json`; M4 and the global validation plan list `rg -n "private|/home/|secret|PHI|personal health" generated/`. Plain `rg` exits with status 1 when it finds no matches. For privacy scans, no matches are the desired passing state, so the plan's validation command would fail when the output is clean and pass when it finds forbidden strings.
- Required outcome: The plan must make negative-match privacy scans executable with correct pass/fail semantics.
- Safe resolution path: Replace those validation commands with shell-negated commands such as `! rg -n "private|/home/|secret|PHI" generated/validation-report.json` and `! rg -n "private|/home/|secret|PHI|personal health" generated/`, or use a small validation helper that exits 0 only when forbidden patterns are absent.

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| self-contained context | pass | The plan names upstream artifacts, repository gaps, source layout, non-goals, milestones, and current handoff state. |
| source alignment | pass | Milestones map to approved spec requirements and the repository-native architecture without adding UI, CMS, AI, or public content scope. |
| milestone size | pass | Four milestones are reviewable and split scaffold, content validation, lifecycle/review gates, and generated output. |
| sequencing | pass | M1 establishes harness before M2/M3 rules; M4 waits for validation gates before generated output. |
| scope discipline | pass | Follow-on safety/governance, licensing, UX/search, CI, and full content library work are kept out of this slice. |
| validation quality | block | PR1 makes privacy-scan validation commands fail on the desired clean-output case. |
| TDD readiness | concern | The plan is ready to feed a test-spec once PR1 is fixed; test-spec must still define exact fixtures and proof mapping before implementation. |
| risk coverage | pass | Risks cover schema overgrowth, authoring ergonomics, safety overreach, generated output authority, no CI, digest stability, and example-content confusion. |
| architecture alignment | pass | Plan implements `schemas/`, `content/`, `media/`, `tools/validation/`, `generated/`, repository-native source, and deterministic generated output. |
| operational readiness | concern | No CI exists yet, but the plan honestly uses local validation and defers CI through `ci-maintenance`. |
| plan maintainability | pass | Handoff summary, milestones, validation notes, decision log, and recovery paths are explicit. |

## Exact Suggested Changes

- In M1, change the privacy scan command to `! rg -n "private|/home/|secret|PHI" generated/validation-report.json`.
- In M4, change the privacy scan command to `! rg -n "private|/home/|secret|PHI|personal health" generated/`.
- In the global Validation plan, make the same negative-match command change and describe that exit 0 means no forbidden patterns were found.

## Readiness

This direct review remains isolated and does not automatically revise the plan or continue to test-spec. After PR1 is resolved, rerun plan-review. No owner decision is needed.
