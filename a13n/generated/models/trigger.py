from enum import StrEnum


class Trigger(StrEnum):
    BROWSER_HANDBACK = "browser_handback"
    CHILD_RESULT = "child_result"
    INPUT = "input"
    QUEUED = "queued"
    RESUME = "resume"
    SPAWNED = "spawned"
    TOOL_RESULT = "tool_result"

    def __str__(self) -> str:
        return str(self.value)
