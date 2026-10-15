from enum import StrEnum


class PlatformGroup(StrEnum):
    AGENTS = "agents"
    CONNECTIONS = "connections"
    ENVIRONMENT_TEMPLATES = "environment_templates"
    EXECUTION = "execution"
    MODELS = "models"
    PROVIDERS = "providers"
    SKILLS = "skills"

    def __str__(self) -> str:
        return str(self.value)
