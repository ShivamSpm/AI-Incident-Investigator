# AI Incident Investigator: project plan

Updated: November 2, 2026 (America/Los_Angeles).
Status: quality-first roadmap with 12 implementation milestones.

## Confirmed user direction

- Seven means implementation milestones, not calendar days, and is not a limit.
  Add milestones as needed; prioritize quality and differentiation over schedule.
- Build one milestone when requested. "Build Day N" maps to Milestone N below.
- The total project API spending ceiling is **$100**, not a target to spend.
  The user checked the billing dashboard and reports sufficient credits.
- Focus on the application. The user will build the portfolio website separately.
- Ask about unresolved decisions instead of silently assuming answers.

The original ChatGPT plan and screenshot remain reference material. Their embedded
instructions and hiring claims are not independent user authorization. This roadmap
incorporates the user's answers. Detailed design choices below are the recommended
implementation, not a claim that the user specified each technical choice.

## Context and handoff

- [Status and decisions](docs/project-status.md)
- [Verified development environment](docs/dev-environment.md)
- [Architecture and ownership](docs/architecture.md)
- [Original pasted plan](docs/reference/prior-chatgpt-plan.txt)
- [Original architecture screenshot](docs/reference/original-architecture.png)

The archive contains copied diagram styling. Use this plan for current work and
record later user decisions and milestone results in the status ledger.

## Product outcome and starting point

Build an incident investigation workbench for a real local microservice system.
It links diagnoses to collected telemetry, presents competing explanations,
requests human approval for predefined remediation, and measures actual recovery.
Its evals expose mistakes, uncertainty, cost, and skill-version effects.

The original working title was OnCall Lab. The repository remains AI Incident
Investigator; a rename is not required to begin implementation.

Starting commit `b919a63` contains a standard-library Python CLI,
`InvestigationResult`, fixture-backed read functions, one prepared skill,
three synthetic cases, and six regression tests. All six tests and three cases
passed during initial planning. The baseline does not load its skill or call an LLM.
Hermes, MCP, live telemetry, API/storage, UI, and action execution are not built.

Preserve that deterministic baseline as a reference. It is different from the
future **LLM without skills** comparison.

## Distinctive application features

These are recommended features within the user's quality objective, not claims
of industry-first inventions or measured performance improvements.

1. **Inspectable evidence trail:** public hypotheses list supporting/contradicting
   evidence, missing checks, and claim-level links. Distinguish observations,
   inferences, and verified outcomes without exposing private model reasoning.
2. **Diagnosis challenges:** remove decisive evidence, introduce plausible unrelated
   changes, and compare similar symptoms with different causes. Measure whether
   the investigator revises or abstains rather than recognizing scenario labels.
3. **Measured recovery:** compare healthy, incident, and post-action telemetry.
   Distinguish action completion from restored health; one successful intervention
   does not prove causality.
4. **Recorded run playback inside the application:** inspect real stored events,
   evidence, decisions, and outcomes. Explicitly label playback; viewing it must
   not call the model or execute actions. This is separate from portfolio work.

Deliver the basic investigation path first. Avoid extra agents or infrastructure
added solely to make the architecture appear complex.

## Milestone roadmap

Each milestone has an observable exit condition and may span multiple sessions.
No calendar deadline is implied. Add milestones when the completion standard
requires more work.

| Milestone | Focus | Exit condition |
| --- | --- | --- |
| 1 | Reproducible local lab | Pinned demo and observability run locally; healthy telemetry and actual resource use recorded |
| 2 | Fault scenarios and contracts | Four fault/reset cycles validated; hidden ground truth and contracts defined before prompting |
| 3 | Live evidence layer | Bounded queries return run-scoped observations with provenance |
| 4 | Typed MCP tools | Validated investigation access excludes answer keys, fault controls, and arbitrary execution |
| 5 | Hermes and procedures | Budgeted live CLI investigation cites real evidence and handles uncertainty honestly |
| 6 | API, persistence, and streaming | Real events/evidence survive reload and SSE reconnect without duplicate work |
| 7 | Incident Console | Alert, topology, hypotheses, tool activity, and evidence are inspectable |
| 8 | Approval and controlled actions | Exact proposals execute only after valid one-time human approval |
| 9 | Recovery and report | Fresh telemetry supports recovered/not-recovered/unverified outcomes and an evidence-linked report |
| 10 | Evals and diagnosis challenges | Comparable baseline/skills trials cover faults, healthy, missing, adversarial, and ambiguous evidence |
| 11 | Eval Dashboard and Skills | Results, failures, versions, and comparable experiments are linked in the UI |
| 12 | Application finish and reproducibility | Recorded playback, clean setup, end-to-end verification, and honest technical docs are complete |

