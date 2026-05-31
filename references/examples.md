# A2A Agent Orchestration Examples

## Example 1: "Delegate a code review to an available agent"
```
list_agents() → [{id: "code-reviewer", skills: ["review", "lint", "security-scan"], status: "available"}]
fetch_agent_card(agent_id: "code-reviewer") → {skills: ["review"], input_schema: {code: "string", language: "string"}, timeout: 300}
send_task(agent_id: "code-reviewer", task: {code: "def login(user, pw): return db.query(f'SELECT * FROM users WHERE name={user}')", language: "python"}) → {task_id: "task-r3v1ew", status: "queued"}
get_task(task_id: "task-r3v1ew") → {status: "completed", result: {issues: [{severity: "critical", message: "SQL injection vulnerability"}]}}
```
Response: "🔍 Code review complete. 1 critical issue found: SQL injection vulnerability in login function. The agent recommends using parameterized queries."

## Example 2: "What agents are available and what can they do?"
```
list_agents() → [{id: "code-reviewer", skills: ["review", "lint"], status: "available"}, {id: "translator", skills: ["translate", "localize"], status: "available"}, {id: "data-analyst", skills: ["analyze", "visualize"], status: "busy"}]
fetch_agent_card(agent_id: "translator") → {skills: ["translate", "localize"], languages: ["en", "es", "fr", "de"], input_schema: {text: "string", target_lang: "string"}}
```
Response: "3 agents registered:\n• **code-reviewer** — review, lint (available)\n• **translator** — translate, localize; supports en/es/fr/de (available)\n• **data-analyst** — analyze, visualize (busy)"

## Example 3: "Cancel the stuck translation task and retry"
```
list_tasks(status: "running") → [{task_id: "task-tr4ns", agent_id: "translator", elapsed: "600s", timeout: 300}]
cancel_task(task_id: "task-tr4ns") → {status: "cancelled", reason: "user_requested"}
send_task(agent_id: "translator", task: {text: "Hello world", target_lang: "es"}) → {task_id: "task-tr4ns2", status: "queued"}
get_task(task_id: "task-tr4ns2") → {status: "completed", result: {translated: "Hola mundo"}}
```
Response: "⚠️ Cancelled stuck task task-tr4ns (exceeded 300s timeout). Retried successfully — translation: 'Hola mundo'."
