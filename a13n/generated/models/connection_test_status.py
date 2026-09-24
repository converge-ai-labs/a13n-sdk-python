from enum import StrEnum


class ConnectionTestStatus(StrEnum):
    FAILED = "failed"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
