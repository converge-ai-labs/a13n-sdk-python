from enum import StrEnum


class OIDCBrand(StrEnum):
    GENERIC = "generic"
    GOOGLE = "google"
    MICROSOFT = "microsoft"

    def __str__(self) -> str:
        return str(self.value)
