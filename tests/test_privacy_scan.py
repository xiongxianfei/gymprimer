import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PRIVACY_SCAN = REPO_ROOT / "tools" / "validation" / "privacy_scan.py"


class PrivacyScanTests(unittest.TestCase):
    def run_scan(self, pattern, target, report):
        return subprocess.run(
            [
                sys.executable,
                str(PRIVACY_SCAN),
                "--pattern",
                pattern,
                "--report",
                str(report),
                "--",
                str(target),
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )

    def test_clean_scan_exits_zero_and_writes_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            target = tmp_path / "clean.txt"
            report_path = tmp_path / "privacy-report.json"
            target.write_text("reviewed educational content\n", encoding="utf-8")

            result = self.run_scan(r"private|/home/|secret|PHI", target, report_path)

            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "pass")
            self.assertEqual(report["findings"], [])
            self.assertEqual(report["target_count"], 1)

    def test_forbidden_match_exits_one_and_redacts_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            target = tmp_path / "bad.txt"
            report_path = tmp_path / "privacy-report.json"
            target.write_text("contains secret token text\n", encoding="utf-8")

            result = self.run_scan(r"private|/home/|secret|PHI", target, report_path)

            self.assertEqual(result.returncode, 1)
            report_text = report_path.read_text(encoding="utf-8")
            report = json.loads(report_text)
            self.assertEqual(report["status"], "fail")
            self.assertEqual(report["findings"][0]["line"], 1)
            self.assertEqual(report["findings"][0]["match"], "[REDACTED]")
            self.assertNotIn("secret", report_text)
            self.assertNotIn(str(tmp_path), report_text)

    def test_missing_target_and_invalid_regex_exit_two(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing_report = tmp_path / "missing-report.json"
            invalid_report = tmp_path / "invalid-report.json"
            target = tmp_path / "target.txt"
            target.write_text("content\n", encoding="utf-8")

            missing = self.run_scan(r"private|secret", tmp_path / "missing", missing_report)
            invalid = self.run_scan("[", target, invalid_report)

            self.assertEqual(missing.returncode, 2)
            self.assertEqual(invalid.returncode, 2)
            self.assertEqual(json.loads(missing_report.read_text(encoding="utf-8"))["status"], "error")
            self.assertEqual(json.loads(invalid_report.read_text(encoding="utf-8"))["status"], "error")


if __name__ == "__main__":
    unittest.main()
