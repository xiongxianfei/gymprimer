# Project Constitution

This constitution defines the durable rules for GymPrimer. It governs agentic development, human review, and repository changes. It is not a roadmap, feature list, or content template.

## Project Purpose

GymPrimer is an open-source Markdown primer for gym beginners. It teaches exercise and training literacy before personalization through short, citation-backed pages that a beginner can read directly in the repository.

The project serves adults in their first ninety days of regular gym training, people returning after a long break, and the maintainers, authors, translators, illustrators, and reviewers who improve the Markdown corpus. It MAY publish static, citation-based consumer education about common exercises, non-diagnostic patterns, well-studied common conditions, programming principles, and generic program examples when an accepted proposal, spec, architecture, and validation plan define the boundaries. It MUST NOT become a workout planner, clinical rehabilitation product, injury-diagnosis tool, AI coach, or video-first source of truth.

Markdown source is the primary product. Optional generated HTML, generated validation output, future search indexes, and future websites are derived conveniences unless a later accepted proposal changes that boundary.

## Source Of Truth Order

When artifacts conflict, agents and reviewers MUST use this order:

1. `CONSTITUTION.md`
2. `VISION.md`
3. Accepted proposals in `docs/proposals/`
4. Approved specs in `specs/`
5. Architecture artifacts and ADRs in `docs/architecture/` and `docs/adr/`
6. Change-local plans and rationale in `docs/changes/<change-id>/`
7. Tests, fixtures, validation evidence, and audit records
8. Markdown content, source files, schemas, configuration, and generated artifacts
9. Chat messages and issue comments

Changes that intentionally revise a higher-ranked artifact MUST update that artifact first or in the same change. Chat context MUST NOT silently override durable project artifacts.

Accepted artifacts from the prior structured-platform direction remain historical until explicitly superseded, archived, or reactivated by a later accepted proposal. Agents MUST NOT treat old schema, lifecycle, generated-output, or expert-review artifacts as active guidance when they conflict with the accepted Markdown-first proposal and current `VISION.md`.

## Spec-Driven Rules

Substantive changes MUST have a durable spec before implementation when they affect user-visible behavior, Markdown card contracts, citation policy, safety language, media policy, localization, licensing, public contribution rules, public URLs, generated output, validation tooling, configuration, or data migration.

Specs MUST identify requirements with stable IDs and include acceptance criteria that can be tested, reviewed, or manually verified. Specs MUST distinguish goals, non-goals, compatibility expectations, security and privacy constraints, accessibility expectations, and open questions.

Small editorial fixes, typo fixes, citation formatting fixes, and documentation clarifications MAY proceed without a spec when they do not change scope, commitments, safety meaning, licensing, behavior, schema, or user obligations.

Formatting-only edits MUST NOT split one existing line into multiple lines, or join multiple existing lines into one line, merely to make text look better. Line wrapping is allowed only when required by a substantive content edit, a reviewed generated format, or an explicit repository formatting rule.

## Test-Driven Rules

Behavior changes MUST be proven by tests or deterministic validation records whenever possible. When automation is not yet possible, the change MUST record a bounded audit record that names the checked files, criteria, result, and residual risk. Bug fixes MUST start with a failing regression test or a documented reproduction that fails before the fix.

Markdown content quality rules SHOULD be automated as soon as structure exists: source sections, claim-level safety citations, disclaimer presence, excluded-scope checks, media path checks, link checks, license/provenance checks, and privacy scans.

Claims about beginner comprehension, citation coverage, localization readiness, review currency, or publication readiness MUST be tied to repeatable checks, audit records, or documented reader-test evidence. Agents MUST NOT make unverifiable completion claims.

If no test framework, markdown linter, link checker, mdBook binary, or CI exists, the change MUST report that gap and the exact manual checks performed.

## Architecture Rules

Architecture decisions are required before implementation when a change affects multiple components, source-of-truth boundaries, repository layout, Markdown URL compatibility, localization structure, media storage, generated output, validation tooling, public interfaces, security boundaries, deployment, or archival of prior artifacts.

Architecture artifacts MUST record tradeoffs, rejected options, migration implications, compatibility surfaces, and how the decision preserves the refusals in `VISION.md`. Implementation details belong in architecture or plans, not in the vision.

The active content model MUST preserve these commitments unless a later accepted proposal revises them: GitHub-readable Markdown pages as source of truth, citation-based authority, page-local sources, global reusable source index, prominent disclaimers, conservative beginner scope, no diagnosis, no individualized medical advice or treatment, original or clearly licensed media only, and optional derived HTML.

## Security And Privacy Rules

Secrets, credentials, private keys, personal contact details, private machine paths, private reviewer or user data, and private health information MUST NOT be committed. Logs, fixtures, examples, and generated artifacts MUST avoid sensitive personal data unless a spec explicitly defines a safe anonymized fixture.

Health-adjacent content MAY describe static, citation-based consumer education for common patterns and well-studied conditions when a reviewed spec defines page contracts, source quality, red-flag routing, review cadence, and proof obligations. It MUST avoid diagnosis, individualized medical advice, treatment plans, return-to-training prescriptions, active rehabilitation protocols, posture-correction promises, and injury-specific protocols. It MUST distinguish general education from personalized care, route red flags to qualified professionals or emergency care, and use claim-level citations from public, named sources for safety warnings.

AI-generated exercise guidance MUST NOT become source-of-truth content. AI MAY assist drafting only when a human author verifies the wording, sources, scope, and safety claims before the content is treated as project material.

Dependencies, media assets, diagrams, screenshots, source references, and content contributions MUST be license-compatible with the repository's licensing posture or explicitly documented as external non-source assets with allowed use.

