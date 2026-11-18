from enum import StrEnum


class OrganizationCandidateStatus(StrEnum):
    APPLIED = "applied"
    DISCARDED = "discarded"
    FAILED = "failed"
    GENERATING = "generating"
    READY = "ready"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
