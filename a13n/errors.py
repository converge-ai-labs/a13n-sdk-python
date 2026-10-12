"""Public failure categories shared by transport, protocol, and resources."""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from pydantic import JsonValue

if TYPE_CHECKING:
    from ._resources import Result
    from .generated.models import EntryView


class A13nError(Exception):
    """Base for SDK failures; observed Run failures remain outcomes."""


class ProtocolError(A13nError):
    """A malformed or oversized Service response."""


class TransportError(A13nError, RuntimeError):
    """Transport failed; a mutation's outcome can be unknown."""


@dataclass(repr=False)
class UnknownOutcomeError(TransportError):
    """A dispatched mutation has no trustworthy acknowledgement; never auto-retried."""

    idempotency_key: str
    operation: str
    thread_id: str | None = None
    run_id: str | None = None
    evidence: object | None = None

    def __str__(self) -> str:
        return f"{self.operation} acknowledgement unavailable; mutation outcome is unknown"


@dataclass(repr=False)
class PreviewInterrupted(A13nError):
    reason: str
    run_id: str

    def __str__(self) -> str:
        return f"Text preview interrupted: {self.reason}"


@dataclass(repr=False)
class SubmissionError(A13nError):
    """An exact inbox entry settled without incorporation into a Run."""

    thread_id: str
    entry_id: str
    entry: "Result[EntryView]"

    def __str__(self) -> str:
        return f"Submission {self.entry_id} ended as {self.entry.value.status}"


@dataclass(repr=False)
class ApiError(A13nError):
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
