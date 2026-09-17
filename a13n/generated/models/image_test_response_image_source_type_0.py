from enum import StrEnum


class ImageTestResponseImageSourceType0(StrEnum):
    LOCAL = "local"
    PULLED = "pulled"

    def __str__(self) -> str:
        return str(self.value)
