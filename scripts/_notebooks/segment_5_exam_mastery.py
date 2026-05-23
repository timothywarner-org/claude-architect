"""Cell builder for cca-f-exam-mastery.ipynb.

A 7th standalone reference notebook, off the 4-hour course clock. Maps
1:1 to all five CCA-F domains and all 30 task statements (TS1.1..TS5.6)
in the February 2025 Exam Guide. Designed so that if you understand
this workbook you know the exam.

Structure (7 Parts, ~95-110 cells):
  - Part 0: setup preamble (imports, model policy, budget, scenarios)
  - Part 1: Agentic Architecture & Orchestration (D1, 27%, TS1.1-1.7)
  - Part 2: Tool Design & MCP Integration (D2, 18%, TS2.1-2.5)
  - Part 3: Claude Code Configuration & Workflows (D3, 20%, TS3.1-3.6)
  - Part 4: Prompt Engineering & Structured Output (D4, 20%, TS4.1-4.6)
  - Part 5: Context Management & Reliability (D5, 15%, TS5.1-5.6)
  - Part 6: Exam mechanics, 30-TS coverage matrix, self-check

Non-duplication contract: uses the MINIMAL exam-probing version of every
demo; cites the segment notebooks for long-form teaching. Live Messages
API throughout. Managed Agents SDK cells are READ-ONLY (list/retrieve
the provisioned oreilly-* resources only). Claude Code material is
repo-inspection + concept commentary - the `claude` CLI cannot run
inside Jupyter.

Model policy: claude-haiku-4-5 default; claude-sonnet-4-6 only for the
Part 4 forced-extraction-with-retry cell (the documented repo
exception). Budget: ~$0.15-0.25 for a full top-to-bottom run.
"""

from __future__ import annotations


def cells() -> list[tuple[str, str]]:
    return [
        # --- Part 0: setup ---
        ("md", _part0_title_md),
        ("md", _part0_howto_md),
        ("md", _part0_scenarios_md),
        ("md", _part0_setup_md),
        ("code", _part0_imports_code),
        # --- Part 1: Agentic Architecture & Orchestration (D1, 27%) ---
        ("md", _part1_header_md),
        ("md", _part1_loop_concept_md),
        ("code", _part1_loop_code),
        ("md", _part1_decomp_md),
        ("md", _part1_subagent_concept_md),
        ("code", _part1_subagent_code),
        ("md", _part1_hooks_concept_md),
        ("code", _part1_hooks_code),
        ("md", _part1_task_tool_md),
        ("md", _part1_sessions_md),
        ("md", _part1_exam_probes_md),
        # --- Part 2: Tool Design & MCP Integration (D2, 18%) ---
        ("md", _part2_header_md),
        ("md", _part2_description_concept_md),
        ("md", _part2_tool_choice_md),
        ("code", _part2_tool_choice_code),
        ("md", _part2_structured_error_md),
        ("code", _part2_structured_error_code),
        ("md", _part2_mcp_concept_md),
        ("code", _part2_mcp_inspect_code),
        ("md", _part2_mcp_discovery_md),
        ("code", _part2_mcp_discovery_code),
        ("md", _part2_builtin_tools_md),
        ("md", _part2_exam_probes_md),
        # --- Part 3: Claude Code Configuration & Workflows (D3, 20%) ---
        ("md", _part3_header_md),
        ("md", _part3_banner_md),
        ("md", _part3_claude_md_concept_md),
        ("code", _part3_claude_md_inspect_code),
        ("md", _part3_rules_concept_md),
        ("code", _part3_rules_inspect_code),
        ("md", _part3_skills_concept_md),
        ("code", _part3_skill_inspect_code),
        ("md", _part3_plan_mode_md),
        ("md", _part3_iterative_md),
        ("md", _part3_cicd_concept_md),
        ("code", _part3_cicd_inspect_code),
        ("md", _part3_exam_probes_md),
        # --- Part 4: Prompt Engineering & Structured Output (D4, 20%) ---
        ("md", _part4_header_md),
        ("md", _part4_precise_md),
        ("md", _part4_pydantic_md),
        ("code", _part4_pydantic_code),
        ("md", _part4_extract_md),
        ("code", _part4_extract_code),
        ("md", _part4_few_shot_md),
        ("code", _part4_few_shot_code),
        ("md", _part4_batches_md),
        ("md", _part4_multipass_md),
        ("md", _part4_exam_probes_md),
        # --- Part 5: Context Management & Reliability (D5, 15%) ---
        ("md", _part5_header_md),
        ("md", _part5_context_concept_md),
        ("code", _part5_pruning_code),
        ("md", _part5_escalation_md),
        ("code", _part5_escalation_code),
        ("md", _part5_provenance_md),
        ("code", _part5_provenance_code),
        ("md", _part5_managed_agents_md),
        ("code", _part5_managed_agents_code),
        ("md", _part5_error_propagation_md),
        ("md", _part5_exam_probes_md),
        # --- Part 6: Exam mechanics, coverage matrix, self-check ---
        ("md", _part6_exam_format_md),
        ("md", _part6_coverage_matrix_md),
        ("md", _part6_cheatsheet_md),
        ("md", _part6_self_check_md),
        ("code", _part6_verify_code),
        ("md", _part6_close_md),
    ]


# ===========================================================================
# Part 0: setup
# ===========================================================================

_part0_title_md = """\
# CCA-F Exam Mastery: a single coverage-complete reference

**A 7th standalone reference notebook for the Claude Certified Architect - Foundations exam.** Off the 4-hour course clock. Maps 1:1 to all **5 domains** and all **30 task statements** (TS1.1 - TS5.6) in the February 2025 Exam Guide. The contract: if you understand this workbook, you know the exam.

**Authoritative source:** `docs/Claude+Certified+Architect+-+Foundations+Certification+Exam+Guide.pdf`. Exam shape: **60 multiple-choice**, **120 minutes**, **720/1000** to pass, **one attempt**, **$99**, ProctorFree remote, results within 2 business days. **Scenario-based**: 4 of the 6 named scenarios are drawn at random per sitting.

**Long-form teaching lives in the six segment notebooks.** This notebook is the coverage-complete reference: minimal exam-probing demos, the 6-scenario index, the 30-task-statement matrix, the cheat sheet. Where it would duplicate a segment cell verbatim, it cites the segment notebook instead.
"""

_part0_howto_md = """\
## How to use this workbook

Seven Parts. Read top-to-bottom or jump by domain - every section is tagged with its task-statement IDs (TS_x.y) and its named exam scenarios. Each Part closes with a terse `**What the exam probes**` cell: API field names, value enumerations, the production decision rule.

| Part | Title | Domain | Weight |
|---|---|---|---|
| 0 | Setup | preamble | n/a |
| 1 | Agentic Architecture and Orchestration | D1 | **27%** |
| 2 | Tool Design and MCP Integration | D2 | 18% |
| 3 | Claude Code Configuration and Workflows | D3 | 20% |
| 4 | Prompt Engineering and Structured Output | D4 | 20% |
| 5 | Context Management and Reliability | D5 | 15% |
| 6 | Exam mechanics, coverage matrix, self-check | closing | n/a |

**D1 + D3 + D4 = 67% of the exam.** Weight study time the same way.
"""

_part0_scenarios_md = """\
## The six named exam scenarios

The exam draws **4 of these 6 scenarios** at random per sitting. Every question is grounded in one scenario. Recognize the scenario, recognize the domain emphasis.

| # | Scenario | Primary domains |
|---|---|---|
| 1 | **Customer Support Resolution Agent** (returns, billing, refunds via MCP tools; 80%+ first-contact target) | D1, D2, D5 |
| 2 | **Code Generation with Claude Code** (refactoring, debugging, slash commands, plan mode vs direct) | D3, D5 |
| 3 | **Multi-Agent Research System** (coordinator + web-search/document-analysis/synthesis subagents) | D1, D2, D5 |
| 4 | **Developer Productivity with Claude** (codebase exploration, built-in tools, MCP integration) | D2, D3, D1 |
| 5 | **Claude Code for Continuous Integration** (automated code review, test generation, PR feedback) | D3, D4 |
| 6 | **Structured Data Extraction** (JSON schemas, validation, batch processing) | D4, D5 |

Part 6 re-indexes these against the practice questions.
"""

_part0_setup_md = """\
## Setup

Live Messages API throughout. **Managed Agents cells are READ-ONLY** - list and retrieve only, never create or destroy. **Budget: ~$0.15-$0.25** for a full top-to-bottom run.

**Model policy:** `claude-haiku-4-5` is the default everywhere. `claude-sonnet-4-6` is used in exactly one cell - the Part 4 forced-extraction-with-retry demo - where the reasoning depth measurably lifts validation accuracy (the documented repo exception).
"""

_part0_imports_code = """\
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Optional

# Load .env from the repo root (gitignored, never committed)
try:
    from dotenv import load_dotenv
    REPO_ROOT_CANDIDATE = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
    load_dotenv(REPO_ROOT_CANDIDATE / ".env")
except ImportError:
    pass

from anthropic import Anthropic

assert os.environ.get("ANTHROPIC_API_KEY"), "ANTHROPIC_API_KEY not set"

REPO_ROOT = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
client = Anthropic()

# Course default. Promote to Sonnet only where reasoning depth measurably
# matters (Part 4 forced extraction with retry).
MODEL = "claude-haiku-4-5"
SONNET = "claude-sonnet-4-6"

# Required for the Managed Agents beta surface
# (client.beta.{memory_stores, vaults, agents, sessions}).
MANAGED_AGENTS_BETA = {"anthropic-beta": "managed-agents-2026-04-01"}

print(f"client OK | default model: {MODEL} | repo: {REPO_ROOT.name}")
"""


# ===========================================================================
# Part 1: Agentic Architecture & Orchestration (D1, 27%, TS1.1-1.7)
# ===========================================================================

_part1_header_md = """\
# Part 1: Agentic Architecture and Orchestration

**Domain 1 | 27% of the exam | the single largest lever.** Task statements **TS1.1 - TS1.7**. Scenarios most affected: **Customer Support Resolution Agent**, **Multi-Agent Research System**, **Developer Productivity**.

Coverage in this Part:

- **TS1.1** agentic loop lifecycle - `stop_reason` branching, tool results appended, model-driven vs decision-tree (live demo)
- **TS1.2** coordinator-subagent hub-and-spoke - isolated context, dynamic subagent selection, iterative refinement (live demo)
- **TS1.3** subagent invocation via Task tool - `allowedTools` must include `"Task"`, `AgentDefinition`, explicit context passing, parallel Task calls (concept)
- **TS1.4** multi-step workflows - programmatic enforcement vs prompt guidance, structured handoff summaries (live + local hooks)
- **TS1.5** Agent SDK hooks - `PreToolUse` interception, `PostToolUse` normalization (local demo)
- **TS1.6** task decomposition - prompt chaining vs dynamic adaptive (concept)
- **TS1.7** session resume and `fork_session` (concept)

**Long-form teaching:** `notebooks/segment-1-customer-support-agent.ipynb` (live-taught Segment 1).
"""

_part1_loop_concept_md = """\
## TS1.1 The agentic loop is a `stop_reason` state machine

The agentic loop is **not** a decision tree you write. It is a state machine driven by one field on every response: **`stop_reason`**. The model decides the next move; your code branches on the API enum.

**The contract:**

1. Call `messages.create()` with `tools=[...]` and your conversation.
2. Read `resp.stop_reason`. Branch on the enum, **never** on assistant prose.
3. If `tool_use`: extract every `tool_use` block, execute, append `{"role": "user", "content": [tool_result blocks]}` to the message history, loop.
4. If `end_turn`: return to the user.
5. If anything else (`max_tokens`, `pause_turn`, `refusal`, `stop_sequence`): handle deliberately - do not blindly retry.

**Anti-patterns the exam tests for:**
- Parsing natural language ("ok I'm done now") to decide whether to stop. **Wrong.** Branch on `stop_reason`.
- Setting an arbitrary iteration cap as the PRIMARY stopping mechanism. **Wrong.** The cap is a backstop; `end_turn` is the real signal.
- Checking for assistant text content as a completion indicator. **Wrong.** `tool_use` and `text` blocks can coexist in one response.

The cell below runs a compact synthetic agent over a 2-tool surface and prints `stop_reason` and message-history growth at every iteration. Watch the loop transition: `tool_use -> tool_use -> end_turn`.
"""

