from enum import StrEnum


class BrowserBindingPreparation(StrEnum):
    FIRST_USE = "first_use"
    RUN_START = "run_start"

    def __str__(self) -> str:
        return str(self.value)
