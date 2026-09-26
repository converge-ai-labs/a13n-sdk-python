from enum import StrEnum


class AttemptViewStartReason(StrEnum):
    HANDOFF = "handoff"
    INITIAL = "initial"
    RECOVERY = "recovery"

    def __str__(self) -> str:
        return str(self.value)