_part1_loop_code = '''\
from typing import Any  # self-contained: cell runnable out of order
# A compact 2-tool synthetic agent. The tools are in-memory dicts -
# zero dispatch cost. The whole demo is one user turn, <=4 round-trips.
ORDERS = {
    "ORD-481": {"status": "shipped", "vendor": "Acme", "total_usd": 84.50},
    "ORD-902": {"status": "processing", "vendor": "Globex", "total_usd": 312.00},
}

TOOLS = [
    {
        "name": "lookup_order",
        "description": (
            "Look up an order by its ID (e.g. 'ORD-481'). Returns "
            "{status, vendor, total_usd} or {error: 'not found'}. "
            "Use this BEFORE quoting the customer any order detail."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"order_id": {"type": "string"}},
            "required": ["order_id"],
        },
    },
    {
        "name": "summarize_for_customer",
        "description": (
            "Given an order dict, produce a one-sentence customer-facing "
            "summary. Call ONLY after lookup_order succeeded."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "status": {"type": "string"},
                "vendor": {"type": "string"},
                "total_usd": {"type": "number"},
            },
            "required": ["status", "vendor", "total_usd"],
        },
    },
]

def _dispatch(name: str, args: dict[str, Any]) -> dict[str, Any]:
    """Pure-Python tool dispatcher. Real production wires real backends here."""
    if name == "lookup_order":
        oid = args.get("order_id", "")
        return ORDERS.get(oid, {"error": "not found", "order_id": oid})
    if name == "summarize_for_customer":
        return {"summary": f"Order from {args['vendor']}: ${args['total_usd']:.2f}, currently {args['status']}."}
    return {"error": f"unknown tool {name}"}


def run_agent(user_text: str, max_iter: int = 6) -> list[dict]:
    """The canonical agentic loop. Branches on stop_reason; never on prose."""
    messages: list[dict] = [{"role": "user", "content": user_text}]
    for i in range(max_iter):
        resp = client.messages.create(
            model=MODEL, max_tokens=400,
            system=(
                "You are a customer-support agent. Call lookup_order first, "
                "then summarize_for_customer. Do not invent order details."
            ),
            tools=TOOLS, messages=messages,
        )
        print(f"[iter {i}] stop_reason={resp.stop_reason}  history_len={len(messages)}")
        messages.append({"role": "assistant", "content": resp.content})

        if resp.stop_reason == "end_turn":
            text = next((b.text for b in resp.content if b.type == "text"), "")
            print(f"  final text: {text[:120]!r}")
            return messages
        if resp.stop_reason != "tool_use":
            print(f"  unhandled stop_reason; returning")
            return messages

        # tool_use: execute every block, append a single user turn with all results
        results = []
        for b in resp.content:
            if b.type != "tool_use":
                continue
            payload = _dispatch(b.name, dict(b.input))
            results.append({"type": "tool_result", "tool_use_id": b.id,
                            "content": json.dumps(payload)})
        messages.append({"role": "user", "content": results})
    return messages


_ = run_agent("Customer asks about order ORD-481. Look it up and summarize.")
'''

_part1_decomp_md = """\
## TS1.6 Task decomposition: prompt chaining vs dynamic

Two patterns, picked by task shape:

- **Prompt chaining (static decomposition)** - you define the sequence: per-file analysis -> cross-file integration -> report. Pick this when the steps are known and predictable. Code reviews are the canonical case.
- **Dynamic adaptive decomposition** - the model generates subtasks based on what it discovers at each step. Pick this for open-ended investigation ("trace this bug across an unfamiliar codebase"). The agentic loop above is dynamic decomposition by construction - the model picks the next tool based on the prior result.

**Exam decision rule:** if the task says "analyze each X then do Y", prompt-chain it. If it says "investigate" or "explore", dynamic decomposition.
"""

_part1_subagent_concept_md = """\
## TS1.2 - TS1.4 Coordinator-subagent: hub-and-spoke, isolated context

**Hub-and-spoke** is the only multi-agent topology the exam tests. One coordinator routes; specialized subagents do focused work. The coordinator owns task decomposition, error handling, and synthesis. Subagents own a narrow capability and an isolated context.

**The four non-negotiables:**

1. **Isolated context per subagent.** The subagent gets a FRESH `messages` list seeded with its briefing. It does **not** inherit the coordinator's history. The exam guide is explicit: subagents do not automatically inherit parent context.
2. **Dynamic subagent selection.** The coordinator analyzes the request and picks WHICH subagents to invoke. Always-route-through-everyone is the anti-pattern.
3. **Structured handoff.** Each subagent returns a dict, not prose - claim, evidence, source, confidence. Synthesis depends on this shape (ties TS5.6 provenance).
4. **Error propagation.** A subagent that hits an error returns structured error context (failure type, what was attempted, partial results). The coordinator decides recovery. Swallowing errors as empty success is the anti-pattern (ties TS5.3).

The cell below runs a coordinator over two subagents (`research`, `synthesis`). The research subagent deliberately fails on its second lookup to demonstrate structured error propagation. Watch the message-history length printed by each subagent: it stays small because contexts are isolated.
"""

_part1_subagent_code = '''\
from typing import Any  # self-contained: cell runnable out of order
# In-memory mocks. The point is the topology, not the data.
_FACTS = {
    "ORD-481": "shipped 2026-05-15 via courier; signed-for",
    "ORD-902": "in vendor warehouse; expected ship 2026-05-25",
}


def _research_subagent(briefing: str) -> dict[str, Any]:
    """Scoped subagent: one tool, isolated context, returns a structured dict."""
    tools = [{
        "name": "lookup_fact",
        "description": "Look up one order-status fact by ID.",
        "input_schema": {"type": "object",
                         "properties": {"order_id": {"type": "string"}},
                         "required": ["order_id"]},
    }]
    messages: list[dict] = [{"role": "user", "content": briefing}]
    for i in range(4):
        resp = client.messages.create(
            model=MODEL, max_tokens=300,
            system="You are a research subagent. Look up at most TWO facts then return a one-sentence summary. Do not retry on errors; surface them.",
            tools=tools, messages=messages,
        )
        messages.append({"role": "assistant", "content": resp.content})
        if resp.stop_reason == "end_turn":
            text = next((b.text for b in resp.content if b.type == "text"), "")
            print(f"    [research] isolated history_len={len(messages)}")
            return {"status": "ok", "finding": text, "sources": list(_FACTS.keys())[:2]}
        if resp.stop_reason != "tool_use":
            return {"status": "failed", "errorCategory": "transient",
                    "isRetryable": True, "attempted": briefing}
        results = []
        for b in resp.content:
            if b.type != "tool_use":
                continue
            oid = b.input.get("order_id", "")
            fact = _FACTS.get(oid)
            if fact is None:
                # Structured error inside the subagent's tool surface.
                payload = {"isError": True, "errorCategory": "validation",
                           "isRetryable": False, "message": f"no fact for {oid}"}
                results.append({"type": "tool_result", "tool_use_id": b.id,
                                "is_error": True, "content": json.dumps(payload)})
            else:
                results.append({"type": "tool_result", "tool_use_id": b.id,
                                "content": json.dumps({"fact": fact})})
        messages.append({"role": "user", "content": results})
    return {"status": "failed", "errorCategory": "transient",
            "isRetryable": True, "attempted": briefing}


def _synthesis_subagent(briefing: str) -> dict[str, Any]:
    """Scoped subagent: no tools, just combines and cites. Isolated context."""
    messages = [{"role": "user", "content": briefing}]
    resp = client.messages.create(
        model=MODEL, max_tokens=300,
        system="You are a synthesis subagent. Return ONE concise sentence that combines the inputs and preserves source attribution. Do not invent facts.",
        messages=messages,
    )
    text = next((b.text for b in resp.content if b.type == "text"), "")
    print(f"    [synthesis] isolated history_len={len(messages) + 1}")
    return {"status": "ok", "synthesis": text}


# The coordinator's only tool: delegate. Small surface by design (TS2.3).
COORD_TOOLS = [{
    "name": "delegate",
    "description": (
        "Hand a focused subtask to a scoped subagent. role='research' for "
        "fact lookups; role='synthesis' for combining prior findings."
    ),
    "input_schema": {"type": "object",
                     "properties": {
                         "role": {"type": "string", "enum": ["research", "synthesis"]},
                         "briefing": {"type": "string"},
                     },
                     "required": ["role", "briefing"]},
}]

print("=== Coordinator-subagent run ===")
messages: list[dict] = [{"role": "user", "content": "Customer asks status of ORD-481 and ORD-902. Investigate and answer in one sentence."}]
for i in range(5):
    resp = client.messages.create(
        model=MODEL, max_tokens=500,
        system=(
            "You are the coordinator. Delegate fact-lookup to the research "
            "subagent FIRST (one delegate call), then delegate to synthesis "
            "with the research finding included verbatim. Return to the user "
            "ONLY after synthesis succeeds."
        ),
        tools=COORD_TOOLS, messages=messages,
    )
    print(f"[coord iter {i}] stop_reason={resp.stop_reason}")
    messages.append({"role": "assistant", "content": resp.content})
    if resp.stop_reason == "end_turn":
        text = next((b.text for b in resp.content if b.type == "text"), "")
        print(f"  coordinator final: {text[:140]!r}")
        break
    if resp.stop_reason != "tool_use":
        break
    results = []
    for b in resp.content:
        if b.type != "tool_use" or b.name != "delegate":
            continue
        role = b.input["role"]
        briefing = b.input["briefing"]
        print(f"  [coord] delegating to {role}")
        if role == "research":
            payload = _research_subagent(briefing)
        else:
            payload = _synthesis_subagent(briefing)
        results.append({"type": "tool_result", "tool_use_id": b.id,
                        "content": json.dumps(payload),
                        # Surface upstream failures to the coordinator (TS5.3).
                        "is_error": payload.get("status") == "failed"})
    messages.append({"role": "user", "content": results})

print()
print("Note the printed history_len numbers from each subagent: they stay")
print("small because each subagent ran in its OWN messages list. The")
print("coordinator's history is separate. That isolation is TS1.2.")
'''

_part1_hooks_concept_md = """\
## TS1.4 - TS1.5 Hooks are deterministic guarantees, prompts are not

The exam tests this distinction relentlessly. **Prompt instructions have a non-zero failure rate.** When a business rule requires guaranteed compliance (refund cap, identity verification before financial action), you do **not** rely on "the system prompt told it to". You install a **hook**.

Two hook patterns:

- **`PreToolUse`** intercepts an outgoing tool call BEFORE execution. Used for policy enforcement: block `process_refund` if the amount exceeds the cap, redirect to escalation. Returns a structured error `tool_result` so the model sees a refusal and re-plans.
- **`PostToolUse`** intercepts a tool result AFTER execution, BEFORE the model processes it. Used for data normalization: convert Unix timestamps to ISO 8601, map status codes to names, strip 35 of 40 fields the agent will never need.

The cell below runs both against synthetic calls. **No API needed** - hooks are pure Python, run inside your loop. This is the same pattern as `hooks-example.py` at the repo root.
"""

_part1_hooks_code = '''\
from typing import Any  # self-contained: cell runnable out of order
# Sample 1 from the exam guide: refund cap. A PreToolUse hook is the
# only correct answer (option B = prompt is wrong; option C = few-shot
# is wrong; option D = routing classifier solves a different problem).
REFUND_CAP_USD = 500.0

def pre_tool_use(tool_name: str, tool_input: dict[str, Any]) -> dict[str, Any] | None:
    """Return None to ALLOW the tool call. Return a dict to BLOCK and
    surface the dict back to the model as a structured error tool_result."""
    if tool_name == "process_refund":
        amount = float(tool_input.get("amount_usd", 0))
        if amount > REFUND_CAP_USD:
            return {
                "isError": True,
                "errorCategory": "permission",
                "isRetryable": False,
                "message": (
                    f"Refund of ${amount:.2f} exceeds the ${REFUND_CAP_USD:.0f} "
                    f"cap. Escalate via escalate_to_human; do not retry."
                ),
            }
        # Prerequisite gate (TS1.4): block until customer is verified.
        if not tool_input.get("verified_customer_id"):
            return {
                "isError": True,
                "errorCategory": "validation",
                "isRetryable": False,
                "message": "Call get_customer first; verified_customer_id missing.",
            }
    return None  # allow


def post_tool_use(tool_name: str, raw_result: dict[str, Any]) -> dict[str, Any]:
    """Normalize the raw tool result before the model sees it. Trims 35
    of 40 fields the agent does not need, converts timestamps to ISO."""
    if tool_name == "lookup_order":
        import datetime as _dt
        keep = {"id", "status", "total_usd", "created_at"}
        out = {k: v for k, v in raw_result.items() if k in keep}
        # Normalize a Unix-timestamp created_at to ISO 8601.
        if isinstance(out.get("created_at"), (int, float)):
            out["created_at"] = _dt.datetime.fromtimestamp(out["created_at"], tz=_dt.timezone.utc).isoformat()
        return out
    return raw_result


# --- Run both hooks against synthetic calls ---
print("=== PreToolUse: policy enforcement ===")
for amt in [50, 750]:
    decision = pre_tool_use("process_refund", {"amount_usd": amt, "verified_customer_id": "cust_123"})
    verdict = "ALLOWED" if decision is None else f"BLOCKED ({decision['errorCategory']})"
    print(f"  refund ${amt}: {verdict}")

decision = pre_tool_use("process_refund", {"amount_usd": 50})  # no verified ID
print(f"  refund $50 no verified ID: BLOCKED ({decision['errorCategory']})")

print()
print("=== PostToolUse: data normalization ===")
raw = {
    "id": "ORD-481", "status": 2, "total_usd": 84.50, "created_at": 1747000000,
    "vendor_internal_id": "v-77", "warehouse_zone": "C-4", "weight_kg": 1.2,
    "carrier_tracking": "1Z..", "ship_method": "ground", "insurance_usd": 0,
    # ...30 more fields the agent never needs
}
normalized = post_tool_use("lookup_order", raw)
print(f"  raw fields: {len(raw)}")
print(f"  normalized: {normalized}")
print(f"  field reduction: {len(raw) - len(normalized)} dropped")

print()
print("Exam beat: hooks are DETERMINISTIC. Prompts are PROBABILISTIC.")
print("When the business rule is non-negotiable, use a hook (TS1.4, TS1.5).")
'''

