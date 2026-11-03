from enum import StrEnum


class ScheduleTargetMode(StrEnum):
    NEW_THREAD = "new_thread"
    THREAD = "thread"

    def __str__(self) -> str:
        return str(self.value)
