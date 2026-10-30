from enum import StrEnum


class BrowserStatus(StrEnum):
    CREATING = "creating"
    DELETED = "deleted"
    DELETING = "deleting"
    LOST = "lost"
    READY = "ready"
    RESERVED = "reserved"

    def __str__(self) -> str:
        return str(self.value)
