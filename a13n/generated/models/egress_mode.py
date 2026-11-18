from enum import StrEnum


class EgressMode(StrEnum):
    CONTROLLED = "controlled"
    DENY = "deny"
    INHERIT = "inherit"

    def __str__(self) -> str:
        return str(self.value)
