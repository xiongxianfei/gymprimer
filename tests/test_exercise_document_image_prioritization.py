from pathlib import Path
import tempfile
import unittest

from tools.checks.exercise_document_image_prioritization import (
    ACCEPTED_REPLACEMENT_REASONS,
    evaluation_population,
    image_count_by_exercise,
    validate_audit_record,
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
            "safety_setup_value": 4,
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


class ExerciseDocumentImagePrioritizationTest(unittest.TestCase):
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
        sixth_without_rationale = valid_audit_record(
            candidate_table=[
                *[candidate(rank) for rank in range(1, 6)],
                candidate(6, disposition="generate_now"),
            ]
        )

        self.assertIn("top_five_candidate_must_not_be_automatic_generation: rank 1", validate_audit_record(automatic_top_five))
        self.assertIn("sixth_candidate_generation_missing_churn_rationale: rank 6", validate_audit_record(sixth_without_rationale))

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


if __name__ == "__main__":
    unittest.main()
