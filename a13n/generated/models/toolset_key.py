from enum import StrEnum


class ToolsetKey(StrEnum):
    ASSETS = "assets"
    CONFIGURATION = "configuration"
    FILES = "files"
    MEMORY = "memory"
    SHELL = "shell"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
