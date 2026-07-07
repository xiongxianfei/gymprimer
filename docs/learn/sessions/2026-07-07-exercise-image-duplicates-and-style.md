# Learn Session: Exercise Image Duplicates and Style Consistency

## Result

- Skill: learn
- Status: recorded
- Artifacts changed: `docs/learn/sessions/2026-07-07-exercise-image-duplicates-and-style.md`
- Open blockers: none for this learn record
- Next stage: none from learn
- Session path: `docs/learn/sessions/2026-07-07-exercise-image-duplicates-and-style.md`
- Lessons captured: none
- Follow-ups: proposal candidate only; no follow-up artifact created

## Frame

- Trigger: explicit `$learn` invocation after PR #16, with maintainer observation that many generated exercise images have duplicate meaning and inconsistent visual style.
- Trigger type: explicit maintainer request and contributor observation.
- Scope: image-selection and image-generation quality practices for the top-five exercise image initiative and future generated exercise image batches.
- Evidence in scope:
  - `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
  - `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
  - `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md`
  - `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m2-first-batch-audit.md`
  - `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m3-remaining-batch-audit.md`
  - `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/verify-report.md`
  - `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/explain-change.md`
- Explicit exclusions:
  - No generated image asset is replaced in this learn session.
  - No exercise page, media provenance row, prompt record, spec, architecture, workflow, or PR metadata is changed.
  - No claim is made that PR #16 is approved, failed, merged, or CI-passed.
  - No new repository policy is created from this learn record alone.
- Prior learnings reviewed:
  - `docs/learn/topics/content-quality.md`
  - `docs/learn/sessions/2026-07-05-walking-image-timing.md`
  - `docs/learn/sessions/2026-07-04-muscle-guidance-best-practices.md`
  - `docs/learn/sessions/2026-06-29-responsible-breadth-content-quality.md`

## Observe

| Observation ID | Observation | Evidence |
| --- | --- | --- |
| OBS-001 | The approved spec already rejects low-value filler and duplicate coverage in principle. | R13 requires a coverage limit below five when the audit cannot identify five distinct, source-supported, beginner-useful image purposes. R25-R26 forbid replacing acceptable images for style alone and allow replacement for duplicate coverage after better images are added. |
| OBS-002 | The implementation recorded duplicate-coverage deferrals, but the audit still optimized mostly page-by-page rather than enforcing a cross-page visual system. | M2 records `band-pull-apart` at four images because a fifth candidate duplicated movement coverage. M3 repeatedly defers alternate support candidates to avoid duplicate coverage within the five-image target. |
| OBS-003 | The current tests prove structure, provenance, prompt records, counts, score ranges, and one muscle-attention image per page, but they cannot judge visual sameness or style mismatch. | The verify report records unit, Markdown-first, privacy, whitespace, and direct image-count proof. It also records that visual inspection was sampled during code review rather than exhaustive across every bitmap pixel. |
| OBS-004 | The maintainer observation points to a broader quality gap: a page can satisfy the numeric top-five target and still feel repetitive or visually inconsistent to a human reader. | The trigger statement names duplicate meaning and different visual styles across images after PR #16. Existing artifacts have no accepted cross-page style rubric, shot taxonomy, or duplicate-similarity threshold. |

## Classify

| Observation ID | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
| --- | --- | --- | --- | --- | --- |
| OBS-001 to OBS-003 | observation | observation | session record only | Existing spec, audit evidence, and verify report | The project already has partial guardrails, and this session should not restate them as new durable guidance. |
| OBS-004 | direction | direction-candidate | future proposal/spec amendment for generated exercise image quality | Maintainer observation; no accepted artifact yet | A style and duplicate-meaning standard would change image-generation policy, audit criteria, prompt templates, review expectations, and possibly validation. It needs an owning proposal/spec, not a learn-topic policy entry. |
| OBS-001 to OBS-004 | no-durable-lesson | no-durable-lesson | none | Learn skill evidence standard | The observation is credible and useful, but durable enforcement needs an accepted artifact. No topic entry was added. |

