from enum import StrEnum


class AssistantReadinessSetupActionsItem(StrEnum):
    CONFIGURE_MODEL = "configure_model"
    CONTACT_ADMINISTRATOR = "contact_administrator"
    OPEN_PROVIDER = "open_provider"

    def __str__(self) -> str:
        return str(self.value)
