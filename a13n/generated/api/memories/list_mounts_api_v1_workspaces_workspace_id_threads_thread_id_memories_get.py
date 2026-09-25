from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.memory_mount_page import MemoryMountPage
from ...types import Response


def build_request(
    workspace_id: str,
    thread_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workspaces/{workspace_id}/threads/{thread_id}/memories".format(
            workspace_id=quote(str(workspace_id), safe=""),
            thread_id=quote(str(thread_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | MemoryMountPage:
    if response.status_code == 200:
        response_200 = MemoryMountPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | MemoryMountPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    thread_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | MemoryMountPage]:
    """List Mounts

    Args:
        workspace_id (str):
        thread_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | MemoryMountPage]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        thread_id=thread_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    thread_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | MemoryMountPage | None:
    """List Mounts

    Args:
        workspace_id (str):
        thread_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | MemoryMountPage
    """

    return sync_detailed(
        workspace_id=workspace_id,
        thread_id=thread_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    thread_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | MemoryMountPage]:
    """List Mounts

    Args:
        workspace_id (str):
        thread_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | MemoryMountPage]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        thread_id=thread_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    thread_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | MemoryMountPage | None:
    """List Mounts

    Args:
        workspace_id (str):
        thread_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | MemoryMountPage
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            thread_id=thread_id,
            client=client,
        )
    ).parsed
