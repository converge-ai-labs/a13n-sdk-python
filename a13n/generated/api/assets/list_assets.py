from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.asset_page import AssetPage
from ...models.error_envelope import ErrorEnvelope
from ...models.list_assets_order import ListAssetsOrder
from ...models.list_assets_source_kind_type_0 import ListAssetsSourceKindType0
from ...models.list_assets_status import ListAssetsStatus
from ...types import UNSET, Response, Unset


def build_request(
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    created_by_id: str | Unset | None = UNSET,
    source_kind: ListAssetsSourceKindType0 | Unset | None = UNSET,
    status: ListAssetsStatus | Unset = UNSET,
    order: ListAssetsOrder | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: str | Unset | None
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_query: str | Unset | None
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    json_created_by_id: str | Unset | None
    if isinstance(created_by_id, Unset):
        json_created_by_id = UNSET
    else:
        json_created_by_id = created_by_id
    params["created_by_id"] = json_created_by_id

    json_source_kind: str | Unset | None
    if isinstance(source_kind, Unset):
        json_source_kind = UNSET
    elif isinstance(source_kind, ListAssetsSourceKindType0):
        json_source_kind = source_kind.value
    else:
        json_source_kind = source_kind
    params["source_kind"] = json_source_kind

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/assets",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AssetPage | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = AssetPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AssetPage | ErrorEnvelope]:
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
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    created_by_id: str | Unset | None = UNSET,
    source_kind: ListAssetsSourceKindType0 | Unset | None = UNSET,
    status: ListAssetsStatus | Unset = UNSET,
    order: ListAssetsOrder | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[AssetPage | ErrorEnvelope]:
    """List Assets

    Args:
        limit (int | Unset):
        cursor (None | str | Unset):
        query (None | str | Unset): Case-insensitive literal filename substring.
        created_by_id (None | str | Unset):
        source_kind (ListAssetsSourceKindType0 | None | Unset):
        status (ListAssetsStatus | Unset):
        order (ListAssetsOrder | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetPage | ErrorEnvelope]
    """

    kwargs = build_request(
        limit=limit,
        cursor=cursor,
        query=query,
        created_by_id=created_by_id,
        source_kind=source_kind,
        status=status,
        order=order,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    created_by_id: str | Unset | None = UNSET,
    source_kind: ListAssetsSourceKindType0 | Unset | None = UNSET,
    status: ListAssetsStatus | Unset = UNSET,
    order: ListAssetsOrder | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> AssetPage | ErrorEnvelope | None:
    """List Assets

    Args:
        limit (int | Unset):
        cursor (None | str | Unset):
        query (None | str | Unset): Case-insensitive literal filename substring.
        created_by_id (None | str | Unset):
        source_kind (ListAssetsSourceKindType0 | None | Unset):
        status (ListAssetsStatus | Unset):
        order (ListAssetsOrder | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetPage | ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        query=query,
        created_by_id=created_by_id,
        source_kind=source_kind,
        status=status,
        order=order,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    created_by_id: str | Unset | None = UNSET,
    source_kind: ListAssetsSourceKindType0 | Unset | None = UNSET,
    status: ListAssetsStatus | Unset = UNSET,
    order: ListAssetsOrder | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[AssetPage | ErrorEnvelope]:
    """List Assets

    Args:
        limit (int | Unset):
        cursor (None | str | Unset):
        query (None | str | Unset): Case-insensitive literal filename substring.
        created_by_id (None | str | Unset):
        source_kind (ListAssetsSourceKindType0 | None | Unset):
        status (ListAssetsStatus | Unset):
        order (ListAssetsOrder | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetPage | ErrorEnvelope]
    """

    kwargs = build_request(
        limit=limit,
        cursor=cursor,
        query=query,
        created_by_id=created_by_id,
        source_kind=source_kind,
        status=status,
        order=order,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    created_by_id: str | Unset | None = UNSET,
    source_kind: ListAssetsSourceKindType0 | Unset | None = UNSET,
    status: ListAssetsStatus | Unset = UNSET,
    order: ListAssetsOrder | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> AssetPage | ErrorEnvelope | None:
    """List Assets

    Args:
        limit (int | Unset):
        cursor (None | str | Unset):
        query (None | str | Unset): Case-insensitive literal filename substring.
        created_by_id (None | str | Unset):
        source_kind (ListAssetsSourceKindType0 | None | Unset):
        status (ListAssetsStatus | Unset):
        order (ListAssetsOrder | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetPage | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            query=query,
            created_by_id=created_by_id,
            source_kind=source_kind,
            status=status,
            order=order,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
