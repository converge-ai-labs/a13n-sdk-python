from enum import StrEnum


class ConnectorEventState(StrEnum):
    FAILED = "failed"
    IGNORED = "ignored"
    PENDING = "pending"
    STORED = "stored"
    SUBMITTED = "submitted"
    UNMATCHED = "unmatched"

    def __str__(self) -> str:
        return str(self.value)
