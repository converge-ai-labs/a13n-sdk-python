"""Python SDK for a13n Native Service."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("a13n")
except PackageNotFoundError:  # pragma: no cover - source-tree imports without installation
    __version__ = "0.0.0"

from ._interaction import Resumed, Submitted, text_input
from ._resources import Result
from .client import Client
from .errors import ApiError, ProtocolError, TransportError
from .generated.resources import Agent, InboxEntry, Organization, Run, Session, Thread, Workspace
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
    "Organization",
    "ProtocolError",
    "ResetFrame",
    "Result",
    "Resumed",
    "Run",
    "Session",
    "StreamResponse",
    "Submitted",
    "Thread",
    "ThreadFrame",
    "ThreadStream",
    "TransportError",
    "Workspace",
    "__version__",
    "text_input",
]
