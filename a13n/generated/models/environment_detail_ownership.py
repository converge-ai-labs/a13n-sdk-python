from enum import StrEnum


class EnvironmentDetailOwnership(StrEnum):
    EXTERNAL = "external"
    MANAGED = "managed"

    def __str__(self) -> str:
        return str(self.value)
