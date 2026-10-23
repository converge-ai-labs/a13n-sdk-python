from enum import StrEnum


class AuthorizationStatusState(StrEnum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    REAUTHENTICATION_REQUIRED = "reauthentication_required"

    def __str__(self) -> str:
        return str(self.value)
