# GymPrimer

<!-- vision:start -->

GymPrimer is an open-source Markdown primer for gym beginners. It teaches exercise literacy before workout prescription through short, citation-backed pages that explain what an exercise is for, how to set up the equipment, what the movement should feel like, common mistakes, easier options, and when to stop.

The repository is the primary product. GymPrimer trades breadth and polish for verifiable beginner understanding: a small Markdown corpus, plain language, conservative scope, prominent disclaimers, and sources a reader can check. Optional mdBook HTML can improve navigation later, but Markdown remains the source of truth.

It is for adults in their first ninety days of regular gym training, people returning after a long break, and maintainers, authors, translators, illustrators, and reviewers who want to improve beginner exercise education in public. Launch content is English-first, with Chinese aliases and later separate-locale translation possible after the English format is proven.

<!-- vision:end -->

For goals, non-goals, commitments, refusals, and what would prove this project wrong, see [VISION.md](./VISION.md).

## Table of Contents

- [Security](#security)
- [Background](#background)
- [Usage](#usage)
- [Repository Layout](#repository-layout)
- [Validation](#validation)
- [Maintainers](#maintainers)
- [Thanks](#thanks)
- [Contributing](#contributing)
- [License](#license)

## Security

Do not put secrets, private reviewer contact details, private health information, local machine paths, credentials, or real user health profiles in this repository.

Security reporting is documented in [SECURITY.md](./SECURITY.md). The security contact is still a placeholder and must be replaced before public release operations.

## Background

GymPrimer is now a Markdown-first primer. The source of truth is the Markdown corpus in this repository, supported by page-local citations, [SOURCES.md](./SOURCES.md), contributor guidance, and templates.

The old structured content-schema platform, generated JSON package, expert-review lifecycle, and validator workflow are superseded historical artifacts. They remain in the repository for traceability, but they are not the v0.1 product route.

The v0.1 implementation is staged. M1 establishes the active route, contributor contract, templates, and legacy supersession. The first five real Markdown pages are drafted in M3, then promoted only after the required checks and beginner read-test evidence exist.

## Usage

Browse the repository directly. No app, database, generated HTML, account, local server, or generated JSON package is required to use promoted Markdown content.

Current active support files:

- [CONTRIBUTING.md](./CONTRIBUTING.md): contributor contract, citation expectations, scope rules, media rules, privacy rules, and inbound license terms.
- [SOURCES.md](./SOURCES.md): global source index for sources reused across more than one page.
- [CONTENT_LICENSE.md](./CONTENT_LICENSE.md): license split for code/tooling and written content/original diagrams.
- [docs/templates/exercise-card.md](./docs/templates/exercise-card.md): exercise-page template.
- [docs/templates/principle-page.md](./docs/templates/principle-page.md): principle-page template.

Draft first-slice pages, not yet promoted:

- [Beginner Training Principles](01-getting-started/beginner-training-principles.md)
- [Lat Pulldown](02-machines/lat-pulldown.md)
- [Seated Row](02-machines/seated-row.md)
- [Chest Press](02-machines/chest-press.md)
- [Incline Push-Up](03-bodyweight/incline-push-up.md)

These pages must not be described as published, approved, expert-reviewed, or promoted source content until the M3 milestone has beginner read-test evidence and review approval.

## Repository Layout

- `README.md`: repository entry point and product navigation after pages are promoted.
- `SOURCES.md`: reusable public source index.
- `CONTRIBUTING.md`: contribution rules for Markdown-first content.
- `CONTENT_LICENSE.md`: license posture for code/tooling and content/media.
- `docs/templates/`: source templates for exercise and principle pages.
- `01-getting-started/`, `02-machines/`, `03-bodyweight/`: planned first-slice Markdown directories.
- `media/`: optional original SVG diagrams and approved AI-generated raster
  illustrations with provenance; no third-party screenshots, stock photos, or
  borrowed public web images for v0.1.
- `content/`, `schemas/`, `generated/`, `tools/validation/`: superseded structured-platform artifacts retained as historical evidence.

## Validation

No hosted CI workflow is configured yet.

For M1, run the Markdown-first contract tests and structural checks:

```sh
python3 -m unittest tests.test_markdown_first_contract tests.test_markdown_first_templates tests.test_markdown_first_legacy_boundary
```

Later milestones add `tools/checks/` for Markdown-first source, disclaimer, citation, scope, media, and privacy checks. The old `tools/validation/` commands are historical structured-platform tooling, not active v0.1 product validation.

## Maintainers

Maintainer ownership is not finalized. Review workflow records live under [docs/changes/](./docs/changes/), and contribution expectations are documented in [CONTRIBUTING.md](./CONTRIBUTING.md).

## Thanks

GymPrimer is shaped by open-source documentation practice, plain-language health communication, accessibility expectations, and reviewable content workflows.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

For this stage of the project, keep contributions focused on the Markdown-first primer contract unless a proposal, spec, and architecture update accept a broader change.

## License

GymPrimer code and tooling are released under Apache-2.0. Written educational content and original diagrams are provided under CC BY 4.0. See [LICENSE](./LICENSE) and [CONTENT_LICENSE.md](./CONTENT_LICENSE.md).
