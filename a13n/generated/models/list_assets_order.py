from enum import StrEnum


class ListAssetsOrder(StrEnum):
    ID = "id"
    NEWEST = "newest"

    def __str__(self) -> str:
        return str(self.value)
