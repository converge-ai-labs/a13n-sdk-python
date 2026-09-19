from enum import StrEnum


class WebProviderMetadataOperationsItem(StrEnum):
    SCRAPE = "scrape"
    SEARCH = "search"

    def __str__(self) -> str:
        return str(self.value)
