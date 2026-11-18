from enum import StrEnum


class CreationProgressProfile(StrEnum):
    DESKTOP = "desktop"
    HEADLESS = "headless"

    def __str__(self) -> str:
        return str(self.value)
