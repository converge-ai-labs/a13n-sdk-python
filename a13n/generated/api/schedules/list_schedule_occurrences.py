import datetime
from http import HTTPStatus
from typing import Any, Literal
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.occurrence_page import OccurrencePage
from ...models.occurrence_status import OccurrenceStatus
from ...models.schedule_trigger import ScheduleTrigger
from ...types import UNSET, Response, Unset


def build_request(
    schedule_id: str,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    status: OccurrenceStatus | Unset | None = UNSET,
    trigger: ScheduleTrigger | Unset | None = UNSET,
    created_after: datetime.datetime | Unset | None = UNSET,
    created_before: datetime.datetime | Unset | None = UNSET,
    unfinished: bool | Unset | None = UNSET,
    include: Literal["execution"] | Unset | None = UNSET,
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

    json_status: str | Unset | None
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, OccurrenceStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_trigger: str | Unset | None
    if isinstance(trigger, Unset):
        json_trigger = UNSET
    elif isinstance(trigger, ScheduleTrigger):
        json_trigger = trigger.value
    else:
        json_trigger = trigger
    params["trigger"] = json_trigger

    json_created_after: str | Unset | None
    if isinstance(created_after, Unset):
        json_created_after = UNSET
    elif isinstance(created_after, datetime.datetime):
        json_created_after = created_after.isoformat()
    else:
        json_created_after = created_after
    params["created_after"] = json_created_after

    json_created_before: str | Unset | None
    if isinstance(created_before, Unset):
        json_created_before = UNSET
    elif isinstance(created_before, datetime.datetime):
        json_created_before = created_before.isoformat()
    else:
        json_created_before = created_before
    params["created_before"] = json_created_before

    json_unfinished: bool | Unset | None
    if isinstance(unfinished, Unset):
        json_unfinished = UNSET
    else:
        json_unfinished = unfinished
    params["unfinished"] = json_unfinished

    json_include: Literal["execution"] | Unset | None
    if isinstance(include, Unset):
        json_include = UNSET
    else:
        json_include = include
    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/schedules/{schedule_id}/occurrences".format(
            schedule_id=quote(str(schedule_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | OccurrencePage:
    if response.status_code == 200:
        response_200 = OccurrencePage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | OccurrencePage]:
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
    schedule_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    status: OccurrenceStatus | Unset | None = UNSET,
    trigger: ScheduleTrigger | Unset | None = UNSET,
    created_after: datetime.datetime | Unset | None = UNSET,
    created_before: datetime.datetime | Unset | None = UNSET,
    unfinished: bool | Unset | None = UNSET,
    include: Literal["execution"] | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | OccurrencePage]:
    """List Schedule Occurrences

    Args:
        schedule_id (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        status (None | OccurrenceStatus | Unset):
        trigger (None | ScheduleTrigger | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        unfinished (bool | None | Unset):
        include (Literal['execution'] | None | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | OccurrencePage]
    """

    kwargs = build_request(
        schedule_id=schedule_id,
        limit=limit,
        cursor=cursor,
        status=status,
        trigger=trigger,
        created_after=created_after,
        created_before=created_before,
        unfinished=unfinished,
        include=include,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schedule_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    status: OccurrenceStatus | Unset | None = UNSET,
    trigger: ScheduleTrigger | Unset | None = UNSET,
    created_after: datetime.datetime | Unset | None = UNSET,
    created_before: datetime.datetime | Unset | None = UNSET,
    unfinished: bool | Unset | None = UNSET,
    include: Literal["execution"] | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | OccurrencePage | None:
    """List Schedule Occurrences

    Args:
        schedule_id (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        status (None | OccurrenceStatus | Unset):
        trigger (None | ScheduleTrigger | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        unfinished (bool | None | Unset):
        include (Literal['execution'] | None | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | OccurrencePage
    """

    return sync_detailed(
        schedule_id=schedule_id,
        client=client,
        limit=limit,
        cursor=cursor,
        status=status,
        trigger=trigger,
        created_after=created_after,
        created_before=created_before,
        unfinished=unfinished,
        include=include,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    schedule_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    status: OccurrenceStatus | Unset | None = UNSET,
    trigger: ScheduleTrigger | Unset | None = UNSET,
    created_after: datetime.datetime | Unset | None = UNSET,
    created_before: datetime.datetime | Unset | None = UNSET,
    unfinished: bool | Unset | None = UNSET,
    include: Literal["execution"] | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | OccurrencePage]:
    """List Schedule Occurrences

    Args:
        schedule_id (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        status (None | OccurrenceStatus | Unset):
        trigger (None | ScheduleTrigger | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        unfinished (bool | None | Unset):
        include (Literal['execution'] | None | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | OccurrencePage]
    """

    kwargs = build_request(
        schedule_id=schedule_id,
        limit=limit,
        cursor=cursor,
        status=status,
        trigger=trigger,
        created_after=created_after,
        created_before=created_before,
        unfinished=unfinished,
        include=include,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    status: OccurrenceStatus | Unset | None = UNSET,
    trigger: ScheduleTrigger | Unset | None = UNSET,
    created_after: datetime.datetime | Unset | None = UNSET,
    created_before: datetime.datetime | Unset | None = UNSET,
    unfinished: bool | Unset | None = UNSET,
    include: Literal["execution"] | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | OccurrencePage | None:
    """List Schedule Occurrences

    Args:
        schedule_id (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        status (None | OccurrenceStatus | Unset):
        trigger (None | ScheduleTrigger | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        unfinished (bool | None | Unset):
        include (Literal['execution'] | None | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | OccurrencePage
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            client=client,
            limit=limit,
            cursor=cursor,
            status=status,
            trigger=trigger,
            created_after=created_after,
            created_before=created_before,
            unfinished=unfinished,
            include=include,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
