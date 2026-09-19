from enum import StrEnum


class DeviceInfoPathStyle(StrEnum):
    POSIX = "posix"
    WINDOWS = "windows"

    def __str__(self) -> str:
        return str(self.value)
