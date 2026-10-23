from enum import StrEnum


class SearchTracesOrderBy(StrEnum):
    COST = "cost"
    DURATION = "duration"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
