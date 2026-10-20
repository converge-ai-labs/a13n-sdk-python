from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.mcp_server_page import McpServerPage
from ...types import UNSET, Response, Unset


def build_request(
    *,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/mcp-servers",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | McpServerPage:
    if response.status_code == 200:
        response_200 = McpServerPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | McpServerPage]:
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
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | McpServerPage]:
    """List Mcp Servers

     Suggested Remote MCP servers, packaged and from the deployment; readable by every signed-in
    principal.

    Args:
        query (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | McpServerPage]
    """

    kwargs = build_request(
        query=query,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ErrorEnvelope | McpServerPage | None:
    """List Mcp Servers

     Suggested Remote MCP servers, packaged and from the deployment; readable by every signed-in
    principal.

    Args:
        query (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | McpServerPage
    """

    return sync_detailed(
        client=client,
        query=query,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | McpServerPage]:
    """List Mcp Servers

     Suggested Remote MCP servers, packaged and from the deployment; readable by every signed-in
    principal.

    Args:
        query (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | McpServerPage]
    """

    kwargs = build_request(
        query=query,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ErrorEnvelope | McpServerPage | None:
    """List Mcp Servers

     Suggested Remote MCP servers, packaged and from the deployment; readable by every signed-in
    principal.

    Args:
        query (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | McpServerPage
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
