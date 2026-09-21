from enum import StrEnum


class ConnectionCleanupReceiptLocalStatus(StrEnum):
    ACTION_REQUIRED = "action_required"
    DELETED = "deleted"
    DISABLED = "disabled"
    PENDING = "pending"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
