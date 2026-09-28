import datetime
from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.span_page import SpanPage
from ...types import UNSET, Response, Unset


def build_request(
    *,
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    attribute: list[str] | Unset | None = UNSET,
    started_after: datetime.datetime | Unset | None = UNSET,
    started_before: datetime.datetime | Unset | None = UNSET,
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

    json_attribute: list[str] | Unset | None
    if isinstance(attribute, Unset):
        json_attribute = UNSET
    elif isinstance(attribute, list):
        json_attribute = attribute

    else:
        json_attribute = attribute
    params["attribute"] = json_attribute

    json_started_after: str | Unset | None
    if isinstance(started_after, Unset):
        json_started_after = UNSET
    elif isinstance(started_after, datetime.datetime):
        json_started_after = started_after.isoformat()
    else:
        json_started_after = started_after
    params["started_after"] = json_started_after

    json_started_before: str | Unset | None
    if isinstance(started_before, Unset):
        json_started_before = UNSET
    elif isinstance(started_before, datetime.datetime):
        json_started_before = started_before.isoformat()
    else:
        json_started_before = started_before
    params["started_before"] = json_started_before

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
        "url": "/api/v1/traces",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | SpanPage:
    if response.status_code == 200:
        response_200 = SpanPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | SpanPage]:
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
    attribute: list[str] | Unset | None = UNSET,
    started_after: datetime.datetime | Unset | None = UNSET,
    started_before: datetime.datetime | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SpanPage]:
    """List Traces

     Trace root spans, one per attempt. A cursor keeps the window of the first page.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | None | Unset): key:value, an exact root span attribute
        started_after (datetime.datetime | None | Unset):
        started_before (datetime.datetime | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SpanPage]
    """

    kwargs = build_request(
        session_id=session_id,
        thread_id=thread_id,
        run_id=run_id,
        attribute=attribute,
        started_after=started_after,
        started_before=started_before,
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
    attribute: list[str] | Unset | None = UNSET,
    started_after: datetime.datetime | Unset | None = UNSET,
    started_before: datetime.datetime | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SpanPage | None:
    """List Traces

     Trace root spans, one per attempt. A cursor keeps the window of the first page.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | None | Unset): key:value, an exact root span attribute
        started_after (datetime.datetime | None | Unset):
        started_before (datetime.datetime | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SpanPage
    """

    return sync_detailed(
        client=client,
        session_id=session_id,
        thread_id=thread_id,
        run_id=run_id,
        attribute=attribute,
        started_after=started_after,
        started_before=started_before,
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
    attribute: list[str] | Unset | None = UNSET,
    started_after: datetime.datetime | Unset | None = UNSET,
    started_before: datetime.datetime | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SpanPage]:
    """List Traces

     Trace root spans, one per attempt. A cursor keeps the window of the first page.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | None | Unset): key:value, an exact root span attribute
        started_after (datetime.datetime | None | Unset):
        started_before (datetime.datetime | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SpanPage]
    """

    kwargs = build_request(
        session_id=session_id,
        thread_id=thread_id,
        run_id=run_id,
        attribute=attribute,
        started_after=started_after,
        started_before=started_before,
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
    attribute: list[str] | Unset | None = UNSET,
    started_after: datetime.datetime | Unset | None = UNSET,
    started_before: datetime.datetime | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SpanPage | None:
    """List Traces

     Trace root spans, one per attempt. A cursor keeps the window of the first page.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | None | Unset): key:value, an exact root span attribute
        started_after (datetime.datetime | None | Unset):
        started_before (datetime.datetime | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SpanPage
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
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
