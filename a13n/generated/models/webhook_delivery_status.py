from enum import StrEnum


class WebhookDeliveryStatus(StrEnum):
    DEAD = "dead"
    DELIVERED = "delivered"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