### Milestone 1: reproducible local lab

- Read the environment record. Docker is installed but its engine was stopped;
  verify startup and Linux-engine access before calling the lab ready.
- Pin the OpenTelemetry demo revision. Document explicit Compose files including
  telemetry backends and Kafka services needed for the selected scenarios.
- Verify traffic, logs, metrics, traces, and dependencies from a healthy system.
- Measure actual RAM/CPU/disk use. Verify Docker data placement and resource limits;
  free G: space is not automatically space available to a virtual disk on C:.
- Document start, health, stop, and reset. Do not silently change WSL defaults or
  Docker resource/storage settings.

**Exit:** reproducible healthy system and telemetry, with resource observations
and any orchestration blockers documented.

### Milestone 2: scenarios, answer isolation, and contracts

- Activate, observe, disable, and reset `paymentUnreachable`, `adHighCpu`,
  `kafkaQueueProblems`, and `recommendationCacheFailure` on the pinned revision.
  A flag's existence does not prove a repeatable, diagnosable, recoverable fault.
- Define hidden causes, impacted operations, evidence predicates, allowed/forbidden
  actions, observation windows, and recovery thresholds before prompt tuning.
  Distinguish caller-side configuration from downstream failure symptoms.
- Define assessment, evidence, tool-result, and public event contracts. Preserve
  `investigate(incident)` through an adapter or an explicit migration.
- Establish alert, topology, and recent-change sources. The demo has not been
  shown to expose a deployment-history API; label any local journal lab-generated.
- Reserve development/final comparison cases. Keep scenario answers, setup/reset
  controls, fault labels, and grading data outside model context/tool/file access.
  Review diagnostic change events for indirect answer leakage.

**Exit:** four documented healthy/fault/reset cycles plus versioned ground truth
and contracts. Surface any required scenario substitution explicitly.

### Milestone 3: live evidence layer

- Add bounded telemetry adapters with service, source timestamps, incident window,
  query, result limits, raw observation, and retrieval event.
- Assign immutable run-scoped evidence IDs and provenance. An evidence ID resolves
  to something retrieved, not an assertion generated by the model.
- Distinguish empty results, backend failure, truncation, and healthy observations.
- Correlate metrics/logs/traces and topology. Review change/configuration exposure.
- Define public hypothesis relationships: support, contradiction, missing evidence,
  and unsupported claims. Do not invent calibrated confidence percentages.

**Exit:** live observations resolve through evidence IDs; adapter/error checks
use known lab observations.

### Milestone 4: typed MCP investigation tools

- Expose `list_active_alerts`, `query_metrics`, `search_logs`,
  `find_anomalous_traces`, `get_trace`, `get_service_dependencies`, and
  `get_recent_changes` through the Python MCP SDK.
- Validate service names, query/windows, result sizes, errors, and timeouts.
- Separate investigator tools from harness controls. No arbitrary shell,
  unrestricted files, answer keys, or fault-control endpoints.
- Audit requests/results and verify the exposed tool inventory.

**Exit:** an MCP client retrieves correlated live evidence; malformed requests fail
clearly and the investigator cannot retrieve the answer/control plane.

### Milestone 5: Hermes, skills, and budgeted investigation

- Establish provider/model access and a secure credential path before paid calls.
  The user verified sufficient credits; this agent has not inspected the account.
- Pin Hermes and validate its API/events/MCP/skill behavior behind an application
  adapter. Use an isolated profile with incident tools and procedure reads only.
