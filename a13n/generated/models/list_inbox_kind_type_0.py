from enum import StrEnum


class ListInboxKindType0(StrEnum):
    CHILD_MESSAGE = "child_message"
    CHILD_RESULT = "child_result"
    MESSAGE = "message"

    def __str__(self) -> str:
        return str(self.value)
