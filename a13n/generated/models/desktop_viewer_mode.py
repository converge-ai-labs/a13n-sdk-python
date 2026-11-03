from enum import StrEnum


class DesktopViewerMode(StrEnum):
    CONTROL = "control"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
