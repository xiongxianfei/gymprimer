import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "tools" / "validation" / "validate_content.py"


class ValidatorCliTests(unittest.TestCase):
    def test_empty_source_tree_writes_privacy_safe_deterministic_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "content"
            schemas = tmp_path / "schemas"
            media = tmp_path / "media"
            out = tmp_path / "generated" / "validation-report.json"
            source.mkdir()
            schemas.mkdir()
            media.mkdir()
            (schemas / "content-schema-version.txt").write_text("content-schema-v1\n", encoding="utf-8")

            cmd = [
                sys.executable,
                str(VALIDATOR),
                "--source",
                str(source),
                "--schemas",
                str(schemas),
                "--media",
                str(media),
                "--out",
                str(out),
            ]

            first = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            first_report = out.read_text(encoding="utf-8")

            second = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(first_report, out.read_text(encoding="utf-8"))

            report = json.loads(first_report)
            self.assertEqual(report["schema_version"], "content-schema-v1")
            self.assertEqual(report["status"], "pass")
            self.assertEqual(report["counts"]["valid_cards"], 0)
            self.assertEqual(report["counts"]["invalid_cards"], 0)
            self.assertEqual(report["counts"]["review_sensitive_changes"], 0)
            self.assertIn(
                {
                    "code": "no_cards_found",
                    "message": "No content card files were found under the source path.",
                },
                report["warnings"],
            )
            self.assertEqual(report["findings"], [])
            self.assertEqual(report["privacy"]["pii_required"], False)
            self.assertEqual(report["privacy"]["sensitive_data_allowed"], False)

            serialized = json.dumps(report, sort_keys=True)
            self.assertNotIn(str(tmp_path), serialized)
            self.assertNotIn(str(REPO_ROOT), serialized)
            self.assertNotIn("Traceback", first.stderr + first.stdout + first_report)

    def test_missing_input_path_fails_without_absolute_path_leak(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            schemas = tmp_path / "schemas"
            media = tmp_path / "media"
            out = tmp_path / "generated" / "validation-report.json"
            schemas.mkdir()
            media.mkdir()

            result = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    "--source",
                    str(tmp_path / "missing-content"),
                    "--schemas",
                    str(schemas),
                    "--media",
                    str(media),
                    "--out",
                    str(out),
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 2)
            report = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "error")
            self.assertEqual(report["findings"][0]["code"], "missing_path")
            self.assertEqual(report["findings"][0]["path_role"], "source")
            self.assertNotIn(str(tmp_path), json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
