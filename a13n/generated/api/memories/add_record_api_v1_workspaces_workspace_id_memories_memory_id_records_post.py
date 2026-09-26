from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.memory_record_text import MemoryRecordText
from ...models.memory_record_view import MemoryRecordView
from ...types import Response


def build_request(
    workspace_id: str,
    memory_id: str,
    *,
    body: MemoryRecordText,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/workspaces/{workspace_id}/memories/{memory_id}/records".format(
            workspace_id=quote(str(workspace_id), safe=""),
            memory_id=quote(str(memory_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | MemoryRecordView:
    if response.status_code == 201:
        response_201 = MemoryRecordView.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | MemoryRecordView]:
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
    body: MemoryRecordText,
) -> Response[ErrorEnvelope | MemoryRecordView]:
    """Add Record

    Args:
        workspace_id (str):
        memory_id (str):
        body (MemoryRecordText):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | MemoryRecordView]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        memory_id=memory_id,
        body=body,
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
    body: MemoryRecordText,
) -> ErrorEnvelope | MemoryRecordView | None:
    """Add Record

    Args:
        workspace_id (str):
        memory_id (str):
        body (MemoryRecordText):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | MemoryRecordView
    """

    return sync_detailed(
        workspace_id=workspace_id,
        memory_id=memory_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    memory_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryRecordText,
) -> Response[ErrorEnvelope | MemoryRecordView]:
    """Add Record

    Args:
        workspace_id (str):
        memory_id (str):
        body (MemoryRecordText):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | MemoryRecordView]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        memory_id=memory_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    memory_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryRecordText,
) -> ErrorEnvelope | MemoryRecordView | None:
    """Add Record

    Args:
        workspace_id (str):
        memory_id (str):
        body (MemoryRecordText):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | MemoryRecordView
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            memory_id=memory_id,
            client=client,
            body=body,
        )
    ).parsed
