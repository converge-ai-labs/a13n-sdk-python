"""Python SDK for a13n Native Service."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("a13n")
except PackageNotFoundError:  # pragma: no cover - source-tree imports without installation
    __version__ = "0.0.0"

from ._interaction import Resumed, Submitted, text_input
from ._resources import Result
from .client import ApiError, Client, ProtocolError, TransportError
from .generated.resources import Agent, InboxEntry, Organization, Run, Session, Thread, Workspace
from .streaming import StreamResponse, ThreadFrame, ThreadStream

__all__ = [
    "Agent",
    "ApiError",
    "Client",
    "InboxEntry",
    "Organization",
    "ProtocolError",
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
