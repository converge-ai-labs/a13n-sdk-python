from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.realtime_availability import RealtimeAvailability
from ...types import UNSET, Response, Unset


def build_request(
    *,
    agent_id: str,
    agent_revision_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    fork_run_id: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    params["agent_id"] = agent_id

    json_agent_revision_id: str | Unset | None
    if isinstance(agent_revision_id, Unset):
        json_agent_revision_id = UNSET
    else:
        json_agent_revision_id = agent_revision_id
    params["agent_revision_id"] = json_agent_revision_id

    json_thread_id: str | Unset | None
    if isinstance(thread_id, Unset):
        json_thread_id = UNSET
    else:
        json_thread_id = thread_id
    params["thread_id"] = json_thread_id

    json_fork_run_id: str | Unset | None
    if isinstance(fork_run_id, Unset):
        json_fork_run_id = UNSET
    else:
        json_fork_run_id = fork_run_id
    params["fork_run_id"] = json_fork_run_id

    json_model: str | Unset | None
    if isinstance(model, Unset):
        json_model = UNSET
    else:
        json_model = model
    params["model"] = json_model

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/realtime",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | RealtimeAvailability:
    if response.status_code == 200:
        response_200 = RealtimeAvailability.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | RealtimeAvailability]:
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
    client: AuthenticatedClient | Client,
    agent_id: str,
    agent_revision_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    fork_run_id: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | RealtimeAvailability]:
    """Realtime Availability

     Report realtime input for the selected Agent and Thread.

    Args:
        agent_id (str):
        agent_revision_id (None | str | Unset):
        thread_id (None | str | Unset):
        fork_run_id (None | str | Unset):
        model (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | RealtimeAvailability]
    """

    kwargs = build_request(
        agent_id=agent_id,
        agent_revision_id=agent_revision_id,
        thread_id=thread_id,
        fork_run_id=fork_run_id,
        model=model,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str,
    agent_revision_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    fork_run_id: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | RealtimeAvailability | None:
    """Realtime Availability

     Report realtime input for the selected Agent and Thread.

    Args:
        agent_id (str):
        agent_revision_id (None | str | Unset):
        thread_id (None | str | Unset):
        fork_run_id (None | str | Unset):
        model (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | RealtimeAvailability
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        agent_revision_id=agent_revision_id,
        thread_id=thread_id,
        fork_run_id=fork_run_id,
        model=model,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str,
    agent_revision_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    fork_run_id: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | RealtimeAvailability]:
    """Realtime Availability

     Report realtime input for the selected Agent and Thread.

    Args:
        agent_id (str):
        agent_revision_id (None | str | Unset):
        thread_id (None | str | Unset):
        fork_run_id (None | str | Unset):
        model (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | RealtimeAvailability]
    """

    kwargs = build_request(
        agent_id=agent_id,
        agent_revision_id=agent_revision_id,
        thread_id=thread_id,
        fork_run_id=fork_run_id,
        model=model,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str,
    agent_revision_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    fork_run_id: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | RealtimeAvailability | None:
    """Realtime Availability

     Report realtime input for the selected Agent and Thread.

    Args:
        agent_id (str):
        agent_revision_id (None | str | Unset):
        thread_id (None | str | Unset):
        fork_run_id (None | str | Unset):
        model (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | RealtimeAvailability
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            thread_id=thread_id,
            fork_run_id=fork_run_id,
            model=model,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
