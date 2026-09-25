from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.memory_revision_page import MemoryRevisionPage
from ...types import UNSET, Response, Unset


def build_request(
    workspace_id: str,
    memory_id: str,
    *,
    path: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_path: str | Unset | None
    if isinstance(path, Unset):
        json_path = UNSET
    else:
        json_path = path
    params["path"] = json_path

    json_run_id: str | Unset | None
    if isinstance(run_id, Unset):
        json_run_id = UNSET
    else:
        json_run_id = run_id
    params["run_id"] = json_run_id

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
        "url": "/api/v1/workspaces/{workspace_id}/memories/{memory_id}/revisions".format(
            workspace_id=quote(str(workspace_id), safe=""),
            memory_id=quote(str(memory_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | MemoryRevisionPage:
    if response.status_code == 200:
        response_200 = MemoryRevisionPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | MemoryRevisionPage]:
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
    memory_id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | MemoryRevisionPage]:
    """List Revisions

    Args:
        workspace_id (str):
        memory_id (str):
        path (None | str | Unset):
        run_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | MemoryRevisionPage]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        memory_id=memory_id,
        path=path,
        run_id=run_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    memory_id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ErrorEnvelope | MemoryRevisionPage | None:
    """List Revisions

    Args:
        workspace_id (str):
        memory_id (str):
        path (None | str | Unset):
        run_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | MemoryRevisionPage
    """

    return sync_detailed(
        workspace_id=workspace_id,
        memory_id=memory_id,
        client=client,
        path=path,
        run_id=run_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    memory_id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | MemoryRevisionPage]:
    """List Revisions

    Args:
        workspace_id (str):
        memory_id (str):
        path (None | str | Unset):
        run_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | MemoryRevisionPage]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        memory_id=memory_id,
        path=path,
        run_id=run_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    memory_id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ErrorEnvelope | MemoryRevisionPage | None:
    """List Revisions

    Args:
        workspace_id (str):
        memory_id (str):
        path (None | str | Unset):
        run_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | MemoryRevisionPage
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            memory_id=memory_id,
            client=client,
            path=path,
            run_id=run_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
