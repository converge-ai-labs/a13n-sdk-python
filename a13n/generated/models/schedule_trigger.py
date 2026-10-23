from enum import StrEnum


class ScheduleTrigger(StrEnum):
    MANUAL = "manual"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
