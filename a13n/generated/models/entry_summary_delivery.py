from enum import StrEnum


class EntrySummaryDelivery(StrEnum):
    NEXT_RUN = "next_run"
    STEER = "steer"

    def __str__(self) -> str:
        return str(self.value)
