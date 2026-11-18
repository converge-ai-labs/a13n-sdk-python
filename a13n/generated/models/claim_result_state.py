from enum import StrEnum


class ClaimResultState(StrEnum):
    APPROVED = "approved"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
