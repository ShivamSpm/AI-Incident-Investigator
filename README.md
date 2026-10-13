# AI Incident Investigator

**Status: In progress — initial Python baseline and evaluation scaffold.**

An ongoing project to build an AI agent that investigates service failures by
correlating logs, metrics, traces, and service dependencies. The intended product
will return evidence-linked diagnoses and support human-approved remediation.

This first milestone is a small, runnable foundation. It uses synthetic incident
fixtures and deterministic rules; it does **not** make LLM calls or use Hermes,
MCP, OpenTelemetry, or a web frontend yet. The baseline establishes a structured
output format and repeatable checks for the future agent.

## What works today

- A Python CLI that investigates a sample checkout/payment incident.
- Small read-only functions for retrieving logs, failed spans, and dependencies.
- Structured JSON output with a hypothesis, evidence IDs, and next steps.
- An inconclusive result when supporting evidence is missing.
- A versioned `SKILL.md` procedure prepared for future agent integration.
- Three deterministic evaluation cases and focused regression tests.
- No action execution, network access, API keys, or third-party dependencies.

## Run locally

Requirements: Python 3.10 or newer. Run commands from the repository root.
On macOS/Linux, use `python3` if `python` is unavailable.

```bash
python main.py
python main.py --incident healthy
python main.py --incident insufficient-evidence
python -m evals.run
python -m unittest discover -s tests -v
```

The default incident contains a checkout error-rate alert, a connection-refused
log, and a failed span referencing the payment dependency. The baseline returns
`suspected`, names `payment`, and cites `log-001` and `trace-001`. This supports an
unreachable dependency hypothesis; it does not establish whether a stopped
service, bad endpoint, or network configuration is the underlying cause.

## Starter layout

| File | Purpose |
| --- | --- |
| `main.py` | Run a sample investigation and print JSON |
| `investigator.py` | Output contract, read-only tools, and deterministic baseline |
| `data/incidents.json` | Synthetic observations without expected answers |
| `skills/incident-triage/SKILL.md` | Investigation procedure, version 0.1.0 |
| `evals/expectations.json` | Expected outcomes, kept separate from observations |
| `evals/run.py` | Evaluate outputs, evidence IDs, and absence of executed actions |
| `tests/test_investigator.py` | Regression checks for evidence and input handling |

## Planned architecture

React/TypeScript UI -> FastAPI application -> Hermes agent -> typed MCP tools ->
OpenTelemetry demo and telemetry backends.

The application will own incident state, evidence storage, and approval checks.
The agent will choose investigation tools and relevant skills. Remediation will
use predefined actions enforced by application code, rather than arbitrary shell
commands. The CLI and eval runner will use the same investigation interface.

## Roadmap

- [x] Build a deterministic baseline with structured output.
- [x] Separate synthetic observations from expected evaluation answers.
- [x] Add an initial operational skill and regression checks.
- [ ] Connect Hermes to the investigation interface and load versioned skills.
- [ ] Expose investigation tools through MCP.
- [ ] Replace synthetic fixtures with observations from the OpenTelemetry demo.
- [ ] Add FastAPI endpoints, persisted runs, and a React/TypeScript console.
- [ ] Add explicit approval checks and allowlisted remediation actions.
- [ ] Compare baseline and agent performance across multiple trials.
- [ ] Record diagnosis accuracy, evidence quality, tool usage, latency, and cost.

## Evaluation limits

The included evaluations are starter checks on three synthetic cases, not an AI
benchmark or a measure of production performance. Future agent evaluations must
keep ground truth out of the model context, use fresh sessions, record model and
skill versions, and repeat trials. Prompt-injection and approval-boundary tests
will be added when an LLM and executable action tools are integrated.

## Next implementation step

Keep `investigate(incident)` and the `InvestigationResult` contract stable. Add a
Hermes-backed implementation, then compare it with this baseline using the same
evaluation cases. Extend the cases before tuning prompts or skills.
