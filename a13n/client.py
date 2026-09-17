"""Bounded async Native transport. Mutations are never replayed automatically."""

import asyncio
import copy
import json
from collections.abc import AsyncIterator, Awaitable, Callable
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from http.cookiejar import Cookie, CookieJar, DefaultCookiePolicy
from typing import Any, Literal
from urllib.parse import quote, urlsplit

import httpx2
from pydantic import BaseModel, JsonValue, TypeAdapter, ValidationError

from .generated.client import AuthenticatedClient
from .generated.resources import (
    Organizations,
    QueuedSubmissions,
    RunAttempts,
    Runs,
    ServiceResources,
    Sessions,
    Threads,
    Workspaces,
)
from .generated.types import Response
from .models import (
    CreateWebProviderRequest,
    Page,
    Representation,
    UpdateWebProviderRequest,
    WebProvider,
    WebProviderDefinition,
    WebProviderReference,
    WebProviderTestResult,
)


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


@dataclass(frozen=True)
class WebProviderScope:
    kind: Literal["workspace", "organization"]
    id: str

    @property
    def path(self) -> str:
        if self.kind not in {"workspace", "organization"}:
            raise ValueError("Invalid Web Provider scope")
        return f"/{self.kind}s/{_segment(self.id)}/web-providers"


def _segment(value: str) -> str:
    if not value or value in {".", ".."}:
        raise ValueError("A nonblank resource identifier is required")
    return quote(value, safe="")


class _CredentialContext(BaseModel):
    workspace_id: str | None = None


class _EmptyRequest(BaseModel):
    pass


class _RejectCookies(DefaultCookiePolicy):
    def set_ok(self, cookie: Cookie, request: Any) -> bool:
        return False

    def return_ok(self, cookie: Cookie, request: Any) -> bool:
        return False


@dataclass
class _ManagedAuth(httpx2.Auth):
    mode: Literal["public", "bearer", "session"]
    token: str | None = field(default=None, repr=False)
    origin: str | None = None
    workspace_id: str | None = None
    csrf_token: str | None = field(default=None, repr=False)

    def auth_flow(self, request: httpx2.Request):
        if self.mode != "session":
            request.headers.pop("Cookie", None)
        if self.mode == "bearer":
            assert self.token is not None
            request.headers["Authorization"] = f"Bearer {self.token}"
        elif self.mode == "session":
            assert self.origin is not None
            request.headers["Origin"] = self.origin
            if self.workspace_id is not None:
                request.headers["X-A13N-Workspace-ID"] = self.workspace_id
            if request.method not in {"GET", "HEAD", "OPTIONS", "TRACE"} and self.csrf_token is not None:
                request.headers["X-A13N-CSRF-Token"] = self.csrf_token
        yield request


