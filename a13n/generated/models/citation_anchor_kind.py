from enum import StrEnum


class CitationAnchorKind(StrEnum):
    CONTENT = "content"
    MARKER = "marker"

    def __str__(self) -> str:
        return str(self.value)
