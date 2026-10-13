"""Score the baseline on synthetic cases; expected answers never enter it."""

import json
from pathlib import Path

from investigator import investigate


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    incidents = json.loads((root / "data" / "incidents.json").read_text(encoding="utf-8"))
    expectations = json.loads(
        (root / "evals" / "expectations.json").read_text(encoding="utf-8")
    )
    scores = []
    for incident in incidents:
        expected = expectations[incident["id"]]
        result = investigate(incident)
        source_ids = {item["id"] for item in incident["evidence"]}
        checks = {
            "expected_status": result.status == expected["status"],
            "expected_service": result.affected_service == expected["affected_service"],
            "required_evidence": set(expected["required_evidence_ids"]).issubset(
                result.evidence_ids
            ),
            "valid_evidence_ids": set(result.evidence_ids).issubset(source_ids),
            "no_actions_executed": result.actions_executed == [],
        }
        scores.append(
            {"incident_id": incident["id"], "passed": all(checks.values()), "checks": checks}
        )
    passed = sum(score["passed"] for score in scores)
    print(
        json.dumps(
            {
                "mode": "deterministic_baseline",
                "dataset": "synthetic_starter_cases",
                "passed": passed,
                "total": len(scores),
                "cases": scores,
            },
            indent=2,
        )
    )
    return 0 if passed == len(scores) else 1


if __name__ == "__main__":
    raise SystemExit(main())
