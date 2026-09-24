from enum import StrEnum


class ModelCatalogStatus(StrEnum):
    READY = "ready"
    STALE = "stale"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
