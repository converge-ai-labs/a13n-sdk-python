from enum import StrEnum


class GetModelCatalogSectionType0(StrEnum):
    ALL = "all"
    CHARACTERISTICS = "characteristics"
    PRICING = "pricing"

    def __str__(self) -> str:
        return str(self.value)
