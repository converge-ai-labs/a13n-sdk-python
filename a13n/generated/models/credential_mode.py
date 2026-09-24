from enum import StrEnum


class CredentialMode(StrEnum):
    FORBIDDEN = "forbidden"
    OPTIONAL = "optional"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
