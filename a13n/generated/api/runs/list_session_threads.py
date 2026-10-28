from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.list_session_threads_origin_type_0_item import ListSessionThreadsOriginType0Item
from ...models.thread_navigation_page import ThreadNavigationPage
from ...types import UNSET, Response, Unset


def build_request(
    session_id: str,
    *,
    origin: list[ListSessionThreadsOriginType0Item] | Unset | None = UNSET,
    thread_id: list[str] | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_origin: list[str] | Unset | None
    if isinstance(origin, Unset):
        json_origin = UNSET
    elif isinstance(origin, list):
        json_origin = []
        for origin_type_0_item_data in origin:
            origin_type_0_item = origin_type_0_item_data.value
            json_origin.append(origin_type_0_item)

    else:
        json_origin = origin
    params["origin"] = json_origin

    json_thread_id: list[str] | Unset | None
    if isinstance(thread_id, Unset):
        json_thread_id = UNSET
    elif isinstance(thread_id, list):
        json_thread_id = thread_id

    else:
        json_thread_id = thread_id
    params["thread_id"] = json_thread_id

    params["limit"] = limit

    json_cursor: str | Unset | None
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sessions/{session_id}/threads".format(
            session_id=quote(str(session_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | ThreadNavigationPage:
    if response.status_code == 200:
        response_200 = ThreadNavigationPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ThreadNavigationPage]:
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
    session_id: str,
    *,
    client: AuthenticatedClient,
    origin: list[ListSessionThreadsOriginType0Item] | Unset | None = UNSET,
    thread_id: list[str] | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ThreadNavigationPage]:
    """List Session Threads

     Lightweight Session navigation, oldest first, with stable per-origin positions and parent
    references.

    Args:
        session_id (str):
        origin (list[ListSessionThreadsOriginType0Item] | None | Unset):
        thread_id (list[str] | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ThreadNavigationPage]
    """

    kwargs = build_request(
        session_id=session_id,
        origin=origin,
        thread_id=thread_id,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient,
    origin: list[ListSessionThreadsOriginType0Item] | Unset | None = UNSET,
    thread_id: list[str] | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | ThreadNavigationPage | None:
    """List Session Threads

     Lightweight Session navigation, oldest first, with stable per-origin positions and parent
    references.

    Args:
        session_id (str):
        origin (list[ListSessionThreadsOriginType0Item] | None | Unset):
        thread_id (list[str] | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ThreadNavigationPage
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        origin=origin,
        thread_id=thread_id,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient,
    origin: list[ListSessionThreadsOriginType0Item] | Unset | None = UNSET,
    thread_id: list[str] | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ThreadNavigationPage]:
    """List Session Threads

     Lightweight Session navigation, oldest first, with stable per-origin positions and parent
    references.

    Args:
        session_id (str):
        origin (list[ListSessionThreadsOriginType0Item] | None | Unset):
        thread_id (list[str] | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ThreadNavigationPage]
    """

    kwargs = build_request(
        session_id=session_id,
        origin=origin,
        thread_id=thread_id,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient,
    origin: list[ListSessionThreadsOriginType0Item] | Unset | None = UNSET,
    thread_id: list[str] | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | ThreadNavigationPage | None:
    """List Session Threads

     Lightweight Session navigation, oldest first, with stable per-origin positions and parent
    references.

    Args:
        session_id (str):
        origin (list[ListSessionThreadsOriginType0Item] | None | Unset):
        thread_id (list[str] | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ThreadNavigationPage
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            origin=origin,
            thread_id=thread_id,
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
