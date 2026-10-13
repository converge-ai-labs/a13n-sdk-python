from enum import StrEnum


class RunContentMediaType(StrEnum):
    APPLICATIONJSON = "application/json"
    TEXTPLAIN = "text/plain"

    def __str__(self) -> str:
        return str(self.value)
