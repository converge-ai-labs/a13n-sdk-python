from enum import StrEnum


class ListInboxApiV1ThreadsThreadIdInboxGetKindType0(StrEnum):
    CHILD_RESULT = "child_result"
    MESSAGE = "message"

    def __str__(self) -> str:
        return str(self.value)
