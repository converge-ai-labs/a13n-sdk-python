from enum import StrEnum


class ItemKind(StrEnum):
    OBSERVATION = "observation"
    REASONING_MESSAGE = "reasoning_message"
    TEXT_MESSAGE = "text_message"
    TOOL_CALL = "tool_call"

    def __str__(self) -> str:
        return str(self.value)
