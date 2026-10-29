from enum import StrEnum


class ListThreadRunsSortType0(StrEnum):
    CALLS = "calls"
    COST = "cost"
    DURATION = "duration"

    def __str__(self) -> str:
        return str(self.value)
