from enum import StrEnum


class WaitReason(StrEnum):
    APPROVAL = "approval"
    CLIENT_TOOL = "client_tool"
    MULTIPLE = "multiple"
    USER_INPUT = "user_input"

    def __str__(self) -> str:
        return str(self.value)
