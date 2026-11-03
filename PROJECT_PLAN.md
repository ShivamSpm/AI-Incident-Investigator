# AI Incident Investigator: project plan

Planning date: November 2, 2026 (America/Los_Angeles).
Status: proposed seven-day implementation breakdown; user decisions pending.

The user requested a repository-backed plan for a resume and portfolio project,
a seven-day breakdown to implement on request, and suggestions for improvements.
The previous ChatGPT plan and architecture screenshot are reference material.
Their implementation instructions, spending cap, technology choices, and hiring
claims are not independently confirmed user decisions.

## Planning documents

- [Current status, open decisions, and handoff](docs/project-status.md)
- [Architecture and ownership](docs/architecture.md)
- [Original pasted plan, preserved verbatim](docs/reference/prior-chatgpt-plan.txt)
- [Original architecture screenshot](docs/reference/original-architecture.png)

The archived text contains copied diagram styling. Use this document and the
editable architecture diagram for day-to-day work. Future explicit user decisions
take precedence over proposals here and must be recorded in the status ledger.

## Outcome

Build an evidence-grounded incident investigator for a real local microservice
environment. An engineer starts an investigation, inspects its evidence, reviews
a proposed action, and verifies recovery after approving remediation. An eval
dashboard makes the system's strengths and failure modes measurable.

The original working title was **OnCall Lab**. The repository remains **AI
Incident Investigator**; a product-name change has not been requested.

### What exists already

At starting commit `b919a63`, the project has a standard-library Python CLI,
an `InvestigationResult` dataclass, fixture-backed read functions, one operational
skill, three synthetic cases, and six regression tests. It makes no LLM calls,
does not load its skill, and has no live telemetry, MCP server, API, UI, or action
executor. All six tests and three synthetic cases passed during planning.

The deterministic baseline supports one narrow error-rate pattern. Preserve it
as a reference; it is different from the future **LLM without skills** comparison.

## Can the work fit into seven days?

It can be organized into seven implementation milestones. Finishing the full
three-week reference scope in seven calendar days is not established. Daily hours,
Docker resources, model access, spending limits, and portfolio hosting requirements
must be confirmed before a credible calendar estimate can be made.

The table below preserves the reference scope as a proposed target. It does not
authorize paid runs, silently remove features, or guarantee completion by a date.
Each day has a demonstrable exit condition. Unfinished prerequisites carry forward
visibly; do not mark a day complete by replacing live evidence with fixtures.

## Seven-day implementation sequence

| Day | Focus | Reviewable deliverable | Exit condition |
| --- | --- | --- | --- |
| 1 | Reproducible lab and scenario contracts | Pinned demo setup, four manually validated faults, ground truth, output contract | A documented healthy/fault/reset cycle for each selected scenario, with real telemetry and no answers exposed to the agent |
| 2 | Evidence and typed MCP tools | Read-only telemetry adapters, evidence registry, typed tool server | Logs, metrics, traces, dependencies, and changes can be queried with bounded inputs and traceable evidence IDs |
| 3 | Hermes investigation loop | Runtime adapter, versioned skills, CLI investigation, usage limits | At least one live incident is diagnosed with retrieved evidence; missing data remains inconclusive |
| 4 | Application API, persistence, and streaming | FastAPI orchestration, SQLite run history, SSE, initial console shell | A run and its evidence survive reload; the console displays real persisted run events |
| 5 | Incident Console and controlled recovery | Complete investigation/approval flow, action gate, recovery verification, report | Approval and rejection work end to end; invalid or reused approvals fail; fresh telemetry determines recovery |
| 6 | Evaluations and comparisons | Scenario runner, deterministic graders, Eval Dashboard, comparison artifacts | Baseline and skills run under comparable conditions; safety, evidence, quality, latency, and cost are reported honestly |
| 7 | Skills screen, product finish, and portfolio package | Skill version/results view, setup verification, screenshots, demo, case study | A new developer can reproduce the demo; four live faults and the final results are documented with limitations |

