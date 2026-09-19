from enum import StrEnum


class MemoryEntrySelectionMode(StrEnum):
    DOCUMENTS = "documents"
    RECORDS = "records"

    def __str__(self) -> str:
        return str(self.value)
