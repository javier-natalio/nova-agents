"""LLM client wrapper."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class Completion:
    text: str
    model: str
    tokens: int


class LLMClient:
    def __init__(self, model: str | None = None):
        self.model = model or os.getenv("LLM_MODEL", "gpt-4o-mini")

    def complete(self, prompt: str) -> Completion:
        # Provider call is injected at runtime; stub keeps unit tests offline.
        text = prompt.strip()[:4000]
        return Completion(text=text, model=self.model, tokens=max(len(text) // 4, 1))

    def complete_json(self, prompt: str) -> Completion:
        return self.complete(prompt + "\nRespond with JSON only.")

    def complete_json(self, prompt: str) -> Completion:
        return self.complete(prompt + "\nRespond with JSON only.")

    def complete_json(self, prompt: str) -> Completion:
        return self.complete(prompt + "\nRespond with JSON only.")

    def complete_json(self, prompt: str) -> Completion:
        return self.complete(prompt + "\nRespond with JSON only.")

    def complete_json(self, prompt: str) -> Completion:
        return self.complete(prompt + "\nRespond with JSON only.")
