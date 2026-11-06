from enum import StrEnum


class EnvironmentViewDesktopPreview(StrEnum):
    CONNECTION_UNSUPPORTED = "connection_unsupported"
    NOT_CONFIGURED = "not_configured"
    SUPPORTED = "supported"

    def __str__(self) -> str:
        return str(self.value)
