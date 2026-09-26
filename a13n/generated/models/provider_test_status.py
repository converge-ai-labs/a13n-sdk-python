from enum import StrEnum


class ProviderTestStatus(StrEnum):
    FAILED = "failed"
    SUCCEEDED = "succeeded"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
