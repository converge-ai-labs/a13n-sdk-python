from enum import StrEnum


class ConnectionAuth(StrEnum):
    ACCOUNT = "account"
    BEARER = "bearer"
    HEADERS = "headers"
    NONE = "none"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
