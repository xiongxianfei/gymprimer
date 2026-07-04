from pathlib import Path
import textwrap
import unittest

from tools.checks.check_markdown_first import validate_exercise_muscle_guidance


ROOT = Path(__file__).resolve().parents[1]
MANUAL_PROOF_ROOT = ROOT / "docs/changes/exercise-muscle-guidance-standard/manual-proof"
VALIDATION_LEDGER = ROOT / "docs/changes/exercise-muscle-guidance-standard/validation-ledger.md"
PROOF_SLICE_PAGES = (
    "exercises/rowing-machine.md",
    "exercises/chest-press.md",
    "exercises/plank.md",
    "exercises/chin-nod.md",
    "exercises/thoracic-extension.md",
    "exercises/band-pull-apart.md",
)
REMAINING_ROLLOUT_PAGES = (
    "exercises/bird-dog.md",
    "exercises/dead-bug.md",
    "exercises/glute-bridge.md",
    "exercises/hip-hinge.md",
    "exercises/incline-push-up.md",
    "exercises/kneeling-hip-flexor-stretch.md",
    "exercises/lat-pulldown.md",
    "exercises/prone-y-t.md",
    "exercises/seated-row.md",
    "exercises/wall-slide.md",
)
PROOF_SLICE_MUSCLE_IMAGES = (
    "media/exercises/rowing-machine/muscle-attention.png",
    "media/exercises/chin-nod/muscle-attention.png",
    "media/exercises/thoracic-extension/muscle-attention.png",
    "media/exercises/band-pull-apart/muscle-attention.png",
)


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
            | Main driver | Chest | Helps press the handles forward. [Source][local-fixture-exercise-source] |
            | Support | Triceps | Help finish the press. |

            ## What you should feel

            You may feel the chest working while the arms help finish.
            """
        )
        role_bullets = exercise_page(
            """\
            ## Muscles involved

            - **Main driver:** upper back and lats help create the pull. [Source][local-fixture-exercise-source]
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
            | Drive | Legs and glutes | Push the machine away. [Source][local-fixture-exercise-source] |
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

    def test_source_sensitive_role_guidance_requires_page_local_source_surface(self) -> None:
        missing_citation = exercise_page(
            """\
            ## Muscles involved

            - **Main driver:** chest helps press the handles forward.
            - **Support:** triceps help finish the press.

            ## What you should feel

            You may feel the chest working while the arms help finish.
            """
        )
        global_only_reference = (
            "# Fixture Exercise\n\n"
            "## Muscles involved\n\n"
            "- **Main driver:** lower trapezius helps guide the shoulder blade. [Source][fixture-global]\n\n"
            "## What you should feel\n\n"
            "You may feel light upper-back work.\n\n"
            "## Sources\n\n"
            "- [Fixture source][local-fixture-exercise-source]\n\n"
            "[local-fixture-exercise-source]: https://example.org/source\n"
        )
        locally_defined_reference = exercise_page(
            """\
            ## Muscles involved

            - **Main driver:** lower trapezius helps guide the shoulder blade. [Source][local-fixture-exercise-source]

            ## What you should feel

            You may feel light upper-back work.
            """
        )

        self.assertIn("exercise_muscle_source_missing", finding_codes(missing_citation))
        self.assertIn("exercise_muscle_source_missing_definition", finding_codes(global_only_reference))
        self.assertEqual(finding_codes(locally_defined_reference), [])

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

    def test_m3_manual_source_audit_records_required_claim_samples(self) -> None:
        path = MANUAL_PROOF_ROOT / "source-audit.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")

        for heading in (
            "# Source Audit",
            "## Scope",
            "## Claim Samples",
            "## Disposition",
            "## Residual Risk",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

        for claim_type in ("main-driver", "support-stabilizer", "feel-cue", "compensation-cue", "safety-cue"):
            with self.subTest(claim_type=claim_type):
                self.assertIn(claim_type, text)

        for token in ("page_path", "claim_type", "supporting_source", "disposition", "residual_risk"):
            with self.subTest(token=token):
                self.assertIn(token, text)

    def test_m3_beginner_comprehension_proof_records_required_prompts(self) -> None:
        path = MANUAL_PROOF_ROOT / "beginner-comprehension.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")

        for page in PROOF_SLICE_PAGES:
            with self.subTest(page=page):
                self.assertIn(page, text)

        for prompt in (
            "muscle region to notice",
            "what it helps do",
            "what they may feel",
            "what not to overuse",
            "when to stop",
            "source they would click",
            "non-identifying",
            "residual confusion",
        ):
            with self.subTest(prompt=prompt):
                self.assertIn(prompt, text)

    def test_m3_muscle_image_alignment_records_each_proof_slice_image(self) -> None:
        path = MANUAL_PROOF_ROOT / "muscle-image-alignment.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")

        for image_path in PROOF_SLICE_MUSCLE_IMAGES:
            with self.subTest(image_path=image_path):
                self.assertIn(image_path, text)

        for requirement in (
            "nearby Markdown",
            "alt text",
            "provenance",
            "broad region",
            "no in-image labels",
            "no red pain marks",
            "no wrong/correct framing",
            "no precise anatomy",
            "no diagnosis or treatment",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, text)

    def test_m3_broad_rollout_gate_classifies_remaining_exercise_pages(self) -> None:
        path = MANUAL_PROOF_ROOT / "broad-rollout-gate.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")

        for page in REMAINING_ROLLOUT_PAGES:
            with self.subTest(page=page):
                self.assertIn(page, text)

        for category in (
            "keep as-is for now",
            "rename only",
            "rewrite role guidance",
            "revise `## What you should feel`",
            "source-audit needed",
            "future image candidate",
        ):
            with self.subTest(category=category):
                self.assertIn(category, text)

    def test_m3_validation_ledger_records_required_commands(self) -> None:
        self.assertTrue(VALIDATION_LEDGER.is_file())
        text = VALIDATION_LEDGER.read_text(encoding="utf-8")

        for command in (
            "python3 tools/checks/check_privacy.py docs/changes/exercise-muscle-guidance-standard",
            "python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md",
            "python3 -m unittest tests.test_exercise_muscle_guidance",
            "git diff --check",
        ):
            with self.subTest(command=command):
                self.assertIn(command, text)


if __name__ == "__main__":
    unittest.main()
