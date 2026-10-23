from enum import StrEnum


class Steering(StrEnum):
    BOUNDARY = "boundary"
    IMMEDIATE = "immediate"

    def __str__(self) -> str:
        return str(self.value)
