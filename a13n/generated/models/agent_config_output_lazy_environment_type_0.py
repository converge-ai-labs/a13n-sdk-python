from enum import StrEnum


class AgentConfigOutputLazyEnvironmentType0(StrEnum):
    EAGER = "eager"
    ON_DEMAND = "on_demand"
    WARMUP = "warmup"

    def __str__(self) -> str:
        return str(self.value)
