from enum import StrEnum


class McpInputResponseAction(StrEnum):
    ACCEPT = "accept"
    CANCEL = "cancel"
    DECLINE = "decline"

    def __str__(self) -> str:
        return str(self.value)
