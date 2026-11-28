from enum import StrEnum


class ConnectorTriggerState(StrEnum):
    ENABLED = "enabled"
    PAUSED = "paused"
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)
