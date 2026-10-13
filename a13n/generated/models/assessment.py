from enum import StrEnum


class Assessment(StrEnum):
    CONFIRMED = "confirmed"
    EXPECTED = "expected"
    FALSE_POSITIVE = "false_positive"
    INSUFFICIENT = "insufficient"
    UNREVIEWED = "unreviewed"

    def __str__(self) -> str:
        return str(self.value)
