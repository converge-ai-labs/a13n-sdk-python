from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.api_key_page import ApiKeyPage
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    *,
    workspace_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_workspace_id: str | Unset | None
    if isinstance(workspace_id, Unset):
        json_workspace_id = UNSET
    else:
        json_workspace_id = workspace_id
    params["workspace_id"] = json_workspace_id

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
        "url": "/api/v1/users/me/keys",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiKeyPage | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = ApiKeyPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiKeyPage | ErrorEnvelope]:
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
    workspace_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ApiKeyPage | ErrorEnvelope]:
    """List User Keys

    Args:
        workspace_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyPage | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
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
    workspace_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ApiKeyPage | ErrorEnvelope | None:
    """List User Keys

    Args:
        workspace_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyPage | ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ApiKeyPage | ErrorEnvelope]:
    """List User Keys

    Args:
        workspace_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyPage | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ApiKeyPage | ErrorEnvelope | None:
    """List User Keys

    Args:
        workspace_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyPage | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
