from pathlib import Path
import tempfile
import unittest

from tools.checks.exercise_document_image_prioritization import (
    ACCEPTED_REPLACEMENT_REASONS,
    NAMED_TOP_FIVE_EXERCISE_DOCUMENTS,
    evaluation_population,
    image_count_by_exercise,
    top_five_image_need,
    validate_slice_scope,
    validate_audit_record,
    validate_closeout_proof,
    validate_named_top_five_population,
)


def write_page(root: Path, slug: str, image_count: int) -> Path:
    exercises = root / "exercises"
    exercises.mkdir(exist_ok=True)
    image_lines = "\n".join(
        f"![{slug} support image {index}](../media/exercises/{slug}/image-{index}.png)"
        for index in range(1, image_count + 1)
    )
    page = exercises / f"{slug}.md"
    page.write_text(
        f"# {slug.replace('-', ' ').title()}\n\n{image_lines}\n",
        encoding="utf-8",
    )
    return page


def candidate(rank: int, **overrides: object) -> dict[str, object]:
    base = {
        "rank": rank,
        "candidate_image": f"Candidate {rank}",
        "page_section_supported": "Setup",
        "purpose": "exercise_setup_illustration",
        "why_it_matters": "Clarifies a beginner setup point.",
        "scores": {
            "beginner_comprehension": 4,
            "setup_value": 4,
            "muscle_attention_value": 1,
            "page_value": 3,
            "readiness": 5,
        },
        "score": 17,
        "disposition": "candidate_backlog" if rank <= 5 else "later_candidate",
    }
    base.update(overrides)
    return base


def valid_audit_record(**overrides: object) -> dict[str, object]:
    record = {
        "exercise_document": "exercises/fixture.md",
        "current_image_count": 2,
        "existing_image_purposes": ["exercise_setup_illustration"],
        "section_coverage": {
            "purpose": "present",
            "setup": "present",
            "movement": "present",
            "muscle_guidance": "present",
            "safety": "present",
            "sources": "present",
        },
        "source_support_issues": [],
        "existing_image_decisions": [
            {
                "image_path": "media/exercises/fixture/setup.png",
                "decision": "preserve",
                "reason": "acceptable_existing_image",
            }
        ],
        "candidate_table": [candidate(rank) for rank in range(1, 11)],
        "generation_decision": {
            "selected_count": 0,
            "decision": "no_generation_needed",
            "rationale": "Current Markdown and existing image are sufficient.",
        },
        "validation_expectations": ["CMD1", "CMD4", "CMD6", "CMD9"],
        "rollback_path": "Remove new references and keep the Markdown page readable.",
        "top_five_are_backlog": True,
        "template_update_status": "deferred",
    }
    record.update(overrides)
    return record


def valid_top_five_audit_record(**overrides: object) -> dict[str, object]:
    record = valid_audit_record(
        initiative="top_five_generated_images_for_fewer_than_five_exercise_documents",
        exercise_document="exercises/bird-dog.md",
        current_image_count=1,
        accepted_existing_image_count=1,
        accepted_older_sequence_image_count=1,
        existing_image_purposes=["exercise_movement_illustration"],
        new_generated_image_need=4,
        candidate_table=[
            candidate(rank, disposition="generate_now" if rank <= 4 else "preserve_existing" if rank == 5 else "later_candidate")
            for rank in range(1, 11)
        ],
        top_five_generation_target=[1, 2, 3, 4, 5],
        coverage_limit_outcome={
            "target_total_images": 5,
            "reason": "five_distinct_supported_purposes",
        },
        generation_decision={
            "selected_count": 4,
            "decision": "generate_to_top_five_total",
            "rationale": "Named population targets five total accepted images.",
            "selected_purposes": [
                "exercise_setup_illustration",
                "exercise_movement_illustration",
                "exercise_movement_illustration",
                "exercise_muscle_attention_illustration",
            ],
        },
    )
    record.update(overrides)
    return record


