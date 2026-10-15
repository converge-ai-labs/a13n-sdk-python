from enum import StrEnum


class ThreadViewPurpose(StrEnum):
    CONVERSATION = "conversation"
    MEMORY_ORGANIZATION = "memory_organization"

    def __str__(self) -> str:
        return str(self.value)
