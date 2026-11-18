from enum import StrEnum


class ApplicationStatus(StrEnum):
    APPLIED = "applied"
    ON_CREATE = "on_create"
    ON_NEXT_USE = "on_next_use"
    PENDING = "pending"
    RETRY = "retry"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
