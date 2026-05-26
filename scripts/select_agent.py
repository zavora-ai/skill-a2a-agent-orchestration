#!/usr/bin/env python3
"""Select best agent for a task based on capabilities and availability."""
import json, sys

def select(data):
    task_requirements = set(data.get("requirements", []))
    agents = data.get("agents", [])
    matches = []
    for agent in agents:
        caps = set(agent.get("capabilities", []))
        overlap = task_requirements & caps
        if overlap:
            matches.append({**agent, "match_score": len(overlap) / len(task_requirements), "matched": list(overlap)})
    return sorted(matches, key=lambda x: x["match_score"], reverse=True)[:3]

if __name__ == "__main__":
    print(json.dumps(select(json.loads(sys.argv[1])), indent=2))
