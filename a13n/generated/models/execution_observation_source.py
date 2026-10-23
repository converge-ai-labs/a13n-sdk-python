from enum import StrEnum


class ExecutionObservationSource(StrEnum):
    LIVE = "live"
    RETAINED = "retained"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
