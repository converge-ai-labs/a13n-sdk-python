from enum import StrEnum


class ThreadNavigationOrigin(StrEnum):
    CHILD = "child"
    FORK = "fork"
    NEW = "new"

    def __str__(self) -> str:
        return str(self.value)
