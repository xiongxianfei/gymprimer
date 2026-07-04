from pathlib import Path
import textwrap
import unittest

from tools.checks.check_markdown_first import validate_exercise_method_guidance


ROOT = Path(__file__).resolve().parents[1]
PROOF_SLICE_METHOD_TYPES = {
    "exercises/chest-press.md": "dynamic_resistance",
    "exercises/incline-push-up.md": "bodyweight_progression",
    "exercises/chin-nod.md": "low_load_control_drill",
    "exercises/plank.md": "isometric_hold",
    "exercises/thoracic-extension.md": "mobility_drill",
    "exercises/kneeling-hip-flexor-stretch.md": "stretch_hold",
}


def method_page(method_section: str) -> str:
    section = textwrap.dedent(method_section).strip()
    return (
        "# Fixture Exercise\n\n"
        "## What this exercise is for\n\n"
        "General exercise education.\n\n"
        f"{section}\n\n"
        "## Sources\n\n"
        "- [Fixture source][local-fixture-exercise-source]\n\n"
        "[local-fixture-exercise-source]: https://example.org/source\n"
    )


def finding_codes(text: str, relative_path: str = "exercises/fixture-exercise.md") -> list[str]:
    path = ROOT / relative_path
    return [finding.code for finding in validate_exercise_method_guidance(path, text)]


