import datetime
from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.run_status import RunStatus
from ...models.session_page import SessionPage
from ...models.trigger import Trigger
from ...types import UNSET, Response, Unset


def build_request(
    *,
    q: str | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    status: list[RunStatus] | Unset = UNSET,
    trigger: list[Trigger] | Unset = UNSET,
    updated_after: datetime.datetime | Unset | None = UNSET,
    updated_before: datetime.datetime | Unset | None = UNSET,
    label: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_q: str | Unset | None
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_agent_id: str | Unset | None
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    json_trigger: list[str] | Unset = UNSET
    if not isinstance(trigger, Unset):
        json_trigger = []
        for trigger_item_data in trigger:
            trigger_item = trigger_item_data.value
            json_trigger.append(trigger_item)

    params["trigger"] = json_trigger

    json_updated_after: str | Unset | None
    if isinstance(updated_after, Unset):
        json_updated_after = UNSET
    elif isinstance(updated_after, datetime.datetime):
        json_updated_after = updated_after.isoformat()
    else:
        json_updated_after = updated_after
    params["updated_after"] = json_updated_after

    json_updated_before: str | Unset | None
    if isinstance(updated_before, Unset):
        json_updated_before = UNSET
    elif isinstance(updated_before, datetime.datetime):
        json_updated_before = updated_before.isoformat()
    else:
        json_updated_before = updated_before
    params["updated_before"] = json_updated_before

    json_label: list[str] | Unset = UNSET
    if not isinstance(label, Unset):
        json_label = label

    params["label"] = json_label

    params["limit"] = limit

    json_cursor: str | Unset | None
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sessions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | SessionPage:
    if response.status_code == 200:
        response_200 = SessionPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | SessionPage]:
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
    q: str | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    status: list[RunStatus] | Unset = UNSET,
    trigger: list[Trigger] | Unset = UNSET,
    updated_after: datetime.datetime | Unset | None = UNSET,
    updated_before: datetime.datetime | Unset | None = UNSET,
    label: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SessionPage]:
    """List Sessions

    Args:
        q (None | str | Unset): A session or thread ID
        agent_id (None | str | Unset):
        status (list[RunStatus] | Unset):
        trigger (list[Trigger] | Unset):
        updated_after (datetime.datetime | None | Unset):
        updated_before (datetime.datetime | None | Unset):
        label (list[str] | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SessionPage]
    """

    kwargs = build_request(
        q=q,
        agent_id=agent_id,
        status=status,
        trigger=trigger,
        updated_after=updated_after,
        updated_before=updated_before,
        label=label,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: str | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    status: list[RunStatus] | Unset = UNSET,
    trigger: list[Trigger] | Unset = UNSET,
    updated_after: datetime.datetime | Unset | None = UNSET,
    updated_before: datetime.datetime | Unset | None = UNSET,
    label: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SessionPage | None:
    """List Sessions

    Args:
        q (None | str | Unset): A session or thread ID
        agent_id (None | str | Unset):
        status (list[RunStatus] | Unset):
        trigger (list[Trigger] | Unset):
        updated_after (datetime.datetime | None | Unset):
        updated_before (datetime.datetime | None | Unset):
        label (list[str] | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SessionPage
    """

    return sync_detailed(
        client=client,
        q=q,
        agent_id=agent_id,
        status=status,
        trigger=trigger,
        updated_after=updated_after,
        updated_before=updated_before,
        label=label,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    status: list[RunStatus] | Unset = UNSET,
    trigger: list[Trigger] | Unset = UNSET,
    updated_after: datetime.datetime | Unset | None = UNSET,
    updated_before: datetime.datetime | Unset | None = UNSET,
    label: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SessionPage]:
    """List Sessions

    Args:
        q (None | str | Unset): A session or thread ID
        agent_id (None | str | Unset):
        status (list[RunStatus] | Unset):
        trigger (list[Trigger] | Unset):
        updated_after (datetime.datetime | None | Unset):
        updated_before (datetime.datetime | None | Unset):
        label (list[str] | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SessionPage]
    """

    kwargs = build_request(
        q=q,
        agent_id=agent_id,
        status=status,
        trigger=trigger,
        updated_after=updated_after,
        updated_before=updated_before,
        label=label,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    status: list[RunStatus] | Unset = UNSET,
    trigger: list[Trigger] | Unset = UNSET,
    updated_after: datetime.datetime | Unset | None = UNSET,
    updated_before: datetime.datetime | Unset | None = UNSET,
    label: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SessionPage | None:
    """List Sessions

    Args:
        q (None | str | Unset): A session or thread ID
        agent_id (None | str | Unset):
        status (list[RunStatus] | Unset):
        trigger (list[Trigger] | Unset):
        updated_after (datetime.datetime | None | Unset):
        updated_before (datetime.datetime | None | Unset):
        label (list[str] | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SessionPage
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            agent_id=agent_id,
            status=status,
            trigger=trigger,
            updated_after=updated_after,
            updated_before=updated_before,
            label=label,
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
