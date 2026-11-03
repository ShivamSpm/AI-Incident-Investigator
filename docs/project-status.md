# Project status and decisions

Last updated: November 2, 2026 (America/Los_Angeles).

## Confirmed user direction

- Keep the supplied project plan in this repository for future context.
- Propose seven days of work; the user intends to request implementation day by day.
- Optimize the finished work for a resume and portfolio presentation.
- Ask about missing decisions instead of making assumptions.
- Suggest improvements that fit the plan; suggestions are not approved additions.
- Push the planning documents to the existing repository.

## Current implementation

Starting commit: `b919a63` (`First commit`). Existing branch: `master` with
`origin/master`. Remote: `https://github.com/ShivamSpm/AI-Incident-Investigator.git`.
The working tree was clean before planning changes.

Implemented: deterministic Python investigator, synthetic observation fixtures,
separate expected outcomes, one prepared skill, CLI, evaluation runner, and tests.
Not implemented: LLM/Hermes, MCP, live OpenTelemetry integration, API/persistence,
frontend, executable remediation, and live/model evaluations.

Validation during planning:

| Check | Result | Interpretation |
| --- | --- | --- |
| `python -m unittest discover -s tests -v` | 6 tests passed | Starter regression checks only |
| `python -m evals.run` | 3/3 cases passed | Deterministic synthetic fixtures only |

## Open decisions

Questions were presented to the user during planning. No answers have been
recorded yet. Do not treat any suggested value as authorization.

| ID | Decision needed | Why it matters |
| --- | --- | --- |
| D1 | Focused hours per day; calendar days versus implementation milestones | Determines whether the full scope can credibly fit seven days |
| D2 | Available API provider/model and authorized total spending | Required before model selection or paid investigations/evals; the reference's $25 is unconfirmed |
| D3 | Machine RAM/free disk and working Docker Desktop/WSL2 setup | Determines whether the full demo, Kafka, and observability fit locally |
| D4 | Whether Hermes and all three screens are firm requirements; acceptable cuts | Avoids silently changing the reference architecture or scope |
| D5 | Public interactive app versus portfolio page with recorded local demo | Affects hosting, access control, recurring cost, and final presentation |

Dependency revisions, trial counts, telemetry queries, and recovery windows are
Day 1/implementation findings to record after validation. Target accuracy and
recruiting impact have not been promised.

## Daily handoff

| Day | State | Evidence / next action |
| --- | --- | --- |
| Planning | Documents prepared | Original references archived; canonical plan and architecture linked from README and AGENTS.md |
| 1 | Not started | Resolve applicable open decisions; validate pinned live lab and four faults |
| 2 | Not started | Follow Day 1 observations and tool/evidence contracts |
| 3 | Not started | Requires model authorization and verified runtime/tool boundary |
| 4 | Not started | Persist real investigation events and expose API/UI flow |
| 5 | Not started | Enforce approval, execute allowed actions, verify recovery |
| 6 | Not started | Run budgeted comparable evals and publish complete results |
| 7 | Not started | Finish Skills view, reproducibility, demo, and portfolio materials |

## Suggestions awaiting a user decision

The plan proposes an evidence-removal challenge, inspectable recorded run playback,
and pre/post recovery comparisons. None has been silently added to committed
implementation scope. Record accepted suggestions and their scope here.

## Next requested work

No implementation day has been requested yet. When the user requests one, read
the plan and this ledger, resolve only the decisions it depends on, implement the
requested milestone, and record the observed result and remaining work here.
