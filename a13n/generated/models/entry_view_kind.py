from enum import StrEnum


class EntryViewKind(StrEnum):
    BROWSER_HANDBACK = "browser_handback"
    CHILD_RESULT = "child_result"
    DESKTOP_HANDBACK = "desktop_handback"
    MESSAGE = "message"
    TOOL_RESULT = "tool_result"

    def __str__(self) -> str:
        return str(self.value)
