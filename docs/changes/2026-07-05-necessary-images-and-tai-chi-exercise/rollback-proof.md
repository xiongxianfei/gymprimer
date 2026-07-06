# Tai Chi Text-Only Rollback Proof

## Status

pass

## Scope

- Change ID: `2026-07-05-necessary-images-and-tai-chi-exercise`
- Milestone: M4
- Proof ID: MP4
- Page: `exercises/tai-chi-basics.md`
- Generated assets in rollback scope:
  - `media/exercises/tai-chi-basics/setup.png`
  - `media/exercises/tai-chi-basics/weight-shift.png`
  - `media/exercises/tai-chi-basics/muscle-attention.png`
- Prompt records in rollback scope:
  - `media/prompts/exercises/tai-chi-basics/setup.md`
  - `media/prompts/exercises/tai-chi-basics/weight-shift.md`
  - `media/prompts/exercises/tai-chi-basics/muscle-attention.md`
- Provenance rows in rollback scope: the three `media/PROVENANCE.md` rows for the Tai Chi assets above
- Audit date: 2026-07-06

## Temporary Review State

The rollback proof uses a temporary review state, not destructive edits to the working tree.

Rollback steps exercised:

1. Copy the Tai Chi page and required repository references to a temporary root.
2. Remove image references from the temporary copy of `exercises/tai-chi-basics.md`.
3. Remove the Tai Chi image rows from the temporary copy of `media/PROVENANCE.md`.
4. Treat `media/exercises/tai-chi-basics/` as unused Tai Chi assets and omit it from the temporary root.
5. Treat `media/prompts/exercises/tai-chi-basics/` as unused prompt records and omit it from the temporary root.
6. Run focused Markdown-first and privacy checks against the temporary text-only page.

## Validation

Commands exercised against the temporary review state:

```sh
python3 tools/checks/check_markdown_first.py /tmp/gymprimer-tai-chi-rollback.*/exercises/tai-chi-basics.md /tmp/gymprimer-tai-chi-rollback.*/media/PROVENANCE.md /tmp/gymprimer-tai-chi-rollback.*/SOURCES.md /tmp/gymprimer-tai-chi-rollback.*/RED-FLAGS.md
python3 tools/checks/check_privacy.py /tmp/gymprimer-tai-chi-rollback.*/exercises/tai-chi-basics.md /tmp/gymprimer-tai-chi-rollback.*/media/PROVENANCE.md /tmp/gymprimer-tai-chi-rollback.*/SOURCES.md /tmp/gymprimer-tai-chi-rollback.*/RED-FLAGS.md
```

Result: pass.

## Cleanup Contract

If any Tai Chi image fails review after promotion, rollback is:

- remove image references from `exercises/tai-chi-basics.md`;
- remove unused Tai Chi assets from `media/exercises/tai-chi-basics/`;
- remove unused prompt records from `media/prompts/exercises/tai-chi-basics/`;
- remove the matching Tai Chi provenance rows from `media/PROVENANCE.md`;
- rerun the focused Markdown-first and privacy checks before handoff.

## Disposition

The text-only Tai Chi page remains valid without image references, unused Tai Chi assets, prompt records, or provenance rows.

## Residual Risk

The rollback proof validates the page fallback and cleanup sequence. It does not evaluate replacement images; any replacement image must repeat prompt-record, provenance, visual-safety, and beginner-comprehension review.
