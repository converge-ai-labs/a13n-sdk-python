from enum import StrEnum


class McpAuth(StrEnum):
    BEARER = "bearer"
    HEADERS = "headers"
    NONE = "none"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
