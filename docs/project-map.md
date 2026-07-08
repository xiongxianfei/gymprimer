# GymPrimer Project Map

## Map metadata

- Map status: current
- Scope: repository
- Baseline: `1fd3909`
- Last reviewed: 2026-07-07
- Coverage: root governance and product references; Markdown content directories; media provenance; templates; validation scripts; tests; specs; architecture, ADR, workflow, plan, change, and learning artifact locations.
- Exclusions: `.git/` internals, `.agents/` skill implementation files, binary media contents beyond path/provenance inventory, Python bytecode caches, historical change-record details not needed for repository orientation, network/hosted services, and uncreated future implementation areas.
- Parent map: not-applicable
- Known gaps: no package manifest, deployment configuration, mdBook configuration, CMS integration, database, runtime application, public release process, or formal expert-review board observed.
- Inspected uncommitted paths: root governance, vision, README front matter, contributor scope, project-map scope notes, strategic positioning, general-audience change record, and advanced rowing proposal.

## Purpose and scope

This map orients future work in the repository as it exists now. It records observed current structure, validation surfaces, workflow artifacts, known gaps, and bounded inferences. It does not approve architecture, define future work, verify branch readiness, or act as a backlog.

The mapped scope is the repository root. No area maps exist because the current repository is one Markdown-first product corpus with supporting governance, media, and validation tooling rather than multiple deployable services, packages, or independently owned subsystems.

## System overview

Observed: GymPrimer is a Markdown-first exercise, movement, and training-literacy primer for a general audience. `README.md` says the repository is the primary product, Markdown pages are the source of truth, and no app, database, generated HTML, account, local server, or generated JSON package is required to use promoted content.

Observed: `CONSTITUTION.md` defines the durable source-of-truth order, requires specs before material Markdown contract, citation, safety, media, validation, licensing, or generated-output changes, and states that Markdown remains canonical while generated HTML and future websites are derived unless a later accepted proposal changes that boundary.

Observed: `VISION.md` defines the product as an open-source Markdown primer for readers who want to train with more understanding, from first-time gym users to experienced readers. It rejects diagnosis, individualized coaching, recovery pathways, workout planning, video-first source of truth, and platform machinery that outranks the Markdown corpus.

Observed: `docs/architecture/system/architecture.md` is the approved current architecture package. It describes five logical blocks: project references, content, media, governance, and tooling/operations.

Observed: `docs/plan.md` has no active work and lists the Markdown-first primer, Responsible Breadth content expansion, and repository layout normalization as completed by PR #5.

Inferred: The next material content expansion should start through proposal/spec workflow rather than direct implementation because the constitution treats Markdown content contracts, safety language, citation policy, media policy, and validation tooling as governed surfaces.

## Repository layout

- `README.md`: public repository entry point, usage guidance, active content navigation, validation command examples, and license summary.
- `CONSTITUTION.md`, `VISION.md`, `AGENTS.md`, `docs/workflows.md`: governance, product direction, agent operating rules, and project-local workflow artifact map.
- `SOURCES.md`, `RED-FLAGS.md`, `CONTENT_LICENSE.md`, `CONTRIBUTING.md`: reusable source index, safety-routing reference, content/media license posture, and contributor contract.
- `exercises/`, `patterns/`, `conditions/`, `principles/`, `programs/`: canonical Markdown content directories named by current architecture and README.
- `docs/templates/`: page templates for exercise, pattern, condition, principle, programming-principle, and program-example pages.
- `media/`: approved AI-generated raster assets organized by content type and slug, plus `media/PROVENANCE.md`.
- `tools/checks/`: local Python checker scripts for Markdown-first content contracts and privacy scanning.
- `tests/`: Python `unittest` test modules and fixtures for Markdown-first rules, Responsible Breadth rules, media/provenance rules, compatibility, and repository layout normalization.
- `specs/`: approved specs and test specs for Markdown-first primer, Responsible Breadth, repository layout normalization, and historical content-schema work.
- `docs/architecture/`, `docs/adr/`: current architecture and durable decision records.
- `docs/proposals/`, `docs/plans/`, `docs/changes/`, `docs/learn/`: lifecycle artifacts, plans, reviews, proof records, verification reports, and learning records.

Not observed: active `content/`, `schemas/`, `generated/`, numbered content directories, `about/red-flags.md`, package manifests, build config, deployment config, or mdBook config.

## Runtime flow

Observed static reader flow:

