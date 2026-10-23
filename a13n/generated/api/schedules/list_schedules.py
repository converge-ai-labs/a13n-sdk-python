from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.schedule_page import SchedulePage
from ...models.schedule_state import ScheduleState
from ...types import UNSET, Response, Unset


def build_request(
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    state: ScheduleState | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    principal_id: str | Unset | None = UNSET,
    label: list[str] | Unset = UNSET,
    q: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: str | Unset | None
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_state: str | Unset | None
    if isinstance(state, Unset):
        json_state = UNSET
    elif isinstance(state, ScheduleState):
        json_state = state.value
    else:
        json_state = state
    params["state"] = json_state

    json_agent_id: str | Unset | None
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    json_principal_id: str | Unset | None
    if isinstance(principal_id, Unset):
        json_principal_id = UNSET
    else:
        json_principal_id = principal_id
    params["principal_id"] = json_principal_id

    json_label: list[str] | Unset = UNSET
    if not isinstance(label, Unset):
        json_label = label

    params["label"] = json_label

    json_q: str | Unset | None
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/schedules",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | SchedulePage:
    if response.status_code == 200:
        response_200 = SchedulePage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | SchedulePage]:
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
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    state: ScheduleState | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    principal_id: str | Unset | None = UNSET,
    label: list[str] | Unset = UNSET,
    q: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SchedulePage]:
    """List Schedules

    Args:
        limit (int | Unset):
        cursor (None | str | Unset):
        state (None | ScheduleState | Unset):
        agent_id (None | str | Unset):
        principal_id (None | str | Unset):
        label (list[str] | Unset):
        q (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SchedulePage]
    """

    kwargs = build_request(
        limit=limit,
        cursor=cursor,
        state=state,
        agent_id=agent_id,
        principal_id=principal_id,
        label=label,
        q=q,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    state: ScheduleState | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    principal_id: str | Unset | None = UNSET,
    label: list[str] | Unset = UNSET,
    q: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SchedulePage | None:
    """List Schedules

    Args:
        limit (int | Unset):
        cursor (None | str | Unset):
        state (None | ScheduleState | Unset):
        agent_id (None | str | Unset):
        principal_id (None | str | Unset):
        label (list[str] | Unset):
        q (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SchedulePage
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        state=state,
        agent_id=agent_id,
        principal_id=principal_id,
        label=label,
        q=q,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    state: ScheduleState | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    principal_id: str | Unset | None = UNSET,
    label: list[str] | Unset = UNSET,
    q: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SchedulePage]:
    """List Schedules

    Args:
        limit (int | Unset):
        cursor (None | str | Unset):
        state (None | ScheduleState | Unset):
        agent_id (None | str | Unset):
        principal_id (None | str | Unset):
        label (list[str] | Unset):
        q (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SchedulePage]
    """

    kwargs = build_request(
        limit=limit,
        cursor=cursor,
        state=state,
        agent_id=agent_id,
        principal_id=principal_id,
        label=label,
        q=q,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    state: ScheduleState | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    principal_id: str | Unset | None = UNSET,
    label: list[str] | Unset = UNSET,
    q: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SchedulePage | None:
    """List Schedules

    Args:
        limit (int | Unset):
        cursor (None | str | Unset):
        state (None | ScheduleState | Unset):
        agent_id (None | str | Unset):
        principal_id (None | str | Unset):
        label (list[str] | Unset):
        q (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SchedulePage
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            state=state,
            agent_id=agent_id,
            principal_id=principal_id,
            label=label,
            q=q,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