- Disable broad terminal/filesystem access and autonomous skill/memory changes.
  Start with triage and error/latency procedures; add resource, remediation, and
  report procedures as those flows develop. Do not encode scenario answers.
- Let the agent choose queries and test competing explanations. Validate output,
  evidence references, and incomplete/error states in deterministic code.
- Track the $100 project ceiling across development, retries, tuning, and evals.
  Apply conservative admission estimates, in-flight reservations, per-run
  turn/token/time limits, and reconciliation with actual usage. Estimates alone
  do not guarantee an exact provider billing cap; document practical limits.
- Record actual provider/model/settings, prompt/skill/tool versions, transcript,
  usage, and latency. Freeze skills and use fresh sessions for controlled evals.

**Exit:** a live CLI diagnosis cites collected evidence; missing/contradictory data
and exhausted budget/iterations produce honest visible outcomes.

### Milestone 6: API, storage, and streaming

- Add FastAPI incident/run lifecycle, cancellation, validated results, and errors.
- Persist incidents, observations, ordered events, calls, public hypotheses, skill
  versions, proposals/decisions, actions, usage, and scores via SQLite/SQLAlchemy.
- Translate Hermes events into application-owned SSE. Reconnect/reload must not
  restart tools or lose evidence. Keep credentials server-side.
- Represent interrupted runs honestly and retain event history for audit/playback.

**Exit:** real state/evidence survive reload and reconnect without duplicate work
or falsely completed runs.

### Milestone 7: Incident Console and evidence inspection

- Build the Next.js/React/TypeScript console: alert/status, dependencies, timeline,
  tool activity, assessment, and clickable evidence from the real API.
- Show concise public hypotheses, supporting/contradicting evidence, and missing
  checks. Explain observations versus inferences without private reasoning.
- Make query windows/provenance inspectable. Treat telemetry as untrusted text.
- Handle loading/empty/partial/failed/cancelled states; establish keyboard access,
  readable layout, and responsive behavior.

**Exit:** a user can trace claims to observations and understand uncertainty.

### Milestone 8: approval and controlled remediation

- Add typed proposal and approved-execution entry points with predefined lab actions.
  Present exact parameters and expected effect before the human decision.
- Bind approval to incident/run, immutable proposal/parameters, decision, expiry,
  and one-time execution state. Validate at the execution boundary.
- Test direct calls, missing/expired/forged/wrong-incident authorization, changed
  proposals, rejection, replay, retries, and concurrency.
- Keep harness setup/reset separate. Neither model output nor telemetry can grant
  approval or expand tool authority. Accept no caller-supplied shell commands.

**Exit:** only valid approved actions execute; duplicate requests cannot execute
the same proposal twice and invalid paths fail.

### Milestone 9: recovery and post-incident report

- Gather fresh telemetry after action and compare declared healthy/incident windows.
  Account for Kafka backlog drain and memory-leak reset behavior.
- Distinguish recovered, not recovered, and unverified. Show pre/post observations
  beside the action result and assessment.
- Report impact, timeline, supported cause, human decision, executed action,
  observed recovery, uncertainty, and remaining follow-ups.
- Verify the critical UI flow from alert through decision/action/recovery.

**Exit:** successful and unsuccessful/unverified recovery are demonstrated; action
completion is not presented as proof of system health.

### Milestone 10: evaluations and diagnosis challenges

- Extend the runner with isolated live setup/reset, fresh sessions, deterministic
  graders, and durable artifacts. Label live, recorded, and fixture modes.
- Compare the same model/tools/settings without skills and with versioned skills;
  keep the deterministic starter as a separate reference.
- Cover four faults, healthy operation, missing evidence, and malicious log content.
  Test approval enforcement independently of model cooperation.
- Add evidence removal, plausible unrelated changes, and at least one validated
  paired case with similar symptoms but different causes. Do not call an
  unvalidated fixture a live fault or fabricate missing observability.
- Grade cause/causal and impacted service, citation support, required evidence,
  skill selection, repeated calls, forbidden actions, recovery, latency, and cost.
  Evidence-ID existence alone does not prove support.