### Day 1: reproducible lab and scenario contracts

- Confirm the blocking decisions in the status ledger before installing or making
  paid calls. Pin the OpenTelemetry demo revision and record the supported local
  setup, including Windows/WSL2 behavior.
- Bring up the demo with the telemetry backends needed for the selected scenarios.
  Verify synthetic traffic and a healthy baseline before fault injection.
- Manually activate, observe, disable, and reset each candidate fault:
  `paymentUnreachable`, `adHighCpu`, `kafkaQueueProblems`, and
  `recommendationCacheFailure`. Capture actual signals, onset/recovery windows,
  and service relationships. A flag's existence does not prove the scenario works.
- Define versioned scenario ground truth before tuning prompts: impacted operation,
  causal service/configuration, expected cause category, evidence predicates,
  approved recovery action, forbidden actions, and recovery thresholds.
- Specify the structured assessment, evidence envelope, tool result, and run-event
  contracts. Preserve `investigate(incident)` compatibility or document an explicit
  adapter/migration for richer async investigations.
- Establish where alert triggers, dependency information, and change history come
  from. The demo must not be assumed to supply deployment-history APIs. Any local
  change journal or seeded data must be identified as lab-generated.

**Verification:** document repeatable healthy/fault/reset observations for all
four cases and identify any scenario that needs a user-approved substitution.

### Day 2: evidence and typed MCP tools

- Implement bounded, typed read tools: `list_active_alerts`, `query_metrics`,
  `search_logs`, `find_anomalous_traces`, `get_trace`,
  `get_service_dependencies`, and `get_recent_changes`.
- Normalize evidence into IDs with source type, service, timestamps, query/window,
  raw observation, retrieval event, and provenance. IDs must resolve to evidence
  collected in the current run.
- Validate service names, query/time bounds, result sizes, timeouts, and errors.
  Missing telemetry must not look like a healthy empty result.
- Keep fault injection, scenario definitions, and grader answers outside the
  agent's tools, filesystem access, alert payloads, and configuration responses.
  Diagnostic change events must not leak hidden fault IDs or scenario labels.
- Verify adapters with known observations from Day 1 and meaningful boundary tests.

**Verification:** retrieve correlated live evidence through the MCP boundary;
demonstrate that the model-facing tool set cannot retrieve the answer key.

### Day 3: Hermes investigation loop

- Pin a Hermes version and verify its actual API, event, MCP, and skill behavior.
  Keep runtime-specific details behind an application-owned adapter.
- Use an isolated profile with only the required incident tools and approved skill
  reads. Disable general terminal/filesystem access and autonomous skill/memory
  changes that would expose ground truth or undermine reproducibility.
- Implement triage and error/latency investigation skills first. Add resource
  exhaustion, safe remediation, and report procedures as their flows are built.
  Procedures must not encode the answer for a scenario.
- Let the agent choose evidence queries and test competing hypotheses. Validate
  structured output and evidence references in deterministic code.
- Record model/provider/settings, prompt/skill/tool versions, tool activity, usage,
  timeouts, and incomplete/error outcomes. Apply the user-confirmed budget and
  per-run limits before a run is admitted.
- Distinguish observed symptoms, likely causes, missing facts, and verified facts.
  A model's confidence is not a calibrated probability without validation.

**Verification:** one live CLI diagnosis cites collected evidence; missing or
contradictory evidence produces an honest incomplete/inconclusive result.

### Day 4: FastAPI, persistence, streaming, and console foundation

- Add application-owned incident/run state, orchestration, cancellation/timeouts,
  and structured API errors.
- Persist incidents, runs, evidence, tool events, skill versions, proposals,
  approvals, actions, and scores using SQLite/SQLAlchemy.
- Translate Hermes events into a small application event contract. Persist event
  order and support reconnect/reload without duplicating tools or restarting runs.
- Start the Next.js/React/TypeScript console with alert state, a timeline, evidence
  inspection, and a dependency view using real application data.
