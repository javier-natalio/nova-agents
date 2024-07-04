"""Vector retrieval interface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Hit:
    id: str
    text: str
    score: float


class Retriever:
    def __init__(self):
        self._docs: list[tuple[str, str, list[float]]] = []

    def add(self, doc_id: str, text: str, embedding: list[float]) -> None:
        self._docs.append((doc_id, text, embedding))

    def search(self, query_embedding: list[float], k: int = 5) -> list[Hit]:
        scored: list[Hit] = []
        for doc_id, text, emb in self._docs:
            score = sum(a * b for a, b in zip(query_embedding, emb))
            scored.append(Hit(doc_id, text, score))
        scored.sort(key=lambda h: h.score, reverse=True)
        return scored[:k]

    def count(self) -> int:
        return len(self._docs)
