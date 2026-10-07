from enum import StrEnum


class PendingAnswersStatus(StrEnum):
    CLOSED = "closed"
    RESUMED = "resumed"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
