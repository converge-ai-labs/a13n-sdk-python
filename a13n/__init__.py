"""Python SDK package for a13n Service."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("a13n")
except PackageNotFoundError:  # pragma: no cover - source-tree imports without installation
    __version__ = "0.0.0"

__all__ = [
    "Agent",
    "AgentConfig",
    "AgentRunOverride",
    "ApiError",
    "Client",
    "CreateWebProviderRequest",
    "DownloadToolConfiguration",
    "FetchToolConfiguration",
    "Organization",
    "Page",
    "ProtocolError",
    "QueuedSubmission",
    "ReplayGap",
    "Representation",
    "Result",
    "Run",
    "RunAccepted",
    "RunAttempt",
    "RunStream",
    "ScrapeToolConfiguration",
    "SearchToolConfiguration",
    "Session",
    "StreamObservation",
    "StreamResponse",
    "SubmissionQueued",
    "Thread",
    "ThreadSubmission",
    "ToolSelection",
    "ToolsetSelection",
    "TransportError",
    "UpdateWebProviderRequest",
    "WebProvider",
    "WebProviderCredential",
    "WebProviderDefinition",
    "WebProviderReference",
    "WebProviderScope",
    "WebProviderTestResult",
    "Workspace",
    "WorkspaceClient",
    "__version__",
    "text_input",
]

from ._interaction import RunAccepted, SubmissionQueued, ThreadSubmission, text_input
from ._resources import Result
from .client import ApiError, Client, ProtocolError, TransportError, WebProviderScope, WorkspaceClient
from .generated.resources import Agent, Organization, QueuedSubmission, Run, RunAttempt, Session, Thread, Workspace
from .models import (
    AgentConfig,
    AgentRunOverride,
    CreateWebProviderRequest,
    DownloadToolConfiguration,
    FetchToolConfiguration,
    Page,
    Representation,
    ScrapeToolConfiguration,
    SearchToolConfiguration,
    ToolSelection,
    ToolsetSelection,
    UpdateWebProviderRequest,
    WebProvider,
    WebProviderCredential,
    WebProviderDefinition,
    WebProviderReference,
    WebProviderTestResult,
)
from .streaming import ReplayGap, RunStream, StreamObservation, StreamResponse
