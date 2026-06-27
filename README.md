# GymPrimer

<!-- vision:start -->

When a beginner is standing in front of an unfamiliar gym machine and needs to train safely without guessing, GymPrimer helps them understand what the exercise is for, how to set up the equipment, what the movement should feel like, and when to stop.

GymPrimer is an open-source educational reference for exercise literacy. It is upstream of workout prescription: reviewed cards over generated answers, canonical SVG step cards over video-first instruction, and depth/correctness over shallow exercise count.

It is for adults in their first ninety days of regular gym training, people returning after a long break, and the trainers, physical therapists, clinicians, content authors, illustrators, translators, and engineers who maintain reviewed exercise cards together. Launch content is English-first, with Chinese treated as a first-class future locale.

<!-- vision:end -->

For goals, non-goals, commitments, refusals, and what would prove this project wrong, see [VISION.md](./VISION.md).

## Table of Contents

- [Security](#security)
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Maintainers](#maintainers)
- [Thanks](#thanks)
- [Contributing](#contributing)
- [License](#license)

## Security

Do not put secrets, private reviewer contact details, private health information, local machine paths, credentials, or real user health profiles in this repository.

Security reporting is documented in [SECURITY.md](./SECURITY.md). The security contact is still a placeholder and must be replaced before public release operations.

## Background

This repository currently contains the project vision, approved content-schema artifacts, repository-native source fixtures, local validation tools, and deterministic generated-output evidence. It does not yet contain a frontend, CMS, AI assistant, public exercise library, or CI workflow.

The current implementation proves a content foundation:

- reviewed source content lives under `content/`;
- canonical SVG media lives under `media/svg/`;
- machine-readable schema summaries live under `schemas/`;
- local validation tools live under `tools/validation/`;
- generated validation and public-content artifacts live under `generated/`.

The first generated public package contains one reviewed example card. It is evidence for the schema and validation workflow, not a launch library.

## Install

No package installation is required for the current repository foundation.

Prerequisites:

- Python 3
- Git
- `rg` for the optional state-sync checks used in workflow artifacts

Clone the repository and run commands from the repository root.

## Usage

Run the local validation suite:

```sh
python3 -m unittest discover -s tests
```

Validate repository content and emit deterministic public output:

```sh
python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json --emit-public generated/public-content.json
```

Run the generated-output privacy scan:

```sh
python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI|personal health" -- generated/
```

The generated public package is [generated/public-content.json](./generated/public-content.json). Future UI or search layers should consume generated public content, not raw draft source files.

## API

GymPrimer does not expose a public runtime API yet.

Current command-line interfaces:

- `tools/validation/validate_content.py`: validates repository-native content and can emit `generated/public-content.json`.
- `tools/validation/privacy_scan.py`: runs negative-match privacy checks with explicit exit codes.

These CLIs are validation tooling for the content foundation, not a stable public product API.

## Maintainers

Maintainer ownership is not finalized. Review workflow records live under [docs/changes/](./docs/changes/), and contribution expectations are documented in [CONTRIBUTING.md](./CONTRIBUTING.md).

## Thanks

GymPrimer is shaped by open-source documentation practice, plain-language health communication, accessibility expectations, and reviewable content workflows.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

For this stage of the project, keep contributions focused on reviewed content-schema foundation work unless a proposal/spec/architecture update has accepted a broader change.

## License

GymPrimer is released under the Apache License 2.0. See [LICENSE](./LICENSE).
