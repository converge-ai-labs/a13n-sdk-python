from enum import StrEnum


class ListInboxKindType0(StrEnum):
    CHILD_RESULT = "child_result"
    MESSAGE = "message"

    def __str__(self) -> str:
        return str(self.value)
