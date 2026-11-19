from enum import StrEnum


class DeploymentCleanupAdditionalProperty(StrEnum):
    NOT_CREATED = "not_created"
    PENDING = "pending"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
