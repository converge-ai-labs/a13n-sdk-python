from enum import StrEnum


class ConfigSection(StrEnum):
    ALL = "all"
    BUILTIN_SKILLS = "builtin_skills"
    CLIENT_TOOLS = "client_tools"
    CONNECTION_TOOLS = "connection_tools"
    DEFAULT_ENVIRONMENT_TEMPLATE_ID = "default_environment_template_id"
    INSTRUCTIONS = "instructions"
    LAZY_ENVIRONMENT = "lazy_environment"
    MEDIA_UNDERSTANDING = "media_understanding"
    MEMORY = "memory"
    MEMORY_MOUNTS = "memory_mounts"
    MODEL = "model"
    MODEL_CHARACTERISTICS = "model_characteristics"
    MODEL_SETTINGS = "model_settings"
    OUTPUT_SPEC = "output_spec"
    PLUGINS = "plugins"
    RETRIES = "retries"
    REVIEWER = "reviewer"
    SKILLS = "skills"
    SKILL_SYNC = "skill_sync"
    SUBAGENTS = "subagents"
    SUBAGENT_MODE = "subagent_mode"
    SUMMARIZE = "summarize"
    TOOLSETS = "toolsets"
    TOOL_SEARCH = "tool_search"
    USER_QUESTIONS = "user_questions"

    def __str__(self) -> str:
        return str(self.value)
