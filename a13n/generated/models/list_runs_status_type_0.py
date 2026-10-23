from enum import StrEnum


class ListRunsStatusType0(StrEnum):
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"
    RUNNING = "running"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
