# GymPrimer Project Map

## Map metadata

- Map status: partial
- Scope: repository
- Baseline: `2c9401f+dirty`
- Last reviewed: 2026-06-26
- Coverage: root documentation and governance files: `README.md`, `VISION.md`, `CONSTITUTION.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `docs/vision/strategic-positioning.md`; repository file inventory excluding `.git/` and `.agents/`
- Exclusions: `.agents/` skill implementation files, `.git/` internals, external services, uncreated future implementation areas
- Parent map: not-applicable
- Known gaps: no source tree, content schema, exercise cards, architecture docs, specs, tests, package/build config, CI workflows, deployment config, or release process observed
- Inspected uncommitted paths: `README.md`, `AGENTS.md`, `CONSTITUTION.md`, `VISION.md`, `docs/vision/strategic-positioning.md`

## Purpose and scope

This map orients future work in the repository as it exists now. It records observed documentation, governance, and absent implementation surfaces. It does not approve architecture, define future implementation, or claim readiness to build.

The mapped scope is the repository root. No area maps exist because no durable subsystem, package, service, content domain, infrastructure area, or deployable component has been created yet.

## System overview

Observed: GymPrimer is currently a documentation-and-governance repository. The project identity is defined by `VISION.md`, which describes an open-source educational reference for gym beginners with reviewed exercise cards, English-first launch content, a locale-aware schema for future Chinese content, tiered expert review, and canonical illustrated SVG step cards.

Observed: `README.md` exposes a managed vision front matter block and states that the repository currently contains only the project vision and supporting strategic-positioning rationale. Its status text still mentions open questions, which is stale relative to the resolved decisions now recorded in `VISION.md`.

Observed: `CONSTITUTION.md` defines project governance, source-of-truth order, spec/test/architecture/review/verification rules, security and privacy rules, and current gaps. `AGENTS.md` provides a shorter agent-facing operating summary.

Observed: `docs/vision/strategic-positioning.md` records supporting rationale for the vision, including category, primary user, tradeoffs, compatibility surfaces, refusals, and falsifiability.

Inferred: Future implementation work will likely need a spec, architecture, and test strategy before code because `CONSTITUTION.md` requires durable artifacts before substantive schema, localization, review, safety, accessibility, licensing, public API, configuration, or data-migration changes.

## Repository layout

- `README.md`: public project entry point with managed vision front matter, license note, and current status text.
- `VISION.md`: canonical project vision and scope boundary.
- `CONSTITUTION.md`: highest-level governance for agentic and human workflows.
- `AGENTS.md`: concise agent operating rules derived from the constitution.
- `CONTRIBUTING.md`: basic contribution expectations for focused pull requests, rationale, tests or docs, and check reporting.
- `CODE_OF_CONDUCT.md`: participation behavior and reporting placeholder.
- `SECURITY.md`: vulnerability reporting instructions with placeholder security contact.
- `LICENSE`: project license file. It was inventoried but not read in this mapping pass.
- `docs/vision/strategic-positioning.md`: rationale supporting `VISION.md`.

Not observed: `src/`, `app/`, `content/`, `schemas/`, `specs/`, `docs/architecture/`, `docs/changes/`, `.github/workflows/`, package manifests, build config, test config, deployment config, or generated output.

## Runtime flow

Not observed in the mapped scope. The repository has no executable source, runtime configuration, package manifest, server entry point, frontend entry point, CLI entry point, or test-demonstrated runtime flow.

## Data flow

Not observed in the mapped scope. The vision and constitution describe intended future content concepts such as locale-aware card fields, review metadata, canonical SVG step media, and equipment-anchored discovery, but no schema, database, file format, fixture, migration, CMS configuration, or content object exists yet.

## External boundaries

Observed: `SECURITY.md` directs vulnerability reports to a private email placeholder rather than public issues.

Observed: `CODE_OF_CONDUCT.md` directs conduct reports to a maintainer email placeholder.

Observed: `CONSTITUTION.md` treats dependencies, media assets, content sources, licensing, reviewer or user data, and health-adjacent safety language as governed external or risk boundaries.

Not observed: live external integrations, package registries, hosting configuration, analytics, CMS providers, authentication providers, payment systems, AI services, media storage, or deployment targets.

## Test map

Configured commands: none observed. No package manifest, test runner config, Makefile, CI workflow, or documented test command exists in the mapped scope.

Executed commands during mapping:

- `sed -n '1,320p' .agents/skills/project-map/SKILL.md`: exit 0
- `find .agents/skills/project-map -maxdepth 3 -type f -print`: exit 0
- `git rev-parse --short HEAD && git status --short`: exit 0
- `rg --files -g '!/.git/**' -g '!/.agents/**'`: exit 0
- `sed -n '1,260p' .agents/skills/project-map/assets/project-map-skeleton.md`: exit 0
- `sed -n '1,220p' AGENTS.md`: exit 0
- `sed -n '1,260p' CONSTITUTION.md`: exit 0
- `sed -n '1,180p' CODE_OF_CONDUCT.md`: exit 0
- `sed -n '1,180p' SECURITY.md`: exit 0
- `find . -maxdepth 3 -type f -not -path './.git/*' -not -path './.agents/*' -printf '%p\n' | sort`: exit 0

No build, test, lint, network, or mutating command was run.

## CI and release map

Not observed in the mapped scope. No `.github/workflows/` directory, release workflow, package manifest, versioning file, deployment config, or release documentation was observed.

`CONSTITUTION.md` states that agents must not claim CI passed unless a CI run was observed and that CI should eventually run the same core checks expected locally.

## Architecture rules observed

Observed from `CONSTITUTION.md` and `AGENTS.md`:

- `CONSTITUTION.md` outranks `VISION.md`, which outranks specs, architecture, plans, tests, code/content, and chat.
- Substantive changes require durable specs before implementation when they affect behavior, schema, exercise-card contracts, localization, review workflow, media policy, safety language, accessibility, licensing, public APIs, configuration, or data migration.
- Architecture decisions are required before changes affecting multiple components, data ownership, schema shape, localization model, CMS workflow, media storage, review workflow, public interfaces, security boundaries, or deployment.
- The future content model must preserve locale-aware fields, English launch content, reviewed exercise cards, tiered review metadata, canonical SVG step media, visible reviewer identity and review date, public review history, and equipment-anchored discovery.
- AI-generated exercise guidance, medical advice, and community video as source-of-truth content are forbidden.

Observed from `VISION.md`:

- GymPrimer is an exercise-literacy reference before workout prescription.
- Reviewed text and SVG illustrations are canonical; community video can only supplement stable cards later.
- The first implementation should not require bilingual card content before the English schema stabilizes, but the schema must support Chinese without rework.

## Risk areas

- README status drift: `README.md` still says to see `VISION.md` for open questions, but `VISION.md` no longer has an open-questions section.
- No implementation surfaces exist yet, so future code placement cannot rely on current source boundaries.
- No test framework or CI exists, so future behavior changes need validation infrastructure or explicit manual verification records.
- No architecture artifact exists for the locale-aware schema, review workflow, media pipeline, CMS workflow, or content storage model.
- `CODE_OF_CONDUCT.md` and `SECURITY.md` contain placeholder contact values.
- `LICENSE` was inventoried but not read in this pass; Apache 2.0 posture is stated in `README.md`, `VISION.md`, and `CONSTITUTION.md`, but license-file contents were not verified here.

## Open questions

- What implementation stack, package manager, runtime, and hosting model will GymPrimer use?
- Where will exercise content live: repository files, a CMS, generated static assets, or another storage model?
- What is the exact locale-aware card schema and migration policy?
- What validation tooling will enforce schema, accessibility, licensing, review metadata, and media-source rules?
- Who owns maintainer and security contact addresses before public contribution begins?
- Should README status text be updated now that the vision open questions have been resolved?

## Downstream recommendation

Next stage: proposal.

Rationale: The map records unresolved direction-level questions about implementation stack, content storage, schema shape, validation tooling, and ownership. Those choices affect scope, tradeoffs, and architecture boundaries, so they should be resolved through proposal work before architecture authoring. Architecture should follow once a direction and spec are stable enough to design against.

## Evidence trail

| Evidence | Type | Result |
| --- | --- | --- |
| `README.md` | source | Public entry point with managed vision block, license note, and status text stating repository contains vision and positioning rationale only. |
| `VISION.md` | source | Canonical project identity: beginner exercise-literacy reference, English-first locale-aware content, tiered review, canonical SVG step cards, refusals, and falsifiability. |
| `CONSTITUTION.md` | source | Governance, source-of-truth order, lifecycle gates, security/privacy, compatibility, verification, review, documentation, and current implementation gaps. |
| `AGENTS.md` | source | Concise agent operating rules and source-order summary. |
| `CONTRIBUTING.md` | source | Basic PR and issue expectations. |
| `CODE_OF_CONDUCT.md` | source | Conduct expectations and placeholder reporting contact. |
| `SECURITY.md` | source | Private vulnerability reporting guidance and placeholder security contact. |
| `docs/vision/strategic-positioning.md` | source | Supporting strategic-positioning rationale for the vision. |
| `rg --files -g '!/.git/**' -g '!/.agents/**'` | executed command | Exit 0; found root docs and `docs/vision/strategic-positioning.md`, no source, specs, tests, package manifests, or CI files. |
| `find . -maxdepth 3 -type f -not -path './.git/*' -not -path './.agents/*' -printf '%p\n' \| sort` | executed command | Exit 0; confirmed mapped file inventory at depth 3. |
| `git rev-parse --short HEAD && git status --short` | executed command | Exit 0; baseline `2c9401f+dirty`, with modified `README.md` and untracked governance/vision/docs files before this map was added. |