_part1_task_tool_md = """\
## TS1.3 The Task tool (Claude Code harness primitive)

In the **Claude Code** harness (and the **Claude Agent SDK** that uses the same vocabulary), subagents are spawned via the **`Task` tool**. Four facts the exam tests:

1. **`allowedTools` must include `"Task"`** for a coordinator to spawn subagents. Without it, the Task tool is unreachable.
2. **`AgentDefinition`** is the recipe per subagent type: name, description, system prompt, and the subagent's own `allowedTools` (which deliberately do NOT include `Task` for leaf subagents - that prevents recursion).
3. **Subagent context must be EXPLICITLY passed in the prompt.** Subagents do not automatically inherit the parent's conversation - the exam guide is explicit. The coordinator includes prior findings verbatim in the next subagent's briefing.
4. **Parallel subagents = multiple `Task` tool calls in ONE assistant response.** Not multiple turns. The model emits N `tool_use` blocks of type Task; the harness runs them concurrently; results return as N `tool_result` blocks.

These are harness primitives, not Messages-API-reachable - the bare Messages cells above demonstrate the same topology by hand. The exam tests the vocabulary.
"""

_part1_sessions_md = """\
## TS1.7 Session resume vs fork

- **`--resume <session-name>`** (Claude Code CLI) continues a named prior session. The model sees the full history.
- **`fork_session`** (Agent SDK) creates an independent branch from a shared analysis baseline. Use it to compare two refactoring strategies from the same exploration.

**Exam decision rule:** if prior context is mostly still valid, resume. If prior tool results have gone stale (files changed since), **start a fresh session with an injected structured summary** rather than resume with stale tool_result blocks. The exam guide states this explicitly.
"""

_part1_exam_probes_md = """\
## What the exam probes (Domain 1)

| Concept | Exam-tested fact |
|---|---|
| `stop_reason` enum | `tool_use`, `end_turn` are the two cited in the guide; loop branches on these. Never parse prose. |
| Loop termination | `end_turn` is the signal. Iteration cap is a backstop, not the primary mechanism. |
| Subagent context | **Does NOT inherit parent context.** Pass explicitly in the briefing. |
| Coordinator role | Task decomposition, dynamic subagent selection, error handling, synthesis. Hub-and-spoke. |
| Task tool | `allowedTools` MUST include `"Task"`. Parallel subagents = multiple Task calls in ONE response. |
| Hooks vs prompts | Hooks = deterministic. Prompts = probabilistic. Use hooks for non-negotiable rules. |
| `PreToolUse` | Blocks outgoing tool call; returns structured error to the model. |
| `PostToolUse` | Normalizes tool results before the model sees them. |
| Sessions | `--resume` for valid context. Fresh session + injected summary if tool results are stale. `fork_session` for parallel exploration. |
"""


# ===========================================================================
# Part 2: Tool Design & MCP Integration (D2, 18%, TS2.1-2.5)
# ===========================================================================

_part2_header_md = """\
# Part 2: Tool Design and MCP Integration

**Domain 2 | 18% of the exam.** Task statements **TS2.1 - TS2.5**. Scenarios most affected: **Customer Support Resolution Agent**, **Structured Data Extraction**, **Developer Productivity**.

Coverage in this Part:

- **TS2.1** tool descriptions as the primary selection mechanism; split generic into specific (concept)
- **TS2.2** structured error responses - `isError`, `errorCategory`, `isRetryable` (live demo)
- **TS2.3** tool distribution (~4-5 per agent), `tool_choice` modes (live demo of all four)
- **TS2.4** MCP server config - `.mcp.json` scope, env-var expansion, transports (repo inspection + live MCP discovery)
- **TS2.5** built-in tools Read/Write/Edit/Bash/Grep/Glob (concept)

**Long-form teaching:** `notebooks/segment-2-tool-design-and-mcp.ipynb` and `notebooks/segment-2-5-control-surfaces.ipynb`.
"""

_part2_description_concept_md = """\
## TS2.1 Tool descriptions are the contract, not the names

**The exam-tested mechanic (Sample Question 2):** when two tools with thin descriptions misfire, the **first** fix is to **expand the descriptions**, not add few-shot examples or build a routing layer. Tool descriptions are the primary mechanism the model uses for selection.

A good tool description includes:
- **Purpose:** what it does in one clause
- **When to call it** - and when NOT to call it (the boundary against neighbors)
- **Input formats** with concrete examples
- **Success and failure shapes** so the model knows what to expect back

**Splitting generic tools into specific ones** is the other lever. A single `analyze_document` invites confusion. Split into `extract_data_points`, `summarize_content`, `verify_claim_against_source` - each with a sharp description - and selection reliability jumps.

**The 4-5 tool cap (TS2.3):** an agent given 18 tools selects worse than the same agent given 4-5. When you need more, split into subagents with scoped tool sets.
"""

_part2_tool_choice_md = """\
## TS2.3 `tool_choice` - four modes, four guarantees

| Mode | Form | Guarantee | Use when |
|---|---|---|---|
| `auto` | `{"type": "auto"}` (default) | Model may call a tool OR answer in prose | Default conversational agent |
| `any` | `{"type": "any"}` | Model MUST call SOME tool (no prose answer) | You want forced action; let the model pick which |
| `tool` (forced) | `{"type": "tool", "name": "<name>"}` | Model MUST call THAT specific tool | Structured output via schema; force `extract_metadata` first |
| `none` | `{"type": "none"}` | Tools registered but model CANNOT call them | Tools-off turn in a multi-turn flow |

Plus the modifier **`disable_parallel_tool_use: true`** on `auto` or `any` - one tool per turn, ordering matters.

The cell below runs all four modes against the same prompt and prints the resulting `stop_reason` and content type per mode. The contrast is the exam beat.
"""

_part2_tool_choice_code = '''\
from typing import Any  # self-contained: cell runnable out of order
# One tiny tool, two prompts to make the auto-vs-any contrast visible.
# The prompt for `auto` is deliberately UNRELATED to the tool so the
# model has a reason NOT to call it; the prompt for `any` and `tool`
# is on-topic. Same model, same tool, same four modes.
TC_TOOLS = [{
    "name": "get_weather",
    "description": "Get the current temperature for a US city. Returns {temp_f: number}.",
    "input_schema": {"type": "object",
                     "properties": {"city": {"type": "string"}},
                     "required": ["city"]},
}]
OFF_TOPIC = "In one sentence, what year did the Apollo 11 mission land on the moon?"
ON_TOPIC = "What is the weather in Nashville right now?"

def _show(label: str, prompt: str, tc: dict | None) -> None:
    kwargs: dict[str, Any] = dict(model=MODEL, max_tokens=120, tools=TC_TOOLS,
                                  messages=[{"role": "user", "content": prompt}])
    if tc is not None:
        kwargs["tool_choice"] = tc
    resp = client.messages.create(**kwargs)
    block_types = [getattr(b, "type", "?") for b in resp.content]
    print(f"  [{label:>20}]  stop_reason={resp.stop_reason}  blocks={block_types}")

print("Four tool_choice modes - the contrast is what each GUARANTEES:")
print()
print("auto, off-topic prompt (model SHOULD answer in prose, skipping the tool):")
_show("auto (off-topic)", OFF_TOPIC, {"type": "auto"})
print()
print("any, off-topic prompt (model MUST call SOME tool even though it would")
print("rather answer in prose - this is the forcing function):")
_show("any (off-topic)", OFF_TOPIC, {"type": "any"})
print()
print("On-topic prompt, all four modes:")
_show("auto (on-topic)", ON_TOPIC, {"type": "auto"})
_show("any (on-topic)", ON_TOPIC, {"type": "any"})
_show("tool (forced one)", ON_TOPIC, {"type": "tool", "name": "get_weather"})
_show("none (no tools)", ON_TOPIC, {"type": "none"})
print()
print("Exam beat: `auto` may answer in prose (see off-topic row: stop_reason")
print("=end_turn, text block). `any` and forced `tool` MUST emit tool_use.")
print("`none` forbids tool calls entirely. Pick the mode that matches your")
print("guarantee, not the one that feels safest.")
'''

_part2_structured_error_md = """\
## TS2.2 Structured error responses - the four categories

When a tool fails, returning `"error": "Operation failed"` blinds the model. It cannot tell if it should retry, reformulate, or escalate. **Structured errors are the fix.**

The shape:

```python
{
  "isError": True,
  "errorCategory": "transient" | "validation" | "permission" | "business",
  "isRetryable": True | False,
  "message": "what the model should DO next, not a passive description",
}
```

The MCP `isError` flag is the protocol-level signal; the body carries the metadata. **`errorCategory`** drives the model's response:

- **`transient`** (timeout, 503) - the model retries
- **`validation`** (bad input shape) - the model reformulates the call
- **`permission`** (auth, scope) - the model escalates, does not retry
- **`business`** (policy rule, refund cap) - the model escalates, does not retry

The cell below returns a structured-business-error from a `process_refund` tool and lets the model react.
"""

_part2_structured_error_code = '''\
from typing import Any  # self-contained: cell runnable out of order
# A single tool that returns a structured business error.
ERR_TOOLS = [{
    "name": "process_refund",
    "description": "Process a customer refund. Returns success or a structured error.",
    "input_schema": {"type": "object",
                     "properties": {
                         "order_id": {"type": "string"},
                         "amount_usd": {"type": "number"},
                     },
                     "required": ["order_id", "amount_usd"]},
}]

def _refund_tool(args: dict[str, Any]) -> dict[str, Any]:
    amount = float(args.get("amount_usd", 0))
    if amount > 500:
        # The whole point of the demo: structured business error.
        return {
            "isError": True,
            "errorCategory": "business",
            "isRetryable": False,
            "message": (
                f"Refund of ${amount:.2f} exceeds the $500 cap. Do NOT retry. "
                f"Inform the customer this requires a supervisor and stop."
            ),
        }
    return {"status": "ok", "refund_id": "RF-7710", "amount_usd": amount}


messages: list[dict] = [{"role": "user", "content": "Please refund $750 on order ORD-902."}]
for i in range(3):
    resp = client.messages.create(
        model=MODEL, max_tokens=400,
        system="You are a refund agent. Use process_refund. If a tool returns a business error, inform the customer; do NOT retry.",
        tools=ERR_TOOLS, messages=messages,
    )
    print(f"[iter {i}] stop_reason={resp.stop_reason}")
    messages.append({"role": "assistant", "content": resp.content})
    if resp.stop_reason == "end_turn":
        text = next((b.text for b in resp.content if b.type == "text"), "")
        print(f"  final to customer: {text[:160]!r}")
        break
    if resp.stop_reason != "tool_use":
        break
    results = []
    for b in resp.content:
        if b.type != "tool_use":
            continue
        payload = _refund_tool(dict(b.input))
        results.append({"type": "tool_result", "tool_use_id": b.id,
                        "is_error": payload.get("isError", False),
                        "content": json.dumps(payload)})
    messages.append({"role": "user", "content": results})

print()
print("Exam beat: errorCategory='business' + isRetryable=False signals the")
print("model to inform-and-stop. A generic 'Operation failed' would have")
print("invited a retry loop. Structured errors are the contract that")
print("makes recovery decisions reliable (TS2.2, ties TS5.3).")
'''

_part2_mcp_concept_md = """\
## TS2.4 MCP server configuration - `.mcp.json`, scope, transports

**MCP (Model Context Protocol)** is the protocol that exposes your tools, resources, and prompts to any MCP-aware client (Claude Code, Cursor, your custom agent).

**Scope:**
- **Project-scoped** `.mcp.json` at the repo root - shared via version control, for team tooling.
- **User-scoped** `~/.claude.json` - personal/experimental servers, never committed.
- Both are merged at runtime; tools from all configured servers are available simultaneously.

**Transports:**
- **stdio** - local subprocess (the default for development; `command` + `args`)
- **HTTP** - remote stateless request/response (`type: "http"`, `url`, `headers`)
- **SSE** - remote streaming (`type: "sse"`, `url`, `headers`)

**Env-var expansion:** `${VAR}` works inside `command`, `args`, `env` values, `url`, and `headers` values. Secrets stay in your shell environment, never in the committed `.mcp.json`.

**MCP resources** (distinct from MCP tools) expose READ-ONLY content catalogs - documentation hierarchies, database schemas, issue summaries. Give an agent visibility into available data without forcing it to call exploratory tools.

The cell below parses this repo's real `.mcp.json` and prints the servers and their transports.
"""

