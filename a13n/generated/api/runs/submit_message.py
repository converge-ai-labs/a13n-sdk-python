from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.message import Message
from ...models.submitted import Submitted
from ...types import UNSET, Response, Unset


def build_request(
    thread_id: str,
    *,
    body: Message,
    idempotency_key: str,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/threads/{thread_id}/inbox".format(
            thread_id=quote(str(thread_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | Submitted:
    if response.status_code == 200:
        response_200 = Submitted.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Submitted.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | Submitted]:
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
    thread_id: str,
    *,
    client: AuthenticatedClient,
    body: Message,
    idempotency_key: str,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Submitted]:
    """Submit Message

     Append a message; it starts a run at once when the thread can accept it, or steers the active run.

    Args:
        thread_id (str):
        idempotency_key (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (Message):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Submitted]
    """

    kwargs = build_request(
        thread_id=thread_id,
        body=body,
        idempotency_key=idempotency_key,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    body: Message,
    idempotency_key: str,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | Submitted | None:
    """Submit Message

     Append a message; it starts a run at once when the thread can accept it, or steers the active run.

    Args:
        thread_id (str):
        idempotency_key (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (Message):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Submitted
    """

    return sync_detailed(
        thread_id=thread_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    body: Message,
    idempotency_key: str,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Submitted]:
    """Submit Message

     Append a message; it starts a run at once when the thread can accept it, or steers the active run.

    Args:
        thread_id (str):
        idempotency_key (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (Message):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Submitted]
    """

    kwargs = build_request(
        thread_id=thread_id,
        body=body,
        idempotency_key=idempotency_key,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    body: Message,
    idempotency_key: str,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | Submitted | None:
    """Submit Message

     Append a message; it starts a run at once when the thread can accept it, or steers the active run.

    Args:
        thread_id (str):
        idempotency_key (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (Message):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Submitted
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
