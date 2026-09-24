from enum import StrEnum


class TraceBackendTypeType0(StrEnum):
    LANGFUSE = "langfuse"
    LOGFIRE = "logfire"

    def __str__(self) -> str:
        return str(self.value)
