from enum import StrEnum


class GrantViewSource(StrEnum):
    MANUAL = "manual"
    OIDC = "oidc"

    def __str__(self) -> str:
        return str(self.value)
