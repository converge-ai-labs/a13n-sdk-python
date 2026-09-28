from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.api_key import ApiKey
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    workspace_id: str,
    key_id: str,
    *,
    if_match: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/workspaces/{workspace_id}/keys/{key_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            key_id=quote(str(key_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiKey | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = ApiKey.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiKey | ErrorEnvelope]:
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
    key_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> Response[ApiKey | ErrorEnvelope]:
    """Revoke Workspace Key

    Args:
        workspace_id (str):
        key_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKey | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        key_id=key_id,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> ApiKey | ErrorEnvelope | None:
    """Revoke Workspace Key

    Args:
        workspace_id (str):
        key_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKey | ErrorEnvelope
    """

    return sync_detailed(
        workspace_id=workspace_id,
        key_id=key_id,
        client=client,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> Response[ApiKey | ErrorEnvelope]:
    """Revoke Workspace Key

    Args:
        workspace_id (str):
        key_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKey | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        key_id=key_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> ApiKey | ErrorEnvelope | None:
    """Revoke Workspace Key

    Args:
        workspace_id (str):
        key_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKey | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            key_id=key_id,
            client=client,
            if_match=if_match,
        )
    ).parsed
