from enum import StrEnum


class ScheduleState(StrEnum):
    ARCHIVED = "archived"
    COMPLETED = "completed"
    ENABLED = "enabled"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