## Route

- Topic updates: none.
- Authoritative artifact updates: none.
- Follow-ups created: none.
- Recommended route: open a proposal for a generated exercise image quality standard before the next broad image-generation batch.

## Best Practices Candidate

These are recommended practices for a future proposal or spec amendment:

1. Use image purpose before image count.
   - Count a candidate only when it teaches a distinct beginner job: setup, one movement phase, easier range, common control cue, or one broad muscle-attention view.
   - If two images answer the same beginner question, keep the clearer one and record a coverage-limit outcome instead of forcing five.

2. Add a duplicate-meaning review before promotion.
   - Compare every new image against existing page images and the other top-five candidates.
   - Reject candidates with the same setup, same pose, same camera angle, and same teaching purpose even if filenames or prompts differ.
   - Treat "slightly different limb position" as duplicate unless the nearby Markdown needs that exact distinction.

3. Create a shot taxonomy per exercise page.
   - Example set: setup, start, finish, easier option, common range limit, muscle attention.
   - Do not generate multiple images from one taxonomy slot unless an approved exception explains why beginners need both.

4. Use a style brief for the whole batch.
   - Keep consistent framing, background simplicity, lighting, clothing neutrality, camera distance, crop ratio, and faceless/non-identifying presentation.
   - For derived crops, make sure the crop still looks intentional next to generated full-frame images.

5. Prefer visual consistency over model variety.
   - Avoid mixing obviously different illustration/photo styles within one exercise page.
   - Avoid mixing high-detail generated images with rough crops unless the crop has a clearly better teaching purpose.

6. Make prompt records carry style constraints.
   - Prompt records should name the desired visual style, framing, camera angle, background, and what must not change from sibling images.
   - The selected-output notes should say why the image is distinct from existing images.

7. Add a human visual review checklist before PR.
   - Check duplicate meaning, style consistency, anatomical plausibility, no embedded text, no brand marks, no misleading visual implication, and no second muscle-attention image.
   - Record exceptions in change-local evidence when a visually inconsistent image is kept because it teaches something uniquely important.

8. Separate page-local and cross-page review.
   - Page-local review checks whether the images help that exercise.
   - Cross-page review checks whether the generated library feels coherent across the primer.

9. Prefer replacing the weakest duplicate over adding another support image.
   - If a better image covers the same purpose as an older accepted image, decide whether the older image should remain, be replaced for a concrete reason, or be removed from the page count.
   - Do not replace style alone, but do not keep duplicate coverage only because both assets exist.

10. Add tests only for what automation can judge.
    - Keep automated tests for counts, provenance, prompt records, purposes, page refs, score fields, and one muscle-attention limit.
    - Treat visual duplicate meaning and style consistency as manual or review evidence unless a later proposal accepts a deterministic heuristic.

## Suggested Proposal Shape

Potential proposal title:
`Generated Exercise Image Quality Standard`

Potential scope:

- Define a batch-level visual style brief for generated exercise images.
- Define duplicate-meaning review criteria and page-local shot taxonomy.
- Require selected-output notes to explain each promoted image's distinct teaching purpose.
- Add change-local manual proof for visual consistency and duplicate-meaning review.
- Decide whether existing PR #16 assets should be audited in a follow-up improvement slice.

Potential non-goals:

- No blanket requirement to replace older accepted images for style alone.
- No automatic computer-vision similarity gate unless separately researched and specified.
- No requirement that every exercise page have exactly five images when distinct useful purposes are unavailable.
- No in-image labels, citations, warnings, clinical assessment claims, treatment, or personalized coaching.

## No-Learn Rationale

No durable topic entry was added.
The maintainer observation identifies a useful improvement direction, but changing image-generation behavior needs a proposal/spec update because it affects audit criteria, prompt records, visual review, validation expectations, and review effort.

## Validation

- Session record only; no product content, media, spec, plan, workflow, skill, provenance, or topic file changed.

## Sources

- `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m2-first-batch-audit.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m3-remaining-batch-audit.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/verify-report.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/explain-change.md`
