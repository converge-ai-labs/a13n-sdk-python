from enum import StrEnum


class GetRunSectionType0(StrEnum):
    ENVIRONMENT_MOUNTS = "environment_mounts"
    FAILURE = "failure"
    INPUT = "input"
    LABELS = "labels"
    MEMORY_MOUNTS = "memory_mounts"
    OPTIONS = "options"
    OUTPUT = "output"
    PENDING = "pending"
    RESUME = "resume"
    USAGE_AT_SEAL = "usage_at_seal"

    def __str__(self) -> str:
        return str(self.value)
