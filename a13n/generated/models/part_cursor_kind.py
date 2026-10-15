from enum import StrEnum


class PartCursorKind(StrEnum):
    REASONING = "reasoning"
    TEXT = "text"
    TOOL_CALL = "tool_call"

    def __str__(self) -> str:
        return str(self.value)
