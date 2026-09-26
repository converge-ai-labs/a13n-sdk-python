from enum import StrEnum


class MemoryRevisionDetailOp(StrEnum):
    CREATE = "create"
    DELETE = "delete"
    MOVE_IN = "move_in"
    MOVE_OUT = "move_out"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
