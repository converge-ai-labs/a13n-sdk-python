from enum import StrEnum


class SubagentsInputMode(StrEnum):
    ASYNC = "async"
    INLINE = "inline"

    def __str__(self) -> str:
        return str(self.value)
