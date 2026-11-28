from enum import StrEnum


class Trigger(StrEnum):
    BROWSER_HANDBACK = "browser_handback"
    CHILD_MESSAGE = "child_message"
    CHILD_RESULT = "child_result"
    DESKTOP_HANDBACK = "desktop_handback"
    INPUT = "input"
    QUEUED = "queued"
    REALTIME = "realtime"
    RESUME = "resume"
    SPAWNED = "spawned"
    TOOL_RESULT = "tool_result"

    def __str__(self) -> str:
        return str(self.value)
