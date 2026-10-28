from enum import StrEnum


class MemberUsageStatus(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
