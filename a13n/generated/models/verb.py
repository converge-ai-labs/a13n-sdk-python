from enum import StrEnum


class Verb(StrEnum):
    ADMIN = "admin"
    READ = "read"
    RUN = "run"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
