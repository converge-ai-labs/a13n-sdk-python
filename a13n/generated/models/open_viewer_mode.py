from enum import StrEnum


class OpenViewerMode(StrEnum):
    CONTROL = "control"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