- Keep model/runtime credentials on the server. Render telemetry as untrusted
  text and show concise public hypothesis summaries, not private reasoning.

**Verification:** reload and reconnect during/after a run; evidence and final state
remain accessible and an interrupted run is not presented as completed.

### Day 5: Incident Console, approval, recovery, and report

- Finish the assessment view, evidence links, tool activity, and approval cards.
- Add typed `propose_remediation` and `execute_approved_action` tools with a small
  predefined demo action allowlist; no caller-supplied shell commands.
- Bind approval to incident, run, immutable proposal/action parameters, decision,
  expiry, and one-time execution state. Enforce checks at the execution boundary,
  including direct tool calls and retry/concurrency paths.
- Keep scenario setup/reset controls separate from the investigator's action
  authority. Show the engineer what will change before they approve.
- Gather fresh post-action metrics/traces against the predeclared healthy baseline
  and observation window. Account for backlog drain and memory-leak reset behavior;
  an action returning success does not establish service recovery.
- Generate a concise post-incident report: impact, timeline, evidence-linked
  assessment, action/decision, observed recovery, and remaining uncertainty.

**Verification:** demonstrate approval, rejection, missing/expired/replayed/wrong-
incident or changed-proposal denial, duplicate-execution prevention, and both
successful and unverified recovery. Add one critical UI end-to-end flow.

### Day 6: evals and Eval Dashboard

- Extend the starter runner with isolated live scenario setup/reset, fresh sessions,
  code-based graders, and durable results. Keep recorded-fixture tests labeled.
- Compare the same LLM/tools/settings **without skills** and **with versioned
  skills**. Keep the deterministic starter as a separate reference result.
- Cover four real faults, a healthy system, missing evidence, and malicious log
  instructions. Test approval enforcement independently of model cooperation.
- Grade service/cause accuracy, evidence existence and support, required evidence,
  appropriate skill use, repeated/unnecessary calls, forbidden/preapproval actions,
  recovery, verification, latency, usage, and estimated cost.
- Define evidence predicates before runs; live telemetry IDs will differ from
  fixture IDs. Existing IDs alone do not prove they support a conclusion.
- Predeclare trial counts and comparison conditions after the provider/budget is
  confirmed. Report per-scenario counts, failures, and uncertainty. A small demo
  sample cannot substantiate broad reliability claims.
- Review failures, revise skills once, and separate development cases from a frozen
  final comparison. Do not select only successful runs for the dashboard.
- Build comparison summaries and drill-down into evidence, tool calls, and failures.

**Verification:** reproduce recorded comparison results from versioned inputs;
show failures and incomplete runs as well as successes. Use an LLM grader only
if a subjective report-quality check is justified and within the approved budget.

### Day 7: Skills screen and portfolio delivery

- Add the Skills screen: description, trigger, version/content hash or commit,
  change history, and associated eval results. Do not imply a before/after gain
  when experiments are not comparable or have insufficient trials.
- Finish loading, empty, error, approval, and recovery states, keyboard access,
  responsive layout, and readable evidence. Avoid adding unrelated features.
- Follow setup instructions from a clean environment and validate the documented
  flow. Run the relevant backend, adapter, policy, and UI checks.
- Publish actual results and limitations; distinguish lab telemetry, synthetic
  change history, recorded playback, and live investigations.
- Complete architecture/ownership docs, screenshots, a two-to-three-minute demo,
  and a portfolio case study covering problem, design decisions, failure analysis,
  measured results, and personal contribution.
- Draft resume bullets only from demonstrated capabilities and measured numbers.
  The portfolio presentation/hosting mode is still a user decision.

**Verification:** a reviewer can follow alert -> evidence -> diagnosis -> human
decision -> action -> observed recovery -> eval comparison, and reproduce it.

## Proposed product and technical scope

