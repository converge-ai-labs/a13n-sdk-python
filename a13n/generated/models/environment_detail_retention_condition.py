from enum import StrEnum


class EnvironmentDetailRetentionCondition(StrEnum):
    ACTIVE = "active"
    IDLE = "idle"

    def __str__(self) -> str:
        return str(self.value)
