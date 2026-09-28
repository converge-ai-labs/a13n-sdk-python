from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    thread_id: str,
    name: str,
    *,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/threads/{thread_id}/memories/{name}".format(
            thread_id=quote(str(thread_id), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorEnvelope:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorEnvelope]:
    from ....errors import ProtocolError

    try:
        return Response(
            status_code=HTTPStatus(response.status_code),
            content=response.content,
            headers=response.headers,
            parsed=_parse_response(client=client, response=response),
        )
    except (ValueError, KeyError, TypeError, AttributeError):
        raise ProtocolError("Malformed Service response") from None


def sync_detailed(
    thread_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[Any | ErrorEnvelope]:
    """Remove Mount

    Args:
        thread_id (str):
        name (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        thread_id=thread_id,
        name=name,
        if_match=if_match,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Any | ErrorEnvelope | None:
    """Remove Mount

    Args:
        thread_id (str):
        name (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return sync_detailed(
        thread_id=thread_id,
        name=name,
        client=client,
        if_match=if_match,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[Any | ErrorEnvelope]:
    """Remove Mount

    Args:
        thread_id (str):
        name (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        thread_id=thread_id,
        name=name,
        if_match=if_match,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Any | ErrorEnvelope | None:
    """Remove Mount

    Args:
        thread_id (str):
        name (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            name=name,
            client=client,
            if_match=if_match,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
