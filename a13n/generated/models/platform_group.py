from enum import StrEnum


class PlatformGroup(StrEnum):
    AGENTS = "agents"
    CONNECTIONS = "connections"
    EGRESS_CREDENTIALS = "egress_credentials"
    ENVIRONMENT_TEMPLATES = "environment_templates"
    EXECUTION = "execution"
    MODELS = "models"
    PROVIDERS = "providers"
    SCHEDULES = "schedules"
    SKILLS = "skills"
    SUBSCRIPTIONS = "subscriptions"
    USAGE = "usage"

    def __str__(self) -> str:
        return str(self.value)
