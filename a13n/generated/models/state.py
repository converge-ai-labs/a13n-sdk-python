from enum import StrEnum


class State(StrEnum):
    CHANGED = "changed"
    DISABLED = "disabled"
    DISCOVERY_FAILED = "discovery_failed"
    NOT_READY = "not_ready"
    RELOAD_REQUESTED = "reload_requested"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
