from enum import StrEnum


class OrganizationRequestOutput(StrEnum):
    CANDIDATE = "candidate"
    DIRECT = "direct"

    def __str__(self) -> str:
        return str(self.value)
