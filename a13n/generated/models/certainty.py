from enum import StrEnum


class Certainty(StrEnum):
    KNOWN = "known"
    NOT_DISPATCHED = "not_dispatched"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
