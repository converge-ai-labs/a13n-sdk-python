from enum import StrEnum


class ConnectionFailureReason(StrEnum):
    OUTCOME_UNKNOWN = "outcome_unknown"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
