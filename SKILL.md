---
name: a2a-agent-orchestration
description: Orchestrate remote AI agents via A2A protocol — discover agent cards, dispatch tasks, stream results, cancel tasks, and manage push notifications. Use when delegating work to remote agents, checking agent capabilities, coordinating multi-agent workflows, or monitoring task progress.
license: Apache-2.0
compatibility: Requires mcp-a2a server connected.
allowed-tools: [fetch_agent_card, validate_agent_card, list_agents, send_task, send_task_streaming, get_task, list_tasks, cancel_task, subscribe_events, manage_push_notifications]
metadata:
  category: platform
  author: Zavora AI
  mcp-server: mcp-a2a
  success-criteria:
    trigger-rate: "90% on agent delegation queries"
    task-completion: "Track every dispatched task to completion"
---

# A2A Agent Orchestration

You coordinate work across remote AI agents. Discover capabilities, dispatch tasks, stream results, and handle failures. Always validate agent cards before trusting capabilities.

## Decision Tree
```
├── "delegate", "send to agent", "dispatch"? → send_task / send_task_streaming
├── "what agents", "capabilities", "who can"? → list_agents / fetch_agent_card
├── "task status", "progress", "check on"? → get_task / list_tasks
├── "cancel", "stop task"? → cancel_task
├── "subscribe", "notifications"? → subscribe_events / manage_push_notifications
```

## Key Workflows

### Discover and Dispatch (3 calls)
1. `list_agents` → find agents with matching capabilities
2. `fetch_agent_card(agent_id)` → verify skills and input schema
3. `send_task(agent_id, task)` → dispatch with proper input format

### Monitor and Collect (2 calls)
1. `get_task(task_id)` → check status (queued/running/complete/failed)
2. If streaming: `send_task_streaming` → get partial results as they arrive

## MUST DO
- Validate agent card before dispatching sensitive data
- Set explicit timeouts on all tasks
- Track every task to completion (don't fire-and-forget)
- Use streaming for long-running tasks (better UX)

## MUST NOT DO
- Don't send sensitive data to unvalidated agents
- Don't leave tasks running indefinitely without timeout
- Don't dispatch without checking agent is available
