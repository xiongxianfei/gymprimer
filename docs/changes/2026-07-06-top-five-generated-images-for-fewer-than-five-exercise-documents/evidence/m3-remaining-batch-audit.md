# M3 Remaining Batch Audit

Date: 2026-07-06

## Batch selection

M3 implements the remaining included exercise documents after the reviewed M2 batch: `brisk-walking`, `chest-press`, `chin-nod`, `dead-bug`, `glute-bridge`, `hip-hinge`, `incline-push-up`, `kneeling-hip-flexor-stretch`, `lat-pulldown`, `plank`, `prone-y-t`, `rowing-machine`, `seated-row`, `tai-chi-basics`, `thoracic-extension`, and `wall-slide`.

## Page outcomes

| Exercise document | Existing accepted images | New promoted images | Total promoted images | Outcome |
|---|---:|---:|---:|---|
| `exercises/brisk-walking.md` | 2 | 3 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/chest-press.md` | 2 | 3 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/chin-nod.md` | 2 | 3 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/dead-bug.md` | 1 | 4 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/glute-bridge.md` | 1 | 4 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/hip-hinge.md` | 1 | 4 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/incline-push-up.md` | 1 | 4 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/kneeling-hip-flexor-stretch.md` | 1 | 4 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/lat-pulldown.md` | 2 | 3 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/plank.md` | 2 | 3 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/prone-y-t.md` | 2 | 3 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/rowing-machine.md` | 3 | 2 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/seated-row.md` | 2 | 3 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/tai-chi-basics.md` | 3 | 2 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/thoracic-extension.md` | 2 | 3 | 5 | Reaches the named top-five target with distinct page-supported images. |
| `exercises/wall-slide.md` | 2 | 3 | 5 | Reaches the named top-five target with distinct page-supported images. |

## Candidate scoring matrix

Scores use 1-5 values for `beginner_comprehension`, `setup_value`, `muscle_attention_value`, `page_value`, and `readiness`.
Disposition values follow the M1 audit framework. Rank 6 and later candidates are not promoted because each M3 page reaches five total accepted images.

### `exercises/brisk-walking.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `movement.png` | 5 | 2 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | New `setup.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `brisk-pace-posture.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `shorter-walk-option.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/chest-press.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `chest-press-machine-example.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | New `setup.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `start-position.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `finish-position.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/chin-nod.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `movement.png` | 5 | 2 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | New `setup.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `start-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `chin-in-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/dead-bug.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `dead-bug-sequence.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | New `setup-crop.png` | 5 | 5 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 3 | New `opposite-reach-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `range-limit-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/glute-bridge.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `glute-bridge-sequence.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | New `setup-crop.png` | 5 | 5 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 3 | New `bridge-top-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `rib-control-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/hip-hinge.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `hip-hinge-sequence.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | New `tall-start-crop.png` | 5 | 5 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 3 | New `hips-back-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `spine-change-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/incline-push-up.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `incline-push-up-phases-example.png` | 5 | 2 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | New `start-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 3 | New `lowered-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `higher-surface.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/kneeling-hip-flexor-stretch.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `kneeling-hip-flexor-stretch-sequence.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | New `setup-crop.png` | 5 | 5 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 3 | New `stretch-position-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `low-back-control-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/lat-pulldown.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `lat-pulldown-machine-example.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `front-lat-pulldown-example.png` | 5 | 2 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | New `setup.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `controlled-finish.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/plank.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `plank-sequence.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | New `full-plank-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `knee-plank-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `hip-control-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/prone-y-t.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `movement.png` | 5 | 2 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | New `setup.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `prone-y-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `prone-t-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/rowing-machine.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `setup.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `movement.png` | 5 | 2 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | Existing `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 4 | New `drive-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `finish-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/seated-row.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `seated-row-machine-example.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | New `setup.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `start-position.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `finish-position.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/tai-chi-basics.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `setup.png` | 5 | 4 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `weight-shift.png` | 5 | 2 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | Existing `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 4 | New `slow-arm-path.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `smaller-range.png` | 5 | 2 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/thoracic-extension.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `movement.png` | 5 | 2 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | New `setup.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `upright-start-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `extension-finish-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |
### `exercises/wall-slide.md`

