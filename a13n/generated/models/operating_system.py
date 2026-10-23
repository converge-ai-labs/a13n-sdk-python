from enum import StrEnum


class OperatingSystem(StrEnum):
    LINUX = "linux"
    MACOS = "macos"
    WINDOWS = "windows"

    def __str__(self) -> str:
        return str(self.value)
