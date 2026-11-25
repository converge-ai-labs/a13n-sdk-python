from enum import StrEnum


class ListAssetsSourceKindType0(StrEnum):
    AGENT_RUN = "agent_run"
    USER_UPLOAD = "user_upload"

    def __str__(self) -> str:
        return str(self.value)
