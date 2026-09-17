from enum import StrEnum


class GetWorkspacesWorkspaceBotsPlatformType0(StrEnum):
    GITHUB = "github"
    LARK = "lark"
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
