from enum import StrEnum


class WebOperation(StrEnum):
    SCRAPE = "scrape"
    SEARCH = "search"

    def __str__(self) -> str:
        return str(self.value)
