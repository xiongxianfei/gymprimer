# Learn Session: Review Finding Summary Titles

## Frame

- Trigger: explicit `$learn` invocation after maintainer observation that review findings without short summary titles are inconvenient to review.
- Trigger type: explicit maintainer request and contributor observation.
- Scope: readability and review ergonomics for material finding records, using `test-spec-review-r1` for the forward-head-posture pattern architecture as the concrete evidence.
- Evidence in scope:
  - `docs/changes/forward-head-posture-pattern-architecture/reviews/test-spec-review-r1.md`
  - `.agents/skills/test-spec-review/assets/material-finding.md`
  - `.agents/skills/test-spec-review/assets/review-result-skeleton.md`
  - `docs/changes/repository-layout-normalization/reviews/plan-review-r1.md`
  - `docs/changes/repository-layout-normalization/reviews/test-spec-review-r1.md`
- Explicit exclusions:
  - No skill, workflow, template, or review-record rewrite in this learn session.
  - No claim that all review skills have the same issue.
  - No PR, verification, or implementation readiness claim.
- Prior learnings reviewed:
  - `docs/learn/sessions/2026-06-29-responsible-breadth-content-quality.md`
  - `docs/learn/topics/content-quality.md`
- Session record path: `docs/learn/sessions/2026-06-30-review-finding-summary-titles.md`

## Observe

- OBS-001: `test-spec-review-r1` records material findings as `## Finding TSR-FHP-1` and `## Finding TSR-FHP-2`. The headings expose only the ID; the short meaning appears later in `Location`, `Evidence`, or final summary text, so scanning the review requires opening each finding body.
- OBS-002: The active `test-spec-review` material-finding asset uses `## Finding <finding ID>` and has no dedicated short summary field, so the generated shape encourages ID-only headings.
- OBS-003: A prior plan review record used a more scannable heading, `### PR-RLN-1 - Plan assigns test-spec authoring to an implementation milestone`, which lets reviewers understand the issue directly from the finding list.
- OBS-004: A prior test-spec-review record for repository layout normalization also used ID-only finding headings, which suggests this is likely a template/style gap for at least test-spec-review records, not only a one-off writing miss.

## Classify

| Observation | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
| --- | --- | --- | --- | --- | --- |
| OBS-001 to OBS-004 | process-follow-up | candidate process-follow-up | update the relevant review-finding asset or skill guidance if the maintainer confirms the change | Not yet routed; maintainer asked for best practices, not an artifact edit | The evidence shows a reusable review-readability problem, but changing review templates or skill behavior needs an owning artifact update. This session records the best-practice direction without making it authoritative. |

## Route

- No topic file was updated.
- No skill asset, workflow guide, or review template was changed.
- Candidate follow-up: update review material-finding templates to include short summary titles, for example `## Finding <ID> - <short summary>`, and optionally a `- Summary:` field for review logs or generated indexes.

## Best Practices

For material review findings, prefer a scan-first structure:

1. Put the short summary in the heading: `## Finding TSR-FHP-1 - Manual semantic checks are underspecified`.
2. Keep the stable ID first in metadata: `- Finding ID: TSR-FHP-1`.
3. Use a concise problem phrase, not a vague category. Prefer "Validation commands lack owner and milestone" over "Command issue".
4. Make the summary outcome-neutral and factual. It should describe the defect, not the fix.
5. Keep summary titles short enough for review logs, usually 6 to 12 words.
6. Reuse the exact summary in `review-log.md` or `review-resolution.md` when helpful.
7. Preserve full fields for rigor: severity, location, evidence, required outcome, safe resolution path, and decision rationale still carry the proof.

Good examples for the current findings:

- `TSR-FHP-1 - Manual semantic checks are underspecified`
- `TSR-FHP-2 - Validation commands lack ownership metadata`

## No Durable Lesson Rationale

This session records a candidate process improvement, not a durable topic-file lesson. The issue is supported by current evidence and one prior contrast, but adopting it as policy should happen through the relevant skill/template or workflow artifact.

## Validation

- Session file created by direct inspection of the named review records and skill assets.
