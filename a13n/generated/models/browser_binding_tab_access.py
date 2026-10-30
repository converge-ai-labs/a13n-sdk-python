from enum import StrEnum


class BrowserBindingTabAccess(StrEnum):
    GLOBAL = "global"
    THREAD = "thread"

    def __str__(self) -> str:
        return str(self.value)
