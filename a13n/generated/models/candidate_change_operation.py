from enum import StrEnum


class CandidateChangeOperation(StrEnum):
    CREATE = "create"
    DELETE = "delete"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
