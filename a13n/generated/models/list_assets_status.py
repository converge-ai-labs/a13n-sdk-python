from enum import StrEnum


class ListAssetsStatus(StrEnum):
    ACTIVE = "active"
    ALL = "all"
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)
