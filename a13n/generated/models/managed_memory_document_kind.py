from enum import StrEnum


class ManagedMemoryDocumentKind(StrEnum):
    EPISODIC = "episodic"
    PROCEDURAL = "procedural"
    SEMANTIC = "semantic"

    def __str__(self) -> str:
        return str(self.value)
