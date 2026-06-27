import json
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_content_contract_m2 import REPO_ROOT, VALIDATOR, valid_card


class GeneratedOutputM4Tests(unittest.TestCase):
    def setUp(self):
        self.source = Path(tempfile.mkdtemp(prefix="gymprimer-generated-output-test-"))
        self.addCleanup(shutil.rmtree, self.source)
        (self.source / "cards").mkdir(parents=True)

    def write_card(self, card: dict, name: str) -> None:
        (self.source / "cards" / name).write_text(json.dumps(card, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    def run_validator(self, public_path: Path) -> tuple[subprocess.CompletedProcess[str], dict]:
        out = self.source / "validation-report.json"
        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--source",
                str(self.source),
                "--schemas",
                str(REPO_ROOT / "schemas"),
                "--media",
                str(REPO_ROOT / "media"),
                "--out",
                str(out),
                "--emit-public",
                str(public_path),
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )
        return result, json.loads(public_path.read_text(encoding="utf-8"))

    def card_variant(self, card_id: str, publication_status: str = "published", review_status: str = "approved") -> dict:
        card = valid_card()
        card["card_id"] = card_id
        card["version_id"] = "v1"
        card["publication_status"] = publication_status
        card["review_status"] = review_status
        card["review"]["content_digest"] = f"sha256:{card_id}"
        card["review"]["reviewer_public_id"] = "trainer-reviewer-a"
        card["locales"]["en-US"]["title"] = card_id.replace("-", " ").title()
        card["locales"]["en-US"]["aliases"] = [f"{card_id} alias"]
        return card

    def test_public_content_package_is_filtered_and_deterministic(self):
        self.write_card(self.card_variant("ex-public"), "01-public.json")
        self.write_card(self.card_variant("ex-draft", publication_status="unpublished", review_status="draft"), "02-draft.json")
        self.write_card(self.card_variant("ex-hidden", publication_status="hidden"), "03-hidden.json")
        self.write_card(self.card_variant("ex-superseded", publication_status="superseded"), "04-superseded.json")
        internal_only = self.card_variant("ex-internal-only", publication_status="unpublished")
        internal_only["license"]["license_kind"] = "unlicensed_internal_only"
        self.write_card(internal_only, "05-internal-only.json")

        first_public = self.source / "public-content.json"
        second_public = self.source / "public-content-rerun.json"
        first, first_payload = self.run_validator(first_public)
        second, second_payload = self.run_validator(second_public)

        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(first_public.read_text(encoding="utf-8"), second_public.read_text(encoding="utf-8"))
        self.assertEqual(first_payload, second_payload)
        self.assertEqual(first_payload["schema_version"], "content-schema-v1")
        self.assertEqual(first_payload["source_boundary"], "repository-reviewed-public-content")
        self.assertEqual(first_payload["counts"]["cards"], 1)
        self.assertEqual([card["card_id"] for card in first_payload["cards"]], ["ex-public"])

        public_card = first_payload["cards"][0]
        self.assertEqual(public_card["discovery"]["difficulty"], "beginner")
        self.assertEqual(public_card["discovery"]["equipment"], ["selectorized_machine"])
        self.assertEqual(public_card["discovery"]["movement_patterns"], ["pull_vertical"])
        self.assertEqual(public_card["discovery"]["primary_muscles"], ["latissimus_dorsi"])
        self.assertEqual(public_card["discovery"]["aliases"]["en-US"], ["ex-public alias"])
        self.assertNotIn("reviewer_public_id", json.dumps(public_card, sort_keys=True))
        self.assertNotIn("draft", json.dumps(first_payload, sort_keys=True).lower())
        self.assertNotIn(str(self.source), json.dumps(first_payload, sort_keys=True))

    def test_pilot_size_generation_completes_under_ten_seconds(self):
        for index in range(60):
            self.write_card(self.card_variant(f"ex-pilot-{index:02d}"), f"pilot-{index:02d}.json")

        public_path = self.source / "pilot-public-content.json"
        started = time.perf_counter()
        result, payload = self.run_validator(public_path)
        elapsed = time.perf_counter() - started

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(payload["counts"]["cards"], 60)
        self.assertLess(elapsed, 10.0)


if __name__ == "__main__":
    unittest.main()
