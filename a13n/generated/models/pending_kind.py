from enum import StrEnum


class PendingKind(StrEnum):
    APPROVAL = "approval"
    CLIENT_TOOL = "client_tool"
    USER_INPUT = "user_input"

    def __str__(self) -> str:
        return str(self.value)
