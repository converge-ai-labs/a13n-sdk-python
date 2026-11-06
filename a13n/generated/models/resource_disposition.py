from enum import StrEnum


class ResourceDisposition(StrEnum):
    BORROWED = "borrowed"
    DELETE = "delete"
    RETAIN = "retain"

    def __str__(self) -> str:
        return str(self.value)