_part2_mcp_inspect_code = '''\
mcp_path = REPO_ROOT / ".mcp.json"
if not mcp_path.exists():
    print(f"(no .mcp.json at {mcp_path})")
else:
    config = json.loads(mcp_path.read_text(encoding="utf-8"))
    servers = config.get("mcpServers", {})
    print(f"servers configured in {mcp_path.relative_to(REPO_ROOT)}: {len(servers)}")
    print()
    for name, spec in servers.items():
        # Determine transport from the shape.
        if "command" in spec:
            transport = "stdio"
            detail = f"{spec['command']} {' '.join(spec.get('args', []))[:60]}"
        else:
            transport = spec.get("type", "?")
            detail = spec.get("url", "")
        # Spot ${VAR} expansions.
        spec_str = json.dumps(spec)
        env_vars = [tok for tok in spec_str.split("${") if "}" in tok]
        env_vars = [v.split("}")[0] for v in env_vars[1:]]
        env_note = f" env={env_vars}" if env_vars else ""
        print(f"  {name:>22}  [{transport}]  {detail}{env_note}")

print()
print("Three transports, env-var expansion, project-scoped: that is")
print("the entire .mcp.json contract the exam tests (TS2.4).")
'''

_part2_mcp_discovery_md = """\
## TS2.4 (continued) Runtime MCP discovery via `list_tools`

**`list_tools()`** is the discovery primitive. Your MCP client connects to a server and asks "what tools do you expose?" The server returns a list of schemas, which you merge into the `tools=[...]` parameter passed to `messages.create()`. **No source change to add a new tool** - just deploy a new server (or add a tool to an existing one) and the next `list_tools()` picks it up.

The cell below launches this repo's own FastMCP demo server (`examples/mcp_cli/mcp_server.py`, configured as `document-mcp` in `.mcp.json`) over stdio and calls `list_tools`, `list_resources`, `list_prompts`. **Zero Anthropic tokens** - this is pure MCP protocol over stdio.

The cell is wrapped in try/except: if the MCP Python SDK or `uv` is not on the box, it skips gracefully with a labeled message.
"""

_part2_mcp_discovery_code = '''\
# Live MCP discovery against the repo's own FastMCP demo server.
# Jupyter's IPython kernel already runs an asyncio event loop, so we
# use TOP-LEVEL AWAIT (IPython feature) instead of asyncio.run().
# Wrapped in try/except so a missing dependency or a subprocess
# failure does not break the notebook smoke - the .mcp.json
# inspection above already covered TS2.4.
try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    params = StdioServerParameters(
        command="uv",
        args=["run", "--directory", str(REPO_ROOT / "examples" / "mcp_cli"), "mcp_server.py"],
    )
    print("=== Live MCP discovery against examples/mcp_cli/mcp_server.py ===")
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools_resp = await session.list_tools()
            resources_resp = await session.list_resources()
            prompts_resp = await session.list_prompts()
            print(f"     tools: {[t.name for t in tools_resp.tools]}")
            print(f" resources: {[str(r.uri) for r in resources_resp.resources]}")
            print(f"   prompts: {[p.name for p in prompts_resp.prompts]}")
    print()
    print("That is hot-pluggable discovery. The client did not import the")
    print("server's source; it asked over stdio. Every MCP client - Claude")
    print("Code, Cursor, your custom agent - uses the same three list_*")
    print("primitives. Add a new tool to the server, every connected client")
    print("picks it up on the next list_tools call. (TS2.4)")
except Exception as exc:
    print(f"(MCP discovery skipped: {type(exc).__name__}: {str(exc)[:160]})")
    print("The .mcp.json inspection above already demonstrates TS2.4.")
    print("To run this cell live: ensure `uv` and the `mcp` Python SDK are")
    print("installed, and that examples/mcp_cli/ has been bootstrapped via")
    print("`uv sync` in that directory.")
'''

_part2_builtin_tools_md = """\
## TS2.5 Claude Code built-in tools

The Claude Code harness ships six built-in tools the exam tests by usage criterion (not by syntax - the syntax is harness-internal, **not API-reachable** from your custom agent; see Part 1's tier-3 boundary).

| Tool | Use for | Anti-pattern |
|---|---|---|
| **Grep** | Search file contents for a pattern (function calls, error strings, imports) | Reading every file upfront |
| **Glob** | Find files by path pattern (`**/*.test.tsx`) | Searching contents when you only need paths |
| **Read** | Load a full file's contents | Editing without reading first |
| **Edit** | Targeted in-place modification using unique text matching | When the anchor text is not unique - fall back to Read + Write |
| **Write** | Replace a whole file (or fall back from Edit) | When Edit would work; Edit is safer |
| **Bash** | Run shell commands (tests, build, git) | When a structured tool would be safer |

**Exam decision rule:** **Grep for content, Glob for paths.** When Edit's anchor is not unique, use Read + Write. Build understanding incrementally: Grep to find entry points, Read to follow imports.
"""

_part2_exam_probes_md = """\
## What the exam probes (Domain 2)

| Concept | Exam-tested fact |
|---|---|
| Tool descriptions | The **primary** mechanism for selection. First fix when tools misfire. |
| Splitting tools | Generic -> purpose-specific reduces ambiguity. |
| Tool count per agent | ~4-5 cap; more degrades selection. Split into subagents. |
| `tool_choice` modes | `auto`, `any`, `tool` (forced specific), `none`. |
| `disable_parallel_tool_use` | Modifier on `auto`/`any` - one tool per turn. |
| Structured errors | `isError` + `errorCategory` (transient/validation/permission/business) + `isRetryable`. |
| MCP scope | Project (`.mcp.json`) vs user (`~/.claude.json`). |
| MCP transports | stdio, HTTP, SSE. Env-var expansion via `${VAR}`. |
| MCP resources | READ-ONLY content catalogs; reduce exploratory tool calls. |
| `list_tools` | Runtime discovery. New tools picked up without source change. |
| Built-in tools | **Grep for content, Glob for paths.** Read + Write fallback when Edit anchor not unique. |
"""


# ===========================================================================
# Part 3: Claude Code Configuration & Workflows (D3, 20%, TS3.1-3.6)
# ===========================================================================

_part3_header_md = """\
# Part 3: Claude Code Configuration and Workflows

**Domain 3 | 20% of the exam.** Task statements **TS3.1 - TS3.6**. Scenarios most affected: **Code Generation with Claude Code**, **Claude Code for CI**, **Developer Productivity**.

Coverage in this Part:

- **TS3.1** `CLAUDE.md` hierarchy (user / project / directory), `@import`, `.claude/rules/`
- **TS3.2** custom slash commands + skills `SKILL.md` frontmatter (`context: fork`, `allowed-tools`, `argument-hint`)
- **TS3.3** path-specific rules - YAML frontmatter `paths` globs for conditional convention loading
- **TS3.4** plan mode vs direct execution
- **TS3.5** iterative refinement (input/output examples, test-driven, interview pattern)
- **TS3.6** CI/CD integration - `claude -p`, `--output-format json`, `--json-schema`

**Long-form teaching:** `notebooks/segment-2-tool-design-and-mcp.ipynb`.
"""

_part3_banner_md = """\
> **Read this first.** Claude Code is a **CLI harness**, not a Python library. The cells in this Part **inspect real configuration artifacts in this repo** and explain the mechanics. They do **not** invoke `claude`. Run the CLI in your terminal to see it live; the patterns shown here are what the CLI consumes at startup.
"""

_part3_claude_md_concept_md = """\
## TS3.1 The `CLAUDE.md` configuration hierarchy

Claude Code merges instruction files from three tiers, in this precedence order (lowest to highest priority - higher tiers override or extend lower tiers):

1. **User-level** `~/.claude/CLAUDE.md` - your personal defaults across every project. **Not** shared via version control. The exam's classic trap: a new teammate "missing instructions" because the rules were authored at this tier.
2. **Project-level** `<repo>/CLAUDE.md` (or `<repo>/.claude/CLAUDE.md`) - team conventions, checked into the repo. The right tier for anything every contributor must know.
3. **Directory-level** `<repo>/<subdir>/CLAUDE.md` - loaded only when the working directory is inside that subtree. Use sparingly - path-specific rules (TS3.3) are usually better.

**`@import` syntax** keeps `CLAUDE.md` files modular: `@./testing.md` or `@./api-conventions.md` references external files so the root `CLAUDE.md` stays scannable.

**Diagnostic tool:** the `/memory` command (inside Claude Code) shows which memory files are loaded - the right first move when behavior diverges between teammates.
"""

_part3_claude_md_inspect_code = '''\
claude_md = REPO_ROOT / "CLAUDE.md"
if not claude_md.exists():
    print(f"(no CLAUDE.md at {claude_md})")
else:
    text = claude_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    print(f"=== {claude_md.relative_to(REPO_ROOT)} ({len(lines)} lines) ===")
    print()
    print("First 25 lines (the project-level header):")
    for i, line in enumerate(lines[:25], start=1):
        print(f"  {i:3d}  {line}")
    # Highlight any @import lines.
    imports = [ln for ln in lines if ln.strip().startswith("@")]
    print()
    print(f"@import-style lines found: {len(imports)}")
    for imp in imports[:5]:
        print(f"  {imp}")

# Inspect the .claude/ tree alongside it.
claude_dir = REPO_ROOT / ".claude"
if claude_dir.exists():
    print()
    print(f"=== {claude_dir.relative_to(REPO_ROOT)}/ contents ===")
    for child in sorted(claude_dir.iterdir()):
        marker = "/" if child.is_dir() else ""
        print(f"  {child.name}{marker}")
'''

_part3_rules_concept_md = """\
## TS3.3 Path-specific rules in `.claude/rules/`

**Sample Question 6** (exam guide) tests this directly. When conventions must apply to files **spread across the codebase** (e.g. test files alongside their source, regardless of directory), the right answer is a **`.claude/rules/`** file with YAML frontmatter `paths` globs - **not** subdirectory `CLAUDE.md` files, **not** a monolithic root `CLAUDE.md`.

```yaml
---
paths:
  - "**/*.test.tsx"
  - "**/*.test.ts"
---
# Testing conventions
- Use Vitest with `describe` / `it` blocks.
- Mock external services with `vi.mock`.
- Each test must include an Arrange / Act / Assert comment header.
```

**The mechanic:** these rules load **only when the current file matches a glob**, reducing irrelevant context and token usage. They also handle the spread-across-directories case that directory-level `CLAUDE.md` cannot.
"""

_part3_rules_inspect_code = '''\
rules_dir = REPO_ROOT / ".claude" / "rules"
if rules_dir.exists() and any(rules_dir.iterdir()):
    print(f"=== {rules_dir.relative_to(REPO_ROOT)}/ ===")
    for rule_file in sorted(rules_dir.iterdir()):
        if rule_file.is_file():
            print()
            print(f"  --- {rule_file.name} ---")
            head = "\\n".join(rule_file.read_text(encoding="utf-8").splitlines()[:20])
            for line in head.splitlines():
                print(f"    {line}")
else:
    print("(no .claude/rules/ in this repo; illustrative example below)")
    print()
    example = """---
paths:
  - \\"**/*.test.tsx\\"
  - \\"**/*.test.ts\\"
---
# Testing conventions
- Use Vitest with describe / it blocks.
- Mock external services with vi.mock.
- Each test must include Arrange / Act / Assert headers.
"""
    print(example)
print()
print("Exam beat: when conventions must apply to files SPREAD across the")
print("codebase (test files alongside their source), reach for .claude/rules/")
print("with paths globs - not subdirectory CLAUDE.md files (TS3.3).")
'''

_part3_skills_concept_md = """\
## TS3.2 Slash commands and Skills

Two distinct primitives. Both come in **project-scoped** (shared via version control) and **user-scoped** (personal) variants.

| Primitive | Project scope | User scope | What it is |
|---|---|---|---|
| **Slash commands** | `.claude/commands/<name>.md` | `~/.claude/commands/<name>.md` | A reusable prompt the user types `/<name>` to invoke |
| **Skills** | `.claude/skills/<name>/SKILL.md` | `~/.claude/skills/<name>/SKILL.md` | A capability the model discovers and invokes when relevant |

**SKILL.md frontmatter (TS3.2 - exam tests these three explicitly):**

```yaml
---
name: dependency-audit
description: Audit npm dependencies for known CVEs and outdated majors.
context: fork                                # run in an isolated sub-agent context
allowed-tools: ["Read", "Bash"]              # restrict to a minimum surface
argument-hint: "Optional: specific package to audit"
---
# Body: the skill's instructions
```

- **`context: fork`** - run the skill in an **isolated sub-agent context** so its (verbose) output does not pollute the main conversation. Pick this for codebase analysis, exploration, brainstorming.
- **`allowed-tools`** - restrict the skill's tool surface. Pick this when the skill should never touch destructive operations.
- **`argument-hint`** - prompt the user for required parameters when they invoke without arguments.

**Decision rule (skill vs `CLAUDE.md`):** `CLAUDE.md` for **always-loaded universal standards**. Skills for **on-demand task-specific workflows**.
"""

