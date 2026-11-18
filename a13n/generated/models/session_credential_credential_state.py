from enum import StrEnum


class SessionCredentialCredentialState(StrEnum):
    ACTIVE = "active"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
