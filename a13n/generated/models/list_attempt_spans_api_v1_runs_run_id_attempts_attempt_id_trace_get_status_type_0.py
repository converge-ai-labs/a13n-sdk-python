from enum import StrEnum


class ListAttemptSpansApiV1RunsRunIdAttemptsAttemptIdTraceGetStatusType0(StrEnum):
    ERROR = "error"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
