from enum import StrEnum


class RunAgentSource(StrEnum):
    REVISION = "revision"
    THREAD_SNAPSHOT = "thread_snapshot"

    def __str__(self) -> str:
        return str(self.value)
