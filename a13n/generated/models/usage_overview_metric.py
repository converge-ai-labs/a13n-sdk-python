from enum import StrEnum


class UsageOverviewMetric(StrEnum):
    COST = "cost"
    TOKENS = "tokens"

    def __str__(self) -> str:
        return str(self.value)
