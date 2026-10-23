from enum import StrEnum


class Status(StrEnum):
    CAPACITY = "capacity"
    DISABLED = "disabled"
    NOT_READY = "not_ready"
    OFFLINE = "offline"
    READY = "ready"
    STALE = "stale"
    UNSUPPORTED = "unsupported"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
