from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.entry_page import EntryPage
from ...models.entry_status import EntryStatus
from ...models.entry_summary_page import EntrySummaryPage
from ...models.error_envelope import ErrorEnvelope
from ...models.list_inbox_api_v1_threads_thread_id_inbox_get_kind_type_0 import (
    ListInboxApiV1ThreadsThreadIdInboxGetKindType0,
)
from ...models.read_view import ReadView
from ...types import UNSET, Response, Unset


def build_request(
    thread_id: str,
    *,
    status: list[EntryStatus] | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    kind: ListInboxApiV1ThreadsThreadIdInboxGetKindType0 | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_status: list[str] | Unset | None
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, list):
        json_status = []
        for status_type_0_item_data in status:
            status_type_0_item = status_type_0_item_data.value
            json_status.append(status_type_0_item)

    else:
        json_status = status
    params["status"] = json_status

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    json_kind: str | Unset | None
    if isinstance(kind, Unset):
        json_kind = UNSET
    elif isinstance(kind, ListInboxApiV1ThreadsThreadIdInboxGetKindType0):
        json_kind = kind.value
    else:
        json_kind = kind
    params["kind"] = json_kind

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
        "url": "/api/v1/threads/{thread_id}/inbox".format(
            thread_id=quote(str(thread_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EntryPage | EntrySummaryPage | ErrorEnvelope:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> EntryPage | EntrySummaryPage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = EntryPage.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = EntrySummaryPage.from_dict(data)

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
) -> Response[EntryPage | EntrySummaryPage | ErrorEnvelope]:
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
    *,
    client: AuthenticatedClient,
    status: list[EntryStatus] | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    kind: ListInboxApiV1ThreadsThreadIdInboxGetKindType0 | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[EntryPage | EntrySummaryPage | ErrorEnvelope]:
    """List Inbox

     In inbox order.

    Args:
        thread_id (str):
        status (list[EntryStatus] | None | Unset):
        view (ReadView | Unset):
        kind (ListInboxApiV1ThreadsThreadIdInboxGetKindType0 | None | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntryPage | EntrySummaryPage | ErrorEnvelope]
    """

    kwargs = build_request(
        thread_id=thread_id,
        status=status,
        view=view,
        kind=kind,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    status: list[EntryStatus] | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    kind: ListInboxApiV1ThreadsThreadIdInboxGetKindType0 | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> EntryPage | EntrySummaryPage | ErrorEnvelope | None:
    """List Inbox

     In inbox order.

    Args:
        thread_id (str):
        status (list[EntryStatus] | None | Unset):
        view (ReadView | Unset):
        kind (ListInboxApiV1ThreadsThreadIdInboxGetKindType0 | None | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntryPage | EntrySummaryPage | ErrorEnvelope
    """

    return sync_detailed(
        thread_id=thread_id,
        client=client,
        status=status,
        view=view,
        kind=kind,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    status: list[EntryStatus] | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    kind: ListInboxApiV1ThreadsThreadIdInboxGetKindType0 | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[EntryPage | EntrySummaryPage | ErrorEnvelope]:
    """List Inbox

     In inbox order.

    Args:
        thread_id (str):
        status (list[EntryStatus] | None | Unset):
        view (ReadView | Unset):
        kind (ListInboxApiV1ThreadsThreadIdInboxGetKindType0 | None | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntryPage | EntrySummaryPage | ErrorEnvelope]
    """

    kwargs = build_request(
        thread_id=thread_id,
        status=status,
        view=view,
        kind=kind,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    status: list[EntryStatus] | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    kind: ListInboxApiV1ThreadsThreadIdInboxGetKindType0 | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> EntryPage | EntrySummaryPage | ErrorEnvelope | None:
    """List Inbox

     In inbox order.

    Args:
        thread_id (str):
        status (list[EntryStatus] | None | Unset):
        view (ReadView | Unset):
        kind (ListInboxApiV1ThreadsThreadIdInboxGetKindType0 | None | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntryPage | EntrySummaryPage | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            client=client,
            status=status,
            view=view,
            kind=kind,
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