| Rank | Candidate | beginner_comprehension | setup_value | muscle_attention_value | page_value | readiness | Disposition | Rationale |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Existing `movement.png` | 5 | 2 | 1 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 2 | Existing `muscle-attention.png` | 5 | 2 | 5 | 5 | 5 | existing_accepted | Already page-supported and readable; counts toward the five total images. |
| 3 | New `setup.png` | 5 | 5 | 1 | 5 | 5 | generate_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 4 | New `start-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 5 | New `raised-finish-crop.png` | 5 | 2 | 1 | 5 | 5 | derived_now | Distinct teaching purpose with prompt record, provenance, page reference, and rollback path. |
| 6 | Alternate support candidate 6 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 7 | Alternate support candidate 7 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 8 | Alternate support candidate 8 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 9 | Alternate support candidate 9 | 3 | 2 | 1 | 2 | 2 | defer | Deferred to avoid duplicate coverage within the five-image target. |
| 10 | Equipment-only or decorative candidate | 1 | 1 | 1 | 1 | 2 | reject | Rejected because Markdown and promoted images already provide enough support. |

## Visual and contract evidence

| Asset | Page section | Evidence |
|---|---|---|
| `media/exercises/brisk-walking/setup.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/brisk-walking/brisk-pace-posture.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/brisk-walking/shorter-walk-option.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/chest-press/setup.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/chest-press/start-position.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/chest-press/finish-position.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/chin-nod/setup.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/chin-nod/start-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/chin-nod/chin-in-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/dead-bug/setup-crop.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/dead-bug/opposite-reach-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/dead-bug/range-limit-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/dead-bug/muscle-attention.png` | Used muscles | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/glute-bridge/setup-crop.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/glute-bridge/bridge-top-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/glute-bridge/rib-control-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/glute-bridge/muscle-attention.png` | Used muscles | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/hip-hinge/tall-start-crop.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/hip-hinge/hips-back-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/hip-hinge/spine-change-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/hip-hinge/muscle-attention.png` | Used muscles | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/incline-push-up/start-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/incline-push-up/lowered-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/incline-push-up/muscle-attention.png` | Used muscles | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/incline-push-up/higher-surface.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/kneeling-hip-flexor-stretch/setup-crop.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/kneeling-hip-flexor-stretch/stretch-position-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/kneeling-hip-flexor-stretch/low-back-control-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/kneeling-hip-flexor-stretch/muscle-attention.png` | Used muscles | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/lat-pulldown/setup.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/lat-pulldown/muscle-attention.png` | Used muscles | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/lat-pulldown/controlled-finish.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/plank/full-plank-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/plank/knee-plank-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/plank/hip-control-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/prone-y-t/setup.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/prone-y-t/prone-y-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/prone-y-t/prone-t-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/rowing-machine/drive-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/rowing-machine/finish-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/seated-row/setup.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/seated-row/start-position.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/seated-row/finish-position.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/tai-chi-basics/slow-arm-path.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/tai-chi-basics/smaller-range.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/thoracic-extension/setup.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/thoracic-extension/upright-start-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/thoracic-extension/extension-finish-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/wall-slide/setup.png` | Setup | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/wall-slide/start-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |
| `media/exercises/wall-slide/raised-finish-crop.png` | Movement or option | No embedded writing, no brand marks, faceless support image, and nearby Markdown carries the instruction. |

## Source-support and beginner-comprehension proof

The promoted images are support-only. Setup images sit next to equipment or setup text, movement images sit next to movement phases, easier-option images sit next to easier-version or important-note text, and muscle-attention images sit next to the used-muscles section.
Existing accepted images remain counted when they are readable and source-compatible. Older sequence images are preserved and supplemented with crops only where a larger single-position reference improves beginner comprehension without replacing the original sequence.

## Rollback proof

Each promoted M3 image is independently removable by deleting its Markdown image reference, generated or derived asset, prompt record, and single `media/PROVENANCE.md` row.
The surrounding exercise page remains readable because the Markdown setup, movement, muscles, feel cues, important notes, and sources remain the source of truth.
No promoted M3 page depends on a sixth image or a second muscle-attention image.

## Validation

M3 validation commands are recorded in the plan after local execution.

## Sources

- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/m1-audit-framework.md`
- `media/PROVENANCE.md`
- M3 exercise pages listed in this audit
