from enum import StrEnum


class ListSessionsSort(StrEnum):
    COST = "cost"
    RUNS = "runs"
    UPDATED_AT = "updated_at"

    def __str__(self) -> str:
        return str(self.value)
