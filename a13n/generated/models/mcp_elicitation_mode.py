from enum import StrEnum


class McpElicitationMode(StrEnum):
    FORM = "form"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
