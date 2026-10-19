from enum import StrEnum


class ListProviderTypesKind(StrEnum):
    CONNECTOR = "connector"
    ENVIRONMENT = "environment"
    MEMORY = "memory"
    MODEL = "model"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
