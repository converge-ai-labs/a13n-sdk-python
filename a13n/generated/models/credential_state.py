from enum import StrEnum


class CredentialState(StrEnum):
    ACTIVE = "active"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