class Client:
    """Async Native client with one explicit credential mode and owned transport."""

    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        *,
        timeout: float = 30,
        transport: httpx2.AsyncBaseTransport | None = None,
    ) -> None:
        self._initialize(
            base_url,
            _ManagedAuth("bearer" if token is not None else "public", token=token),
            cookies=None,
            timeout=timeout,
            transport=transport,
        )

    @classmethod
    def session(
        cls,
        base_url: str,
        *,
        origin: str,
        workspace_id: str | None = None,
        cookies: httpx2.Cookies | None = None,
        csrf_token: str | None = None,
        timeout: float = 30,
        transport: httpx2.AsyncBaseTransport | None = None,
    ) -> "Client":
        if not origin:
            raise ValueError("origin must be nonblank")
        client = cls.__new__(cls)
        managed_cookies = httpx2.Cookies()
        if cookies is not None:
            for cookie in cookies.jar:
                managed_cookies.jar.set_cookie(copy.copy(cookie))
        client._initialize(
            base_url,
            _ManagedAuth("session", origin=origin, workspace_id=workspace_id, csrf_token=csrf_token),
            cookies=managed_cookies,
            timeout=timeout,
            transport=transport,
        )
        return client

    def _initialize(
        self,
        base_url: str,
        auth: _ManagedAuth,
        *,
        cookies: httpx2.Cookies | None,
        timeout: float,
        transport: httpx2.AsyncBaseTransport | None,
    ) -> None:
        url = urlsplit(base_url)
        if (
            url.scheme not in {"http", "https"}
            or not url.netloc
            or url.username
            or url.password
            or url.query
            or url.fragment
        ):
            raise ValueError("base_url must be an HTTP(S) URL without credentials, query, or fragment")
        if timeout <= 0:
            raise ValueError("timeout must be positive")
        self._timeout = timeout
        self._auth = auth
        self._tasks: dict[asyncio.Task[Any], int] = {}
        self._streams: set[httpx2.Response] = set()
        self._closed = False
        if auth.mode != "session":
            cookies = httpx2.Cookies(CookieJar(policy=_RejectCookies()))
        self._http = httpx2.AsyncClient(
            base_url=base_url.rstrip("/") + "/",
            auth=auth,
            cookies=cookies,
            timeout=timeout,
            follow_redirects=False,
            trust_env=False,
            transport=transport,
        )
        self._api = AuthenticatedClient(base_url=base_url, token="").set_async_httpx_client(self._http)

    def set_csrf_token(self, value: str | None) -> None:
        if self._auth.mode != "session":
            raise RuntimeError("CSRF proof is available only for session clients")
        if value is not None and not isinstance(value, str):
            raise TypeError("csrf_token must be a string or None")
        self._auth.csrf_token = value

    @property
    def resources(self) -> ServiceResources:
        return ServiceResources(self)

    @property
    def workspaces(self) -> Workspaces:
        return self.resources.workspaces

    @property
    def organizations(self) -> Organizations:
        return self.resources.organizations

    @property
    def runs(self) -> Runs:
        return self.resources.runs

    @property
    def threads(self) -> Threads:
        return self.resources.threads

    @property
    def sessions(self) -> Sessions:
        return self.resources.sessions

    @property
    def queued_submissions(self) -> QueuedSubmissions:
        return self.resources.queued_submissions

    @property
    def run_attempts(self) -> RunAttempts:
        return self.resources.run_attempts

    def _enter_io(self) -> asyncio.Task[Any] | None:
        if self._closed:
            raise TransportError("Client is closed")
        task = asyncio.current_task()
        if task is not None:
            self._tasks[task] = self._tasks.get(task, 0) + 1
        return task

    def _leave_io(self, task: asyncio.Task[Any] | None) -> None:
        if task is None:
            return
        remaining = self._tasks[task] - 1
        if remaining:
            self._tasks[task] = remaining
        else:
            self._tasks.pop(task)

    async def execute[T](self, operation: Callable[[AuthenticatedClient], Awaitable[Response[T]]]) -> Response[T]:
        """Execute one generated async operation without automatic replay."""
        task = self._enter_io()
        try:
            async with asyncio.timeout(self._timeout):
                return await operation(self._api)
        except (httpx2.HTTPError, TimeoutError):
            raise TransportError("Service transport failed; mutation outcome may be unknown") from None
        finally:
            self._leave_io(task)

    @asynccontextmanager
    async def stream(self, request: dict[str, Any]) -> AsyncIterator[httpx2.Response]:
        """Send a generated request without buffering its response body."""
        task = self._enter_io()
        try:
            async with self._http.stream(**request) as response:
                self._streams.add(response)
                try:
                    yield response
                finally:
                    self._streams.discard(response)
        finally:
            self._leave_io(task)

    async def __aenter__(self) -> "Client":
        return self

    async def __aexit__(self, *_args: object) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        if self._closed:
            return
        self._closed = True
        current = asyncio.current_task()
        active = tuple(task for task in self._tasks if task is not current)
        for response in tuple(self._streams):
            await response.aclose()
        for task in active:
            task.cancel()
        if active:
            await asyncio.gather(*active, return_exceptions=True)
        self._auth.token = None
        self._auth.csrf_token = None
        self._http.headers.clear()
        self._http.cookies.clear()
        await self._http.aclose()

    async def _request[T](
        self,
        method: str,
        path: str,
        result_type: type[T],
        *,
        body: BaseModel | None = None,
        etag: str | None = None,
        params: dict | None = None,
    ) -> Representation[T]:
        task = self._enter_io()
        payload = body.model_dump(mode="json", exclude_unset=True) if body else None
        if isinstance(body, CreateWebProviderRequest | UpdateWebProviderRequest) and body.credential is not None:
            assert payload is not None
            payload["credential"] = body.credential.get_secret_value()
        try:
            async with asyncio.timeout(self._timeout):
                async with self._http.stream(
                    method,
                    "api/v1/" + path.lstrip("/"),
                    json=payload,
                    headers={"If-Match": etag} if etag else None,
                    params=params,
                ) as response:
                    raw = bytearray()
                    async for chunk in response.aiter_bytes():
                        raw.extend(chunk)
                        if len(raw) > 1_048_576:
                            raise ProtocolError("Service response exceeded the byte limit")
                    try:
                        value = json.loads(raw)
                    except (ValueError, UnicodeError):
                        raise ProtocolError("Service returned invalid JSON") from None
                    request_id = response.headers.get("X-Request-ID")
                    if not response.is_success:
                        error = value.get("error", {}) if isinstance(value, dict) else {}
                        if not isinstance(error, dict):
                            error = {}
                        raise ApiError(
                            response.status_code,
                            code if isinstance(code := error.get("code"), str) else "http_error",
                            message if isinstance(message := error.get("message"), str) else "Service request failed",
                            details if isinstance(details := error.get("details"), dict) else {},
                            error.get("request_id") if isinstance(error.get("request_id"), str) else request_id,
                            response.headers.get("Retry-After"),
                        )
                    try:
                        parsed = TypeAdapter(result_type).validate_python(value)
                    except ValidationError:
                        raise ProtocolError("Service returned an invalid representation") from None
                    return Representation(value=parsed, etag=response.headers.get("ETag"), request_id=request_id)
        except (httpx2.HTTPError, TimeoutError):
            raise TransportError("Service transport failed; mutation outcome may be unknown") from None
        finally:
            if payload is not None:
                payload.clear()
            self._leave_io(task)

    async def workspace(self) -> "WorkspaceClient":
        """Bind operations to the API key's Workspace, sharing this transport."""
        context = (await self._request("GET", "/auth/context", _CredentialContext)).value
        if not context.workspace_id:
            raise ValueError("Workspace operations require a Workspace-bound credential")
        return WorkspaceClient(self, context.workspace_id)

    async def web_provider_types(self) -> Page[WebProviderDefinition]:
        return (await self._request("GET", "/web-provider-types", Page[WebProviderDefinition])).value

    async def web_provider_type(self, provider_type: str) -> WebProviderDefinition:
        return (
            await self._request("GET", f"/web-provider-types/{_segment(provider_type)}", WebProviderDefinition)
        ).value

    async def web_providers(
        self,
        scope: WebProviderScope,
        *,
        cursor: str | None = None,
        limit: int = 100,
        type: str | None = None,
        enabled: bool | None = None,
    ) -> Page[WebProvider]:
        params = {
            key: value
            for key, value in {"cursor": cursor, "limit": limit, "type": type, "enabled": enabled}.items()
            if value is not None
        }
        return (await self._request("GET", scope.path, Page[WebProvider], params=params)).value

    async def web_provider(self, scope: WebProviderScope, provider_id: str) -> Representation[WebProvider]:
        return await self._request("GET", f"{scope.path}/{_segment(provider_id)}", WebProvider)

    async def create_web_provider(
        self, scope: WebProviderScope, request: CreateWebProviderRequest
    ) -> Representation[WebProvider]:
        return await self._request("POST", scope.path, WebProvider, body=request)

    async def update_web_provider(
        self, scope: WebProviderScope, provider_id: str, etag: str, request: UpdateWebProviderRequest
    ) -> Representation[WebProvider]:
        if not etag or etag.startswith("W/"):
            raise ValueError("A strong account ETag is required")
        return await self._request(
            "PATCH", f"{scope.path}/{_segment(provider_id)}", WebProvider, body=request, etag=etag
        )

    async def test_web_provider(self, scope: WebProviderScope, provider_id: str) -> WebProviderTestResult:
        # Explicit empty object; a saved-account probe is never retried.
        return (
            await self._request(
                "POST", f"{scope.path}/{_segment(provider_id)}/test", WebProviderTestResult, body=_EmptyRequest()
            )
        ).value

    async def web_provider_references(
        self, scope: WebProviderScope, provider_id: str, *, cursor: str | None = None, limit: int = 100
    ) -> Page[WebProviderReference]:
        params = {"limit": limit, **({"cursor": cursor} if cursor is not None else {})}
        return (
            await self._request(
                "GET", f"{scope.path}/{_segment(provider_id)}/references", Page[WebProviderReference], params=params
            )
        ).value


