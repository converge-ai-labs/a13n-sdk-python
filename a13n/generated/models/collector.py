from enum import StrEnum


class Collector(StrEnum):
    ALLOY = "alloy"
    VMAGENT = "vmagent"

    def __str__(self) -> str:
        return str(self.value)
