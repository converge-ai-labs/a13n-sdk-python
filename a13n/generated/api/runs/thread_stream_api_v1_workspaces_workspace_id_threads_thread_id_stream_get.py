from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    workspace_id: str,
    thread_id: str,
    *,
    last_event_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(last_event_id, Unset):
        headers["Last-Event-ID"] = last_event_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workspaces/{workspace_id}/threads/{thread_id}/stream".format(
            workspace_id=quote(str(workspace_id), safe=""),
            thread_id=quote(str(thread_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorEnvelope]:
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
    thread_id: str,
    *,
    client: AuthenticatedClient,
    last_event_id: str | Unset | None = UNSET,
) -> Response[Any | ErrorEnvelope]:
    """Thread Stream

     Live output of the thread's runs over SSE: `delta` and `boundary` frames with `changed`, `reset`,
    `gap`.

    Args:
        workspace_id (str):
        thread_id (str):
        last_event_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        thread_id=thread_id,
        last_event_id=last_event_id,
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
    last_event_id: str | Unset | None = UNSET,
) -> Any | ErrorEnvelope | None:
    """Thread Stream

     Live output of the thread's runs over SSE: `delta` and `boundary` frames with `changed`, `reset`,
    `gap`.

    Args:
        workspace_id (str):
        thread_id (str):
        last_event_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return sync_detailed(
        workspace_id=workspace_id,
        thread_id=thread_id,
        client=client,
        last_event_id=last_event_id,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    thread_id: str,
    *,
    client: AuthenticatedClient,
    last_event_id: str | Unset | None = UNSET,
) -> Response[Any | ErrorEnvelope]:
    """Thread Stream

     Live output of the thread's runs over SSE: `delta` and `boundary` frames with `changed`, `reset`,
    `gap`.

    Args:
        workspace_id (str):
        thread_id (str):
        last_event_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        thread_id=thread_id,
        last_event_id=last_event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    thread_id: str,
    *,
    client: AuthenticatedClient,
    last_event_id: str | Unset | None = UNSET,
) -> Any | ErrorEnvelope | None:
    """Thread Stream

     Live output of the thread's runs over SSE: `delta` and `boundary` frames with `changed`, `reset`,
    `gap`.

    Args:
        workspace_id (str):
        thread_id (str):
        last_event_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            thread_id=thread_id,
            client=client,
            last_event_id=last_event_id,
        )
    ).parsed
