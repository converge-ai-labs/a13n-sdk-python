from enum import StrEnum


class EntryStatus(StrEnum):
    ASSIGNED = "assigned"
    CONSUMED = "consumed"
    FAILED = "failed"
    PENDING = "pending"
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