def valid_closeout_proof(**overrides: object) -> dict[str, object]:
    proof = {
        "exercise_documents": ["exercises/bird-dog.md"],
        "generated_image_count": 0,
        "generated_image_paths": [],
        "visual_safety_review": {
            "status": "not_triggered_no_generated_images",
            "reviewed_items": [],
        },
        "source_support_audit": {
            "status": "passed",
            "sampled_claims": [
                "setup",
                "movement",
                "muscle_guidance",
                "safety_notes",
                "sources",
            ],
            "unsupported_claims": [],
        },
        "beginner_comprehension_proof": {
            "status": "minimum_needed_subset_is_zero",
            "prompts": [
                "Can the page explain setup without new images?",
                "Can the page explain movement without new images?",
            ],
            "unresolved_confusion": [],
        },
        "privacy_review": {
            "status": "passed",
            "private_data_present": False,
        },
        "rollback_proof": {
            "status": "passed",
            "paths_to_remove": [],
            "commands": [
                "python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization",
                "python3 tools/checks/check_privacy.py -- exercises media docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization",
            ],
            "page_readable_without_new_images": True,
        },
        "non_goal_smoke": {
            "no_pr_review_rule": True,
            "no_hosted_app": True,
            "no_cms": True,
            "no_database": True,
            "no_api": True,
            "no_video_first_path": True,
            "no_personalized_coaching": True,
        },
    }
    proof.update(overrides)
    return proof


