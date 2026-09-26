from enum import StrEnum


class ThreadViewOrigin(StrEnum):
    CHILD = "child"
    FORK = "fork"
    NEW = "new"

    def __str__(self) -> str:
        return str(self.value)
