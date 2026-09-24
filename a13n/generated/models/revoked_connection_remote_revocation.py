from enum import StrEnum


class RevokedConnectionRemoteRevocation(StrEnum):
    FAILED = "failed"
    REVOKED = "revoked"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
