from enum import StrEnum


class PresetKind(StrEnum):
    COMPOSER = "composer"
    FINDING = "finding"
    MEMORY_ORGANIZER = "memory_organizer"

    def __str__(self) -> str:
        return str(self.value)
