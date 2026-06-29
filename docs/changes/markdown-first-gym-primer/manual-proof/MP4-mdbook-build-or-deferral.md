# MP4 - mdBook Build Or Deferral Proof

| Field | Value |
| --- | --- |
| Owner | release/check maintainer |
| Owning milestone | M4 |
| Classification | conditional/external |
| Evidence date | 2026-06-29 |
| Status | deferred |

## Decision

mdBook is deferred for v0.1 because the `mdbook` binary is not installed in the
local validation environment.

Markdown remains the source of truth. The first-slice pages are still directly
readable through the repository and README links. No generated HTML is required
to use the current primer.

## Commands

```sh
command -v mdbook || true
```

Result: no `mdbook` executable was found.

```sh
if command -v mdbook >/dev/null 2>&1; then mdbook build; else printf 'mdbook not installed; mdBook deferred\n'; fi
```

Result: `mdbook not installed; mdBook deferred`.

`mdbook build` was not run because the required binary is unavailable. This is
an explicit M4 deferral path, not a failed generated-output requirement.

## Files Not Added

The following files were not added because mdBook is deferred:

- `book.toml`
- `SUMMARY.md`

The generated `book/` directory is not present and is not treated as a product
surface.

## Pass Condition

Pass. mdBook is either allowed to build from a minimal default configuration or
durably deferred. This record chooses the deferral path.

## Re-run Trigger

Revisit this record if `mdbook` becomes available or if a later accepted
proposal makes static HTML output required.
