from enum import StrEnum


class ScheduleCreateState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