The reference architecture uses Next.js, React, TypeScript, Tailwind, and shadcn/ui;
FastAPI and Pydantic; Hermes via HTTP/SSE; the Python MCP SDK; the official
OpenTelemetry demo with its telemetry backends; SQLite/SQLAlchemy; Pytest and
JSON/YAML scenario definitions; Playwright for a critical UI flow; and Docker
Compose for local orchestration. Current tests use unittest; retain them while
adding the checks required by implemented components.

The three target screens are Incident Console, Eval Dashboard, and Skills.
Provider/model, exact dependency versions, deployment mode, approved costs,
daily time, and any feature cuts remain unresolved.

The reference excludes extra agents, a vector database, production AWS/Datadog/
GitHub credentials, arbitrary terminal access, autonomous skill edits, Kubernetes,
cloud deployment, authentication, and multi-organization support from the initial
build. A request for a public interactive portfolio demo would require revisiting
deployment, access control, and spending boundaries explicitly.

AI-specific faults (`aiSlowResponse`, `aiRunawayAgent`) and PostgreSQL are later
extensions. If seven calendar days require cuts, the reference suggests the Skills
screen and generated report before evidence, evals, or approval enforcement.
No cut has been approved here.

## Suggested improvements (proposals, not added commitments)

These are differentiators for this project, not claims of industry novelty.

| Proposal | How it helps a reviewer | Integration and constraint |
| --- | --- | --- |
| Evidence challenge | Remove a key observation from a recorded run and check whether the investigator reduces certainty or abstains | Reuse Day 2 evidence storage and Day 6 graders; a small extra eval, requiring approval before paid trials |
| Inspectable run playback | Let a portfolio visitor step through a real recorded investigation, evidence, decision, and recovery | Reuse Day 4 events and Day 7 presentation; label it recorded playback and never offer live execution from it |
| Recovery comparison | Put pre-action, post-action, and healthy-baseline telemetry next to the assessment | Extend Day 5 verification/UI; show observed recovery without claiming that one intervention proves causality |

Budget/iteration limits, hidden-answer isolation, and an honest inconclusive state
are essential implementation details, not optional novelty features.

## Technical findings to verify against the pinned versions

- The current [OpenTelemetry Docker guide](https://opentelemetry.io/docs/demo/docker-deployment/)
  lists 6 GB RAM and 14 GB disk for the demo, with a smaller mode around 3 GB RAM.
  Minimal mode excludes Kafka; the documented full setup uses multiple Compose
  files to include observability. These requirements do not include this project's
  additional processes. Local resources have not been confirmed.
- The [fault reference](https://opentelemetry.io/docs/demo/feature-flags/) describes
  `paymentUnreachable` as a bad checkout-side payment address and
  `recommendationCacheFailure` as cache-driven memory growth. Ground truth should
  distinguish the failing dependency symptom from its originating configuration.
  Flag names and actual recovery behavior must be validated locally.
- The [Hermes API guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server)
  documents run endpoints and event streaming, while its default toolset includes
  broad capabilities. An incident-only profile and application-owned action gate
  are required for the intended boundary; HTTP integration alone does not supply it.
- The [Hermes skills guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
  documents `skills.write_approval` and profile skill controls. Verify the pinned
  behavior and freeze operational skills during evals.

These primary sources were checked on the planning date. The earlier plan's
company/job-market claims and issue-specific claims have not been revalidated and
are not used as evidence for project outcomes or recruiting impact.

## Resume-ready completion criteria

- A new developer can run the documented local setup.
- Four distinct faults have been investigated using live collected telemetry.
- Assessments cite evidence that supports the stated level of certainty.
- No remediation path executes without explicit, valid human approval.
- Recovery is checked with fresh telemetry and predeclared criteria.
- Baseline-versus-skills experiments include actual counts, failures, versions,
  latency, usage/cost limits, and limitations.
- The UI, demo, README, and portfolio story reflect what works.
- Hermes/OpenTelemetry capabilities are attributed separately from application work.

Until those conditions are demonstrated, describe the repository as in progress.