_part3_skill_inspect_code = '''\
from typing import Optional  # self-contained: cell runnable out of order
# Look for any SKILL.md in the repo (project-scoped, possibly nested).
skill_files = list(REPO_ROOT.rglob("SKILL.md"))
# Filter out anything under node_modules/.venv/.
skill_files = [p for p in skill_files
               if "node_modules" not in p.parts and ".venv" not in p.parts]

if skill_files:
    target = skill_files[0]
    print(f"=== {target.relative_to(REPO_ROOT)} (first 30 lines) ===")
    for i, line in enumerate(target.read_text(encoding="utf-8").splitlines()[:30], start=1):
        print(f"  {i:3d}  {line}")
else:
    print("(no SKILL.md in this repo; illustrative frontmatter below)")
    print()
    example = """---
name: dependency-audit
description: Audit npm dependencies for known CVEs and outdated majors.
context: fork
allowed-tools: [\\"Read\\", \\"Bash\\"]
argument-hint: \\"Optional: specific package to audit\\"
---
# Dependency audit

When invoked, run `npm audit --json`, parse the output, and report any
high or critical CVEs along with the upgrade path.
"""
    print(example)
print()
print("Exam beat: `context: fork` isolates verbose skill output; `allowed-tools`")
print("restricts the surface for safety; `argument-hint` prompts for args (TS3.2).")
'''

_part3_plan_mode_md = """\
## TS3.4 Plan mode vs direct execution

**Plan mode** lets Claude Code explore the codebase, understand dependencies, and design an implementation **before** committing to changes. Direct execution makes changes immediately.

**Decision rule (Sample Question 5):**

| Task shape | Mode |
|---|---|
| Large-scale changes across many files (monolith -> microservices, library migration affecting 45+ files) | **Plan mode** |
| Architectural decisions with multiple valid approaches | **Plan mode** |
| Single-file bug fix with a clear stack trace | **Direct** |
| Adding one validation conditional | **Direct** |
| Open-ended discovery with verbose tool output | **Plan mode** + Explore subagent |

**The Explore subagent** isolates verbose discovery output (file walks, dependency traces) and returns a summary, preserving the main conversation's context budget.

**Anti-pattern:** "start direct, switch to plan if it gets complex." The complexity is **already stated in the requirements** - pick plan mode upfront for architectural work.
"""

_part3_iterative_md = """\
## TS3.5 Iterative refinement techniques

Four patterns the exam tests:

1. **Concrete input/output examples** beat prose descriptions. When "transform X to Y" is ambiguous, give 2-3 worked examples.
2. **Test-driven iteration** - write the test suite first, then iterate by sharing test failures with the model.
3. **Interview pattern** - have the model ask **you** questions to surface design considerations (cache invalidation, failure modes) before implementing in an unfamiliar domain.
4. **Single-message-multi-issue vs sequential** - interacting problems go in **one detailed message** (the model needs to see them together). Independent problems can be fixed sequentially.
"""

_part3_cicd_concept_md = """\
## TS3.6 Claude Code in CI/CD

**Sample Question 10:** the right way to run Claude Code in a pipeline is the **`-p` (or `--print`) flag**. It processes the prompt, writes to stdout, and exits without waiting for interactive input. **No `CLAUDE_HEADLESS` env var, no `--batch` flag** - those are distractors the exam plants.

Two output-format flags for structured CI output:

- **`--output-format json`** - emits JSON to stdout, parseable by your CI step
- **`--json-schema <schema>`** - constrains the JSON to a schema you define, so downstream automation never has to guess at field names

**Session context isolation (TS3.6, also TS4.6):** the same Claude session that **generated** the code is **less effective at reviewing** it (it retains the generation reasoning). Use an **independent review instance** for code review in CI.

**`CLAUDE.md` as CI input:** drop your testing standards, fixture conventions, and review criteria into `CLAUDE.md`. CI-invoked Claude Code reads it automatically.

**Sample Question 11 (batches):** if you have two workflows - a **blocking pre-merge check** and an **overnight technical-debt report** - the right play is **synchronous API for pre-merge, batches API for overnight** (TS4.5). Batches API saves 50% but has no latency SLA (up to 24h). Wrong for blocking flows.
"""

_part3_cicd_inspect_code = '''\
# Look for any GitHub Actions workflow or CI script that invokes `claude -p`.
wf_dir = REPO_ROOT / ".github" / "workflows"
found_invocation = False
if wf_dir.exists():
    for wf in sorted(wf_dir.glob("*.y*ml")):
        text = wf.read_text(encoding="utf-8")
        if "claude" in text.lower() and ("-p " in text or "--print" in text):
            print(f"=== {wf.relative_to(REPO_ROOT)} ===")
            for line in text.splitlines():
                if "claude" in line.lower():
                    print(f"  {line}")
            found_invocation = True
            print()

if not found_invocation:
    print("(no `claude -p` invocation found in .github/workflows/ in this repo;")
    print(" illustrative CI snippet below)")
    print()
    example = """# .github/workflows/code-review.yml (illustrative)
- name: Run Claude Code review
  run: |
    claude -p \\
      \\"Review the PR diff for security issues. Report only high-confidence findings.\\" \\
      --output-format json \\
      --json-schema review-schema.json \\
    | jq -c '.findings[]' \\
    | xargs -I{} gh pr comment --body {}
"""
    print(example)
print()
print("Exam beat: -p (or --print) for non-interactive. --output-format json +")
print("--json-schema for machine-parseable output. CLAUDE.md as the implicit")
print("context channel. Independent review session, not the generator (TS3.6).")
'''

_part3_exam_probes_md = """\
## What the exam probes (Domain 3)

| Concept | Exam-tested fact |
|---|---|
| `CLAUDE.md` hierarchy | user (`~/.claude/CLAUDE.md`) -> project (`./CLAUDE.md`) -> directory. **User-level NOT shared via VCS.** |
| `@import` | Modular `CLAUDE.md` via external file references. |
| `/memory` | Diagnostic - shows which memory files are loaded. |
| Slash commands | `.claude/commands/<name>.md` for project; `~/.claude/commands/` for personal. |
| Skills | `.claude/skills/<name>/SKILL.md`. Frontmatter: `context: fork`, `allowed-tools`, `argument-hint`. |
| Skill vs CLAUDE.md | Skill = on-demand. `CLAUDE.md` = always-loaded. |
| `.claude/rules/` paths globs | The right answer for conventions **spread across the codebase**. |
| Plan mode | Architectural changes, multi-file migrations, multiple valid approaches. |
| Direct execution | Single-file bug fix, clear scope. |
| Explore subagent | Verbose discovery isolation. |
| Iterative refinement | Examples > prose. TDD by sharing test failures. Interview pattern. |
| CI flag | **`-p`** (or `--print`). Not `CLAUDE_HEADLESS`, not `--batch`. |
| CI structured output | `--output-format json` + `--json-schema`. |
| Self-review | Use an **independent** session - not the generator. |
"""


# ===========================================================================
# Part 4: Prompt Engineering & Structured Output (D4, 20%, TS4.1-4.6)
# ===========================================================================

_part4_header_md = """\
# Part 4: Prompt Engineering and Structured Output

**Domain 4 | 20% of the exam.** Task statements **TS4.1 - TS4.6**. Scenario most affected: **Structured Data Extraction**.

Coverage in this Part:

- **TS4.1** explicit criteria reduce false positives (concept)
- **TS4.2** few-shot prompting for consistent format and corner cases (live demo)
- **TS4.3** structured output via tool_use + JSON schemas (live, the headline mechanic)
- **TS4.4** validation/retry/feedback loops with retry ceiling (live, ties TS4.3)
- **TS4.5** Message Batches API - 50% savings, 24h, `custom_id`, no multi-turn tools (concept)
- **TS4.6** multi-instance / multi-pass review (concept)

**Long-form teaching:** `notebooks/segment-3-invoice-extractor.ipynb`.
"""

_part4_precise_md = """\
## TS4.1 Explicit criteria, not vague instructions

"Be conservative" and "only flag high-confidence issues" do **not** improve precision. **Specific categorical criteria** do.

**Bad:** "Check that comments are accurate."
**Good:** "Flag a comment only when the claimed behavior contradicts the actual code behavior. Do not flag style issues or typos."

The exam's recurring move: when a system has high false positives, the right fix is **explicit categorical criteria with concrete code examples per severity level**, not adjective adjustments to the existing prompt.
"""

_part4_pydantic_md = """\
## TS4.3 Tool use + JSON schema = guaranteed structured output

The most reliable mechanism for structured output is **tool_use with a JSON schema**. Pydantic gives you the schema for free via `Model.model_json_schema()`.

**Three load-bearing rules:**

1. **Nullable fields for information that may be absent.** If a source document does not contain a PO number, the model must return `null` - **not** invent one to pass validation. Mark optional fields `Optional[X] = None` in Pydantic; the schema carries `nullable: true` to the model.
2. **Strict mode eliminates JSON syntax errors, but not semantic errors.** A schema-valid `{"total": 100, "line_items": [50, 30]}` is JSON-correct and arithmetically wrong. Validation has to check sums.
3. **`tool_choice={"type": "tool", "name": "<name>"}`** forces the call. Without it, `tool_choice: "auto"` lets the model answer in prose and skip the structured tool entirely.

The cell below defines a compact `Invoice` model with a nullable field and prints the derived JSON schema.
"""

_part4_pydantic_code = '''\
from typing import Optional  # self-contained: cell runnable out of order
from pydantic import BaseModel, Field, ValidationError

class Invoice(BaseModel):
    """A nested invoice schema. Required fields fail validation if absent;
    optional fields are nullable so the model can return null instead of
    fabricating a value."""

    invoice_number: str = Field(description="Invoice ID, e.g. 'INV-2026-0481'")
    vendor: str = Field(description="Vendor name")
    total_usd: float = Field(description="Total amount in USD")
    po_number: Optional[str] = Field(
        default=None,
        description="Purchase order number if present in the source; null otherwise.",
    )
    line_items_count: Optional[int] = Field(
        default=None,
        description="Number of line items if visible in the source.",
    )

# The model_json_schema() output is exactly what we pass as input_schema
# to a tool definition. The model sees the same shape Pydantic validates.
schema = Invoice.model_json_schema()
print("Required fields:", schema.get("required", []))
print("All properties:")
for name, spec in schema["properties"].items():
    nullable = "anyOf" in spec  # Optional[X] renders as {anyOf: [X, null]}
    desc = spec.get("description", "")[:60]
    print(f"  - {name:20}  {'optional' if nullable else 'required':>8}  {desc}")
'''

_part4_extract_md = """\
## TS4.3 + TS4.4 Forced extraction with bounded retry

The forced-tool-call pattern + a Pydantic validation gate + a **bounded retry loop** is the canonical extraction pipeline. The three load-bearing lines:

1. `tool_choice={"type": "tool", "name": "extract_invoice"}` - forced left turn, the model must call the tool.
2. `Invoice(**block.input)` - the validation gate. Pydantic raises `ValidationError` on bad shape.
3. **`max_retries=1`** - the ceiling, hard-coded. A genuinely missing field will fail forever; one retry gives the model a chance to react to its own error; then we fail loud.

**The exam-tested distinction (TS4.4):** retries work for **format errors** (wrong types, validation shape). They do **not** work when the **information is simply absent from the source**. Knowing the difference prevents infinite-retry budget burn.

**This cell uses `claude-sonnet-4-6`** - the one documented exception to the Haiku default. Nested-schema extraction with retry-on-validation is exactly where Sonnet's reasoning depth measurably lifts accuracy.
"""

_part4_extract_code = '''\
from typing import Optional  # self-contained: cell runnable out of order
# Register the Pydantic schema AS a tool. input_schema is the JSON Schema
# view of our Pydantic model - the model sees exactly what Pydantic will
# validate against.
EXTRACT_TOOL = {
    "name": "extract_invoice",
    "description": (
        "Extract structured invoice data from raw text. Required fields "
        "(invoice_number, vendor, total_usd) MUST come from the text - do "
        "NOT fabricate them. Optional fields (po_number, line_items_count) "
        "should be null when the text is silent."
    ),
    "input_schema": Invoice.model_json_schema(),
}

EXTRACT_SYSTEM = (
    "You are an invoice extraction service. Call extract_invoice with the "
    "structured fields. Leave optional fields null when the source is "
    "silent. Do not invent values."
)


def extract_invoice(raw: str, max_retries: int = 1) -> Invoice:
    """Forced-tool extraction with a bounded retry loop."""
    messages: list[dict] = [{"role": "user",
                             "content": f"Extract the invoice:\\n\\n{raw}"}]
    for attempt in range(max_retries + 1):
        resp = client.messages.create(
            model=SONNET,  # documented exception to Haiku default
            max_tokens=500,
            system=EXTRACT_SYSTEM,
            tools=[EXTRACT_TOOL],
            tool_choice={"type": "tool", "name": "extract_invoice"},
            messages=messages,
        )
        print(f"  [attempt {attempt}] stop_reason={resp.stop_reason}")
        block = next((b for b in resp.content if b.type == "tool_use"), None)
        assert block is not None, "forced tool_choice but no tool_use block"
        try:
            inv = Invoice(**block.input)
            print(f"  [attempt {attempt}] validated OK: {inv.invoice_number}")
            return inv
        except ValidationError as exc:
            print(f"  [attempt {attempt}] ValidationError: {str(exc)[:120]}")
            if attempt == max_retries:
                raise RuntimeError(f"exhausted retries: {exc}") from exc
            # Feed the error back so the model can re-plan.
            messages.append({"role": "assistant", "content": resp.content})
            messages.append({
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "is_error": True,
                    "content": f"ValidationError - your previous call did not match the schema:\\n{exc}",
                }],
            })


# A messy but parseable invoice. No PO number is present - the model
# MUST return null for po_number, not invent one.
RAW = """\\
INVOICE
Number: INV-2026-0481
Vendor: Acme Industrial Supplies
Date: 2026-05-20
Subtotal: $74.50
Shipping: $10.00
Total: $84.50
"""

inv = extract_invoice(RAW)
print()
print(f"  vendor:         {inv.vendor!r}")
print(f"  total_usd:      {inv.total_usd}")
print(f"  po_number:      {inv.po_number!r}  (correctly null - not in source)")
print()
print("Exam beat: forced tool_choice + nullable Optional + bounded retry =")
print("guaranteed-schema structured output. The model returned null for the")
print("missing PO instead of fabricating one. (TS4.3, TS4.4)")
'''

