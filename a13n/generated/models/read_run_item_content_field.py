from enum import StrEnum


class ReadRunItemContentField(StrEnum):
    ALL = "all"
    ARGUMENTS = "arguments"
    FAILURE = "failure"
    METADATA = "metadata"
    RESULT = "result"
    RESULT_PARTS = "result_parts"
    TEXT = "text"
    VALUE = "value"

    def __str__(self) -> str:
        return str(self.value)
