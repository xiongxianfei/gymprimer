# MP5 - Validation Command Ledger And Source-Of-Truth Drift Inspection

| Field | Value |
| --- | --- |
| Owner | release/check maintainer |
| Owning milestone | M4 |
| Classification | manual-only |
| Evidence date | 2026-06-29 |
| Status | current for M4 handoff |

## Source-Of-Truth Result

Markdown remains the source of truth. README links to the first-slice Markdown
pages, and no mdBook HTML, generated JSON package, old schema, or old validator
surface is treated as the v0.1 product.

mdBook is deferred in
`docs/changes/markdown-first-gym-primer/manual-proof/MP4-mdbook-build-or-deferral.md`.

## Commands Run

### mdBook Availability

```sh
command -v mdbook || true
```

Result: pass. No `mdbook` executable was found, so mdBook was deferred.

```sh
if command -v mdbook >/dev/null 2>&1; then mdbook build; else printf 'mdbook not installed; mdBook deferred\n'; fi
```

Result: pass. The command printed `mdbook not installed; mdBook deferred`.

### Markdown-First Tests

```sh
python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'
```

Result: pass. The Markdown-first test suite passed with 51 tests after the M4
proof records were added.

### Markdown-First Checker

```sh
python3 tools/checks/check_markdown_first.py README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight
```

Result: pass. The first-slice Markdown pages and active guidance files passed
source, disclaimer, scope, media, and citation checks.

### Privacy Scan

```sh
python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight media docs/changes/markdown-first-gym-primer
```

Result: pass. The first-slice pages, media, provenance records, and
change-local proof records passed the privacy scan.

### Excluded-Scope Scan

```sh
if rg -n "barbell|deadlift|bench press|Olympic|kettlebell|plyometric|sprint|diagnos|rehab|treat pain|posture correction" 01-getting-started 02-machines 03-bodyweight; then
  exit 1
else
  printf "no excluded-scope terms found\n"
fi
```

Result: pass. The scan printed `no excluded-scope terms found`.

### Scoped Markdown Lint

```sh
markdownlint --disable MD013 -- docs/changes/markdown-first-gym-primer/manual-proof/MP4-mdbook-build-or-deferral.md docs/changes/markdown-first-gym-primer/manual-proof/MP5-validation-command-ledger.md docs/plans/2026-06-27-markdown-first-gym-primer.md docs/plan.md docs/workflows.md
```

Result: pass. Scoped Markdown lint passed with line length disabled.

### Diff Whitespace

```sh
git diff --check
```

Result: pass. Diff whitespace checks passed.

## CI Statement

CI was not run. This record does not claim CI success.

## Residual Risks

- mdBook remains deferred because the binary is unavailable locally.
- Repository-wide `markdownlint "**/*.md"` is still not the M4 gate because
  broad pre-existing lint issues exist outside this slice.
- Final verification and PR readiness are not claimed by this manual proof.
