# Safer Running Text-Only Rollback Proof

## Status

pass

## Scope

- Change ID: `2026-07-06-safer-running-basics-and-running-images`
- Milestone: M4
- Proof ID: MP4
- Page: `exercises/safer-running-basics.md`
- Generated assets in rollback scope:
  - `media/exercises/safer-running-basics/posture.png`
  - `media/exercises/safer-running-basics/landing.png`
  - `media/exercises/safer-running-basics/run-walk.png`
  - `media/exercises/safer-running-basics/warm-up.png`
  - `media/exercises/safer-running-basics/muscle-attention.png`
  - `media/exercises/safer-running-basics/overstride-comparison.png`
- Prompt records in rollback scope:
  - `media/prompts/exercises/safer-running-basics/posture.md`
  - `media/prompts/exercises/safer-running-basics/landing.md`
  - `media/prompts/exercises/safer-running-basics/run-walk.md`
  - `media/prompts/exercises/safer-running-basics/warm-up.md`
  - `media/prompts/exercises/safer-running-basics/muscle-attention.md`
  - `media/prompts/exercises/safer-running-basics/overstride-comparison.md`
- Provenance rows in rollback scope: the six `media/PROVENANCE.md` rows for the safer-running assets above
- Audit date: 2026-07-07

## Temporary Review State

The rollback proof uses a temporary review state, not destructive edits to the working tree.

Rollback steps exercised:

1. Copy the safer-running page and required repository references to a temporary root.
2. Remove image references from the temporary copy of `exercises/safer-running-basics.md`.
3. Remove the safer-running image rows from the temporary copy of `media/PROVENANCE.md`.
4. Treat `media/exercises/safer-running-basics/` as unused safer-running assets and omit it from the temporary root.
5. Treat `media/prompts/exercises/safer-running-basics/` as unused prompt records and omit it from the temporary root.
6. Run focused Markdown-first and privacy checks against the temporary text-only page.

## Validation

Commands exercised against the temporary review state:

```sh
tmp=/tmp/gymprimer-safer-running-rollback.m4
if [ -e "$tmp" ]; then rm -rf "$tmp"; fi
mkdir -p "$tmp/exercises" "$tmp/media"
sed '/media\/exercises\/safer-running-basics/d' exercises/safer-running-basics.md > "$tmp/exercises/safer-running-basics.md"
awk '!/media\/exercises\/safer-running-basics\//' media/PROVENANCE.md > "$tmp/media/PROVENANCE.md"
cp SOURCES.md RED-FLAGS.md "$tmp"/
GYMPRIMER_ROOT="$tmp" python3 tools/checks/check_markdown_first.py "$tmp/exercises/safer-running-basics.md" "$tmp/media/PROVENANCE.md" "$tmp/SOURCES.md" "$tmp/RED-FLAGS.md"
GYMPRIMER_ROOT="$tmp" python3 tools/checks/check_privacy.py "$tmp/exercises/safer-running-basics.md" "$tmp/media/PROVENANCE.md" "$tmp/SOURCES.md" "$tmp/RED-FLAGS.md"
```

Result: pass; Markdown-first checked 4 Markdown files, and privacy checked 4 files.

## Cleanup Contract

If any safer-running image fails review after promotion, rollback is:

- remove image references from `exercises/safer-running-basics.md`;
- remove unused safer-running assets from `media/exercises/safer-running-basics/`;
- remove unused prompt records from `media/prompts/exercises/safer-running-basics/`;
- remove the matching safer-running provenance rows from `media/PROVENANCE.md`;
- rerun the focused Markdown-first and privacy checks before handoff.

## Disposition

The text-only safer-running page remains valid without image references, unused safer-running assets, prompt records, or provenance rows.

## Residual Risk

The rollback proof validates the page fallback and cleanup sequence.
It does not evaluate replacement images; any replacement image must repeat prompt-record, provenance, visual-safety, and beginner-comprehension review.

## Sources

- [Safer Running Basics and High-Quality Running Images spec](../../../../specs/safer-running-basics-and-running-images.md)
- [Safer Running Basics and High-Quality Running Images test spec](../../../../specs/safer-running-basics-and-running-images.test.md)
- [Safer Running Basics page](../../../../exercises/safer-running-basics.md)
