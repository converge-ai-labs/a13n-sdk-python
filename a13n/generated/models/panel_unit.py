from enum import StrEnum


class PanelUnit(StrEnum):
    AUTO = "auto"
    BYTES = "bytes"
    BYTES_PER_SECOND = "bytes_per_second"
    COUNT = "count"
    OPERATIONS_PER_SECOND = "operations_per_second"
    RATIO = "ratio"
    SECONDS = "seconds"

    def __str__(self) -> str:
        return str(self.value)
