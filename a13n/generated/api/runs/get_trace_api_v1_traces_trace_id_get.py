from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_trace_api_v1_traces_trace_id_get_section_type_0 import GetTraceApiV1TracesTraceIdGetSectionType0
from ...models.read_view import ReadView
from ...models.span import Span
from ...models.span_summary import SpanSummary
from ...models.text_read import TextRead
from ...types import UNSET, Response, Unset


def build_request(
    trace_id: str,
    *,
    view: ReadView | Unset = UNSET,
    section: GetTraceApiV1TracesTraceIdGetSectionType0 | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
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

    json_section: str | Unset | None
    if isinstance(section, Unset):
        json_section = UNSET
    elif isinstance(section, GetTraceApiV1TracesTraceIdGetSectionType0):
        json_section = section.value
    else:
        json_section = section
    params["section"] = json_section

    params["offset"] = offset

    params["limit"] = limit

    json_version: str | Unset | None
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    json_query: str | Unset | None
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/traces/{trace_id}".format(
            trace_id=quote(str(trace_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | Span | SpanSummary | TextRead:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Span | SpanSummary | TextRead:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = Span.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = SpanSummary.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = TextRead.from_dict(data)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | Span | SpanSummary | TextRead]:
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
    view: ReadView | Unset = UNSET,
    section: GetTraceApiV1TracesTraceIdGetSectionType0 | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Span | SpanSummary | TextRead]:
    """Get Trace

     The trace's root span.

    Args:
        trace_id (str):
        view (ReadView | Unset):
        section (GetTraceApiV1TracesTraceIdGetSectionType0 | None | Unset):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        query (None | str | Unset): Case-sensitive literal text search.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Span | SpanSummary | TextRead]
    """

    kwargs = build_request(
        trace_id=trace_id,
        view=view,
        section=section,
        offset=offset,
        limit=limit,
        version=version,
        query=query,
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
    view: ReadView | Unset = UNSET,
    section: GetTraceApiV1TracesTraceIdGetSectionType0 | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | Span | SpanSummary | TextRead | None:
    """Get Trace

     The trace's root span.

    Args:
        trace_id (str):
        view (ReadView | Unset):
        section (GetTraceApiV1TracesTraceIdGetSectionType0 | None | Unset):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        query (None | str | Unset): Case-sensitive literal text search.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Span | SpanSummary | TextRead
    """

    return sync_detailed(
        trace_id=trace_id,
        client=client,
        view=view,
        section=section,
        offset=offset,
        limit=limit,
        version=version,
        query=query,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    trace_id: str,
    *,
    client: AuthenticatedClient,
    view: ReadView | Unset = UNSET,
    section: GetTraceApiV1TracesTraceIdGetSectionType0 | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Span | SpanSummary | TextRead]:
    """Get Trace

     The trace's root span.

    Args:
        trace_id (str):
        view (ReadView | Unset):
        section (GetTraceApiV1TracesTraceIdGetSectionType0 | None | Unset):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        query (None | str | Unset): Case-sensitive literal text search.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Span | SpanSummary | TextRead]
    """

    kwargs = build_request(
        trace_id=trace_id,
        view=view,
        section=section,
        offset=offset,
        limit=limit,
        version=version,
        query=query,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trace_id: str,
    *,
    client: AuthenticatedClient,
    view: ReadView | Unset = UNSET,
    section: GetTraceApiV1TracesTraceIdGetSectionType0 | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | Span | SpanSummary | TextRead | None:
    """Get Trace

     The trace's root span.

    Args:
        trace_id (str):
        view (ReadView | Unset):
        section (GetTraceApiV1TracesTraceIdGetSectionType0 | None | Unset):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        query (None | str | Unset): Case-sensitive literal text search.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Span | SpanSummary | TextRead
    """

    return (
        await asyncio_detailed(
            trace_id=trace_id,
            client=client,
            view=view,
            section=section,
            offset=offset,
            limit=limit,
            version=version,
            query=query,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
