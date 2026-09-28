"""Python SDK for a13n Native Service."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("a13n")
except PackageNotFoundError:  # pragma: no cover - source-tree imports without installation
    __version__ = "0.0.0"

from ._interaction import Agent, InboxEntry, Interaction, Resumed, Run, RunOutcome, Submitted, Thread, text_input
from ._resources import Result
from .client import Client
from .errors import ApiError, ProtocolError, SubmissionError, TransportError
from .generated.resources import Organization, Session, Workspace
from .streaming import (
    BoundaryFrame,
    ChangedFrame,
    DeltaFrame,
    GapFrame,
    ResetFrame,
    StreamResponse,
    ThreadFrame,
    ThreadStream,
)

__all__ = [
    "Agent",
    "ApiError",
    "BoundaryFrame",
    "ChangedFrame",
    "Client",
    "DeltaFrame",
    "GapFrame",
    "InboxEntry",
    "Interaction",
    "Organization",
    "ProtocolError",
    "ResetFrame",
    "Result",
    "Resumed",
    "Run",
    "RunOutcome",
    "Session",
    "StreamResponse",
    "SubmissionError",
    "Submitted",
    "Thread",
    "ThreadFrame",
    "ThreadStream",
    "TransportError",
    "Workspace",
    "__version__",
    "text_input",
]
