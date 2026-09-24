from enum import StrEnum


class ConnectionStatus(StrEnum):
    PENDING = "pending"
    READY = "ready"
    REAUTHORIZATION_REQUIRED = "reauthorization_required"

    def __str__(self) -> str:
        return str(self.value)
