from enum import StrEnum


class StartupErrorPolicy(StrEnum):
    RAISE = "raise"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
