from enum import StrEnum


class CreationProgressStage(StrEnum):
    BUILDING = "building"
    FAILED = "failed"
    INACTIVE = "inactive"
    PREPARING = "preparing"
    READY = "ready"
    STARTING = "starting"

    def __str__(self) -> str:
        return str(self.value)
