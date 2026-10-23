from enum import StrEnum


class CollectorCapabilityReasonType0(StrEnum):
    MONITORING_DISABLED = "monitoring_disabled"
    NOT_CONFIGURED = "not_configured"

    def __str__(self) -> str:
        return str(self.value)
