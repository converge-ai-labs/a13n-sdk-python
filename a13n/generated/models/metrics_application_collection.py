from enum import StrEnum


class MetricsApplicationCollection(StrEnum):
    NATIVE = "native"
    PROXY = "proxy"
    PULL = "pull"

    def __str__(self) -> str:
        return str(self.value)
