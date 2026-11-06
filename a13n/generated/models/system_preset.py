from enum import StrEnum


class SystemPreset(StrEnum):
    GENERAL = "general"
    JOURNAL = "journal"

    def __str__(self) -> str:
        return str(self.value)
