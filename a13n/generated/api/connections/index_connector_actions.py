from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.catalog_index import CatalogIndex
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    provider_id: str,
    app: str,
    *,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_query: str | Unset | None
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

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
        "url": "/api/v1/connector-providers/{provider_id}/apps/{app}/actions/index".format(
            provider_id=quote(str(provider_id), safe=""),
            app=quote(str(app), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CatalogIndex | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = CatalogIndex.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CatalogIndex | ErrorEnvelope]:
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
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[CatalogIndex | ErrorEnvelope]:
    """Index Connector Actions

     Search full names and descriptions; definitions are read separately by exact name.

    Args:
        provider_id (str):
        app (str):
        query (None | str | Unset): Case-insensitive substring of full names and descriptions.
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogIndex | ErrorEnvelope]
    """

    kwargs = build_request(
        provider_id=provider_id,
        app=app,
        query=query,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> CatalogIndex | ErrorEnvelope | None:
    """Index Connector Actions

     Search full names and descriptions; definitions are read separately by exact name.

    Args:
        provider_id (str):
        app (str):
        query (None | str | Unset): Case-insensitive substring of full names and descriptions.
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogIndex | ErrorEnvelope
    """

    return sync_detailed(
        provider_id=provider_id,
        app=app,
        client=client,
        query=query,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[CatalogIndex | ErrorEnvelope]:
    """Index Connector Actions

     Search full names and descriptions; definitions are read separately by exact name.

    Args:
        provider_id (str):
        app (str):
        query (None | str | Unset): Case-insensitive substring of full names and descriptions.
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogIndex | ErrorEnvelope]
    """

    kwargs = build_request(
        provider_id=provider_id,
        app=app,
        query=query,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> CatalogIndex | ErrorEnvelope | None:
    """Index Connector Actions

     Search full names and descriptions; definitions are read separately by exact name.

    Args:
        provider_id (str):
        app (str):
        query (None | str | Unset): Case-insensitive substring of full names and descriptions.
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogIndex | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            app=app,
            client=client,
            query=query,
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
