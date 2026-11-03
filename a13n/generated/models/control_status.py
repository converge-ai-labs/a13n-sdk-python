from enum import StrEnum


class ControlStatus(StrEnum):
    AUTOMATION = "automation"
    DRAINING = "draining"
    HUMAN = "human"
    RETURNING = "returning"

    def __str__(self) -> str:
        return str(self.value)
