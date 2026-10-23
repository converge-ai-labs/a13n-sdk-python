from enum import StrEnum


class GetInboxEntrySectionType0(StrEnum):
    FAILURE = "failure"
    OPTIONS = "options"
    PAYLOAD = "payload"

    def __str__(self) -> str:
        return str(self.value)
