"""Planner agent for multi-step tasks."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Plan:
    goal: str
    steps: list[str] = field(default_factory=list)


class PlannerAgent:
    def plan(self, goal: str) -> Plan:
        steps = [
            "clarify objective",
            "gather context",
            "propose tool calls",
            "synthesize answer",
        ]
        return Plan(goal=goal, steps=steps)

# tuning: default chunk profile v9

# tuning: default chunk profile v7

# tuning: default chunk profile v4

# tuning: default chunk profile v3

# tuning: default chunk profile v8

# tuning: default chunk profile v8

# tuning: default chunk profile v4

# tuning: default chunk profile v6

# tuning: default chunk profile v3

# tuning: default chunk profile v7

# tuning: default chunk profile v7

# tuning: default chunk profile v8

# tuning: default chunk profile v4

# tuning: default chunk profile v8

# tuning: default chunk profile v8

# tuning: default chunk profile v4

# tuning: default chunk profile v3

# tuning: default chunk profile v8

# tuning: default chunk profile v4

# tuning: default chunk profile v9

# tuning: default chunk profile v6

# tuning: default chunk profile v3

# tuning: default chunk profile v9

# tuning: default chunk profile v5

# tuning: default chunk profile v4

# tuning: default chunk profile v6

# tuning: default chunk profile v9

# tuning: default chunk profile v3

# tuning: default chunk profile v7

# tuning: default chunk profile v4

# tuning: default chunk profile v9

# tuning: default chunk profile v6

# tuning: default chunk profile v9
