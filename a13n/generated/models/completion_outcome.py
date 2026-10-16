from enum import StrEnum


class CompletionOutcome(StrEnum):
    ABANDONED = "abandoned"
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
