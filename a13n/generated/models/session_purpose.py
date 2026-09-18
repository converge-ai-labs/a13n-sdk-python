from enum import StrEnum


class SessionPurpose(StrEnum):
    DEBUG = "debug"
    EXECUTION = "execution"

    def __str__(self) -> str:
        return str(self.value)
