from enum import StrEnum


class MountApplicationStatus(StrEnum):
    FAILED = "failed"
    PENDING = "pending"
    PREPARING = "preparing"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
