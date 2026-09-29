from enum import StrEnum


class WaitReason(StrEnum):
    APPROVAL = "approval"
    CALL = "call"
    MULTIPLE = "multiple"

    def __str__(self) -> str:
        return str(self.value)
