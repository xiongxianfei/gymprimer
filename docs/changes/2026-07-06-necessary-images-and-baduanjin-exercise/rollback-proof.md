# Baduanjin Text-Only Rollback Proof

## Status

pass

## Scope

- Change ID: `2026-07-06-necessary-images-and-baduanjin-exercise`
- Milestone: M4
- Proof ID: MP4
- Page: `exercises/baduanjin-basics.md`
- Generated assets in rollback scope:
  - `media/exercises/baduanjin-basics/setup.png`
  - `media/exercises/baduanjin-basics/two-hands-lift.png`
  - `media/exercises/baduanjin-basics/drawing-bow.png`
  - `media/exercises/baduanjin-basics/alternating-reach.png`
  - `media/exercises/baduanjin-basics/muscle-attention.png`
- Prompt records in rollback scope:
  - `media/prompts/exercises/baduanjin-basics/setup.md`
  - `media/prompts/exercises/baduanjin-basics/two-hands-lift.md`
  - `media/prompts/exercises/baduanjin-basics/drawing-bow.md`
  - `media/prompts/exercises/baduanjin-basics/alternating-reach.md`
  - `media/prompts/exercises/baduanjin-basics/muscle-attention.md`
- Provenance rows in rollback scope: the five `media/PROVENANCE.md` rows for the Baduanjin assets above
- Audit date: 2026-07-06

## Temporary Review State

The rollback proof uses a temporary review state, not destructive edits to the working tree.

Rollback steps exercised:

1. Copy the Baduanjin page and required repository references to a temporary root.
2. Remove image references from the temporary copy of `exercises/baduanjin-basics.md`.
3. Remove the Baduanjin image rows from the temporary copy of `media/PROVENANCE.md`.
4. Treat `media/exercises/baduanjin-basics/` as unused Baduanjin assets and omit it from the temporary root.
5. Treat `media/prompts/exercises/baduanjin-basics/` as unused prompt records and omit it from the temporary root.
6. Run focused Markdown-first and privacy checks against the temporary text-only page.

## Validation

Commands exercised against the temporary review state:

```sh
tmp=/tmp/gymprimer-baduanjin-rollback.cr-m4-001
if [ -e "$tmp" ]; then rm -rf "$tmp"; fi
mkdir -p "$tmp/exercises" "$tmp/media"
awk 'NR < 22 || NR > 32' exercises/baduanjin-basics.md > "$tmp/exercises/baduanjin-basics.md"
awk '!/media\/exercises\/baduanjin-basics\//' media/PROVENANCE.md > "$tmp/media/PROVENANCE.md"
cp SOURCES.md RED-FLAGS.md "$tmp"/
GYMPRIMER_ROOT="$tmp" python3 tools/checks/check_markdown_first.py "$tmp/exercises/baduanjin-basics.md" "$tmp/media/PROVENANCE.md" "$tmp/SOURCES.md" "$tmp/RED-FLAGS.md"
GYMPRIMER_ROOT="$tmp" python3 tools/checks/check_privacy.py "$tmp/exercises/baduanjin-basics.md" "$tmp/media/PROVENANCE.md" "$tmp/SOURCES.md" "$tmp/RED-FLAGS.md"
```

Result: pass; Markdown-first checked 4 Markdown files, and privacy checked 4 files.

## Cleanup Contract

If any Baduanjin image fails review after promotion, rollback is:

- remove image references from `exercises/baduanjin-basics.md`;
- remove unused Baduanjin assets from `media/exercises/baduanjin-basics/`;
- remove unused prompt records from `media/prompts/exercises/baduanjin-basics/`;
- remove the matching Baduanjin provenance rows from `media/PROVENANCE.md`;
- rerun the focused Markdown-first and privacy checks before handoff.

## Disposition

The text-only Baduanjin page remains valid without image references, unused Baduanjin assets, prompt records, or provenance rows.

## Residual Risk

The rollback proof validates the page fallback and cleanup sequence.
It does not evaluate replacement images; any replacement image must repeat prompt-record, provenance, visual-safety, and beginner-comprehension review.

## Sources

- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Baduanjin Basics page](../../../exercises/baduanjin-basics.md)
