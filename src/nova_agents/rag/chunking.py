"""Document chunking for RAG."""
from __future__ import annotations


def chunk_text(text: str, size: int = 800, overlap: int = 120) -> list[str]:
    text = " ".join(text.split())
    if size <= 0:
        raise ValueError("size must be positive")
    chunks: list[str] = []
    i = 0
    while i < len(text):
        chunks.append(text[i : i + size])
        i += max(size - overlap, 1)
    return chunks
