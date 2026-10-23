from enum import StrEnum


class ToolSearchGroupCapabilitiesItem(StrEnum):
    ENVIRONMENT = "environment"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
