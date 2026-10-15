from enum import StrEnum


class ComputerCheckStatus(StrEnum):
    CHECKED = "checked"
    NOT_READY = "not_ready"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
