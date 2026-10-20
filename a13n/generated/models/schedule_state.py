from enum import StrEnum


class ScheduleState(StrEnum):
    ARCHIVED = "archived"
    ENABLED = "enabled"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
