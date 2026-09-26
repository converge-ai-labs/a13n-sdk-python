from enum import StrEnum


class OperationKind(StrEnum):
    COMPLETE = "complete"
    REFRESH = "refresh"
    REVOKE = "revoke"
    SETUP = "setup"

    def __str__(self) -> str:
        return str(self.value)
