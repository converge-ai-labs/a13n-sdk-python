from enum import StrEnum


class BuiltinToolsetKey(StrEnum):
    ASSETS = "assets"
    BROWSER = "browser"
    COMPUTER = "computer"
    FILES = "files"
    MEMORY = "memory"
    SHELL = "shell"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
