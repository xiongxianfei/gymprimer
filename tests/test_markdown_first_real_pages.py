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


if __name__ == "__main__":
    unittest.main()
