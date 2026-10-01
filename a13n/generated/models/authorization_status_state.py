from enum import StrEnum


class AuthorizationStatusState(StrEnum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    REAUTHENTICATION_REQUIRED = "reauthentication_required"
    REFRESHING = "refreshing"

    def __str__(self) -> str:
        return str(self.value)
