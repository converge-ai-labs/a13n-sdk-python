from enum import StrEnum


class ProviderConnectivityStatus(StrEnum):
    CONNECTED = "connected"
    UNAVAILABLE = "unavailable"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
