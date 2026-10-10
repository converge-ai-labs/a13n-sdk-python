from enum import StrEnum


class Preset(StrEnum):
    ANSWER = "answer"
    EXECUTION = "execution"
    RECOVERY = "recovery"

    def __str__(self) -> str:
        return str(self.value)
