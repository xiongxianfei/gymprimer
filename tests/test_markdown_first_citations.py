from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_markdown_first.py"
FIXTURES = ROOT / "tests/fixtures/markdown-first/citations"
VALID = ROOT / "tests/fixtures/markdown-first/pages/valid-exercise.md"


def run_check(*paths: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECK), *map(str, paths)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class MarkdownFirstCitationTest(unittest.TestCase):
    def test_claim_level_safety_citation_passes(self) -> None:
        result = run_check(VALID)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_global_source_id_present_in_sources_md_passes(self) -> None:
        result = run_check(FIXTURES / "valid-global-source-id.md")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_global_source_id_missing_from_sources_md_is_rejected(self) -> None:
        result = run_check(FIXTURES / "missing-global-source-id.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("source_id_missing_from_sources_md", result.stdout)
        self.assertIn("unknown-source", result.stdout)

    def test_page_local_source_id_is_allowed_without_sources_md_entry(self) -> None:
        result = run_check(FIXTURES / "lat-pulldown.md")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_page_local_source_id_reused_across_pages_is_rejected(self) -> None:
        result = run_check(
            FIXTURES / "reused-local-a/shared.md",
            FIXTURES / "reused-local-b/shared.md",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("local_source_id_reused_across_pages", result.stdout)

    def test_reused_source_id_missing_from_sources_md_is_rejected(self) -> None:
        result = run_check(
            FIXTURES / "reused-missing-global-a.md",
            FIXTURES / "reused-missing-global-b.md",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("reused_source_id_missing_from_sources_md", result.stdout)

    def test_page_source_url_must_match_sources_index(self) -> None:
        result = run_check(FIXTURES / "source-url-mismatch.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("source_url_mismatch_sources_md", result.stdout)

    def test_uncited_stop_rule_fails(self) -> None:
        result = run_check(FIXTURES / "uncited-stop-rule.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF003", result.stdout)

    def test_global_only_safety_source_fails(self) -> None:
        result = run_check(FIXTURES / "global-only-safety.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF004", result.stdout)

    def test_placeholder_source_url_fails(self) -> None:
        result = run_check(FIXTURES / "broken-placeholder-source.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF005", result.stdout)


if __name__ == "__main__":
    unittest.main()
