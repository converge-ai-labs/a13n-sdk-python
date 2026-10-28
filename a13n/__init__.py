"""Python SDK for a13n Native Service."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("a13n")
except PackageNotFoundError:  # pragma: no cover - source-tree imports without installation
    __version__ = "0.0.0"

from ._interaction import Agent, InboxEntry, Interaction, Run, RunOutcome, Submitted, Thread
from ._resources import Result
from ._values import (
    AgentOverride,
    Answer,
    Approve,
    AssetPart,
    Deny,
    ExecutionOverride,
    Failed,
    Failure,
    Input,
    JsonPart,
    MemoryMount,
    MountCreate,
    Pending,
    PendingRequest,
    Returned,
    RunConfiguration,
    RunOptions,
    TextPart,
    ToolExecutionOverride,
    UrlPart,
    UsageLimit,
)
from .client import Client
from .errors import (
    A13nError,
    ApiError,
    PreviewInterrupted,
    ProtocolError,
    SubmissionError,
    TransportError,
    UnknownOutcomeError,
)
from .generated.models import Delivery, RunStatus
from .generated.resources import Organization, Session, Workspace
from .generated.types import UNSET, Unset
from .session_streaming import (
    SessionAppReadyFrame,
    SessionDeltaFrame,
    SessionFrame,
    SessionGapFrame,
    SessionItemsFrame,
    SessionOccurrenceFrame,
    SessionScheduleFrame,
    SessionStream,
    SessionThreadFrame,
)
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
    "UNSET",
    "A13nError",
    "Agent",
    "AgentOverride",
    "Answer",
    "ApiError",
    "Approve",
    "AssetPart",
    "BoundaryFrame",
    "ChangedFrame",
    "Client",
    "Delivery",
    "DeltaFrame",
    "Deny",
    "ExecutionOverride",
    "Failed",
    "Failure",
    "GapFrame",
    "InboxEntry",
    "Input",
    "Interaction",
    "JsonPart",
    "MemoryMount",
    "MountCreate",
    "Organization",
    "Pending",
    "PendingRequest",
    "PreviewInterrupted",
    "ProtocolError",
    "ResetFrame",
    "Result",
    "Returned",
    "Run",
    "RunConfiguration",
    "RunOptions",
    "RunOutcome",
    "RunStatus",
    "Session",
    "SessionAppReadyFrame",
    "SessionDeltaFrame",
    "SessionFrame",
    "SessionGapFrame",
    "SessionItemsFrame",
    "SessionOccurrenceFrame",
    "SessionScheduleFrame",
    "SessionStream",
    "SessionThreadFrame",
    "StreamResponse",
    "SubmissionError",
    "Submitted",
    "TextPart",
    "Thread",
    "ThreadFrame",
    "ThreadStream",
    "ToolExecutionOverride",
    "TransportError",
    "UnknownOutcomeError",
    "Unset",
    "UrlPart",
    "UsageLimit",
    "Workspace",
    "__version__",
]
