from enum import StrEnum


class MemorySourceKind(StrEnum):
    FILE = "file"
    RECORD = "record"

    def __str__(self) -> str:
        return str(self.value)