1. A reader opens `README.md`.
2. The reader follows relative links to promoted Markdown content in `patterns/`, `conditions/`, `principles/`, or `programs/`, or to draft first-slice exercise/principle pages in `exercises/` and `principles/`.
3. Safety-relevant pages route to `RED-FLAGS.md`.
4. Pages include page-local source sections and may reuse source IDs listed in `SOURCES.md`.
5. Pages may reference approved media under `media/<content-type>/<slug>/`.

Observed local validation flow:

1. Python `unittest` modules call repository files and checker scripts directly.
2. `tools/checks/check_markdown_first.py` statically scans Markdown paths for content-contract rules, citation/source behavior, Responsible Breadth metadata and headings, stale path references, media/provenance constraints, and excluded scope patterns.
3. `tools/checks/check_privacy.py` statically scans supplied files or directories for configured forbidden privacy patterns.

Not observed: server runtime, frontend runtime, CLI application runtime, database runtime, deployed static site, hosted search, authentication, analytics, or runtime user input flow.

## Data flow

Observed content data flow:

- Markdown pages are source files read directly by humans and by local validation scripts.
- Page-local reference-style links and `SOURCES.md` provide citation traceability.
- Media references in Markdown point to repository-relative assets under `media/`.
- `media/PROVENANCE.md` is the central index for AI-generated raster asset metadata, including asset path, media purpose, generator, creation notes, human review, license assertion, source inputs, review status, and page references.
- Change-local audit and verification records under `docs/changes/<change-id>/` provide lifecycle evidence, but they do not replace Markdown product content.

Observed validation data flow:

- `tests/test_markdown_first_real_pages.py` invokes `tools/checks/check_markdown_first.py` over README, source files, red flags, principles, and exercises.
- `tests/test_responsible_breadth_m1.py` builds temporary fixtures and invokes the Markdown-first checker with `GYMPRIMER_ROOT` to prove Responsible Breadth constraints.
- `tests/test_repository_layout_normalization.py` builds temporary fixtures and invokes the Markdown-first checker to prove canonical paths, stale old-path rejection, media provenance, and historical artifact boundary behavior.

Not observed: database schema, migration path, generated public JSON, API payloads, CMS data model, user data collection, analytics events, or production artifact pipeline.

## External boundaries

Observed external-source boundary: `SOURCES.md` requires public, named, authoritative sources for reused references and says global sources do not replace page-local source sections.

Observed media boundary: `CONTRIBUTING.md`, `CONTENT_LICENSE.md`, `media/README.md`, and `media/PROVENANCE.md` prohibit undocumented third-party media and require approved provenance for AI-generated raster assets.

Observed privacy/security boundary: `README.md`, `CONSTITUTION.md`, `CONTRIBUTING.md`, and `tools/checks/check_privacy.py` forbid secrets, credentials, private contact details, private local paths, private health information, and real user health profiles.

Observed licensing boundary: `README.md` and `CONTENT_LICENSE.md` state that code/tooling use Apache-2.0 and written educational content, templates, original diagrams, and accepted AI-generated raster illustrations use CC BY 4.0 unless a file states otherwise.

Observed contact boundary: `SECURITY.md` and `CODE_OF_CONDUCT.md` still use placeholder reporting contacts.

Not observed: external package dependencies, hosted services, deployment targets, authentication providers, CMS providers, payment systems, telemetry, or network calls in active tooling.

## Test map

Configured commands observed in `README.md`:

