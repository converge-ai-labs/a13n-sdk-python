from enum import StrEnum


class ContentRefMediaType(StrEnum):
    APPLICATIONJSON = "application/json"
    TEXTPLAIN = "text/plain"

    def __str__(self) -> str:
        return str(self.value)
