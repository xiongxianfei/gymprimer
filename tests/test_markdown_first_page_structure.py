from pathlib import Path
import subprocess
import sys
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


class MarkdownFirstPageStructureTest(unittest.TestCase):
    def test_valid_page_structure_passes(self) -> None:
        result = run_check(FIXTURES / "valid-exercise.md")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_disclaimer_fails_with_rule_and_path(self) -> None:
        path = FIXTURES / "missing-disclaimer.md"
        result = run_check(path)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF001", result.stdout)
        self.assertIn(str(path), result.stdout)

    def test_disclaimer_too_low_fails(self) -> None:
        result = run_check(FIXTURES / "disclaimer-too-low.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF001", result.stdout)

    def test_missing_sources_fails(self) -> None:
        result = run_check(FIXTURES / "missing-sources.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF002", result.stdout)


if __name__ == "__main__":
    unittest.main()
