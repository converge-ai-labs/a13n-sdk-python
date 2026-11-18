from enum import StrEnum


class CandidateApplyMode(StrEnum):
    CHECKED = "checked"
    REPLACE_ALL = "replace_all"

    def __str__(self) -> str:
        return str(self.value)
