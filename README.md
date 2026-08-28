<img src="images/cover.png" alt="Claude Architect Foundations cover" width="400">

# Claude Architect Foundations - O'Reilly Live Training

[![Website TechTrainerTim.com](https://img.shields.io/badge/Website-TechTrainerTim.com-0a66c2)](https://techtrainertim.com)
[![LinkedIn timothywarner](https://img.shields.io/badge/LinkedIn-timothywarner-0a66c2?logo=linkedin)](https://www.linkedin.com/in/timothywarner/)
[![GitHub timothywarner-org](https://img.shields.io/badge/GitHub-timothywarner--org-181717?logo=github)](https://github.com/timothywarner-org)
[![O'Reilly Author Page](https://img.shields.io/badge/O'Reilly-Author%20Page-cf2f1d)](https://learning.oreilly.com/search/?query=Tim%20Warner)
[![YouTube TechTrainerTim](https://img.shields.io/badge/YouTube-TechTrainerTim-ff0000?logo=youtube&logoColor=white)](https://www.youtube.com/c/TechTrainerTim)
[![Microsoft MVP 2026](https://img.shields.io/badge/Microsoft%20MVP-2026-blueviolet?logo=microsoft&logoColor=white)](https://mvp.microsoft.com/en-us/PublicProfile/5004754)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Contact:** [Website](https://techtrainertim.com) | [LinkedIn](https://www.linkedin.com/in/timothywarner/) | [GitHub](https://github.com/timothywarner-org) | [O'Reilly](https://learning.oreilly.com/search/?query=Tim%20Warner) | [YouTube](https://www.youtube.com/c/TechTrainerTim)

---

Reference architectures, code examples, and practice scenarios for the **Claude Architect** role. This 4-hour O'Reilly Media live training is **skills-first** for Segments 1-3, then closes with a **CCA-F certification capstone** in Segment 4 (cert briefing + weighted practice questions). It teaches the production patterns that define a Claude Architect (agentic orchestration, tool design with MCP, Claude Code workflows, prompt engineering, context management) and gives you a runway to Anthropic's CCA-F exam.

> Anthropic's **Claude Certified Architect: Foundations (CCA-F)** exam is currently restricted to Anthropic partners. The five reference files in this repo map to the published 5-domain exam blueprint, and [`CERT-PROGRAM-BRIEFING.md`](./docs/CERT-PROGRAM-BRIEFING.md) walks through exam mechanics, prep stack, and a week-before punchlist.

> **New: [`EXAM-STUDY-PATH.md`](./docs/EXAM-STUDY-PATH.md)** is the learner-facing bridge from this workshop's notebooks to CCA-F domains and scenario families. Read it after the course-at-a-glance table below if you are aiming at the exam.

## What is a Claude Architect?

The Claude Architect is an emerging job role focused on designing and building production-grade applications with **Claude Code**, the **Claude Agent SDK**, the **Claude API**, and **Model Context Protocol (MCP)**. Organizations across the Claude Partner Network are hiring for this skillset.

## Course at a glance

| Segment | Duration | Topic | Key deliverable |
|---|---|---|---|
| 1 | 50 min | Building AI Agents That Use Tools | Customer support agent with hook-enforced policy |
| 2 | 50 min | Tool Design, Integration, and Claude Code Workflows | MCP config walkthrough + Claude Code hierarchy demo |
| **2.5** | *self-study* | **Control Surfaces, Tool Enumeration, Console Assets** | **All `tool_choice` modes live, `stop_sequences` / `max_tokens` / `pause_turn`, MCP `list_tools`, and the live Claude Console asset surface (`memory_stores`, `vaults`, `agents`, `sessions`). Q&A overflow / cohort homework, not on the 4-hour clock.** |
| 3 | 50 min | Structured Output, Context, and Production Reliability | Invoice extractor with retry + triage scorecard |
| 4 | 50 min | CCA-F Certification Capstone | Cert briefing + 10 weighted practice questions + take-home punchlist |

Total live class time: 4 hours (4 × 50-min segments + 3 × 10-min breaks). Segment 2.5 is a deep-dive notebook taught only as Q&A overflow or post-class homework. Instructors and learners should start at **[COURSE-FLOW.md](./COURSE-FLOW.md)**.

## CCA-F exam blueprint (the five core competencies)

| Domain | Weight | Reference file | Focus |
|---|---|---|---|
| 1 - Agentic Architecture & Orchestration | **27%** | [domain-1-agentic.md](./docs/domain-1-agentic.md) | Agentic loops, multi-agent coordination, hooks, session management |
| 2 - Tool Design & MCP Integration | 18% | [domain-2-tools-mcp.md](./docs/domain-2-tools-mcp.md) | Tool descriptions, structured errors, scoped distribution, MCP config |
| 3 - Claude Code Configuration & Workflows | 20% | [domain-3-claude-code.md](./docs/domain-3-claude-code.md) | CLAUDE.md hierarchy, skills, slash commands, plan mode, CI/CD |
| 4 - Prompt Engineering & Structured Output | 20% | [domain-4-prompts.md](./docs/domain-4-prompts.md) | Explicit criteria, few-shot prompting, JSON schemas via tool use, batch API |
| 5 - Context Management & Reliability | 15% | [domain-5-context.md](./docs/domain-5-context.md) | Context preservation, escalation, error propagation, provenance |

**Exam mechanics:** 60 multiple-choice questions, 120 minutes, scaled 100-1000 with **720 passing**, proctored via ProctorFree, **one attempt only**, $99 (partner discount available). See [`CERT-PROGRAM-BRIEFING.md`](./docs/CERT-PROGRAM-BRIEFING.md) for the full briefing.

## Repository layout

```text
claude-architect/
├── COURSE-FLOW.md              # Master instructor punchlist (4 segments × 50 min)
├── docs/                       # Reference scaffolds and instructor/learner guides (moved out of repo root)
│   ├── INSTRUCTOR-SETUP.md         # Multi-day setup arc (machine config, env vars, repo clone, backup plans)
│   ├── PRE-CLASS-CHECKLIST.md      # Instructor pre-flight (PowerShell)
│   ├── EMERGENCY-CARD.md           # One-page live-class recovery card (what to do when a demo goes sideways)
│   ├── CERT-PROGRAM-BRIEFING.md    # Segment 4 talk-track: exam mechanics, domain weights, week-before punchlist
│   ├── EXAM-STUDY-PATH.md          # Learner-facing bridge from notebooks to CCA-F domains and scenarios
│   ├── PRACTICE-QUESTIONS.md       # 60-question practice bank, hand-maintained (cohort take-home)
│   ├── COOKBOOK-INDEX.md           # Index of the vendored Anthropic cookbook notebooks cited by the course
│   ├── scenario-cicd-integration.md # Exam scenario 5: `claude -p` headless in a GitHub Actions PR review
│   ├── domain-1-agentic.md         # Reference: Agentic Architecture & Orchestration
│   ├── domain-2-tools-mcp.md       # Reference: Tool Design & MCP Integration
│   ├── domain-3-claude-code.md     # Reference: Claude Code Configuration & Workflows
│   ├── domain-4-prompts.md         # Reference: Prompt Engineering & Structured Output
│   └── domain-5-context.md         # Reference: Context Management & Reliability
├── practice-questions.json     # Machine-readable practice-question source
├── .mcp.json                   # Segment 2 Demo A anchor (6 servers, 3 transports; the course's own server is `oreilly-cca-mcp`)
├── .vscode/mcp.json            # VS Code / GitHub Copilot agent-mode MCP config (sibling schema to .mcp.json)
├── hooks-example.py            # Agent SDK hooks: compliance enforcement
├── coordinator-subagent-sketch.py  # Domain 1 coordinator-subagent scaffold (read-only reference)
├── start-sidecar-group.ps1     # Brings up the teaching sidecars (JupyterLab, MCP Inspector, MCP CLI REPL); idempotent
├── stop-sidecar-group.ps1      # Takes the same sidecars back down
├── CLAUDE.md                   # Claude Code project instructions for this repo
├── notebooks/                  # Tim's seven teaching notebooks (five live + one self-study deep dive + one exam-mastery reference), plus two self-paced suites
│   ├── segment-0-pre-flight.ipynb
│   ├── segment-1-customer-support-agent.ipynb
│   ├── segment-2-tool-design-and-mcp.ipynb
│   ├── segment-2-5-control-surfaces.ipynb     # self-study; control surfaces + Console assets
│   ├── segment-3-invoice-extractor.ipynb
│   ├── segment-4-cca-f-capstone.ipynb
│   ├── cca-f-exam-mastery.ipynb               # off-clock; all five domains, all 30 task statements
│   ├── 00-prerequisites/                      # 10 Messages API primer notebooks - the on-ramp to the raw API
│   └── 06-managed-agents/                     # 6 Managed Agents notebooks - Anthropic hosts the loop, domain-banded
├── claude-cookbooks-main/      # Vendored snapshot of Anthropic's official Claude Cookbooks (MIT, Copyright (c) 2023 Anthropic). See claude-cookbooks-main/NOTICE.md
├── examples/                   # One runnable example suite (self-paced study, not on the 4-hour clock)
│   └── mcp_cli/                # Reference MCP CLI (FastMCP server + client + chat), from Anthropic's Skilljar course. See examples/mcp_cli/NOTICE.md
├── slides/                     # Course slide deck (rebuilt from scripts/build-deck.py)
└── scripts/
    ├── build-notebooks.py                 # Rebuilds the seven teaching notebooks from source (sha256-deterministic, idempotent)
    ├── preflight-class.ps1                # Read-only go/no-go board for class day. Exit 0 = GO. Changes nothing
    ├── run-jupyter.ps1                    # Lifecycle helper: starts JupyterLab on port 8888 with Jupyter AI v3 persona override
    ├── stop-jupyter.ps1                   # Lifecycle helper: port-scoped clean shutdown with PID fallback for Windows half-states
    ├── run-mcp-cli.ps1                    # Lifecycle helper: bootstraps and starts the vendored MCP CLI REPL
    ├── run-mcp-inspector.ps1              # Lifecycle helper: starts the MCP Inspector against the FastMCP demo server
    ├── smoke-cookbooks.ps1                # Smoke-runs the 8 heavy-rotation vendored cookbooks against notebooks/.venv
    ├── voice-lint.ps1                     # Voice-lint sweep (no em dashes, no AWS, etc.) - run via `npm run lint:voice`
    ├── preflight.ps1                      # Instructor pre-flight - run via `npm run preflight`
    ├── build-deck.py                      # Rebuilds the slide deck
    └── extract-practice-questions.py      # RETIRED extractor (practice-question files are now hand-maintained)
```

## Getting started

### Prerequisites

- [**Python**](https://www.python.org/) 3.13+ (every notebook and demo in this course runs against the Python [`anthropic`](https://pypi.org/project/anthropic/) SDK, pinned `>=0.40,<1.0` in [`notebooks/pyproject.toml`](./notebooks/pyproject.toml))
- [**uv**](https://docs.astral.sh/uv/) (the Python package manager): `pip install uv` or `winget install astral-sh.uv`
- [Claude Code CLI](https://docs.claude.com/en/docs/claude-code) installed and authenticated. On Windows the native installer is the fastest path: `irm https://claude.ai/install.ps1 | iex`
- An [Anthropic API key](https://console.anthropic.com/) set as `ANTHROPIC_API_KEY` (PowerShell: `$env:ANTHROPIC_API_KEY = "sk-ant-..."`, or place it in a gitignored `.env` at repo root)
- **VS Code** with the **Python** and **Jupyter** extensions (the seven teaching notebooks open here)
- Optional, instructors only: [Node.js](https://nodejs.org/) 18+ for the two npm scripts ([`npm run lint:voice`](./scripts/voice-lint.ps1), [`npm run preflight`](./scripts/preflight.ps1)). Learners can skip Node entirely.

### Setup (on-rails, one command)

```powershell
git clone https://github.com/timothywarner-org/claude-architect.git
cd claude-architect
uv run --project notebooks jupyter lab notebooks/
```

That is the entire learner setup. **First run** auto-creates `notebooks/.venv/`, installs all dependencies from `notebooks/pyproject.toml`, and launches Jupyter. **Subsequent runs** reuse the venv and start in seconds. The Anthropic cookbook ships in the repo at `claude-cookbooks-main/`, so you don't need a second clone. Instructors who run the voice-lint scripts also need `npm install`; learners don't.

**Fallback** if `uv` isn't available: `pip install -r notebooks/requirements.txt` still works; the requirements file is kept in sync with `pyproject.toml`.

**Interactive teaching sessions** should use the lifecycle helpers instead of a bare Jupyter invocation:

```powershell
.\scripts\run-jupyter.ps1            # default port 8888, overrides Jupyter AI default persona to Jupyternaut
.\scripts\stop-jupyter.ps1           # port-scoped clean shutdown with PID fallback
```

`run-jupyter.ps1` sets the Jupyter AI v3 default persona to Jupyternaut so chat messages route to someone (the upstream default points at the older package ID and silently routes to nobody). `stop-jupyter.ps1` matches the server by `root_dir`, falls back to `Stop-Process` on the exact PID if the graceful path hangs (Jupyter AI can leave the server half-interrupted on Windows). For headless smoke runs (`nbconvert --execute`) neither script is needed - nbconvert spawns its own kernel.

### Class day: pre-flight and sidecars

Three scripts cover the live-teaching lifecycle. Run them in this order:

```powershell
.\scripts\preflight-class.ps1        # read-only go/no-go board. Exit 0 = GO
.\start-sidecar-group.ps1            # brings the teaching sidecars up
.\stop-sidecar-group.ps1             # takes them back down
```

[`scripts/preflight-class.ps1`](./scripts/preflight-class.ps1) is **read-only and changes nothing**. It checks tooling, secrets, both venvs, the `claude-architect` kernelspec, both MCP configs, that all seven notebooks parse, and that the ports it needs are free. An exit code of 0 means you're clear to teach.

[`start-sidecar-group.ps1`](./start-sidecar-group.ps1) brings up the three teaching sidecars: **JupyterLab**, the **MCP Inspector**, and the **MCP CLI REPL**. It's **idempotent**, so it skips any sidecar that's already running rather than starting a second copy. Four flags shape what it does: `-Restart` cycles everything, `-SkipPreflight` bypasses the go/no-go check, `-NoMcpCli` leaves the REPL out, and `-NoJupyter` skips the JupyterLab server. **If you teach from VS Code rather than JupyterLab, `-NoJupyter` is the flag you want** - the VS Code Jupyter extension spawns its own kernel and never talks to a JupyterLab server, so starting one just burns a port. [`stop-sidecar-group.ps1`](./stop-sidecar-group.ps1) takes the same set back down.

When a demo goes sideways mid-class, [`docs/EMERGENCY-CARD.md`](./docs/EMERGENCY-CARD.md) is the one-page recovery card. Keep it open on a second monitor.

### The `notebooks/` self-paced suites (off the 4-hour clock)

[`notebooks/`](./notebooks/) is the unified course tree: the seven live-taught segment notebooks at its root, plus two self-paced suites that bookend them - an on-ramp for people new to the raw API and a managed-agents counterpart to the loops the course hand-rolls. [`examples/`](./examples/) now holds only the standalone [`mcp_cli/`](./examples/mcp_cli/) reference app, a separate vendored uv project. None of the self-paced material is on the 4-hour clock, and all of it is runnable.

#### `notebooks/00-prerequisites/` - the API on-ramp

If you've never called the Claude API directly, **start here, before Segment 1**. Ten notebooks in [`notebooks/00-prerequisites/`](./notebooks/00-prerequisites/) walk the Messages API one concept at a time: `001_requests`, `002_system_prompt`, `003_temperature`, `004_streaming`, and `005_controlling_output`, with `_exercise` variants of 001, 002, and 005 for hands-on reps, plus [`first_request.ipynb`](./notebooks/00-prerequisites/first_request.ipynb) and [`multi_turn_conversation.ipynb`](./notebooks/00-prerequisites/multi_turn_conversation.ipynb) as the two bookends. They're adapted from [jaozc/building-with-the-claude-api](https://github.com/jaozc/building-with-the-claude-api), and every one of them is smoke-verified green against the live API. They request the `claude-architect` kernel, so once the notebook venv exists they open and run without any further setup.

#### `notebooks/06-managed-agents/` - Anthropic hosts the loop

The live course teaches you to **hand-roll the agentic loop**, because you can't reason about a loop you've never written. The six notebooks in [`notebooks/06-managed-agents/`](./notebooks/06-managed-agents/) are the counterpart: the same patterns, but with Anthropic running the loop for you through the **Managed Agents** beta (`anthropic-beta: managed-agents-2026-04-01`). They're banded by exam domain:

| Notebook | Domain focus |
|---|---|
| [`01_agentic_loop_and_sessions`](./notebooks/06-managed-agents/01_agentic_loop_and_sessions.ipynb) | Domain 1: the managed loop and session lifecycle |
| [`02_coordinator_and_subagents`](./notebooks/06-managed-agents/02_coordinator_and_subagents.ipynb) | Domain 1: multi-agent coordination |
| [`03_tools_and_structured_errors`](./notebooks/06-managed-agents/03_tools_and_structured_errors.ipynb) | Domain 2: tool design and structured errors |
| [`04_structured_output_and_validation`](./notebooks/06-managed-agents/04_structured_output_and_validation.ipynb) | Domain 4: schema-guaranteed output |
| [`05_context_and_escalation`](./notebooks/06-managed-agents/05_context_and_escalation.ipynb) | Domain 5: context preservation and escalation |
| [`06_cca_f_capstone`](./notebooks/06-managed-agents/06_cca_f_capstone.ipynb) | All five domains end to end |

All six are smoke-verified green, and **all six archive the resources they create**, so a full run leaves nothing behind in your Console workspace. Read them after the live segments, not before - the managed loop is much easier to trust once you've written the unmanaged one.

#### `examples/mcp_cli/` - the MCP reference app (one command)

The vendored [`examples/mcp_cli/`](./examples/mcp_cli/) Skilljar reference app gets the same on-rails treatment via a wrapper that auto-bootstraps its `.env` and hands off to `uv`:

```powershell
.\scripts\run-mcp-cli.ps1
```

First run creates `examples/mcp_cli/.env` from the template, lifts `ANTHROPIC_API_KEY` from your repo-root `.env`, and then runs `uv run --directory examples/mcp_cli main.py`. Subsequent runs go straight to the REPL. The wrapper sits in [`scripts/run-mcp-cli.ps1`](./scripts/run-mcp-cli.ps1) and never touches the vendored `examples/mcp_cli/` tree, preserving the NOTICE.md modification count at 2. Its FastMCP server is what [`.mcp.json`](./.mcp.json) registers as **`oreilly-cca-mcp`**, and it's the server [`scripts/run-mcp-inspector.ps1`](./scripts/run-mcp-inspector.ps1) points the MCP Inspector at.

### Recommended learning path

0. **New to the Claude API?** Run [`notebooks/00-prerequisites/`](./notebooks/00-prerequisites/) first. Ten short notebooks take you from a bare request to streaming and controlled output, which is the vocabulary every later segment assumes.
1. **Read [COURSE-FLOW.md](./COURSE-FLOW.md)** for the full 4-segment teaching arc.
2. **Walk the five `domain-*.md` reference files** in order. Each maps to a course segment and points at runnable cookbook notebooks.
3. **Run the five live-teaching notebooks in [`notebooks/`](./notebooks/)** in order, plus the [`segment-2-5-control-surfaces.ipynb`](./notebooks/segment-2-5-control-surfaces.ipynb) self-study deep dive when time allows. These are the primary teaching surface - markdown cells carry the concepts, code cells run the demos, and each one closes with a **"Going further"** appendix that links the rest of the repo's assets. Anthropic's official cookbooks ship alongside in [`claude-cookbooks-main/`](./claude-cookbooks-main/) as the bundled-in reference library (full attribution in [`claude-cookbooks-main/NOTICE.md`](./claude-cookbooks-main/NOTICE.md)).
4. **Then run [`notebooks/06-managed-agents/`](./notebooks/06-managed-agents/).** Once you've hand-rolled an agentic loop in Segment 1, these six notebooks show you the same patterns with Anthropic managing the loop. The contrast is the lesson.
5. **Work through [`CERT-PROGRAM-BRIEFING.md`](./docs/CERT-PROGRAM-BRIEFING.md)** and the [`PRACTICE-QUESTIONS.md`](./docs/PRACTICE-QUESTIONS.md) bank if you're aiming at the CCA-F exam.
6. **Build something.** The reference architectures only land when you wire one of these patterns into a real workflow.

## Practice scenarios (CCA-F exam pool)

Each scenario frames a realistic production context that a Claude Architect would encounter. The CCA-F exam draws **4 scenarios at random from a pool of 6**:

| # | Scenario | Primary competencies |
|---|---|---|
| 1 | Customer Support Resolution Agent | Domains 1, 2, 5 |
| 2 | Code Generation with Claude Code | Domains 3, 5 |
| 3 | Multi-Agent Research System | Domains 1, 2, 5 |
| 4 | Developer Productivity Tooling | Domains 1, 2, 3 |
| 5 | CI/CD Integration with Claude Code | Domains 3, 4 |
| 6 | Structured Data Extraction Pipeline | Domains 4, 5 |

## Key concepts quick reference

### Agentic loop

```text
Send request -> Check stop_reason -> "tool_use"? Execute tool, append tool_result, loop
                                  -> "end_turn"? Done
                                  -> "pause_turn"? Resume in next request
```

### Tool selection

- **Descriptions drive selection.** Detailed descriptions beat clever tool names.
- **Cap at 4-5 tools per agent.** More tools degrade selection accuracy.
- **Structured errors as tool_result content.** Never raise exceptions from tool implementations.

### `tool_choice` modes (Segment 2.5)

| Mode | Forces what? | When to pick |
|---|---|---|
| `{"type": "auto"}` | nothing | default |
| `{"type": "any"}` | a tool call (model picks which) | action required, model picks verb |
| `{"type": "tool", "name": "X"}` | call to tool X | forced structured output (Segment 3) |
| `{"type": "none"}` | no tool calls | "explain, don't act" turns |
| add `disable_parallel_tool_use: true` | one tool per turn | ordering matters (write-then-read, lookup-then-act) |

### Stop conditions (Segment 2.5)

Branch on `stop_reason`, never parse prose to decide control flow. Six values: `end_turn`, `tool_use`, `max_tokens`, `stop_sequence`, `pause_turn`, `refusal`. `stop_sequences` gives you a deterministic cutoff token (matched value comes back in `resp.stop_sequence`, the token itself is excluded from the output). `max_tokens` doubles as a deliberate cutoff lever: set it low, replay the partial assistant turn in the next call to resume.

### Tool enumeration, four lenses (Segment 2.5)

1. **Static** - iterate the `tools=[...]` array you registered
2. **Runtime loop** - log scoped tools + `tool_choice` per iteration
3. **MCP `list_tools`** - the pattern that scales beyond hand-registered tools
4. **Claude Code harness** - separate surface from API `tool_use`, discovered via `/help` and `~/.claude/`

### Claude Console asset surface (Segment 2.5)

All reachable from the SDK with `anthropic-beta: managed-agents-2026-04-01`:

- `client.beta.memory_stores` - persistence that survives restarts (Domain 5)
- `client.beta.vaults` (+ `.credentials.mcp_oauth_validate`) - secrets hygiene with MCP OAuth (Domain 3)
- `client.beta.agents` + `client.beta.sessions` - the managed-loop alternative to a hand-rolled agentic loop (Domain 1)

### Claude Code configuration

- **User-level** `~/.claude/CLAUDE.md` for personal defaults
- **Project-level** `./CLAUDE.md` at repo root for team conventions
- **Subtree** `<subdir>/CLAUDE.md` loads on demand
- **`claude -p`** for headless / CI/CD usage

### Structured output

- **`tool_use` with JSON schema = guaranteed schema compliance.** Define output as a tool's `input_schema`, force the model to call it with `tool_choice: {"type": "tool", "name": "..."}`.
- **Few-shot examples > temperature.** Two or three input-output pairs beat tuning sampling parameters.

### Prompt caching floors (gotcha)

`cache_control` silently no-ops if the cacheable prefix is below the model's floor. **Sonnet 4.x: 1024 tokens. Haiku 4.5: 4096 tokens (4x higher).** A cell can exit clean with `cache_creation=0` and `cache_read=0` if the prefix sits between the two floors; the smoke output, not the exit code, is what tells you caching engaged. Target +25% above the floor for safety margin against tokenizer drift.

### Model policy

- **Haiku 4.5 default everywhere.** Production-quality tool use, agentic loops, and MCP discovery at ~1/5 the Sonnet cost.
- **Sonnet 4.6 reserved** for two cells: Segment 3's nested invoice schemas with retry-on-validation-error, and the Part 4 forced-extraction cell of the off-clock `cca-f-exam-mastery.ipynb`.
- **Opus never used** in code in this repo. Console-managed agents carry their own configured model field (Deep Researcher resolves to Sonnet 4.6); the SDK respects what the Console sets.

### Context and reliability

- Pin case-facts at the top of long sessions
- Summarize resolved turns; keep verbatim history only for the active issue
- Escalate on explicit human request, policy gaps, or low confidence - never on sentiment alone

## About the instructor

**Tim Warner** is a Microsoft MVP (Azure AI), Pluralsight Principal Author (200+ courses, 1M+ learners), Microsoft Press / Pearson senior content developer, and O'Reilly Live Learning instructor with 28+ years on the Microsoft stack. He teaches Feynman-style: first principles, no fluff, real demos.

- Website: [TechTrainerTim.com](https://techtrainertim.com)
- LinkedIn: [@timothywarner](https://www.linkedin.com/in/timothywarner/)
- GitHub: [@timothywarner-org](https://github.com/timothywarner-org)
- YouTube: [TechTrainerTim](https://www.youtube.com/c/TechTrainerTim)
- O'Reilly: [Author page](https://learning.oreilly.com/search/?query=Tim%20Warner)

## Attribution and licensing

This repo bundles several distinct bodies of work. The split matters for attribution and for reuse:

- **Original content by Tim Warner.** Everything in [`notebooks/`](./notebooks/), including [`notebooks/06-managed-agents/`](./notebooks/06-managed-agents/), the five [`domain-*.md`](./docs/domain-1-agentic.md) reference files, [`COURSE-FLOW.md`](./COURSE-FLOW.md), [`CERT-PROGRAM-BRIEFING.md`](./docs/CERT-PROGRAM-BRIEFING.md), [`PRE-CLASS-CHECKLIST.md`](./docs/PRE-CLASS-CHECKLIST.md), [`INSTRUCTOR-SETUP.md`](./docs/INSTRUCTOR-SETUP.md), [`CLAUDE.md`](./CLAUDE.md), and everything under [`scripts/`](./scripts/) is authored by Tim Warner and licensed under MIT via this repo's [`LICENSE`](./LICENSE) file.
- **Vendored Anthropic content.** [`claude-cookbooks-main/`](./claude-cookbooks-main/) is a vendored copy of Anthropic's official [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks), MIT licensed, **Copyright (c) 2023 Anthropic**. Full attribution, upstream commit reference, and the unmodified MIT license live in [`claude-cookbooks-main/NOTICE.md`](./claude-cookbooks-main/NOTICE.md) and [`claude-cookbooks-main/LICENSE`](./claude-cookbooks-main/LICENSE). It is committed here so learners get the entire reference library on `git clone` without a second clone step.
- **Reference application from Anthropic's Skilljar course.** [`examples/mcp_cli/`](./examples/mcp_cli/) is a complete MCP CLI application (stdio FastMCP server + client + interactive chat with `@doc-id` retrieval and `/prompt-name` commands) distributed as starter material with Anthropic's [Claude with the Anthropic API](https://anthropic.skilljar.com/claude-with-the-anthropic-api/) Skilljar course. Treated as Anthropic-authored instructional reference; full attribution and the two minor modifications (rename `.env` to `.env.example`, add `NOTICE.md`) are documented in [`examples/mcp_cli/NOTICE.md`](./examples/mcp_cli/NOTICE.md). Segment 2 of the course opens its `mcp_server.py` source during Demo A.
- **Practice bank with split provenance.** In [`PRACTICE-QUESTIONS.md`](./docs/PRACTICE-QUESTIONS.md) the question stems, options, and correct answers are community-sourced from Paul Larionov's study repo; the answer explanations are this repo's own work, grounded in Anthropic documentation. The file is hand-maintained (see the [Disclaimer](#disclaimer) below for the full provenance and calibration-only framing).
- **Adapted community content.** The primer notebooks in [`notebooks/00-prerequisites/`](./notebooks/00-prerequisites/) are adapted from [jaozc/building-with-the-claude-api](https://github.com/jaozc/building-with-the-claude-api), with three portability fixes for this repo: the install cell shells out to `uv pip install` rather than `%pip` (uv venvs ship without pip), the model is pinned to `claude-haiku-4-5` per this repo's model policy, and the demo prompts are Azure-first. Attribution is in each notebook's first cell and in [`examples/README.md`](./examples/README.md). The managed-agents notebooks in [`notebooks/06-managed-agents/`](./notebooks/06-managed-agents/) are original work by Tim Warner and fall under this repo's MIT license.
- **Point-in-time snapshots, not submodules.** Both [`claude-cookbooks-main/`](./claude-cookbooks-main/) and [`examples/mcp_cli/`](./examples/mcp_cli/) are static snapshots, not git submodules. Refresh procedures are documented in each directory's `NOTICE.md`.

## Disclaimer

This is an **unofficial study guide** built around Anthropic's publicly documented CCA-F exam blueprint. Practice questions in [`PRACTICE-QUESTIONS.md`](./docs/PRACTICE-QUESTIONS.md) are community-sourced from [Paul Larionov's study repo](https://github.com/paullarionov/claude-certified-architect) and are intended for **calibration only**, not as exam predictors. The authoritative source for exam content, registration, and policy is **Anthropic** (see the [public CCA-F page](https://anthropic.skilljar.com/) and the Exam Policy). Use Anthropic's own Practice Exam to gauge readiness before scheduling.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT - see [LICENSE](LICENSE).

---

*Found this useful? Open an issue with questions or feedback - I read every one.*

## Exam access and registration

Registration runs through the Anthropic Partner Academy and requires affiliation with a Claude Partner Network organization; there is no individual sign-up. Exams are delivered by [Pearson VUE](https://www.pearsonvue.com/us/en/anthropic.html) (online proctored or at a test center), the fee is $125 per attempt as of the mid-2026 exam guide, and credentials are valid for 12 months with a free on-time renewal.

No partner organization? The routes in are an employer that joins the [Claude Partner Network](https://claude.com/partners), a qualifying company of your own, or membership in an existing partner firm ([how the partner-firm route works](https://youraidept.com/network/claude-certification) — disclosure: that guide is maintained by YAID, a partner firm).
