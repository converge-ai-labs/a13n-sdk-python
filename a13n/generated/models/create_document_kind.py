from enum import StrEnum


class CreateDocumentKind(StrEnum):
    EPISODIC = "episodic"
    PROCEDURAL = "procedural"
    SEMANTIC = "semantic"

    def __str__(self) -> str:
        return str(self.value)
