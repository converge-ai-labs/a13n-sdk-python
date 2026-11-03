from enum import StrEnum


class DiscoverySourceKind(StrEnum):
    CAPABILITIES = "capabilities"
    CONNECTIONS = "connections"
    PLATFORM = "platform"

    def __str__(self) -> str:
        return str(self.value)
