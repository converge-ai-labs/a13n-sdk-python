from enum import StrEnum


class EventConnectionStatusState(StrEnum):
    CONNECTED = "connected"
    CONNECTING = "connecting"
    DISABLED = "disabled"
    DISCONNECTED = "disconnected"
    HTTP = "http"
    RECONNECTING = "reconnecting"

    def __str__(self) -> str:
        return str(self.value)
