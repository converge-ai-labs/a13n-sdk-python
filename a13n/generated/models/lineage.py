from enum import StrEnum


class Lineage(StrEnum):
    CONTINUE = "continue"
    FORK = "fork"
    ROOT = "root"

    def __str__(self) -> str:
        return str(self.value)
