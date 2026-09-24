from enum import StrEnum


class AttemptViewStatus(StrEnum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    LEASED = "leased"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    YIELDED = "yielded"

    def __str__(self) -> str:
        return str(self.value)
