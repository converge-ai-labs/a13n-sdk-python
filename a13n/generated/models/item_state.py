from enum import StrEnum


class ItemState(StrEnum):
    COMPLETED = "completed"
    FAILED = "failed"
    INTERRUPTED = "interrupted"
    IN_PROGRESS = "in_progress"

    def __str__(self) -> str:
        return str(self.value)
