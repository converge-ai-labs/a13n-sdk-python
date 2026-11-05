from enum import StrEnum


class RunViewRevisionSelection(StrEnum):
    DEFAULT = "default"
    INHERITED = "inherited"
    PINNED = "pinned"
    SNAPSHOT = "snapshot"

    def __str__(self) -> str:
        return str(self.value)
