from enum import StrEnum


class SkillPublicationReceiptOutcome(StrEnum):
    ALREADY_DEFAULT = "already_default"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)
