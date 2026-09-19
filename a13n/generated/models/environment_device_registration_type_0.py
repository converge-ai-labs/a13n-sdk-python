from enum import StrEnum


class EnvironmentDeviceRegistrationType0(StrEnum):
    PAIRED = "paired"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
