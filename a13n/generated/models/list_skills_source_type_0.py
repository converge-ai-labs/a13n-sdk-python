from enum import StrEnum


class ListSkillsSourceType0(StrEnum):
    GITHUB = "github"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
