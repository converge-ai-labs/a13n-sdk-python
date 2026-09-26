"""Bounded async Native transport. Mutations are never replayed automatically."""

import asyncio
import copy
import ssl
from collections.abc import AsyncIterator, Awaitable, Callable
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from http.cookiejar import Cookie, CookieJar, DefaultCookiePolicy
from typing import Any, Literal
from urllib.parse import urlsplit

import httpx2

from .errors import TransportError
from .generated.client import AuthenticatedClient
from .generated.models import ErrorEnvelope
from .generated.resources import Organizations, ServiceResources, Workspaces
from .generated.types import Response


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
            if request.method not in {"GET", "HEAD", "OPTIONS"} and self.csrf_token is not None:
                request.headers["X-CSRF-Token"] = self.csrf_token
        yield request


class Client:
    """Async Native client with one explicit credential mode and owned transport."""

    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        *,
        timeout: float = 30,
        ca_bundle: str | None = None,
        transport: httpx2.AsyncBaseTransport | None = None,
    ) -> None:
        self._initialize(
            base_url,
            _ManagedAuth("bearer" if token is not None else "public", token=token),
            cookies=None,
            timeout=timeout,
            ca_bundle=ca_bundle,
            transport=transport,
        )

    @classmethod
    def session(
        cls,
        base_url: str,
        *,
        origin: str,
        cookies: httpx2.Cookies | None = None,
        csrf_token: str | None = None,
        timeout: float = 30,
        ca_bundle: str | None = None,
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
            _ManagedAuth("session", origin=origin, csrf_token=csrf_token),
            cookies=managed_cookies,
            timeout=timeout,
            ca_bundle=ca_bundle,
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
        ca_bundle: str | None,
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
        self._io_changed = asyncio.Event()
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
            verify=ssl.create_default_context(cafile=ca_bundle) if ca_bundle is not None else True,
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
            self._io_changed.set()

    async def execute[T](
        self, operation: Callable[[AuthenticatedClient], Awaitable[Response[T | ErrorEnvelope] | Response[T]]]
    ) -> Response[T | ErrorEnvelope] | Response[T]:
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
        # Cancellation ends owned I/O, not necessarily the caller's application task.
        while any(task in self._tasks for task in active):
            self._io_changed.clear()
            await self._io_changed.wait()
        self._auth.token = None
        self._auth.csrf_token = None
        self._http.headers.clear()
        self._http.cookies.clear()
        await self._http.aclose()
