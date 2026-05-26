# A2A Cross-MCP Workflows

## A2A + Workflow: Multi-Agent Pipeline
```
A2A: list_agents() → find research-agent and writing-agent
A2A: send_task(agent: "research-agent", task: "Research competitor pricing")
A2A: get_task(task_id) → {status: "complete", output: research_data}
A2A: send_task(agent: "writing-agent", task: "Write report from research", input: research_data)
WORKFLOW: advance_step(instance_id, step: "research_complete")
```

## A2A + Slack: Task Completion Notification
```
A2A: get_task(task_id) → {status: "complete"}
SLACK: send_message(channel: "#agents", text: "✅ Research agent completed task. Output ready for review.")
```
