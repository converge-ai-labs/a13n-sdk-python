from enum import StrEnum


class SecurityAdvisorySeverity(StrEnum):
    CRITICAL = "critical"
    HIGH = "high"

    def __str__(self) -> str:
        return str(self.value)
