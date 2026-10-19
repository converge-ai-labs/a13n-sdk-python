from enum import StrEnum


class ListTracesApiV1TracesGetStatusType0(StrEnum):
    ERROR = "error"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
