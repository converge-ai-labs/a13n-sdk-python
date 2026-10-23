from enum import StrEnum


class PanelVisualization(StrEnum):
    STAT = "stat"
    TIMESERIES = "timeseries"

    def __str__(self) -> str:
        return str(self.value)
