from enum import StrEnum


class RunSummaryRevisionSelection(StrEnum):
    DEFAULT = "default"
    INHERITED = "inherited"
    PINNED = "pinned"
    SNAPSHOT = "snapshot"

    def __str__(self) -> str:
        return str(self.value)