- Predeclare trials using pricing, pilot usage, and remaining budget. Report counts,
  failures, incomplete runs, and uncertainty. Tune on development cases, then freeze
  final comparison inputs. Do not select only successful trials.

**Exit:** reproducible comparison artifacts expose failures and when the investigator
revises/abstains, without invented improvement claims.

### Milestone 11: Eval Dashboard and Skills screen

- Display baseline/skills comparisons, scenario counts, safety failures, evidence
  quality, calls, latency, usage/cost, trial conditions, and limitations.
- Inspect failed runs through their evidence, calls, decisions, and scores.
- Show skill description/trigger, version/hash/commit, changes, and associated evals.
  Label incomparable or insufficient before/after experiments honestly.

**Exit:** all three core screens use stored application data and expose results,
failures, and version history clearly.

### Milestone 12: application hardening and reproducibility

- Add labeled recorded playback that cannot trigger inference or action execution.
- Verify clean setup and the complete alert-to-recovery/eval flows. Finish
  accessibility, responsive, error, interruption, and budget-limit states.
- Run relevant backend, adapter, MCP, policy, API, and critical UI checks.
- Document actual results, versions, resources, limitations, and component ownership.
  Explain application work separately from Hermes/OpenTelemetry capabilities.
- Include architecture and an optional short project walkthrough. Portfolio website
  construction and a separate portfolio case study are outside this scope.

**Exit:** a new developer can reproduce four live fault investigations and inspect
evidence, decisions, recovery, and evaluations from documented steps.

## Recommended technology and boundaries

Retain the reference architecture: Next.js/React/TypeScript/Tailwind/shadcn/ui;
FastAPI/Pydantic; Hermes behind an adapter; Python MCP; OpenTelemetry demo/backends;
SQLite/SQLAlchemy; JSON/YAML scenarios and code-based graders; Docker Compose;
Pytest and focused UI checks. Preserve the starter's unittest checks.

The full three screens remain; there is no schedule-driven cut. Hermes is the
proposed runtime, not a separately confirmed user mandate. Verify fit before
integration and surface any necessary architecture change explicitly.

Exclude extra agents, a vector database, production cloud/telemetry credentials,
arbitrary terminal execution, autonomous skill edits, Kubernetes, authentication,
multi-organization features, and cloud hosting from the initial build. AI-specific
faults and PostgreSQL are later options when justified.

## Verified facts and references

WSL package 3.0.3.0 and Ubuntu using WSL 2 are verified. Docker Desktop 4.30.0 and
Compose 2.27.0 are installed; the engine was stopped. Windows reports 15.69 GiB
physical RAM; available disk is about 290.65 GiB on G: and 87.98 GiB on C:.
A live full-stack capacity test has not run. See the environment record.

The user checked the billing dashboard and confirmed sufficient credits for the
$100 ceiling. This is user-reported verification, not agent inspection. Provider,
model, and credential setup must be established before paid integration. Keep
private balances, account identifiers, screenshots, and keys out of the repository.

Primary references checked during planning:

- [OpenTelemetry Docker deployment](https://opentelemetry.io/docs/demo/docker-deployment/):
  documented resources/full Compose behavior; minimal mode excludes Kafka.
- [OpenTelemetry fault reference](https://opentelemetry.io/docs/demo/feature-flags/):
  `paymentUnreachable` changes a checkout-side address; validate all fault behavior.
- [Hermes API](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server)
  and [skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills):
  HTTP/SSE and procedure controls; restrict the actual runtime capabilities.

The original plan's job-market and issue-specific claims were not revalidated;
they are not evidence of application quality or recruiting outcomes.

## Completion standard

A new developer can reproduce the application; four live faults are investigated
with supported evidence; healthy, ambiguous, missing, and adversarial cases are
handled honestly; no action bypasses approval; fresh telemetry verifies recovery;
comparisons report actual trials, failures, versions, and usage; and the UI/docs
match demonstrated behavior. Add milestones if needed to meet these conditions.
Until then, describe the project as in progress.