class WorkspaceClient:
    """Search operations bound to an immutable Workspace ID by Client.workspace()."""

    def __init__(self, client: Client, workspace_id: str):
        self._client = client
        self._scope = WebProviderScope("workspace", workspace_id)

    async def web_providers(
        self,
        *,
        cursor: str | None = None,
        limit: int = 100,
        type: str | None = None,
        enabled: bool | None = None,
    ) -> Page[WebProvider]:
        return await self._client.web_providers(self._scope, cursor=cursor, limit=limit, type=type, enabled=enabled)

    async def web_provider(self, provider_id: str) -> Representation[WebProvider]:
        return await self._client.web_provider(self._scope, provider_id)

    async def create_web_provider(self, request: CreateWebProviderRequest) -> Representation[WebProvider]:
        return await self._client.create_web_provider(self._scope, request)

    async def update_web_provider(
        self,
        provider_id: str,
        etag: str,
        request: UpdateWebProviderRequest,
    ) -> Representation[WebProvider]:
        return await self._client.update_web_provider(self._scope, provider_id, etag, request)

    async def test_web_provider(self, provider_id: str) -> WebProviderTestResult:
        return await self._client.test_web_provider(self._scope, provider_id)

    async def web_provider_references(
        self,
        provider_id: str,
        *,
        cursor: str | None = None,
        limit: int = 100,
    ) -> Page[WebProviderReference]:
        return await self._client.web_provider_references(self._scope, provider_id, cursor=cursor, limit=limit)
