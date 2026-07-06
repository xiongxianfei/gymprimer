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

ACCEPTED_PURPOSES = {
    "exercise_setup_illustration",
    "exercise_movement_illustration",
    "exercise_muscle_attention_illustration",
}

LEGACY_COMPATIBLE_PURPOSES = {
    "equipment_identification",
    "key_movement_illustration",
}

FORBIDDEN_CLAIM_TERMS = (
    "treatment",
    "cure",
    "individualized coaching",
    "clinical assessment",
    "recovery-care protocol",
    "workout planner",
)

REQUIRED_CLOSEOUT_PROOF_FIELDS = {
    "exercise_documents",
    "generated_image_count",
    "generated_image_paths",
    "visual_safety_review",
    "source_support_audit",
    "beginner_comprehension_proof",
    "privacy_review",
    "rollback_proof",
    "non_goal_smoke",
}

REQUIRED_NON_GOAL_FLAGS = (
    "no_pr_review_rule",
    "no_hosted_app",
    "no_cms",
    "no_database",
    "no_api",
    "no_video_first_path",
    "no_personalized_coaching",
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

TOP_FIVE_INITIATIVE = "top_five_generated_images_for_fewer_than_five_exercise_documents"
NAMED_TOP_FIVE_EXERCISE_DOCUMENTS = (
    "exercises/band-pull-apart.md",
    "exercises/bird-dog.md",
    "exercises/brisk-walking.md",
    "exercises/chest-press.md",
    "exercises/chin-nod.md",
    "exercises/dead-bug.md",
    "exercises/glute-bridge.md",
    "exercises/hip-hinge.md",
    "exercises/incline-push-up.md",
    "exercises/kneeling-hip-flexor-stretch.md",
    "exercises/lat-pulldown.md",
    "exercises/plank.md",
    "exercises/prone-y-t.md",
    "exercises/rowing-machine.md",
    "exercises/seated-row.md",
    "exercises/tai-chi-basics.md",
    "exercises/thoracic-extension.md",
    "exercises/wall-slide.md",
)
TOP_FIVE_REQUIRED_AUDIT_FIELDS = {
    "accepted_existing_image_count",
    "accepted_older_sequence_image_count",
    "new_generated_image_need",
    "top_five_generation_target",
    "coverage_limit_outcome",
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


def is_top_five_initiative(record: Mapping[str, object]) -> bool:
    return record.get("initiative") == TOP_FIVE_INITIATIVE


def validate_named_top_five_population(exercise_documents: Sequence[str]) -> list[str]:
    expected = set(NAMED_TOP_FIVE_EXERCISE_DOCUMENTS)
    actual = set(exercise_documents)
    errors: list[str] = []
    for path in sorted(expected - actual):
        errors.append(f"named_top_five_population_missing: {path}")
    for path in sorted(actual - expected):
        if path == "exercises/baduanjin-basics.md":
            errors.append(f"named_top_five_population_excludes_baduanjin: {path}")
        else:
            errors.append(f"named_top_five_population_unexpected: {path}")
    return errors


def top_five_image_need(record: Mapping[str, object]) -> int | None:
    accepted_existing = record.get("accepted_existing_image_count")
    if not isinstance(accepted_existing, int):
        return None
    return max(0, 5 - accepted_existing)


def validate_audit_record(record: Mapping[str, object]) -> list[str]:
    errors: list[str] = []
    for field in sorted(REQUIRED_AUDIT_FIELDS):
        if field not in record:
            errors.append(f"audit_missing_required_field: {field}")
    if is_top_five_initiative(record):
        for field in sorted(TOP_FIVE_REQUIRED_AUDIT_FIELDS):
            if field not in record:
                errors.append(f"audit_missing_required_field: {field}")
        errors.extend(validate_top_five_audit_record(record))

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

    errors.extend(validate_generation_decision(record))

    return errors


def validate_top_five_audit_record(record: Mapping[str, object]) -> list[str]:
    errors: list[str] = []
    exercise_document = record.get("exercise_document")
    if isinstance(exercise_document, str):
        if exercise_document not in NAMED_TOP_FIVE_EXERCISE_DOCUMENTS:
            if exercise_document == "exercises/baduanjin-basics.md":
                errors.append(f"named_top_five_population_excludes_baduanjin: {exercise_document}")
            else:
                errors.append(f"named_top_five_population_unexpected: {exercise_document}")

    accepted_existing = record.get("accepted_existing_image_count")
    if not isinstance(accepted_existing, int):
        if "accepted_existing_image_count" in record:
            errors.append("accepted_existing_image_count_must_be_integer")
        return errors
    if accepted_existing < 0 or accepted_existing > 5:
        errors.append("accepted_existing_image_count_out_of_range")

    accepted_older_sequence = record.get("accepted_older_sequence_image_count", 0)
    if not isinstance(accepted_older_sequence, int):
        errors.append("accepted_older_sequence_image_count_must_be_integer")
    elif accepted_older_sequence < 0:
        errors.append("accepted_older_sequence_image_count_out_of_range")
    elif accepted_older_sequence > accepted_existing:
        errors.append("accepted_older_sequence_count_exceeds_existing_count")

    expected_need = max(0, 5 - accepted_existing)
    if record.get("new_generated_image_need") != expected_need:
        errors.append("new_generated_image_need_mismatch")

    target = record.get("top_five_generation_target")
    if not isinstance(target, Sequence) or isinstance(target, (str, bytes)):
        errors.append("top_five_generation_target_must_be_list")
    elif len(target) > 5:
        errors.append("top_five_generation_target_exceeds_five")

    coverage_limit = record.get("coverage_limit_outcome")
    if not isinstance(coverage_limit, Mapping):
        if "coverage_limit_outcome" in record:
            errors.append("coverage_limit_outcome_must_be_mapping")
    else:
        target_total = coverage_limit.get("target_total_images")
        if not isinstance(target_total, int):
            errors.append("coverage_limit_target_total_images_must_be_integer")
        elif target_total > 5:
            errors.append("coverage_limit_target_exceeds_five")
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
        purpose = str(raw_candidate.get("purpose", ""))
        if purpose and purpose not in ACCEPTED_PURPOSES:
            errors.append(f"candidate_purpose_not_accepted: rank {rank}")
        errors.extend(validate_forbidden_claims(raw_candidate, rank))
        if isinstance(rank, int) and rank <= 5 and disposition in GENERATE_DISPOSITIONS and not is_top_five_initiative(record):
            if disposition == "automatic_generation":
                errors.append(f"top_five_candidate_must_not_be_automatic_generation: rank {rank}")
            else:
                errors.append(f"top_five_candidate_must_not_select_generation_directly: rank {rank}")
        if isinstance(rank, int) and rank > 5 and disposition in GENERATE_DISPOSITIONS:
            if is_top_five_initiative(record):
                if not raw_candidate.get("later_approved_sixth_image_authorization"):
                    errors.append(f"sixth_candidate_generation_not_allowed: rank {rank}")
            elif not raw_candidate.get("downstream_churn_rationale"):
                errors.append(f"sixth_candidate_generation_missing_churn_rationale: rank {rank}")
    return errors


def validate_generation_decision(record: Mapping[str, object]) -> list[str]:
    errors: list[str] = []
    generation_decision = record.get("generation_decision")
    if not isinstance(generation_decision, Mapping):
        if "generation_decision" in record:
            errors.append("generation_decision_must_be_mapping")
        return errors

    selected_count = generation_decision.get("selected_count", 0)
    if not isinstance(selected_count, int):
        errors.append("generation_selected_count_must_be_integer")
        return errors

    current_image_count = record.get("current_image_count", 0)
    if not isinstance(current_image_count, int):
        errors.append("current_image_count_must_be_integer")
        return errors

    final_image_count = current_image_count + selected_count
    if final_image_count in {4, 5} and not is_top_five_initiative(record) and not record.get("image_count_exception_approval"):
        errors.append("image_count_exception_required_for_four_or_five_images")
    if final_image_count > 5:
        errors.append("image_count_exceeds_first_slice_limit")

    selected_purposes = generation_decision.get("selected_purposes", [])
    if not isinstance(selected_purposes, Sequence) or isinstance(selected_purposes, (str, bytes)):
        errors.append("generation_selected_purposes_must_be_list")
        return errors

    for purpose in selected_purposes:
        if purpose not in ACCEPTED_PURPOSES:
            errors.append(f"generation_purpose_not_accepted: {purpose}")

    existing_purposes = record.get("existing_image_purposes", [])
    if not isinstance(existing_purposes, Sequence) or isinstance(existing_purposes, (str, bytes)):
        errors.append("existing_image_purposes_must_be_list")
        return errors

    muscle_attention_count = sum(
        1
        for purpose in (*existing_purposes, *selected_purposes)
        if purpose == "exercise_muscle_attention_illustration"
    )
    if muscle_attention_count > 1:
        errors.append("second_muscle_attention_image_not_allowed")
    return errors


def validate_forbidden_claims(candidate: Mapping[str, object], rank: object) -> list[str]:
    candidate_text = " ".join(
        str(candidate.get(field, ""))
        for field in ("candidate_image", "why_it_matters", "page_section_supported", "disposition")
    ).lower()
    return [
        f"candidate_forbidden_claim: rank {rank} {term}"
        for term in FORBIDDEN_CLAIM_TERMS
        if term in candidate_text
    ]


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


def validate_slice_scope(exercise_documents: Sequence[str], rationale: str = "") -> list[str]:
    if len(exercise_documents) <= 1:
        return []
    if len(exercise_documents) == 2 and rationale.strip():
        return []
    return ["first_slice_scope_too_broad_without_rationale"]


def validate_closeout_proof(proof: Mapping[str, object]) -> list[str]:
    errors: list[str] = []
    for field in sorted(REQUIRED_CLOSEOUT_PROOF_FIELDS):
        if field not in proof:
            errors.append(f"closeout_proof_missing_required_field: {field}")

    generated_count = proof.get("generated_image_count", 0)
    if not isinstance(generated_count, int):
        errors.append("generated_image_count_must_be_integer")
        return errors

    generated_paths = proof.get("generated_image_paths", [])
    if not isinstance(generated_paths, Sequence) or isinstance(generated_paths, (str, bytes)):
        errors.append("generated_image_paths_must_be_list")
        return errors
    if generated_count != len(generated_paths):
        errors.append("generated_image_count_path_mismatch")

    top_five_initiative = is_top_five_initiative(proof)
    visual_review = proof.get("visual_safety_review")
    if isinstance(visual_review, Mapping):
        visual_status = visual_review.get("status")
        reviewed_items = visual_review.get("reviewed_items", [])
        if generated_count > 0 and visual_status == "not_triggered_no_generated_images":
            errors.append("visual_safety_review_required_for_generated_images")
        if generated_count > 0 and len(reviewed_items) != generated_count and not top_five_initiative:
            errors.append("visual_safety_review_item_count_mismatch")
    elif "visual_safety_review" in proof:
        errors.append("visual_safety_review_must_be_mapping")

    source_audit = proof.get("source_support_audit")
    if isinstance(source_audit, Mapping):
        if source_audit.get("status") != "passed":
            errors.append("source_support_audit_not_passed")
        unsupported_claims = source_audit.get("unsupported_claims", [])
        if unsupported_claims:
            errors.append("source_support_audit_has_unsupported_claims")
    elif "source_support_audit" in proof:
        errors.append("source_support_audit_must_be_mapping")

    privacy_review = proof.get("privacy_review")
    if isinstance(privacy_review, Mapping):
        if privacy_review.get("status") != "passed":
            errors.append("privacy_review_not_passed")
        if privacy_review.get("private_data_present") is not False:
            errors.append("privacy_review_private_data_present")
    elif "privacy_review" in proof:
        errors.append("privacy_review_must_be_mapping")

    rollback_proof = proof.get("rollback_proof")
    if isinstance(rollback_proof, Mapping):
        commands = rollback_proof.get("commands", [])
        if not isinstance(commands, Sequence) or isinstance(commands, (str, bytes)) or not commands:
            errors.append("rollback_proof_missing_commands")
        if rollback_proof.get("page_readable_without_new_images") is not True:
            errors.append("rollback_proof_page_not_readable")
    elif "rollback_proof" in proof:
        errors.append("rollback_proof_must_be_mapping")

    non_goal_smoke = proof.get("non_goal_smoke")
    if isinstance(non_goal_smoke, Mapping):
        for flag in REQUIRED_NON_GOAL_FLAGS:
            if non_goal_smoke.get(flag) is not True:
                errors.append(f"non_goal_smoke_failed: {flag}")
    elif "non_goal_smoke" in proof:
        errors.append("non_goal_smoke_must_be_mapping")

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
