from enum import StrEnum


class StatusChangeStatus(StrEnum):
    DISABLED = "disabled"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
