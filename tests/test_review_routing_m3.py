import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_content_contract_m2 import REPO_ROOT, VALIDATOR, valid_card
from test_lifecycle_m3 import approval


class ReviewRoutingM3Tests(unittest.TestCase):
    def run_validator(self, card: dict) -> tuple[subprocess.CompletedProcess[str], dict]:
        source = Path(tempfile.mkdtemp(prefix="gymprimer-review-routing-test-"))
        self.addCleanup(shutil.rmtree, source)
        cards = source / "cards"
        cards.mkdir(parents=True)
        (cards / "card.json").write_text(json.dumps(card, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        out = source / "report.json"
        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--source",
                str(source),
                "--schemas",
                str(REPO_ROOT / "schemas"),
                "--media",
                str(REPO_ROOT / "media"),
                "--out",
                str(out),
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )
        return result, json.loads(out.read_text(encoding="utf-8"))

    def assert_invalid(self, card: dict, *codes: str):
        result, report = self.run_validator(card)
        self.assertEqual(result.returncode, 1, result.stderr)
        reported = {finding["code"] for finding in report["findings"]}
        for code in codes:
            self.assertIn(code, reported)

    def test_trainer_only_mechanics_change_is_publishable_with_trainer_review(self):
        card = valid_card()
        card["content_digest"] = "sha256:test-digest"
        card["change_categories"] = ["exercise_mechanics"]
        card["approval_events"] = [approval("trainer", "movement_mechanics")]
        result, report = self.run_validator(card)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report["status"], "pass")

    def test_card_specific_safety_language_requires_physical_therapist(self):
        card = valid_card()
        card["content_digest"] = "sha256:test-digest"
        card["change_categories"] = ["card_safety_language"]
        card["approval_events"] = [approval("trainer", "card_content")]
        self.assert_invalid(card, "missing_review_tier")

    def test_emergency_policy_requires_sports_medicine_clinician(self):
        card = valid_card()
        card["content_digest"] = "sha256:test-digest"
        card["change_categories"] = ["emergency_criteria_policy"]
        card["approval_events"] = [approval("physical_therapist", "safety_language_policy")]
        self.assert_invalid(card, "missing_review_tier")

    def test_elevated_risk_default_deny_until_policy_defined(self):
        card = valid_card()
        card["safety_category"] = "elevated_risk"
        card["publication_status"] = "published"
        card["content_digest"] = "sha256:test-digest"
        card["change_categories"] = ["elevated_risk_card"]
        card["approval_events"] = [
            approval("trainer", "movement_mechanics"),
            approval("sports_medicine_clinician", "elevated_risk_card"),
        ]
        self.assert_invalid(card, "elevated_risk_policy_not_defined")

    def test_blocked_rehab_is_not_publishable_in_v1(self):
        card = valid_card()
        card["safety_category"] = "blocked_rehab"
        self.assert_invalid(card, "blocked_rehab_not_publishable")

    def test_cumulative_review_obligations_report_every_missing_tier(self):
        card = valid_card()
        card["content_digest"] = "sha256:test-digest"
        card["change_categories"] = ["card_safety_language", "emergency_criteria_policy"]
        card["approval_events"] = []
        result, report = self.run_validator(card)
        self.assertEqual(result.returncode, 1, result.stderr)
        missing = {
            finding["required_tier"]
            for finding in report["findings"]
            if finding["code"] == "missing_review_tier"
        }
        self.assertEqual(missing, {"physical_therapist", "sports_medicine_clinician"})


if __name__ == "__main__":
    unittest.main()
