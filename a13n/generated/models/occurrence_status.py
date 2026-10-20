from enum import StrEnum


class OccurrenceStatus(StrEnum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    SKIPPED = "skipped"
    SUBMITTED = "submitted"

    def __str__(self) -> str:
        return str(self.value)
