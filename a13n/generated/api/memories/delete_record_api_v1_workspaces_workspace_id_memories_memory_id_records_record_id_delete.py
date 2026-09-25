from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...types import Response


def build_request(
    workspace_id: str,
    memory_id: str,
    record_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/workspaces/{workspace_id}/memories/{memory_id}/records/{record_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            memory_id=quote(str(memory_id), safe=""),
            record_id=quote(str(record_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorEnvelope:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    memory_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ErrorEnvelope]:
    """Delete Record

    Args:
        workspace_id (str):
        memory_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        memory_id=memory_id,
        record_id=record_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    memory_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ErrorEnvelope | None:
    """Delete Record

    Args:
        workspace_id (str):
        memory_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return sync_detailed(
        workspace_id=workspace_id,
        memory_id=memory_id,
        record_id=record_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    memory_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ErrorEnvelope]:
    """Delete Record

    Args:
        workspace_id (str):
        memory_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        memory_id=memory_id,
        record_id=record_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    memory_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ErrorEnvelope | None:
    """Delete Record

    Args:
        workspace_id (str):
        memory_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            memory_id=memory_id,
            record_id=record_id,
            client=client,
        )
    ).parsed
