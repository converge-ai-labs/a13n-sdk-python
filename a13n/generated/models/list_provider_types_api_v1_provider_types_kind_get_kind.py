from enum import StrEnum


class ListProviderTypesApiV1ProviderTypesKindGetKind(StrEnum):
    CONNECTOR = "connector"
    ENVIRONMENT = "environment"
    MEMORY = "memory"
    MODEL = "model"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
