# Development environment observations

Inspected November 2, 2026 (America/Los_Angeles), with read-only local commands.
These observations do not establish that the complete planned stack runs or fits.

| Component | Verified observation |
| --- | --- |
| Physical memory reported by Windows | 15.69 GiB; user describes the machine as 16 GB |
| G: free space | 290.65 GiB; project checkout is on G: |
| C: free space | 87.98 GiB; Docker data placement not yet verified |
| WSL package | 3.0.3.0 |
| WSL kernel | 6.18.54.1-1 |
| Default WSL distribution version | 2 |
| Ubuntu | Running, WSL version 2 |
| docker-desktop | Stopped, WSL version 2 |
| docker-desktop-data | Stopped, WSL version 2; currently the default distribution |
| Docker Desktop installed executable | 4.30.0.149282 |
| Docker CLI | 26.1.1, Windows amd64 client |
| Docker Compose | v2.27.0-desktop.2 |
| Docker engine | Unavailable: engine-pipe connection failed |

The WSL package version 3.0.3.0 and a distribution's WSL 2 execution mode describe
different things. Ubuntu is confirmed to use WSL 2.

Restricted checks could not enumerate distributions/read Docker config. Read-only
checks with the required access returned these observations. Engine connection
still failed with that access. No Docker or WSL configuration was changed.

## Milestone 1 follow-up

- Start/verify the Docker Linux engine as part of the requested lab work.
- Explicitly select Ubuntu for WSL commands; the default is a Docker data distro.
  Do not silently change the user's default.
- Pin the demo and check Compose/API requirements before deciding on any upgrade.
- Verify Docker data placement/limits; free G: space does not automatically expand
  a virtual disk stored on C:.
- Measure actual lab/application resource use. No live load test has run.

## API access

The user authorizes a $100 total project API ceiling and reports checking adequate
credits in the billing dashboard. The agent's available browser required sign-in;
the account balance was not independently inspected. No paid requests, purchases,
or billing changes were made.

Keep private balances, credentials, billing screenshots, and account identifiers
out of this repository. Record only project budget/usage controls and readiness.
