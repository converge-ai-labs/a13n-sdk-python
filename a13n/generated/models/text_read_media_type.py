from enum import StrEnum


class TextReadMediaType(StrEnum):
    APPLICATIONJSON = "application/json"
    TEXTPLAIN = "text/plain"

    def __str__(self) -> str:
        return str(self.value)
