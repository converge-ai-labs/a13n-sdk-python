import datetime
from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.search_traces_direction import SearchTracesDirection
from ...models.search_traces_order_by import SearchTracesOrderBy
from ...models.trace_search_page import TraceSearchPage
from ...types import UNSET, Response, Unset


def build_request(
    *,
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    attribute: list[str] | Unset = UNSET,
    started_after: datetime.datetime,
    started_before: datetime.datetime,
    order_by: SearchTracesOrderBy | Unset = UNSET,
    direction: SearchTracesDirection | Unset = UNSET,
    min_duration_seconds: float | str | Unset | None = UNSET,
    max_duration_seconds: float | str | Unset | None = UNSET,
    min_cost_usd: float | str | Unset | None = UNSET,
    max_cost_usd: float | str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_session_id: str | Unset | None
    if isinstance(session_id, Unset):
        json_session_id = UNSET
    else:
        json_session_id = session_id
    params["session_id"] = json_session_id

    json_thread_id: str | Unset | None
    if isinstance(thread_id, Unset):
        json_thread_id = UNSET
    else:
        json_thread_id = thread_id
    params["thread_id"] = json_thread_id

    json_run_id: str | Unset | None
    if isinstance(run_id, Unset):
        json_run_id = UNSET
    else:
        json_run_id = run_id
    params["run_id"] = json_run_id

    json_attribute: list[str] | Unset = UNSET
    if not isinstance(attribute, Unset):
        json_attribute = attribute

    params["attribute"] = json_attribute

    json_started_after = started_after.isoformat()
    params["started_after"] = json_started_after

    json_started_before = started_before.isoformat()
    params["started_before"] = json_started_before

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    json_min_duration_seconds: float | str | Unset | None
    if isinstance(min_duration_seconds, Unset):
        json_min_duration_seconds = UNSET
    else:
        json_min_duration_seconds = min_duration_seconds
    params["min_duration_seconds"] = json_min_duration_seconds

    json_max_duration_seconds: float | str | Unset | None
    if isinstance(max_duration_seconds, Unset):
        json_max_duration_seconds = UNSET
    else:
        json_max_duration_seconds = max_duration_seconds
    params["max_duration_seconds"] = json_max_duration_seconds

    json_min_cost_usd: float | str | Unset | None
    if isinstance(min_cost_usd, Unset):
        json_min_cost_usd = UNSET
    else:
        json_min_cost_usd = min_cost_usd
    params["min_cost_usd"] = json_min_cost_usd

    json_max_cost_usd: float | str | Unset | None
    if isinstance(max_cost_usd, Unset):
        json_max_cost_usd = UNSET
    else:
        json_max_cost_usd = max_cost_usd
    params["max_cost_usd"] = json_max_cost_usd

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
        "url": "/api/v1/traces/search",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | TraceSearchPage:
    if response.status_code == 200:
        response_200 = TraceSearchPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | TraceSearchPage]:
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
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    attribute: list[str] | Unset = UNSET,
    started_after: datetime.datetime,
    started_before: datetime.datetime,
    order_by: SearchTracesOrderBy | Unset = UNSET,
    direction: SearchTracesDirection | Unset = UNSET,
    min_duration_seconds: float | str | Unset | None = UNSET,
    max_duration_seconds: float | str | Unset | None = UNSET,
    min_cost_usd: float | str | Unset | None = UNSET,
    max_cost_usd: float | str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | TraceSearchPage]:
    """Search Traces

     Rank and filter the entire root-start window before paging. Costs sum reported span costs, not
    billing.

    Providers execute each query without a result cache; pages may reflect updates between requests.
    Keyset cursors bind the ordering, filters and last sort value with trace/span IDs.
    Incomplete queries fail without a partial rank.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | Unset):
        started_after (datetime.datetime):
        started_before (datetime.datetime):
        order_by (SearchTracesOrderBy | Unset):
        direction (SearchTracesDirection | Unset):
        min_duration_seconds (float | None | str | Unset):
        max_duration_seconds (float | None | str | Unset):
        min_cost_usd (float | None | str | Unset):
        max_cost_usd (float | None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | TraceSearchPage]
    """

    kwargs = build_request(
        session_id=session_id,
        thread_id=thread_id,
        run_id=run_id,
        attribute=attribute,
        started_after=started_after,
        started_before=started_before,
        order_by=order_by,
        direction=direction,
        min_duration_seconds=min_duration_seconds,
        max_duration_seconds=max_duration_seconds,
        min_cost_usd=min_cost_usd,
        max_cost_usd=max_cost_usd,
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
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    attribute: list[str] | Unset = UNSET,
    started_after: datetime.datetime,
    started_before: datetime.datetime,
    order_by: SearchTracesOrderBy | Unset = UNSET,
    direction: SearchTracesDirection | Unset = UNSET,
    min_duration_seconds: float | str | Unset | None = UNSET,
    max_duration_seconds: float | str | Unset | None = UNSET,
    min_cost_usd: float | str | Unset | None = UNSET,
    max_cost_usd: float | str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | TraceSearchPage | None:
    """Search Traces

     Rank and filter the entire root-start window before paging. Costs sum reported span costs, not
    billing.

    Providers execute each query without a result cache; pages may reflect updates between requests.
    Keyset cursors bind the ordering, filters and last sort value with trace/span IDs.
    Incomplete queries fail without a partial rank.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | Unset):
        started_after (datetime.datetime):
        started_before (datetime.datetime):
        order_by (SearchTracesOrderBy | Unset):
        direction (SearchTracesDirection | Unset):
        min_duration_seconds (float | None | str | Unset):
        max_duration_seconds (float | None | str | Unset):
        min_cost_usd (float | None | str | Unset):
        max_cost_usd (float | None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | TraceSearchPage
    """

    return sync_detailed(
        client=client,
        session_id=session_id,
        thread_id=thread_id,
        run_id=run_id,
        attribute=attribute,
        started_after=started_after,
        started_before=started_before,
        order_by=order_by,
        direction=direction,
        min_duration_seconds=min_duration_seconds,
        max_duration_seconds=max_duration_seconds,
        min_cost_usd=min_cost_usd,
        max_cost_usd=max_cost_usd,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    attribute: list[str] | Unset = UNSET,
    started_after: datetime.datetime,
    started_before: datetime.datetime,
    order_by: SearchTracesOrderBy | Unset = UNSET,
    direction: SearchTracesDirection | Unset = UNSET,
    min_duration_seconds: float | str | Unset | None = UNSET,
    max_duration_seconds: float | str | Unset | None = UNSET,
    min_cost_usd: float | str | Unset | None = UNSET,
    max_cost_usd: float | str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | TraceSearchPage]:
    """Search Traces

     Rank and filter the entire root-start window before paging. Costs sum reported span costs, not
    billing.

    Providers execute each query without a result cache; pages may reflect updates between requests.
    Keyset cursors bind the ordering, filters and last sort value with trace/span IDs.
    Incomplete queries fail without a partial rank.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | Unset):
        started_after (datetime.datetime):
        started_before (datetime.datetime):
        order_by (SearchTracesOrderBy | Unset):
        direction (SearchTracesDirection | Unset):
        min_duration_seconds (float | None | str | Unset):
        max_duration_seconds (float | None | str | Unset):
        min_cost_usd (float | None | str | Unset):
        max_cost_usd (float | None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | TraceSearchPage]
    """

    kwargs = build_request(
        session_id=session_id,
        thread_id=thread_id,
        run_id=run_id,
        attribute=attribute,
        started_after=started_after,
        started_before=started_before,
        order_by=order_by,
        direction=direction,
        min_duration_seconds=min_duration_seconds,
        max_duration_seconds=max_duration_seconds,
        min_cost_usd=min_cost_usd,
        max_cost_usd=max_cost_usd,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    attribute: list[str] | Unset = UNSET,
    started_after: datetime.datetime,
    started_before: datetime.datetime,
    order_by: SearchTracesOrderBy | Unset = UNSET,
    direction: SearchTracesDirection | Unset = UNSET,
    min_duration_seconds: float | str | Unset | None = UNSET,
    max_duration_seconds: float | str | Unset | None = UNSET,
    min_cost_usd: float | str | Unset | None = UNSET,
    max_cost_usd: float | str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | TraceSearchPage | None:
    """Search Traces

     Rank and filter the entire root-start window before paging. Costs sum reported span costs, not
    billing.

    Providers execute each query without a result cache; pages may reflect updates between requests.
    Keyset cursors bind the ordering, filters and last sort value with trace/span IDs.
    Incomplete queries fail without a partial rank.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | Unset):
        started_after (datetime.datetime):
        started_before (datetime.datetime):
        order_by (SearchTracesOrderBy | Unset):
        direction (SearchTracesDirection | Unset):
        min_duration_seconds (float | None | str | Unset):
        max_duration_seconds (float | None | str | Unset):
        min_cost_usd (float | None | str | Unset):
        max_cost_usd (float | None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | TraceSearchPage
    """

    return (
        await asyncio_detailed(
            client=client,
            session_id=session_id,
            thread_id=thread_id,
            run_id=run_id,
            attribute=attribute,
            started_after=started_after,
            started_before=started_before,
            order_by=order_by,
            direction=direction,
            min_duration_seconds=min_duration_seconds,
            max_duration_seconds=max_duration_seconds,
            min_cost_usd=min_cost_usd,
            max_cost_usd=max_cost_usd,
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
