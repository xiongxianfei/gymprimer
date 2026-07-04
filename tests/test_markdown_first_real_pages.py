from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_markdown_first.py"
FIRST_SLICE = (
    "principles/beginner-training-principles.md",
    "exercises/lat-pulldown.md",
    "exercises/seated-row.md",
    "exercises/chest-press.md",
    "exercises/incline-push-up.md",
)
ROWING_MACHINE_PAGE = ROOT / "exercises/rowing-machine.md"
ROWING_REQUIRED_SECTIONS = (
    "## What this is for",
    "## Before you start",
    "## Equipment setup",
    "## Muscles involved",
    "## Movement breakdown",
    "## What you should feel",
    "## Common mistakes",
    "## How much to do",
    "## Easier version",
    "## Harder version",
    "## Safety notes",
    "## Sources",
)


class MarkdownFirstRealPagesTest(unittest.TestCase):
    def test_first_slice_pages_exist(self) -> None:
        for relative_path in FIRST_SLICE:
            with self.subTest(path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file())

    def test_first_slice_pages_pass_checker(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(CHECK),
                "README.md",
                "SOURCES.md",
                "RED-FLAGS.md",
                "principles",
                "exercises",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_readme_links_first_slice_pages(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for relative_path in FIRST_SLICE:
            with self.subTest(path=relative_path):
                self.assertIn(f"]({relative_path})", readme)

    def rowing_text(self) -> str:
        return ROWING_MACHINE_PAGE.read_text(encoding="utf-8")

    def test_rowing_machine_page_has_required_shape(self) -> None:
        self.assertTrue(ROWING_MACHINE_PAGE.is_file())
        text = self.rowing_text()

        for section in ROWING_REQUIRED_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, text)

        forbidden_runtime_terms = (
            "JavaScript",
            "database",
            "user account",
            "tracking flow",
            "local server",
            "workout tracker",
            "calculator",
            "user input",
        )
        for term in forbidden_runtime_terms:
            with self.subTest(term=term):
                self.assertNotIn(term, text)

    def test_rowing_machine_stroke_sequence_setup_and_method(self) -> None:
        text = self.rowing_text().lower()
        compact = " ".join(text.split())

        for term in ("catch", "drive", "finish", "recovery"):
            with self.subTest(term=term):
                self.assertIn(term, text)

        self.assertIn("drive: legs -> body -> arms", text)
        self.assertIn("recovery: arms -> body -> legs", text)
        self.assertIn("foot strap", text)
        self.assertIn("ball or widest part", text)
        self.assertIn("shins approach vertical only as far as comfortable", compact)
        self.assertIn("damper changes the feel", text)
        self.assertIn("you create the work with your stroke effort", compact)
        self.assertIn("method type: basic_cardio_equipment", text)
        self.assertIn("beginner starting point:", text)
        self.assertIn("effort:", text)
        self.assertIn("rest/reset:", text)
        self.assertIn("progression:", text)
        self.assertIn("stop condition:", text)
        self.assertIn("3-5 minutes", text)
        self.assertIn("technique first, then time, then moderate effort", text)

    def test_rowing_machine_safety_sources_and_forbidden_scope(self) -> None:
        text = self.rowing_text()
        lower = text.lower()

        self.assertIn("../RED-FLAGS.md", text)
        for term in (
            "chest pain",
            "dizziness",
            "fainting",
            "unusual shortness of breath",
            "sharp pain",
            "numbness",
            "symptoms that worsen",
            "painful",
            "jerky or uncontrolled",
        ):
            with self.subTest(term=term):
                self.assertIn(term, lower)

        for term in (
            "all-out",
            "maximal damper",
            "2k test",
            "multi-week",
            "weight-loss",
            "heart-rate zone",
            "personalized conditioning plan",
            "diagnosis",
            "rehabilitation",
            "return-to-training",
        ):
            with self.subTest(term=term):
                self.assertNotIn(term, lower)

        for source_id in (
            "concept2-rowing-technique",
            "concept2-foot-position",
            "concept2-damper-setting",
            "concept2-getting-started-workouts",
            "cdc-adult-activity",
            "who-physical-activity",
            "local-rowing-machine-safety",
            "local-rowing-machine-exercise-pain",
            "nhs-back-pain",
            "mayo-weight-training",
        ):
            with self.subTest(source_id=source_id):
                self.assertIn(f"[{source_id}]:", text)
                self.assertIn(f"][{source_id}]", text)


if __name__ == "__main__":
    unittest.main()
