from enum import StrEnum


class ModelCatalogPageStatus(StrEnum):
    READY = "ready"
    STALE = "stale"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
