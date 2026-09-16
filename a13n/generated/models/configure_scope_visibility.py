from enum import StrEnum


class ConfigureScopeVisibility(StrEnum):
    GROUP = "group"
    INSTALLATION = "installation"

    def __str__(self) -> str:
        return str(self.value)
