from enum import StrEnum


class VideoUrlType(StrEnum):
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
