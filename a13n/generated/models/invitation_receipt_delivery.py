from enum import StrEnum


class InvitationReceiptDelivery(StrEnum):
    MANUAL = "manual"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
