from enum import StrEnum


class OccurrenceStatus(StrEnum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    PENDING = "pending"
    SKIPPED = "skipped"
    SUBMITTED = "submitted"

    def __str__(self) -> str:
        return str(self.value)
