# Project Constitution

This constitution defines the durable rules for GymPrimer. It governs agentic development, human review, and repository changes. It is not a roadmap or feature list.

## Project Purpose

GymPrimer is an open-source educational reference for gym beginners. It teaches exercise literacy before workout prescription through reviewed, plain-language exercise cards, canonical illustrated SVG step cards, English-first content, and a locale-aware schema that keeps Chinese as a first-class future locale.

The project serves beginners in their first ninety days of regular gym training, people returning after a long break, and the reviewers, authors, translators, illustrators, and engineers who maintain the content library. It MUST NOT become a workout planner, clinical rehabilitation product, injury-diagnosis tool, AI coach, or video-first source of truth.

## Source Of Truth Order

When artifacts conflict, agents and reviewers MUST use this order:

1. `CONSTITUTION.md`
2. `VISION.md`
3. Approved specs in `specs/`
4. Architecture artifacts in `docs/architecture/`
5. Change-local plans and rationale in `docs/changes/<change-id>/`
6. Tests, fixtures, and validation evidence
7. Code, content, schemas, and configuration
8. Chat messages and issue comments

Changes that intentionally revise a higher-ranked artifact MUST update that artifact first or in the same change. Chat context MUST NOT silently override durable project artifacts.

## Spec-Driven Rules

Substantive changes MUST have a durable spec before implementation when they affect user-visible behavior, content schema, exercise-card contracts, localization, review workflow, media policy, safety language, accessibility, licensing, public APIs, configuration, or data migration.

Specs MUST identify requirements with stable IDs and include acceptance criteria that can be tested, reviewed, or manually verified. Specs MUST distinguish goals, non-goals, compatibility expectations, security and privacy constraints, accessibility expectations, and open questions.

Small editorial fixes, typo fixes, and documentation clarifications MAY proceed without a spec when they do not change scope, commitments, behavior, schema, or user obligations.

## Test-Driven Rules

Behavior changes MUST be proven by tests or by an explicit manual verification record when automation is not yet possible. Bug fixes MUST start with a failing regression test or a documented reproduction that fails before the fix.

Schema, localization, content validation, accessibility, review-state, and media-source rules SHOULD be automated as soon as the relevant structure exists. Claims about beginner comprehension, review currency, or localization readiness MUST be tied to repeatable checks, audit records, or documented user-test evidence.

Agents MUST NOT make unverifiable completion claims. If no test framework or CI exists, the change MUST report that gap and the exact manual checks performed.

## Architecture Rules

Architecture decisions are required before implementation when a change affects multiple components, data ownership, schema shape, localization model, CMS workflow, media storage, review workflow, public interfaces, security boundaries, or deployment.

The content model MUST preserve GymPrimer's core commitments: locale-aware fields from day one, English launch content, reviewed exercise cards, tiered review metadata, canonical SVG step media, visible reviewer identity and review date, public review history, and equipment-anchored discovery.

Architecture artifacts MUST record tradeoffs, rejected options, migration implications, compatibility surfaces, and how the decision preserves the refusals in `VISION.md`. Implementation details belong in architecture or plans, not in the vision.

## Security And Privacy Rules

Secrets, credentials, private keys, personal contact details, private machine paths, and private reviewer or user data MUST NOT be committed. Logs and fixtures MUST avoid sensitive personal data unless a spec explicitly defines a safe anonymized fixture.

Health-adjacent content MUST avoid diagnosis, individualized medical advice, treatment plans, and active-rehab guidance. Safety language MUST follow the tiered review model defined in `VISION.md`: trainers or strength coaches review cards, physical therapists review safety and pain-language policy, and sports medicine clinicians advise on disclaimers, emergency criteria, and elevated-risk cards.

Dependencies, media assets, and content sources MUST be license-compatible with the repository's Apache 2.0 posture or explicitly documented as external non-source assets with allowed use. AI-generated exercise guidance MUST NOT become source-of-truth content.

## Compatibility Rules

Public schemas, content IDs, locale keys, review metadata, media references, URLs, APIs, config names, and persisted data formats MUST be treated as compatibility surfaces once published.

