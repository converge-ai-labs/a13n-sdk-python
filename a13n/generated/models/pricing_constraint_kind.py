from enum import StrEnum


class PricingConstraintKind(StrEnum):
    ALWAYS = "always"
    DAILY_TIME = "daily_time"
    START_DATE = "start_date"

    def __str__(self) -> str:
        return str(self.value)
