from enum import StrEnum


class ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0(StrEnum):
    SERVICE_ACCOUNT = "service_account"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