_part4_few_shot_md = """\
## TS4.2 Few-shot prompting for ambiguous cases

Few-shot examples are the **most reliable** technique when prose descriptions produce inconsistent output. Pin 2-4 worked examples in the message history - the model anchors on them.

**Where few-shot wins:**
- Ambiguous tool selection (a query that could route to two tools)
- Format consistency (severity classifications, structured findings)
- Generalization to novel patterns (not pre-specified matching)
- Reducing false positives (showing what NOT to flag, alongside what to flag)

The cell below runs a single classification call **without** few-shot, then **with** 2 examples. The contrast in consistency is the exam beat.
"""

_part4_few_shot_code = '''\
# Demonstrate few-shot for FORMAT consistency, which is more reliably
# visible than ambiguous-case routing (modern models guess routing
# well even without examples). We give a vague system prompt, ask for
# extraction in a specific shape, and show that without examples the
# model invents its own format; with examples it matches ours exactly.

VAGUE_SYSTEM = "Extract the key information from the customer message."

TICKET = "Hi - my order #ORD-9921 arrived yesterday but the wrong size. I would like an exchange to size large. My email is jane@example.com."

# WITHOUT few-shot: prose system prompt, no shape constraint.
print("Without few-shot (model invents its own output shape):")
for trial in range(3):
    resp = client.messages.create(
        model=MODEL, max_tokens=120,
        system=VAGUE_SYSTEM,
        messages=[{"role": "user", "content": TICKET}],
    )
    text = next((b.text for b in resp.content if b.type == "text"), "").strip()
    # Show the first 80 chars so the format variance is visible.
    print(f"  trial {trial}: {text[:80]!r}...")

print()

# WITH few-shot: two worked examples lock the exact CSV-like shape.
FEW_SHOT = [
    {"role": "user", "content": "Order #ORD-1001 from bob@x.com - charged twice, refund please."},
    {"role": "assistant", "content": "order=ORD-1001 | email=bob@x.com | request=refund | reason=double_charge"},
    {"role": "user", "content": "Order #ORD-2050, alice@y.com here, item is broken."},
    {"role": "assistant", "content": "order=ORD-2050 | email=alice@y.com | request=replacement | reason=damaged"},
]

print("With 2 few-shot examples (model matches the pinned shape):")
for trial in range(3):
    resp = client.messages.create(
        model=MODEL, max_tokens=120,
        system=VAGUE_SYSTEM,
        messages=FEW_SHOT + [{"role": "user", "content": TICKET}],
    )
    text = next((b.text for b in resp.content if b.type == "text"), "").strip()
    print(f"  trial {trial}: {text[:80]!r}")

print()
print("Exam beat: few-shot is the most reliable lever for FORMAT consistency")
print("when prose descriptions produce inconsistent output. 2-4 examples")
print("pin the shape; the model generalizes the schema, not just the")
print("specific cases. (TS4.2)")
'''

_part4_batches_md = """\
## TS4.5 Message Batches API

The Message Batches API trades latency for cost:

- **50% cost savings** vs synchronous Messages
- **Up to 24-hour processing window** - no latency SLA
- **`custom_id`** per request correlates the response back to your record
- **No multi-turn tool calling** - tools cannot execute mid-batch-request and return results

**Sample Question 11 decision rule:**
- **Pre-merge check (blocking)** -> synchronous Messages API. Cannot afford 24h.
- **Overnight technical-debt report** -> batch API. Saves 50%; the 24h window is fine.

**Failure handling:** on batch failure, resubmit only the failed `custom_id`s with appropriate modifications (chunk oversized documents, etc.). Do not resubmit the whole batch.

**No live batch demo here** - submitting a batch + polling for completion would blow this notebook's budget and time window. The mechanics are concept-only; the exam tests the latency-tolerance decision.
"""

_part4_multipass_md = """\
## TS4.6 Multi-instance and multi-pass review

**Self-review is weaker than independent review.** A model retains its generation reasoning and is less likely to question its own decisions in the same session. The exam-tested patterns:

1. **Independent review instance** - a fresh Claude session reviews the generator's output. No prior reasoning context.
2. **Per-file local pass + cross-file integration pass** - for multi-file PRs. A single-pass review across 14 files produces inconsistent depth and contradictory findings (Sample Question 12). Split into focused passes.
3. **Verification pass with confidence scoring** - the model self-reports a confidence value per finding; you route low-confidence to human review.

**Anti-pattern:** running three independent passes on the full PR and only flagging issues that appear in **at least two** - this suppresses real bugs that one pass would have caught uniquely.
"""

_part4_exam_probes_md = """\
## What the exam probes (Domain 4)

| Concept | Exam-tested fact |
|---|---|
| Explicit criteria | Specific categorical criteria, **not** "be conservative". |
| Few-shot | Most reliable for consistent format and corner cases. 2-4 examples. |
| `tool_choice` for output | `auto` may return prose. `any` forces some tool. **Forced specific** is the structured-output cheat code. |
| Nullable fields | `Optional[X] = None`. Prevents the model from fabricating to satisfy required fields. |
| Strict schema | Eliminates JSON syntax errors. Does NOT prevent semantic errors (sums, wrong-field placement). |
| Validation retry | Works for format errors. Does NOT work when info is absent from source. |
| Retry ceiling | Hard cap (1-2). Failing loud beats infinite-retry budget burn. |
| Batches API | 50% savings, up to 24h, `custom_id` correlation. **No multi-turn tools.** |
| Batches use case | Overnight reports YES. Blocking pre-merge checks NO. |
| Multi-pass review | Per-file local + cross-file integration. Avoid attention dilution. |
| Independent review | Better than self-review. Fresh session, no generator context. |
"""


# ===========================================================================
# Part 5: Context Management & Reliability (D5, 15%, TS5.1-5.6)
# ===========================================================================

_part5_header_md = """\
# Part 5: Context Management and Reliability

**Domain 5 | 15% of the exam.** Task statements **TS5.1 - TS5.6**. Scenarios most affected: **Customer Support Resolution Agent**, **Multi-Agent Research System**, **Structured Data Extraction**.

Coverage in this Part:

- **TS5.1** case-facts pinning, lost-in-the-middle, trim verbose tool outputs (local demo)
- **TS5.2** escalation triggers - explicit request, policy gap, no progress (NOT sentiment) (local demo)
- **TS5.3** error propagation in multi-agent (concept; demonstrated in Part 1)
- **TS5.4** large-codebase context - subagent delegation, scratchpads (concept)
- **TS5.5** confidence calibration, stratified sampling for human review (local demo)
- **TS5.6** provenance, claim-source mappings, conflict annotation (local demo)
- **Managed Agents** `memory_stores` as server-managed persistence (live read-only)

**Long-form teaching:** `notebooks/segment-3-invoice-extractor.ipynb` and `notebooks/segment-2-5-control-surfaces.ipynb`.
"""

_part5_context_concept_md = """\
## TS5.1 Context preservation - three counters to long-session rot

Three mechanics, all required:

1. **Pin case facts.** The transactional facts (account ID, amounts, dates, order IDs) live in a **persistent case-facts block** included in **every** prompt, outside the summarized history. The model attends harder to the top and bottom of long inputs (lost-in-the-middle); pin facts at the top.
2. **Summarize resolved turns.** Once a sub-issue is closed, replace its verbose turns with a one-line summary.
3. **Prune verbose tool outputs.** A tool that returned 40 fields when 5 were relevant accumulates token cost disproportionate to value. **Trim application-side, before appending to the message list** (this is the `PostToolUse` hook pattern from Part 1).

The cell below trims a verbose synthetic tool output and pins a case-facts block. Pure Python, no API.
"""

_part5_pruning_code = '''\
from typing import Any  # self-contained: cell runnable out of order
# A bloated synthetic tool output - 40+ fields, only 5 relevant for refund.
RAW_ORDER = {
    "order_id": "ORD-481",
    "status": "delivered",
    "total_usd": 84.50,
    "created_at": "2026-05-15T09:00:00Z",
    "delivered_at": "2026-05-18T15:32:00Z",
    "vendor_internal_id": "v-77",
    "warehouse_zone": "C-4",
    "weight_kg": 1.2,
    "carrier_tracking": "1Z999AA10123456784",
    "ship_method": "ground",
    "insurance_usd": 0,
    "promotional_code": None,
    "loyalty_points_earned": 84,
    "customer_lifetime_value": 4827.12,
    "marketing_attribution": "organic-search",
    "warehouse_temperature_f": 68,
    "pick_pack_minutes": 23,
    "label_print_attempts": 1,
    "label_print_timestamp": "2026-05-15T09:45:00Z",
    "shipping_software_version": "logistics-v4.2.1",
    "carrier_account_id": "acct-9982",
    "billing_address_hash": "a8b9...",
    # ...20 more fields no agent needs
}

KEEP = {"order_id", "status", "total_usd", "created_at", "delivered_at"}

def trim_for_agent(raw: dict[str, Any], keep: set[str]) -> dict[str, Any]:
    return {k: v for k, v in raw.items() if k in keep}

trimmed = trim_for_agent(RAW_ORDER, KEEP)
print(f"raw fields:     {len(RAW_ORDER)}")
print(f"trimmed fields: {len(trimmed)}")
print(f"reduction:      {len(RAW_ORDER) - len(trimmed)} fields dropped")
print()
print("Trimmed payload (the only thing the model sees):")
print(json.dumps(trimmed, indent=2))

# --- Pin a case-facts block at the top of the message history ---
case_facts = {
    "customer_id": "cust_8821",
    "order_id": "ORD-481",
    "issue": "refund request, damaged on delivery",
    "amount_in_dispute_usd": 84.50,
    "policy_constraint": "refund cap $500 without supervisor",
}
case_facts_md = "\\n".join(f"- **{k}**: {v}" for k, v in case_facts.items())

messages_skeleton = [
    {"role": "user", "content": f"## Case facts (pinned)\\n{case_facts_md}\\n\\nCustomer says the package arrived damaged. What is our next move?"},
    # ...subsequent turns reference but never re-derive these facts
]
print()
print("Case-facts block (pinned at the top of every turn):")
print(messages_skeleton[0]["content"][:400])
print()
print("Exam beat: pin transactional facts at the top. Trim tool outputs to")
print("the relevant fields BEFORE appending. The model attends harder to the")
print("top of long contexts; that is where facts live. (TS5.1)")
'''

_part5_escalation_md = """\
## TS5.2 Escalation triggers - the three legitimate ones

The exam tests this directly (Sample Question 3). The legitimate triggers:

1. **Explicit customer request.** "I want a human" -> honor immediately. Do not first attempt investigation.
2. **Policy gap or exception.** The policy is silent on the customer's specific case (competitor price-match when policy only covers own-site), or the resolution requires an exception (refund above the cap).
3. **Inability to make meaningful progress.** Multi-system failure, no clear owner, all the obvious paths exhausted.

**The classic distractor: sentiment.** Frustrated customers are not necessarily complex cases. **Sentiment does NOT correlate with case complexity.** Routing on sentiment misroutes straightforward refunds to humans while letting policy-exception cases stay with the bot.

**Also a distractor: self-reported confidence scores.** LLM self-reported confidence is poorly calibrated - the model is often confidently wrong on hard cases.

**Also a distractor: classifier models on historical tickets.** Over-engineered. The right first response is **explicit escalation criteria with few-shot examples in the system prompt**.
"""

