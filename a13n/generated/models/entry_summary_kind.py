from enum import StrEnum


class EntrySummaryKind(StrEnum):
    CHILD_RESULT = "child_result"
    MESSAGE = "message"

    def __str__(self) -> str:
        return str(self.value)
