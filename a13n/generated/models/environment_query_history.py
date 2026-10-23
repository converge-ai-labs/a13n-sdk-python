from enum import StrEnum


class EnvironmentQueryHistory(StrEnum):
    CONFIGURED = "configured"
    TEMPORARY = "temporary"

    def __str__(self) -> str:
        return str(self.value)
