from enum import StrEnum


class RunSummaryRevisionSelection(StrEnum):
    DEFAULT = "default"
    INHERITED = "inherited"
    PINNED = "pinned"

    def __str__(self) -> str:
        return str(self.value)
