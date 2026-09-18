from enum import StrEnum


class ClientConnectionStatusStatus(StrEnum):
    CONNECTING = "connecting"
    OFFLINE = "offline"
    ONLINE = "online"

    def __str__(self) -> str:
        return str(self.value)
