from enum import StrEnum


class EnvironmentViewKind(StrEnum):
    EXTERNAL = "external"
    EXTERNAL_HTTP = "external_http"
    MANAGED = "managed"

    def __str__(self) -> str:
        return str(self.value)
