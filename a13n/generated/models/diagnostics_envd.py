from enum import StrEnum


class DiagnosticsEnvd(StrEnum):
    NOT_VERIFIED = "not_verified"
    PREVIOUSLY_READY = "previously_ready"

    def __str__(self) -> str:
        return str(self.value)
