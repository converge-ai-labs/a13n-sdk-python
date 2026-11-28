from enum import StrEnum


class TransitionConnectorTriggerCommand(StrEnum):
    ENABLE = "enable"
    PAUSE = "pause"
    RECONCILE = "reconcile"
    RETIRE = "retire"

    def __str__(self) -> str:
        return str(self.value)
