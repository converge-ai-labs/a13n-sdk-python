from enum import StrEnum


class ListMembersKindType0(StrEnum):
    SERVICE_ACCOUNT = "service_account"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
