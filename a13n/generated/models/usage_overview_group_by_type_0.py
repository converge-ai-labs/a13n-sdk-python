from enum import StrEnum


class UsageOverviewGroupByType0(StrEnum):
    AGENTS = "agents"
    MODELS = "models"

    def __str__(self) -> str:
        return str(self.value)
