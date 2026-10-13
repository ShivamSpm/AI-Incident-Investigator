"""Regression checks for evidence handling and conservative diagnoses."""

import copy
import json
import unittest
from pathlib import Path

from investigator import investigate


class InvestigationTests(unittest.TestCase):
    def setUp(self) -> None:
        fixture = Path(__file__).resolve().parents[1] / "data" / "incidents.json"
        self.incident = json.loads(fixture.read_text(encoding="utf-8"))[0]

    def test_diagnosis_requires_correlated_logs_and_traces(self) -> None:
        self.incident["evidence"] = self.incident["evidence"][:1]
        result = investigate(self.incident)
        self.assertEqual(result.status, "needs_more_evidence")
        self.assertIsNone(result.affected_service)

    def test_evidence_for_other_services_does_not_support_diagnosis(self) -> None:
        self.incident["evidence"][1]["service"] = "unrelated-service"
        self.assertEqual(investigate(self.incident).status, "needs_more_evidence")

    def test_undeclared_dependencies_do_not_support_diagnosis(self) -> None:
        self.incident["dependencies"] = []
        self.assertEqual(investigate(self.incident).status, "needs_more_evidence")

    def test_two_supported_dependencies_remain_inconclusive(self) -> None:
        extra = copy.deepcopy(self.incident["evidence"])
        for item in extra:
            item["id"] += "-inventory"
            item["target"] = "inventory"
        self.incident["dependencies"].append("inventory")
        self.incident["evidence"].extend(extra)
        self.assertEqual(investigate(self.incident).status, "needs_more_evidence")

    def test_duplicate_evidence_ids_are_rejected(self) -> None:
        self.incident["evidence"][1]["id"] = self.incident["evidence"][0]["id"]
        with self.assertRaisesRegex(ValueError, "Duplicate evidence"):
            investigate(self.incident)

    def test_non_finite_rates_are_rejected(self) -> None:
        self.incident["alert"]["value"] = float("nan")
        with self.assertRaisesRegex(ValueError, "finite rate"):
            investigate(self.incident)


if __name__ == "__main__":
    unittest.main()
