from enum import StrEnum


class ListTraceSpansView(StrEnum):
    COMPACT = "compact"
    DETAILED = "detailed"
    OVERVIEW = "overview"

    def __str__(self) -> str:
        return str(self.value)
