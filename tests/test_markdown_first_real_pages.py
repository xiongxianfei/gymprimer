from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_markdown_first.py"
FIRST_SLICE = (
    "01-getting-started/beginner-training-principles.md",
    "02-machines/lat-pulldown.md",
    "02-machines/seated-row.md",
    "02-machines/chest-press.md",
    "03-bodyweight/incline-push-up.md",
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
                "01-getting-started",
                "02-machines",
                "03-bodyweight",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_readme_links_draft_first_slice_pages(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("not yet promoted", readme)
        for relative_path in FIRST_SLICE:
            with self.subTest(path=relative_path):
                self.assertIn(f"]({relative_path})", readme)


if __name__ == "__main__":
    unittest.main()
