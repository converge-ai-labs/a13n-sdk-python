from enum import StrEnum


class CollectorStatusStateType1(StrEnum):
    CAPACITY = "capacity"
    FAILED = "failed"
    NOT_CONFIGURED = "not_configured"
    NOT_SELECTED = "not_selected"
    PENDING = "pending"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
