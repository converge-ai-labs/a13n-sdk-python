from enum import StrEnum


class EnvironmentProviderAccountConfigurationSource(StrEnum):
    DEPLOYMENT = "deployment"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
