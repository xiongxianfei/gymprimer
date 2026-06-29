from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_privacy.py"
FIXTURES = ROOT / "tests/fixtures/markdown-first/privacy"


def run_check(*paths: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECK), "--", *map(str, paths)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class MarkdownFirstPrivacyTest(unittest.TestCase):
    def test_clean_fixture_exits_zero(self) -> None:
        result = run_check(FIXTURES / "clean.md")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_forbidden_fixture_exits_nonzero(self) -> None:
        result = run_check(FIXTURES / "forbidden.md")
        self.assertEqual(result.returncode, 1)
        self.assertIn("PF001", result.stdout)
        self.assertIn("forbidden", result.stdout.lower())

    def test_missing_target_is_setup_error(self) -> None:
        result = run_check(FIXTURES / "missing.md")
        self.assertEqual(result.returncode, 2)
        self.assertIn("setup", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
