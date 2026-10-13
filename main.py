"""Run the local investigation baseline against a synthetic incident."""

import argparse
import json
from pathlib import Path

from investigator import investigate


def main() -> None:
    fixture_path = Path(__file__).parent / "data" / "incidents.json"
    incidents = json.loads(fixture_path.read_text(encoding="utf-8"))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--incident",
        default="payment-unreachable",
        choices=[incident["id"] for incident in incidents],
        help="Synthetic incident to investigate.",
    )
    args = parser.parse_args()
    selected = next(incident for incident in incidents if incident["id"] == args.incident)
    try:
        result = investigate(selected)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result.to_dict(), indent=2))


if __name__ == "__main__":
    main()
