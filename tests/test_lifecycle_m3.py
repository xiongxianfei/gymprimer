import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_content_contract_m2 import REPO_ROOT, VALIDATOR, valid_card


def approval(tier: str = "trainer", scope: str = "card_content", digest: str = "sha256:test-digest") -> dict:
    return {
        "reviewer_public_id": f"{tier}-reviewer",
        "review_tier": tier,
        "review_scope": scope,
        "timestamp": "2026-06-27T12:00:00Z",
        "content_digest": digest,
    }


def audit_event() -> dict:
    return {
        "card_id": "ex-lat-pulldown",
        "version_id": "v1",
        "locale": "en-US",
        "event_type": "publish",
        "review_status_before": "approved",
        "review_status_after": "approved",
        "publication_status_before": "unpublished",
        "publication_status_after": "published",
        "actor_id": "maintainer-a",
        "actor_role": "schema_owner",
        "required_review_tiers": ["trainer"],
        "completed_review_tiers": ["trainer"],
        "content_digest_before": "sha256:test-digest",
        "content_digest_after": "sha256:test-digest",
        "timestamp": "2026-06-27T12:00:00Z",
        "reason": "Publish approved fixture.",
    }


class LifecycleM3Tests(unittest.TestCase):
    def run_validator(self, card: dict) -> tuple[subprocess.CompletedProcess[str], dict]:
        source = Path(tempfile.mkdtemp(prefix="gymprimer-lifecycle-test-"))
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

    def assert_invalid(self, card: dict, code: str):
        result, report = self.run_validator(card)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(report["status"], "fail")
        self.assertIn(code, {finding["code"] for finding in report["findings"]})

    def test_non_approved_published_card_is_rejected(self):
        card = valid_card()
        card["review_status"] = "draft"
        self.assert_invalid(card, "review_not_approved")

    def test_direct_draft_to_approved_review_transition_is_rejected(self):
        card = valid_card()
        card["lifecycle_events"] = [
            {
                **audit_event(),
                "event_type": "review_transition",
                "review_status_before": "draft",
                "review_status_after": "approved",
                "publication_status_before": "unpublished",
                "publication_status_after": "unpublished",
            }
        ]
        self.assert_invalid(card, "review_transition_invalid")

    def test_approved_unpublished_publish_request_with_review_is_eligible(self):
        card = valid_card()
        card["publication_status"] = "unpublished"
        card["publish_request"] = True
        card["content_digest"] = "sha256:test-digest"
        card["approval_events"] = [approval()]
        result, report = self.run_validator(card)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report["status"], "pass")

    def test_hidden_restore_requires_eligibility_recheck(self):
        card = valid_card()
        card["publication_status"] = "hidden"
        card["lifecycle_events"] = [
            {
                **audit_event(),
                "publication_status_before": "hidden",
                "publication_status_after": "published",
                "eligibility_rechecked": False,
            }
        ]
        self.assert_invalid(card, "publication_eligibility_recheck_required")

    def test_superseded_publish_request_is_rejected(self):
        card = valid_card()
        card["publication_status"] = "superseded"
        card["publish_request"] = True
        self.assert_invalid(card, "version_superseded")

    def test_review_sensitive_edit_to_published_requires_new_unpublished_version(self):
        card = valid_card()
        card["edit_event"] = {
            "review_sensitive": True,
            "source_publication_status": "published",
            "creates_new_version": False,
            "new_publication_status": "published",
        }
        self.assert_invalid(card, "review_sensitive_edit_requires_new_version")

    def test_review_sensitive_edit_to_approved_unpublished_expires_review(self):
        card = valid_card()
        card["publication_status"] = "unpublished"
        card["edit_event"] = {
            "review_sensitive": True,
            "source_publication_status": "unpublished",
            "new_review_status": "approved",
        }
        self.assert_invalid(card, "review_sensitive_edit_requires_review_expired")

    def test_lifecycle_audit_event_requires_separate_status_fields(self):
        card = valid_card()
        event = audit_event()
        event.pop("review_status_before")
        card["audit_events"] = [event]
        self.assert_invalid(card, "audit_event_missing_field")

    def test_combined_lifecycle_status_is_rejected(self):
        card = valid_card()
        card["audit_events"] = [{**audit_event(), "lifecycle_status": "approved_published"}]
        self.assert_invalid(card, "lifecycle_status_combined_forbidden")

    def test_approval_event_requires_digest_scope(self):
        card = valid_card()
        event = approval()
        event.pop("content_digest")
        card["approval_events"] = [event]
        self.assert_invalid(card, "approval_event_missing_field")

    def test_approval_event_digest_must_match_current_content_digest(self):
        card = valid_card()
        card["content_digest"] = "sha256:current"
        card["approval_events"] = [approval(digest="sha256:stale")]
        self.assert_invalid(card, "approval_digest_mismatch")


if __name__ == "__main__":
    unittest.main()
