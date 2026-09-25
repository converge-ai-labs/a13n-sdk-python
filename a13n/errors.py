"""Public failure categories shared by transport, protocol, and resources."""

from dataclasses import dataclass, field

from pydantic import JsonValue


class ProtocolError(Exception):
    """A malformed or oversized Service response."""


class TransportError(RuntimeError):
    """Transport failed; a mutation's outcome can be unknown."""


@dataclass(repr=False)
class ApiError(Exception):
    status: int
    code: str
    message: str
    details: dict[str, JsonValue] = field(default_factory=dict)
    request_id: str | None = None
    retry_after: str | None = None

    def __str__(self) -> str:
        return f"{self.code}: {self.message} ({self.status})"

    def __repr__(self) -> str:
        return f"ApiError(status={self.status}, code={self.code!r})"
