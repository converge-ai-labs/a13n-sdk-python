"""Shared mechanics for statically generated resource objects."""

from collections.abc import AsyncIterator, Awaitable, Callable, Mapping
from contextlib import AbstractAsyncContextManager
from dataclasses import dataclass
from types import MappingProxyType
from typing import TYPE_CHECKING, Any

import httpx2

from .generated.client import AuthenticatedClient
from .generated.models.error_response import ErrorResponse
from .generated.types import Response, Unset

if TYPE_CHECKING:
    from .client import Client


@dataclass(frozen=True, repr=False)
class Result[T]:
    """A typed HTTP snapshot with evidence, never a live resource mirror."""

    value: T
    status: int
    headers: Mapping[str, str]
    content: bytes

    @property
    def etag(self) -> str | None:
        return self.headers.get("etag")

    @property
    def request_id(self) -> str | None:
        return self.headers.get("x-request-id")

    def __repr__(self) -> str:
        return f"Result(status={self.status})"


class Resource:
    """A local identity binding. Construction never performs I/O."""

    def __init__(self, client: "Client", bindings: Mapping[str, str] | None = None) -> None:
        self._client = client
        self._bindings = MappingProxyType(dict(bindings or {}))

    @property
    def id(self) -> str:
        """Last bound selector; this may be a key, not a resolved immutable ID."""
        if not self._bindings:
            raise ValueError("This collection has no bound identity")
        return self._bindings[next(reversed(self._bindings))]

    def _bind(self, name: str, value: str) -> dict[str, str]:
        if not isinstance(value, str) or not value or value in {".", ".."}:
            raise ValueError("A nonblank resource selector is required")
        return {**self._bindings, name: value}

    async def _call[T](
        self, operation: Callable[[AuthenticatedClient], Awaitable[Response[T | ErrorResponse]]]
    ) -> Result[T]:
        from .client import ApiError, ProtocolError

        try:
            response = await self._client.execute(operation)
        except (ValueError, KeyError, TypeError, AttributeError):
            raise ProtocolError("Malformed Service response") from None
        parsed = response.parsed
        if isinstance(parsed, ErrorResponse):
            error = parsed.error
            raise ApiError(
                status=int(response.status_code),
                code=error.code,
                message=error.message,
                details={} if isinstance(error.details, Unset) or error.details is None else error.details.to_dict(),
                request_id=response.headers.get("x-request-id") or error.request_id,
                retry_after=response.headers.get("retry-after"),
            )
        if not 200 <= response.status_code < 300:
            raise ProtocolError("Service returned an unexpected response status")
        # Generated parsers own body requirements. None is valid both for 204
        # and JSON null (for example, accepted password/email change requests).
        # A missing or malformed required model already failed during parsing.
        from typing import cast

        return Result(
            cast("T", parsed),
            int(response.status_code),
            MappingProxyType({key.lower(): value for key, value in response.headers.items()}),
            response.content,
        )

    def _stream(self, request: dict[str, Any]) -> AbstractAsyncContextManager[httpx2.Response]:
        return self._client.stream(request)

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"


async def pages[T](
    fetch: Callable[[str | Unset | None], Awaitable[Result[T]]],
    cursor_of: Callable[[T], str | Unset | None],
    cursor: str | Unset | None,
) -> AsyncIterator[Result[T]]:
    """Lazy, no prefetch, and never terminate on a short/empty page."""
    from .client import ProtocolError

    seen: set[str] = {cursor} if isinstance(cursor, str) else set()
    while True:
        page = await fetch(cursor)
        yield page
        following = cursor_of(page.value)
        if following is None or isinstance(following, Unset):
            return
        if following in seen:
            raise ProtocolError("Service returned a repeated pagination cursor")
        seen.add(following)
        cursor = following
