from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.execution_observation import ExecutionObservation
from ...types import UNSET, Response, Unset


def build_request(
    thread_id: str,
    execution_id: str,
    *,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/threads/{thread_id}/tool-executions/{execution_id}/observation".format(
            thread_id=quote(str(thread_id), safe=""),
            execution_id=quote(str(execution_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | ExecutionObservation:
    if response.status_code == 200:
        response_200 = ExecutionObservation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ExecutionObservation]:
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
    execution_id: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ExecutionObservation]:
    """Observe Tool Execution

    Args:
        thread_id (str):
        execution_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ExecutionObservation]
    """

    kwargs = build_request(
        thread_id=thread_id,
        execution_id=execution_id,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | ExecutionObservation | None:
    """Observe Tool Execution

    Args:
        thread_id (str):
        execution_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ExecutionObservation
    """

    return sync_detailed(
        thread_id=thread_id,
        execution_id=execution_id,
        client=client,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ExecutionObservation]:
    """Observe Tool Execution

    Args:
        thread_id (str):
        execution_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ExecutionObservation]
    """

    kwargs = build_request(
        thread_id=thread_id,
        execution_id=execution_id,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | ExecutionObservation | None:
    """Observe Tool Execution

    Args:
        thread_id (str):
        execution_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ExecutionObservation
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            execution_id=execution_id,
            client=client,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
