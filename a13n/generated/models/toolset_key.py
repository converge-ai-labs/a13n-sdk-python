from enum import StrEnum


class ToolsetKey(StrEnum):
    ASSETS = "assets"
    CONFIGURATION = "configuration"
    FILES = "files"
    FINDINGS = "findings"
    MEMORY = "memory"
    SHELL = "shell"
    TRACES = "traces"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