Breaking changes MUST have a migration plan, versioning or deprecation notes when applicable, tests or fixtures that prove the migration, and documentation updates. The schema MUST support adding Chinese content without reworking existing card structure.

Community video MAY supplement reviewed cards only when licensing, attribution, accessibility, and review rules are specified. Video MUST NOT replace reviewed text and SVG illustrations as the canonical source.

## Verification Rules

Before completion, every change MUST report the exact validation commands run and their outcomes. If a command cannot be run, the report MUST say why and identify residual risk.

CI configuration, when present, SHOULD run the same core checks expected locally. Agents MUST NOT claim CI passed unless they observed the run result. For documentation-only changes, validation MAY be limited to relevant linting, link checks, word-count or marker checks, and direct file review.

Vision and constitution updates MUST verify required sections, source-of-truth consistency, and README marker integrity when README front matter is affected.

## Review Rules

Proposal review SHOULD be used when problem framing, scope, or strategic fit is uncertain. Spec review MUST precede implementation for material specs. Architecture review MUST precede implementation for hard-to-reverse design decisions. Plan review SHOULD precede multi-milestone implementation.

Code review MUST be used before claiming completion for implementation work that changes behavior, schema, workflows, security posture, or user-facing content. Final verification MUST be performed after review issues are resolved and before PR handoff.

Review findings MUST lead with risks, bugs, missing tests, compatibility issues, or governance violations. Summaries are secondary.

## Documentation Rules

Docs MUST be updated with the change they describe. Changes to project identity update `VISION.md` and, when applicable, README vision front matter. Changes to governance update `CONSTITUTION.md` and, when applicable, `AGENTS.md`. Changes to architecture update `docs/architecture/`. Changes to workflow expectations update workflow documentation or the relevant change-local artifact.

Specs, plans, tests, and implementation MUST stay traceable through stable requirement IDs where specs exist. Lessons that reveal recurring mistakes or durable process improvements SHOULD be captured with the learning workflow instead of left only in chat.

README content outside managed marker blocks MUST NOT be rewritten as part of artifact synchronization unless the user explicitly authorizes broader README editing.

## Agent Behavior Rules

Agents MUST state important assumptions, blockers, and validation gaps. Agents MUST NOT silently broaden scope, invent external facts, fake test results, claim unobserved CI, discard user changes, or perform unrelated refactors.

Agents MUST inspect existing files before editing, prefer repository patterns over new abstractions, keep changes focused, and preserve a dirty working tree unless explicitly instructed otherwise.

Agents MUST use durable artifacts for durable decisions. Chat-only decisions are acceptable for temporary coordination, but project rules, requirements, architecture, and verification evidence belong in the repository.

## Standard Workflow And Manual Skill Use

The standard workflow for material work is:

1. Explore or research when assumptions are uncertain.
2. Create or update a proposal when direction or scope needs a decision.
3. Create or update a spec for observable requirements.
4. Create or update architecture for cross-component or hard-to-reverse decisions.
5. Create or update a plan for multi-step execution.
6. Define tests or proof obligations before implementation.
7. Implement the scoped change.
8. Run code review and resolve findings.
9. Explain meaningful changes when useful for review or handoff.
10. Verify artifacts, tests, code, and documentation together.
11. Prepare PR handoff when the branch is ready.
12. Capture durable lessons when the work exposes recurring process or project rules.

Individual skills MAY be invoked directly for isolated work, such as updating the vision, reviewing a plan, or fixing a narrow bug. A direct skill invocation MUST still report files changed, validation evidence, unresolved questions, and whether downstream workflow steps are required before implementation.

Workflow completion claims require durable evidence: changed files, linked artifacts, validation commands, review status, unresolved risks, and any skipped steps with rationale.

## Current Assumptions And Gaps

This repository currently has vision and governance artifacts but no implementation, specs, architecture docs, test framework, package configuration, CI workflows, or project map. Until those exist, agents MUST treat implementation requests as requiring upstream specification and validation setup rather than assuming a stack or workflow.

The README status text may lag behind vision decisions outside the managed vision front matter. Broad README maintenance requires explicit authorization unless paired with a requested README update.

