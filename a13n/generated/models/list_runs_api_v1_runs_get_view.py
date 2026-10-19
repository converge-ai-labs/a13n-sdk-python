from enum import StrEnum


class ListRunsApiV1RunsGetView(StrEnum):
    COMPACT = "compact"
    DETAILED = "detailed"

    def __str__(self) -> str:
        return str(self.value)
