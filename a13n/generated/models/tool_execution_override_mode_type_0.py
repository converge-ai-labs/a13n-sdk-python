from enum import StrEnum


class ToolExecutionOverrideModeType0(StrEnum):
    AUTO = "auto"
    INLINE = "inline"

    def __str__(self) -> str:
        return str(self.value)
