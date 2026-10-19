from enum import StrEnum


class ReadSpanContentApiV1TracesTraceIdSpansSpanIdContentGetSection(StrEnum):
    ALL = "all"
    ATTRIBUTES = "attributes"
    EVENTS = "events"
    INPUT = "input"
    LINKS = "links"
    OUTPUT = "output"
    RESOURCE_ATTRIBUTES = "resource_attributes"
    USAGE = "usage"

    def __str__(self) -> str:
        return str(self.value)
