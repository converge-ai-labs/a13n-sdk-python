from enum import IntEnum


class DashboardConfigRefreshSeconds(IntEnum):
    VALUE_0 = 0
    VALUE_10 = 10
    VALUE_30 = 30
    VALUE_60 = 60
    VALUE_300 = 300

    def __str__(self) -> str:
        return str(self.value)