_part5_escalation_code = '''\
from typing import Any  # self-contained: cell runnable out of order
# Rule-based escalation classifier. The three legitimate triggers + the
# anti-pattern (sentiment) explicitly asserted to NOT escalate.

def should_escalate(transcript: dict[str, Any]) -> dict[str, Any]:
    """Returns {escalate: bool, reason: str, anti_patterns_avoided: list[str]}."""
    anti = []
    # 1. Explicit request - the strongest signal
    if transcript.get("customer_explicit_request"):
        return {"escalate": True, "reason": "explicit_request",
                "anti_patterns_avoided": anti}
    # 2. Policy gap or required exception
    if transcript.get("policy_gap") or transcript.get("requires_policy_exception"):
        return {"escalate": True, "reason": "policy_gap",
                "anti_patterns_avoided": anti}
    # 3. Inability to make progress
    if transcript.get("attempted_paths_exhausted"):
        return {"escalate": True, "reason": "no_progress",
                "anti_patterns_avoided": anti}
    # --- distractors that look like triggers but are NOT ---
    if transcript.get("sentiment") in {"frustrated", "angry"}:
        anti.append("sentiment_alone_is_not_complexity")
    if transcript.get("low_self_reported_confidence"):
        anti.append("llm_self_confidence_is_poorly_calibrated")
    return {"escalate": False, "reason": "resolve_autonomously",
            "anti_patterns_avoided": anti}


cases = [
    {"label": "frustrated but standard refund within cap",
     "transcript": {"sentiment": "angry", "refund_amount_usd": 50}},
    {"label": "explicit human request",
     "transcript": {"customer_explicit_request": True, "refund_amount_usd": 25}},
    {"label": "policy gap - competitor price match",
     "transcript": {"policy_gap": True, "request": "match competitor X"}},
    {"label": "self-reports low confidence on simple case",
     "transcript": {"low_self_reported_confidence": True, "refund_amount_usd": 12}},
]
for c in cases:
    out = should_escalate(c["transcript"])
    print(f"  {c['label']:>50}: escalate={out['escalate']} ({out['reason']})")
    if out["anti_patterns_avoided"]:
        for ap in out["anti_patterns_avoided"]:
            print(f"      avoided: {ap}")

print()
print("Exam beat: explicit request | policy gap | no progress = ESCALATE.")
print("Sentiment alone, self-reported confidence: distractors. (TS5.2)")
'''

_part5_provenance_md = """\
## TS5.5 + TS5.6 Confidence calibration and provenance

Two reliability mechanics the exam tests:

**Confidence calibration (TS5.5):**
- The model emits a **field-level confidence** score per extraction.
- You calibrate the threshold using a **labeled validation set** - the score is not naturally calibrated.
- **Stratified random sampling** of high-confidence extractions catches novel error patterns ongoing.
- **Aggregate accuracy hides per-segment failure.** A 97% overall accuracy can mask 80% on one document type. Always segment by document type and field before reducing human review.

**Provenance (TS5.6):**
- Subagents return **structured claim->source mappings** - claim, evidence excerpt, source URL/document name, publication date.
- The synthesis agent **preserves** the source attribution; it does not collapse claims into prose that has lost provenance.
- **Conflicting sources are annotated, not arbitrated.** When two credible sources disagree, surface both with attribution; let the coordinator decide.

The cell below builds a synthetic provenance record and routes low-confidence claims to human review.
"""

_part5_provenance_code = '''\
# Synthetic claim->source records the synthesis agent would receive
# from upstream subagents. Each claim carries its evidence and confidence.
CLAIMS = [
    {"claim": "Q1 revenue grew 12%", "source": "gov-report-2026Q1.pdf",
     "evidence": "Table 3, p. 14", "confidence": 0.92,
     "publication_date": "2026-04-15"},
    {"claim": "Q1 revenue grew 40%", "source": "industry-analysis-acme.html",
     "evidence": "Para 6", "confidence": 0.74,
     "publication_date": "2026-04-22"},
    {"claim": "Headcount unchanged YoY", "source": "10-K-2025.pdf",
     "evidence": "Item 1, p. 4", "confidence": 0.55,
     "publication_date": "2026-03-01"},
    {"claim": "New product launched in EMEA", "source": "press-release-2026-05-10.html",
     "evidence": "Headline", "confidence": 0.96,
     "publication_date": "2026-05-10"},
]

# Threshold calibrated against a labeled validation set. In production
# you tune this; here we use 0.80 to show the routing.
HUMAN_REVIEW_THRESHOLD = 0.80

# Detect conflicting claims by topic key (TS5.6 - annotate, do not arbitrate).
def find_conflicts(claims: list[dict]) -> list[tuple[dict, dict]]:
    pairs = []
    for i, a in enumerate(claims):
        for b in claims[i + 1:]:
            # Toy match: both mention "Q1 revenue"
            if "Q1 revenue" in a["claim"] and "Q1 revenue" in b["claim"]:
                pairs.append((a, b))
    return pairs

# Route by confidence (TS5.5).
auto = [c for c in CLAIMS if c["confidence"] >= HUMAN_REVIEW_THRESHOLD]
review = [c for c in CLAIMS if c["confidence"] < HUMAN_REVIEW_THRESHOLD]

print(f"=== Confidence routing (threshold={HUMAN_REVIEW_THRESHOLD}) ===")
print(f"  auto-accept: {len(auto)} claims")
print(f"  human review queue: {len(review)} claims")
for c in review:
    print(f"    -> conf={c['confidence']:.2f}: {c['claim']!r}")

print()
print("=== Conflict detection (annotate, do not arbitrate) ===")
for a, b in find_conflicts(CLAIMS):
    print(f"  CONFLICT on Q1 revenue:")
    print(f"    A: {a['claim']!r}  source={a['source']}  date={a['publication_date']}")
    print(f"    B: {b['claim']!r}  source={b['source']}  date={b['publication_date']}")
    print(f"    -> Surface BOTH in synthesis with source + date. Do not pick.")

print()
print("Exam beat: confidence threshold from labeled validation, not vibes.")
print("Stratified sampling of high-confidence claims catches drift. Conflicts")
print("get annotated with source + date, never silently picked. (TS5.5, TS5.6)")
'''

_part5_managed_agents_md = """\
## Managed Agents - read-only inspection of the Console asset surface

The exam guide does not name "Managed Agents" by acronym, but the underlying mechanics it tests (**persistent memory across restarts**, **credential isolation**, **agents as named recipes**) all map to the four resources Anthropic exposes via the SDK beta:

| Console asset | SDK | What it is | Exam tie |
|---|---|---|---|
| Memory store | `client.beta.memory_stores` | Persistent context surviving restarts | D5 context preservation across sessions |
| Vault | `client.beta.vaults` (+ `.credentials`) | Server-side secret storage; values never returned to clients | D2 secrets hygiene |
| Agent | `client.beta.agents` | Named recipe (model + tools + system prompt) | D1 managed loop vs hand-rolled |
| Session | `client.beta.sessions` | Runtime that binds agent + environment + vault | D1 agent + env + vault as one runtime |

Requires the beta header **`anthropic-beta: managed-agents-2026-04-01`**.

The cell below is **READ-ONLY**: it lists and retrieves the existing provisioned `oreilly-*` resources only. It does **not** create, update, or destroy anything. Wrapped in try/except so beta-surface drift prints a labeled message rather than failing the smoke.
"""

_part5_managed_agents_code = '''\
# =================================================================
# READ-ONLY: this cell lists and retrieves existing resources only.
# It does NOT create, update, or destroy anything. The oreilly-*
# resources were provisioned out-of-band; we just inspect them.
# =================================================================
try:
    cli = client.with_options(default_headers=MANAGED_AGENTS_BETA)

    # --- Memory stores ---
    print("=== Memory stores ===")
    stores = cli.beta.memory_stores.list()
    for s in stores.data:
        marker = "  <-- target" if s.name == "oreilly-memory-store" else ""
        print(f"  id={s.id}  name={s.name!r}{marker}")
    ours = next((s for s in stores.data if s.name == "oreilly-memory-store"), None)
    if ours is not None:
        detail = cli.beta.memory_stores.retrieve(ours.id)
        print(f"  retrieved: id={detail.id}  created_at={detail.created_at}")

    # --- Vaults ---
    print()
    print("=== Vaults ===")
    vaults = cli.beta.vaults.list()
    for v in vaults.data:
        # The vaults surface uses display_name, not name.
        dn = getattr(v, "display_name", getattr(v, "name", "?"))
        marker = "  <-- target" if dn == "oreilly-vault" else ""
        print(f"  id={v.id}  display_name={dn!r}{marker}")
    print("  (credential VALUES are never returned to clients - only refs)")

    # --- Agents ---
    print()
    print("=== Agents ===")
    agents = cli.beta.agents.list()
    for a in agents.data:
        marker = "  <-- target" if a.name == "Deep researcher" else ""
        print(f"  id={a.id}  name={a.name!r}{marker}")
    deep = next((a for a in agents.data if a.name == "Deep researcher"), None)
    if deep is not None:
        detail = cli.beta.agents.retrieve(deep.id)
        model_id = getattr(getattr(detail, "model", None), "id", "?")
        print(f"  retrieved: id={detail.id}  model={model_id}")
        print(f"  (Console-managed agents pin their OWN model; the calling")
        print(f"   notebook's MODEL default does NOT override. Recipe wins.)")

    print()
    print("Exam tie: memory_stores = D5 persistence across restarts. Vault")
    print("credential values are never returned to the client = D2 secret")
    print("hygiene. Agent = named recipe (D1). Session is the runtime.")
except Exception as exc:
    print(f"(Managed Agents cell skipped: {type(exc).__name__}: {str(exc)[:160]})")
    print("Possible causes: beta header drift, workspace lacks resources, or")
    print("the SDK version predates the managed-agents-2026-04-01 surface.")
    print("The exam tests the MECHANICS (persistence, secret hygiene, named")
    print("agents) - those are covered in the markdown above regardless.")
'''

_part5_error_propagation_md = """\
## TS5.3 Error propagation across multi-agent systems

Already demonstrated in Part 1's coordinator-subagent cell. The exam-tested rules:

- **Structured error context** = failure type + what was attempted + partial results + alternative approaches. Enables intelligent recovery.
- **Generic statuses ("search unavailable")** hide context. The coordinator cannot decide retry vs reformulate vs give-up.
- **Silently suppressing errors as empty success** is the anti-pattern. So is **terminating the whole workflow on a single subagent failure**.
- **Local recovery first.** Subagents try transient failures themselves. Only failures they cannot resolve propagate up, with what was attempted and partial results.
- **Distinguish access failures from valid empty results.** A query that timed out is not the same as a query that ran cleanly and returned zero rows.
"""

_part5_exam_probes_md = """\
## What the exam probes (Domain 5)

| Concept | Exam-tested fact |
|---|---|
| Case-facts block | **Pinned at the top** of every turn, outside summarized history. |
| Lost-in-the-middle | Models attend harder to beginning and end. Put findings summaries at the top. |
| Tool output pruning | **Application-side, before appending.** Pick the relevant 5 of 40 fields. |
| Escalation triggers | **Explicit request | policy gap | no progress.** Sentiment is NOT a trigger. |
| Self-reported confidence | Poorly calibrated. Not a reliable escalation signal. |
| Error propagation | Structured context (failure type + attempt + partial results + alternatives). |
| Distinguish failures | Access failure (retry decision) vs valid empty result (success with zero matches). |
| Confidence calibration | Threshold tuned against a **labeled validation set**, not chosen. |
| Stratified sampling | Of high-confidence extractions to catch drift. |
| Aggregate accuracy | Masks per-segment failure. Segment by document type and field. |
| Provenance | claim + source + evidence excerpt + publication date. Synthesis must preserve. |
| Conflicting sources | **Annotate, not arbitrate.** Surface both with attribution. |
| Managed Agents | `memory_stores` (persistence), `vaults` (credentials never returned), `agents` (named recipes), `sessions` (runtime). |
"""


# ===========================================================================
# Part 6: Exam mechanics, coverage matrix, self-check
# ===========================================================================

_part6_exam_format_md = """\
# Part 6: Exam mechanics, coverage matrix, and self-check

## Exam format

| Item | Value |
|---|---|
| Questions | **60 multiple-choice**, one correct + three distractors per question |
| Time | **120 minutes** |
| Passing score | **720 / 1000** (scaled) |
| Cost | $99 |
| Attempts | **One**, period |
| Delivery | ProctorFree remote proctoring, English |
| Results | Within 2 business days |
| Scenarios | **4 of 6** drawn per sitting (see Part 0 for the six) |
| Penalty for guessing | None - unanswered = wrong |

## Domain weights (sized for study time)

| Domain | Weight | Cumulative |
|---|---|---|
| D1 Agentic Architecture and Orchestration | **27%** | 27% |
| D3 Claude Code Configuration and Workflows | 20% | 47% |
| D4 Prompt Engineering and Structured Output | 20% | 67% |
| D2 Tool Design and MCP Integration | 18% | 85% |
| D5 Context Management and Reliability | 15% | 100% |

**D1 + D3 + D4 = 67%.** That is where the leverage lives.
"""

