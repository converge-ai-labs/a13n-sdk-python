from enum import StrEnum


class ListSkillsApiV1WorkspacesWorkspaceIdSkillsGetSourceType0(StrEnum):
    GITHUB = "github"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