class ExerciseDocumentImagePrioritizationTest(unittest.TestCase):
    def test_named_top_five_population_is_exact_and_excludes_baduanjin(self) -> None:
        errors = validate_named_top_five_population(NAMED_TOP_FIVE_EXERCISE_DOCUMENTS)

        self.assertEqual(errors, [])
        self.assertIn(
            "named_top_five_population_excludes_baduanjin: exercises/baduanjin-basics.md",
            validate_named_top_five_population(
                [*NAMED_TOP_FIVE_EXERCISE_DOCUMENTS, "exercises/baduanjin-basics.md"]
            ),
        )
        self.assertIn(
            "named_top_five_population_missing: exercises/bird-dog.md",
            validate_named_top_five_population(
                [path for path in NAMED_TOP_FIVE_EXERCISE_DOCUMENTS if path != "exercises/bird-dog.md"]
            ),
        )

    def test_evaluation_population_uses_fewer_than_five_trigger(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            zero = write_page(root, "zero-image", 0)
            one = write_page(root, "one-image", 1)
            four = write_page(root, "four-image", 4)
            write_page(root, "five-image", 5)
            write_page(root, "six-image", 6)

            counts = image_count_by_exercise(root)
            population = evaluation_population(root)

        self.assertEqual(counts["exercises/zero-image.md"], 0)
        self.assertEqual(counts["exercises/four-image.md"], 4)
        self.assertEqual(population, sorted([zero, one, four]))

    def test_top_five_need_counts_existing_and_older_sequence_images(self) -> None:
        self.assertEqual(top_five_image_need(valid_top_five_audit_record(accepted_existing_image_count=1)), 4)
        self.assertEqual(top_five_image_need(valid_top_five_audit_record(accepted_existing_image_count=2)), 3)
        self.assertEqual(top_five_image_need(valid_top_five_audit_record(accepted_existing_image_count=3)), 2)
        self.assertEqual(
            validate_audit_record(
                valid_top_five_audit_record(
                    accepted_existing_image_count=1,
                    accepted_older_sequence_image_count=2,
                )
            ),
            ["accepted_older_sequence_count_exceeds_existing_count"],
        )

    def test_named_top_five_audit_uses_setup_value_score_field(self) -> None:
        setup_value_record = valid_top_five_audit_record()
        missing_setup_value = valid_top_five_audit_record(
            candidate_table=[
                candidate(
                    1,
                    scores={
                        "beginner_comprehension": 4,
                        "muscle_attention_value": 1,
                        "page_value": 3,
                        "readiness": 5,
                    },
                    score=13,
                ),
                *[candidate(rank) for rank in range(2, 11)],
            ]
        )

        self.assertEqual(validate_audit_record(setup_value_record), [])
        self.assertIn("candidate_score_out_of_range: rank 1 setup_value", validate_audit_record(missing_setup_value))

    def test_fewer_than_five_can_record_no_generation_needed(self) -> None:
        errors = validate_audit_record(valid_audit_record())

        self.assertEqual(errors, [])

    def test_page_local_audit_requires_core_fields(self) -> None:
        record = valid_audit_record()
        del record["rollback_path"]

        errors = validate_audit_record(record)

        self.assertIn("audit_missing_required_field: rollback_path", errors)

    def test_candidate_table_requires_fields_scores_and_fewer_than_ten_rationale(self) -> None:
        missing_rationale = valid_audit_record(candidate_table=[candidate(rank) for rank in range(1, 4)])
        bad_score = valid_audit_record(candidate_table=[candidate(1, score=99)])
        missing_field = valid_audit_record(candidate_table=[{"rank": 1}])

        self.assertIn("candidate_table_missing_fewer_than_ten_rationale", validate_audit_record(missing_rationale))
        self.assertIn("candidate_score_mismatch: rank 1", validate_audit_record(bad_score))
        self.assertIn("candidate_missing_required_field: rank 1 candidate_image", validate_audit_record(missing_field))

    def test_top_five_are_backlog_and_sixth_generation_requires_churn_rationale(self) -> None:
        automatic_top_five = valid_audit_record(
            candidate_table=[candidate(rank, disposition="automatic_generation") for rank in range(1, 6)]
        )
        generate_now_top_five = valid_audit_record(
            candidate_table=[candidate(rank, disposition="generate_now") for rank in range(1, 6)]
        )
        first_generation_top_five = valid_audit_record(
            candidate_table=[candidate(rank, disposition="first_generation_candidate") for rank in range(1, 6)]
        )
        sixth_without_rationale = valid_audit_record(
            candidate_table=[
                *[candidate(rank) for rank in range(1, 6)],
                candidate(6, disposition="generate_now"),
            ]
        )

        self.assertIn("top_five_candidate_must_not_be_automatic_generation: rank 1", validate_audit_record(automatic_top_five))
        self.assertIn("top_five_candidate_must_not_select_generation_directly: rank 1", validate_audit_record(generate_now_top_five))
        self.assertIn("top_five_candidate_must_not_select_generation_directly: rank 1", validate_audit_record(first_generation_top_five))
        self.assertIn("sixth_candidate_generation_missing_churn_rationale: rank 6", validate_audit_record(sixth_without_rationale))

    def test_named_top_five_target_accepts_rank_one_to_five_generation_only(self) -> None:
        generate_now = valid_top_five_audit_record()
        first_generation = valid_top_five_audit_record(
            candidate_table=[
                candidate(rank, disposition="first_generation_candidate" if rank <= 4 else "preserve_existing" if rank == 5 else "later_candidate")
                for rank in range(1, 11)
            ]
        )
        automatic_generation = valid_top_five_audit_record(
            candidate_table=[
                candidate(rank, disposition="automatic_generation" if rank == 1 else "generate_now" if rank <= 4 else "preserve_existing" if rank == 5 else "later_candidate")
                for rank in range(1, 11)
            ]
        )
        sixth = valid_top_five_audit_record(
            candidate_table=[
                *[
                    candidate(rank, disposition="generate_now" if rank <= 4 else "preserve_existing")
                    for rank in range(1, 6)
                ],
                candidate(6, disposition="generate_now"),
            ],
            generation_decision={
                "selected_count": 5,
                "decision": "generate_to_top_five_total",
                "rationale": "Fixture tries to add a sixth image candidate.",
                "selected_purposes": [
                    "exercise_setup_illustration",
                    "exercise_movement_illustration",
                    "exercise_movement_illustration",
                    "exercise_muscle_attention_illustration",
                    "exercise_movement_illustration",
                ],
            },
        )

        self.assertEqual(validate_audit_record(generate_now), [])
        self.assertEqual(validate_audit_record(first_generation), [])
        self.assertIn("top_five_candidate_must_not_be_automatic_generation: rank 1", validate_audit_record(automatic_generation))
        self.assertIn("sixth_candidate_generation_not_allowed: rank 6", validate_audit_record(sixth))

    def test_style_only_replacement_fails_but_concrete_replacement_reason_passes(self) -> None:
        style_only = valid_audit_record(
            existing_image_decisions=[
                {
                    "image_path": "media/exercises/fixture/sequence.png",
                    "decision": "replace",
                    "reason": "style_consistency",
                }
            ]
        )
        concrete_reason = valid_audit_record(
            existing_image_decisions=[
                {
                    "image_path": "media/exercises/fixture/sequence.png",
                    "decision": "replace",
                    "reason": next(iter(ACCEPTED_REPLACEMENT_REASONS)),
                }
            ]
        )

        self.assertIn("style_only_replacement_not_allowed: media/exercises/fixture/sequence.png", validate_audit_record(style_only))
        self.assertEqual(validate_audit_record(concrete_reason), [])

    def test_template_update_is_deferred_until_first_slice_proof(self) -> None:
        premature_update = valid_audit_record(template_update_status="updated")

        errors = validate_audit_record(premature_update)

        self.assertIn("template_update_requires_later_approval", errors)

    def test_image_count_exception_required_for_four_or_five_images(self) -> None:
        four_images_without_exception = valid_audit_record(
            current_image_count=3,
            generation_decision={
                "selected_count": 1,
                "decision": "generate_minimum_needed_subset",
                "rationale": "Fixture would end with four images.",
                "selected_purposes": ["exercise_setup_illustration"],
            },
        )
        four_images_with_exception = valid_audit_record(
            current_image_count=3,
            image_count_exception_approval="docs/plans/fixture.md#approved-fourth-image",
            generation_decision={
                "selected_count": 1,
                "decision": "generate_minimum_needed_subset",
                "rationale": "Fixture has approved page-specific exception.",
                "selected_purposes": ["exercise_setup_illustration"],
            },
        )

        self.assertIn("image_count_exception_required_for_four_or_five_images", validate_audit_record(four_images_without_exception))
        self.assertEqual(validate_audit_record(four_images_with_exception), [])

    def test_candidate_purposes_and_selected_muscle_attention_are_bounded(self) -> None:
        invalid_candidate_purpose = valid_audit_record(
            candidate_table=[candidate(1, purpose="pattern_alignment_illustration"), *[candidate(rank) for rank in range(2, 11)]]
        )
        second_muscle_attention = valid_audit_record(
            existing_image_purposes=["exercise_muscle_attention_illustration"],
            generation_decision={
                "selected_count": 1,
                "decision": "generate_minimum_needed_subset",
                "rationale": "Fixture would add a second muscle-attention image.",
                "selected_purposes": ["exercise_muscle_attention_illustration"],
            },
        )

        self.assertIn("candidate_purpose_not_accepted: rank 1", validate_audit_record(invalid_candidate_purpose))
        self.assertIn("second_muscle_attention_image_not_allowed", validate_audit_record(second_muscle_attention))

    def test_forbidden_image_adjacent_claims_fail_audit_validation(self) -> None:
        forbidden_candidate = valid_audit_record(
            candidate_table=[
                candidate(1, candidate_image="Treatment protocol correction image", why_it_matters="Promises a cure for pain."),
                *[candidate(rank) for rank in range(2, 11)],
            ]
        )

        errors = validate_audit_record(forbidden_candidate)

        self.assertIn("candidate_forbidden_claim: rank 1 treatment", errors)
        self.assertIn("candidate_forbidden_claim: rank 1 cure", errors)

    def test_first_slice_scope_is_one_page_or_deliberately_small_batch(self) -> None:
        one_page = validate_slice_scope(["exercises/bird-dog.md"])
        small_batch = validate_slice_scope(["exercises/bird-dog.md", "exercises/dead-bug.md"], rationale="paired sequence-image audit")
        broad_batch = validate_slice_scope(["exercises/bird-dog.md", "exercises/dead-bug.md", "exercises/glute-bridge.md"])

        self.assertEqual(one_page, [])
        self.assertEqual(small_batch, [])
        self.assertIn("first_slice_scope_too_broad_without_rationale", broad_batch)

    def test_closeout_proof_accepts_zero_generated_image_slice(self) -> None:
        errors = validate_closeout_proof(valid_closeout_proof())

        self.assertEqual(errors, [])

    def test_closeout_proof_requires_rollback_and_non_goal_evidence(self) -> None:
        missing_rollback_command = valid_closeout_proof(
            rollback_proof={
                "status": "passed",
                "paths_to_remove": [],
                "commands": [],
                "page_readable_without_new_images": True,
            }
        )
        leaked_non_goal = valid_closeout_proof(
            non_goal_smoke={
                "no_pr_review_rule": True,
                "no_hosted_app": True,
                "no_cms": True,
                "no_database": False,
                "no_api": True,
                "no_video_first_path": True,
                "no_personalized_coaching": True,
            }
        )

        self.assertIn("rollback_proof_missing_commands", validate_closeout_proof(missing_rollback_command))
        self.assertIn("non_goal_smoke_failed: no_database", validate_closeout_proof(leaked_non_goal))

    def test_closeout_proof_requires_visual_review_for_generated_images(self) -> None:
        generated_without_review = valid_closeout_proof(
            generated_image_count=1,
            generated_image_paths=["media/exercises/fixture/setup.png"],
            visual_safety_review={
                "status": "not_triggered_no_generated_images",
                "reviewed_items": [],
            },
        )

        errors = validate_closeout_proof(generated_without_review)

        self.assertIn("visual_safety_review_required_for_generated_images", errors)

    def test_top_five_closeout_proof_does_not_require_repository_visual_review(self) -> None:
        generated_without_review = valid_closeout_proof(
            initiative="top_five_generated_images_for_fewer_than_five_exercise_documents",
            exercise_documents=["exercises/bird-dog.md"],
            generated_image_count=1,
            generated_image_paths=["media/exercises/bird-dog/setup.png"],
            visual_safety_review={
                "status": "not_required_named_top_five_initiative",
                "reviewed_items": [],
            },
        )

        errors = validate_closeout_proof(generated_without_review)

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
