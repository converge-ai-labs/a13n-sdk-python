from enum import StrEnum


class Collection(StrEnum):
    EXTERNAL = "external"
    NATIVE = "native"
    PROXY = "proxy"
    PULL = "pull"

    def __str__(self) -> str:
        return str(self.value)
