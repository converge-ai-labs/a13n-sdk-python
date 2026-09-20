from enum import StrEnum


class DocumentEntryLegacyKindType0(StrEnum):
    DAILY = "daily"
    LONG_TERM = "long_term"

    def __str__(self) -> str:
        return str(self.value)
