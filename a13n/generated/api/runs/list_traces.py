import datetime
from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.list_traces_status_type_0 import ListTracesStatusType0
from ...models.read_view import ReadView
from ...models.span_page import SpanPage
from ...models.span_read_page import SpanReadPage
from ...types import UNSET, Response, Unset


def build_request(
    *,
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    attribute: list[str] | Unset | None = UNSET,
    started_after: datetime.datetime | Unset | None = UNSET,
    started_before: datetime.datetime | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    status: ListTracesStatusType0 | Unset | None = UNSET,
    kind: str | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
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

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    json_status: str | Unset | None
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, ListTracesStatusType0):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_kind: str | Unset | None
    if isinstance(kind, Unset):
        json_kind = UNSET
    else:
        json_kind = kind
    params["kind"] = json_kind

    json_tool_name: str | Unset | None
    if isinstance(tool_name, Unset):
        json_tool_name = UNSET
    else:
        json_tool_name = tool_name
    params["tool_name"] = json_tool_name

    json_limit: int | Unset | None
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

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


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | SpanPage | SpanReadPage:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> SpanPage | SpanReadPage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = SpanPage.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = SpanReadPage.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | SpanPage | SpanReadPage]:
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
    view: ReadView | Unset = UNSET,
    status: ListTracesStatusType0 | Unset | None = UNSET,
    kind: str | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SpanPage | SpanReadPage]:
    """List Traces

     Trace root spans, one per attempt. A cursor keeps the window of the first page.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | None | Unset): key:value, an exact root span attribute
        started_after (datetime.datetime | None | Unset):
        started_before (datetime.datetime | None | Unset):
        view (ReadView | Unset):
        status (ListTracesStatusType0 | None | Unset):
        kind (None | str | Unset):
        tool_name (None | str | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SpanPage | SpanReadPage]
    """

    kwargs = build_request(
        session_id=session_id,
        thread_id=thread_id,
        run_id=run_id,
        attribute=attribute,
        started_after=started_after,
        started_before=started_before,
        view=view,
        status=status,
        kind=kind,
        tool_name=tool_name,
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
    view: ReadView | Unset = UNSET,
    status: ListTracesStatusType0 | Unset | None = UNSET,
    kind: str | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SpanPage | SpanReadPage | None:
    """List Traces

     Trace root spans, one per attempt. A cursor keeps the window of the first page.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | None | Unset): key:value, an exact root span attribute
        started_after (datetime.datetime | None | Unset):
        started_before (datetime.datetime | None | Unset):
        view (ReadView | Unset):
        status (ListTracesStatusType0 | None | Unset):
        kind (None | str | Unset):
        tool_name (None | str | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SpanPage | SpanReadPage
    """

    return sync_detailed(
        client=client,
        session_id=session_id,
        thread_id=thread_id,
        run_id=run_id,
        attribute=attribute,
        started_after=started_after,
        started_before=started_before,
        view=view,
        status=status,
        kind=kind,
        tool_name=tool_name,
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
    view: ReadView | Unset = UNSET,
    status: ListTracesStatusType0 | Unset | None = UNSET,
    kind: str | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SpanPage | SpanReadPage]:
    """List Traces

     Trace root spans, one per attempt. A cursor keeps the window of the first page.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | None | Unset): key:value, an exact root span attribute
        started_after (datetime.datetime | None | Unset):
        started_before (datetime.datetime | None | Unset):
        view (ReadView | Unset):
        status (ListTracesStatusType0 | None | Unset):
        kind (None | str | Unset):
        tool_name (None | str | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SpanPage | SpanReadPage]
    """

    kwargs = build_request(
        session_id=session_id,
        thread_id=thread_id,
        run_id=run_id,
        attribute=attribute,
        started_after=started_after,
        started_before=started_before,
        view=view,
        status=status,
        kind=kind,
        tool_name=tool_name,
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
    view: ReadView | Unset = UNSET,
    status: ListTracesStatusType0 | Unset | None = UNSET,
    kind: str | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SpanPage | SpanReadPage | None:
    """List Traces

     Trace root spans, one per attempt. A cursor keeps the window of the first page.

    Args:
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        attribute (list[str] | None | Unset): key:value, an exact root span attribute
        started_after (datetime.datetime | None | Unset):
        started_before (datetime.datetime | None | Unset):
        view (ReadView | Unset):
        status (ListTracesStatusType0 | None | Unset):
        kind (None | str | Unset):
        tool_name (None | str | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SpanPage | SpanReadPage
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
            view=view,
            status=status,
            kind=kind,
            tool_name=tool_name,
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