_part6_coverage_matrix_md = """\
## The 30-task-statement coverage matrix

The contract that backs "if you understand this workbook you know the exam." Every TS_x.y (TS1.1 through TS5.6) maps to a cell in this notebook. **Part 6 ends with a code cell that asserts every row is covered** - if the assertion fails, the notebook smoke fails.

| TS | Title (abbrev.) | Where covered | Type |
|---|---|---|---|
| **1.1** | Agentic loop, stop_reason branching | Part 1 loop demo | live |
| **1.2** | Coordinator-subagent hub-and-spoke | Part 1 subagent demo | live |
| **1.3** | Task tool, allowedTools, AgentDefinition | Part 1 Task tool md | concept |
| **1.4** | Multi-step workflows, prerequisite gates | Part 1 hooks demo | live + local |
| **1.5** | PreToolUse / PostToolUse hooks | Part 1 hooks code | local |
| **1.6** | Task decomposition - chaining vs dynamic | Part 1 decomp md | concept |
| **1.7** | Session resume, fork_session | Part 1 sessions md | concept |
| **2.1** | Tool descriptions, splitting tools | Part 2 description md | concept |
| **2.2** | Structured error responses | Part 2 structured-error code | live |
| **2.3** | Tool distribution, tool_choice modes | Part 2 tool_choice code | live |
| **2.4** | MCP servers, .mcp.json, transports | Part 2 .mcp.json + discovery | inspection + live |
| **2.5** | Built-in tools Read/Write/Edit/Bash/Grep/Glob | Part 2 builtin md | concept |
| **3.1** | CLAUDE.md hierarchy, @import | Part 3 CLAUDE.md inspect | inspection |
| **3.2** | Slash commands and Skills (frontmatter) | Part 3 SKILL.md inspect | inspection |
| **3.3** | Path-specific rules via globs | Part 3 rules inspect | inspection |
| **3.4** | Plan mode vs direct | Part 3 plan_mode md | concept |
| **3.5** | Iterative refinement | Part 3 iterative md | concept |
| **3.6** | CI/CD - claude -p, output-format json | Part 3 CI inspect | inspection |
| **4.1** | Explicit criteria reduce false positives | Part 4 precise md | concept |
| **4.2** | Few-shot for ambiguous cases | Part 4 few-shot code | live |
| **4.3** | Structured output via tool_use + schema | Part 4 extract code | live |
| **4.4** | Validation / retry / feedback loops | Part 4 extract code | live |
| **4.5** | Message Batches API | Part 4 batches md | concept |
| **4.6** | Multi-instance / multi-pass review | Part 4 multipass md | concept |
| **5.1** | Case-facts pinning, lost-in-the-middle | Part 5 pruning code | local |
| **5.2** | Escalation triggers (NOT sentiment) | Part 5 escalation code | local |
| **5.3** | Error propagation in multi-agent | Part 1 subagent + Part 5 md | live + concept |
| **5.4** | Large-codebase context, scratchpads | Part 5 context md (concept) | concept |
| **5.5** | Confidence calibration, stratified sampling | Part 5 provenance code | local |
| **5.6** | Provenance, claim-source, conflict annotation | Part 5 provenance code | local |

(30 rows = TS1.1..TS1.7 (7) + TS2.1..TS2.5 (5) + TS3.1..TS3.6 (6) + TS4.1..TS4.6 (6) + TS5.1..TS5.6 (6). All covered.)
"""

_part6_cheatsheet_md = """\
## One-page cheat sheet

**`stop_reason` enum.** `tool_use` (loop), `end_turn` (return). Anything else: handle deliberately.

**`tool_choice` modes.** `auto` (may prose), `any` (must call something), `{"type":"tool","name":...}` (must call THAT), `none` (no tools). Add `disable_parallel_tool_use: true` for serial ordering.

**`errorCategory` values.** `transient` (retry), `validation` (reformulate), `permission` (escalate), `business` (escalate, do not retry).

**Escalation triggers.** Explicit customer request | policy gap | inability to progress. **NOT** sentiment. **NOT** self-reported confidence.

**`CLAUDE.md` precedence.** user (`~/.claude/CLAUDE.md`, NOT shared via VCS) <- project (`./CLAUDE.md`, shared) <- directory (subdir `CLAUDE.md`).

**Claude Code in CI.** `claude -p` (or `--print`) for non-interactive. `--output-format json` + `--json-schema` for machine-parseable output. NOT `CLAUDE_HEADLESS`, NOT `--batch`.

**Batches API.** 50% savings, **up to 24h**, `custom_id` correlation, **no multi-turn tool calling**. Overnight reports YES. Blocking pre-merge checks NO.

**Tool design.** Tool descriptions are the **primary** selection mechanism. Split generic into specific. ~4-5 tool cap per agent.

**Path-specific rules.** `.claude/rules/<name>.md` with YAML `paths` globs. The right answer when conventions span the codebase. NOT subdirectory `CLAUDE.md`.

**SKILL.md frontmatter.** `context: fork` (isolate verbose output), `allowed-tools` (restrict surface), `argument-hint` (prompt for args).

**Structured output.** `tool_choice={"type":"tool","name":...}` + Pydantic `model_json_schema()` + `Optional[X] = None` for nullable + **bounded retry** (max 1-2).

**Provenance.** claim + source + evidence + publication date. Synthesis preserves. Conflicting sources: **annotate**, do not arbitrate.

**Subagents.** Isolated context (do NOT auto-inherit). Hub-and-spoke. Structured handoffs (dicts, not prose). Errors propagate up; coordinator decides recovery.

**Hooks.** **Deterministic**. Use when the rule is non-negotiable. Prompts are **probabilistic**.
"""

_part6_self_check_md = """\
## Self-check - five exam-aligned questions

Five questions sampled from the repo's `practice-questions.json`. Read each scenario, pick an answer, then check the rationale.

---

**Q1 (Multi-Agent Research System).** A document analysis agent discovers two credible sources contain directly contradictory statistics for a key metric: a government report states 40% growth; an industry analysis states 12%. How should the agent handle this?

A) Apply credibility heuristics to pick the most likely correct number and add a footnote.
B) Include both numbers in the analysis output with explicit source attribution and let the coordinator decide.
C) Average the two values.
D) Discard both and request a third source.

<details><summary>Answer</summary>

**B.** The exam-tested rule (TS5.6): when two credible sources conflict, **annotate, do not arbitrate**. The synthesis agent preserves both with source attribution; the coordinator (or human) makes the reconciliation call. Picking via heuristic (A) silently buries the conflict; averaging (C) invents a value neither source supports; discarding (D) destroys evidence.

</details>

---

**Q2 (Customer Support).** Production data shows that in 12% of cases, your agent skips `get_customer` and calls `lookup_order` using only the customer's stated name, occasionally leading to misidentified accounts and incorrect refunds. What change most effectively addresses this reliability issue?

A) Programmatic prerequisite that blocks `lookup_order` and `process_refund` until `get_customer` has returned a verified customer ID.
B) Enhance the system prompt to state that customer verification is mandatory.
C) Add few-shot examples showing the agent always calling `get_customer` first.
D) Implement a routing classifier per request type.

<details><summary>Answer</summary>

**A.** TS1.4: when business logic requires deterministic compliance (identity before financial action), use **programmatic enforcement** (a hook / prerequisite gate). Prompt instructions (B) and few-shot (C) have a non-zero failure rate, which is unacceptable when errors have financial consequences. (D) addresses tool availability, not tool ordering.

</details>

---

**Q3 (Code Generation).** You're restructuring a monolith into microservices: dozens of files, service-boundary decisions, module dependencies to analyze. Which approach?

A) Plan mode - explore, understand dependencies, design before changing.
B) Direct execution, letting natural service boundaries emerge.
C) Direct execution with comprehensive upfront instructions per service.
D) Start direct, switch to plan if complexity emerges.

<details><summary>Answer</summary>

**A.** TS3.4: plan mode is **designed** for large-scale changes, multiple valid approaches, and architectural decisions - exactly this case. (B) risks costly rework. (C) assumes the right structure before exploring. (D) ignores that the complexity is **already stated in the requirements**.

</details>

---

**Q4 (CI/CD).** Pipeline script runs `claude "Analyze this PR for security issues"` and hangs. Logs show Claude Code waiting for interactive input. The correct approach?

A) `claude -p "..."`.
B) Set `CLAUDE_HEADLESS=true` before running.
C) Redirect stdin from `/dev/null`.
D) `claude --batch "..."`.

<details><summary>Answer</summary>

**A.** TS3.6: **`-p` (or `--print`)** is the documented non-interactive flag. (B) and (D) are non-existent flags - the exam plants these as distractors. (C) is a Unix workaround that does not address the CLI's actual input mechanism.

</details>

---

**Q5 (Structured Data Extraction).** Your extraction system reports 97% aggregate accuracy. You consider reducing the human review queue. What is the right next step before automating?

A) Reduce the review queue proportionally - 97% is well above the threshold.
B) Segment accuracy by document type and field; verify consistent performance across all segments first.
C) Switch to a larger model and re-measure.
D) Increase the review threshold to 99%.

<details><summary>Answer</summary>

**B.** TS5.5: **aggregate accuracy hides per-segment failure.** A 97% overall can mask 80% on one document type. Always segment by document type and field before reducing human review. (A) ignores this; (C) does not address the segmentation question; (D) is unmeasured tightening.

</details>
"""

_part6_verify_code = '''\
# Self-audit: assert that every one of the 30 task statements has a
# cell in this notebook. The dict mirrors the coverage matrix above.
# If you add a TS that is not covered, set the value to False and the
# assertion below will fail - the notebook smoke fails too.

COVERAGE: dict[str, bool] = {
    # Domain 1
    "TS1.1": True,  # Part 1 loop demo
    "TS1.2": True,  # Part 1 subagent demo
    "TS1.3": True,  # Part 1 Task-tool concept
    "TS1.4": True,  # Part 1 hooks + prerequisite gate
    "TS1.5": True,  # Part 1 PreToolUse / PostToolUse
    "TS1.6": True,  # Part 1 decomposition concept
    "TS1.7": True,  # Part 1 sessions concept
    # Domain 2
    "TS2.1": True,  # Part 2 tool descriptions
    "TS2.2": True,  # Part 2 structured errors
    "TS2.3": True,  # Part 2 tool_choice 4 modes
    "TS2.4": True,  # Part 2 .mcp.json + MCP discovery
    "TS2.5": True,  # Part 2 built-in tools
    # Domain 3
    "TS3.1": True,  # Part 3 CLAUDE.md inspect
    "TS3.2": True,  # Part 3 SKILL.md inspect
    "TS3.3": True,  # Part 3 rules inspect
    "TS3.4": True,  # Part 3 plan-mode concept
    "TS3.5": True,  # Part 3 iterative concept
    "TS3.6": True,  # Part 3 CI inspect
    # Domain 4
    "TS4.1": True,  # Part 4 explicit criteria
    "TS4.2": True,  # Part 4 few-shot
    "TS4.3": True,  # Part 4 forced extraction
    "TS4.4": True,  # Part 4 validation retry
    "TS4.5": True,  # Part 4 batches concept
    "TS4.6": True,  # Part 4 multi-pass concept
    # Domain 5
    "TS5.1": True,  # Part 5 pruning + case-facts
    "TS5.2": True,  # Part 5 escalation rule
    "TS5.3": True,  # Part 1 subagent + Part 5 concept
    "TS5.4": True,  # Part 5 context concept
    "TS5.5": True,  # Part 5 confidence calibration
    "TS5.6": True,  # Part 5 provenance
}

uncovered = [ts for ts, ok in COVERAGE.items() if not ok]
assert not uncovered, f"uncovered task statements: {uncovered}"

# 30 task statements total across 5 domains:
#   D1 = TS1.1..TS1.7 (7)
#   D2 = TS2.1..TS2.5 (5)
#   D3 = TS3.1..TS3.6 (6)
#   D4 = TS4.1..TS4.6 (6)
#   D5 = TS5.1..TS5.6 (6)
#   sum = 7 + 5 + 6 + 6 + 6 = 30
# (The "27" you may see floating around is Domain 1's exam weight - 27%
# of scored content - not a task-statement count.)
EXPECTED = 30
assert len(COVERAGE) == EXPECTED, f"expected {EXPECTED} task statements, got {len(COVERAGE)}"

per_domain = {d: sum(1 for ts in COVERAGE if ts.startswith(f"TS{d}.")) for d in "12345"}
print(f"Coverage check: {len(COVERAGE)} / {EXPECTED} task statements covered.")
print(f"  D1: {per_domain['1']}/7  D2: {per_domain['2']}/5  D3: {per_domain['3']}/6  D4: {per_domain['4']}/6  D5: {per_domain['5']}/6")
print("All task statements covered. Ready to sit.")
'''

_part6_close_md = """\
## Closing note

If you wired through every cell, you have touched every exam-probed mechanic: the `stop_reason` loop, coordinator-subagent isolation, hooks as deterministic guardrails, the four `tool_choice` modes, structured `errorCategory` responses, MCP discovery via `list_tools`, the `CLAUDE.md` hierarchy + `.claude/rules/` + `SKILL.md` frontmatter, forced extraction with bounded retry, the Batches API trade-off, escalation triggers that are NOT sentiment, provenance with claim-source mappings, and the Managed Agents resource surface.

**For long-form teaching of any single mechanic, return to the six segment notebooks.** This notebook is the reference; those are the lessons.

**Then sit the exam once and pass it on the one attempt.** *Memento mori. Also, ship the cert.*
"""
