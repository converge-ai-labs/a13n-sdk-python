from enum import StrEnum


class GetTraceApiV1TracesTraceIdGetSectionType0(StrEnum):
    ATTRIBUTES = "attributes"
    EVENTS = "events"
    INPUT = "input"
    LINKS = "links"
    OUTPUT = "output"
    RESOURCE_ATTRIBUTES = "resource_attributes"
    USAGE = "usage"

    def __str__(self) -> str:
        return str(self.value)
