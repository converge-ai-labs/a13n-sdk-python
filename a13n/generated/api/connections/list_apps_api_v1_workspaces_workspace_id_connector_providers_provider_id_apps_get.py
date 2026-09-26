from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.connector_app_page import ConnectorAppPage
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    workspace_id: str,
    provider_id: str,
    *,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    refresh: bool | Unset = UNSET,
) -> dict[str, Any]:

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

    params["refresh"] = refresh

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workspaces/{workspace_id}/connector-providers/{provider_id}/apps".format(
            workspace_id=quote(str(workspace_id), safe=""),
            provider_id=quote(str(provider_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectorAppPage | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = ConnectorAppPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConnectorAppPage | ErrorEnvelope]:
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
    provider_id: str,
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    refresh: bool | Unset = UNSET,
) -> Response[ConnectorAppPage | ErrorEnvelope]:
    """List Apps

    Args:
        workspace_id (str):
        provider_id (str):
        query (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectorAppPage | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        provider_id=provider_id,
        query=query,
        limit=limit,
        cursor=cursor,
        refresh=refresh,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    refresh: bool | Unset = UNSET,
) -> ConnectorAppPage | ErrorEnvelope | None:
    """List Apps

    Args:
        workspace_id (str):
        provider_id (str):
        query (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectorAppPage | ErrorEnvelope
    """

    return sync_detailed(
        workspace_id=workspace_id,
        provider_id=provider_id,
        client=client,
        query=query,
        limit=limit,
        cursor=cursor,
        refresh=refresh,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    refresh: bool | Unset = UNSET,
) -> Response[ConnectorAppPage | ErrorEnvelope]:
    """List Apps

    Args:
        workspace_id (str):
        provider_id (str):
        query (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectorAppPage | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        provider_id=provider_id,
        query=query,
        limit=limit,
        cursor=cursor,
        refresh=refresh,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    refresh: bool | Unset = UNSET,
) -> ConnectorAppPage | ErrorEnvelope | None:
    """List Apps

    Args:
        workspace_id (str):
        provider_id (str):
        query (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectorAppPage | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            provider_id=provider_id,
            client=client,
            query=query,
            limit=limit,
            cursor=cursor,
            refresh=refresh,
        )
    ).parsed
