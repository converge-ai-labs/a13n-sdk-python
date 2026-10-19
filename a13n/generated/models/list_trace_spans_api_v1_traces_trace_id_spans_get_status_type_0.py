from enum import StrEnum


class ListTraceSpansApiV1TracesTraceIdSpansGetStatusType0(StrEnum):
    ERROR = "error"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
