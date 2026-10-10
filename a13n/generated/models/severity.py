from enum import StrEnum


class Severity(StrEnum):
    CRITICAL = "critical"
    SUGGESTION = "suggestion"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
