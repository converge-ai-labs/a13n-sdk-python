from enum import StrEnum


class MemorySourceStatus(StrEnum):
    CHANGES = "changes"
    FAILED = "failed"
    FULL = "full"
    OMITTED = "omitted"
    RECALLED = "recalled"
    TIMEOUT = "timeout"
    UNAVAILABLE = "unavailable"
    UNCHANGED = "unchanged"

    def __str__(self) -> str:
        return str(self.value)
