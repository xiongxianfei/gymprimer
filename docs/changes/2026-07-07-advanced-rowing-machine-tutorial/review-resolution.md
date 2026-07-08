# Review Resolution: Advanced Rowing Machine Tutorial

Change ID: `2026-07-07-advanced-rowing-machine-tutorial`

Current milestone: M1

Status: closed

Closeout status: closed

## Findings

| Finding ID | Source review | Severity | Status | Required outcome |
| --- | --- | --- | --- | --- |
| CR1 | `reviews/code-review-r1.md` | major | resolved | Added advanced-rowing media forbidden text checks and temporary-root tests for copied PM5 UI, screenshots, logos or brand marks, identifiable people, correct/wrong badges, red pain marks, elite/race-win framing, and unsupported promises; accepted by code-review R2. |
| CR2 | `reviews/code-review-r1.md` | major | resolved | Extended advanced-rowing forbidden-scope checks and tests for calculated personal targets, personal watts or paces, full benchmark plans, competition programming, active recovery protocols, and clinical protocol wording; accepted by code-review R2. |

## Resolution Notes

CR1 fix applied:

- Added `ADVANCED_ROWING_FORBIDDEN_MEDIA_TEXT_RE` to reject copied UI, screenshots, logos or brand marks, identifiable people, correct/wrong badges, red pain marks, elite/race-win framing, and unsupported promises from advanced rowing media prompt/provenance text.
- Added `advanced_rowing_media_text_forbidden` findings for matching advanced rowing image-instruction packets.
- Added temporary-root tests for representative excluded media text cases.

CR2 fix applied:

- Extended `ADVANCED_ROWING_FORBIDDEN_SCOPE_PATTERNS` for calculated personal targets, personal watts or paces, full benchmark plans, competition programming, active recovery protocols, medical judgment, treatment plans, and injury-specific protocols.
- Added temporary-root tests for the missing forbidden-scope cases.

Code-review R2 accepted both finding resolutions.

## Validation Evidence

Passed locally:

```bash
python3 -m unittest tests.test_advanced_rowing_machine_tutorial
python3 -m unittest discover -s tests
python3 tools/checks/check_markdown_first.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md
python3 tools/checks/check_privacy.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial
git diff --check
```

## Required Validation After Fix

```bash
python3 -m unittest tests.test_advanced_rowing_machine_tutorial
python3 -m unittest discover -s tests
python3 tools/checks/check_markdown_first.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md
python3 tools/checks/check_privacy.py tests/fixtures/advanced-rowing-machine-tutorial media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-07-advanced-rowing-machine-tutorial
git diff --check
```

## Sources

- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/code-review-r1.md`
- `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`
- `specs/advanced-rowing-machine-tutorial.test.md`
