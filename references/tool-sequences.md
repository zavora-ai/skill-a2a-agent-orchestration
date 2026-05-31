# A2A Agent Orchestration Tool Sequences (10 tools)

## Discovery (3)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_agents` | List available agents and capabilities | read |
| `fetch_agent_card` | Get agent card with skills/input schema | read |
| `validate_agent_card` | Verify agent card integrity | read |

## Task Dispatch (3)
| Tool | Purpose | Risk |
|------|---------|------|
| `send_task` | Dispatch task to remote agent | write |
| `send_task_streaming` | Dispatch with streaming results | write |
| `cancel_task` | Cancel a running task | write |

## Monitoring (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `get_task` | Check task status/result | read |
| `list_tasks` | List all dispatched tasks | read |

## Notifications (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `subscribe_events` | Subscribe to task events | write |
| `manage_push_notifications` | Configure push notification endpoints | write |

## Sequence: Discover and Dispatch (4 calls)
```
1. list_agents() → [{id: "code-reviewer", skills: ["review", "lint"]}, {id: "translator", skills: ["translate"]}]
2. fetch_agent_card(agent_id: "code-reviewer") → {skills: ["review", "lint"], input_schema: {type: "object", properties: {code: "string", language: "string"}}}
3. validate_agent_card(agent_id: "code-reviewer") → {valid: true, last_seen: "2min ago"}
4. send_task(agent_id: "code-reviewer", task: {code: "fn main() {}", language: "rust"}) → {task_id: "task-abc123", status: "queued"}
```

## Sequence: Stream Long-Running Task (3 calls)
```
1. fetch_agent_card(agent_id: "data-analyst") → {skills: ["analyze", "summarize"], streaming: true}
2. send_task_streaming(agent_id: "data-analyst", task: {dataset: "sales-q4", query: "top trends"}) → {task_id: "task-def456", status: "running", partial_results: [...]}
3. get_task(task_id: "task-def456") → {status: "completed", result: {trends: [...]}}
```

## Sequence: Cancel and Reassign (3 calls)
```
1. get_task(task_id: "task-abc123") → {status: "running", agent_id: "code-reviewer", elapsed: "15min"}
2. cancel_task(task_id: "task-abc123") → {status: "cancelled"}
3. send_task(agent_id: "code-reviewer-v2", task: {code: "fn main() {}", language: "rust"}) → {task_id: "task-ghi789", status: "queued"}
```
