# A2A Agent Orchestration Skill

> Multi-agent coordination — discover capabilities, dispatch tasks, stream results, and manage remote agent lifecycles via the A2A protocol.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Achieves |
|----------|-------|----------|
| Discover & Dispatch | 3 | Find agent → verify → send task |
| Stream Results | 1 | Real-time partial outputs |
| Monitor | 1-2 | Track task to completion |
| Cancel | 1 | Abort stuck tasks |

### Without this skill:
- Tasks dispatched to wrong agents (capability mismatch)
- No timeout — tasks run forever
- Sensitive data sent to unvalidated agents
- Fire-and-forget with no completion tracking

### With this skill:
- Agent capabilities verified before dispatch
- Explicit timeouts on every task
- Agent cards validated before trusting
- Every task tracked to completion or failure

## Installation

```bash
git clone https://github.com/zavora-ai/skill-a2a-agent-orchestration.git \
  ~/.skills/skills/a2a-agent-orchestration
```

## Requirements

**Required:** `mcp-a2a (10 tools)`

**Cross-MCP:** mcp-workflow (pipeline coordination), mcp-slack (completion notifications)

## Folder Structure

```
a2a-agent-orchestration/
├── SKILL.md                       # Decision tree + workflows + MUST DO/MUST NOT DO
├── scripts/
│   └── select_agent.py
├── references/
│   ├── tool-sequences.md
│   ├── cross-mcp-workflows.md
│   └── examples.md
├── README.md
└── LICENSE
```

## Example

**User:** "Delegate research to the best available agent"

**Result:**
```
✅ Task dispatched to research-agent (match: 92%)
Streaming results... 3 findings so far.
ETA: 2 minutes remaining.
```

## Scripts

### `select_agent.py`
```bash
python scripts/select_agent.py '{"requirements": ["research", "analysis"], "agents": [...]}'
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
