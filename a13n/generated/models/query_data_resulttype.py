from enum import StrEnum


class QueryDataResulttype(StrEnum):
    MATRIX = "matrix"
    SCALAR = "scalar"
    STRING = "string"
    VECTOR = "vector"

    def __str__(self) -> str:
        return str(self.value)
