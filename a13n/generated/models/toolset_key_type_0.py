from enum import StrEnum


class ToolsetKeyType0(StrEnum):
    ASSETS = "assets"
    COMPUTER = "computer"
    FILES = "files"
    MEMORY = "memory"
    SHELL = "shell"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
