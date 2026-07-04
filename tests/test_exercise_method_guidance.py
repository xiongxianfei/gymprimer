from pathlib import Path
import textwrap
import unittest

from tools.checks.check_markdown_first import validate_exercise_method_guidance


ROOT = Path(__file__).resolve().parents[1]


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


def finding_codes(text: str) -> list[str]:
    path = ROOT / "exercises/fixture-exercise.md"
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

    def test_unknown_and_deferred_method_types_fail(self) -> None:
        for method_type in ("loaded_carry", "basic_cardio_equipment", "unknown_type"):
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


if __name__ == "__main__":
    unittest.main()
