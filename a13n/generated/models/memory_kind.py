from enum import StrEnum


class MemoryKind(StrEnum):
    FILE = "file"
    RECORD = "record"

    def __str__(self) -> str:
        return str(self.value)
