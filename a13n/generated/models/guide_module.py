from enum import StrEnum


class GuideModule(StrEnum):
    JOURNAL = "journal"
    SESSION_NOTES = "session_notes"
    TOPICS = "topics"

    def __str__(self) -> str:
        return str(self.value)