## Compatibility Rules

Stable Markdown paths, headings used as anchors, source reference IDs, card filenames, media references, license terms, contribution terms, validation command names, config names, public URLs, and generated output formats MUST be treated as compatibility surfaces once published or documented for contributors.

Breaking changes MUST have a migration plan, deprecation or versioning notes when applicable, tests or fixtures that prove the migration, and documentation updates.

English is the first content language. Chinese aliases MAY appear where useful. Full Chinese translation MUST use a reviewed separate-locale structure before it becomes active source content.

mdBook or other static HTML output MAY supplement repository browsing, but generated HTML MUST NOT become the canonical source of truth without a new accepted proposal and architecture decision.

## Verification Rules

Before completion, every change MUST report the exact validation commands run and their outcomes. If a command cannot be run, the report MUST say why and identify residual risk.

CI configuration, when present, SHOULD run the same core checks expected locally. Agents MUST NOT claim CI passed unless they observed the run result.

For documentation-only changes, validation MAY be limited to relevant linting, link checks, word-count checks, marker checks, source-order consistency checks, and direct file review.

Vision and constitution updates MUST verify required sections, source-of-truth consistency, README marker integrity when README front matter is affected, and absence of stale governance language that conflicts with the new direction.

## Review Rules

Proposal review SHOULD be used when problem framing, scope, strategic fit, or trust model is uncertain. Spec review MUST precede implementation for material specs. Architecture review MUST precede implementation for hard-to-reverse design decisions. Plan review SHOULD precede multi-milestone implementation.

Code review MUST be used before claiming completion for implementation work that changes behavior, validation tooling, generated output, workflows, security posture, licensing posture, or user-facing content. Final verification MUST be performed after review issues are resolved and before PR handoff.

Review findings MUST lead with risks, bugs, missing tests, compatibility issues, source-order conflicts, or governance violations. Summaries are secondary.

## Documentation Rules

Docs MUST be updated with the change they describe. Changes to project identity update `VISION.md` and, when applicable, README vision front matter. Changes to governance update `CONSTITUTION.md` and, when applicable, `AGENTS.md`. Changes to architecture update `docs/architecture/` or `docs/adr/`. Changes to workflow expectations update workflow documentation or the relevant change-local artifact.

Specs, plans, tests, and implementation MUST stay traceable through stable requirement IDs where specs exist. Lessons that reveal recurring mistakes or durable process improvements SHOULD be captured with the learning workflow instead of left only in chat.

README content outside managed marker blocks MUST NOT be rewritten as part of artifact synchronization unless the user explicitly authorizes broader README editing.

## Agent Behavior Rules

Agents MUST state important assumptions, blockers, source conflicts, and validation gaps. Agents MUST NOT silently broaden scope, invent external facts, fake test results, claim unobserved CI, discard user changes, or perform unrelated refactors.

Agents MUST inspect existing files before editing, prefer repository patterns over new abstractions, keep changes focused, and preserve a dirty working tree unless explicitly instructed otherwise.

Agents MUST preserve existing line breaks when editing nearby text unless changing the line break is necessary for the substantive edit or an explicit formatting rule. Cosmetic wrapping and unwrapping are formatting churn.

Agents MUST use durable artifacts for durable decisions. Chat-only decisions are acceptable for temporary coordination, but project rules, requirements, architecture, verification evidence, and accepted exceptions belong in the repository.

Agents MUST NOT introduce secrets, private data, unlicensed media, generated exercise guidance as source of truth, or medical advice.

## Standard Workflow And Manual Skill Use

The standard workflow for material work is:

1. Explore or research when assumptions are uncertain.
2. Create or update a proposal when direction or scope needs a decision.
3. Run proposal review when direction, scope, or strategic fit is material.
4. Create or update a spec for observable requirements.
5. Run spec review for material specs.
6. Create or update architecture for cross-component or hard-to-reverse decisions.
7. Run architecture review when architecture is material.
8. Create or update a plan for multi-step execution.
9. Define tests or proof obligations before implementation.
10. Implement the scoped change.
11. Run code review and resolve findings.
12. Explain meaningful changes when useful for review or handoff.
13. Verify artifacts, tests, code, and documentation together.
14. Prepare PR handoff when the branch is ready.
15. Capture durable lessons when the work exposes recurring process or project rules.

Individual skills MAY be invoked directly for isolated work, such as updating the vision, reviewing a proposal, updating governance, or fixing a narrow bug. A direct skill invocation MUST still report files changed, validation evidence, unresolved questions, and whether downstream workflow steps are required before implementation.

Workflow completion claims require durable evidence: changed files, linked artifacts, validation commands, review status, unresolved risks, and any skipped steps with rationale.

## Current Assumptions And Gaps

This repository has accepted a Markdown-first direction and the Responsible Breadth direction. The prior structured content-schema platform, validator, generated-output pipeline, and related reviews are historical evidence unless explicitly reactivated.

The Responsible Breadth direction still requires ADR supersession, spec and architecture updates, planning, proof-map updates, validation changes, and review before expanded pattern, condition, principle, or program-example content may rely on it. The repository also still needs a refreshed workflow guide, updated project map, content contribution rules for the broader scope, license-file clarification for CC BY 4.0 content, Markdown templates for the expanded page types, lightweight Markdown/content checks, and a non-canonical expanded-scope proof slice before broad implementation.

No hosted CI workflow, deployment target, CMS integration, public release process, formal expert-review board, production exercise library, or public mdBook publication is assumed. Agents MUST NOT assume those exist.
