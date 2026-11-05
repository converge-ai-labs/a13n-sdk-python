from enum import StrEnum


class ClientConnectionObservationState(StrEnum):
    CONNECTING = "connecting"
    OFFLINE = "offline"
    ONLINE = "online"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
