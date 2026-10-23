from enum import StrEnum


class SchedulePauseReasonType0(StrEnum):
    AUTHORITY_INVALID = "authority_invalid"
    MANUAL = "manual"
    TARGET_INVALID = "target_invalid"

    def __str__(self) -> str:
        return str(self.value)
