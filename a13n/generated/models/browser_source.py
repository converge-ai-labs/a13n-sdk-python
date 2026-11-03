from enum import StrEnum


class BrowserSource(StrEnum):
    EXTERNAL_CDP = "external_cdp"
    MANAGED = "managed"

    def __str__(self) -> str:
        return str(self.value)
