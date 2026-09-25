from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.thread_page import ThreadPage
from ...types import UNSET, Response, Unset


def build_request(
    workspace_id: str,
    *,
    session_id: str | Unset | None = UNSET,
    label: list[str] | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_session_id: str | Unset | None
    if isinstance(session_id, Unset):
        json_session_id = UNSET
    else:
        json_session_id = session_id
    params["session_id"] = json_session_id

    json_label: list[str] | Unset | None
    if isinstance(label, Unset):
        json_label = UNSET
    elif isinstance(label, list):
        json_label = label

    else:
        json_label = label
    params["label"] = json_label

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
        "url": "/api/v1/workspaces/{workspace_id}/threads".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ThreadPage:
    if response.status_code == 200:
        response_200 = ThreadPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ThreadPage]:
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
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    session_id: str | Unset | None = UNSET,
    label: list[str] | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ThreadPage]:
    """List Threads

    Args:
        workspace_id (str):
        session_id (None | str | Unset):
        label (list[str] | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ThreadPage]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        session_id=session_id,
        label=label,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    session_id: str | Unset | None = UNSET,
    label: list[str] | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ErrorEnvelope | ThreadPage | None:
    """List Threads

    Args:
        workspace_id (str):
        session_id (None | str | Unset):
        label (list[str] | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ThreadPage
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        session_id=session_id,
        label=label,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    session_id: str | Unset | None = UNSET,
    label: list[str] | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ThreadPage]:
    """List Threads

    Args:
        workspace_id (str):
        session_id (None | str | Unset):
        label (list[str] | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ThreadPage]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        session_id=session_id,
        label=label,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    session_id: str | Unset | None = UNSET,
    label: list[str] | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ErrorEnvelope | ThreadPage | None:
    """List Threads

    Args:
        workspace_id (str):
        session_id (None | str | Unset):
        label (list[str] | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ThreadPage
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            session_id=session_id,
            label=label,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
