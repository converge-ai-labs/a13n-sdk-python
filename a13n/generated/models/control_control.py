from enum import StrEnum


class ControlControl(StrEnum):
    AUTOMATION = "automation"
    DRAINING = "draining"
    HUMAN = "human"
    RETURNING = "returning"

    def __str__(self) -> str:
        return str(self.value)