- `python3 -m unittest tests.test_markdown_first_contract tests.test_markdown_first_templates`
- `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'`
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises`
- `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md RED-FLAGS.md patterns conditions principles programs exercises docs/changes/responsible-breadth media`

Observed test surfaces:

- Markdown-first tests: `tests/test_markdown_first_*.py`
- Responsible Breadth tests: `tests/test_responsible_breadth_m1.py`
- Repository layout tests: `tests/test_repository_layout_normalization.py`
- Fixture Markdown: `tests/fixtures/markdown-first/`
- Local checkers: `tools/checks/check_markdown_first.py`, `tools/checks/check_privacy.py`

Executed commands during this mapping session:

- `sed -n '1,260p' .agents/skills/project-map/SKILL.md`: exit 0
- `sed -n '261,520p' .agents/skills/project-map/SKILL.md`: exit 0
- `sed -n '1,260p' docs/project-map.md`: exit 0
- `sed -n '1,140p' docs/workflows.md`: exit 0
- `git rev-parse --short HEAD && git status --short --branch`: exit 0
- `rg --files -g '!/.git/**' -g '!/.agents/**' | sort`: exit 0
- `find .github -maxdepth 3 -type f -print 2>/dev/null | sort`: exit 0, printed `.github/workflows/ci.yml`
- `find . -maxdepth 2 \( -name 'package.json' -o -name 'pyproject.toml' -o -name 'requirements*.txt' -o -name 'Makefile' -o -name 'tox.ini' -o -name 'pytest.ini' -o -name 'setup.cfg' -o -name 'Cargo.toml' -o -name 'go.mod' \) -print | sort`: exit 0, no files printed
- `find patterns conditions principles programs exercises media tools tests specs docs/templates -maxdepth 3 -type f -print 2>/dev/null | sort`: exit 0
- `sed -n '1,220p' README.md`: exit 0
- `sed -n '1,220p' CONSTITUTION.md`: exit 0
- `sed -n '1,220p' VISION.md`: exit 0
- `sed -n '1,220p' docs/architecture/system/architecture.md`: exit 0
- `sed -n '1,180p' media/README.md && sed -n '1,120p' media/PROVENANCE.md`: exit 0
- `sed -n '1,220p' tools/checks/check_markdown_first.py`: exit 0
- `sed -n '1,220p' tools/checks/check_privacy.py`: exit 0
- `for f in patterns/anterior-pelvic-tilt.md conditions/non-specific-chronic-low-back-pain.md principles/how-many-days-a-week.md programs/generic-3-day-full-body-example.md exercises/lat-pulldown.md exercises/dead-bug.md RED-FLAGS.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md; do printf '\n== %s ==\n' "$f"; sed -n '1,80p' "$f"; done`: exit 0
- `for f in tests/test_markdown_first_contract.py tests/test_markdown_first_templates.py tests/test_markdown_first_real_pages.py tests/test_responsible_breadth_m1.py tests/test_repository_layout_normalization.py; do printf '\n== %s ==\n' "$f"; sed -n '1,140p' "$f"; done`: exit 0

No build, hosted CI, network, mdBook, full test suite, or mutating validation command was run during this mapping session.

## CI and release map

Observed: `.github/workflows/ci.yml` defines a GitHub Actions validation workflow for pull requests, pushes to `main`, manual dispatch, and a weekly schedule.

The workflow runs the full Python unittest suite, Markdown-first checks, privacy checks, and `git diff --check`.

Not observed: package manifest scripts, release workflow, deployment configuration, mdBook configuration, or release process file.

Observed: `CONSTITUTION.md` says agents must not claim CI passed unless a CI run was observed and that CI, when present, should run the same core checks expected locally.

## Architecture rules observed

Observed from `CONSTITUTION.md` and `AGENTS.md`:

- Source-of-truth order starts with `CONSTITUTION.md`, then `VISION.md`, accepted proposals, approved specs, architecture/ADRs, plans/rationale, tests/evidence, code/content/configuration/generated artifacts, and chat.
- Material changes to Markdown page contracts, citation policy, safety language, media policy, localization, licensing, public contribution rules, public URLs, generated output, validation tooling, configuration, or migration require durable specs before implementation.
- Architecture decisions are required before changes affecting multiple components, source-of-truth boundaries, repository layout, Markdown URL compatibility, localization, media storage, generated output, validation tooling, public interfaces, security boundaries, deployment, or archival of prior artifacts.
- Markdown source is the primary product; generated HTML, generated validation output, search indexes, and websites are derived unless a later accepted proposal changes that boundary.
- AI-generated exercise guidance, diagnosis, individualized medical advice, treatment plans, rehabilitation pathways, and user-adaptive programming are forbidden as source-of-truth content.

Observed from `docs/architecture/system/architecture.md`:

- The durable architecture view has five logical blocks: project references, content, media, governance, and tooling/operations.
- Active content paths are `exercises/`, `patterns/`, `conditions/`, `principles/`, and `programs/`.
- `RED-FLAGS.md` is the canonical red-flags reference.
- `media/<content-type>/<slug>/` and `media/PROVENANCE.md` own optional supporting raster illustrations and provenance.
- RigorLoop governance and operations artifacts remain under `docs/`.

Observed from active checks:

- The Markdown-first checker rejects stale old content paths, stale `about/red-flags.md` links, old media buckets, excluded-scope terms, missing Responsible Breadth metadata, missing page sections, and unproven or mismatched media provenance.
- The privacy checker performs a negative-match scan over supplied files or directories for configured sensitive-pattern examples.

## Risk areas

- `docs/workflows.md` still has a `Current change` section naming `markdown-first-gym-primer` as branch-ready for `pr`, while `docs/plan.md` and change metadata now show no active work after PR #5. Treat the workflow guide's current-change section as stale until refreshed.
- `CONSTITUTION.md` still says Responsible Breadth requires ADR/spec/architecture/plan/test/validation updates before relying on expanded content, but those artifacts now exist and PR #5 completed the proof slice. Treat that current-assumptions paragraph as stale relative to the completed lifecycle artifacts unless it is intentionally preserving a broader-scaling warning.
- `README.md` marks the five original exercise/principle pages as draft first-slice pages, while additional APT-support exercise pages also exist in `exercises/`. Downstream content work should inspect exact page status instead of assuming all `exercises/` pages are promoted or draft.
- Hosted CI exists, but agents still must not claim it passed unless a run result was actually observed.
- No package manifest pins Python version or dependencies; active tests use the standard library plus repository scripts.
- `SECURITY.md` and `CODE_OF_CONDUCT.md` still contain placeholder reporting contacts.
- `tests/__pycache__/` exists in the working tree filesystem during inspection, but it is generated bytecode cache and not part of the tracked product surface.

## Open questions

- Should `docs/workflows.md` be refreshed now that PR #5 has merged and all active plans are closed?
- Should `CONSTITUTION.md` current-assumptions wording be normalized after the Responsible Breadth proof slice?
- Which next content slice should be proposed, and should it expand pattern pages, exercise pages, conditions, or programming literacy first?
- Should the hosted CI workflow expand its Markdown-first check path list to include `programs`, `conditions`, media provenance, and governance files?
- When should placeholder security and conduct contacts be replaced for public release operations?
- Should mdBook remain deferred, or should a future proposal add minimal derived HTML output?

## Downstream recommendation

Next stage: workflow.

Rationale: The repository map is now refreshed, but it identifies stale workflow/governance routing text rather than an implementation-ready feature. Use workflow routing to decide whether to refresh `docs/workflows.md` and `CONSTITUTION.md` current-assumptions text first, or start a new proposal for the next content slice.

## Evidence trail

| Evidence | Type | Result |
| --- | --- | --- |
| `README.md` | source | Observed current Markdown-first product route, active content directories, promoted Responsible Breadth pages, draft first-slice pages, and local validation command examples. |
| `CONSTITUTION.md` | source | Observed source-of-truth order, spec/test/architecture/review rules, Markdown-first product boundary, privacy/safety rules, and remaining stated assumptions. |
| `VISION.md` | source | Observed project identity, audience, commitments, refusals, and failure conditions. |
| `docs/architecture/system/architecture.md` | source | Observed approved architecture status, five logical blocks, active content paths, media/provenance boundary, and optional mdBook boundary. |
| `docs/workflows.md` | source | Observed artifact location map and stale current-change routing section. |
| `docs/plan.md` | source | Observed no active plans and three recent completed tracks from PR #5. |
| `SOURCES.md` | source | Observed reusable source-index rules and public source IDs. |
| `RED-FLAGS.md` | source | Observed root red-flags reference and page-local sources. |
| `CONTRIBUTING.md` | source | Observed contributor scope, citation, media, and privacy rules. |
| `CONTENT_LICENSE.md` | source | Observed Apache-2.0 and CC BY 4.0 split license posture. |
| `media/README.md`, `media/PROVENANCE.md` | source | Observed media path contract and AI-generated raster provenance rows. |
| `tools/checks/check_markdown_first.py` | source | Observed Markdown-first structural, citation, Responsible Breadth, old-path, media, and scope checks. |
| `tools/checks/check_privacy.py` | source | Observed negative-match privacy scanner. |
| `tests/test_markdown_first_*.py` | source | Observed active Markdown-first unittest coverage. |
| `tests/test_responsible_breadth_m1.py` | source | Observed Responsible Breadth fixture/checker coverage. |
| `tests/test_repository_layout_normalization.py` | source | Observed canonical path and layout-normalization fixture/checker coverage. |
| `rg --files -g '!/.git/**' -g '!/.agents/**' \| sort` | executed command | Exit 0; found current product, governance, specs, tests, media, and lifecycle artifact inventory. |
| `find .github -maxdepth 3 -type f -print 2>/dev/null \| sort` | executed command | Exit 0; current inspection found `.github/workflows/ci.yml`. |
| `find . -maxdepth 2 \( -name 'package.json' -o -name 'pyproject.toml' -o -name 'requirements*.txt' -o -name 'Makefile' -o -name 'tox.ini' -o -name 'pytest.ini' -o -name 'setup.cfg' -o -name 'Cargo.toml' -o -name 'go.mod' \) -print \| sort` | executed command | Exit 0; no package/build manifest files printed. |
| `git rev-parse --short HEAD && git status --short --branch` | executed command | Exit 0; baseline `2c0c41a`, branch `main...origin/main`, no uncommitted paths before map edit. |
