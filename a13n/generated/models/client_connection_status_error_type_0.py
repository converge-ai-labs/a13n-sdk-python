from enum import StrEnum


class ClientConnectionStatusErrorType0(StrEnum):
    CONTROL_DRAINING = "control_draining"
    ENVIRONMENT_INITIALIZATION_FAILED = "environment_initialization_failed"
    ENVIRONMENT_UNAVAILABLE = "environment_unavailable"

    def __str__(self) -> str:
        return str(self.value)
