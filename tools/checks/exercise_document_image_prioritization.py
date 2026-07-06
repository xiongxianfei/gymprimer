from __future__ import annotations

from pathlib import Path
import re
from typing import Mapping, Sequence


IMAGE_REFERENCE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

REQUIRED_AUDIT_FIELDS = {
    "exercise_document",
    "current_image_count",
    "existing_image_purposes",
    "section_coverage",
    "source_support_issues",
    "existing_image_decisions",
    "candidate_table",
    "generation_decision",
    "validation_expectations",
    "rollback_path",
    "top_five_are_backlog",
    "template_update_status",
}

REQUIRED_CANDIDATE_FIELDS = {
    "rank",
    "candidate_image",
    "page_section_supported",
    "purpose",
    "why_it_matters",
    "scores",
    "score",
    "disposition",
}

SCORE_FIELDS = (
    "beginner_comprehension",
    "safety_setup_value",
    "muscle_attention_value",
    "page_value",
    "readiness",
)

ACCEPTED_REPLACEMENT_REASONS = {
    "unsafe_visual_implication",
    "missing_required_provenance_or_prompt_record",
    "alt_text_requires_asset_change",
    "misleading_common_mistake_framing",
    "incompatible_purpose",
    "low_readability",
    "duplicate_coverage_after_better_images",
}

ACCEPTED_NO_REPLACEMENT_REASONS = {
    "acceptable_existing_image",
    "not_page_local_scope",
}

GENERATE_DISPOSITIONS = {
    "generate_now",
    "first_generation_candidate",
    "automatic_generation",
}


def markdown_image_count(text: str) -> int:
    return len(IMAGE_REFERENCE_RE.findall(text))


def image_count_by_exercise(root: Path) -> dict[str, int]:
    exercise_root = root / "exercises"
    counts: dict[str, int] = {}
    for page in sorted(exercise_root.glob("*.md")):
        relative_path = page.relative_to(root).as_posix()
        counts[relative_path] = markdown_image_count(page.read_text(encoding="utf-8"))
    return counts


def evaluation_population(root: Path, threshold: int = 5) -> list[Path]:
    exercise_root = root / "exercises"
    population: list[Path] = []
    for page in sorted(exercise_root.glob("*.md")):
        count = markdown_image_count(page.read_text(encoding="utf-8"))
        if count < threshold:
            population.append(page)
    return population


def validate_audit_record(record: Mapping[str, object]) -> list[str]:
    errors: list[str] = []
    for field in sorted(REQUIRED_AUDIT_FIELDS):
        if field not in record:
            errors.append(f"audit_missing_required_field: {field}")

    candidate_table = record.get("candidate_table")
    if isinstance(candidate_table, Sequence) and not isinstance(candidate_table, (str, bytes)):
        errors.extend(validate_candidate_table(candidate_table, record))
    elif "candidate_table" in record:
        errors.append("candidate_table_must_be_list")

    image_decisions = record.get("existing_image_decisions")
    if isinstance(image_decisions, Sequence) and not isinstance(image_decisions, (str, bytes)):
        errors.extend(validate_image_decisions(image_decisions))
    elif "existing_image_decisions" in record:
        errors.append("existing_image_decisions_must_be_list")

    if record.get("top_five_are_backlog") is not True:
        errors.append("top_five_are_backlog_must_be_true")

    if record.get("template_update_status") != "deferred" and "template_update_approval" not in record:
        errors.append("template_update_requires_later_approval")

    return errors


def validate_candidate_table(candidate_table: Sequence[object], record: Mapping[str, object]) -> list[str]:
    errors: list[str] = []
    if len(candidate_table) < 10 and not record.get("fewer_than_ten_rationale"):
        errors.append("candidate_table_missing_fewer_than_ten_rationale")

    for raw_candidate in candidate_table:
        if not isinstance(raw_candidate, Mapping):
            errors.append("candidate_must_be_mapping")
            continue
        rank = raw_candidate.get("rank", "unknown")
        for field in sorted(REQUIRED_CANDIDATE_FIELDS):
            if field not in raw_candidate:
                errors.append(f"candidate_missing_required_field: rank {rank} {field}")
        errors.extend(validate_candidate_scores(raw_candidate))
        disposition = str(raw_candidate.get("disposition", ""))
        if isinstance(rank, int) and rank <= 5 and disposition == "automatic_generation":
            errors.append(f"top_five_candidate_must_not_be_automatic_generation: rank {rank}")
        if isinstance(rank, int) and rank > 5 and disposition in GENERATE_DISPOSITIONS:
            if not raw_candidate.get("downstream_churn_rationale"):
                errors.append(f"sixth_candidate_generation_missing_churn_rationale: rank {rank}")
    return errors


def validate_candidate_scores(candidate: Mapping[str, object]) -> list[str]:
    errors: list[str] = []
    rank = candidate.get("rank", "unknown")
    scores = candidate.get("scores")
    if not isinstance(scores, Mapping):
        return [f"candidate_scores_must_be_mapping: rank {rank}"]

    total = 0
    for field in SCORE_FIELDS:
        value = scores.get(field)
        if not isinstance(value, int) or value < 1 or value > 5:
            errors.append(f"candidate_score_out_of_range: rank {rank} {field}")
            continue
        total += value

    if "score" in candidate and candidate.get("score") != total:
        errors.append(f"candidate_score_mismatch: rank {rank}")
    return errors


def validate_image_decisions(image_decisions: Sequence[object]) -> list[str]:
    errors: list[str] = []
    for raw_decision in image_decisions:
        if not isinstance(raw_decision, Mapping):
            errors.append("image_decision_must_be_mapping")
            continue
        image_path = str(raw_decision.get("image_path", "unknown"))
        decision = str(raw_decision.get("decision", ""))
        reason = str(raw_decision.get("reason", ""))
        if decision in {"replace", "normalize"}:
            if reason == "style_consistency":
                errors.append(f"style_only_replacement_not_allowed: {image_path}")
            elif reason not in ACCEPTED_REPLACEMENT_REASONS:
                errors.append(f"replacement_reason_not_accepted: {image_path}")
        elif decision == "preserve" and reason not in ACCEPTED_NO_REPLACEMENT_REASONS:
            errors.append(f"preserve_reason_not_accepted: {image_path}")
    return errors
