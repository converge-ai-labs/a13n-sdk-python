from enum import StrEnum


class MemberUsageKind(StrEnum):
    SERVICE_ACCOUNT = "service_account"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
