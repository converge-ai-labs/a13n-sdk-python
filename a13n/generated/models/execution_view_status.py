from enum import StrEnum


class ExecutionViewStatus(StrEnum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    LOST = "lost"
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
