from enum import StrEnum


class RunAgentApiV1RunsRunIdAgentGetSectionType0(StrEnum):
    EFFECTIVE = "effective"
    ORIGINAL = "original"
    OVERRIDES = "overrides"

    def __str__(self) -> str:
        return str(self.value)
