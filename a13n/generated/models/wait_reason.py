from enum import StrEnum


class WaitReason(StrEnum):
    APPROVAL = "approval"
    CALL = "call"
    DESKTOP_CONTROL = "desktop_control"
    MULTIPLE = "multiple"

    def __str__(self) -> str:
        return str(self.value)
