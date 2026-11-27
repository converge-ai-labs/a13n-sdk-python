from enum import StrEnum


class McpConfigAuthority(StrEnum):
    NONE = "none"
    OPERATOR = "operator"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
