from enum import StrEnum


class OccurrenceSummaryExecutionOutcomeType0(StrEnum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
