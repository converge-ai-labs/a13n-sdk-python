from enum import StrEnum


class NativeToolSearchConfigStrategyType0(StrEnum):
    BM25 = "bm25"
    REGEX = "regex"

    def __str__(self) -> str:
        return str(self.value)
