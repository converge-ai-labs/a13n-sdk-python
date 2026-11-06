from enum import StrEnum


class ResourceObservationObservation(StrEnum):
    ABSENT = "absent"
    CONFLICT = "conflict"
    PRESENT = "present"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
