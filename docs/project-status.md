# Project status and decisions

Updated: November 2, 2026 (America/Los_Angeles).

## Confirmed user direction

- Persist and push the plan/context to the existing repository.
- Seven means milestones, not calendar days, and is not a ceiling. Add milestones
  as needed; prioritize quality, differentiation, and engineering depth.
- Implement milestones individually when requested.
- Authorized total project API spending ceiling: **$100**.
- The user reports checking the billing dashboard and confirms sufficient credits.
  The agent has not independently inspected the account. Do not publish its balance.
- The user requested verification of the local setup; see the environment record.
- The user will build the portfolio website separately. Focus on the application.
- Ask about unresolved decisions instead of assuming answers.

## Decision log

| ID | Status | Decision / implication |
| --- | --- | --- |
| D1 | Resolved by user | No seven-milestone ceiling or calendar deadline; no need to constrain work by daily hours |
| D2 | Budget and funding confirmed by user | $100 total API ceiling; sufficient credits reported after dashboard inspection; provider/model and secure credential path still to establish |
| D3 | Environment inspected | WSL 2 verified; Docker installed but stopped; live stack capacity remains a Milestone 1 check |
| D4 | Scope direction resolved | Full quality over schedule; recommended 12-milestone roadmap retains three screens; verify proposed Hermes integration before implementation |
| D5 | Resolved by user | Portfolio website excluded; application UI, technical docs, and reproducibility remain in scope |

Recommended differentiators: claim-level evidence inspection, diagnosis challenges,
measured recovery, and in-app recorded playback. These are design recommendations
within the user's broad quality objective, not individually user-specified features
or claims of industry-first novelty.

## Current implementation and validation

Starting implementation commit: `b919a63` (`First commit`). Initial planning
documents were pushed in `0ae0b37`. Existing branch: `master` tracking
`origin/master`. Remote:
`https://github.com/ShivamSpm/AI-Incident-Investigator.git`.

Implemented: deterministic investigator, synthetic fixtures, separate expectations,
one prepared skill, CLI, eval runner, and six regression tests.
Runtime/MCP/live telemetry/API/storage/UI/action execution are not implemented.
No implementation milestone has started.

| Existing check | Observed result | Interpretation |
| --- | --- | --- |
| `python -m unittest discover -s tests -v` | 6 passed during initial planning | Starter regression checks only |
| `python -m evals.run` | 3/3 passed during initial planning | Deterministic synthetic fixtures only |

Latest changes update planning documents only. No paid API calls, credit purchases,
or billing-setting changes were made during planning.

## Environment and account follow-up

See [the environment record](dev-environment.md) for verified versions, capacity,
and the stopped Docker engine. Installed Docker does not mean a running lab.

The available billing browser redirected to sign-in. The user subsequently checked
their balance and confirmed adequate credits. Keep private billing screenshots,
balances, account identifiers, and credentials outside this public repository.

Establish provider/model and secure API credentials before Milestone 5. These do
not block independent lab preparation. Record pinned dependencies, query details,
recovery windows, trial counts, and actual resource use during implementation.

## Milestone handoff

These 12 milestones replace the earlier seven-day grouping. A future "Day N"
request maps to Milestone N in `PROJECT_PLAN.md`.

| Milestone | State | Next evidence needed |
| --- | --- | --- |
| Planning | Updated for user answers | Roadmap, constraints, local observations, and context synchronized |
| 1: Local lab | Not started | Running Linux engine, pinned demo, healthy telemetry, resources |
| 2: Scenarios/contracts | Not started | Four validated fault/reset cycles and isolated ground truth |
| 3: Evidence layer | Not started | Live normalized observations and provenance |
| 4: MCP tools | Not started | Typed queries and answer/control isolation |
| 5: Hermes/skills | Not started | Model/credential readiness and budgeted real investigation |
| 6: API/storage/SSE | Not started | Durable run and reconnect behavior |
| 7: Console | Not started | Inspectable evidence and hypotheses |
| 8: Approval/actions | Not started | Exact approval enforcement and one-time execution |
| 9: Recovery/report | Not started | Fresh verification and honest outcomes |
| 10: Evals/challenges | Not started | Comparable trials, ambiguous/adversarial cases, failures |
| 11: Dashboard/Skills | Not started | Stored results and version-linked comparisons |
| 12: Finish/reproducibility | Not started | Recorded playback, clean setup, relevant checks/docs |

No implementation milestone has been requested yet. For each requested milestone,
record concrete changes, validation, remaining work, and applicable decisions here.
