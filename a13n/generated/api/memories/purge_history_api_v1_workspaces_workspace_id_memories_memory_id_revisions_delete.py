from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.history_purge import HistoryPurge
from ...types import UNSET, Response


def build_request(
    workspace_id: str,
    memory_id: str,
    *,
    path: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/workspaces/{workspace_id}/memories/{memory_id}/revisions".format(
            workspace_id=quote(str(workspace_id), safe=""),
            memory_id=quote(str(memory_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | HistoryPurge:
    if response.status_code == 200:
        response_200 = HistoryPurge.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | HistoryPurge]:
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
    path: str,
) -> Response[ErrorEnvelope | HistoryPurge]:
    """Purge History

     Delete every retained revision of one file path.

    Args:
        workspace_id (str):
        memory_id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | HistoryPurge]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        memory_id=memory_id,
        path=path,
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
    path: str,
) -> ErrorEnvelope | HistoryPurge | None:
    """Purge History

     Delete every retained revision of one file path.

    Args:
        workspace_id (str):
        memory_id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | HistoryPurge
    """

    return sync_detailed(
        workspace_id=workspace_id,
        memory_id=memory_id,
        client=client,
        path=path,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    memory_id: str,
    *,
    client: AuthenticatedClient,
    path: str,
) -> Response[ErrorEnvelope | HistoryPurge]:
    """Purge History

     Delete every retained revision of one file path.

    Args:
        workspace_id (str):
        memory_id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | HistoryPurge]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        memory_id=memory_id,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    memory_id: str,
    *,
    client: AuthenticatedClient,
    path: str,
) -> ErrorEnvelope | HistoryPurge | None:
    """Purge History

     Delete every retained revision of one file path.

    Args:
        workspace_id (str):
        memory_id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | HistoryPurge
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            memory_id=memory_id,
            client=client,
            path=path,
        )
    ).parsed
