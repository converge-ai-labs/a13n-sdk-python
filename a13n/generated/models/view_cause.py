from enum import StrEnum


class ViewCause(StrEnum):
    AGENT = "agent"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
