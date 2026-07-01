from pathlib import Path
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


if __name__ == "__main__":
    unittest.main()