class ExerciseMethodGuidanceTest(unittest.TestCase):
    def test_valid_visible_method_section_passes(self) -> None:
        text = method_page(
            """\
            ## How much to do

            Method type: dynamic_resistance

            Beginner starting point: Try 1-3 easy sets of 8-15 controlled repetitions.
            Effort: Keep several repetitions in reserve.
            Rest: Rest about 60-120 seconds.
            Progression: Add repetitions first, then a small load increase.
            Stop if: Stop when controlled form breaks.
            """
        )

        self.assertEqual(finding_codes(text), [])

    def test_unselected_page_without_method_section_remains_valid_for_method_contract(self) -> None:
        text = method_page("")

        self.assertEqual(finding_codes(text), [])

    def test_method_section_requires_visible_type_and_labels(self) -> None:
        text = method_page(
            """\
            ## How much to do

            Beginner starting point: Try a small amount.
            Effort: Keep it easy.
            """
        )

        codes = finding_codes(text)
        self.assertIn("exercise_method_missing_type", codes)
        self.assertIn("exercise_method_missing_label", codes)

    def test_method_section_heading_must_be_exact(self) -> None:
        text = method_page(
            """\
            ## How much to do wrong

            Method type: dynamic_resistance

            Beginner starting point: Try a small amount.
            Effort: Keep it easy.
            Rest: Rest as needed.
            Progression: Add repetitions first.
            Stop if: Stop when form breaks.
            """
        )

        self.assertIn("exercise_method_missing_section", finding_codes(text))

    def test_required_method_labels_must_have_content(self) -> None:
        text = method_page(
            """\
            ## How much to do

            Method type: dynamic_resistance

            Beginner starting point:
            Effort:
            Rest:
            Progression:
            Stop if:
            """
        )

        codes = finding_codes(text)
        self.assertIn("exercise_method_empty_label", codes)

    def test_unknown_and_deferred_method_types_fail(self) -> None:
        for method_type in ("loaded_carry", "unknown_type"):
            with self.subTest(method_type=method_type):
                text = method_page(
                    f"""\
                    ## How much to do

                    Method type: {method_type}

                    Beginner starting point: Use a simple starting point.
                    Effort: Keep it easy.
                    Rest: Rest as needed.
                    Progression: Progress gradually.
                    Stop if: Stop when form breaks.
                    """
                )

                self.assertIn("exercise_method_inactive_type", finding_codes(text))

    def test_basic_cardio_equipment_passes_only_for_rowing_machine_scope(self) -> None:
        text = method_page(
            """\
            ## How much to do

            Method type: basic_cardio_equipment

            Beginner starting point: Start with 3-5 minutes of easy rowing.
            Effort: Keep the effort easy or moderate.
            Rest/reset: Take a break to walk, breathe, or reset technique.
            Progression: Make the stroke smoother, then add time.
            Stop condition: Stop when technique gets painful, jerky, or uncontrolled.
            """
        )

        self.assertEqual(finding_codes(text, "exercises/rowing-machine.md"), [])
        self.assertIn("exercise_method_inactive_type", finding_codes(text, "exercises/fixture-exercise.md"))

    def test_basic_cardio_equipment_still_requires_visible_labels(self) -> None:
        text = method_page(
            """\
            ## How much to do

            Method type: basic_cardio_equipment

            Beginner starting point: Start with 3-5 minutes of easy rowing.
            Effort: Keep the effort easy or moderate.
            Progression: Make the stroke smoother, then add time.
            """
        )

        self.assertIn("exercise_method_missing_label", finding_codes(text, "exercises/rowing-machine.md"))

    def test_hidden_only_method_metadata_fails_but_visible_markdown_remains_authoritative(self) -> None:
        hidden_only = textwrap.dedent(
            """\
            ---
            method_type: isometric_hold
            ---

            # Fixture Exercise

            ## Sources

            [local-fixture-exercise-source]: https://example.org/source
            """
        )
        visible_with_conflict = textwrap.dedent(
            """\
            ---
            method_type: isometric_hold
            ---

            # Fixture Exercise

            ## How much to do

            Method type: dynamic_resistance

            Beginner starting point: Try 1-3 easy sets.
            Effort: Keep it easy.
            Rest: Rest as needed.
            Progression: Add repetitions first.
            Stop if: Stop when form breaks.

            ## Sources

            [local-fixture-exercise-source]: https://example.org/source
            """
        )

        self.assertIn("exercise_method_hidden_only_metadata", finding_codes(hidden_only))
        self.assertNotIn("exercise_method_hidden_only_metadata", finding_codes(visible_with_conflict))
        self.assertNotIn("exercise_method_inactive_type", finding_codes(visible_with_conflict))

    def test_adaptive_programming_and_treatment_language_fail(self) -> None:
        adaptive = method_page(
            """\
            ## How much to do

            Method type: bodyweight_progression

            Beginner starting point: If your shoulder hurts, switch to a different exercise for two weeks.
            Effort: Keep it easy.
            Rest: Rest as needed.
            Progression: Increase reps based on your training response.
            Stop if: Stop when form breaks.
            """
        )
        treatment = method_page(
            """\
            ## How much to do

            Method type: low_load_control_drill

            Beginner starting point: Use this as a rehab progression to fix posture correction.
            Effort: Keep it easy.
            Rest: Rest as needed.
            Progression: Progress gradually.
            Stop if: Stop when form breaks.
            """
        )

        self.assertIn("exercise_method_adaptive_programming", finding_codes(adaptive))
        self.assertIn("exercise_method_forbidden_scope", finding_codes(treatment))

    def test_related_specs_point_to_focused_method_spec_without_copying_enum(self) -> None:
        markdown_first = (ROOT / "specs/markdown-first-primer.md").read_text(encoding="utf-8")
        responsible_breadth = (ROOT / "specs/responsible-breadth.md").read_text(encoding="utf-8")

        for text in (markdown_first, responsible_breadth):
            self.assertIn("specs/exercise-method-guidance.md", text)
            self.assertIn("Method type:", text)
            self.assertNotIn("dynamic_resistance`, `bodyweight_progression`, `low_load_control_drill`", text)

    def test_six_proof_slice_pages_have_method_sections_and_mappings(self) -> None:
        for relative_path, method_type in PROOF_SLICE_METHOD_TYPES.items():
            with self.subTest(path=relative_path):
                path = ROOT / relative_path
                text = path.read_text(encoding="utf-8")

                self.assertIn("## How much to do", text)
                self.assertIn(f"Method type: {method_type}", text)
                self.assertIn("../principles/sets-reps-holds-rest-and-progression.md", text)
                self.assertEqual(
                    [finding.code for finding in validate_exercise_method_guidance(path, text)],
                    [],
                )

    def test_pattern_previews_align_with_method_guidance_ranges(self) -> None:
        forward_head = (ROOT / "patterns/forward-head-posture.md").read_text(encoding="utf-8")
        anterior_pelvic_tilt = (ROOT / "patterns/anterior-pelvic-tilt.md").read_text(encoding="utf-8")

        for expected in (
            "*Starter range:* 1-3 sets of 6-10 slow reps; rest about 30 seconds.",
            "*Starter range:* 1-2 sets of 6-10 slow reps; rest 30-60 seconds.",
        ):
            self.assertIn(expected, forward_head)

        for expected in (
            "*Starter range:* 2-3 holds of 10-30 seconds; rest 45-60 seconds.",
            "*Starter range:* 1-2 holds of about 20-30 seconds per side; breathe normally between sides.",
        ):
            self.assertIn(expected, anterior_pelvic_tilt)


if __name__ == "__main__":
    unittest.main()
