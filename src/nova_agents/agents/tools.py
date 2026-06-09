"""Tool registry for agents."""
from __future__ import annotations

from typing import Any, Callable

ToolFn = Callable[..., Any]


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, ToolFn] = {}

    def register(self, name: str, fn: ToolFn) -> None:
        self._tools[name] = fn

    def call(self, name: str, **kwargs: Any) -> Any:
        if name not in self._tools:
            raise KeyError(name)
        return self._tools[name](**kwargs)

    def names(self) -> list[str]:
        return sorted(self._tools)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)
