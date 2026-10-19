from enum import StrEnum


class GetModelCatalogApiV1ModelCatalogGetSectionType0(StrEnum):
    ALL = "all"
    CHARACTERISTICS = "characteristics"
    PRICING = "pricing"

    def __str__(self) -> str:
        return str(self.value)
