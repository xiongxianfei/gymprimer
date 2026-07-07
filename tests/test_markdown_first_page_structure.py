from pathlib import Path
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_markdown_first.py"
FIXTURES = ROOT / "tests/fixtures/markdown-first/pages"


def run_check(*paths: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECK), *map(str, paths)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def run_check_with_root(root: Path, *paths: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["GYMPRIMER_ROOT"] = str(root)
    return subprocess.run(
        [sys.executable, str(CHECK), *map(str, paths)],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


SAFER_RUNNING_REQUIRED_HEADINGS = (
    "## What this is for",
    "## What this page cannot promise",
    "## Before you start",
    "## Warm up",
    "## Running form basics",
    "## Muscles involved",
    "## What you should feel",
    "## How much to do",
    "## Common mistakes",
    "## Easier version",
    "## Harder version",
    "## Safety notes",
    "## Sources",
)


def write_safer_running_sources(root: Path, include_mchs: bool = True) -> None:
    lines = [
        "# Sources",
        "",
        "[nhs-couch-to-5k]: https://www.nhs.uk/better-health/get-active/get-running-with-couch-to-5k/couch-to-5k-running-plan/",
        "[mayo-exercise-chronic-disease]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-and-chronic-disease/art-20046049",
    ]
    if include_mchs:
        lines.append("[mchs-better-runner]: https://www.mayoclinichealthsystem.org/hometown-health/speaking-of-health/how-can-i-become-a-better-runner-and-avoid-injury")
    (root / "SOURCES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def safer_running_page_text(
    *,
    title: str = "# Safer Running Basics",
    alias_line: str = "Also searched as: injury-free running, beginner running, running without getting hurt",
    omit_heading: str | None = None,
    omit_mchs_definition: bool = False,
) -> str:
    sections = {
        "## What this is for": "Use this page to learn a simple beginner run/walk starting point. [NHS][nhs-couch-to-5k]",
        "## What this page cannot promise": "No page can guarantee injury-free running; this is general risk-reduction education. [Mayo Clinic Health System][mchs-better-runner]",
        "## Before you start": "Start on a clear route and stop if symptoms feel unusual. [Mayo Clinic][mayo-exercise-chronic-disease]",
        "## Warm up": "Begin with a few easy minutes before running. [Mayo Clinic Health System][mchs-better-runner]",
        "## Running form basics": "Run tall, keep the shoulders relaxed, and avoid forcing a specific foot strike. [Mayo Clinic Health System][mchs-better-runner]",
        "## Muscles involved": (
            "| Role | Muscle region | What it helps do |\n"
            "|---|---|---|\n"
            "| Support and push-off | Glutes, thighs, and calves | Help support each step and push the ground away. [Mayo Clinic Health System][mchs-better-runner] |\n"
            "| Landing control | Feet, ankles, calves, and thighs | Help absorb and control each landing. |\n"
            "| Posture and transfer | Trunk | Helps you stay tall while the legs move. |\n"
            "| Rhythm and balance | Shoulders, upper back, and arms | Help arm swing stay relaxed and coordinated. |"
        ),
        "## What you should feel": "You should feel warm and slightly out of breath, not panicked. Stop for chest pain, dizziness, unusual shortness of breath, sharp pain, or worsening symptoms. [Mayo Clinic][mayo-exercise-chronic-disease]",
        "## How much to do": (
            "Method type: basic_cardio_activity\n\n"
            "Beginner starting point: Try 10-20 minutes total with short easy running intervals and walking breaks.\n"
            "Effort: Keep the running portions easy enough that you could speak in short sentences.\n"
            "Progression: First make running feel smoother, then add a little total time.\n"
            "Stop if: Stop for chest pain, dizziness, unusual shortness of breath, sharp pain, or worsening symptoms. [Mayo Clinic][mayo-exercise-chronic-disease]"
        ),
        "## Common mistakes": (
            "| Mistake | Safer framing |\n"
            "|---|---|\n"
            "| Running too far too soon | Use run/walk intervals and increase gradually. [NHS][nhs-couch-to-5k] |\n"
            "| Ignoring sharp or worsening symptoms | Stop and use the safety guidance. [Mayo Clinic][mayo-exercise-chronic-disease] |"
        ),
        "## Easier version": "Use shorter total time, more walking, flatter routes, and fewer running days.",
        "## Harder version": "First add a little total time or a little more easy running inside the same session.",
        "## Safety notes": "Use the central [red flags](../RED-FLAGS.md) page for symptoms such as chest pain, dizziness, fainting, severe shortness of breath, numbness, weakness, sharp pain, or worsening symptoms. [Mayo Clinic][mayo-exercise-chronic-disease]",
        "## Sources": (
            "- [NHS Couch to 5K][nhs-couch-to-5k]\n"
            "- [Mayo Clinic Health System running guidance][mchs-better-runner]\n"
            "- [Mayo Clinic exercise and chronic disease guidance][mayo-exercise-chronic-disease]\n\n"
            "[nhs-couch-to-5k]: https://www.nhs.uk/better-health/get-active/get-running-with-couch-to-5k/couch-to-5k-running-plan/\n"
            + ("" if omit_mchs_definition else "[mchs-better-runner]: https://www.mayoclinichealthsystem.org/hometown-health/speaking-of-health/how-can-i-become-a-better-runner-and-avoid-injury\n")
            + "[mayo-exercise-chronic-disease]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-and-chronic-disease/art-20046049"
        ),
    }
    body = [
        title,
        "",
        "Author: Fixture Maintainer",
        "Created: 2026-07-06",
        "Last reviewed: 2026-07-06",
        "Next review due: 2027-07-06",
        "Review scope: safer running fixture contract",
        "",
        alias_line,
        "",
    ]
    for heading in SAFER_RUNNING_REQUIRED_HEADINGS:
        if heading == omit_heading:
            continue
        body.extend([heading, "", sections[heading], ""])
    return "\n".join(body)


def write_safer_running_fixture_page(root: Path, text: str) -> Path:
    (root / "exercises").mkdir(exist_ok=True)
    (root / "RED-FLAGS.md").write_text(
        "# Red Flags\n\n> Disclaimer: GymPrimer is educational content. It is not medical advice and not personalized coaching.\n",
        encoding="utf-8",
    )
    page = root / "exercises/safer-running-basics.md"
    page.write_text(text, encoding="utf-8")
    return page


class MarkdownFirstPageStructureTest(unittest.TestCase):
    def test_valid_page_structure_passes(self) -> None:
        result = run_check(FIXTURES / "valid-exercise.md")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_page_local_disclaimer_is_not_required(self) -> None:
        path = FIXTURES / "missing-disclaimer.md"
        result = run_check(path)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_low_page_local_disclaimer_is_not_a_structure_error(self) -> None:
        result = run_check(FIXTURES / "disclaimer-too-low.md")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_red_flags_central_disclaimer_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SOURCES.md").write_text(
                "# Sources\n\n[mayo-weight-training]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842\n",
                encoding="utf-8",
            )
            red_flags = root / "RED-FLAGS.md"
            red_flags.write_text(
                textwrap.dedent(
                    """\
                    # Red Flags

                    ## Sources

                    - [Mayo Clinic - Weight training][mayo-weight-training]

                    [mayo-weight-training]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842
                    """
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(CHECK), str(red_flags)],
                cwd=ROOT,
                env={"GYMPRIMER_ROOT": str(root)},
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF001", result.stdout)
        self.assertIn(str(red_flags), result.stdout)

    def test_missing_sources_fails(self) -> None:
        result = run_check(FIXTURES / "missing-sources.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF002", result.stdout)

    def test_safer_running_fixture_contract_passes_with_registered_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_safer_running_sources(root)
            page = write_safer_running_fixture_page(root, safer_running_page_text())

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_safer_running_fixture_rejects_injury_free_title_and_missing_alias(self) -> None:
        cases = (
            (safer_running_page_text(title="# Injury-Free Running"), "safer_running_title_invalid"),
            (safer_running_page_text(alias_line="Also searched as: beginner running"), "safer_running_alias_missing"),
        )
        for page_text, expected_code in cases:
            with self.subTest(expected_code=expected_code), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_safer_running_sources(root)
                page = write_safer_running_fixture_page(root, page_text)

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn(expected_code, result.stdout)

    def test_safer_running_fixture_requires_headings_page_sources_and_source_registration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_safer_running_sources(root)
            page = write_safer_running_fixture_page(root, safer_running_page_text(omit_heading="## Warm up"))

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("safer_running_missing_section", result.stdout)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_safer_running_sources(root)
            page = write_safer_running_fixture_page(root, safer_running_page_text(omit_mchs_definition=True))

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("citation_missing_page_reference_definition", result.stdout)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_safer_running_sources(root, include_mchs=False)
            page = write_safer_running_fixture_page(root, safer_running_page_text())

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("source_id_missing_from_sources_md", result.stdout)


if __name__ == "__main__":
    unittest.main()
