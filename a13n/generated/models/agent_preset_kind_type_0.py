from enum import StrEnum


class AgentPresetKindType0(StrEnum):
    COMPOSER = "composer"
    FINDING = "finding"

    def __str__(self) -> str:
        return str(self.value)
