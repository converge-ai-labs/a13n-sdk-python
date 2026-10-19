from enum import StrEnum


class GetEntryApiV1ThreadsThreadIdInboxEntryIdGetSectionType0(StrEnum):
    FAILURE = "failure"
    OPTIONS = "options"
    PAYLOAD = "payload"

    def __str__(self) -> str:
        return str(self.value)
