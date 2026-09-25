from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.memory_kind import MemoryKind
from ...models.memory_page import MemoryPage
from ...types import UNSET, Response, Unset


def build_request(
    workspace_id: str,
    *,
    label: list[str] | Unset | None = UNSET,
    kind: MemoryKind | Unset | None = UNSET,
    type_: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_label: list[str] | Unset | None
    if isinstance(label, Unset):
        json_label = UNSET
    elif isinstance(label, list):
        json_label = label

    else:
        json_label = label
    params["label"] = json_label

    json_kind: str | Unset | None
    if isinstance(kind, Unset):
        json_kind = UNSET
    elif isinstance(kind, MemoryKind):
        json_kind = kind.value
    else:
        json_kind = kind
    params["kind"] = json_kind

    json_type_: str | Unset | None
    if isinstance(type_, Unset):
        json_type_ = UNSET
    else:
        json_type_ = type_
    params["type"] = json_type_

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
        "url": "/api/v1/workspaces/{workspace_id}/memories".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | MemoryPage:
    if response.status_code == 200:
        response_200 = MemoryPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | MemoryPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    kind: MemoryKind | Unset | None = UNSET,
    type_: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | MemoryPage]:
    """List Memories

    Args:
        workspace_id (str):
        label (list[str] | None | Unset):
        kind (MemoryKind | None | Unset):
        type_ (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | MemoryPage]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        label=label,
        kind=kind,
        type_=type_,
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
    label: list[str] | Unset | None = UNSET,
    kind: MemoryKind | Unset | None = UNSET,
    type_: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ErrorEnvelope | MemoryPage | None:
    """List Memories

    Args:
        workspace_id (str):
        label (list[str] | None | Unset):
        kind (MemoryKind | None | Unset):
        type_ (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | MemoryPage
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        label=label,
        kind=kind,
        type_=type_,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    kind: MemoryKind | Unset | None = UNSET,
    type_: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | MemoryPage]:
    """List Memories

    Args:
        workspace_id (str):
        label (list[str] | None | Unset):
        kind (MemoryKind | None | Unset):
        type_ (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | MemoryPage]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        label=label,
        kind=kind,
        type_=type_,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    kind: MemoryKind | Unset | None = UNSET,
    type_: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ErrorEnvelope | MemoryPage | None:
    """List Memories

    Args:
        workspace_id (str):
        label (list[str] | None | Unset):
        kind (MemoryKind | None | Unset):
        type_ (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | MemoryPage
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            label=label,
            kind=kind,
            type_=type_,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
