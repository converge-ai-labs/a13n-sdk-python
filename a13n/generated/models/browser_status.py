from enum import StrEnum


class BrowserStatus(StrEnum):
    CREATING = "creating"
    DELETED = "deleted"
    DELETING = "deleting"
    LOST = "lost"
    READY = "ready"
    RESERVED = "reserved"
    STARTING = "starting"
    STOPPED = "stopped"
    STOPPING = "stopping"

    def __str__(self) -> str:
        return str(self.value)
