from enum import StrEnum


class ServiceAccountUpdateStatusType0(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
