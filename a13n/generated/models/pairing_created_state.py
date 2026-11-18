from enum import StrEnum


class PairingCreatedState(StrEnum):
    APPROVED = "approved"
    APPROVING = "approving"
    CANCELLED = "cancelled"
    CLAIMED = "claimed"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
