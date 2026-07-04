from pathlib import Path
import textwrap
import unittest

from tools.checks.check_markdown_first import validate_exercise_muscle_guidance


ROOT = Path(__file__).resolve().parents[1]


def exercise_page(*sections: str) -> str:
    return (
        "# Fixture Exercise\n\n"
        "General beginner exercise education.\n\n"
        + "\n\n".join(textwrap.dedent(section).strip() for section in sections if section.strip())
        + "\n\n## Sources\n\n"
        "- [Fixture source][local-fixture-exercise-source]\n\n"
        "[local-fixture-exercise-source]: https://example.org/source\n"
    )


def finding_codes(text: str, relative_path: str = "exercises/fixture-exercise.md") -> list[str]:
    path = ROOT / relative_path
    return [finding.code for finding in validate_exercise_muscle_guidance(path, text)]


class ExerciseMuscleGuidanceTest(unittest.TestCase):
    def test_adopted_page_requires_muscles_involved_and_feel_section(self) -> None:
        missing_muscles = exercise_page(
            """\
            ## What you should feel

            You may feel a controlled push across the front of the body.
            """
        )
        missing_feel = exercise_page(
            """\
            ## Muscles involved

            - **Main driver:** chest helps press the handles forward.
            """
        )

        self.assertIn("exercise_muscle_missing_section", finding_codes(missing_muscles))
        self.assertIn("exercise_muscle_missing_feel_section", finding_codes(missing_feel))

    def test_migrated_page_cannot_keep_used_muscles_heading(self) -> None:
        text = exercise_page(
            """\
            ## Used muscles

            Primary: chest and triceps.

            ## What you should feel

            You may feel a smooth press across the front of the body.
            """
        )

        self.assertIn("exercise_muscle_legacy_heading_migrated", finding_codes(text))

    def test_untouched_legacy_used_muscles_page_remains_compatible(self) -> None:
        text = exercise_page(
            """\
            ## Used muscles

            Primary: rectus abdominis, obliques, and transverse abdominis.
            """
        )

        self.assertEqual(finding_codes(text, "exercises/dead-bug.md"), [])

    def test_role_table_and_bullets_pass_but_bare_list_fails(self) -> None:
        role_table = exercise_page(
            """\
            ## Muscles involved

            | Role | Muscle region | What it helps do |
            |---|---|---|
            | Main driver | Chest | Helps press the handles forward. |
            | Support | Triceps | Help finish the press. |

            ## What you should feel

            You may feel the chest working while the arms help finish.
            """
        )
        role_bullets = exercise_page(
            """\
            ## Muscles involved

            - **Main driver:** upper back and lats help create the pull.
            - **Support:** arms help finish the movement.

            ## What you should feel

            Pay attention to a smooth pull without the arms taking over.
            """
        )
        bare_list = exercise_page(
            """\
            ## Muscles involved

            Muscles: back, arms, core.

            ## What you should feel

            You may feel the exercise in the back and arms.
            """
        )

        self.assertEqual(finding_codes(role_table), [])
        self.assertEqual(finding_codes(role_bullets), [])
        self.assertIn("exercise_muscle_role_guidance_missing", finding_codes(bare_list))

    def test_phase_table_requires_phase_region_and_action_columns(self) -> None:
        valid_phase_table = exercise_page(
            """\
            ## Muscles involved

            | Phase | Muscle region | What it helps do |
            |---|---|---|
            | Drive | Legs and glutes | Push the machine away. |
            | Finish | Upper back and arms | Complete the pull. |

            ## What you should feel

            You may feel a leg-driven push and a light upper-back finish.
            """
        )
        invalid_phase_table = exercise_page(
            """\
            ## Muscles involved

            | Phase | Muscles |
            |---|---|
            | Drive | Legs and glutes |

            ## What you should feel

            You may feel a leg-driven push.
            """
        )

        self.assertEqual(finding_codes(valid_phase_table), [])
        self.assertIn("exercise_muscle_table_columns", finding_codes(invalid_phase_table))

    def test_forbidden_muscle_and_feel_wording_fails(self) -> None:
        cases = {
            "exercise_muscle_exact_activation": "This exercise activates your lower trapezius by 42 percent.",
            "exercise_muscle_emg_instruction": "EMG proves this is how beginners should activate the rotator cuff.",
            "exercise_muscle_must_feel": "You must feel your glutes or you are doing it wrong.",
            "exercise_muscle_forbidden_scope": "This fixes your weak muscle and treats posture correction.",
        }
        for expected_code, sentence in cases.items():
            with self.subTest(expected_code=expected_code):
                text = exercise_page(
                    f"""\
                    ## Muscles involved

                    - **Main driver:** chest helps press the handles forward.

                    ## What you should feel

                    {sentence}
                    """
                )

                self.assertIn(expected_code, finding_codes(text))

    def test_validation_findings_include_file_paths_and_stable_categories(self) -> None:
        text = exercise_page(
            """\
            ## What you should feel

            You must feel your glutes or you are doing it wrong.
            """
        )
        path = ROOT / "exercises/fixture-exercise.md"
        findings = validate_exercise_muscle_guidance(path, text)

        self.assertTrue(findings)
        for finding in findings:
            self.assertEqual(finding.path, path)
            self.assertRegex(finding.code, r"^exercise_muscle_")


if __name__ == "__main__":
    unittest.main()
