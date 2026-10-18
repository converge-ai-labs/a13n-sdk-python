from enum import StrEnum


class AccessMode(StrEnum):
    CONTROL = "control"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
