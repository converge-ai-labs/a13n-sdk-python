from enum import StrEnum


class Delivery(StrEnum):
    NEXT_RUN = "next_run"
    STEER = "steer"

    def __str__(self) -> str:
        return str(self.value)
