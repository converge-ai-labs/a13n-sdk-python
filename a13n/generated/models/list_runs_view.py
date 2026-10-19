from enum import StrEnum


class ListRunsView(StrEnum):
    COMPACT = "compact"
    DETAILED = "detailed"

    def __str__(self) -> str:
        return str(self.value)
