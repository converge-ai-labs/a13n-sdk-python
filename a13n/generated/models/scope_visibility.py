from enum import StrEnum


class ScopeVisibility(StrEnum):
    GROUP = "group"
    INSTALLATION = "installation"

    def __str__(self) -> str:
        return str(self.value)
