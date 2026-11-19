from enum import StrEnum


class DeploymentStatus(StrEnum):
    DEPLOYING = "deploying"
    NEEDS_ATTENTION = "needs_attention"
    READY = "ready"
    RETIRED = "retired"
    RETIRING = "retiring"

    def __str__(self) -> str:
        return str(self.value)
