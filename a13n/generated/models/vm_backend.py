from enum import StrEnum


class VmBackend(StrEnum):
    BOXLITE = "boxlite"
    MICROSANDBOX = "microsandbox"

    def __str__(self) -> str:
        return str(self.value)
