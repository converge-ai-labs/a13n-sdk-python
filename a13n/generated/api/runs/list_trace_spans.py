from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.list_trace_spans_status_type_0 import ListTraceSpansStatusType0
from ...models.list_trace_spans_view import ListTraceSpansView
from ...models.span_page import SpanPage
from ...models.span_read_page import SpanReadPage
from ...types import UNSET, Response, Unset


def build_request(
    trace_id: str,
    *,
    view: ListTraceSpansView | Unset = UNSET,
    status: ListTraceSpansStatusType0 | Unset | None = UNSET,
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

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    json_status: str | Unset | None
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, ListTraceSpansStatusType0):
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
        "url": "/api/v1/traces/{trace_id}/spans".format(
            trace_id=quote(str(trace_id), safe=""),
        ),
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
    trace_id: str,
    *,
    client: AuthenticatedClient,
    view: ListTraceSpansView | Unset = UNSET,
    status: ListTraceSpansStatusType0 | Unset | None = UNSET,
    kind: str | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SpanPage | SpanReadPage]:
    """List Trace Spans

     The trace's spans.

    Args:
        trace_id (str):
        view (ListTraceSpansView | Unset): Overview keeps exact timeline and cost fields without
            observation payloads.
        status (ListTraceSpansStatusType0 | None | Unset):
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
        trace_id=trace_id,
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
    trace_id: str,
    *,
    client: AuthenticatedClient,
    view: ListTraceSpansView | Unset = UNSET,
    status: ListTraceSpansStatusType0 | Unset | None = UNSET,
    kind: str | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SpanPage | SpanReadPage | None:
    """List Trace Spans

     The trace's spans.

    Args:
        trace_id (str):
        view (ListTraceSpansView | Unset): Overview keeps exact timeline and cost fields without
            observation payloads.
        status (ListTraceSpansStatusType0 | None | Unset):
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
        trace_id=trace_id,
        client=client,
        view=view,
        status=status,
        kind=kind,
        tool_name=tool_name,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    trace_id: str,
    *,
    client: AuthenticatedClient,
    view: ListTraceSpansView | Unset = UNSET,
    status: ListTraceSpansStatusType0 | Unset | None = UNSET,
    kind: str | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SpanPage | SpanReadPage]:
    """List Trace Spans

     The trace's spans.

    Args:
        trace_id (str):
        view (ListTraceSpansView | Unset): Overview keeps exact timeline and cost fields without
            observation payloads.
        status (ListTraceSpansStatusType0 | None | Unset):
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
        trace_id=trace_id,
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
    trace_id: str,
    *,
    client: AuthenticatedClient,
    view: ListTraceSpansView | Unset = UNSET,
    status: ListTraceSpansStatusType0 | Unset | None = UNSET,
    kind: str | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SpanPage | SpanReadPage | None:
    """List Trace Spans

     The trace's spans.

    Args:
        trace_id (str):
        view (ListTraceSpansView | Unset): Overview keeps exact timeline and cost fields without
            observation payloads.
        status (ListTraceSpansStatusType0 | None | Unset):
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
            trace_id=trace_id,
            client=client,
            view=view,
            status=status,
            kind=kind,
            tool_name=tool_name,
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
